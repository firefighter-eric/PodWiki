# AI researchers debate how close we are to recursive self-improvement

[00:00:00] Today, I’m chatting with three of my AI researcher friends  
[00:00:03] from whom I learn a lot every time we talk. They also happen to be at somewhat open-ish  
[00:00:08] labs and companies, so you guys can actually say things on the record.  
[00:00:12] I’m joined by Beren Millidge, who is the CTO of Zyphra, which is developing open source models.  
[00:00:16] John Schulman is the chief scientist at Thinking Machines, previously a co-founder of  
[00:00:20] OpenAI, and led the RLHF work that led to ChatGPT. And Charlie O’Neill is head of  
[00:00:27] model training at Baseten. The first question I have:  
[00:00:30] If we’re in 2036 and we don’t have billions of crazy superintelligences running around that have  
[00:00:38] radically transformed the world, what is the most likely reason that doesn’t end up being the case?  
[00:00:43] Other than exogenous political shocks, or there’s a war, or they ban AI or something.  
[00:00:49] What is the most likely technical reason that 2036 isn’t a crazy alien superintelligence world?  
[00:01:00] There’s been a classic thing, almost like Moravec’s paradox, where we think of the AI as,  
[00:01:06] "If it can do this, it’s going to be amazing." If it can solve these hard maths problems,  
[00:01:09] if it can win at chess, blah, blah, blah… Then it solves these things, and it’s not that impactful.  
[00:01:13] Obviously, it’s somewhat impactful, but not everything.  
[00:01:15] If somehow that continues, and there’s never the true spark of generalization that occurs,  
[00:01:21] I think that could lead to the AI just being extremely good at everything that people put  
[00:01:26] into a benchmark or put into an environment. But there’s still some persistent sim-to-real gap  
[00:01:30] which is somehow blocking everything. I think this is unlikely.  
[00:01:33] We do actually see this kind of generalization even from RL in practice already.  
[00:01:37] But if it is just ridiculously hard to generalize meta-learning, plus we don’t solve continual  
[00:01:42] learning and it’s just super hard and impossible… This would be my default scenario in that case.  
[00:01:48] I agree with that. Humans have a lot of advantages over models now.  
[00:01:54] Each time a new model comes out, it’ll catch up in some of these areas.  
[00:02:00] But you end up getting bottlenecked by the places where the model is weaker and where  
[00:02:06] it has worse judgment, or the models can’t check themselves well enough.  
[00:02:12] There’s this cycle that keeps repeating where a new model comes out and people are  
[00:02:17] blown away and they’re like, "This is it. This is AGI." But then they use it a bit,  
[00:02:21] and it starts to feel dumb after a month or so. That cycle just might keep going.  
[00:02:27] It’s hard to predict how many times it’s going to repeat.  
[00:02:31] Right now, you don’t get explosive growth in capabilities because  
[00:02:36] you still get bottlenecked enough when you’re trying to do research and engineering.  
[00:02:40] Even if the model can write way more code than a person, it doesn’t make you 100X more productive.  
[00:02:47] So maybe there are just more of these cycles than we would expect.  
[00:02:52] For me, it’s a question of how far off the global optimum of "a learner you could have  
[00:02:58] on a chip" is from the transformer + RL, basically the current recipe.  
[00:03:05] People imagine that once you have an agent which is better than all humans at AI research,  
[00:03:12] even if it’s 0.1% better than all humans, then the fact that you can run hundreds of thousands, if  
[00:03:17] not millions, of these in parallel — and you can run them much faster as chips speed up — is going  
[00:03:20] to outweigh every other bottleneck. You’re eventually going to hit this very  
[00:03:25] fast takeoff with regards to self-improvement. I could imagine that if we continue along the  
[00:03:29] trajectory that we’re currently on with that paradigm, where it’s basically self-attention,  
[00:03:35] RL, scaling up RL environments… Think about what happened with Moore’s law.  
[00:03:41] We had this very nice straight line and that held for a really, really long time.  
[00:03:45] But there were so many discrete discontinuities and innovations that had  
[00:03:50] to happen to keep that scaling law going. The same thing has happened with LLMs.  
[00:03:54] We had this pre-training scaling law, and then that was hitting diminishing returns.  
[00:03:59] Then we came up with RL and solved that, and then we got this new diminishing  
[00:04:02] returns curve to hit that made it keep looking like a straight line going up.  
[00:04:06] So if it requires another one of those discontinuities to solve,  
[00:04:11] I’m not sure that the current method of training LLMs with these RL environments,  
[00:04:15] even RSI-targeted RL environments, would be able to discover that discontinuity.  
[00:04:21] If not, we’re probably going to hit this asymptotic curve.  
[00:04:25] But do you think the discontinuity will be harder than anything that’s come since 2012?  
[00:04:31] If we had the answer to that, we’d kind of have the ability to implement it.  
[00:04:35] But maybe we should distinguish between a discontinuity which adds to the current paradigm,  
[00:04:40] which is cumulative — there’s something beyond the RL that we have to discover,  
[00:04:43] and maybe they’re capable of connecting the dots in that straight line — or, again,  
[00:04:49] how far off the global optimum are we? Do we have to go back and throw out  
[00:04:53] gradient descent and neural nets in general? I don’t think, if you continue to scale up the  
[00:04:59] current paradigm, an LLM, no matter how many LLMs you’re running, is necessarily capable  
[00:05:02] of discovering that if it’s too far away. The only hope really is if deep learning just  
[00:05:09] can’t get us to an AI which can at least dominate human research and human development,  
[00:05:17] including the human ability to come up with new paradigms and so forth.  
[00:05:20] Or, I don't know, maybe humans would also never have discovered the next learning architecture.  
[00:05:26] But to the extent humans could have discovered it eventually… But it just seems like… If you  
[00:05:32] just look at the progress that’s happened since 2012 till now, and you just continue  
[00:05:36] that on —I know it’s just been powered by huge amounts of compute scaling and so forth—  
[00:05:42] it would be weird if it just didn’t get to the point where it could dominate humans, at least  
[00:05:47] in R&D, especially over the next few years. Ryan Greenblatt was on the podcast recently.  
[00:05:54] He made this point that I’d be curious to get your thoughts on.  
[00:05:55] You could imagine, as AIs get more and more capable, that they’re capable of making progress  
[00:06:00] on simulations which incentivize getting better at not only AI R&D, but at science generally.  
[00:06:07] This is a thing that all the labs are targeting and many startups are targeting.  
[00:06:10] Another intuition pump is if you look at the Elo score of chess bots since the ’80s.  
[00:06:14] There’s a very linear increase in Elo over time. But there’s this huge discontinuity as they cross  
[00:06:20] the human range, from human experts always winning against AIs to human experts never winning against  
[00:06:25] AIs, as this linear increase in Elo happens. I agree with your point that so far, AI  
[00:06:31] capabilities have not been that big of a deal in terms of their end economic impact in the world.  
[00:06:36] But that is because they’re slowly rising in Elo relative to humans.  
[00:06:40] I agree it would be very surprising. The only way for this to not happen is if,  
[00:06:44] as you said, it somehow asymptotes just before. Because we’re already pretty close, in my opinion,  
[00:06:48] to where we’ll start crossing the human Elo score. So we’ll need to asymptote before that.  
[00:06:53] That’s the only way — in this scenario you pose where somehow  
[00:06:55] we’re sitting here in 2035 and everything is normal — for this to happen, I think.  
[00:06:59] The only other way is there’s some dramatic regulation on AI.  
[00:07:03] This is what I see as the most likely way for this scenario to happen,  
[00:07:05] actually, rather than a technical thing. I think there’s different kinds of research.  
[00:07:10] There’s research in the autoresearch style where the objective is already specified very cleanly  
[00:07:15] and you’re optimizing that objective. I think everyone is picturing that if  
[00:07:18] we continue along this path of making pre-training loss go down and making our  
[00:07:22] environments have the reward on them go up, that’s going to lead to improvement.  
[00:07:25] But maybe what Ryan is talking about is this much more open-ended type of science which  
[00:07:29] is required for paradigm shifts, where we can’t specify the objective, and the AIs are definitely  
[00:07:33] not able to specify that objective either. We have to be really, really careful about how  
[00:07:37] we specify objectives for any of these things. Maybe your point is that the nature of the  
[00:07:41] breakthroughs that have happened since 2012 is that we have found… In 2012,  
[00:07:45] people weren’t saying… I’m assuming, I don’t know, you guys were there.  
[00:07:49] Or at least John, you were there. But I was not.  
[00:07:51] I was in primary school. Actually, John, I’m curious  
[00:07:55] for your wisdom of the ages, or wisdom of being in the trenches way back when.  
[00:08:01] Presumably, a big breakthrough was realizing that next token prediction is the… You wouldn’t  
[00:08:06] have thought that the nanoGPT speed run is the thing to be optimizing for in 2014.  
[00:08:12] But now that we have come to this new paradigm, you would think to do a speed run on that and  
[00:08:16] have AIs get really good at that. But maybe there’s a next inner loop  
[00:08:20] to optimize that the AIs wouldn’t anticipate. There’s an outer loop of revenue or something  
[00:08:25] that eventually should be strong, but it’s a very slow outer loop.  
[00:08:30] In fact, I remember in the early OpenAI days having the intuition that just minimizing log  
[00:08:39] loss wasn’t going to get you to intelligence. Because the important bits are accounting for  
[00:08:46] such a small fraction of the loss that it was going to be overwhelmed by noise.  
[00:08:52] So just training a language model on next token prediction wasn’t going to learn the  
[00:08:58] interesting things you want it to learn. We needed to craft better objectives that  
[00:09:02] would put more emphasis on the important things. You can make all sorts of arguments for this.  
[00:09:09] You could say, "Oh, humans probably don’t learn how to model everything in our environment.  
[00:09:18] Most people can’t create a photorealistic reproduction of  
[00:09:23] some kind of scene they’ve looked at. So we must need a better objective."  
[00:09:30] But then it turned out that it just worked anyway. As you were pointing out, the inner loop,  
[00:09:35] even in current AI research, of post-training benchmarks or whatever, doesn’t necessarily  
[00:09:39] translate into what users like. Oh, yeah. The whole field relies  
[00:09:43] a lot on generalization and it’s very hard to predict when you’re going to get generalization,  
[00:09:49] or when you’re going to get some kind of out-of-distribution generalization.  
[00:09:52] We know that if you train on the task you care about, you’re going to do better.  
[00:09:56] But the most important advances are often types of generalization that we have no right to expect.  
[00:10:06] For example, from just pre-training on this very naive next-token-prediction objective  
[00:10:14] to various tasks of interest that require understanding of the input in some deep way,  
[00:10:24] or learning some skill from pre-training that’s very rare and not heavily represented.  
[00:10:32] Then also generalization from these verifiable tasks to less verifiable ones,  
[00:10:38] this is also a type of generalization that there’s no reason a priori to expect.  
[00:10:44] This is an interesting question, because one intuition pump you could have for why you  
[00:10:48] would see some sort of singularity very rapidly — without even scaling up the inputs to AI progress  
[00:10:55] that are not just AI labor — is that before every single 7-figure experiment you run, you spend an  
[00:11:02] equivalent amount of compute on AI labor. So you just have automated versions of you  
[00:11:08] guys spending a century thinking about what is the optimal experiment to run, doing small-scale  
[00:11:15] ablations, developing literally a century’s worth of theory, going back even before deep learning.  
[00:11:23] Before you decide what experiment to run, you’re doing extremely  
[00:11:25] optimal setting up of the experiment. Then you do a century of thinking after the  
[00:11:28] experiment is over, where you’re analyzing what happened and what the next experiment to run is.  
[00:11:34] If you think hard enough, you probably could have expected some of these things beforehand.  
[00:11:40] There is probably some very clever way to do a small-scale experiment that’ll  
[00:11:44] let you build the theory that then will generalize to the large-scale experiment.  
[00:11:48] So I would expect that we’re nowhere near the ceiling of how well you can do research.  
[00:11:53] I would imagine a future where AI is doing a lot of analysis and theory building,  
[00:12:05] spending a comparable amount of compute to the amount that you’re spending on the experiments  
[00:12:08] themselves, doing various kinds of analysis and building a theory around what we’ve seen so far.  
[00:12:15] I think there are really concrete examples of this when the objective is well specified.  
[00:12:20] All thinking can do is update your posterior based on the bits  
[00:12:24] that you’ve gotten since you formed your prior. You can’t gain any new bits from just thinking.  
[00:12:28] But when the objective is well specified and there is this data sitting around,  
[00:12:32] I imagine there will be this big speed-up in the current paradigm we’re in.  
[00:12:35] A good example of this is if you got an AI to think about the Kaplan scaling laws.  
[00:12:40] An AI at this point would have noticed, "Oh, they’ve just taken these intermediate  
[00:12:45] checkpoints and didn’t account for the annealing, and so this is wrong."  
[00:12:49] That would have been caught years earlier. We would have cut off a year or two of  
[00:12:54] progress just from that observation from an AI. Again, once the objective is well specified, which  
[00:12:59] is lower pre-training loss or whatever, there are many, many good examples where if you just thought  
[00:13:04] about it a bit more, you would have been able to cut down significantly on things that you’ve done.  
[00:13:09] So muP, and how learning rate scales with model size, and realizing that  
[00:13:13] model width is important in that as well. I feel like you can really back out a lot of these  
[00:13:18] things and cut off a lot of low-hanging fruit. I would imagine a 10x speed-up if our thing is  
[00:13:23] just, "Maximize the objective we’re currently on." But I don’t see how that generalizes at all  
[00:13:27] to coming up with the right objective in the first place.  
[00:13:30] Just thinking doesn’t necessarily buy you the right objective in the first place.  
[00:13:33] I think this is really the key question for any kind of very rapid RSI from current AIs.  
[00:13:40] How well can AIs generalize to learning their own objectives?  
[00:13:43] To have any kind of self-propelling automated loop, we need the AI to propose objectives,  
[00:13:47] optimize them, figure that out, propose a new objective, and have this not go off  
[00:13:50] the rails at any point for a long, long time. To come back to Moravec’s paradox, there might  
[00:13:55] be a case of Moravec’s paradox where we think this kind of autonomy and being self-encapsulated — so  
[00:14:01] we can think of what we should do ourselves and then go do it and have this loop — is super  
[00:14:04] easy because we always do this. Obviously, evolution needs to  
[00:14:07] create creatures that can survive by themselves for long periods of time.  
[00:14:10] And this just might be something that for some reason is really hard for the AI, in the same  
[00:14:14] way that locomotion stuff is really hard but math is super easy despite being super hard for us.  
[00:14:19] But doesn’t the time horizon increasing suggest that that’s—  
[00:14:21] Yeah, exactly. This is another possibility, but I agree, there’s no obvious evidence for this.  
[00:14:26] In fact, the fact that our agents are now super persistent and it’s quite easy to  
[00:14:30] do this is kind of evidence against this. But this would potentially be one of the  
[00:14:35] reasons why we just don’t get this immediate takeoff, if this is hard.  
[00:14:39] If you look back from 2012 till now — or maybe from when you started doing  
[00:14:45] your research till now — what part of all the innovations that have happened since that time,  
[00:14:53] including purely engineering ones, including purely conceptual ones, seems like the thing  
[00:14:58] that would be the last thing humans would have to do before AI totally automates AI R&D?  
[00:15:05] Probably just iteratively asking the right questions.  
[00:15:08] If you can get the AI to do any experiment, you still need to decide what experiments to do.  
[00:15:12] Right now I think AIs are not very good at this compared to coding the experiment.  
[00:15:17] Whenever we talk about research, they propose a bunch of miscellaneous  
[00:15:20] things which are very, very tiny steps. Or even going from DeepMind’s approach of,  
[00:15:24] "We’re going to solve intelligence by learning to play games at a superhuman level," to one  
[00:15:30] random researcher like Radford being, "I’m going to try and just predict the  
[00:15:34] next token of a very wide swath of data"… Even once Radford had discovered that,  
[00:15:40] it took a while before people decided to scale it up, because we had to come up  
[00:15:43] with the idea of scaling laws and the fact that you could very reliably predict these things.  
[00:15:47] I would say that the last job for humans, or the role for humans that’ll last the longest,  
[00:15:55] is defining the objective and deciding what we actually want.  
[00:16:03] In that vein, something like deciding how the AI assistants should behave, or what it means  
[00:16:12] to be helpful, or what the objective is when we’re doing RL from human feedback, is one such thing.  
[00:16:19] Then later, defining constitutions and model specs is another one.  
[00:16:25] Even if the AIs can do all the technical work, we’ll still have to do a lot of that  
[00:16:29] and decide what we actually want. Alignment is the final job.  
[00:16:33] Alignment is sort of the answer. But alignment itself can be decomposed into  
[00:16:41] specification of the objective, or figuring out what the right objective should be, and then  
[00:16:47] actually achieving or optimizing the objective you’ve defined.  
[00:16:52] I think the first one is not going to go away anytime soon.  
[00:16:57] If I think about a post-training team and why you need a lot of people on the team,  
[00:17:05] it’s just because there are a lot of different areas where you have  
[00:17:09] to figure out how the model should behave. It would be very hard to automate the whole thing,  
[00:17:19] just because someone has to think about how the model should behave in this area.  
[00:17:24] Jane Street started using Antithesis to test its software in early 2025,  
[00:17:28] and the team was so impressed by the product that it decided to invest in the company.  
[00:17:32] I recently caught up with Ron Minsky, who co-leads Jane Street’s tech group,  
[00:17:36] to ask how Antithesis actually plugs in. The thing that I think is most impressive  
[00:17:40] about Antithesis is that we started using it on a team that was building  
[00:17:44] high-assurance software and being really careful. Nonetheless, it was able to shake out bugs that  
[00:17:50] were otherwise going to be really hard to find. That’s important both because it helps make  
[00:17:54] those systems more reliable and because it helps the teams that build them move faster.  
[00:17:59] This matters more and more as code production is increasingly automated.I think, in general,  
[00:18:03] as we’ve been using agents more and more, the key problem you run into is the verification  
[00:18:08] bottleneck: just the time it takes for people to look at code and figure out,  
[00:18:12] is that actually something you want to accept into your production software?  
[00:18:16] Tools that make testing better are just incredibly helpful there.  
[00:18:19] They ease the verification bottleneck and make it possible for you to get more stuff  
[00:18:23] done and move faster, because you can have more confidence that the code generated  
[00:18:27] by the agent isn’t introducing new problems. To see how Antithesis fits into your development  
[00:18:32] process, go to antithesis.com/dwarkesh. What is the story for why there isn’t huge  
[00:18:43] consolidation in model providers? There are just so many things  
[00:18:45] that point to centralization here. If you step back over the course of years,  
[00:18:51] is there something that is going to prevent that? I think distillation is the main thing that  
[00:18:57] fights against the centralizing force. Basically anything that can be learned  
[00:19:02] through RL can be distilled very easily, because it’s a small number of bits.  
[00:19:09] It’s something that you can learn from a small amount of data.  
[00:19:12] If you can get trajectories from the model that show a behavior, you can easily distill it.  
[00:19:20] I think distillation is one of the things that fights centralization.  
[00:19:29] There is also a possibility that there’ll be company-specific models, that it’ll be  
[00:19:34] possible to learn from deployment and have a company continually improving its own model.  
[00:19:42] Such a system could be provided by the current oligopoly of model providers  
[00:19:47] or some other currently smaller company. But I think that’ll change the game a bit.  
[00:19:54] I also want to point out that continual learning, honestly, doesn’t stop distillation.  
[00:19:58] Even if your model is improving every day, people could be distilling it every day.  
[00:20:02] The loops could just operate at the same pace. That makes sense. So copying model behavior…  
[00:20:10] I guess you need to know yourself what the right distribution to prompt is in order to  
[00:20:14] get the relevant model behavior? Oh, yeah. For just distilling  
[00:20:19] with supervised learning, the prompt distribution is extremely important.  
[00:20:23] It’s very non-trivial to distill a model, even if you have full access to it and have  
[00:20:28] the chain of thought and everything. It’s non-trivial to distill all of the  
[00:20:35] useful capabilities from it, because you need to prompt the model with something.  
[00:20:40] You need to prompt it with realistic prompts. You need to have a really wide  
[00:20:47] distribution of realistic prompts. One thing that’s been coming out recently is  
[00:20:54] that some of the Chinese companies are probably using these router services which are designed  
[00:20:59] to allow people in China to use the US frontier models, which would otherwise be blocked in China.  
[00:21:05] There are all these router or proxy services that allow people in China  
[00:21:09] to use these models, mostly for coding. And these router services are collecting  
[00:21:15] and selling some of the data. This is a very useful data set  
[00:21:20] for distillation because it gives you the perfect prompt distribution.  
[00:21:25] I think this is one of those things where AIs help a lot.  
[00:21:28] If you actually look at the frontier pipelines, or the Chinese models that  
[00:21:31] they’ve actually put in their papers, they get seed prompts from somewhere, which is some  
[00:21:36] combination of humans and this kind of data. Then they synthesize a vast coverage from  
[00:21:40] those seed prompts using their existing models or the other frontier models.  
[00:21:44] You can automate an awful lot of this prompt distribution gathering and environment creation.  
[00:21:49] Humans need to provide increasingly fewer bits as the models get better.  
[00:21:53] But it still seems you’re bottlenecked by having a service which has users going through it.  
[00:22:01] Not necessarily. That’s obviously very helpful, but theoretically,  
[00:22:04] you can just think about what users want. But the whole point is that the user says,  
[00:22:10] "Make me an application like this. Oh, that didn’t work. I actually want  
[00:22:13] you to make this new feature. But actually,  
[00:22:15] let’s step back and do this other thing." Capturing that whole trace is the thing.  
[00:22:19] Or to the extent you could have done that anyway, then you just have RSI.  
[00:22:24] Ultimately, if you have this fully automated loop, that is basically RSI.  
[00:22:28] The AI is deciding the data, it’s deciding the training.  
[00:22:30] That is the loop. But it depends how much human information you need.  
[00:22:34] At some point, if you’re just like, "I want traces that look  
[00:22:36] like this," you prompt that to the model. The model will be able to come up with a  
[00:22:39] pretty good approximation. But what if you want to do,  
[00:22:41] "Make me a really good politician," and then it has to anticipate de novo how a discussion in the  
[00:22:47] Senate halls would go or something? I just feel like there are going  
[00:22:51] to be a lot of things which are— Ironically, this is actually easier for  
[00:22:52] the distillers than the frontier labs. The distiller’s just like,  
[00:22:55] "I want a good politician." They go to the frontier model.  
[00:22:57] The frontier model already knows how to be a good politician, so it just generates those traces.  
[00:23:01] Whereas if you actually want to build the first model that does this,  
[00:23:03] you have to actually somehow get data on what politicians do every day and build that.  
[00:23:08] It’s actually much easier to say, "I want something like this," and then get the AI to  
[00:23:11] produce a billion variations, than to actually create the thing like this to begin with.  
[00:23:15] I think you can actually make a really concrete prediction based off this observation  
[00:23:20] that the Chinese labs have this router data. The thing that started this originally was I  
[00:23:25] was saying, "Isn’t it weird how Sonnet 5 and Opus 5 are almost objectively worse models  
[00:23:32] than GLM-5.3 and Kimi K3, even though they’ve had access to not only distillation but logit  
[00:23:37] distillation from Mythos?" The counter was that the  
[00:23:40] prompt distribution really, really matters. You need to see what users are doing so that you  
[00:23:45] can distill these behaviors and things in. I think the prediction from this is that the  
[00:23:50] frontier labs don’t necessarily have much of an advantage, if at all, in RL environments now.  
[00:23:56] Yes, user distribution matters for general behavior and so on, but the best measure  
[00:24:01] of a capability is the very, very hard RL environments you’ve made at the frontier.  
[00:24:05] If you have access to those RL environments as Anthropic,  
[00:24:08] and you have access to logit distillation, and you’ve still made a worse model, then maybe—  
[00:24:13] Then real-world deployment matters more than the environment.  
[00:24:15] That’s really interesting. But they had to incentivize those capabilities in the  
[00:24:20] first place in Fable, or the frontier model. So it’s weird that they can’t incentivize them  
[00:24:26] again with a smaller model or something. Maybe we’re just in this weird uncanny  
[00:24:32] valley where trying to copy that frontier model too much, the student-teacher gap,  
[00:24:38] whatever it is, is just too large. People have made this point with Opus.  
[00:24:42] The difference between Opus 4.6 and Opus 5 is that Opus 5 really feels like it’s  
[00:24:47] got this AI-as-a-judge checking every possible thing it’s done.  
[00:24:51] That’s why it uses so many tokens. It tries to think about all these things,  
[00:24:54] but it doesn’t necessarily have the big model smell of Fable to know when to stop doing that,  
[00:24:58] or when’s a good path to go down. The reach exceeds the grasp.  
[00:25:02] I would offer a slightly different hypothesis. I would say there are a couple of different axes  
[00:25:09] for the environments you can create. One of them is difficulty  
[00:25:13] and the other is realism. It’s comparatively easy to create a  
[00:25:19] lot of difficult environments that involve doing a much more complicated task or doing something that  
[00:25:29] requires a lot more cleverness. You could say this is the  
[00:25:33] benchmaxxing distribution, because a lot of the most prominent benchmarks just involve doing some  
[00:25:38] very hard puzzle-like task that’s easy to verify. Then there’s the realism axis, where you want the  
[00:25:45] model to be good in the realistic coding agent setting where there’s multiple back-and-forths  
[00:25:49] with the human and there’s multiple objectives. The labs who are crafting the model behavior for  
[00:26:01] the first time need to push in both directions. To get good model behavior, you need to really  
[00:26:05] push on the realism axis and have rubrics or some kind of human feedback that’s informing  
[00:26:12] the reward function you use there. But if you try to do distillation naively,  
[00:26:18] you end up just matching the teacher on the benchmaxxing distribution.  
[00:26:24] If you don’t have enough of the environments that really exercise the capabilities in these  
[00:26:30] trickier realistic settings, then you’re not going to get those into your student model.  
[00:26:36] I think maybe one thing that’s happening is the big models generalize better from the  
[00:26:42] tricky narrow tasks to these more realistic tasks. If you have a really good realistic prompt  
[00:26:52] distribution for distillation, you can match the big model really well.  
[00:26:56] But if you only have this distribution of easily verifiable tasks, then you can match  
[00:27:03] the big model on all the benchmarks, but you do worse on this broader distribution.  
[00:27:10] That might even explain something about the smaller Anthropic models, like Sonnet 5,  
[00:27:17] though it’s hard to predict exactly what they’re doing to post-train those models.  
[00:27:22] It could also be that they’re always changing their post-training stack, and they just got  
[00:27:28] a few things wrong in some of these models. I don’t know… they turned something up too  
[00:27:37] high and created some quirks that people really don’t like.  
[00:27:39] It’s really easy to screw up post-training in some way that doesn’t show up in benchmarks.  
[00:27:45] Just one other very basic point is that the frontier AI labs buy  
[00:27:50] all their data from big data companies. The Chinese can also just buy the same  
[00:27:52] data from data companies. And they are, right?  
[00:27:54] And they are. Exactly. There’s a lot of people being annoyed about this,  
[00:27:57] but if they have exactly the same data and they can buy that, they can also distill.  
[00:28:02] It means it’s quite easy to keep up, really. The other question I had is how the first  
[00:28:11] models that are capable of automating AI R&D will actually be trained.  
[00:28:15] There’s a toy version, which is this thing that Ryan was talking about.  
[00:28:19] You just have GPT-8 try to build GPT-3 size models that are really good at inner loop  
[00:28:26] type challenges: beating video games that require continual learning, or just getting to a certain  
[00:28:32] loss with the least amount of compute, et cetera. But John, I think you had an interesting point  
[00:28:36] that maybe that’s not the way it actually will happen in practice.  
[00:28:39] So I’m curious, by the point at which you have AIs that are actually capable of automating AI R&D,  
[00:28:44] how are they probably trained? We’ll probably do some combination  
[00:28:47] of learning from human feedback to absorb the researchers’ taste,  
[00:28:52] and just creating a lot of practice environments which involve doing multi-step research projects.  
[00:29:03] People will in practice do some combination of those two things and,  
[00:29:08] each iteration, patch whatever seems to be most broken in the last iteration.  
[00:29:14] Researchers will be using the AIs a lot and will notice that they have some consistent weaknesses.  
[00:29:23] Those things will either be patched by collecting human feedback or creating environments.  
[00:29:29] Maybe a useful way to think about this is how much of the lineage we  
[00:29:33] roll back and then let self-play from there. In the limit, you’re picturing just giving  
[00:29:38] them a GPU and maybe neural nets or something and saying, "Okay, figure out how to train  
[00:29:44] a model to do these particular tasks." The way it currently works is we go up  
[00:29:49] to the very edge of the lineage and say, "Okay, here are the bugs Anthropic has found in their  
[00:29:54] training stack in the last few months. We’ll turn those into environments."  
[00:29:56] You need to train and get better on the frontier.  
[00:29:59] So you obviously lock in all the previous history of the lineage.  
[00:30:01] But you could imagine a world in which you roll back to before GRPO or something.  
[00:30:06] Then you have environments which try to get it to discover the best form to RL models on, and  
[00:30:12] then maybe you roll further and further back… But I think we will still be so compute bottlenecked  
[00:30:16] that people will just keep staying at the frontier and essentially diffing the bugs and whatever  
[00:30:21] improvements they found since the last model version, turning those into training environments.  
[00:30:24] Which is also really good for having non-stale, new data between model generations.  
[00:30:30] Again, this is basically continual learning within the AI lab, of distilling the last three months of  
[00:30:35] AI research progress through environments and RLHF-type stuff back into the model itself.  
[00:30:41] And it is distilling. That’s maybe why some of us feel like it’s asymptotic.  
[00:30:46] You’re always just trying to get the last three months of progress.  
[00:30:50] That progress is being contributed to by AIs, of course, but it also still has humans in the loop.  
[00:30:54] It feels like you’re just constantly inching closer and closer to what the human researchers  
[00:30:58] are finding and capable of doing. The one thing I will say, though,  
[00:31:01] is obviously if you’re just distilling on trajectories, you can never go above it.  
[00:31:04] But environments can go quite a far way above what a human can do.  
[00:31:07] It’s very easy to design an environment that no human can solve, but the AI can  
[00:31:10] obviously still try and solve it. That would be the path to go ahead  
[00:31:14] of just what the human AI research is. Do you have an example in terms of RSI,  
[00:31:18] of what kind of training set? Nanochat speedrun, but doing it  
[00:31:21] even faster than a human speedrunner. I feel like in AI research especially,  
[00:31:24] it’s very easy to define goals. You could say the loss needs to be 1.3 or  
[00:31:29] something, and no human can get that now. But that’s an extremely measurable,  
[00:31:34] verifiable task. If the AI gets that, then great.  
[00:31:37] Or I don’t know, building a 100 million parameter model that beats Minecraft.  
[00:31:41] That’s maybe too easy, but beats a much more complicated game or something.  
[00:31:45] Isn’t it crazy that 100 million parameter models beat Minecraft?  
[00:31:48] We’re calling that too easy? Imagine if you said that five years ago.  
[00:31:52] I would say a lot of research is not exactly like that, though,  
[00:31:56] where it’s hill climbing on a well-defined goal. It’s more like, here’s an intuition we have about  
[00:32:02] some way models should be better. We also have some idea for an algorithm  
[00:32:07] that seems to go a little bit in this direction. So let’s come up with a task that is designed  
[00:32:15] to show signs of life on this approach, and see if we get those signs of life.  
[00:32:22] If we do, we can make successively more realistic versions of the task.  
[00:32:26] It’s a lot more guided by intuition. The inner loop is to test for that  
[00:32:35] intuition rather than the test itself leading to the insight.  
[00:32:40] Right. You’re not directly optimizing for the eventual objective you care  
[00:32:45] about or the practical production objective. You’re relaxing your objective a little bit.  
[00:32:54] You’re saying, "Let’s relax on the realism axis a little bit and find some methods that actually  
[00:32:59] work, and then try to get back to realism later after the method matures a little bit."  
[00:33:05] There’s also research that’s more oriented towards explaining things and developing a theory.  
[00:33:15] Often we don’t have mathematical theories in machine learning that are that predictive.  
[00:33:20] But we have a lot of more informal theories for what’s going on.  
[00:33:27] Presumably the models will be trained on some combination of all of these tasks.  
[00:33:30] Some will be very easily verifiable, some will be LLM-as-a-judge or just ask the human,  
[00:33:34] "Does this look reasonable?" The hope would be that these would  
[00:33:39] all generalize to these much harder, more vague, fuzzy kinds of tasks.  
[00:33:43] It probably will to some extent. Whether it generalizes enough that  
[00:33:46] the loop can become self-sealing without humans being in the loop at all is unclear.  
[00:33:51] Maybe taking a step back. Here’s what it seems to me  
[00:33:55] the plan for AI research going forward is. You tell me if you think it’s going to work  
[00:34:00] or if you agree with this characterization. The bet is that we will scale up RLVR training  
[00:34:08] across millions of diverse environments, across hundreds of different kinds of domains.  
[00:34:14] What will emerge at the other end is an agent which has learned these basic skills — or less  
[00:34:19] than basic skills — around being persistent, being able to triage information and context,  
[00:34:26] eventually having end-to-end optimization of working with other agents and things like that.  
[00:34:31] Such an agent will be very sample efficient within the context —you've done research on how you  
[00:34:36] scale up in-context learning to make it arbitrarily long, but you keep scaling it up.  
[00:34:40] And what comes out the other end will be something that basically functions like a drop-in remote  
[00:34:45] worker over the course of a week or a month. First of all, do you agree that that is  
[00:34:49] the bet the labs are making? And second, is that enough?  
[00:34:53] Basically learning how to learn within these simulacra within a data center,  
[00:34:58] and then getting deployed into the real world, but not actually learning from real-world deployment…  
[00:35:02] only learning these meta skills from the simulated environments in the data center.  
[00:35:08] I think it’s now hard to separate out how much of the labs’ effort is going  
[00:35:13] towards direct RSI versus making generally intelligent models that they can continue  
[00:35:17] to deploy to collect revenue to fund the next big training run.  
[00:35:20] For the latter, yes, that’s probably just the bet they’re making.  
[00:35:30] It’s very clear, the pattern of where these environments are going over the last few years.  
[00:35:32] Anthropic’s lineage of environments is a very clear example of this.  
[00:35:35] First, we just focus on coding and we’re going to get really, really good at that.  
[00:35:38] Then, from the task horizon that we’ve got from coding — which is probably the  
[00:35:42] lowest-hanging fruit in terms of data available on the internet to create environments, and  
[00:35:46] their own internal stuff that they can turn into environments — then we’re going to generalize.  
[00:35:50] We’re going to go up to finance next, and literally just so much Excel data and all  
[00:35:54] that sort of stuff in the RL training. Then it’s PowerPoints. It’s this long  
[00:35:58] tail of the working economy. That seemed to work really well.  
[00:36:02] A lot of the other labs, even the open source labs, have now realized  
[00:36:05] that that was the correct bet to make. But what is the implication from that?  
[00:36:07] When I had Dario on the podcast, the thing I asked him was, if you truly expect models which  
[00:36:12] will be human-like in their ability to learn on the job, why would you try to bake in all these  
[00:36:18] skills of working with PowerPoint or something? Wouldn’t you just expect the model to be able  
[00:36:22] to pick that up while it’s deployed? There’s multiple different explanations.  
[00:36:26] One is just that we expect models to get there soon, but they’re not there yet, so why not  
[00:36:31] amortize these skills into the model training? Another is that we’re not concentrated on making  
[00:36:38] it really good at widely deployed work. We just want it really good at RSI.  
[00:36:43] This is just a way for us to get revenue so that we can pour it back into a model that is actually  
[00:36:48] really good at doing RSI development. Then once the singularity happens,  
[00:36:52] the thing that comes out the other end will be really good at all the things which seem like  
[00:36:56] bottlenecks to the current generation of models. John, I don’t know if you have takes on  
[00:37:00] how one should construe why there is so much task-specific knowledge in these models if the  
[00:37:06] path is this kind of generalization. If the models were good enough at  
[00:37:10] learning in context, then in theory, you wouldn’t need to train them on finance.  
[00:37:15] They would just be able to read all the books on the fly and figure out how to do everything  
[00:37:22] in the appropriate jurisdiction. You could argue that you need to do  
[00:37:29] a lot of this domain-specific training just to make them more efficient.  
[00:37:35] Even if they were smart enough to figure this out on the fly, you still might want to do a bunch of  
[00:37:40] RL and bake all these intuitions into the weights, so the model would be more efficient at runtime.  
[00:37:49] In practice, it does seem like model providers are going domain by domain and trying to strengthen  
[00:37:55] the models in the highest value domains. I’d say that that’s one of the answers to  
[00:37:59] why the models have gotten so much better. It’s just because the model providers have  
[00:38:04] covered a lot of the high-value domains and the most common types of skills.  
[00:38:10] Another thing is just that it’s not that expensive to do both at the same time.  
[00:38:14] The models are massive. They can easily afford, in terms of their parameters, to learn everything.  
[00:38:18] There is likely some transfer. Even if finance is not specific,  
[00:38:22] the information is important for RSI. Just the general meta-learning of how to figure  
[00:38:26] out what’s important, how to have taste, how to do long-horizon work is potentially generalizable.  
[00:38:31] There’s not that much RSI data in the world as well.  
[00:38:34] It’s hard to generate and requires a lot of effort.  
[00:38:36] So if you can amortize in this other data, you get some transfer from it.  
[00:38:40] You already have masses of compute and masses of parameter space,  
[00:38:42] so why not do that as well as, obviously, the direct commercial intent of selling a model?  
[00:38:48] I’ll add that there’s one question about whether this current paradigm of doing  
[00:38:55] sim-to-real will be the dominant one forever. You look at what the real-world tasks are like.  
[00:39:03] Then you try to create a bunch of environments that can be simulated  
[00:39:07] in the data center, and you can do RL on them. Obviously, this has been very successful.  
[00:39:14] But it has a lot of weaknesses, because a lot of things are just hard to simulate,  
[00:39:19] especially if they involve interacting with a bunch of humans in real time.  
[00:39:25] So there’s some question about whether sim-to-real will be the dominant framework forever.  
[00:39:31] I think sim-to-real has to be the dominant framework while sample efficiency is low,  
[00:39:34] because right now you need thousands and thousands of interactions with the humans.  
[00:39:38] No human is going to sit there and be in the loop of RL training.  
[00:39:42] So we have to simulate that now to get the samples you need.  
[00:39:45] But obviously, if sample efficiency improves a lot, you’d expect learning from  
[00:39:48] deployment to become a much bigger part of it. Though there are also other things you could do.  
[00:39:53] You can learn off-policy, so you can take all the traces, and even without resimulating everything,  
[00:39:59] you can potentially learn something from them. Jane Street just launched a new competition,  
[00:40:03] and it’s its most ambitious one yet: design a protocol-emulator ASIC.  
[00:40:08] Basically, if you have a chip you want to test, you can connect it to this ASIC,  
[00:40:11] and the ASIC will simulate realistic traffic. That way, you can see how the chip responds  
[00:40:16] without having to plug it into a live system. Jane Street is looking for flexible,  
[00:40:20] general-purpose designs, not single-protocol emulators.  
[00:40:23] When I was chatting with them, they suggested that I start by trying to implement what are apparently  
[00:40:28] three very common protocols: UART, SPI, and I²C. Jane Street also mentioned that they hope more  
[00:40:35] ambitious designs will tackle low-speed USB, Ethernet, and any other protocols that flex  
[00:40:41] your chip’s specific architecture. Importantly, your design should be  
[00:40:44] reprogrammable rather than smashing a bunch of specific protocols onto a chip.  
[00:40:49] If a new protocol comes out after your ASIC is taped out, your chip  
[00:40:53] still needs to be able to handle it. How exactly it does that is up to you.  
[00:40:57] But there is one hard constraint: your design must target an open-source 130-nanometer process node.  
[00:41:03] That’s because Jane Street will pay to tape out the most novel submissions  
[00:41:07] and send physical copies to the winners. The competition is open until January 18,  
[00:41:12] 2027, and working in teams is highly encouraged. Go to janestreet.com/dwarkesh to download the  
[00:41:19] template code and get started. I want to ask more about this,  
[00:41:23] because it’s weird that you have 50% of compute that’s spent on inference that is  
[00:41:30] not directly helping the model become better. One of the key advantages you’d expect digital  
[00:41:35] minds to eventually have is that, unlike a human who gets to have 50  
[00:41:38] years of real-world experience, a model will get to experience, through all its instances,  
[00:41:45] millions of years of deployment across all kinds of economically relevant work in the economy.  
[00:41:51] Right now, that data is just not, in a meaningful sense, helping the model get better.  
[00:41:56] It seems so obvious that eventually models should be able to learn from this data.  
[00:42:00] Once they do, you would have something that almost feels like a widely deployed  
[00:42:03] intelligence explosion, because the model is assimilating so much information  
[00:42:07] across all these deployed instances. When do you expect this kind of hive-mind,  
[00:42:11] crazy shit to start happening? I think broadly, at a very basic level,  
[00:42:15] this is already happening… just in the next generation of models.  
[00:42:18] Right now, you can obviously take your deployment data and put this in the pre-train or the  
[00:42:21] mid-train of future models, especially if you do some kind of filtering or some kind of judgment  
[00:42:26] or annotation or synthesization of that. How much do you think that explains the  
[00:42:30] generation-over-generation improvement? I think it explains quite a bit.  
[00:42:35] I don’t know whether the labs do this, because theoretically, they claim not  
[00:42:37] to train on people’s data. But the Chinese 100% do.  
[00:42:41] They definitely get this advantage. This is basically what distillation is.  
[00:42:45] They take the models, they get some fraction of their deployment data by pinging the model,  
[00:42:50] and then they train their next generation of models on it.  
[00:42:52] They can certainly do it on their own models as well.  
[00:42:54] There’s no reason not to whatsoever. I completely agree with this.  
[00:42:56] If you zoom out far enough, this is definitely happening.  
[00:43:00] What we’re all picturing, the holy grail of continual learning, is this very organic,  
[00:43:06] live loop of an individual model getting an experience and live-updating on the  
[00:43:10] spot and learning from that. A lot of things break when you  
[00:43:13] zoom into that level of granularity. But the big labs are doing this.  
[00:43:17] The closed models are doing this. There are also early signs of life  
[00:43:19] of people using open-source models doing this at a much faster cadence.  
[00:43:24] A good example is probably Composer. Harvey’s doing the same thing with legal agents.  
[00:43:27] You have some sort of model, and you are getting very specific environments from the  
[00:43:38] data that you have for that particular task, and things that users are complaining about,  
[00:43:42] and all the feedback that you’re somehow extracting from your specific deployments.  
[00:43:46] A lot of these companies have the advantage over the big labs in that they  
[00:43:49] can use this data really, really well. Then they will create environments.  
[00:43:52] They will do a big post-train of Kimi K3. They will go deploy it.  
[00:43:57] They might do some online learning as well, like Composer did online…  
[00:44:00] basically REINFORCE for a long time. There’s still a human in the loop.  
[00:44:04] There’s still a human saying, "Okay, these are the signals we care about.  
[00:44:07] Here’s how we’re going to create environments from the data that we have."  
[00:44:09] It’s still a longer cadence than maybe the one that you’re thinking of,  
[00:44:12] but it really is happening. Eventually that loop will  
[00:44:15] become faster and faster. The Composer thing is interesting  
[00:44:17] because this is where, in Cursor, people press Tab or they don’t press Tab on the  
[00:44:24] next completion that the model suggests. Based on that, every single day, Composer  
[00:44:28] gets better at predicting the next— That was the old Tab model.  
[00:44:31] They actually did the same thing not just for the Tab model, but for the actual generative model.  
[00:44:35] Oh, I see. Interesting. It’s hard because when you do online  
[00:44:39] reinforcement learning, you don’t have groups. You just have one user saying one thing,  
[00:44:42] and then you get one rollout. So you have a big variance-reduction problem.  
[00:44:47] Cursor’s fuzzy answer to this was, "We have very good heuristics which are able to estimate how  
[00:44:53] much better than average this response was, or how much worse than average this response was."  
[00:44:57] Then they would do this big REINFORCE update. Their solution to whether it got worse or not  
[00:45:03] was that if it improved on CursorBench, they would deploy the new model every five hours.  
[00:45:07] If it didn’t, they would throw that version out. I think your biggest problem is actually  
[00:45:11] just not knowing what the reward function should be for natural data.  
[00:45:14] If you use some kind of superficial signal, like did they accept the edit,  
[00:45:22] that might get reward-hacked in some way. But isn’t this a bigger issue with the sim-to-real  
[00:45:27] thing, where the longer-horizon tasks get, the harder they are to simulate within a data center?  
[00:45:34] It seems to me that even in coding, we’re already getting to the point where there’s not some  
[00:45:42] year-long coding task that doesn’t eventually require you to talk to a client or interact  
[00:45:47] with the company or interact with users. If you think about the gamut of things we  
[00:45:51] would want AI to be capable of, eventually superintelligence should be able to run a  
[00:45:56] business, or start a new business and make it profitable, or have a profitable day trading  
[00:46:00] in the markets, or win a court case. These are all things which are very  
[00:46:03] hard to simulate in a data center. An inherent part of the learning  
[00:46:07] there is interacting with the real world. Maybe they learn how to get better at these  
[00:46:11] things from the transfer between sim-to-real. But alternatively, maybe you do need weight  
[00:46:16] updates from these kinds of interactions in order to get better at them.  
[00:46:21] If that is the case — if transfer isn’t strong enough and you do need weight  
[00:46:24] updates — then the fact that the models are quite sample-inefficient is maybe a deeper problem.  
[00:46:30] The reason I’m curious about this is that by default, I don’t see how  
[00:46:34] you don’t get some kind of crazy recursive self-improvement within the next 10 years.  
[00:46:39] But the one reason why that might not happen is that in terms of the sample efficiency of weight  
[00:46:45] updates, models just seem way far behind humans. They’re plausibly a millionfold behind humans in  
[00:46:50] terms of how much data a human sees from birth to adulthood versus how much a model  
[00:46:53] sees from cold start to finishing training. This is all to say, first of all, is there going  
[00:47:02] to be good transfer between simulations and the extremely long-horizon, really complicated real  
[00:47:05] shit that we want the AI to do in the real world? And if not, does that really mean that the  
[00:47:10] lack of sample efficiency in these models comes to bite us?  
[00:47:14] Maybe the way I’d break down the two types of tasks — the ones in which models get good  
[00:47:18] and the ones where models will still continue to struggle — is whether the task is cumulative,  
[00:47:22] or whether you have this non-stationary distribution where you have to keep  
[00:47:26] learning and relitigating a bunch of stuff. An example of a cumulative task might be RSI.  
[00:47:32] It’s theoretically possible to have a less-than-a-million-token Python file  
[00:47:36] which from scratch trains a model that is capable of recursive self-improvement.  
[00:47:41] Every discovery that you make is a line in the sand that you hold.  
[00:47:45] If it’s true that for RSI we don’t need to discover a new attention variant or whatever,  
[00:47:49] then once you’ve discovered attention, and once you’ve discovered mixture of experts,  
[00:47:52] and once you discover GRPO, you just add that to the training stack and that’s there.  
[00:47:56] A good example of this is 5.6 Sol training, 5.6 Terra, or whichever one OpenAI told us it trained.  
[00:48:03] It didn’t have to go back and discover attention. It basically would have called a bunch of  
[00:48:07] scripts, like pre-training.sh and post-training.sh, and just done that.  
[00:48:12] That’s an example of a cumulative task. I think the real world — and the reason  
[00:48:16] people are thinking so much about continual learning — is not really a cumulative task.  
[00:48:20] Imagine in a law firm, you have an agent acting as a legal associate.  
[00:48:25] That’s a very non-stationary distribution.  
[00:48:27] You have to be able to fit in your context all the relationships between  
[00:48:30] all the important people at that company, which are also changing all the time.  
[00:48:33] You have all these implicit ways about how things are done, where to find information, et cetera.  
[00:48:38] That’s not as clean an example of a cumulative task as RSI is.  
[00:48:43] I think there will be this breakdown between tasks.  
[00:48:45] But if the labs realize that — and they do believe that RSI is cumulative in the sense  
[00:48:50] that we don’t need to go back and discover some brand-new architecture or whatever — then maybe  
[00:48:54] more and more effort and compute gets focused on that versus the other tasks.  
[00:48:56] It’s so unfortunate that RSI happened to be easier than being a paralegal.  
[00:49:04] I would say today’s models are weaker than humans in a lot of different ways.  
[00:49:13] Some of them might have to do with sample efficiency in a certain regime.  
[00:49:19] In some regimes, models are very sample-efficient, like learning in context.  
[00:49:23] But then there might be some medium-length regime where they’re less sample-efficient,  
[00:49:27] because humans can do some kind of weight update more efficiently than models.  
[00:49:34] I think being less sample-efficient in certain regimes might be one of the sources of weakness.  
[00:49:41] But I think there are other sources of weakness that are completely different from that.  
[00:49:45] For example, having lower diversity of thought than humans, or being bad at  
[00:49:52] certain kinds of long-horizon judgments. I think a lot of what people call taste  
[00:49:58] is something about behavior that works in the long run, and that  
[00:50:05] people have realized works in the long run. Not everything, but some aspect of taste.  
[00:50:12] Especially for something like software engineering, I think a lot of taste is "What  
[00:50:16] are the systems that are going to be maintainable and work well in the long run of this project?"  
[00:50:25] There are a variety of weaknesses of models which limit RSI along with other things.  
[00:50:34] Some of them are related to sample efficiency, and some of them aren’t.  
[00:50:37] Maybe an interesting thought experiment is this. Let’s say you were able to give a model a context  
[00:50:42] window of a trillion tokens, or whatever you would have needed to fit in your  
[00:50:46] experience prior to, let’s say, RLHF. It’s got all that experience in the  
[00:50:51] context window, and it has the same sample efficiency and in-context learning ability  
[00:50:55] as it does at a million tokens. Do you think taste is then solved?  
[00:50:59] Would it be able to make the same judgments that you did?  
[00:51:02] Or is there something fundamentally missing, apart from just a longer context window with  
[00:51:05] the same sample efficiency? It would have to be trained  
[00:51:08] to learn from that context. Either it would have to be  
[00:51:16] trained to learn the right update to make from that context, or it would have to generalize.  
[00:51:22] So you don’t think you can just dump it all in, your whole life, your research experience?  
[00:51:26] You still need the data to train it on long context.  
[00:51:28] Even if you could theoretically get a trillion context, you would need a trillion lengths  
[00:51:31] of data to train it. Right now you have 10k context,  
[00:51:34] you can't just dump in a million. Yeah, I’m just asking if you had that.  
[00:51:37] In theory, I think, yes. This really just comes down to the  
[00:51:39] question of how meta-learnable taste is from shorter-horizon episodes.  
[00:51:44] I feel like there’s no obvious reason it’s super long, because humans somehow developed taste  
[00:51:48] without having many long episodes. We don’t live to be 10,000.  
[00:51:53] We develop pretty quickly. If you think about even a PhD, the difference between  
[00:51:57] a first-year PhD student and a final-year student or postdoc, that’s five years maybe.  
[00:52:02] They’ve only done maybe 10-30 research projects in total.  
[00:52:05] But somehow they develop taste quite quickly from a relatively short succession of small things.  
[00:52:10] Theoretically, it’s possible to develop it like that.  
[00:52:13] The AI obviously will have vastly more experience in which to develop taste, to meta-learn it.  
[00:52:18] Then the question is how well that generalizes to really long-horizon things, which I think is  
[00:52:22] really unsolved at this point. We don’t know.  
[00:52:25] Going back to this question, eventually there should be a regime where AIs are  
[00:52:29] learning a ton from each individual instance of deployment that they have.  
[00:52:33] Currently you could say there’s a fuzzy meta process  
[00:52:36] by which models do improve from deployment. But I feel like it’s a very weak feedback loop.  
[00:52:43] Do you see this on the horizon, where there’s this hive mind kind of learning that’s very rapid,  
[00:52:48] and if so, how exactly does it happen? I would say that whether we get a hive  
[00:52:55] mind that learns from all of its deployment experience is in a big part about incentives,  
[00:53:02] rather than being a technical question. Companies aren’t going to want to  
[00:53:08] have the model provider learn from all of their deployment, because that might just  
[00:53:13] reduce the advantage of their business. I think the economics of this will pressure,  
[00:53:20] not necessarily weight updates to one big common shared model, but modules that get subbed in.  
[00:53:26] A very obvious example of this is a LoRA, but it might be something else.  
[00:53:30] There’s been a lot of work to try and fit an arbitrary context length into a fixed size.  
[00:53:34] This is all the linear attention stuff. And cartridges, which are essentially  
[00:53:39] KV caches trained to be very, very compressed to fit in a lot of information.  
[00:53:43] That’s another example of something that companies may be willing to sign up for, if that gets  
[00:53:48] subbed into the model and it’s not actually changing the base underlying model itself.  
[00:53:53] There are many different versions of learning from your data in real time.  
[00:53:56] The latter ones are not really helping the big labs, because they are just these modules.  
[00:54:00] But I think the economic pressure will force the labs to go down that  
[00:54:06] path first before they can embark on this... Which economic pressure, though? I feel like  
[00:54:11] even if you have a bunch of cartridges or LoRAs or whatnot, you can still just  
[00:54:14] take all these traces and dump them into the pre-training of your next generation of models.  
[00:54:19] Yes. It may be a more indirect form of learning that the big labs are getting.  
[00:54:23] That’s obviously still really valuable to them. But I can’t imagine a world in which we start  
[00:54:26] off with, "We’re going to just directly train this one big  
[00:54:29] model on all the exact data that we’re getting." No, I think it will definitely go through stages,  
[00:54:33] because this is assuming there’s one discontinuous event where suddenly  
[00:54:36] we fix weight updates continuously. In practice, I think it’s much more  
[00:54:39] likely to be that the cartridges and stuff allow you to specialize in deployments.  
[00:54:43] Then you generate traces, you put that in your model, and three months later you come  
[00:54:46] out with a model which is better at this stuff. You specialize it again, you consolidate it again,  
[00:54:50] and then eventually we’ll just make this leap faster and faster.  
[00:54:52] Instead of releasing a model every three months, now it’s every week,  
[00:54:55] and then every day, and then every hour, at which point we’ve basically solved it.  
[00:54:59] I think this is a good point as well, because you asked how far off the current  
[00:55:03] paradigm we are from being able to do this. We’ve done a bit of research into this,  
[00:55:07] and people have done a lot of research. At a really large scale, when you wash  
[00:55:11] out enough noise and you have large enough batches, this outer-loop process  
[00:55:14] of putting data into mid-training and creating our own environments does work  
[00:55:18] in some sort of continual learning regime. But the problem is, when you zoom in close  
[00:55:21] enough at a micro level — I’ve got one model and I’m trying to update it again for a law  
[00:55:26] firm or something, and I’m trying to do that very continuously with a relatively small amount of  
[00:55:30] data — all the methods kind of break down a bit. If I SFT the model on just successful traces,  
[00:55:39] off-policy or on-policy, eventually in the very iterative regime, when you’re doing  
[00:55:44] hundreds of these micro-updates, you see catastrophic forgetting.  
[00:55:48] You see forgetting of previous information learned on top of the base model that was much earlier on,  
[00:55:53] and you see degradation of general capabilities.  
[00:55:58] On-policy distillation seems to push this horizon out a little bit, but it still  
[00:56:02] eventually succumbs to the same thing. RL is good at getting capabilities in,  
[00:56:09] but it’s not as good at getting knowledge in, this very explicit knowledge of, "Ah,  
[00:56:13] okay, this person does this at this law firm, and this is a very specific process we find."  
[00:56:17] You have to pour in a lot of compute to create the right  
[00:56:19] environments to get the knowledge in with RL. Do you think the fundamental issue here — why  
[00:56:23] you get worse at these other skills or there’s forgetting — is fundamentally an issue of capacity  
[00:56:28] or an issue of techniques? A little bit of both.  
[00:56:31] I think SFT and even on-policy distillation can be way too destructive.  
[00:56:38] The reason RL is so nice is because it changes a very, very small amount about the model.  
[00:56:44] There’s a lot of evidence for why this is the case.  
[00:56:47] It just tweaks it in this very, very small loss valley to get it into the right point.  
[00:56:53] But that also then limits what you can do with RL, how much you can actually change the model.  
[00:56:57] So you’re saying the reason this isn't a winner-take-all, potentially,  
[00:57:00] is that it is just very hard to distill that much information into the base model?  
[00:57:03] Without ruining something, in an iterative fashion.  
[00:57:06] It’s easy to distill it into a different base model.  
[00:57:08] This is where I think it’s mostly technique. It’s definitely not that there isn’t capacity.  
[00:57:13] If you had some model with all this data, and you take literally the same-size model and  
[00:57:17] pre-train it from scratch with all of the stuff in mid-training, it will be better.  
[00:57:20] I think that’s a lot of what’s happening today. There’s very much a bottleneck that stops us from  
[00:57:24] just keeping training the same model forever, versus just getting all the data from the old  
[00:57:28] model and training a new model from scratch. This is exactly as Charlie was saying:  
[00:57:31] some combination of plasticity and catastrophic forgetting.  
[00:57:35] If you just naively train on non-stationary data, because you’re adding new data as you go,  
[00:57:39] this is messing with the data distribution, so the old stuff is just forgotten.  
[00:57:43] We don’t really have good methods to stop that from happening.  
[00:57:46] So maybe in the limit you’re just bottlenecked by retraining the model  
[00:57:49] from scratch with all this new information. Yes, which of course is very expensive.  
[00:57:52] Training a model from scratch is expensive. But you’re going to do that anyways.  
[00:57:56] Not necessarily. Maybe eventually, if you have continual learning, you never train a new model.  
[00:57:59] You just have a model and it keeps learning and expanding.  
[00:58:02] But there might be some deep technical reason why that’s very difficult.  
[00:58:06] That’s the question. I think we have pushed back how much from scratch we need to do.  
[00:58:11] It is definitely possible now to take the pre-trained base and do  
[00:58:15] very good mid-training on top of that, kind of continuously, plus some RL from different  
[00:58:20] checkpoints that are later on in the training. That’s looking more like continual learning,  
[00:58:23] but it’s certainly not the case of taking the most recent model, applying a couple of very small  
[00:58:27] updates, and iteratively never losing anything. Sorry, but I’m a bit confused, because isn’t this  
[00:58:32] literally what happens during training? During post-training or something,  
[00:58:35] you have a model that’s already gone through so much training, and then you distill some  
[00:58:40] fork that’s been further RL’d. Isn’t that literally what happens?  
[00:58:44] But it’s still at a large enough scale, I think, that you’re washing out a lot  
[00:58:47] of the noise, and you’re not just focused on one distribution, which, as Beren said, is the issue.  
[00:58:53] If you’re just focusing on one task— But in the eventual regime you’d be doing…  
[00:58:59] There are billions of deployed instances. You’re learning from all of them at once,  
[00:59:05] so hopefully there’s some washing out of noise from that.  
[00:59:09] Maybe at that scale, yeah. As Charlie was saying,  
[00:59:13] you can definitely do continual mid-training for a long time, and you can roll back to a  
[00:59:16] checkpoint and give it new mid-training data. But at the same time,  
[00:59:18] you can’t do this indefinitely. If you just keep continually training the  
[00:59:21] same base forever, it asymptotes at some point. You can’t just learn new stuff in that base.  
[00:59:27] This is why people end up training new bases. Otherwise you would just keep mid-training  
[00:59:31] the same base forever. Whenever I finish recording  
[00:59:33] an interview, I immediately brain-dump all my thoughts into Slack—things like what was  
[00:59:37] most interesting and what should get cut. This ensures that my editors have all the  
[00:59:40] context they need to start editing the episode. But these brain dumps don’t have clear timestamps,  
[00:59:45] and my unedited recordings are many hours long. It can take a ton of editor time just to find the  
[00:59:52] exact moments I was referencing. So we decided to try adding  
[00:59:55] a Grok Bot producer to our chat. Now, whenever one of my editors posts  
[00:59:59] a rough cut of an episode, Grok Bot opens the transcript on its own computer and starts working,  
[01:00:04] usually before I’ve even seen the message. It takes the notes I dropped into Slack  
[01:00:08] and highlights the relevant snippets in the transcript.  
[01:00:10] It also uses a big case file I’ve compiled with all my preferences,  
[01:00:13] so it can suggest potential edits. When it’s done, it sends me its  
[01:00:17] top clip candidates so I can review everything from my phone.  
[01:00:20] This has worked really well. Being able to send informal messages,  
[01:00:23] like I’m texting my editor, and then have the transcript immediately reflect my  
[01:00:27] preferences has just been so helpful. Try Grok Bot yourself at x.ai/bot.  
[01:00:34] Let’s talk a bit about data now. I’m generally interested in this  
[01:00:38] question of how much of AI progress is just explained by data progress.  
[01:00:41] That doesn’t mean it will necessarily be hard to automate, but that's a separate question.  
[01:00:46] Is there some data distribution which, if you trained current architectures on it, would result  
[01:00:53] in a superintelligence that totally dominates human experts across every single field?  
[01:00:58] Are we talking about pre-training plus post-training data, environments as well?  
[01:01:03] I think the existence of this is obvious. It’s just whether we can create the right  
[01:01:07] environment to get there. In the trivial case,  
[01:01:09] we could just train it to output the Python file which trains the actual superintelligence.  
[01:01:12] Just have that memorized in the weights. Yes, there’s probably a ladder of RL  
[01:01:17] environments that is possible to construct such that you would get an AI researcher which is  
[01:01:23] at least as good as a human researcher. But the effort to climb each successive  
[01:01:28] rung grows kind of exponentially. Those are the two things you have to  
[01:01:34] trade off against as to how fast we’re going to hit that final rung where it’s better.  
[01:01:40] I think that’s fairly clear. We’re still relatively  
[01:01:44] early in RL environment creation. There are a lot of asymmetries that  
[01:01:47] we exploit in order to create good environments. One of the asymmetries which we’ve talked about  
[01:01:51] before is that there are environments where it’s easier to go backwards than forwards.  
[01:01:56] What I mean by that is, it’s very easy to define this complex data-generating process,  
[01:02:01] and this is the latent variable you keep hidden from the model.  
[01:02:04] You can generate arbitrarily complex environments, and the model has to do a lot of irreducible  
[01:02:09] token spend and irreducible work to figure out what that data-generating process was.  
[01:02:14] There are asymmetries in terms of injecting information from the real world.  
[01:02:18] Anthropic finds a bug through tens of thousands of humans and LLMs combined,  
[01:02:23] and turns that into a very, very neat environment which a single LLM could  
[01:02:26] theoretically find within a few million tokens. There are all these asymmetries which we’re  
[01:02:31] cherry-picking, and we’re counting on this kind of task-horizon generalization.  
[01:02:36] But I think it’s just going to hit diminishing returns at some point, diminishing returns in  
[01:02:41] how hard it is to create those environments in the first place, coming up with them, because  
[01:02:44] you can’t necessarily just have these processes where it’s easier to go backwards than forwards.  
[01:02:50] You actually have to sit down and construct something that looks like a long enough time  
[01:02:55] horizon with humans, and it’s going to be a really complex task to create.  
[01:02:59] Then there are also going to be the compute and time bottlenecks for the  
[01:03:01] agent to actually do those tasks. I think you’re just going to start  
[01:03:05] seeing this curve flatten out. I saw something about how someone  
[01:03:08] fine-tuned the Talkie model, which is only trained on data up to 1930, on modern coding agent data.  
[01:03:18] It did better than Claude 3 Opus on SWE-bench. So this model that has no knowledge of code  
[01:03:26] whatsoever can be fine-tuned on a moderate amount of data and  
[01:03:31] behave better as a coding agent than this much larger pre-trained model, which is pretty crazy.  
[01:03:36] It kind of shows you that once you have an example of the right expert behavior,  
[01:03:42] it’s actually surprisingly easy to copy that into a relatively weak model.  
[01:03:48] But a counterexample to that is a paper recently where they trained a model up to  
[01:03:53] fifth-grade maths, and also primary-school English and stuff, so it was a decent language model.  
[01:03:59] They tried to RL it to do late high school and college maths.  
[01:04:03] The gap was just too large. They couldn’t get it to climb at all.  
[01:04:06] But if you did successive rungs of year 7 maths and then year 8 maths… and so on,  
[01:04:11] you could obviously climb to year 12. Again, it’s just what is the distance  
[01:04:15] between the rungs on those ladders, and how hard is it to create?  
[01:04:18] This just comes back to the RL signal problem. RL is not very good at exploring right now.  
[01:04:23] If the model can’t get it in 128 rollouts, it’s very unlikely to get signal to progress.  
[01:04:28] This is why in RL we need curricula, whereas in pre-training we don’t, because that’s not  
[01:04:33] a problem for pre-training at all. Again, pre-training data is  
[01:04:37] different to post-training data. I imagine as we continue on, humans  
[01:04:42] will be involved less and less, but that doesn’t change the fact that you’re bottlenecked on how  
[01:04:46] much signal you can extract from the real world. There’s a lot of signal in the world,  
[01:04:51] and that’s true. There’s people doing  
[01:04:53] spreadsheet tasks, there’s people doing legal tasks and all this sort of stuff.  
[01:04:56] But at the capability frontier of where the models are at now,  
[01:05:00] how many bits in the world are actually really relevant to improving the model’s capabilities?  
[01:05:06] How many new maths problems are being solved that are just beyond  
[01:05:09] the reach or grasp of the current models? How many new coding problems are being  
[01:05:13] created or solved that are beyond the reach of the current models?  
[01:05:16] I think that’s why the diminishing returns kick in, because even the world as a whole is not  
[01:05:19] giving you the bits, going back to the start of this, that are useful for tipping you into  
[01:05:22] the next basin of capability. I totally agree with this.  
[01:05:26] It’s really a question of where the signal is coming from.  
[01:05:30] In pre-training, the signal is already in Common Crawl.  
[01:05:33] For the tasks that you care about in pre-training, the problem is not getting signal at all.  
[01:05:38] It’s filtering out all the noise that exists. That’s quite an automatable process.  
[01:05:41] But as the models get better, as we enter mid-training and post-training,  
[01:05:45] the signal just doesn’t exist anywhere in the original data we have.  
[01:05:48] No amount of filtering will get this. There’s no hidden proof of a Millennium  
[01:05:52] Prize problem sitting in Common Crawl that we can just filter until we see it.  
[01:05:56] At that point, you have to get bits some other way, either from humans directly, asking them  
[01:06:00] to write out their reasoning, or by creating environments where humans decide what environment  
[01:06:05] should be created and what the objectives of these environments are, or some kind of training on  
[01:06:10] the human data that exists in deployment. You have to get the bits from somewhere.  
[01:06:14] There’s a question of how much of the progress in pre-training is being driven by data.  
[01:06:18] I did this investigation with Jerry Han, who’s a student at Princeton, where we trained all  
[01:06:24] the recipes from 2019 till now pairwise with all the data sets from 2019 to now.  
[01:06:31] You’re training GPT-2 on the newest data set, like Ultra-FineWeb.  
[01:06:36] You train Delphi, which is the newest open source training recipe, on the Pile or some old data set.  
[01:06:42] You do the whole grid. You see, getting to some  
[01:06:48] level of capabilities, how much less compute does it take, across this grid?  
[01:06:52] You see that the data seems to explain something like a 12.0x compute efficiency  
[01:06:58] gain, but the architecture improvements explain something like a 3.7x compute  
[01:07:01] efficiency gain, at a very small scale. To the extent that that is true at large  
[01:07:06] scale — that most of the pre-training compute efficiency gains are coming from  
[01:07:10] better data — how much can that continue? Can you keep filtering data more and more  
[01:07:16] and building more and more synthetic data? Do you have a sense of how much this kind of  
[01:07:20] pre-training progress can continue? My prior is that, again, the  
[01:07:26] low-hanging fruit is somewhat exhausted. We got the internet as this big block,  
[01:07:31] and it’s not like the internet is necessarily growing at the same rate.  
[01:07:36] All the useful stuff on the internet isn’t growing at the same rate.  
[01:07:38] We’ve probably got a bunch of 0.1% loss drops to go, but definitely  
[01:07:42] not as many as have currently occurred. But it’s also really interesting that you  
[01:07:46] find this cumulative 33x improvement across both. I think it was Epoch or someone who estimated  
[01:07:53] 3x a year since 2019, which would imply something like 3⁷, over 2,000X improvement.  
[01:08:01] So where’s that missing 100x or whatever coming from?  
[01:08:05] That probably gives you a good signal of how much of this is post-training.  
[01:08:08] I think the explanation has to be that a lot of the compute efficiency gains are scale dependent,  
[01:08:14] and we’re starting at extremely small scale. That raises a question of whether the data compute  
[01:08:20] efficiency gains or the algorithmic compute efficiency gains have more scale dependence.  
[01:08:25] I don't know if you have a prior on that.  
[01:08:27] We just didn’t have enough compute to investigate that question.  
[01:08:29] Just naively, theoretically, the scale dependence of the architecture is fairly well known,  
[01:08:36] and you can fit a straight line to it. Whereas I would have no idea how to  
[01:08:40] do that for combining pre-training plus post-training data and mid-training data.  
[01:08:44] Funnily enough, I feel like data is actually more important with scale.  
[01:08:48] I feel like architectures are kind of a one-time thing.  
[01:08:53] Saying just an X% efficiency gain is kind of misleading, because what an architecture does is  
[01:08:57] let you reach a qualitatively new regime which you couldn’t reach with the old architecture.  
[01:09:01] Within that regime, obviously the data is the primary thing determining it.  
[01:09:04] But if we didn’t have even GQA, if we were doing full attention all day, it would be  
[01:09:10] ridiculously expensive to do a million context. Because of that, we could never use the data  
[01:09:15] which is actually at a million context, so we couldn’t get these capabilities.  
[01:09:18] Even though if you just do a naive "how much does this do at 2K context", where the architecture  
[01:09:23] isn’t unlocking anything, then the data will look much more important than in some sense it is.  
[01:09:27] It’s unclear to me that these things are really just multiplicative gains in this way.  
[01:09:32] I see. So what’s your take on the scale dependence of data?  
[01:09:37] On scale dependence, I think a lot of the mid-training and post-training data  
[01:09:41] we have now actually gets better with scale, because a lot of it — the very long context  
[01:09:46] horizon environment stuff — really requires big models to be able to make use of it.  
[01:09:51] If you try and train your 100 million parameter model on SWE-bench traces,  
[01:09:54] it’s not going to get anywhere. It’s not going to show you the  
[01:09:57] same kind of improvement that you would get if you train an actual sensible size model on it.  
[01:10:01] It’s hard as well now because so many of the architecture changes — you look at Kimi,  
[01:10:05] for instance, or DeepSeek — they’re doing these architectural modifications not just with dropping  
[01:10:10] the pre-training loss in mind, but with how the models are going to be used in the real world.  
[01:10:15] The inference efficiency, having some form of compressed attention in the DeepSeek models,  
[01:10:19] is not necessarily geared around a fundamental trade-off improvement.  
[01:10:23] It’s just, "Okay, we’re considering how the models are going to be used."  
[01:10:27] One question I’m curious about, to understand the future,  
[01:10:28] is how parameter scaling will go as we’re getting into more of an RL-heavy regime.  
[01:10:37] You can look at open source architectures and see how fast parameters have been scaling.  
[01:10:42] Maybe it’s roughly 2x every year for frontier open source models.  
[01:10:46] To the extent that even frontier closed source models have 100B or 200B active parameters,  
[01:10:52] do you think that keeps 2x-ing year over year? Or, now that we’re in an RL regime where you  
[01:10:55] also want to conserve compute on rollouts… Also, maybe there is a threshold effect where you have  
[01:11:01] enough capacity and at that point increasing parameters arbitrarily doesn’t matter as much.  
[01:11:06] Do you guys have a sense of, in 2030, how many active parameters a frontier model will have?  
[01:11:11] I think for the next few years, because we are so focused on doing longer and longer horizon  
[01:11:17] rollouts for RL, where inference efficiency matters a lot, it feels like the models aren’t  
[01:11:23] necessarily saturated on their ability to do that. The bottleneck is still the environments.  
[01:11:27] So we might see a little bit of a plateau. I have a feeling that Mythos and the GPT  
[01:11:33] models are much smaller than the 10 trillion parameter range that people are talking about.  
[01:11:38] Even just naively comparing them to open source models, you can probably back out that conclusion.  
[01:11:44] Probably for the next few years, I wouldn’t imagine a huge growth in the number of parameters.  
[01:11:47] But again, there’s so many different things to trade off here.  
[01:11:51] You decide the size of your model based on how much pre-training data you have,  
[01:11:55] and then the difficulty of the RL environments that you’ve got to train on.  
[01:11:58] You ideally want to get to the optimal point where you can get a decent pass@1 or something  
[01:12:04] on the hardest environments you have. It wouldn’t make sense to make a bigger  
[01:12:08] model pass there, because then you’re just paying much more inference than you need to.  
[01:12:12] So a lot of it depends on how quickly Mercor and the in-house teams can scale up the complexity  
[01:12:18] of the RL environments they’re training on. I would expect the models to keep getting  
[01:12:22] bigger just because people are scaling up compute and the GPUs are getting bigger.  
[01:12:26] But exactly how much they get bigger depends a bit on the scaling laws in non-obvious ways.  
[01:12:34] One thing is that I think data efficiency is going to be a bigger driver than compute efficiency of  
[01:12:40] the exact architectures people use, now that we’re getting to the regime where we’re running  
[01:12:46] low on high quality pre-training data. That might affect how sparse you want  
[01:12:51] to make the model. I also think we don’t  
[01:12:55] understand sparsity that well. Parameters are a different  
[01:12:59] resource than active parameters. Sparsity has definitely increased a bit,  
[01:13:08] but it’s not clear that it’s going to keep increasing without bound.  
[01:13:11] There might be some kind of sweet spot. There’s an argument that sparsity should  
[01:13:16] make data efficiency worse, because you might have to learn the same thing on multiple experts,  
[01:13:22] though that’s debatable. I don’t think we have a  
[01:13:27] good enough theory of scaling laws that we really understand why sparsity is helping,  
[01:13:33] how much it’ll help, and if that’ll plateau at some point at a certain level of sparsity.  
[01:13:38] Sorry, can you spell out exactly what the implication of data  
[01:13:42] efficiency would be on parameters? It sounds like you’d say there  
[01:13:46] should be less sparsity, but what are the other implications on parameter scaling?  
[01:13:50] Just that with the scaling law, you’re not trying to optimize compute efficiency.  
[01:13:56] You have all your choices you can make on the architecture.  
[01:14:00] Each of these gives you a different scaling law. Traditionally, you would look at some  
[01:14:04] kind of envelope based on compute. You would look at performance versus  
[01:14:08] compute and take the envelope of the best models. But if we’re making that decision based on data —  
[01:14:20] we’re assuming we can spend a lot of compute, so data is on our x-axis instead of compute — then  
[01:14:33] we just get a different set of optima, or a different set of models that are on that frontier.  
[01:14:39] I also don’t think that we’ve necessarily doubled the size of the  
[01:14:44] models every year for the last few years. People have been training 1 trillion  
[01:14:49] parameter models for at least a few years. There was even an open source one called Falcon.  
[01:14:53] Liam from Periodic Labs, I think, posted yesterday on Twitter about how  
[01:14:56] an early experiment was training a 1 trillion parameter model that was very, very sparse.  
[01:15:00] That was what they did before OpenAI, at Google, the Switch Transformer.  
[01:15:05] It was very, very good at knowledge but terrible at reasoning because it was so sparse.  
[01:15:12] It feels like we’ve been playing in this 100 billion up to 2 trillion parameter range for  
[01:15:18] at least a little bit. It certainly hasn’t  
[01:15:19] been this nice linear increase. I feel like there’s two things.  
[01:15:23] As Charlie was saying, inference efficiency is super important for RL rollouts.  
[01:15:27] This will really push down active parameters quite a lot.  
[01:15:31] I think the total parameters really depends a lot on the hardware as well.  
[01:15:35] You really need very high memory bandwidth and VRAM size to actually be able to serve  
[01:15:39] multi-trillion parameter models. Right now, people are still using  
[01:15:43] a lot of H100s and stuff. As everyone moves to GBs and  
[01:15:46] then Vera Rubins, we’ll get more of the ability to scale and actually serve and  
[01:15:51] do large RL inference at larger scales. The data question I think is interesting,  
[01:15:56] because naively, larger models are much more sample efficient in the actual data points.  
[01:16:00] Even if you’re not saturating the model, it’s still better to go bigger,  
[01:16:04] because larger models generalize better and get to a better loss for the same amount of data.  
[01:16:09] Right now I think we have a lot of data, and that’s not the constraint.  
[01:16:13] Compute is. So we’re having smaller models which are very inference efficient.  
[01:16:16] But if compute is no longer the bottleneck, it might come back to larger models which are  
[01:16:20] undersaturated, but have this generalization ability because they’re much larger.  
[01:16:25] If you just look at the basic Chinchilla scaling law and you just maximize out  
[01:16:31] parameters, it actually decreases the amount of data you need to get to the same loss very little.  
[01:16:36] If you go to infinity on parameters, the amount of data you need I think goes down less than 10X,  
[01:16:41] just because of the nature of the power law. But we’re now on the way-too-much-data side  
[01:16:45] of the Chinchilla laws. Right now we over-train  
[01:16:47] models according to Chinchilla. So we could easily get back to  
[01:16:49] a point where, as we’re running out of data, we move back to the Chinchilla optimal point,  
[01:16:53] or even a bit on the under-training model side. But surely, even with these new chips that come  
[01:16:59] online, we’re just going to be so compute bottlenecked for the next few years that  
[01:17:02] that won’t necessarily be the case. This depends on the ratio you have of  
[01:17:06] training and inference compute, really. If you’re super bottlenecked on data,  
[01:17:09] not on compute, you should go bigger. If you’re super bottlenecked on compute,  
[01:17:12] you should always go smaller. You can also use computer-generated  
[01:17:16] synthetic data, so it’s one of these very hard things to predict.  
[01:17:20] I think part of the reason it took people so long to figure out the scaling laws in the first place  
[01:17:24] was that if you don’t get all these things right, then you don’t get such a clean relationship.  
[01:17:30] The beautiful straight lines on graphs hide a lot of complexity in how you have to make sure  
[01:17:37] to scale every hyperparameter the right way, or parameterize your optimizer in a way that  
[01:17:43] scales and where you don’t have to change your hyperparameters as you change the model size.  
[01:17:47] Bugs have their own clean scaling laws as well. Like with Kaplan forgetting the cosine  
[01:17:53] annealing thing, or even just not considering embedding parameters, I think.  
[01:17:56] That messed up the estimate at smaller models because embedding  
[01:18:00] parameters are a decent size of the model. A bit on RL. A year ago, a lot of people  
[01:18:08] were making this argument that RL will not be super successful at scaling for models.  
[01:18:14] John, you wrote a research paper where you were pointing out that models learn one  
[01:18:19] bit per episode when you RL. They learn, "Did I get the  
[01:18:22] answer right or did I get it wrong?" Then I wrote some blog posts earlier  
[01:18:25] this year where I was like, "It’s even worse than that," because when the pass rate is low and the  
[01:18:28] model is very unlikely to get the answer right, it learns almost nothing at all from an RL episode.  
[01:18:35] But I look at the models today, and they seem pretty smart.  
[01:18:39] It seems to be the result of scaling up RL. Beren, you had a post a few weeks ago where  
[01:18:43] you were trying to explain what’s going on. Why has RL been more successful than  
[01:18:47] one would have naively thought? I think the success of RL comes  
[01:18:52] down to a bunch of different things. First, what is slightly underestimated  
[01:18:56] is the mid-training. An awful lot of what we  
[01:18:59] see as successes of RL actually comes from very, very good mid-training data, which is where we’re  
[01:19:04] essentially doing pre-training but on synthetic reasoning data and the kind of environments  
[01:19:08] that get the model warm-started for RL. This takes the model almost 80% of the  
[01:19:12] way to the final RL checkpoint often. Then what RL does on top of that is  
[01:19:18] essentially tweaking the policy. This is one of the reasons why it doesn’t  
[01:19:22] need as many bits as you would naively think. It doesn’t have to learn all of these  
[01:19:25] behaviors from scratch. It needs just a few bits  
[01:19:28] from these episodes, which you do get. The other thing that I point out in my  
[01:19:31] blog is that these bits are extremely high signal compared to regular pre-training,  
[01:19:36] which is why you need RL at all versus just SFT-ing on successful reasoning traces.  
[01:19:40] Because it’s exactly the bits about how to get the answer right.  
[01:19:44] There’s two things. Yes, one, it’s exactly the bits about how to get the answer right.  
[01:19:47] But this is not exactly how you think of it, because in SFT, you have a trace.  
[01:19:52] You have, say, a bunch of math reasoning and then the answer at the end.  
[01:19:55] The bit is still there. You still SFT on the answer token.  
[01:19:58] What’s important is that the objective ignores all the other bits.  
[01:20:01] In SFT, you have to try and match the exact reasoning tokens that the model produces.  
[01:20:07] You’re essentially getting too many bits about the exact way this other  
[01:20:10] model you’re training on reasons. For RL, you only get the one bit.  
[01:20:14] That means that signal is not drowned out in the noise of all the other bits the model has.  
[01:20:20] It’s really a super dramatic increase in the signal-to-noise ratio during training,  
[01:20:24] which is why RL is so dramatically efficient in terms of steps.  
[01:20:31] There’s been so much debate about what RL does to the model versus mid-training or SFT or whatever.  
[01:20:38] Everyone talks about how pass@1 will go up, but pass@256 will go down.  
[01:20:42] Very rare correct reasoning traces will be down-weighted and outweighed  
[01:20:46] by a gradient signal from easier reasoning traces. I think the simple way to view RL now is that if  
[01:20:53] you have a large enough amount of compute to sample a large enough group size — such  
[01:20:58] that your probability of getting a bunch of correct answers is past some not insignificant  
[01:21:03] probability — then it will be up-weighted. To Beren’s point, mid-training and more  
[01:21:10] pre-training — the pass@1, the starting point for RL — scales in  
[01:21:15] a log number of pre-training tokens. Can I ask some very basic questions?  
[01:21:20] That answer makes sense, and maybe there’s empirical research which  
[01:21:24] shows that this is what’s happening. But then I just look at the models  
[01:21:28] themselves… I don’t know what’s happened. Maybe you can give me a sense of what is  
[01:21:34] the basis of the AI progress over the last year. Maybe it’s just up-weighting the policies which  
[01:21:44] were going to do the correct thinking anyways. But it just seems like qualitatively,  
[01:21:48] the models have gotten so much more capable. Maybe there’s no inherent contradiction there.  
[01:21:56] But how do we square the relatively small impact this take would imply that  
[01:22:02] RL would have with the actual qualitative capabilities the models seem to be gaining?  
[01:22:06] One thing I want to point out here is that it doesn’t  
[01:22:08] necessarily imply that RL has a small effect. Even if you have a few bits and you only change  
[01:22:13] the parameters a small amount, the actual impact on function space — the input-to-output mapping  
[01:22:18] the model learns — can still be super dramatic. Even one bit can change your function space a lot.  
[01:22:22] It can rule out half the hypothesis space, which is huge.  
[01:22:25] I don’t think it’s necessarily the case that small amounts of bits, small amounts of RL, once you’re  
[01:22:29] starting from a really good point, means that you don’t have dramatic impacts in behavior.  
[01:22:33] At least… not necessarily. I think it comes down to two things.  
[01:22:36] The first thing is that everyone was hoping that RL would generalize this reasoning  
[01:22:41] across all these different domains. I don’t think we necessarily got  
[01:22:44] this horizontal generalization. Just training on math doesn’t  
[01:22:47] necessarily make you the greatest coder. You do have to do RL on code environments.  
[01:22:51] I think what we did get, though, is horizon generalization.  
[01:22:55] The models just learned how to use more tokens for longer and still  
[01:23:00] make progress on some sort of task. You can train on environments where  
[01:23:04] they get longer and longer and then put them into a completely new environment.  
[01:23:07] Yes, they may not have generalized the reasoning patterns which allow them to do well in that  
[01:23:10] environment, but they’ve at least generalized the ability to continue on that task for longer,  
[01:23:14] which is correlated with success. There was a paper called EdgeBench which  
[01:23:18] showed that the rate at which models can work for longer is doubling every three months.  
[01:23:23] That’s clear evidence of generalization. The final way to think about it is,  
[01:23:28] in pre-training, there’s this idea of quanta. You have this very smooth pre-training loss curve.  
[01:23:34] When you look at what’s happening in the model, the model is learning all these very discrete  
[01:23:39] tasks, and there’s all these emergent points where there’s a phase transition.  
[01:23:43] It didn’t have induction heads, now it has induction heads.  
[01:23:46] There’s tens of thousands, millions, probably hundreds of millions of these things.  
[01:23:50] You average them all together and you get this very smooth loss curve.  
[01:23:54] To an extent, a similar thing is happening for RL. There is this very slow outer loop,  
[01:23:58] as Beren mentioned. We will train a model and then  
[01:24:01] RL it, and then in the next model iteration of training, we will dump a bunch of these synthetic  
[01:24:07] reasoning traces into the mid-training data. We’re kind of hitting all these quanta for  
[01:24:11] all these different tasks, and on an individual task level, it may look like a phase transition.  
[01:24:15] You’re suddenly going from a 0.5% pass rate to a 90% pass rate on a particular  
[01:24:21] finance task or Excel task or whatever. But you average all these things together,  
[01:24:24] plus the horizon generalization, and you kind of go, "Wow, we’ve got qualitatively better models."  
[01:24:30] I think a lot of this as well is just… RL does generalize a bit.  
[01:24:34] You get some transfer between math and code, or puzzles and math and this kind of stuff.  
[01:24:38] Also, the sheer amount of environments people are targeting is just vastly greater.  
[01:24:43] Before, when you tried to do some task which you do in your daily life, two years ago,  
[01:24:48] the labs wouldn’t really care about this. They wouldn’t train the model for it.  
[01:24:50] Now it’s just so much broader. They have a lot of environments  
[01:24:53] targeting this specific thing. Earlier in the conversation we were talking  
[01:24:56] about RL in the context of causing this entropy collapse, or just concentrating probability on  
[01:25:02] solutions the base model had already done, and causing relatively sparse updates in the policy.  
[01:25:08] But I think there’s also another story about RL, which is going back to the  
[01:25:16] Atari games and then AlphaGo coming up with move 37, the super creative move.  
[01:25:21] Because it was never initialized on human data, it can think in ways that  
[01:25:25] humans are not even thinking and come up with extremely creative solutions.  
[01:25:29] Do you have a sense of when we should expect, or if we should expect, RL on LLMs to result  
[01:25:35] in things like move 37, extreme creativity even beyond human creativity, because there’s just de  
[01:25:41] novo initialization of intelligence? A couple of things here.  
[01:25:47] First off, I think that AlphaGo is using MCTS, which obviously does more exploration and stuff  
[01:25:52] than regular policy gradients. But I also think that RL doesn’t  
[01:25:56] necessarily reduce the creativity. This is obviously qualitative, but if  
[01:26:01] we look at the OpenAI-Hugging Face incident, these models were coming up with multiple zero-days at  
[01:26:06] a time to break out of the sandbox. This is clearly some level of move 37  
[01:26:11] creativity already, which we just get from the general generalization properties of the LLMs.  
[01:26:17] It’s definitely not the case that RL is totally destroying entropy, especially on long horizons.  
[01:26:23] One thing that people call creativity is just solving hard search problems.  
[01:26:31] Move 37 is obviously an example of that, or writing some kind of poem  
[01:26:36] that satisfies a ton of different constraints. That’s something AI is obviously going to be  
[01:26:42] extremely good at, if trained for it. Then there’s another way in which the  
[01:26:51] diversity of the models’ outputs is a lot lower after RL, and they develop these tics.  
[01:26:58] Even though the models seem like they’re good at writing, when you do some kind of  
[01:27:02] distributional analysis, you find that they’re reusing certain themes all the time and they’re  
[01:27:10] using the same character names all the time. You’re not getting the same kind of diversity  
[01:27:15] that you get from human authors. You’re getting one really good style.  
[01:27:21] So I think that kind of diversity has definitely been cut down by RL a lot.  
[01:27:29] In fact, since we were talking about distillation earlier, one thing that’s happening is that so  
[01:27:38] many people are distilling, mostly from Claude, that all the open-weight models write the same  
[01:27:44] way as Claude and have the same tics. This seems kind of concerning to me,  
[01:27:50] that we’re having this monoculture emerge. Again, I don’t think this is fundamental  
[01:27:56] to RL as a method, though. The same with distillation. Even with  
[01:27:59] distillation, you’re just training on the data. Just because your data is not super broad,  
[01:28:03] that doesn’t mean the training method itself is somehow wrong.  
[01:28:06] It’s a problem with the data. I think a lot of the RL entropy collapse, for  
[01:28:08] instance, is basically due to exploitation of fairly simple verifiers when you don’t have a  
[01:28:15] huge diversity of environments. The writing, for instance,  
[01:28:19] is presumably graded by some judge. The judge has some specific tics,  
[01:28:22] and the model is learning to reward hack the judge, and that’s why it collapses.  
[01:28:26] But this is really a problem with the judge. It’s not a problem with RL in general.  
[01:28:30] Okay, super rapid-fire predictions about the future.  
[01:28:34] I want timelines on the following couple of questions.  
[01:28:38] By when do we have models which… Here’s what it feels like to a user.  
[01:28:46] You basically hire it as a drop-in remote worker for all kinds of white-collar work?  
[01:28:53] Not just coding, but video editing, law, paralegal, et cetera.  
[01:28:59] It’s literally an actual remote worker, with full computer use,  
[01:29:02] with literally a month of seamless learning and operation, executing on complex projects that  
[01:29:10] require interacting with other people, et cetera. Everything a human worker could do over a month.  
[01:29:15] If you mandate it to use a browser or whatever — rather than the firm setting  
[01:29:20] up the information to be programmatically accessible — maybe a couple of years.  
[01:29:23] But if it’s not browser-based — it can send Slack messages, it can do all this stuff — I’d  
[01:29:28] still probably say around a year. I would say maybe three years for  
[01:29:32] the full generality. But to Charlie’s point,  
[01:29:36] we will end up with a lot of people making their organizations easier for the AIs to use, and so  
[01:29:41] you get 80-90% of the way there before that. Sorry, but the diff between one year and  
[01:29:48] three years there is just literally… I think there’s going to be a long tail  
[01:29:51] of miscellaneous stuff which some human can do, which will take the models quite a while to do.  
[01:29:56] Are you thinking of computer stuff or basic cognitive capabilities?  
[01:29:59] I think this really comes down to a question of how quickly we can solve  
[01:30:03] this kind of online learning, and whether we can get 80-90% of the way there with compaction and  
[01:30:08] writing files to yourself and stuff. That’s my big uncertainty. I really don’t know.  
[01:30:14] An example of something that it wouldn’t be good at is if I have to yell at someone  
[01:30:17] to get something at work, or really push someone to get something done.  
[01:30:21] The model just isn’t going to do that. It’s going to be too nice.  
[01:30:24] I’d say there’s a wide variation in quality of human remote workers.  
[01:30:29] If you try to hire someone off of Upwork to do a software engineering project,  
[01:30:33] there’s going to be a huge variation. It’s often quite hard to get them to  
[01:30:37] do a good job or pay attention to all the feedback you’re giving.  
[01:30:44] I would guess that in some cases, the pre-AI version of this was worse than  
[01:30:51] what you can get now from existing AI. I think it might end up being a little  
[01:30:57] complicated, because to some extent we already have this for some not-so-high-quality work.  
[01:31:04] But then obviously we’re not matching human level in certain higher-quality forms of work.  
[01:31:14] But I basically agree with Charlie and Beren that maybe we’ll have some  
[01:31:19] version of this in a year or so that’s okay. We’ll have that form factor, and it’ll be able  
[01:31:27] to do some things really well, some things not so well, and things will be improving from there.  
[01:31:33] We shift the goalposts based on the very long tail all the time.  
[01:31:36] I feel like you’ve used this example before of doing your taxes or something.  
[01:31:40] This year, I literally just told Codex to go get everything I needed and send it to the accountant.  
[01:31:45] There was this massive list of stuff it had to use computers to click through and download.  
[01:31:49] It did it. It was perfect. A lot of this stuff it can already do.  
[01:31:55] Okay: give you 10x total productivity uplift. Basically, if it takes you a year to make a  
[01:32:02] breakthrough now, you make a breakthrough every month.  
[01:32:05] I think I would just refuse to give you a scalar on this.  
[01:32:10] We might already be past that in some types of work.  
[01:32:14] Let’s say you’re trying to do certain types of math, and—  
[01:32:20] Oh, sorry. But for you as AI researchers trying to advance the state of AI research.  
[01:32:27] How much are AI researchers sped up or uplifted? Somewhere between 5-10 years?  
[01:32:33] Oh, really? Okay, that’s far away. Really, you think it’s longer than  
[01:32:36] for a general remote worker? Interesting.  
[01:32:39] I’m realizing you probably have a very different definition of a fully general remote worker.  
[01:32:43] I could have specified that earlier. This is true, because obviously an  
[01:32:47] AI researcher can be a remote worker. I’m picturing normal white-collar work  
[01:32:52] over the period of a month. I think it starts to diverge  
[01:32:55] a little bit past two months. A very competent white-collar worker,  
[01:32:58] but not necessarily a super creative researcher. I would say two years.  
[01:33:02] Two years? 10x? Okay. How about you, Beren? I can kind of see that, actually, because  
[01:33:09] right now it’s already definitely more than 10X for coding stuff.  
[01:33:12] So if it can do even one or two loops of experimental feedback,  
[01:33:16] that would actually be massive already. So 10x uplift of AI researchers within two years.  
[01:33:22] If you plug that into a very naive model of AI progress and how much is  
[01:33:26] coming from AI researchers, and there’s a 10x increase in their productivity,  
[01:33:32] you have a radically accelerated pace of AI progress starting two years from now.  
[01:33:36] I think this will mean that AI progress doesn’t get bottlenecked on AI researchers’  
[01:33:40] ability to run small experiments. It gets bottlenecked on other things.  
[01:33:43] Of course. But it just happens 10x faster, which is a huge deal.  
[01:33:47] That also helps the next thing, which gives you a 100x speedup, happen sooner, et cetera.  
[01:33:53] I’m happy to just take a bit longer on that one. What’s the crux?  
[01:33:58] My capacity to absorb information and make the Bayesian optimal decision on the next experiment.  
[01:34:04] I’m assuming that you can delegate some of this to the AI.  
[01:34:07] The AI is becoming decent at deciding. It’s run this experiment, it’s got  
[01:34:10] this result, it runs the next experiment. If it can run two or three experiments in a  
[01:34:14] row without crashing, then that is actually a big uplift.  
[01:34:19] Okay, final question. An AI which dominates top human experts across every single field  
[01:34:27] of work that can be done over a computer. So not only AI research, but all cognitive work.  
[01:34:35] Not just short-horizon work, but literally, if it takes three years or something, the AI will  
[01:34:40] still do better than humans. This is basically just ASI?  
[01:34:43] Yeah. I would say 3-4 years.  
[01:34:46] The fuck? I mean that doesn’t seem wrong, but— AI is obviously getting more attention.  
[01:34:56] It’s one of the harder things, but a lot of energy is being put into it.  
[01:35:01] It’s also not one of the hardest things for AI, because it involves a lot of code and math,  
[01:35:07] which models are really good at. For things that involve 3D and  
[01:35:12] spatial stuff and physical stuff, I think that will take a little longer.  
[01:35:20] If it’s mechanical engineering or something, and it’s not getting the most attention right now,  
[01:35:26] that might take a little longer. But it also does include fields  
[01:35:28] where there is relatively little data because of the nature of the field,  
[01:35:31] and it has to learn that data on the fly. For example, it has to become superhuman  
[01:35:37] at being an engineer at TSMC or something. So you would have to assume that you can give  
[01:35:47] the AI the same onboarding material. Then something has to be solved about  
[01:35:54] longer-horizon learning. I’d say 5 to 10.  
[01:35:58] So basically, you think automating AI research is ASI-complete or something?  
[01:36:06] Yeah, I think so. I think there are so many things in the world where, even if you have  
[01:36:11] some sort of memory system external to the model, and even if context length grows a little bit,  
[01:36:16] there are just fundamentally things where, even if you could research the information  
[01:36:19] or write notes yourself, you’d need more than a million-token context window today.  
[01:36:24] I kind of agree on the 5-year range, at least for the stuff that labs are focusing on.  
[01:36:29] But I think there’s going to be a long tail of stuff which the AI could theoretically go out  
[01:36:33] and learn about, but no one has bothered to do it and the compute hasn’t been allocated to that.  
[01:36:37] So that might take longer for literally every single human expert.  
[01:36:41] Sorry, but by this I also included the ability to learn a new domain as fast as a human.  
[01:36:46] I think that’s not necessarily necessary, because the AI will have  
[01:36:49] vastly greater experience than any human. Thanks so much for doing this, guys.  
[01:36:52] I feel like this was a great format for getting different experts to disagree and debate and  
[01:36:56] discuss things together. It was very productive.  
[01:36:59] Thanks for having us.  
