# How GPT, Claude, and Gemini are actually trained and served – Reiner Pope

[00:00:00] Today, I'm interviewing Reiner Pope, who is the CEO of MatX,  
[00:00:03] which is a new chip startup.  
[00:00:04] Previously, he was doing TPU architecture and many other things at Google.  
[00:00:09] This is a very different format from my usual interviews.  
[00:00:10] This is going to be a blackboard lecture.  
[00:00:12] We're going to get up in a second.  
[00:00:13] We in fact built this whole new studio with specifically this  
[00:00:16] format in mind, so it's a pleasure to get to inaugurate it with you.  
[00:00:21] We're going to be talking about model architecture, ML  
[00:00:23] infra, and many other things.  
[00:00:25] The reason I think it's an important topic is because once you understand how  
[00:00:29] training and inference work in a cluster, a lot of things—about why AI is the way  
[00:00:35] it is, why AI architectures are the way they are, why API prices are the way they  
[00:00:40] are, and fundamentally why AI progress is the way it is—start making sense.  
[00:00:45] You need to understand the details to get there, and you need a  
[00:00:47] blackboard to understand the details.  
[00:00:48] Reiner, thank you so much for doing this.  
[00:00:50] Very happy to be here.  
[00:00:52] Full disclosure, I am an angel investor in MatX, but that's  
[00:00:56] unrelated to this podcast.  
[00:00:56] Reiner, to kick us off I'll ask this question.  
[00:01:01] We have a couple of companies like Claude and Codex and Cursor  
[00:01:05] offering something like Fast Mode, where for 6x the price, they'll  
[00:01:09] stream you tokens at 2.5x the speed.  
[00:01:12] Mechanically, I'm curious what's going on here.  
[00:01:14] Why is it the case that you can pay more to get faster latency?  
[00:01:18] Two, could you keep going?  
[00:01:19] Could you pay 100x more and somehow get much faster speeds?  
[00:01:25] Three, could you go the other way?  
[00:01:27] Could you have something like Claude Code "Slow Mode", where if you are  
[00:01:31] willing to wait for minutes on end, you could get even cheaper prices?  
[00:01:36] Maybe this will help motivate the analysis that you'll be doing through the lecture.  
[00:01:39] Great.  
[00:01:40] To jump to the conclusion a little bit, the big effect is batch size.  
[00:01:44] What we're going to do now is quantify exactly what that looks like and what  
[00:01:47] its implications are on latency and cost.  
[00:01:50] There's another effect, which you can call speculative decoding  
[00:01:53] or multi-token prediction.  
[00:01:55] We can maybe come back to that later, but the first thing that  
[00:01:58] we'll talk through is batch size.  
[00:02:00] What I'd like to introduce is the two principles of analysis.  
[00:02:04] First, we're going to look at a roofline analysis of how we run a  
[00:02:07] transformer model on a cluster of chips.  
[00:02:10] We'll take a  
[00:02:13] Blackwell NVL72 cluster, so a rack of 72 GPUs.  
[00:02:19] The roofline analysis means we look at memory bandwidth and compute performance.  
[00:02:25] The other side of that is that we're going to look at just two simple  
[00:02:27] factors of the model: the time to operate on the weights, and the time to  
[00:02:32] operate on the context, the KV cache.  
[00:02:36] Let's jump in.  
[00:02:37] We're going to try and estimate the time that it takes to run  
[00:02:42] an inference of a certain shape.  
[00:02:45] We're not perfect here.  
[00:02:46] We can't exactly predict the time, so instead we're going to approximate.  
[00:02:50] We're going to say that the time must be greater than or  
[00:02:52] equal to a certain quantity.  
[00:02:55] We're going to consider two different aspects: the time it takes to  
[00:03:01] do the memory fetches, and the time it takes to do the compute.  
[00:03:07] It will turn out that this gives us very strong predictive  
[00:03:09] power, even with a simple model.  
[00:03:12] One by one, what is the time that it takes to do the compute?  
[00:03:19] There are really two things I need to do in the compute.  
[00:03:21] I need to multiply by all of the active parameters, and then I need  
[00:03:25] to do some work on the attention.  
[00:03:28] Multiplying by all the active parameters, I have a certain batch size that  
[00:03:30] I'm running, and I've got a number of active parameters in my model.  
[00:03:38] Then I'm just going to divide this by the compute throughput,  
[00:03:41] which is the FLOPs of the chip.  
[00:03:45] This is a hardware concern.  
[00:03:48] This accounts for all of the compute time for all of the weight matrix multiplies.  
[00:03:54] There's a little caveat here.  
[00:03:56] We've ignored the time to do any of the attention computation, but that in general  
[00:04:00] will be quite small in comparison to this.  
[00:04:02] So we'll ignore this.  
[00:04:03] I'll just interrupt from time to time to ask some very naive questions  
[00:04:05] or to clarify some basic points.  
[00:04:09] For the audience, you're not serving one user at a time.  
[00:04:11] The batch refers to the fact that you're serving many different users at the  
[00:04:14] same time, and that's a whole batch.  
[00:04:17] I can motivate the batch at least a little bit.  
[00:04:20] We will see exactly why batch is such a favorable optimization.  
[00:04:23] What will turn out to be the case is that if you do not batch together many  
[00:04:28] users, the cost and the economics you get can be a thousand times worse than  
[00:04:34] if you do batch many users together.  
[00:04:36] We'll be able to see that quite explicitly.  
[00:04:38] Then, number of active parameters.  
[00:04:40] If I look at, for example, a DeepSeek model, the DeepSeek V3 model has  
[00:04:44] about 37 billion active parameters, and 700 billion total parameters.  
[00:04:52] We're focusing on just the ones that are active for a single AI token.  
[00:04:56] We're modeling compute performance.  
[00:04:58] I'm going to keep writing equals, but in all of these cases, you can think of this  
[00:05:00] time as being at least this much, and maybe there will be some terms we ignored.  
[00:05:05] On the memory side, what do we need to do with memory?  
[00:05:09] We need to fetch all of the weights, so there is some time to fetch  
[00:05:16] the total number of parameters, not just the active parameters.  
[00:05:21] There's weight fetch time, and then in addition, there's a KV cache fetch time.  
[00:05:27] This actually depends on batch size.  
[00:05:30] For every element of the batch, we have to fetch an entire context  
[00:05:36] length worth of tokens, and there's a size per token, bytes  
[00:05:44] for one token.  
[00:05:46] This is a model parameter.  
[00:05:47] Maybe just backing up, let's explain what the KV cache is real quick.  
[00:05:52] When I do a forward pass… Let me draw how the autoregressive inference works.  
[00:05:58] This is during decode.  
[00:06:01] If I have a bunch of text tokens… I'm drawing a tensor because ultimately  
[00:06:06] the tokens are represented as  
[00:06:09] a tensor in some embedding dimension.  
[00:06:12] In this direction, I have the sequence length.  
[00:06:18] The work of running a decode is that I have to run each token through  
[00:06:22] a whole bunch of matrix multiplies over a bunch of different layers.  
[00:06:29] In general, I'm going to have to do that work over all of these tokens.  
[00:06:35] But one step of decode is to produce just this one additional token up here.  
[00:06:42] What I'm going to do there is run a full forward pass of multiplying by all of  
[00:06:47] the weight matrices in the entire model.  
[00:06:50] But then I've got this attention mechanism where this token is looking  
[00:06:55] at all of the past tokens, and what is it looking at specifically?  
[00:07:01] It is looking at some internal representation that the model  
[00:07:03] has produced of the tokens, and we call that the KV cache.  
[00:07:08] This process of this single token attending to all of the  
[00:07:11] history of tokens is attention.  
[00:07:13] It is mostly dominated by memory fetches rather than matrix multiplies.  
[00:07:19] So we've got the amount of memory that we're fetching shown over here,  
[00:07:23] and then this is of course just divided by the memory bandwidth,  
[00:07:27] so the memory bytes per second.  
[00:07:35] In fact, these equations here are enough for us to now draw some fit lines.  
[00:07:41] The things that we'd like to look at are sensitivity to batch, and then also,  
[00:07:46] which we'll draw separately, to context  
[00:07:51] length.  
[00:07:52] We said that the big effect you can get is some trade-off in  
[00:07:55] latency versus cost in batch size.  
[00:07:58] Let's draw them out.  
[00:08:00] I think there are just really two graphs that we want to draw.  
[00:08:02] We'll first draw batch size versus time here.  
[00:08:11] When we look at the shape of this, we've got a maximum of  
[00:08:15] the sum and then another term.  
[00:08:19] Let's look at these terms one by one and how they scale: the time for compute  
[00:08:24] and memory, and how they show up.  
[00:08:27] Let's first look at this compute time.  
[00:08:31] This is just purely linear in batch size with no offset, so  
[00:08:35] it is some curve like this.  
[00:08:37] This is t compute.  
[00:08:44] On the memory side, we've got some portion here that is just this constant  
[00:08:51] in some base offset here, which is the weight fetch.  
[00:09:00] Finally, we have this term here, which is the KV fetch, which is pretty  
[00:09:14] linear in batch size, and so it looks like that.  
[00:09:17] The sum of this plus this maxed with this… Let's at least first draw the sum.  
[00:09:29] The two memory times in conjunction end up looking on this curved slope like this.  
[00:09:35] Then the overall maximum is—I'll draw a little thicker here—the  
[00:09:41] maximum of these two curves.  
[00:09:44] What does this mean?  
[00:09:47] This is a latency plot.  
[00:09:54] If I grow my batch size, initially I get some not very strong dependence  
[00:09:59] on batch size, so there is some lower bound on latency here.  
[00:10:11] This already partially answers the question.  
[00:10:13] For a given hardware configuration—and we can talk about varying the hardware  
[00:10:18] configuration—there is a lower bound on latency.  
[00:10:20] It is simply that I need to read all of my total parameters  
[00:10:27] from memory into the chips, and that takes a certain amount of time.  
[00:10:31] If I use all of my memory bandwidth, I can't do any better than that.  
[00:10:34] It seems like the way you've drawn the slopes for compute time and how  
[00:10:40] the KV grows—and what implication the KV has on memory time—  
[00:10:42] What if  
[00:10:48] this were above or below?  
[00:10:49] Yeah, is that necessarily the case?  
[00:10:52] If this is always true, then as batch size grows compute always  
[00:10:56] dominates KV, which suggests that if you have a big enough batch size,  
[00:11:00] maybe memory is never an issue.  
[00:11:02] This is really sensitive to the context length, so I think we  
[00:11:05] should come back and explore this.  
[00:11:08] As you vary the context length, the KV fetch time will go up and up, and  
[00:11:11] that will cause a transition from compute-limited to memory-limited.  
[00:11:15] Is there something especially significant about the slope being  
[00:11:19] exactly the slope of the compute time?  
[00:11:25] Whenever we have balance points, it says that you're getting it exactly right.  
[00:11:29] For the particular context length where the slopes match, that says I am  
[00:11:34] equally memory-bound and compute-bound, which is a really desirable place to  
[00:11:39] be.  
[00:11:40] This is a very simple algebra problem, but suppose the optimal is 100K context  
[00:11:48] length, and you go to 200K context length.  
[00:11:52] Does your MFU go down to 50%?  
[00:11:54] Does it have a humongous impact on MFU to be slightly outside of the optimal  
[00:11:58] context length range, the Goldilocks zone?  
[00:12:01] That's right.  
[00:12:02] That is true as modeled here.  
[00:12:04] There is a key point here that  
[00:12:08] I'm modeling the memory fetch as linear in context length.  
[00:12:11] That depends on model architecture.  
[00:12:13] It is true for all of the model architectures with dense attention.  
[00:12:20] Sparse attention actually scales much better than that.  
[00:12:22] Got it.  
[00:12:23] Is sparse attention what everybody uses in practice?  
[00:12:25] I'm pretty excited about sparse attention.  
[00:12:27] It's hard to know what the labs are using.  
[00:12:29] DeepSeek has published a sparse attention mechanism.  
[00:12:31] I'll just put a plug in that some of the DeepSeek papers that have  
[00:12:36] published sparse attention end up putting a square root in this term.  
[00:12:40] So far, we've looked at the latency.  
[00:12:42] It's hard to read off cost from this.  
[00:12:45] If I think about what cost means…  
[00:12:49] To run this inference, I'm going to use the GPU for a certain number of seconds,  
[00:12:52] like one millisecond or 20 milliseconds.  
[00:12:56] I have to pay the rental time for that time.  
[00:12:59] So it's $2/hour per GPU or something like that.  
[00:13:05] That's the cost of this inference, but how many tokens have I  
[00:13:08] processed during that inference?  
[00:13:10] That is the batch size.  
[00:13:12] What we actually want to plot is the cost versus batch size, which  
[00:13:18] is t over B versus batch size.  
[00:13:23] This is the cost per token.  
[00:13:30] We have to imagine dividing each of these three curves by B, so  
[00:13:34] multiplying by this reciprocal.  
[00:13:38] What we end up with there is… The compute curve  
[00:13:44] was linear.  
[00:13:44] We divide by B, and that makes it a constant here.  
[00:13:48] This is t compute.  
[00:13:52] The KV fetch was linear, and now it becomes a constant as well.  
[00:14:00] Then the weight fetch  
[00:14:10] was constant, and now we've divided by B, so it becomes this  
[00:14:22] parabola.  
[00:14:22] Again, we're going to compute the max of the sum.  
[00:14:28] The sum of these two terms shifts the parabola up.  
[00:14:33] The sum of the KV fetch and the weight fetch gives us  
[00:14:39] a higher parabola that's like this.  
[00:14:41] Then we're going to take the max with the compute  
[00:14:45] here.  
[00:14:45] We end up with this being the overall shape that we care about.  
[00:14:52] Again, we see some limiting behavior.  
[00:14:54] The cost initially starts very high at a batch size of one.  
[00:14:59] It almost goes to infinity because we've got so many weight fetches that are  
[00:15:04] not amortized over a large batch size.  
[00:15:07] But as we increase the batch size, the weight fetches become amortized over so  
[00:15:11] many different batch elements that their cost grows very small, and eventually the  
[00:15:15] compute time ends up driving the cost.  
[00:15:18] So there is a limiting  
[00:15:23] lower bound on cost,  
[00:15:29] which is this line here.  
[00:15:31] So Claude Code Slow or Codex Slow or whatever would just live on this line.  
[00:15:35] It wouldn't help much because you're not able to amortize the KV  
[00:15:40] values over a much bigger batch.  
[00:15:44] They're unique per batch.  
[00:15:45] The compute is also unique per batch.  
[00:15:46] So what is the minimum work you can do per batch after  
[00:15:49] amortizing everything else away?  
[00:15:52] This point where you are no longer memory bandwidth bound, practically  
[00:16:00] how big a batch do you need?  
[00:16:04] How big are the batches practically for frontier models?  
[00:16:07] You can just solve for that.  
[00:16:09] It's not even particularly sensitive to model architecture.  
[00:16:13] Let's go ahead and do that.  
[00:16:15] What we're talking about is when the memory time is equal to the compute time.  
[00:16:19] That’s what that question is.  
[00:16:26] Because we're focused on what the batch size is—and really there's a question  
[00:16:30] of when the weights are amortized over the multiplies—I'm going to  
[00:16:34] focus on comparing the weight fetch time to the weight multiply time.  
[00:16:38] I'm going to disregard the KV fetch term just to simplify the analysis  
[00:16:43] so we can get a clean answer out.  
[00:16:46] We're going to equate  
[00:16:50] this portion with these two times.  
[00:16:58] Writing that out, we get N, number of total parameters,  
[00:17:04] over memory bandwidth,  
[00:17:09] is equal to  
[00:17:12] batch size times number of active parameters  
[00:17:17] divided by the compute performance.  
[00:17:22] Looking over here, everything on the top are model parameters.  
[00:17:26] Everything on the bottom are hardware parameters.  
[00:17:28] It turns out to be nice to rearrange them such that we have  
[00:17:31] the hardware parameters on one side.  
[00:17:33] This is equivalent to  
[00:17:40] FLOPs over memory bandwidth  
[00:17:44] being equal to batch size times number of active parameters,  
[00:17:52] divided by the number of total parameters.  
[00:17:56] This hardware  
[00:17:59] parameter ends up being a dimensionless constant.  
[00:18:01] If you look in terms of FLOPs… What are the dimensions of this?  
[00:18:04] This is multiplies per second.  
[00:18:06] This is bytes per second.  
[00:18:07] So that's not quite dimensionless.  
[00:18:09] But what you do is you say, how many FP4 multiplies per second times  
[00:18:20] the fact that each FP4 is half a byte.  
[00:18:24] I can actually make this end up being dimensionless.  
[00:18:25] On most GPUs, this ends up being  
[00:18:32] somewhere around 300.  
[00:18:37] Has that ratio changed over time as we've gone from model  
[00:18:39] generation to model generation, where the FLOPs keep increasing?  
[00:18:41] This is a hardware parameter.  
[00:18:43] To what extent has the hardware changed?  
[00:18:46] From A100 to H100 to B100, the FLOPs have increased substantially,  
[00:18:51] the memory bandwidth has also increased substantially, and it  
[00:18:53] has remained reasonably stable.  
[00:18:56] We can express this one as well.  
[00:18:57] This is a sparsity parameter.  
[00:19:00] I might even phrase this slightly differently.  
[00:19:01] Let's solve for batch size in total.  
[00:19:05] Moving this back over to the other side, we end up with batch size needs  
[00:19:09] to be bigger than approximately 300  
[00:19:13] times sparsity.  
[00:19:16] For example, in DeepSeek I activate 32  
[00:19:21] out of 256 experts, so this would be 8 for DeepSeek.  
[00:19:27] This actually gives you a ballpark which is remarkably accurate to practice.  
[00:19:31] Generally, people will go a little bit larger than this.  
[00:19:33] They don't really want to be exactly at the balance point because  
[00:19:37] real-world efficiencies aren't as good as a roofline analysis would say.  
[00:19:41] But take this and maybe double or triple it.  
[00:19:44] Okay, so it's two to three thousand tokens per batch.  
[00:19:49] But then if you included the KV cache, the implication would be  
[00:19:55] that the optimal batch size...  
[00:19:57] Should grow larger.  
[00:20:00] We solved for the equivalence between when compute time is equal to memory time.  
[00:20:06] If I add in something that consumes more memory bandwidth, then I have  
[00:20:10] less available for the weight loads.  
[00:20:13] I need to grow the memory bandwidth more, and therefore the batch size more.  
[00:20:17] This seems incredibly small.  
[00:20:19] This would be less than one sequence, right?  
[00:20:24] Keep in mind that I'm talking about the number of tokens that  
[00:20:27] I'm generating one more token for.  
[00:20:30] It's actually 2,000 unique sequences.  
[00:20:33] Got it.  
[00:20:33] We're just talking about a single forward pass on these sequences.  
[00:20:39] You think of the batch as the number of sequences.  
[00:20:41] That’s right.  
[00:20:43] When I'm prepping for interviews, I often talk to experts in the field.  
[00:20:45] So for Reiner, I chatted with two of Jane Street's engineers, Clark and Axel.  
[00:20:50] Clark, who works on low latency trading systems, walked me through why Jane  
[00:20:53] Street uses FPGAs to make sure that they have predictable nanosecond latencies.  
[00:20:57] “You can just build these like giant grids of compute very easily that do  
[00:21:01] exactly what you need that touch a hundred megabytes of SRAM and then  
[00:21:04] get your response back in tens of nanoseconds very easily. And that's  
[00:21:08] basically impossible on a CPU.”  
[00:21:09] He then went on to explain why CPUs just wouldn't work for this kind of thing.  
[00:21:13] “And so if you have a clock that's going every three nanoseconds, you actually  
[00:21:16] have several bytes of information at a time to make your decision.  
[00:21:21] That's as opposed to a CPU where you'll just collect up a whole packet, you  
[00:21:24] know, let's say a 1500-byte packet, and then you say, okay, this packet's ready.  
[00:21:26] Here you go, CPU.  
[00:21:27] You can start thinking about it now.”  
[00:21:29] FPGAs allow you to react to the earliest part of the packet as it arrives, rather  
[00:21:33] than having to wait for the full thing.  
[00:21:34] We also talked about liquid cooling, network design, and many other things.  
[00:21:37] If you're interested in this stuff, Jane Street is hiring.  
[00:21:40] You can check out their open roles at JaneStreet.com/Dwarkesh.  
[00:21:46] And if you want to watch the full prep conversation, we posted it there too.  
[00:21:49] If you've got a frontier model and you are actually doing inference, surely they must  
[00:21:56] have more than 2,000 concurrent users.  
[00:21:58] Is there any added latency from the fact that you need to  
[00:22:01] have the whole batch fill up?  
[00:22:02] Or if you have a reasonable amount of users, is it so unlikely that  
[00:22:08] it would take you 100 milliseconds to fill up the next 2,000 slots?  
[00:22:13] The way to think about this is: when does the train depart, as a model?  
[00:22:18] Let's say I've picked a batch size that I'm going to run at.  
[00:22:25] By the way, this intersection point is the same intersection point here.  
[00:22:30] I pick this batch size, and I know that it's going to take, for  
[00:22:32] example, 20 milliseconds, which is a common place this ends up landing.  
[00:22:36] This is a timeline of what  
[00:22:42] is running on the GPU.  
[00:22:43] It's going to start a new batch every 20 milliseconds regardless.  
[00:22:56] You can think of this as a schedule for the train.  
[00:22:58] A new train departs every 20 milliseconds.  
[00:23:00] Any passengers who are ready board the train.  
[00:23:02] If the train is full, they wait until the next train.  
[00:23:05] If the train is not full, the train is going to go anyway.  
[00:23:07] In terms of what that means for queuing latency, the worst case is that a request  
[00:23:15] arrives just after the train departed.  
[00:23:17] It has to wait for the next train, so that's up to 20 milliseconds, and then it  
[00:23:21] has to wait for that train to complete.  
[00:23:25] So the worst-case latency is 40 milliseconds.  
[00:23:27] How is the 20 milliseconds derived?  
[00:23:28] It's a rule of thumb, but where it comes from is not fully explained yet.  
[00:23:36] So far we've focused on memory bandwidth and compute time.  
[00:23:40] When we look at memory, the other consideration is that we want to use  
[00:23:43] all of the memory capacity we have.  
[00:23:47] Generally, we're going to use all of that memory capacity to  
[00:23:50] store the weights or the KVs.  
[00:23:55] In the time of doing a forward pass, we want to read all of the  
[00:23:58] memory capacity into the chip.  
[00:24:01] That is capacity divided by bandwidth.  
[00:24:03] That tends to be 20 milliseconds on many different generations of HBM.  
[00:24:07] The units make sense.  
[00:24:08] You would have  
[00:24:11] a byte divided by bytes per second.  
[00:24:13] For example, on the Rubin generation, it is something like 288 gigabytes  
[00:24:18] divided by 20 terabytes per second.  
[00:24:22] This  
[00:24:28] comes out to about 15  
[00:24:32] milliseconds.  
[00:24:33] Let me make sure I understand what this is saying.  
[00:24:36] I understand the unit analysis.  
[00:24:38] What it's saying is  
[00:24:43] we can evacuate and replace the HBM in this amount of time.  
[00:24:50] So we don't want to be in a situation where the HBM is not big enough that we're  
[00:24:56] not actually able to write everything we want to it or take everything out of it.  
[00:25:02] Or we don't want to be in a situation where our ability to write back  
[00:25:05] and forth is so small compared...  
[00:25:08] There are sort of two scenarios.  
[00:25:09] Why don't we pick a latency that is bigger than 15 milliseconds?  
[00:25:14] If I think about what that means, it means I actually have  
[00:25:16] time to read the HBM twice.  
[00:25:19] By the way, most HBM accesses are reads, not writes.  
[00:25:21] It's almost all reads because the weight matrices are read-only, and  
[00:25:25] almost all of the KV cache accesses  
[00:25:30] are reads.  
[00:25:30] In around 30 milliseconds, I can read all of HBM twice,  
[00:25:32] but what's the point of that?  
[00:25:35] I don't want to read the weight matrices twice.  
[00:25:37] I don't want to read the KVs twice.  
[00:25:38] Makes a ton of sense.  
[00:25:40] A couple of quick questions.  
[00:25:43] If it is the case that the optimal batch size is something like 2,000,  
[00:25:49] it's totally dependent on the sparsity, not dependent on  
[00:25:51] the model size or anything.  
[00:25:52] Sparsity shows up in model size, but beyond that, it only depends  
[00:25:55] on sparsity, not on scale.  
[00:25:57] That's a very interesting result.  
[00:26:02] One question is how much of a push towards centralization is it that  
[00:26:07] you would have these economies of scale from inference for batching?  
[00:26:10] But it seems like it's not that big a deal.  
[00:26:13] Is 2,000 users at the same time a lot?  
[00:26:14] It doesn't seem like a lot.  
[00:26:15] We can do a bit of analysis on this.  
[00:26:18] You can think of it in terms of number of users, but a more productive way to think  
[00:26:21] of it is in terms of tokens per second.  
[00:26:25] What does this batch size mean in terms of tokens  
[00:26:30] per second of the system?  
[00:26:32] Tokens per second is going to be equal to the batch size.  
[00:26:34] We run a batch of tokens, and we do that  
[00:26:40] every time interval, which is  
[00:26:44] equal to the 15-millisecond or 20-millisecond number.  
[00:26:48] This ends up being batch size times about 60, so 64  
[00:26:56] x B.  
[00:26:58] This ends up being around 2,000 x 64, so 128,000 tokens per second.  
[00:27:09] This is in more digestible units.  
[00:27:11] It's hard to reason about concurrent users, but what is  
[00:27:14] the global traffic for a system?  
[00:27:20] When you look at some of the announcements, sometimes the  
[00:27:23] API providers will brag about how much traffic they have.  
[00:27:28] The numbers I remember from some announcements of Gemini last year  
[00:27:31] were in the hundreds of millions of tokens per second worldwide.  
[00:27:34] This  
[00:27:37] is one-thousandth of that.  
[00:27:40] Gemini is big.  
[00:27:42] One-thousandth of Gemini is a lot.  
[00:27:44] To actually be competitive at scale, you need to be able to serve at  
[00:27:49] least one-thousandth of Gemini.  
[00:27:50] That's interesting.  
[00:27:57] The more sparsity you have, the less compute you need.  
[00:28:04] It does seem that as batch sizes get bigger, compute ends up being the  
[00:28:09] bottleneck, according to this analysis.  
[00:28:11] Then the question is, how far can you take sparsity?  
[00:28:14] As the sparsity ratio increases, as you have fewer active parameters relative  
[00:28:19] to total parameters, how much is the performance of the model degrading?  
[00:28:23] Is it degrading faster than you're saving compute by increasing the sparsity factor?  
[00:28:31] You mean the quality of the model, rather than the speed of the model.  
[00:28:36] Unfortunately, we're not able to answer that analytically.  
[00:28:40] That is an empirical question of model quality.  
[00:28:43] The best I can do is pull up a paper and answer that empirically.  
[00:28:46] Should  
[00:28:50] we pull up the paper now?  
[00:28:50] This paper is "Unified Scaling Laws for Routed Language Models."  
[00:28:53] It's a somewhat old paper by this stage, but one of the things they looked  
[00:28:57] at is if I keep increasing sparsity, what is the model quality impact?  
[00:29:01] This answer is very sensitive to the actual choice of mixture of experts.  
[00:29:05] Mixture of experts has been around for a really long time, maybe even back in 2017,  
[00:29:11] but the techniques have changed a lot.  
[00:29:13] DeepSeek's mixture of experts was a big change in how it worked.  
[00:29:17] There have been older papers, like "GShard" and "Switch Transformer".  
[00:29:21] The actual empirical results are going to depend on all of that.  
[00:29:24] On one of the older techniques shown here, you can see if I hold constant  
[00:29:29] the number of active parameters at a certain size, and then I increase  
[00:29:32] the sparsity, which they call expert count, the quality keeps increasing.  
[00:29:37] If you imagine drawing a horizontal line from 1.3B dense across, you end up  
[00:29:43] seeing that, in this case, the 64-expert 370-million activated parameter model  
[00:29:49] is as good as a dense 1.3-billion model.  
[00:29:52] So in some sense, it's actually not amazing returns where you need  
[00:29:55] to increase total parameters a hundredfold to get the equivalent  
[00:30:00] of 10x as many active parameters.  
[00:30:04] Actually even more so.  
[00:30:05] It's a huge increase in parameter count for a modest increase in efficiency.  
[00:30:10] So in this case, actually it's 4x?  
[00:30:11] 64x for 4x.  
[00:30:13] So while it is true that you get this benefit of being able to economize  
[00:30:24] on your compute time if you increase sparsity, naively it would seem  
[00:30:29] like a trade-off worth making.  
[00:30:32] But if you're decreasing  
[00:30:35] this by 2x and then having this go up by 8x every time you double sparsity...  
[00:30:42] Is that good or bad, actually?  
[00:30:44] Even from a memory point of view… Keep in mind you are doubling this  
[00:30:48] portion of the memory fetches, which is amortized by batch.  
[00:30:52] So just keep running a larger batch size.  
[00:30:56] From the point of view of the analysis we've done here, this is a pure win.  
[00:31:00] Keep doing it until you run out of available users, basically.  
[00:31:08] There's  
[00:31:12] this equivalence where if I have a lot of users, I can go to a much sparser model.  
[00:31:16] From that point of view, it's a reasonable trade-off.  
[00:31:18] The other trade-off that shows up here is that it also consumes memory capacity.  
[00:31:23] We've only reasoned about memory bandwidth here, but it  
[00:31:25] also consumes memory capacity.  
[00:31:26] I see.  
[00:31:27] Let me make sure I understood.  
[00:31:29] You're saying we want  
[00:31:35] to spend less time computing, therefore we do more sparsity.  
[00:31:40] To make that work, we need bigger batch sizes.  
[00:31:42] Which means we need more memory capacity  
[00:31:48] to have more sparsity.  
[00:31:49] Maybe this would be a good point to talk about how a mixture of experts layer is  
[00:31:54] typically laid out on a rack of GPUs.  
[00:31:58] Cool.  
[00:31:58] Makes sense.  
[00:32:00] Where were we?  
[00:32:01] Sparse mixture of experts.  
[00:32:03] Maybe how we lay that out on a GPU.  
[00:32:08] Let's zoom in on the mixture of experts layer first and draw what that looks like.  
[00:32:15] Typically, we'll have some kind of a router layer, which is making the  
[00:32:20] decision of where we route the tokens to.  
[00:32:23] We get tokens coming in here, they go through a router layer, and then  
[00:32:27] we have a bunch of different experts.  
[00:32:34] I'll draw a few more to line some up.  
[00:32:38] The router will make a decision of which experts it's going to  
[00:32:41] route to, and it will be a small fraction of them, maybe 1 in 32.  
[00:32:45] Maybe it will make a decision to route to this one,  
[00:32:49] maybe this one, and maybe this one.  
[00:32:56] Each expert itself is a normal MLP.  
[00:32:59] It has an up projection and then a down projection with a nonlinearity in between.  
[00:33:04] Then finally, we do the inverse operation.  
[00:33:07] Where we were broadcasting things out here, we're going to bring  
[00:33:10] them back in and sum them up.  
[00:33:16] Bringing them in like  
[00:33:19] this.  
[00:33:19] Then finally, we have our residual connections.  
[00:33:21] The token is also passed through here, and it gets added to  
[00:33:26] the result of the MoE layer.  
[00:33:28] This is a normal MoE layer.  
[00:33:31] What I want to talk through is how this is mapped to a GPU rack and what  
[00:33:37] this means for communication, because I think this will start to show some  
[00:33:41] of the limits of how sparse we can go.  
[00:33:46] The standard practice here, and it is the best solution,  
[00:33:48] is to use expert parallelism.  
[00:33:51] That means different experts go on different GPUs.  
[00:33:54] If we take something like a DeepSeek model, they have 256 experts.  
[00:34:00] Let's say we want to run that on a Blackwell rack.  
[00:34:04] There are 72 GPUs.  
[00:34:07] We have a divisibility problem.  
[00:34:09] This is not a power of two.  
[00:34:11] We'll just simplify and say we're only going to use 64 of them.  
[00:34:16] Just ignore the other eight.  
[00:34:17] It's not a big deal.  
[00:34:18] So we have four experts per GPU.  
[00:34:23] Very simple.  
[00:34:24] For the sake of the diagram, actually let's just say we  
[00:34:26] have two experts per GPU.  
[00:34:28] We end up just putting these GPU boundaries.  
[00:34:34] Every pair of experts is on its own GPU.  
[00:34:39] Then we can look at the communication cost.  
[00:34:40] We had some tokens stored centrally here.  
[00:34:44] They get routed to all of these experts,  
[00:34:48] and there is some communication cost paid here.  
[00:34:51] There's the same communication cost paid on the output.  
[00:34:55] The hope is that this does not become communication limited.  
[00:34:58] Now  
[00:35:01] what is the traffic pattern here?  
[00:35:03] The traffic pattern here is that any GPU will be talking to  
[00:35:06] any other GPU, depending on the decisions made by the model.  
[00:35:11] This is an all-to-all traffic pattern.  
[00:35:14] When you say any GPU in the pre-tense, the router is more than one GPU?  
[00:35:20] I drew this as one router.  
[00:35:22] In reality, you would actually have many copies of the router, and you would  
[00:35:25] have as many routers as GPUs, in fact.  
[00:35:30] As the incoming traffic.  
[00:35:32] Yeah.  
[00:35:33] These are 64 GPUs and these are 64 GPUs.  
[00:35:37] It's actually the same GPUs, we just draw them as separate because  
[00:35:40] they're serving different purposes.  
[00:35:42] So at this point, any GPU can be sending to any other GPU.  
[00:35:46] This all-to-all pattern of communication that shows up and how the Blackwell  
[00:35:52] racks are configured is a perfect fit for the communication pattern that the MoE  
[00:35:59] actually wants to do.  
[00:36:01] However, if you think maybe one rack is too slow and I want to do two  
[00:36:06] racks, then I have this challenge that maybe I've got some sort of rack  
[00:36:11] boundary drawn outside here like this,  
[00:36:17] and I no longer have all-to-all communication between all  
[00:36:21] the GPUs in two racks.  
[00:36:24] The rack-to-rack communication ends up being a substantial bottleneck.  
[00:36:30] The fundamental thing here is that one rack bounds the size  
[00:36:33] of an expert layer you can do.  
[00:36:36] This has been part of what's been driving towards larger and  
[00:36:40] larger interconnect domains.  
[00:36:42] Before we continue, it may be worth you explaining what exactly a rack is.  
[00:36:47] The differences in bandwidth between a rack and within a rack, and the  
[00:36:52] all-to-all versus not all-to-all nature of communication within versus outside.  
[00:36:56] This is a place where it starts to be very different between Nvidia, for example,  
[00:37:00] and Google, and then others, including us.  
[00:37:04] Generally, a rack  
[00:37:09] is a physical structure.  
[00:37:11] It's a few meters tall, a meter or two wide, depending on configuration,  
[00:37:16] and it stores some number of GPUs or XPUs, which is typically about  
[00:37:24] 64.  
[00:37:24] What constrains it being a certain size is power delivery,  
[00:37:27] weight, and cooling ability.  
[00:37:31] It ends up being about this size in many cases because of  
[00:37:34] these physical constraints.  
[00:37:38] When I deploy a data center, a data center may have thousands of these racks.  
[00:37:42] I've got one of these tall racks, it's got a bunch of GPUs in it, and so on.  
[00:37:46] And then I put another rack next to it.  
[00:37:50] You make it sound so easy.  
[00:37:51] Right.  
[00:37:52] I just drop them in.  
[00:37:55] In Nvidia's case, the communication topology…  
[00:38:02] They actually put the GPUs on the outside of the rack, and then they put  
[00:38:07] these switches on the inside of the rack.  
[00:38:09] What this ends up being is that there's a set of switches in here.  
[00:38:13] These are the NV switches.  
[00:38:17] Then they run a bunch of cables.  
[00:38:19] Every single GPU has cables going to the switches in the middle.  
[00:38:33] The switches have connections to all the GPUs.  
[00:38:35] All of the GPUs can talk to all the other GPUs in just two hops: going to  
[00:38:39] the switch, going to the other GPU.  
[00:38:41] Now, when I want to leave the rack, I end up going via a different path.  
[00:38:47] The GPUs also have a much slower connectivity, which is typically  
[00:38:52] about eight times slower.  
[00:38:56] The green that I drew here in the GPU cases is the NVLink.  
[00:38:59] More generally, it's called the scale-up network.  
[00:39:06] You will typically also have a scale-out network, which allows you  
[00:39:10] to connect to some data center switch.  
[00:39:13] All  
[00:39:19] of the GPUs will have some connectivity up to some data center switch somewhere.  
[00:39:23] This is  
[00:39:26] the scale-out, and  
[00:39:31] it tends to be about 8x slower  
[00:39:35] in bandwidth.  
[00:39:39] The challenge, if you want to lay out a mixture of experts layer across two racks,  
[00:39:44] is that half of the GPUs here are going to be wanting to talk to the GPUs here.  
[00:39:54] On average, when I look at where the tokens on these GPUs want to go, half of  
[00:39:59] the tokens want to go inside the rack.  
[00:40:00] That's great.  
[00:40:00] They can use the fast scale-up network.  
[00:40:03] But half the tokens are going to want to leave the rack and go to the  
[00:40:06] other rack, and that's not as good.  
[00:40:07] They need to use a much slower network, and so that becomes the  
[00:40:10] bottleneck on the all-to-all pattern.  
[00:40:13] A different choice would be, why don't I have a big switch  
[00:40:18] here and connect everything to  
[00:40:24] a much bigger switch that actually combines the two racks together?  
[00:40:27] There are many ideas in this direction, but in general, the  
[00:40:31] reason you have this hierarchy of switches rather than one big switch  
[00:40:34] is to manage the cabling congestion.  
[00:40:35] You just need to run a large number of cables.  
[00:40:39] Sorry, is that question you just asked basically, why isn't it a bigger scale-up?  
[00:40:43] Exactly.  
[00:40:44] Why not just have a million chips in scale-up or a thousand chips?  
[00:40:47] What has changed that has allowed Nvidia to go from Hopper, which was 8, then  
[00:40:53] Blackwell is 72, and now Rubin will be...  
[00:41:00] is it 500 something?  
[00:41:00] Yeah, 500 and something.  
[00:41:01] What has allowed that to happen?  
[00:41:02] From Hopper to Blackwell is mostly just the decision to switch from  
[00:41:10] trays as the form factor to switching to racks as the form factor.  
[00:41:15] That's a product decision.  
[00:41:16] There wasn't a substantial technical barrier there.  
[00:41:21] Switching from 64 to 500 or  
[00:41:27] so, there's a bit of Jensen math there, but there is at least a genuine 4x  
[00:41:33] increase, which is coming from a much more complicated and difficult rack design.  
[00:41:38] That is actually a new physical design to run more cables.  
[00:41:42] The cable complication is just the cost of figuring out which cable hops to which,  
[00:41:49] or which signal goes from what to what?  
[00:41:51] Let's zoom in on this and look at the wire density.  
[00:41:57] I'll draw this diagram just once more so we have a bit of a cleaner  
[00:41:59] and larger version to work with.  
[00:42:03] Let's say I have some switches in the middle.  
[00:42:04] Initially, I'm going to start with just two GPUs on each side  
[00:42:09] or two trays of GPUs on each side.  
[00:42:12] Let's say maybe each tray wants to have two cables coming out of it.  
[00:42:21] I physically run vertical cables that look like this running out to the switches.  
[00:42:25] Now if I want to double the number of GPUs in a rack,  
[00:42:31] I need to run literally twice the density of cables.  
[00:42:35] I need to run  
[00:42:38] these as well.  
[00:42:42] Extremely naive question.  
[00:42:43] But if you look at a physical data center, it seems like there's  
[00:42:47] a lot of space within a rack.  
[00:42:49] I don't know.  
[00:42:49] The cables are really big and...  
[00:42:52] There is space outside the rack.  
[00:42:54] Inside the rack… As they become more optimized, these racks are  
[00:42:59] very tight.  
[00:42:59] There's  
[00:43:02] connector density going from  
[00:43:07] the tray into the rack and the rack's backplane, and the backplane  
[00:43:10] itself has a really high density.  
[00:43:13] There are other physical constraints including the bend radius of cables.  
[00:43:16] You don't want to snap them and so on.  
[00:43:19] Okay, so it's literally the physical space to put a cable that's constraining it.  
[00:43:22] I had no idea.  
[00:43:23] Interesting.  
[00:43:24] That seems surprising.  
[00:43:25] The  
[00:43:27] rack is so big and we can't just stuff more cables in there.  
[00:43:31] Rack design is not my expertise, but when I talk to folks on what  
[00:43:34] constraints they're up against, it's a combination of things.  
[00:43:39] What are the big physical things you're optimizing for?  
[00:43:42] Space, weight of the rack.  
[00:43:45] It's actually really heavy, so you need enough metal to not sag and fall.  
[00:43:50] But then you add more metal, and it's heavier.  
[00:43:52] Then power and cooling.  
[00:43:53] All of those are competing.  
[00:43:56] Modern racks are pushing all of those to very extreme physical limits.  
[00:44:00] Deep work is by its nature quite aversive, so even things which seem  
[00:44:03] like work, like Slack and email, can be easy ways to distract yourself.  
[00:44:07] So I often wish that I could just turn the internet off.  
[00:44:11] But if I'm prepping for an interview, even if I have the papers and books on hand,  
[00:44:14] it's still super useful to be able to do a back and forth with an LLM so I can break  
[00:44:18] down concepts and research follow-ups.  
[00:44:20] Google's new Gemma 4 is the first open model that allows me to have this kind  
[00:44:24] of fully disconnected focus machine.  
[00:44:26] It's small enough to run on my laptop, but good enough to actually be useful.  
[00:44:29] So to prep for this episode, I downloaded Reiner's scaling  
[00:44:32] book and shut off the internet.  
[00:44:33] I was able to have Gemma help me understand the material  
[00:44:35] and answer my questions.  
[00:44:36] If you want an LLM that you can run locally on your laptop or even your  
[00:44:39] phone, you should check out Gemma 4.  
[00:44:45] When was GPT-4 released again?  
[00:44:46] Was it 2022 or 2023?  
[00:44:48] 2023.  
[00:44:48] Okay.  
[00:44:49] And it was rumored to be over one trillion parameters.  
[00:44:53] It seems like only now, within the last six months, have models been getting  
[00:44:58] released that have significantly more parameters than the model released three  
[00:45:00] years ago, when supposedly there should have been this scaling in the meantime.  
[00:45:07] Is the reason that we were just waiting for racks with enough memory  
[00:45:11] to hold a five-trillion parameter model, along with its KV cache for  
[00:45:18] enough users for a lot of sequences?  
[00:45:21] Or if you're doing RL, a similar consideration of actually  
[00:45:25] holding the KV cache for  
[00:45:28] the batch of problems you're trying to solve.  
[00:45:30] If you look at Hopper, you had eight Hoppers, and I think  
[00:45:35] that's 640 gigabytes as of 2022.  
[00:45:39] With Blackwell finally, which was deployed in…?  
[00:45:42] Very recently.  
[00:45:43] Maybe last year.  
[00:45:44] Last year.  
[00:45:44] You finally have a scale-up on the order of 10-20 terabytes, which is  
[00:45:49] enough for a 5T model plus KV cache.  
[00:45:53] Deploying in larger scale-up domains is a huge unlock.  
[00:45:58] I've drawn here the Nvidia Blackwell deployment.  
[00:46:01] The Google deployment has actually had very large scale-up  
[00:46:04] domains for a long time.  
[00:46:05] That also explains why Gemini seemed to be ahead.  
[00:46:08] It  
[00:46:11] just seems like Gemini has had successful pre-training for longer  
[00:46:14] than some of the other labs.  
[00:46:15] Not having been there at the time, I'm not sure how much is coming  
[00:46:17] from successfully deploying higher sparsity ratios, which it could be.  
[00:46:22] It could also be a whole bunch of actual modeling things,  
[00:46:27] specifically how you do the mixture of experts.  
[00:46:29] We've seen  
[00:46:33] the DeepSeek mixture of experts activate more experts, but finer-grained experts.  
[00:46:38] That was a big innovation.  
[00:46:39] I'm sure there are many other innovations on the model architecture  
[00:46:43] as well as on the training data.  
[00:46:44] It's hard to disentangle all of them, but what shows up in terms  
[00:46:48] of the limits of what you can do  
[00:46:52] is that the active parameters, as we saw, are limited by the compute  
[00:46:57] cost, and the total parameters are limited by the scale-up size.  
[00:47:02] When you're operating within a single scale-up domain, is that  
[00:47:06] a consideration specifically for either forward or backward, or  
[00:47:12] specifically for prefill versus decode?  
[00:47:17] Or is it preferred to always be within a scale-up whatever kind  
[00:47:23] of workload you have, whether you're doing a pre-training run, RL  
[00:47:29] generation, or inference for users?  
[00:47:32] Really interesting.  
[00:47:37] To answer that question, we're going to need to talk about  
[00:47:38] the communication patterns.  
[00:47:40] We've talked about the mixture of experts communication pattern.  
[00:47:43] That is this all-to-all.  
[00:47:51] All-to-all very strongly favors full connectivity,  
[00:47:57] which is what we've just shown here, and it favors being within one rack.  
[00:48:03] There are other kinds of parallelism besides expert parallelism,  
[00:48:06] which we just showed here.  
[00:48:08] In the literature is  
[00:48:12] tensor parallelism.  
[00:48:12] With the trend towards smaller experts, this has become much less  
[00:48:15] relevant, so we can ignore that.  
[00:48:17] But the other two things we have available are data parallelism  
[00:48:20] and pipeline parallelism.  
[00:48:24] They can be a much better fit for using multiple racks.  
[00:48:28] Let's focus on pipeline parallelism specifically.  
[00:48:32] This is one layer of MoE.  
[00:48:34] I'm going to have a hundred more layers up above.  
[00:48:39] I could decide at this point, for example, to move to a different rack, change rack.  
[00:48:50] Now, is that going to become a communication bottleneck?  
[00:48:54] We can actually solve for when this becomes a communication bottleneck.  
[00:48:57] Before we do that algebraically, let's  
[00:49:00] visualize it out and sketch the path.  
[00:49:01] We're going to have another MoE layer, and another MoE layer here, and so on.  
[00:49:09] Let's say I change rack here, and then some number of layers  
[00:49:12] later, I change rack here as  
[00:49:21] well.  
[00:49:21] The methodology we're going to use to determine whether we have  
[00:49:24] a communication bottleneck at the point where we change rack is we're  
[00:49:28] going to compare the scale-out  
[00:49:35] bandwidth requirements to the scale-up bandwidth requirements.  
[00:49:43] Let's write this.  
[00:49:44] The hint is going to be that there's a lot more sends here.  
[00:49:49] We're sending many things here, whereas we're only sending one thing here, and  
[00:49:52] we're also maybe doing it many times.  
[00:49:54] That's  
[00:49:56] what makes the difference.  
[00:49:58] Can I try to guess?  
[00:49:59] Just out of curiosity, to see if I'm actually understanding, it seems like  
[00:50:03] you're sending batch size into the rack.  
[00:50:07] In here?  
[00:50:08] Yes.  
[00:50:09] But the communication within the rack is batch size times number of GPUs.  
[00:50:18] Number of activated GPUs.  
[00:50:21] I don't send to this GPU at all.  
[00:50:23] There's an explosion from 1-3x larger here in this diagram.  
[00:50:29] The key thing is that I didn't even need to send to this GPU at  
[00:50:32] all, and so that's a big saving.  
[00:50:35] We're going to talk through  
[00:50:40] to what extent scale-up is a bottleneck over scale-out.  
[00:50:48] We will directly jump to the ratio of the time spent on scale-up  
[00:51:00] over the time spent on scale-out.  
[00:51:04] This is the quantity we're talking about.  
[00:51:09] The first consideration is that scale-up is  
[00:51:15] 8x faster than scale-out generally.  
[00:51:18] At a baseline, if the bandwidths were the same, we would have this  
[00:51:21] 1/8, which is coming from bandwidth.  
[00:51:28] But then we have some amount of expansion in how much data we're sending.  
[00:51:34] If one token comes in here, then this one token gets routed to, in the DeepSeek  
[00:51:40] case maybe 32 experts or 16 experts.  
[00:51:44] It gets routed to some number of experts.  
[00:51:47] So this is the number of  
[00:51:51] activated  
[00:51:54] experts.  
[00:52:03] This same thing applies on multiple different layers, so  
[00:52:05] maybe I'm going to run two layers.  
[00:52:08] There's also multiple times the number of layers  
[00:52:16] per stage.  
[00:52:19] Don't you need to multiply the whole thing by two for the all-to-all?  
[00:52:22] For the up and down.  
[00:52:23] Yes, there's a factor of two.  
[00:52:28] Thank you.  
[00:52:29] What we would like is for the scale-up time to be greater than the scale-out  
[00:52:33] time, because the scale-up time is the more important and precious resource.  
[00:52:38] We would like this number to be greater than or equal to one.  
[00:52:43] This really doesn't seem hard.  
[00:52:44] There's just a factor of 8 that we need to overcome.  
[00:52:46] So we need the product of these three things to be bigger than 8.  
[00:52:50] Typically we have a fairly large number of activated experts.  
[00:52:53] It could be 8 by itself.  
[00:52:55] Then we can increase the number of layers per stage a lot until we satisfy this.  
[00:53:01] What this ends up looking like is that I can have an entire pipeline of racks  
[00:53:05] where one rack does one layer, and then I move on to the next rack and  
[00:53:08] do another layer, and then I move on to the next rack and do another layer.  
[00:53:11] It's interesting to me that the best  
[00:53:15] parallelism strategy in practice ends up being one which physically  
[00:53:20] resembles the actual architecture.  
[00:53:23] It's not some galaxy brain thing.  
[00:53:25] It's like, "Oh, we have experts, we're going to put them on different GPUs,  
[00:53:27] or we have different layers, we're just going to put them on different  
[00:53:29] racks." I feel that's interesting.  
[00:53:31] The cutting matches the model architecture.  
[00:53:37] Exactly.  
[00:53:38] It could have been something wackier with tensor parallelism and whatever.  
[00:53:45] The galaxy brain way to think of it is,  
[00:53:49] what are all the different dimensions in which a model is scaled up?  
[00:53:54] It is scaled up by layers,  
[00:53:58] it is scaled up by the model dimension, it is scaled up by the DFF dimension, it  
[00:54:00] is scaled up by the number of experts.  
[00:54:02] Every single one of those numbers you can choose to cut along.  
[00:54:06] If those numbers are big enough, it eventually becomes  
[00:54:08] profitable to cut along there.  
[00:54:11] We have selected two of them.  
[00:54:12] The other two, in the way models are typically sized, are not profitable.  
[00:54:16] So there's a talk by Ilya where he says, "Today we know not  
[00:54:21] to do pipeline parallelism."  
[00:54:23] And Horace He gave my friends and me… I hate that it sounds  
[00:54:29] like a Dr. Seuss quote.  
[00:54:33] But he gave us a lecture on these different kinds of parallelisms.  
[00:54:36] He said the problem with pipeline parallelism is that, other than  
[00:54:39] the bubbles, it creates these architectural constraints.  
[00:54:42] Kimi,  
[00:54:45] for example, has these residuals where attention attends to layers a few back, so  
[00:54:52] it becomes hard to implement in this way.  
[00:54:56] I guess we didn't fully articulate even what is the  
[00:54:59] benefit that we're getting from  
[00:55:05] pipelining.  
[00:55:05] These complexities are real.  
[00:55:06] Pipelining is a massive hassle, but it does give you some benefits.  
[00:55:15] You can then decide whether those benefits are worth the costs.  
[00:55:22] It has some benefits in inference, maybe bigger benefits in training.  
[00:55:25] In inference, what are we saving on?  
[00:55:27] Are we saving on memory time or compute time?  
[00:55:31] Not really.  
[00:55:32] We're just moving the memory time from one chip to another chip,  
[00:55:35] or one rack to a different rack.  
[00:55:37] There's no actual benefit in runtime.  
[00:55:41] However, what we are saving on is memory capacity.  
[00:55:45] If we think that the memory in a rack is a bottleneck, then there's  
[00:55:51] a constraint on how fast we can go.  
[00:55:55] Pipelining allows us to massively reduce that bottleneck.  
[00:55:59] The opposite connotation to this… Before this interview, I was  
[00:56:06] chatting with Axel, who's a GPU performance engineer at Jane Street.  
[00:56:11] He was explaining that to do pipelining, you have to do  
[00:56:13] micro-batches rather than full batches.  
[00:56:16] If you do micro-batches, then you're by definition not able to  
[00:56:23] amortize loading the weights across all the users or all the sequences.  
[00:56:30] The positive connotation of that is you don't have to use as much memory.  
[00:56:32] The negative connotation is that we can't amortize loading the  
[00:56:36] weights across all those users.  
[00:56:37] Maybe it's worth explaining why you have to do micro-batches.  
[00:56:40] Shall we draw the pipeline bubble?  
[00:56:46] What is this micro-batching that shows up in pipeline  
[00:56:53] parallelism?  
[00:56:53] I'll focus on inference first.  
[00:56:55] It's a slightly simpler problem.  
[00:56:56] I'm going to draw time, and then which rack  
[00:57:06] we're on.  
[00:57:07] The idea is that maybe I'll have four racks.  
[00:57:10] I've got an inference that is going to step through these four  
[00:57:14] racks in some time like this.  
[00:57:19] This is inference number zero.  
[00:57:20] It  
[00:57:23] runs at a certain batch size and steps through all the pipeline stages like this.  
[00:57:28] Now, if we were to say, "Well, we're going to run inference number one  
[00:57:30] here," this is clearly a massive waste.  
[00:57:34] Like three-quarters of the time each of the racks is doing  
[00:57:40] nothing.  
[00:57:40] We don't actually run inference one here, we run it as soon as we can, which is  
[00:57:44] immediately after inference zero finishes.  
[00:57:47] And  
[00:57:50] then we keep going.  
[00:57:53] If we hadn't filled this in, we would call this the pipeline bubble.  
[00:57:56] When I've drawn it in this inference context where we're only going  
[00:57:58] in a forwards pass, it's obvious.  
[00:58:00] Why would you do this stupid thing?  
[00:58:02] In a training context, it's maybe less obvious.  
[00:58:05] But in the inference context, it's really natural to make this change.  
[00:58:09] Oh, interesting.  
[00:58:14] This is sort of obvious, but the difference between micro-batch and batch  
[00:58:16] doesn't matter at all in inference because you can just call it whatever you want.  
[00:58:22] It only matters in training because there is an optimal batch size.  
[00:58:27] Yes.  
[00:58:28] Before you do a full backward step, you want to have accumulated  
[00:58:33] all the sequences in that batch.  
[00:58:33] If you want to do  
[00:58:38] pipelining in training, in order to avoid that bubble, you need to—  
[00:58:43] Should we draw the training diagram  
[00:58:48] with that?  
[00:58:48] Let’s do that.  
[00:58:48] This is the inference diagram, and I'll call this forward so we don't  
[00:58:51] have the wrong thing showing up there.  
[00:58:53] Let's do the same thing for training now.  
[00:58:55] We've got a forwards pass, but at some stage we're going to have to  
[00:58:57] transition to a backwards pass.  
[00:59:01] We'll do some number of batches in the forwards pass,  
[00:59:11] and then we're going to transition to the backwards pass for everyone all  
[00:59:24] in one go.  
[00:59:24] The inference part is the same here, but then we do a hard stop at this point  
[00:59:28] and transition everyone to the backwards pass, with similar numbering like this.  
[00:59:33] It may be worth clarifying the reason there is that hard stop  
[00:59:35] is because you want to do a whole batch at once for the backward step.  
[00:59:40] And then there is an optimal size for how big that batch should be.  
[00:59:45] Smaller is always better, actually, is a way to put it.  
[00:59:48] From an ML convergence rate perspective, smaller is always better  
[00:59:53] because you're getting the freshest information from the gradient descent.  
[00:59:55] But from a total training time perspective?  
[00:59:58] From a total training time perspective, smaller is worse  
[01:00:01] from a systems perspective.  
[01:00:02] The optimum is the trade-off between those two.  
[01:00:05] So you pick a batch size, and  
[01:00:10] for that batch size, you do some amount forwards and then some amount backwards.  
[01:00:14] You asked why there is even a hard stop there.  
[01:00:16] With pipeline parallelism, because  
[01:00:21] you've got this idle time here which is the bubble, there are so many  
[01:00:26] techniques in the literature for how to lay this out differently and avoid that.  
[01:00:31] There are more complicated schemes called zero bubble or one-forward-one-backward,  
[01:00:35] which interweave the forwards and the backwards in complicated ways.  
[01:00:40] You can mine Bitcoin in that bubble.  
[01:00:42] Right.  
[01:00:42] More usefully, you can do the weight gradient step, but  
[01:00:46] you can also mine Bitcoin.  
[01:00:49] In inference, the effect of pipelining on anything you care about, like  
[01:00:55] batch size or latency, is neutral.  
[01:00:58] It doesn't improve it, it doesn't make it worse.  
[01:01:00] If you look at the latency of this inference, running it if it were pipelined  
[01:01:03] versus if it were all on one rack… If it were all on one rack, we would just slide  
[01:01:07] all the boxes down and still put them in a row, and the latency would be the same.  
[01:01:11] Pipelining  
[01:01:14] is neither better nor worse for latency.  
[01:01:17] It does mean that you just use less memory capacity per rack.  
[01:01:23] Because now instead of needing the whole model, you only need a quarter  
[01:01:25] of the model, and you can expand.  
[01:01:26] Makes a ton of sense.  
[01:01:27] So it's a no-brainer to use pipelining during inference, but there's this  
[01:01:33] harder trade-off during training.  
[01:01:36] Even in inference, in fact, it is not used a ton.  
[01:01:39] It reduces your memory capacity requirements, but there's  
[01:01:42] actually a huge surplus.  
[01:01:44] I think you were saying that a rack of Blackwell has many tens of terabytes.  
[01:01:52] That's much bigger than a trillion parameter model.  
[01:01:58] A trillion parameter model only needs one terabyte, so it already fits.  
[01:01:59] There's not a huge benefit from pipelining because you're reducing a  
[01:02:05] number that's already pretty small.  
[01:02:07] But it does say that theoretically, maybe you had too much memory there.  
[01:02:11] You could have  
[01:02:14] built different hardware that has less memory.  
[01:02:16] If you were designing your hardware, you could say, "I didn't need that  
[01:02:19] much memory because I don't need the weights to fit in one rack.  
[01:02:22] I can fit the weights in eight racks, then I could have built hardware that  
[01:02:28] didn't have so much HBM per GPU."  
[01:02:30] Last week, Horace He was kind enough to give me and my friends a great lecture  
[01:02:34] on large-scale pre-training systems.  
[01:02:36] And there were some concepts that I wanted to animate for a write-up  
[01:02:39] on my blog, like how weights shard and gradients flow depending on  
[01:02:43] the parallelism that you're using.  
[01:02:45] So I gave Cursor my lecture notes and a sketch that I made during the lecture.  
[01:02:49] And I asked it to visualize a specific hierarchical collective  
[01:02:53] that Horace had explained.  
[01:02:55] The first version was already pretty good, and then I was able to use  
[01:02:57] design mode to select and tweak any specific components from there.  
[01:03:01] I was able to do all of this without a clear end state in mind.  
[01:03:03] Cursor's Composer 2 Fast model was quick enough that I was able to  
[01:03:06] iterate almost instantaneously.  
[01:03:08] I could try an idea, test the results in the built-in browser,  
[01:03:11] and immediately make any changes.  
[01:03:13] I went through 10 different versions in under 20 minutes.  
[01:03:15] If you want to check out this animation, I published it along with  
[01:03:18] the lecture notes in a blog post.  
[01:03:20] The link is in the description.  
[01:03:21] And if you want to try out this kind of iterative design flow for yourself, go  
[01:03:24] to cursor.com/dwarkesh to get started.  
[01:03:31] everybody's talking about the memory wall right now.  
[01:03:33] Memory is getting super expensive.  
[01:03:34] There's not enough memory.  
[01:03:36] Smartphone volume will go down 30% because there's not enough memory.  
[01:03:41] This is shocking, Dylan said hyperscalers are spending 50% of  
[01:03:45] their CapEx this year on memory.  
[01:03:47] That’s believable.  
[01:03:50] What is hyperscaler CapEx?  
[01:03:51] That's high hundreds of billions, maybe a trillion, and they're  
[01:03:54] spending half of that on memory?  
[01:03:57] That is a huge constraint.  
[01:03:58] That's why we're not going to get new laptops and phones this year.  
[01:04:00] But at the same time, we have too much memory?  
[01:04:04] People are willing to put too much memory into these systems.  
[01:04:06] Why is Jensen shoving all this memory into these racks if you don't need it?  
[01:04:14] In the equations we had here before we erased them, we were doing memory time,  
[01:04:18] memory bandwidth and compute bandwidth.  
[01:04:20] Let's now start looking at memory capacity.  
[01:04:23] We'll start off with memory capacity without even thinking  
[01:04:26] about a parallelism scheme.  
[01:04:35] The demand on memory is the number of total parameters.  
[01:04:43] This is what we need to fit the weights in some system that we are using.  
[01:04:48] Then we need to fit the KVs as well.  
[01:04:51] KVs go as batch size times the length of the context  
[01:04:56] times the bytes per  
[01:05:06] token.  
[01:05:07] What I was arguing about in this context, and the case I was making  
[01:05:10] for pipelining, is that there are some techniques that allow us to solve this.  
[01:05:18] Let's consider running this on some number of GPUs.  
[01:05:23] We're going to have one extent, which  
[01:05:28] is E, the expert  
[01:05:32] parallelism.  
[01:05:33] When we had this sharding of an expert layer across many GPUs,  
[01:05:38] to what extent do we do that?  
[01:05:39] How many GPUs?  
[01:05:42] We're going to say that this is, for example 64.  
[01:05:46] Then P is going to be the extent of  
[01:05:52] pipelining.  
[01:05:52] This is the number of racks,  
[01:05:56] maybe we'll pick 4 or something  
[01:06:01] like that.  
[01:06:03] This is the total memory requirement across the system,  
[01:06:07] but now I'm going to calculate a  
[01:06:11] memory requirement per GPU.  
[01:06:20] I'll use a lowercase  
[01:06:26] cmem.  
[01:06:26] Obviously, we just take all of these numbers and divide  
[01:06:27] it by E and P. Really easy.  
[01:06:29] It's  
[01:06:32] this Ntotal, plus the batch times length of context times bytes per  
[01:06:42] token, all divided by E times P.  
[01:06:49] Why is this correct as divided this way?  
[01:06:54] We knew that the parameters were perfectly divided amongst all the GPUs in a rack.  
[01:07:00] The layers are perfectly divided amongst the different racks.  
[01:07:04] So that works here.  
[01:07:05] Somehow we're going to arrange—I'll hand-wave exactly how—the same  
[01:07:10] perfect sharding of the contexts across GPUs in a rack, and then  
[01:07:15] based on layer across racks.  
[01:07:17] Sorry, 4 is the number of racks?  
[01:07:18] Yeah, for  
[01:07:25] example.  
[01:07:26] This is the place where we actually need to go back and analyze this batch size B.  
[01:07:30] You were making this comment that there's micro-batching versus global  
[01:07:35] batching.  
[01:07:35] Let's come back to this pipelining diagram here.  
[01:07:38] We've got one batch going forward here, and then as I drew it,  
[01:07:42] it kind of just disappeared.  
[01:07:44] That's not really correct.  
[01:07:45] If you think about how decode is working, I have a bunch of tokens  
[01:07:50] that I have generated already.  
[01:07:52] I do one forwards pass where I generate a new token,  
[01:07:57] and then I write that to my KV cache.  
[01:08:00] Then I do another forwards pass that generates the next token.  
[01:08:04] I'm actually going to be running this batch zero in a loop.  
[01:08:06] In fact, I go forwards.  
[01:08:10] Once I finish, I can start the next iteration of the loop up here.  
[01:08:17] We'll just  
[01:08:29] fill this in.  
[01:08:29] We've got the two,  
[01:08:36] three, two and three, and two and three.  
[01:08:36] Let's split this batch.  
[01:08:38] This batch will be the global batch size.  
[01:08:41] B is going to be the number of micro-batches times  
[01:08:51] the batch size per micro-batch.  
[01:08:53] How many micro-batches do we need?  
[01:08:55] The number of micro-batches in this diagram is 4: zero, one, two, three.  
[01:09:03] The micro-batch size is still this 2000-ish number.  
[01:09:08] Sorry, no, this is the  
[01:09:14] 300 times sparsity.  
[01:09:16] This is  
[01:09:22] how big the train that takes off every 20 milliseconds is.  
[01:09:23] Right.  
[01:09:23] This is going to be the 20-millisecond train.  
[01:09:29] The global batch size is the number of micro-batches times the local batch size.  
[01:09:33] Local batch size is set by this hardware parameter.  
[01:09:35] The number of micro-batches  
[01:09:39] is as small as possible, such that we can wrap around and not leave any idle time.  
[01:09:47] If we had fewer, we would have this idle time when we wrap around.  
[01:09:51] You can visually see that it is equal to the number of pipeline stages.  
[01:09:55] It's a proof by visual here.  
[01:09:57] It is 4, and it's 4 this way as well.  
[01:09:59] You can look and see that it goes along here, and then it wraps around  
[01:10:03] to the number of pipeline stages.  
[01:10:05] Sorry, very basic question.  
[01:10:06] Is this what is actually done?  
[01:10:10] A frontier model today will have pipelining during inference?  
[01:10:15] For sure during massive scale training this is done.  
[01:10:19] It can be done for inference.  
[01:10:21] I'm actually going to make the case for why it is less attractive.  
[01:10:24] It is useful for weights, but not so useful for KVs.  
[01:10:28] The  
[01:10:30] big challenge is... Let's fill this in.  
[01:10:33] The micro-batch size here ends up being equal to the number of pipeline stages.  
[01:10:40] When we go back and substitute all of that into here,  
[01:10:49] we get  
[01:10:52] a number of pipeline stages times this little b showing up in here.  
[01:10:59] When we factor this out, I'm going to split this plus into two terms.  
[01:11:04] We  
[01:11:08] get the full division by E times P over here.  
[01:11:12] We still have division by E times P over here, but the Ps cancel.  
[01:11:22] What we find is that if you increase the number of pipeline stages, the  
[01:11:26] memory footprint for the number of weights keeps going down and down and  
[01:11:29] down, but the memory footprint for the number of activations stays constant.  
[01:11:34] So it doesn't actually work.  
[01:11:37] Most of your memory…  
[01:11:40] Once you do enough pipelining—and it's really not much, even two is often  
[01:11:44] enough—this term becomes very small.  
[01:11:48] The KV cache becomes the dominant term.  
[01:11:52] I know this is wrong.  
[01:11:53] I'm just trying to think about why my train of logic here is wrong.  
[01:11:56] If  
[01:11:59] you're pipelining through many different stages, the KV values  
[01:12:02] are not shared between layers.  
[01:12:03] Why would it not help to be pipelining across multiple layers?  
[01:12:06] Because then you don't have to store...  
[01:12:08] You only need to store one layer rather than two layers of KVs.  
[01:12:12] It helps from that perspective, you're right.  
[01:12:16] What's competing with that, though, is that you need to be keeping all  
[01:12:19] of the racks usefully busy at a time, so the number of sequences that are  
[01:12:24] in flight simultaneously has gone up.  
[01:12:27] Ah, that makes sense.  
[01:12:28] Those exactly cancel, and you end up not getting a saving per GPU.  
[01:12:31] Right.  
[01:12:32] This is going back fundamentally to the point of how you're not  
[01:12:34] able to amortize across KV caches.  
[01:12:38] First, we established you can’t amortize KV caches across batch size.  
[01:12:41] Now we're saying you also can't shard it across pipeline stages.  
[01:12:48] It sucks from both of those points of view.  
[01:12:49] Interesting.  
[01:12:50] So then what is done during inference?  
[01:12:54] The DeepSeek paper reports what they do, which is that they just  
[01:12:58] do a lot of expert parallelism.  
[01:13:00] In effect, you should increase your expert parallelism up to your scale-up domain  
[01:13:04] size, and then do very little pipelining.  
[01:13:08] Maybe none at all, maybe two, just enough to make the weight  
[01:13:12] storage not too big of an issue.  
[01:13:15] Those are the only two parallelisms that really make sense.  
[01:13:17] In the past, there was tensor parallelism, which was cutting up within an expert,  
[01:13:24] but the experts are so small now that that is not a profitable optimization.  
[01:13:30] Does that mean that frontier labs, when they're doing inference, are  
[01:13:33] just within a single scale-up?  
[01:13:35] Yes.  
[01:13:36] You can look at how it depends on model size.  
[01:13:41] You could have a very large model,  
[01:13:46] one that exceeds the memory of a rack.  
[01:13:49] There you should be doing a bit of pipelining.  
[01:13:52] Maybe it's extremely sparse, for example, and that would be a reason to do it.  
[01:13:56] This goes back to the promise at the beginning of the lecture,  
[01:14:00] which was this will actually tell you about AI progress as well.  
[01:14:03] To the extent it is the case that model size scaling has been slow until recently…  
[01:14:10] Let me make sure I understand the claim.  
[01:14:12] The claim would not be you could have trained across more racks.  
[01:14:17] It was just that it would not have made sense before, we didn't have the ability  
[01:14:20] to do inference for a bigger model easily.  
[01:14:24] Actually, pipelining doesn't help with context length.  
[01:14:29] It totally helps with model size.  
[01:14:31] Because of the ability to do pipelining, a rack at least should  
[01:14:36] not be a constraint on your ability to fit the model parameters.  
[01:14:40] The other consideration you're asking is, why hasn't it scaled up more, and  
[01:14:43] why did bigger scale-up domains help?  
[01:14:46] We talked through one aspect of that, which is that it's  
[01:14:49] not because of memory capacity.  
[01:14:52] We have a solution to the memory capacity at least with respect to model size,  
[01:14:55] not with respect to KV cache size but at least with respect to model size.  
[01:15:03] The other issue that shows up is latency.  
[01:15:06] I was just about to ask, going from rack to rack, what is the latency cost per hop?  
[01:15:13] This is very much dependent on the hardware.  
[01:15:20] I can't say with a lot of authority.  
[01:15:21] I think it's probably on the order of a few milliseconds, but it could be  
[01:15:24] off by an order of magnitude there.  
[01:15:26] Is 4 a realistic number of how many pipelining stages you might have?  
[01:15:28] Yes.  
[01:15:29] So that's not that much.  
[01:15:31] On a small number of pipelining stages, this is not a huge latency impact.  
[01:15:35] But I guess it's 10 milliseconds per token.  
[01:15:39] That's right.  
[01:15:39] 2 times 4-ish, or I don't know how many you said… 10 milliseconds  
[01:15:45] per token is actually a lot.  
[01:15:46] If it goes from 20 to 30, or something  
[01:15:50] like that…  
[01:15:50] Just to chart the path that it goes through, here you're going from your  
[01:15:56] GPU or TPU to a network card, which  
[01:16:04] then goes to a top-of-rack switch,  
[01:16:08] and then hops over to the other rack and does the same thing in reverse.  
[01:16:12] You have to sum up the latencies of these different things.  
[01:16:15] Sorry, is this the same thing as the data center switch?  
[01:16:18] It may in fact go up to a data center switch and back.  
[01:16:21] It depends on deployment configuration.  
[01:16:22] Got it.  
[01:16:24] And because it's decode and sequential,  
[01:16:30] they stack up across the stages.  
[01:16:32] You can't do them at the same time.  
[01:16:34] That’s right.  
[01:16:36] This brings us back to the question then, is the size of the scale-up at  
[01:16:39] all relevant to why AI model sizes have been what they have been over  
[01:16:44] the last few years, whether through training or through inference?  
[01:16:48] We talked about latency of the hop.  
[01:16:53] There is also just the tmem  
[01:16:56] latency.  
[01:16:57] The memory time latency is actually massively improved  
[01:17:02] by larger scale-up domains.  
[01:17:06] I'll recall tmem down here.  
[01:17:07] tmem for the weights  
[01:17:18] was equal to the number of total parameters  
[01:17:24] divided by the memory bandwidth.  
[01:17:28] Which memory bandwidth are we talking about here?  
[01:17:30] Is it just one GPU?  
[01:17:32] It  
[01:17:34] is the number of GPUs that I can use in parallel to load these weights.  
[01:17:40] I can't use different pipeline stages in parallel because they're not  
[01:17:43] running at the same time, but I can use all the GPUs in my scale-up domain  
[01:17:46] in parallel to load the weights.  
[01:17:50] This is actually extremely effective.  
[01:17:54] Basically, I end up with a term here, this memory bandwidth term  
[01:17:57] itself is equal to scale-up size...  
[01:18:03] Times memory bandwidth per GPU.  
[01:18:05] Yeah.  
[01:18:05] Times GPU  
[01:18:09] bandwidth.  
[01:18:10] This term doesn't increase a lot.  
[01:18:11] It maybe increases 1.5 or 2x per generation, but this one increased  
[01:18:14] by a factor of 8 from Hopper.  
[01:18:16] So the reason the bigger scale-up matters, it's not the memory capacity of the whole  
[01:18:19] scale-up, but really the memory bandwidth.  
[01:18:21] Yeah.  
[01:18:22] Pipelining totally solves the capacity problem, but  
[01:18:27] scale-up size helps solve the bandwidth problem.  
[01:18:30] And the bandwidth problem helps you do longer context lengths,  
[01:18:34] which is more and more relevant as these models get more agentic.  
[01:18:37] It lets you just run the model at lower latency as a first thing.  
[01:18:41] If I just do a very sparse model and it's on a little H100 box,  
[01:18:46] the latency will be really high.  
[01:18:49] A super tangential question.  
[01:18:53] There's Chinchilla scaling, which tells you how big a model should  
[01:18:57] be relative to the amount of data you're going to train it on.  
[01:19:01] But now, obviously, you're not just trying to optimize for the highest quality model  
[01:19:07] you could get with training compute.  
[01:19:09] You want the best results a user can get with a mixture of  
[01:19:11] training and inference compute.  
[01:19:14] So there's a question of how much you should over-train a model  
[01:19:18] such that compute amortized over training and inference is minimized  
[01:19:23] to get a certain performance.  
[01:19:24] But now with RL, there's another consideration which is, you're going  
[01:19:30] to do some amount of pre-training.  
[01:19:32] That pre-training will be used both for RL generation and then  
[01:19:36] for inference for the final user.  
[01:19:39] By over-training here I mean that while it would have been more efficient just from  
[01:19:42] a training compute perspective to have a bigger model that you train for less time  
[01:19:46] because it can learn faster, maybe you get a smaller model, spend more compute  
[01:19:50] training it than you otherwise would have, but now it's cheaper to give it to users.  
[01:19:55] Let me make the question more concrete.  
[01:19:56] Basically, how much more than Chinchilla optimal are models over-trained?  
[01:20:00] And has that changed as a result of RL generation?  
[01:20:03] This is a place where we have to do a bit of guesswork because the updated  
[01:20:07] scaling laws and the model traffic are not reported, so we have to guess there.  
[01:20:14] One way to look at it…  
[01:20:19] Let me first just make a general heuristic claim.  
[01:20:23] If I have some cost, and I've got a total cost which is a sum of cost A  
[01:20:30] and cost B, like maybe this is the training cost and this is the inference  
[01:20:34] cost, and I want to minimize this sum…  
[01:20:39] For many  
[01:20:42] curves, the minimum tends to be where the costs are equalized.  
[01:20:47] That's something of a heuristic claim, but  
[01:20:52] there are many examples where it's true.  
[01:20:54] Where one is 1/x and the other one is x, for example, they tend to be minimized  
[01:20:59] at the point where they equal each other.  
[01:21:03] It's also true for ex and e-x and all kinds of other things.  
[01:21:10] Basically, I've got some curve that's going down, some other curve  
[01:21:14] that's going up, and they tend to be minimized at this equal point.  
[01:21:17] Heuristically,  
[01:21:21] I will conjecture that that is true for the setup you described as  
[01:21:27] well.  
[01:21:28] Actually showing that would be true would require looking at the  
[01:21:30] scaling laws and fitting these weird exponents, but things that follow  
[01:21:37] power laws tend to have this property.  
[01:21:39] So I'll just make that claim and move on.  
[01:21:43] We're going to say that we want to equalize the cost of training  
[01:21:47] and the cost of inference.  
[01:21:56] We can do all of it in general.  
[01:21:58] The cost of pre-training, that's the number of  
[01:22:05] active params times the data on pre-training.  
[01:22:13] There's a factor of 6 out here, which is the number of FLOPs.  
[01:22:16] There's the famous 6ND formula.  
[01:22:18] Then  
[01:22:20] in RL, we have approximately the same thing.  
[01:22:24] We've got the same number of active parameters, but now the  
[01:22:28] amount of data is the RL data.  
[01:22:31] There is this extra efficiency multiplier, or inefficiency...  
[01:22:42] Which is the fact that you're not training on all your rollouts.  
[01:22:45] Well, there's that, and then the other, perhaps even bigger  
[01:22:49] inefficiency is that this involves a substantial amount of decode.  
[01:22:54] Often decode runs at less MFU than training.  
[01:22:58] Okay.  
[01:22:59] So if you're doing a backward pass on every single generation  
[01:23:03] in RL, it would be 6ND.  
[01:23:06] So this could be a smaller number, right?  
[01:23:07] It  
[01:23:09] would at least be two, because that's the lower...  
[01:23:11] Somewhere in the range of two to six.  
[01:23:12] We'll say somewhere in the range of two to six and leave it  
[01:23:18] at that.  
[01:23:18] Then we can add in the inference cost.  
[01:23:20] The inference cost is two, the number of active parameters  
[01:23:24] times the data in inference.  
[01:23:28] Sorry, I think the way I said it was super garbled.  
[01:23:30] Just for the audience,  
[01:23:33] forward plus backwards per parameter is 6.  
[01:23:37] Forward alone is 2.  
[01:23:39] That's why RL, where you're definitely going to generate all the trajectories  
[01:23:43] but you might or might not train all the trajectories, is 2 to 6.  
[01:23:46] Yes.  
[01:23:48] Thank you.  
[01:23:48] And then inference is just 2.  
[01:23:51] We're going to solve for essentially equality of all three of these terms.  
[01:23:54] That is the ballpark of where people are going to be.  
[01:23:58] Labs have more information on what is productive in doing more RL, for  
[01:24:03] example, versus doing more pre-training.  
[01:24:04] I don't have that information, but I think a good ballpark is a  
[01:24:09] 33% split between each of them.  
[01:24:11] I'm not sure I understand the intuition for that.  
[01:24:15] Another naive model could have been that RL plus pre-training would  
[01:24:17] be 50% and inference would be 50%.  
[01:24:20] That's also a valid answer.  
[01:24:24] Because this is heuristic, I can't really argue for one versus the other.  
[01:24:27] They don't differ by that much.  
[01:24:28] Thirty-three versus twenty-five is only a small factor off.  
[01:24:36] Let's pick one of them.  
[01:24:38] All equal seems simple enough,  
[01:24:42] so we're just going to solve for equality of them.  
[01:24:44] It's pretty straightforward.  
[01:24:45] We can immediately see that the number of activated parameters totally  
[01:24:47] disappears, so let's factor that out.  
[01:24:49] We're going to just say that data in pre-training—I decided to do it your  
[01:24:55] way, it's a little bit nicer—plus...  
[01:24:59] Oh,  
[01:25:02] I didn't have the inefficiency over here either.  
[01:25:04] Data  
[01:25:08] in pre-training plus some multiple of α times the data in RL is  
[01:25:17] going to end up equal to some β times the data in inference.  
[01:25:28] Let's just roughly size the α.  
[01:25:30] This α  
[01:25:37] is maybe somewhere in the range of 2 to 6.  
[01:25:40] Over 6, from this term compared to this term.  
[01:25:44] And then we've got an inefficiency term, which I would say is  
[01:25:47] maybe in the range of 30%.  
[01:25:50] So this alpha is going to be something like  
[01:25:59] 1/10.  
[01:26:00] And this β here is actually the same.  
[01:26:02] It's a third.  
[01:26:03] It's one third times 30%.  
[01:26:05] So it also equals 1/10.  
[01:26:11] If both of them are one in ten, that kind of implies that there's  
[01:26:13] never a backward pass on RL?  
[01:26:15] Yeah.  
[01:26:15] Okay, we can make this 2/10.  
[01:26:17] Make it a bit bigger.  
[01:26:20] Just write it out once more, this is 2/10, this is 1/10.  
[01:26:27] The number of inference tokens you have is just a function of hundreds  
[01:26:32] of millions of tokens per second times my model is deployed for two months  
[01:26:37] before I ship to the next version.  
[01:26:40] That should determine  
[01:26:45] the number of tokens in RL and pre-training.  
[01:26:48] I guess we didn't do the equivalence between pre-training  
[01:26:50] and RL, so we'll do that here.  
[01:26:52] Data in pre-training should be equal to 2/10 data in RL for  
[01:26:57] them to be cost equivalent.  
[01:27:03] Sorry, 1/10.  
[01:27:04] I got it backwards.  
[01:27:06] We pay more cost when it's inefficient, so this needs to be 1/10.  
[01:27:15] Tracing this back… This thing ends up actually being, as written here…  
[01:27:21] This is like 1.5, and this is one.  
[01:27:28] Billions of dollars worth of compute just flowed in the other direction.  
[01:27:31] Right?  
[01:27:33] I think if you do it with a spreadsheet and actually model  
[01:27:35] it out, you might notice when the money’s going down the drain.  
[01:27:42] All of these end up being close in, as modeled here.  
[01:27:45] This 30% may have been a little bit too generous.  
[01:27:47] So let's say something like 1.5 here, and leave this as a one here.  
[01:27:53] I think at this point, you can almost read it off.  
[01:27:56] The number of inference tokens should be about the same as the number of  
[01:27:58] pre-training tokens, which should be about the same as the number  
[01:28:00] of RL tokens, within factors that we're not able to reason about.  
[01:28:08] Sorry for making a basic algebra mistake.  
[01:28:09] It seems like there should be fewer RL tokens than pre-training tokens?  
[01:28:12] That's in general right.  
[01:28:13] Because RL is less efficient in terms of machine time,  
[01:28:22] if you're trying to equalize the RL and pre-training time, then  
[01:28:24] you should have fewer tokens in order to have the same wall time.  
[01:28:28] This is all quite interesting.  
[01:28:31] I never thought about it in terms of equalizing data.  
[01:28:35] I think starting with equalizing in cost is right, but depending  
[01:28:39] on how you model the cost, this comes close to equalizing in data.  
[01:28:42] So for GPT to be trained optimally, every single user who uses GPT-5,  
[01:28:51] the total amount of tokens that they stream should equal the total amount  
[01:28:53] that has gone into pre-training.  
[01:28:54] And the total amount of tokens that have gone into pre-training  
[01:28:58] is the sum of all human knowledge.  
[01:29:01] Each model should generate the sum of human knowledge on the  
[01:29:04] output that it gets on the input.  
[01:29:06] Yeah.  
[01:29:07] Which way are people going to err?  
[01:29:08] If you think that people's power of prediction is not perfect, and also you  
[01:29:14] run the risk that you make a model that is not a frontier model and then you  
[01:29:19] just throw it away, then that changes the cost trade-off because there's some  
[01:29:26] probability that applies to the inference.  
[01:29:28] And you should derate the inference tokens by some amount.  
[01:29:30] Right.  
[01:29:31] Can we back out how much more compute than Chinchilla optimal  
[01:29:37] for a given sized model?  
[01:29:40] I think we just have to make some real-world assumptions here in order to do  
[01:29:45] that.  
[01:29:46] The inference tokens, we should totally be able to count, right?  
[01:29:49] Let's say a few hundred million.  
[01:29:51] Maybe it's five hundred million tokens a second now, I don't really know.  
[01:29:56] Five hundred million tokens a second times.  
[01:29:58] A model is deployed for two months before it becomes obsolete?  
[01:30:02] I  
[01:30:05] can't do this in my head.  
[01:30:06] Can you type it into a computer?  
[01:30:08] 2.6 x 1015.  
[01:30:15] Okay.  
[01:30:15] 2.6 x 1015.  
[01:30:20] This number is probably too large because this is going to  
[01:30:23] be multiple models in a family.  
[01:30:25] Let's make it  
[01:30:30] 5x smaller or 10x smaller or something  
[01:30:33] like that.  
[01:30:35] So we're estimating maybe fifty million tokens per second, per specific model.  
[01:30:41] The model is live for two months.  
[01:30:46] This comes out to around two hundred trillion tokens.  
[01:30:50] And then we want to compare that to active parameters on a frontier model.  
[01:30:55] I don't actually know the latest rumors.  
[01:30:57] Do  
[01:31:00] you know?  
[01:31:01] Somebody told me a hundred and fifty trillion.  
[01:31:03] Active parameters?  
[01:31:04] Sorry, I meant tokens.  
[01:31:06] Trained on a hundred and fifty trillion tokens.  
[01:31:07] Interesting.  
[01:31:08] Which is similar.  
[01:31:09] That's actually similar.  
[01:31:11] So data on pre-training.  
[01:31:12] This is not well-cited but it’s fine.  
[01:31:17] I think often the number of active parameters  
[01:31:21] could be in the range of  
[01:31:30] a hundred billion, something like that.  
[01:31:31] Maybe a bit larger.  
[01:31:31] So multiply by 20 to get the Chinchilla token count.  
[01:31:34] So Chinchilla, DChinchilla, would be around two trillion.  
[01:31:43] We see we're about a hundred times larger than that.  
[01:31:47] What does DChinchilla actually mean?  
[01:31:48] The token count for pre-training  
[01:31:53] that the Chinchilla scaling law would recommend, I guess.  
[01:31:56] Oh, I see.  
[01:31:57] So how much is it over-trained?  
[01:31:59] Got it.  
[01:32:00] The ratio of this two hundred trillion or a hundred trillion parameters over the  
[01:32:07] Chinchilla optimal of two trillion, that's the amount it's over-trained.  
[01:32:10] Which is a factor of a hundred over-trained.  
[01:32:12] A hundred.  
[01:32:14] So if you consider this right here, to the extent this is in the right  
[01:32:16] ballpark, just by thinking about how you want everything to be equal in terms of  
[01:32:22] compute… If OpenAI also realizes that and they're serving a certain amount of  
[01:32:28] tokens per second, that tells you how much data went into the pre-training of GPT-5.  
[01:32:34] Even if it's 50% off or something, it is wild that you can first-principles  
[01:32:40] these kinds of numbers.  
[01:32:41] This is why you should just approximate everywhere, because  
[01:32:44] there are big error bars on this.  
[01:32:45] But it's kind of empowering to just set A equal to B and figure it out.  
[01:32:49] That's super cool.  
[01:32:51] Okay, so in the spirit of trying to deduce things, we can publicly look  
[01:32:56] up the API prices of these models, and maybe we can learn something from that.  
[01:33:03] First, with longer context, Gemini 3.1 is 50% more expensive if you go over 200k  
[01:33:15] tokens than if you're below 200k tokens.  
[01:33:21] At a high level, I understand why that might be, but why specifically  
[01:33:26] 50%?  
[01:33:27] Why specifically 50%?  
[01:33:30] The high level, even in the first place, is that there is some amount of  
[01:33:36] increasing cost with context length.  
[01:33:42] We can bring that back up.  
[01:33:43] That was  
[01:33:46] the memory time versus the compute time.  
[01:33:50] We've put up these same equations from before, of the time for memory  
[01:33:54] fetches which is the weights and the KV cache, and then the time for  
[01:33:58] the compute which is just the matrix multiplications for the weights.  
[01:34:03] I will also draw the cost curve, but this time I'll do it as a function of  
[01:34:05] context length instead of batch size.  
[01:34:05] So this is the cost curve as  
[01:34:13] a function of context length.  
[01:34:26] We'll draw the compute.  
[01:34:28] The cost of the compute is actually constant as a function of context length.  
[01:34:31] There's no dependence here on context length.  
[01:34:33] In reality, there is some dependence, but it is very mild, so we'll ignore it.  
[01:34:38] So this is the time for the compute.  
[01:34:48] Then we'll also draw the dependence of the memory fetch on context length.  
[01:34:53] This starts at a large number for the weights and then grows  
[01:34:56] gradually with the context length.  
[01:35:00] Maybe starting here, and then grow gradually with context length.  
[01:35:04] And  
[01:35:09] so, you take the maximum and you see there is this inflection point here.  
[01:35:13] So this is the cost that Gemini might be paying.  
[01:35:18] And then you think, how might you put a pricing structure on top of that?  
[01:35:23] You would like to ensure that no matter what the context length  
[01:35:25] is, you are still profitable.  
[01:35:30] So we've got a two-tier pricing structure.  
[01:35:31] Maybe we've got something that looks like this up to some extent.  
[01:35:36] I think it says something about, given that the bump is at 200k, it  
[01:35:41] probably means that this is somewhat aligned with this crossover point.  
[01:35:44] Maybe not exactly aligned with it.  
[01:35:47] We can actually probably even complete that calculation just  
[01:35:50] to see where it lands out.  
[01:35:53] We can solve for the number of bytes per token if we make some assumptions  
[01:35:58] about the number of active parameters.  
[01:36:01] So solving for the number of bytes per token, we're going to assume  
[01:36:05] the point where we equalize the time of memory and the time of compute  
[01:36:08] is at, let's say, 200k tokens.  
[01:36:12] So we equalize these two.  
[01:36:14] We're also going to assume that the batch size is large enough that the memory  
[01:36:20] time spent on weights is negligible.  
[01:36:22] So we'll forget about this, and we'll focus on the actual  
[01:36:25] memory time spent on KV cache.  
[01:36:29] That ends up saying, copying this term over, batch times length of context times  
[01:36:36] bytes per token over memory bandwidth  
[01:36:44] is going to be equal to the number of activated  
[01:36:49] params over FLOPs.  
[01:36:54] And then we're going to solve for bytes per token.  
[01:37:18] Batch size was missing here.  
[01:37:20] It shows up here, and then it cancels out by the time we get to here.  
[01:37:28] And I dropped the length of context.  
[01:37:35] So we can plug in numbers.  
[01:37:36] This is the reciprocal of the number that we saw before.  
[01:37:40] This is 1/300, which is reasonably stable across many different hardware platforms.  
[01:37:47] We conjecturally said that maybe the number of activated  
[01:37:50] parameters is a hundred billion.  
[01:37:54] The length of the context we said was 200k.  
[01:37:59] Something is wrong here, though.  
[01:38:01] Length of the context should  
[01:38:20] be on the denominator, not the numerator.  
[01:38:22] 1667. Almost two kilobytes.  
[01:38:23] That is plausible, actually.  
[01:38:27] You said around two kilobytes.  
[01:38:35] Let's just do a sanity check for what this could be.  
[01:38:38] There are two mechanisms that people do attention with a  
[01:38:42] small number of bytes per token.  
[01:38:44] One is dense attention with a lot of reuse across layers.  
[01:38:50] Character AI has a blog post talking about that, alternating long and short context.  
[01:38:56] In the Character AI kind of model, which also showed up in the Gemma  
[01:38:59] models, the global context—which is really what we're talking about  
[01:39:03] here—was shared across all the layers.  
[01:39:06] To get this to kilobytes, you could get that, for example, as  
[01:39:09] a dhead of 128, which is typical.  
[01:39:14] Then  
[01:39:16] the number of bytes is typically the number of attention layers  
[01:39:26] times two times dhead times the number of KV heads.  
[01:39:39] This is the number of unique contexts per layer.  
[01:39:43] Do you share the context across many layers, or do you use it only once?  
[01:39:49] In the Character AI-like models, this number is one.  
[01:39:54] We said this is 128.  
[01:40:00] This is a choice which typically ranges from one...  
[01:40:03] Sorry, this is KV heads, I meant.  
[01:40:06] The difference between a head and a KV head is that…?  
[01:40:08] The KV heads are the heads that are stored in memory, store the  
[01:40:13] contents of the previous tokens.  
[01:40:14] The Q heads are the retrieval heads.  
[01:40:17] They're only used temporarily and they’re used by the attending token.  
[01:40:23] In this autoregressive context, I've got KV heads associated with all  
[01:40:26] of the contexts, and then Q heads associated with this new token here.  
[01:40:30] But this head, the  
[01:40:36] 128.  
[01:40:37] Oh, sorry.  
[01:40:37] This d-head is the dimension of the vector.  
[01:40:39] The  
[01:40:41] number of KV heads is typically in the range of 1 to 8.  
[01:40:47] It is totally plausible to get this by, for example, having 8  
[01:40:50] KV heads and a d-head of 128.  
[01:40:52] That gives you exactly this number.  
[01:40:54] Or you could have fewer KV heads, but more layers.  
[01:41:00] This is one way to get there via dense attention.  
[01:41:02] There's also a way to get there via sparse attention, where you  
[01:41:04] increase all of these numbers, but then you have a 1/sparsity term.  
[01:41:12] I think this number is plausible, if maybe a little bit small.  
[01:41:15] It's funny that they would leak so much information through their API pricing.  
[01:41:18] I mean, you are incentivized to price close to your costs because  
[01:41:22] otherwise someone could scoop you.  
[01:41:24] Maybe we can learn something about the difference in input versus output  
[01:41:26] prices, and what that tells us about decode versus prefill in these models.  
[01:41:33] I think last I checked it's 50% more expensive or something like that?  
[01:41:38] I don't remember.  
[01:41:39] What I've seen in the past is 3-5x more expensive.  
[01:41:42] Okay, that makes more sense.  
[01:41:42] So let's say it's 5x more expensive.  
[01:41:45] This is the compute to process the next token in decode.  
[01:41:50] Suppose you're doing prefill, where you're not just processing the most  
[01:41:54] recent token, you're processing all the tokens in parallel.  
[01:41:57] I want to say that it would be this times length prefill?  
[01:42:05] Or length of the pass in general.  
[01:42:10] If we can think of decode as being a pass with one, and then  
[01:42:13] prefill being a pass with many.  
[01:42:14] Okay.  
[01:42:16] So maybe prefix?  
[01:42:17] Okay,  
[01:42:20] memory.  
[01:42:22] You're not storing the KV cache for the tokens that are the prefill tokens.  
[01:42:28] Let's actually draw how prefill shows up here, if I may clarify.  
[01:42:33] We do a bit of decode like this.  
[01:42:37] We may actually come back and do more prefill.  
[01:42:40] If you think this is a chat session, the user says something, the AI generates  
[01:42:44] a response, and then the user says something else and we prefill this.  
[01:42:48] Maybe this is the general case, rather than this.  
[01:42:52] In fact, this is like you read a file or something.  
[01:42:54] Read a file or the AI is responding to a user input, tool call, or  
[01:42:58] anything that's not AI-generated.  
[01:43:01] Okay, suppose we're here.  
[01:43:11] You will have calculated all of this previously.  
[01:43:14] So just the KV of everything that came before.  
[01:43:19] But what is the memory cost of this?  
[01:43:22] Well, the  
[01:43:26] memory bandwidth cost of this.  
[01:43:28] If you're doing flash attention, it would—  
[01:43:31] It's basically temporary.  
[01:43:33] It doesn't even go to main memory.  
[01:43:34] Just ignore that.  
[01:43:35] Exactly.  
[01:43:35] So then it would just be everything that came before.  
[01:43:39] Is it not just that then?  
[01:43:41] There's actually no adjustment at all to the memory time.  
[01:43:42] Okay.  
[01:43:43] Great.  
[01:43:43] So it's a very trivial change to accommodate.  
[01:43:47] This  
[01:43:50] term is making it 5x more expensive.  
[01:43:52] Now, why would that be?  
[01:43:53] What  
[01:43:57] does that actually tell us?  
[01:43:58] What variable does this help us clamp?  
[01:44:00] The  
[01:44:05] only thing that could have changed is that the compute is  
[01:44:06] 5x more expensive as a result.  
[01:44:09] This is the time for one pass, but actually the amount of  
[01:44:12] tokens is that much larger.  
[01:44:14] We want the cost per token, in fact, or the time per token.  
[01:44:19] I'm not sure I understood.  
[01:44:20] This  
[01:44:24] is for processing the next token in prefix?  
[01:44:27] Well, actually for processing the entire batch.  
[01:44:31] At this cost, we have processed this many tokens, the length of prefill.  
[01:44:34] Or I guess the length of the pass.  
[01:44:34] Not this prefix, but it's this cost.  
[01:44:34] Okay.  
[01:44:34] Let's just do this pass.  
[01:44:34] So this is 5x more expensive.  
[01:44:34] Input is 5x more expensive.  
[01:44:34] Output is more expensive, in fact.  
[01:44:34] Output is 5x more expensive.  
[01:44:34] The result we want to work towards is that prefill is compute-limited and  
[01:44:34] decode is memory bandwidth-limited.  
[01:44:34] Why don't we do this?  
[01:44:34] Why don't we just chart it with len-pass  
[01:45:11] on the X-axis and t on the Y-axis.  
[01:45:17] We want the cost per token, so it'll be t over  
[01:45:22] length of the pass.  
[01:45:28] That'll be  
[01:45:32] right.  
[01:45:46] I  
[01:45:49] guess I’m getting confused by this.  
[01:45:50] Len-pass is... It seems like this should be higher when you're doing prefill.  
[01:45:56] Prefill has a bigger length pass.  
[01:45:57] Yeah.  
[01:45:59] But then why is it cheaper?  
[01:46:01] Why is the cost higher?  
[01:46:06] It's this division by length pass.  
[01:46:12] This is going to divide out, but then all of this is going to divide  
[01:46:16] by length of pass, and it's going to make the memory costs cheaper.  
[01:46:19] Okay.  
[01:46:21] Let me think about this then.  
[01:46:21] Basically we'll have four different lines.  
[01:46:22] Let's do  
[01:46:31] prefill first...  
[01:46:34] Actually, let's do decode first.  
[01:46:39] Length of the pass, when it's one, that is decode.  
[01:46:42] When it is bigger, that is prefill.  
[01:46:44] Oh, okay.  
[01:46:45] I see.  
[01:46:46] That makes sense.  
[01:46:47] Getting back to it.  
[01:46:48] So tcompute, if you have basically just this divided by  
[01:46:52] len-pass, so just this amount.  
[01:46:55] This actually does not vary based on t, so it'll just be some flat value like this.  
[01:47:03] And this is tcompute.  
[01:47:09] And  
[01:47:12] this is—  
[01:47:12] That's decode.  
[01:47:13] Decode.  
[01:47:13] Right.  
[01:47:15] Now tmem, we have this whole thing divided by len-pass.  
[01:47:18] Well, it doesn't really matter what's up there, it'll just be  
[01:47:21] something that looks like this.  
[01:47:25] Let's say this is tmem.  
[01:47:31] This is decode again.  
[01:47:33] So as the length of the prefix goes up, or pass, your memory bandwidth time  
[01:47:46] declines, and that means that to the extent that you were bottlenecked on  
[01:47:51] memory bandwidth before, you can avoid being bottlenecked on memory bandwidth.  
[01:47:56] The fact that they are charging 5x less for prefill than decode does suggest that  
[01:48:04] they are bottlenecked on memory bandwidth to quite a degree, such that for them at  
[01:48:08] least—because t is equivalent to cost, it's the cost of renting a compute—this  
[01:48:16] would be at 1, and this would be at 5.  
[01:48:18] That's right.  
[01:48:20] So it is, in fact, tremendously memory bandwidth bottlenecked.  
[01:48:23] The real graph looks something like  
[01:48:29] that.  
[01:48:30] It still crosses, but yeah.  
[01:48:32] Exactly.  
[01:48:33] Let me do it this way.  
[01:48:35] This is  
[01:48:44] the gap on decode between the memory and the compute time.  
[01:48:50] Okay, interesting.  
[01:48:52] Another interesting one would be why cache hits are so much cheaper.  
[01:48:58] If I remember correctly, cache hits are like 10x… It's more expensive  
[01:49:02] to write to cache according to the pricing on all these models.  
[01:49:06] But if you do hit a cache, it's  
[01:49:13] 10x.  
[01:49:15] Presumably, this is the cost of keeping something in HBM  
[01:49:19] rather than just evacuating it.  
[01:49:22] But if you do keep it in HBM, then it's cheaper to load again?  
[01:49:25] Right.  
[01:49:26] There are two ways you can produce the KV  
[01:49:30] cache for a token.  
[01:49:31] You can just produce it from scratch by computing it from the  
[01:49:34] underlying token IDs, which are tiny.  
[01:49:37] Or  
[01:49:40] you can previously have produced it and stored it in a memory  
[01:49:45] somewhere.  
[01:49:45] The cost ratio is really talking about the ratio between those  
[01:49:48] two mechanisms of producing it.  
[01:49:49] A cache miss means you've deleted it from all your memories, and you have to  
[01:49:53] recompute it from the tokens directly.  
[01:49:55] You can even take that a step further and think about which  
[01:49:59] memory tier you store it in.  
[01:50:01] You could store it in HBM.  
[01:50:03] There are other slower and cheaper memories than HBM, like DDR  
[01:50:07] on your host or flash as well.  
[01:50:11] One of the things you can do is a calculation of where it makes sense to be  
[01:50:17] in each memory tier, and this is related to how long you're going to store it for.  
[01:50:24] We want to look at the cost of storage in a few different memory tiers and  
[01:50:27] also the cost of rematerialization.  
[01:50:32] Remat means the cost to rebuild all of the KV cache from scratch after you  
[01:50:38] deleted it, so we rematerialize it.  
[01:50:42] Basically, this is going to cost the length of the context.  
[01:50:48] Actually, we'll look at the cost per token, so we don't need to carry around  
[01:50:52] this length of context everywhere.  
[01:50:54] To rematerialize one token of KV cache, I just need to run a  
[01:51:02] forward pass on the whole model.  
[01:51:07] This is going to be the compute time.  
[01:51:08] I have to rerun the compute at whatever speed my GPU does it, and then I  
[01:51:13] multiply it by my GPU dollars per second.  
[01:51:19] Sorry, excuse a naive question.  
[01:51:21] Why is there not a quadratic term?  
[01:51:24] There is a quadratic term.  
[01:51:27] It shows up in the compute.  
[01:51:35] As an approximation, I chose to remove it.  
[01:51:39] I'll just show you quickly what that looks like.  
[01:51:42] If you look at the  
[01:51:47] cost per token, or the number of FLOPs per token, there are the FLOPs  
[01:51:52] that are coming from doing the weight matrix multiplies as a function of—  
[01:51:56] Which is flat.  
[01:51:56] ...context length.  
[01:51:58] And then there is the number of multiplies that comes from doing the  
[01:52:01] KV cache, which goes up linearly with the amount of stuff you attend to.  
[01:52:07] The slope on this is so low that when you draw it like this, it's very  
[01:52:11] well approximated by a flat line.  
[01:52:15] You start to notice the effect of the quadratic or the linear term  
[01:52:18] up in the millions of tokens or so.  
[01:52:20] So it's just not super relevant.  
[01:52:22] So what is the reason that there's no company which has over a million  
[01:52:26] token context length, if this is true?  
[01:52:30] There are two costs of long context.  
[01:52:31] One is the memory bandwidth cost, which we've spent a lot of time analyzing.  
[01:52:34] That's this thing.  
[01:52:37] The other one is the compute cost.  
[01:52:39] The compute cost is almost always forced by  
[01:52:45] fundamental principles to be a much smaller slope than  
[01:52:49] the memory bandwidth cost.  
[01:52:52] The primary things that limit you to really large contexts are memory  
[01:52:56] bandwidth and memory capacity, which is exactly this effect.  
[01:53:01] There's this idea that Dario said on the podcast, and others have said, which  
[01:53:04] is, "We don't need continual learning for AGI, in-context learning is enough."  
[01:53:09] If you believe that, then you have to think that we have to get to a  
[01:53:12] hundred-million-token context length to have an employee that is the equivalent  
[01:53:17] of working with you for a month.  
[01:53:19] Now, maybe that's no longer true with sparse attention or something.  
[01:53:25] But if you think that, then some ML infra thing would have to change to  
[01:53:29] allow for a hundred million, like the memory bandwidth, to allow for a  
[01:53:33] hundred-million-token context lengths.  
[01:53:36] Sparse attention gives you a get-out for sure, because you get this square root.  
[01:53:40] It gives you a big improvement.  
[01:53:46] But if you look at the history of context lengths of models,  
[01:53:54] from earlier models like GPT-3, maybe to GPT-4—I don't remember when the  
[01:53:59] transition happened exactly—they shot up from about 8K to 100-200K.  
[01:54:04] And then for the last year or two, they've all been hovering around there.  
[01:54:08] I think that indicates that this is the reasonably balanced cost  
[01:54:13] point, and going massively beyond that would be cost-prohibitive.  
[01:54:17] Not because of the compute cost, because of the memory bandwidth...  
[01:54:19] Because of memory bandwidth cost, yeah.  
[01:54:24] I actually don't see a very good path to solving that.  
[01:54:29] The HBM is where it is.  
[01:54:34] It's not getting hugely better.  
[01:54:35] And why doesn't sparse attention solve it?  
[01:54:38] Sparse attention is a big improvement.  
[01:54:39] Maybe that is priced in already, perhaps.  
[01:54:44] It's not an infinite improvement because if you go too sparse,  
[01:54:47] you lose too much quality.  
[01:54:49] The empirical result is that the context lengths haven't been increasing that much.  
[01:54:53] I think it's because there is no solution to the memory wall here.  
[01:55:00] Going too sparse just means you're attending to a very small subset of the  
[01:55:03] tokens, and the quality will get worse.  
[01:55:05] Makes sense.  
[01:55:05] What is the cost of these different ways of  
[01:55:10] resynthesizing the KV cache?  
[01:55:13] Computing it from scratch is based on my GPU time.  
[01:55:15] I have to do a certain amount of multiplies, of GPU time  
[01:55:18] that I spend in order to  
[01:55:22] produce it.  
[01:55:25] Storing in  
[01:55:30] HBM.  
[01:55:33] This really goes as my  
[01:55:36] bytes per token.  
[01:55:39] I need to just have some number of bytes per token, and then I  
[01:55:44] need to store this in the HBM.  
[01:55:46] It's going to use up some of my HBM capacity.  
[01:55:50] A way to think of this is that if I have too many of these things  
[01:55:55] sitting in my HBM, if I fill up my HBM with just KV caches that I'm  
[01:55:59] not using, I can't use that GPU.  
[01:56:02] How do I price that?  
[01:56:03] Maybe I say that the cost of it is proportional to the  
[01:56:06] fraction of the HBM I'm using.  
[01:56:08] There's also times GPU dollars.  
[01:56:14] Let's just do one more memory tier and say  
[01:56:17] store in DDR instead.  
[01:56:23] The same kind of thing goes up for flash and for DDR.  
[01:56:27] I put these in the wrong columns.  
[01:56:29] I meant to make two columns.  
[01:56:32] The distinction I want to make is that there is the cost to  
[01:56:35] retrieve, and then there's a cost to  
[01:56:46] hold on.  
[01:56:49] This is a cost per second, whereas this is an instantaneous cost.  
[01:56:55] Rematerialization has a cost to retrieve and has zero cost to  
[01:56:58] store it because we've deleted it.  
[01:57:02] This is the one that I put in the wrong location.  
[01:57:04] This is actually the cost just to hold on, so I will rewrite it.  
[01:57:27] If we're just storing it in HBM, it has this sort of cost profile.  
[01:57:30] If  
[01:57:34] we store in DDR, it's actually going to take some time.  
[01:57:38] We get the same thing here:  
[01:57:41] bytes per token over DDR capacity  
[01:57:47] times DDR cost per  
[01:57:53] second.  
[01:57:53] But now this has a cost to retrieve that is higher than the HBM because  
[01:57:58] we need to copy it into the HBM.  
[01:58:00] So this is bytes per token  
[01:58:06] over  
[01:58:09] DDR bandwidth.  
[01:58:11] And then this consumes some amount of the DDR as well.  
[01:58:14] And every scale-up has DDR and flash?  
[01:58:17] This is really a deployment question, so you can choose that.  
[01:58:20] Nvidia does deploy in this form.  
[01:58:23] It has both.  
[01:58:24] Why isn't the cost to retrieve HBM  
[01:58:28] the bytes divided by memory bandwidth?  
[01:58:30] It depends what you define a retrieve to be.  
[01:58:32] Here, I'm defining retrieve to be, move it into HBM so that you can  
[01:58:37] start actually doing inference on it.  
[01:58:40] Because if it's already in HBM, you can be doing compute while  
[01:58:43] you're getting it from HBM to SRAM?  
[01:58:44] Interesting.  
[01:58:44] Yeah, for example.  
[01:58:47] These are three things, and I guess I ordered them wrong.  
[01:58:50] In general, if you're balancing two costs and you've got different  
[01:58:54] tiers in the memory hierarchy, you should expect as this cost  
[01:58:58] goes up, this cost should go down.  
[01:59:01] You can kind of see where the zeros are.  
[01:59:06] I should have ordered them this one first, this one second, and this one third.  
[01:59:12] If you're going to hold onto it for a very short amount of time, then all of  
[01:59:18] this is multiplied by the hold time.  
[01:59:24] This one is, and so is this  
[01:59:29] one.  
[01:59:29] Interestingly, they have different prices to write for.  
[01:59:32] Do you specify this in the API for five minutes versus an hour?  
[01:59:38] Which suggests that the five minutes is HBM and the hour is DDR.  
[01:59:41] I think that's a pretty good assumption.  
[01:59:44] If you look at the numbers, it might also turn out that it's one tier  
[01:59:47] down, and it's DDR versus flash.  
[01:59:50] Interesting.  
[01:59:50] I'll look up the price difference.  
[01:59:59] The base input tokens is $5 per million tokens.  
[02:00:04] Base, which means remat.  
[02:00:04] This is $5.  
[02:00:05] That's $5  
[02:00:08] to "retrieve".  
[02:00:12] And then to write,  
[02:00:21] presumably HBM, for five minutes is 6.25.  
[02:00:25] We might be able to determine which memory tier it is by the durations.  
[02:00:35] Five minutes versus one hour.  
[02:00:37] Exactly.  
[02:00:37] I think this will probably end up being  
[02:00:42] the drain time of the memory tier that you're in.  
[02:00:45] What that means is,  
[02:00:49] given that I know I'm going to be holding something for  
[02:00:51] five minutes, I would like to  
[02:00:55] pick a memory that I can read every five minutes.  
[02:00:58] I can read the whole memory once per five minutes, ballpark.  
[02:01:01] That is the drain time of the memory.  
[02:01:02] So if I take the storage capacity over storage bandwidth,  
[02:01:11] I would like this to be equal to five minutes.  
[02:01:16] We did this calculation for HBM.  
[02:01:17] For HBM, we know that this number is 20 milliseconds.  
[02:01:21] So HBM is much  
[02:01:26] too small.  
[02:01:27] DDR could be about an order of magnitude or two off from this, so  
[02:01:30] this is probably on the order of  
[02:01:34] seconds, like 1 to 10 seconds.  
[02:01:40] I don't have these numbers memorized, but generally, as you go to  
[02:01:42] slower tiers, flash is plausibly on the order of one minute.  
[02:01:46] And then spinning disk, which is massively different, is on the order of one hour.  
[02:01:52] So this might actually identify the tiers of flash and spinning disk.  
[02:01:57] Sorry, why is this the calculation?  
[02:01:58] This is the storage capacity divided by the bandwidth?  
[02:02:02] You've got a bunch of different memory tiers, we've listed four of them.  
[02:02:08] Your choice of which memory tier is about minimizing the cost.  
[02:02:15] What fraction of the device are you using?  
[02:02:20] You're using some fraction of the device for holding onto it, and  
[02:02:22] then you're using some fraction of the device to retrieve it.  
[02:02:27] Let's say I'm using 10% of the device.  
[02:02:31] And I want to equalize those two fractions.  
[02:02:33] That's a sign that I've hit the right thing.  
[02:02:36] Let's say I've got some runtime here.  
[02:02:39] I'm going to hold on for all of this time,  
[02:02:43] so this is the time-hold.  
[02:02:47] And then there's going to be some amount of time here, which is time-retrieve.  
[02:02:55] Basically to equalize these two costs, I want the retrieval time  
[02:03:00] to be equal to the hold time  
[02:03:06] times the fraction of capacity.  
[02:03:13] Because this is the retrieval time, this is how many other  
[02:03:18] things I can hold simultaneously.  
[02:03:20] Basically,  
[02:03:22] you want to store things in there for so long such that the amount of  
[02:03:28] time it's in there is the time to get all your things in there and out.  
[02:03:32] Yeah basically.  
[02:03:33] I think that probably indicates that the two tiers are flash and spinning disk.  
[02:03:38] I'm kind of shocked to see spinning disk being used at all, because  
[02:03:41] it's such an old technology.  
[02:03:43] Interesting.  
[02:03:44] It’s also crazy that it’s so slow that it takes an hour to  
[02:03:46] load its full capacity to it in.  
[02:03:48] It’s a really unattractive technology but it’s useful in some places.  
[02:03:52] We're sitting down because I want to ask you some questions  
[02:03:54] that don't need a blackboard.  
[02:03:56] You have this extremely interesting blog post where you talk about how,  
[02:04:01] at a high level, the architecture of different cryptographic protocols  
[02:04:05] looks a lot like neural networks.  
[02:04:08] There's this convergent evolution where they both need to jumble  
[02:04:11] information across all their inputs.  
[02:04:13] For cryptographic protocols, it's to make sure that each new  
[02:04:17] input into a hash function will totally scramble what happens.  
[02:04:20] For neural networks, of course, they need to consider how this piece of  
[02:04:25] information changes what you should make of this other piece of information.  
[02:04:29] I thought that was an extremely interesting point.  
[02:04:32] At a high level, in some sense they're trying to do the inverse thing.  
[02:04:38] Cryptographic protocols are trying to take information which has structure and make  
[02:04:43] it look indistinguishable from randomness.  
[02:04:45] Neural networks are trying to take things which look random—protein  
[02:04:51] sequences, DNA, garbled text—and extract higher-level structure from it.  
[02:04:58] They have similar high-level mechanisms, but they're actually  
[02:05:01] trying to do the opposite things.  
[02:05:04] I wonder what you make of that.  
[02:05:10] I try to look for other examples where mixing and scrambling shows up as well.  
[02:05:14] There's almost a physical example where you're making a cake and  
[02:05:19] you want to stir the batter.  
[02:05:21] Literally the idea to first stir it this way and then stir it this  
[02:05:23] way is not too bad of an approach.  
[02:05:26] Beyond that, back to the digital world,  
[02:05:31] there are some differences, and the one you call out is  
[02:05:34] a pretty strong difference.  
[02:05:37] The way it shows up,  
[02:05:43] if you just randomly initialize a neural network, maybe it's a reasonable  
[02:05:48] cipher as well because the random initialization is going to jumble  
[02:05:51] stuff in a complicated way.  
[02:05:52] It may even do what you want.  
[02:05:53] Who knows?  
[02:05:56] The thing that makes it interpretable is the gradient descent.  
[02:05:59] You can differentiate a neural network and get a meaningful derivative.  
[02:06:04] We do a lot of work to not overcomplicate the derivative, so the residual  
[02:06:10] connection keeps it contained and simple.  
[02:06:14] And so does the LayerNorm stuff that we do.  
[02:06:18] One of the biggest attacks against cryptographic ciphers is also  
[02:06:21] to differentiate the cipher.  
[02:06:22] Ciphers  
[02:06:26] run in a different number field.  
[02:06:27] They run in the field of two elements, so just binary, whereas neural nets run,  
[02:06:34] in theory, in the field of real numbers.  
[02:06:38] You have to differentiate with respect to binary numbers, but you  
[02:06:43] can absolutely differentiate a cipher.  
[02:06:46] This is called differential cryptanalysis.  
[02:06:50] Basically, what it says is that if you take a small difference of the  
[02:06:52] input, it's quite difficult to make the difference of the output be small.  
[02:06:58] The whole job of a well-designed cipher is to make the  
[02:07:01] difference in output very large.  
[02:07:04] The distinction is that the optimization goals at that  
[02:07:07] point are about complexifying.  
[02:07:10] They don't have the same residual connections, like LayerNorms.  
[02:07:14] I guess a place where the two merge is  
[02:07:22] backdoors.  
[02:07:22] With a backdoor in an LLM, you're trying to hide… Would you consider it an  
[02:07:27] input?  
[02:07:28] It’s not an input into the forward pass but it’s an input into the backward pass.  
[02:07:31] You’re trying to hide an input into the backward pass.  
[02:07:34] This is an adversarial  
[02:07:39] context?  
[02:07:39] This is actually a place where you get exactly the avalanche  
[02:07:44] property that ciphers have as well.  
[02:07:49] Adversarial attacks on image classification models are about finding  
[02:07:56] a very small perturbation of the image that totally changes the classification,  
[02:07:59] totally changes the output.  
[02:08:01] That is the common case in ciphers, whereas that's the  
[02:08:02] undesired case in neural nets.  
[02:08:02] Interesting.  
[02:08:02] Has it at all been a successful field to actually use neural networks as ciphers?  
[02:08:02] Almost anything you do in trying to create a cipher, if it doesn't have 10  
[02:08:02] years of scrutiny, it's probably broken.  
[02:08:02] So in that direction, it's a little dangerous.  
[02:08:03] In the other direction, there has been at least one very  
[02:08:03] clear adoption of technology.  
[02:08:03] There is a construction where you take a function, an f[x] function,  
[02:08:03] which is not invertible, and use that to build an invertible function.  
[02:08:03] That started in ciphers.  
[02:08:03] It's called a Feistel cipher or Feistel network.  
[02:08:04] You apply the function f—I want to write on the blackboard but I won’t—remember  
[02:08:05] the input, and then you swap the two.  
[02:08:06] That allows you to construct invertible layers.  
[02:08:06] There is a paper from 2018 or 2019 called Reversible Nets, RevNets,  
[02:08:06] which does exactly this construction.  
[02:08:06] In addition to your residual connection, you also remember the  
[02:08:06] input from the previous layer.  
[02:08:06] That actually makes the entire layer reversible and almost  
[02:08:06] completely eliminates your memory footprint during training.  
[02:08:06] Instead of needing to save activations for the backwards pass, you can  
[02:08:06] run the entire network backwards and rematerialize the activations.  
[02:08:07] Ok, so I was asking you,  
[02:08:10] have neural networks actually been used for cryptography?  
[02:08:13] And we realized it may be better to just do this on the blackboard.  
[02:08:18] Are they actually being used for cryptography?  
[02:08:20] Using neural nets for cryptography… In general, creating a new cipher  
[02:08:26] is a very dangerous proposition.  
[02:08:27] Almost all of them are broken.  
[02:08:29] 99% of them are broken, so it’s probably a bad place to start.  
[02:08:34] But the other direction has been, in at least one very  
[02:08:38] clear case, quite productive.  
[02:08:41] There's a construction  
[02:08:44] that exists in ciphers and then was imported into neural nets called a  
[02:08:48] Feistel cipher, or Feistel network.  
[02:08:51] The idea is that you may have some function f which is not invertible,  
[02:09:00] but you like the function because it does interesting things, like  
[02:09:03] it does an MLP, for example.  
[02:09:06] Or it mixes it in an interesting way.  
[02:09:08] You'd like to build something out of this that is invertible.  
[02:09:11] The construction we're going to make is going to be a two-input function  
[02:09:13] rather than a one-input function.  
[02:09:15] We're  
[02:09:19] going to apply  
[02:09:22] f[x].  
[02:09:25] We need to actually remember what x was, so we're going to stick x over  
[02:09:28] here so that we can work backwards, and then we also can't drop y.  
[02:09:33] We're going to remember y, and we're going to add them together to form this tuple.  
[02:09:36] The way to invert this, if you think I have  
[02:09:43] this output and I want to recover x and y, I can easily recover x.  
[02:09:47] That's right there, I just read it off.  
[02:09:49] To recover y, if this thing was called z, I can recover y by z minus f[x],  
[02:09:58] because I've already recovered x.  
[02:10:01] That means this construction is invertible.  
[02:10:06] This was used in ciphers a ton and still is used.  
[02:10:08] It's one of the main mechanisms of constructing ciphers.  
[02:10:11] Often you want ciphers to be invertible, especially the layers of ciphers, because  
[02:10:16] that has better cryptographic properties.  
[02:10:16] This has actually been  
[02:10:20] ported over  
[02:10:24] into neural nets.  
[02:10:25] There's a 2017 paper called RevNets, reversible networks.  
[02:10:32] What it does is make the entire network invertible.  
[02:10:34] You can apply it to any network, like a transformer network.  
[02:10:38] I do a forwards pass, but then I can run the entire pass backwards as well.  
[02:10:42] The whole neural network is invertible with exactly this construction.  
[02:10:48] This paper applied it to some layer, like a transformer layer, for example.  
[02:10:53] We've got this function f, which is our transformer layer.  
[02:10:57] Normally we would have just an input and then a residual connection  
[02:11:01] coming out, and it gets added  
[02:11:06] over here.  
[02:11:08] Now, the variation of this is going to be we've got two inputs, x and y.  
[02:11:20] x goes through the function, gets added to y,  
[02:11:28] and then this becomes the new x, output x.  
[02:11:34] Then this x becomes the output y.  
[02:11:40] Really what this is doing, if  
[02:11:44] you think of two layers back, is the thing you mentioned before.  
[02:11:48] It's doing the residual connection from two layers back.  
[02:11:52] This y came from the previous layer and was the residual connection there.  
[02:11:56] Because of this construction, the whole thing is invertible.  
[02:12:00] Why do I care?  
[02:12:00] What does invertible matter for?  
[02:12:02] The big thing that it can be interesting for is training.  
[02:12:05] If I think of a forward pass of training… Let's say I have four layers and I run  
[02:12:10] them in zero, one, two, three order.  
[02:12:13] I have to write all of the activations to HBM.  
[02:12:19] I get an HBM footprint here that is kind of linear  
[02:12:24] in the number of layers.  
[02:12:30] This can actually be the largest memory footprint during training.  
[02:12:35] This is normal training, and then I run the backwards pass and read it in reverse.  
[02:12:39] The  
[02:12:41] forward pass goes forward, and the backward pass goes backwards.  
[02:12:43] I have to read them back out.  
[02:12:46] The idea of this RevNets paper is that because it's invertible, I  
[02:12:51] don't need to store this at all.  
[02:12:52] I can completely rematerialize it.  
[02:12:56] I run my forwards pass, and then when I'm running my backwards pass,  
[02:12:59] I'm simultaneously in lockstep undoing all of the forwards pass  
[02:13:03] steps that I did in order to have the activations that I need here.  
[02:13:08] This ends up being memory saving, which is a nice idea.  
[02:13:11] Interesting.  
[02:13:12] In some sense you're spending more compute to save memory.  
[02:13:15] That's right.  
[02:13:16] Interesting.  
[02:13:17] It's the opposite of what you're doing with the KV cache.  
[02:13:20] With the KV cache, you're spending more memory to save compute.  
[02:13:23] Yeah.  
[02:13:25] Spending more memory to save compute is generally profitable  
[02:13:27] given where hardwares are.  
[02:13:29] Interesting.  
[02:13:30] That was super fun.  
[02:13:32] Reiner, thank you so much for doing it.  
[02:13:33] I feel like it really vindicated the vision behind  
[02:13:36] the studio and the blackboard.  
[02:13:38] Yeah.  
[02:13:38] Cool, thanks so much for doing it.  
[02:13:39] Thanks.  
