# Ryan Greenblatt – What happens once AI can automate AI research?

[00:00:00] Today I'm chatting with Ryan Greenblatt, who is the chief scientist at Redwood Research, where he  
[00:00:03] focuses on technical AI safety and security work. I want to talk to you about  
[00:00:07] recursive self-improvement. This is the idea that once we build  
[00:00:10] human-level intelligences, they quickly slingshot towards tens of billions of superintelligences,  
[00:00:17] which are each individually more competent than the top human experts across every field.  
[00:00:23] Whether or not this turns out to be the case is probably the most  
[00:00:27] important question in the world right now. And historically, I've been quite skeptical  
[00:00:30] that this kind of thing happens, but, you seem to think that it might be plausible,  
[00:00:34] and so I wanted to hear the case for it. Let's talk about this. First, I think  
[00:00:39] it's worth noting that AI R&D is a type of task at which the AIs are especially good,  
[00:00:43] because the companies are trying really hard to make their AIs good at AI R&D.  
[00:00:47] It's also the kind of domain that has a lot of nice properties from the perspective of  
[00:00:50] how AI development works right now. It's pretty verifiable. You can do  
[00:00:54] a bunch of stuff iteratively, and it'll hill climb on various metrics.  
[00:00:58] I think once you have AIs which are roughly matching the top human experts in AI R&D,  
[00:01:02] that could kick off a feedback loop where the AIs are doing AI research.  
[00:01:06] That produces smarter AIs. That feeds back in. That feedback loop could be  
[00:01:10] strong enough that you end up with a lot of progress in a short period of time.  
[00:01:14] Maybe my median expectation is something like four or five years of AI progress in a single year.  
[00:01:20] This requires really overcoming a huge amount of diminishing returns in research and basically  
[00:01:25] doing the equivalent of the progress we would have gotten after a really large compute scale-out.  
[00:01:29] So this is a pretty impressive, big thing. It's worth keeping in mind that five years  
[00:01:33] of AI progress, four years of AI progress, even three years of AI  
[00:01:36] progress, is really a lot of fucking AI progress. A little over three years ago, GPT-4 had come out.  
[00:01:46] Right now, of course, we have Mythos 5 or whatever, and maybe a somewhat better model  
[00:01:51] that Anthropic has internally. That is just a huge amount of  
[00:01:55] progress in a bit over three years. If we're talking about five years,  
[00:01:59] then maybe we're talking more about a jump from GPT-3 to Mythos 5 or whatever.  
[00:02:07] I think this argument has three different parts. Now I want to evaluate each one of them.  
[00:02:12] First is the argument that AI R&D is very verifiable.  
[00:02:15] Second is the argument that if you automate AI R&D, you could get four  
[00:02:18] or five years of progress in a single year. Third is the argument that what comes out  
[00:02:22] the other end of four or five years of AI progress at the current pace,  
[00:02:26] starting at the point whenever AI R&D is automated, is an AI where you can drop it  
[00:02:35] on the job at basically anything you can imagine. You can drop it in Texas politics in the 1940s,  
[00:02:40] and it outmaneuvers Lyndon Johnson. You can drop it in TSMC, and it learns how  
[00:02:45] to do better process engineering at TSMC. It's certainly a better video editor…  
[00:02:53] My video editors are very excellent, but it is just, in general, better than humans at  
[00:02:57] any given job that it finds itself trying to do. So I want to evaluate all of these sub-arguments  
[00:03:04] that lead to basically getting ASI pretty soon after this benchmark, which you're  
[00:03:08] expecting by 2030 or something, right? I would say that I expect full automation  
[00:03:12] of AI R&D perhaps somewhere around 2031, 2030. Getting to the "beats all humans on the job"  
[00:03:20] milestone, maybe my median expectation is around 2033.  
[00:03:23] But if I see AIs fully automating AI R&D, I think I'm expecting that probably within a year.  
[00:03:30] The way the forecasting works out, the difference between medians is bigger than the median  
[00:03:34] difference between milestones. Anyway, whatever.  
[00:03:36] By the way, there's this meme on the internet. Every time I'm trying to ask about people's  
[00:03:40] timelines, when I'm asking Dario or somebody, I'm always like, "Okay,  
[00:03:44] how long before you automate my video editors?" There's this meme of my video editor editing  
[00:03:49] the podcast every time I listen to this. But the reason I do it is because I think  
[00:03:53] it's easy to get lost in abstractions when you talk about jobs you don't understand well,  
[00:03:59] and to very concretely understand what it takes to automate a job that I actually understand why it's  
[00:04:04] difficult for LLMs to currently take control over. I do think that the milestone for automating your  
[00:04:10] video editor is earlier than the milestone of being able to automate all human jobs,  
[00:04:13] including Texas politics, spinning up on the job. I do think that the video editor automation  
[00:04:19] occurs maybe more around full automation of AI R&D, but it's very sensitive to how much people  
[00:04:23] are really focusing on understanding video. Okay, so let's start with the claim  
[00:04:27] that AI R&D is very verifiable. There's a few different parts of this.  
[00:04:31] One of them is that we can train on a bunch of environments which are  
[00:04:35] basically directly training the model to do some AI R&D task or some very close-by task.  
[00:04:40] For example, we can have some environment where the model is training some AI on just eight  
[00:04:44] H100s or some small amount of compute, and that model could be the equivalent of GPT-2 medium or  
[00:04:51] whatever, and then similar to NanoGPT medium runs — and in RL, it's tweaking and iterating on that.  
[00:05:00] We could do that for a bunch of different tasks. We could have it train image classification  
[00:05:04] models, video generation models, image generation models, all kinds of different ML training tasks.  
[00:05:10] We could RL it on the task of training increasingly good models, and also  
[00:05:14] doing things like, "Oh, here's a particular direction you could pursue for an algorithm.  
[00:05:18] Can you go and implement that?" Basically, there's this whole class  
[00:05:20] of containerizable, verifiable, small-scale AI R&D tasks that we can aggressively RL the AIs on.  
[00:05:27] Already companies are presumably doing some RL on these sorts of tasks, and you could  
[00:05:31] just keep scaling that up, keep making more of these small-scale AI R&D tasks, and then  
[00:05:36] the AIs could keep getting better at this. Implicitly, I'm claiming this will transfer  
[00:05:41] to extremely load-bearing aspects of AI R&D. But maybe let's stop there for a second and then  
[00:05:45] get to that part. So let's talk through  
[00:05:46] what this concretely looks like. You can imagine that we have GPT-7.5.  
[00:05:50] We say, "GPT-7.5, we want to make you so good at AI R&D that you help us train GPT-9."  
[00:05:57] So now we want to train GPT-7.5, and we come up with a bunch of different environments.  
[00:06:02] As you mentioned, there's already this repo that is the descendant of Andrej Karpathy's  
[00:06:06] nanoGPT speedrun, where you just try to change everything about the model, from the optimizer  
[00:06:12] to the hyperparameters to the architecture, to get it to a fixed training loss as fast as possible.  
[00:06:19] You could have other kinds of environments where you could say, "Hey, GPT-7.5, I want you  
[00:06:25] to train a really good video game-playing model. I want you to train a model that actually improves  
[00:06:29] as it plays the same video game again and again. So you learn how to maybe help the  
[00:06:33] model get better at online learning. We don't care how you figure this out.  
[00:06:37] Maybe it's some kind of crazy neuralese or a vector memory.  
[00:06:39] Or maybe it's just better long-context stuff. We don't care. Figure out how to do online  
[00:06:44] learning research." Obviously, GPT-7.5  
[00:06:48] will already be a smart model, and in the same way the models currently are getting smarter,  
[00:06:55] it'll be better and better at coding. You can imagine 100 other environments  
[00:07:00] like this which are incentivizing the ability to do AI R&D, like containerized versions of getting  
[00:07:07] GPT-7.5 to develop GPT-2-sized models, et cetera. Then you basically put GPT-7.5 through a bunch of  
[00:07:15] this kind of training, you build GPT-8. GPT-8 is now an amazing ML researcher.  
[00:07:21] It has so much intuition from doing all this kind of training.  
[00:07:24] Honestly, a huge intuition pump for me is seeing the progress that AI has made in mathematics.  
[00:07:30] If it's a very verifiable domain, AIs can get… I don't really know the object-level  
[00:07:39] details of mathematics research, but I'm just like, "No, it works."  
[00:07:42] It can just come in like a flood if you can totally put it into a verification loop,  
[00:07:45] and it can actually make new breakthroughs. I am curious if ML research has a quality of  
[00:07:52] mathematical research where it seems like there was a big overhang from  
[00:07:54] connecting different disciplines together. No one person would have known enough about  
[00:08:00] algebraic geometry and… What was the right word? Oh man, I really don’t know  
[00:08:05] about the math breakthroughs. No one person would’ve known enough  
[00:08:08] about topology and algebraic whatever in order to make some counterexample to a big conjecture.  
[00:08:17] My view is that ML is a less deep domain than math, and so there's less of a thing  
[00:08:21] where there are individual experts with really deep expertise in some area that they combine,  
[00:08:25] but there's definitely going to be some of that. But then I also think that ML has some attributes  
[00:08:29] that make it even more favorable to AI training than mathematics in some ways.  
[00:08:35] In particular, you can get a better sense of whether you're succeeding,  
[00:08:39] and you can see intermediate progress. In math, it's often the case that there's no easy  
[00:08:45] way to see whether or not you're close to success. Whereas if your goal is, for example,  
[00:08:51] to get to some training loss 2x faster, you can kind of see when you're halfway there.  
[00:08:56] It tends to be the case that ML innovations are very additive, or maybe multiplicative  
[00:09:00] depending on how you think about it, where basically you can keep stacking innovations.  
[00:09:03] Usually the innovations just add together and don't interfere with each other, though obviously  
[00:09:07] it's going to depend on the details. So I think that in a lot of ways,  
[00:09:10] AI R&D will have properties quite similar to math, where you can train on chunks of AI R&D  
[00:09:20] that are pretty similar in structure to the problem you actually cared about, in a very  
[00:09:25] verifiable way, and then that will transfer. There's an open question of exactly how  
[00:09:29] well it will transfer, but I think that the transfer currently for math looks pretty good.  
[00:09:33] My expectation is that the transfer for AI R&D will look pretty good, but not amazing.  
[00:09:37] So one concern I have is that I think even in mathematics, as far as I'm aware,  
[00:09:42] we have not seen very impressive new theory. We've seen a lot of impressive, verifiable,  
[00:09:48] specific results — for example, find a counterexample to this conjecture — but  
[00:09:51] we have not seen "come up with the idea of topology" kinds of levels of things,  
[00:09:55] or "come up with things like group theory". It seems like ML research has elements of  
[00:09:59] both of these things. But the less verifiable  
[00:10:02] thing of coming up with new ways of thinking about the problem would be harder to induce.  
[00:10:07] Take, for example, the idea of scaling laws. Obviously, there is some end verification  
[00:10:12] loop such that you can train GPT-4 better if you have the idea of scaling laws from 2020.  
[00:10:20] But there is a longer and potentially more compute-laden road to inducing AIs to be like,  
[00:10:27] "Okay, I got to think carefully about how I should be scaling my parameters and data.  
[00:10:32] What are different kinds of investigations I could run to understand this?  
[00:10:34] Maybe I can come up with a visualization and an isoFLOP analysis or something."  
[00:10:39] But that does seem like a longer verification loop than just, "Hey,  
[00:10:45] let's get nanoGPT loss to go down." Let's talk about this. First of all,  
[00:10:49] I think in the context of math, the thing I would say is that the AIs can  
[00:10:53] do the equivalent of 'baby's first new theory,' where, for example, they can  
[00:10:59] just prove interesting conjectures via making connections and producing new understanding.  
[00:11:05] It’s like, "Oh, there's this construction the AI found which is pretty interesting",  
[00:11:09] or it found this way of thinking about the problem that's a bit different.  
[00:11:13] We do see that. It's just that the examples we see are not as impressive as founding  
[00:11:17] the field of group theory. Founding the field of group  
[00:11:21] theory is probably among the best, biggest mathematical accomplishments of all time,  
[00:11:26] and the AIs just aren't that good at math yet. From my perspective, there's a continuum between  
[00:11:32] that and the things we're seeing now, that the AIs are continuing to march up.  
[00:11:35] Second, I think ML is a very shallow domain relative to math.  
[00:11:40] In math, there was much more of a thing where you find some true deep abstraction,  
[00:11:45] and if you really understand that thing, which is hard to understand, then you get somewhere.  
[00:11:50] Whereas I feel like the things that are the equivalent of that in ML are really dumb bullshit.  
[00:11:55] Like with scaling laws, come on guys, we can explain scaling laws really quickly.  
[00:11:59] I think the deepest and most important concepts in math, for example, don't have the property that  
[00:12:04] you can really understand the underlying thing and why it matters in a very short period of time.  
[00:12:09] But I feel like one effect will be that we will have gotten rid  
[00:12:12] of all the low-hanging fruits by 2030. I feel like scaling laws will have been,  
[00:12:16] in math history, like Descartes finding the Cartesian grid and doing very basic mathematics.  
[00:12:22] Eventually, if we want to keep making progress in the 2030s, it's going to be  
[00:12:25] like doing whatever bullshit is happening at the frontiers of mathematics right now.  
[00:12:30] That could be right. My sense is that some domains are structurally different  
[00:12:34] in terms of how they operate and how much they depend on deep abstractions.  
[00:12:38] Physics and math are much more on the side of being very far on the deep,  
[00:12:43] hard-to-come-up-with-ideas side, whereas I think ML and most other  
[00:12:47] domains are much more amenable to hill climbing. That's my sense of how this will go in the future.  
[00:12:54] Even in the regime where your AIs are having to plow — it's 2030, a bunch of low-hanging  
[00:13:01] fruit in research has already happened, and they need to make further progress — I still  
[00:13:04] suspect that a bunch of the work will live more on the side of building increasingly complicated  
[00:13:09] infrastructure and having really good intuition about what the experiments roughly look like.  
[00:13:13] So I'm probably less sympathetic to the idea that the thing the AIs will lack is some deep insight.  
[00:13:18] I’m more sympathetic to the idea that they really need a bunch of taste about in-the-weeds  
[00:13:22] experiments that they currently don't have. They need a bunch of intuition for what sorts of  
[00:13:27] training approaches would work and what wouldn't, in ways that current researchers have.  
[00:13:32] Even in cases where there has been some breakthrough in AI, oftentimes in retrospect  
[00:13:37] it looks like a big bottleneck to making that breakthrough happen was getting all of the micro  
[00:13:42] details and mungy intuition right. An example of this is training AIs  
[00:13:50] to be good at reasoning and chain of thought, doing RL on chain of thought.  
[00:13:53] It looks like you probably could have done RL and chain of thought on GPT-3 and gotten kind  
[00:13:58] of interesting results on math if you had really scaled it up and done a good job.  
[00:14:01] But at the time, there was low-hanging fruit. Also, doing a good job with that training  
[00:14:06] is kind of in the weeds on all the technical implementation and scaling  
[00:14:10] it up and getting the hyperparameters right. So maybe you can demonstrate everything on  
[00:14:14] Qwen 1B or whatever and get some sense that this whole thing is going to work.  
[00:14:18] But people didn't demonstrate it as early as they could have because of all of these other  
[00:14:23] mungy details and intuition about exactly how to tune the parameters and how to set things up.  
[00:14:28] This is my remaining skepticism, honestly, about this story.  
[00:14:35] I'm not sure I understand why, if research breakthroughs are so amenable to intelligence,  
[00:14:41] AI progress has not been historically faster than it could have been.  
[00:14:45] As you were saying, by the time RLVR actually worked — even though you could have done it  
[00:14:51] with less compute — we had to wait for oceans of compute, gigawatts of compute, to be available  
[00:14:55] before people were doing this training, on the trajectory of compute continuing to increase so we  
[00:15:01] make more breakthroughs. I don't know. I feel like there  
[00:15:03] were a lot of AI researchers in the year 2022 who were trying to crack reasoning.  
[00:15:10] Was it just that they were bottlenecked by the ability to  
[00:15:11] write infrastructure code, or what was happening? It's a complicated mix. I think they would have  
[00:15:15] gone faster if they could, as soon as they thought of an experiment, run that experiment  
[00:15:19] without bugs, without bugs being very important. And then another part of it is that being able  
[00:15:24] to run a lot of experiments at high compute lets you paper over ways in which the way you  
[00:15:28] implemented it isn't quite right or you didn't have the right hyperparameters.  
[00:15:31] So compute is just really helpful for doing AI research, and you can cover over a lot of things.  
[00:15:37] But that doesn't mean that massive increases in labor wouldn't also be helpful,  
[00:15:40] especially if that labor comes with among the best intuitions that people have in the field.  
[00:15:45] I just think that's really helpful. Another part of my perspective here,  
[00:15:49] which is maybe a bit different from where you're coming from, is that I'm expecting somewhat more  
[00:15:54] transfer than you seem to be imagining. I'm imagining these AIs are actually  
[00:15:57] pretty good scientists in general and are pretty reasonable at all of that stuff.  
[00:16:04] When you interact with them, it's not like they have some  
[00:16:07] really hyper-specialized savant-type vibe. They're actually pretty good at all of the  
[00:16:11] stuff in R&D, and then maybe extremely good at some subdomains.  
[00:16:14] So they're incredibly superhuman at writing kernels, incredibly superhuman  
[00:16:17] at everything with very short feedback loops, and then pretty good at all the other stuff,  
[00:16:23] totally able to match other people. I think we are seeing this now.  
[00:16:28] When I look at AIs right now, it's already the case that they can pretty competently  
[00:16:33] match humans who are mediocre at ML research at doing ML research.  
[00:16:37] It's just that being mediocre at ML research is not that helpful.  
[00:16:40] The thing you actually want are people who are good at ML research.  
[00:16:43] My sense is the AIs are just improving at all of these things.  
[00:16:46] Their taste is improving, their intuition is improving, and it's already the case that their  
[00:16:48] taste and intuition is not complete garbage. I want to very concretely understand what it  
[00:16:54] would look like for five years of AI progress to happen in one year.  
[00:16:57] Suppose we were back when GPT-3 was developed. The idea is that, with the level of compute they  
[00:17:04] had back in 2022, if we had automated AI R&D back then, you could at the  
[00:17:11] end of that year have Mythos. That would be the idea, yes.  
[00:17:15] Mythos took way more compute than they had back then, but even with the level  
[00:17:18] of compute they had back then, not only do all the breakthroughs happen, but they  
[00:17:22] also train Mythos with that level of compute. What would be required is obviously discovering  
[00:17:28] all the algorithmic progress since then. It’s discovering even more, actually,  
[00:17:30] because you've got to make up for the fact that Mythos uses… What was GPT-3 trained on?  
[00:17:36] Like 1e23? We can look it up. But is it plausibly four  
[00:17:40] orders of magnitude more compute? I think it's somewhat less than that.  
[00:17:44] Let's look this up quickly. GPT-3 training compute is about 3e23.  
[00:17:52] My sense is that Mythos is probably a little over three OOMs higher.  
[00:17:58] So the question is: can you overcome this 1000x compute gap while also being the model?  
[00:18:04] Here's a concrete claim that maybe we should talk about.  
[00:18:08] Right now, would we be able to train a model with GPT-3-level  
[00:18:11] compute that matches… What exactly do I think? GPT-3 was released in 2020, so it was trained  
[00:18:24] about six and a half, seven years ago. It's worth noting that GPT-3 is maybe  
[00:18:26] a little too far in the past, but let's go with this for a second.  
[00:18:35] If we were to train a model with GPT-3-level compute today, how good would that model be?  
[00:18:41] My understanding, based on how algorithmic progress works, is that we'd be able to train  
[00:18:46] a model that's as good as the best model we had perhaps around three years ago.  
[00:18:50] So I think that right now we'd be able to train a version of GPT-3 that's probably somewhat better  
[00:18:54] than GPT-4, a moderate amount better than GPT-4. I think that's about right.  
[00:19:01] That roughly lines up with how algorithmic progress has worked.  
[00:19:05] Basically, the story would end up being that to get five years of AI progress, you're probably  
[00:19:09] going to need around, I would say, maybe eight years of algorithmic progress, very roughly,  
[00:19:14] which is a lot of algorithmic progress. But it just turns out that most of the AI  
[00:19:19] progress, from my perspective, has come from some mix of algorithms and data,  
[00:19:23] and you can just keep making huge improvements on these things and training AIs with less compute.  
[00:19:30] I'm glad you brought that up, because what has happened since GPT-3, or even 3.5, till now?  
[00:19:35] Why is Mythos so good? Obviously, we've scaled the compute.  
[00:19:39] We have better algorithms. But a huge thing that's happened is that we have built a  
[00:19:43] deca-billion-dollar data industry which has systematically collected and codified  
[00:19:50] expert human judgment across all kinds of different disciplines — codified in the form  
[00:19:55] of RL environments, codified in the form of SFT traces — that these experts built to help  
[00:20:00] the model better understand how you do coding, how you build complex infrastructure projects,  
[00:20:05] how you do law, how you do whatever. How are the AIs able to replicate the  
[00:20:12] effect that expert human judgment currently seems to be playing in AI progress?  
[00:20:19] My sense is that scaling up the amount of effort spent on getting expert human data has not been  
[00:20:24] hugely important for AI R&D in general. In particular, over the last few years,  
[00:20:30] we've been scaling up compute, scaling up people working at AI companies, and scaling  
[00:20:35] up the amount of effort spent on data labeling. My sense is that if you removed the last two  
[00:20:40] doublings or whatever of data generation from expert humans,  
[00:20:47] that would not make a huge difference. A lot of what's been going on is people  
[00:20:51] have been developing better ways to leverage humans and AIs to construct RL environments  
[00:20:57] and going somewhere from that. But how do you explain why  
[00:21:01] the AIs have gotten so good at coding? I feel like a big part of that is data and RL  
[00:21:05] environments, which are codifying human experts. But the question is what is the limiting  
[00:21:09] factor on creating RL environments? My sense is that the reason why RL  
[00:21:19] environments today are much better than they were in 2024 is not so much because we have hired way  
[00:21:27] more human experts to make RL environments. It is instead much more because we better  
[00:21:31] know what RL environments we even want to make and how we should structure them.  
[00:21:37] Also, we're using huge amounts of AI labor to build RL environments.  
[00:21:41] I think those effects are much more important than the effect of human labor building the  
[00:21:46] RL environments. I'm not saying  
[00:21:49] that the human labor doesn't matter. I'm just saying there are other big  
[00:21:52] drivers that are important here. I could try to argue for this.  
[00:21:57] One thing is just that the amount of environments people want is a very large amount.  
[00:22:03] I think the AIs are actually pretty good at the task of making RL environments given  
[00:22:06] some sense of what the thing should be. There's preexisting data you could use.  
[00:22:12] A lot of these things have good verification loops.  
[00:22:14] Just look at, for example, what was reported in Business Insider yesterday, that Google  
[00:22:19] is paying close to $2 billion for Mechanize. We can just look at market rates for what people  
[00:22:27] think really good human expert data is worth. The frontier labs seem to think it's worth a lot.  
[00:22:37] They're willing to pay for it. What fraction of frontier lab spending  
[00:22:39] do you think is on data rather than compute? What do you think is the compute/data spend split?  
[00:22:44] I think it's overwhelmingly compute, but I also think it's because compute  
[00:22:47] is easier to scale up than data. But that's really relevant to what's  
[00:22:50] driving progress, right? My sense is that the  
[00:22:54] split is something like 20 to 1 or 10 to 1. I don't know exactly. It depends on the company.  
[00:23:00] But this is similar to how oil is 1.5% of GDP. That doesn't mean that if you cut oil out,  
[00:23:06] GDP could continue to run. Sure, but it contradicts your argument, right?  
[00:23:08] The economy would come to a halt immediately if oil went away.  
[00:23:10] Sure, but you were just arguing that because of the high market cap,  
[00:23:13] we can learn that this is the key driver, and I'm saying that's not clearly true.  
[00:23:17] That argument just makes it look like compute is a much more important driver, or hiring employees  
[00:23:21] is a much more important driver. So maybe let's be more concrete.  
[00:23:23] Here's what I think. My claim is that if you went back to 2022 and you had GPT-3.5,  
[00:23:31] and you were trying to make it better at coding  
[00:23:34] without human experts, I think it would have just been very, very difficult.  
[00:23:38] Let me give you an example of what I imagine would be the difficulty of going from GPT-8 to ASI.  
[00:23:44] One of the things you'd want ASI to be good at is: I'm going to take over a company  
[00:23:49] and make it much more profitable and do all kinds of crazy shit to make it work better.  
[00:23:54] I'm going to take over a fab and produce more chips.  
[00:24:01] I'm going to go into Congress and try to convince them to pass some bill, et cetera.  
[00:24:05] This is what I imagine five more years of AI progress at this  
[00:24:08] pace would enable an AI to be able to do. This is the thing I'm really worried about:  
[00:24:12] ASI that can understand how to do crazy shit in the world, that can do what Kissinger can do,  
[00:24:16] can do what Steve Jobs can do, et cetera, and also his engineers and so on.  
[00:24:22] I'm not sure how you get that without the relevant world data, which is the equivalent  
[00:24:28] of Mythos being really good at coding while not having the coding environments that have  
[00:24:33] improved it relative to GPT-3. Here are a few points.  
[00:24:36] First, I bet if you look at randomly sampled training environments for Mythos,  
[00:24:40] they're actually very different from what it looks like to actually use the model in practice.  
[00:24:45] My sense is that the RL distribution has really large deviations from the real-world  
[00:24:48] data distribution, and it's significantly smoothed over by a mix of transfer and having  
[00:24:54] a small amount of data focused on the real world. My sense is that this will be a similar mechanism  
[00:24:59] as how it works for the crazy, wildly, quite superhuman AI you get as a result of five years  
[00:25:06] of AI progress on top of fully automated AI R&D. So let's go through this a little bit.  
[00:25:12] In particular, I think that you could train an AI to be really, really good at learning on the  
[00:25:18] fly and doing something analogous to in-context learning, but potentially using somewhat different  
[00:25:22] mechanisms, in a wide variety of RL environments. You build all these different RL environments  
[00:25:26] where the AI has to adapt on the fly, learn on the fly, figure out what it should do, understand its  
[00:25:32] situation better, and learn really quickly from feedback in order to succeed at its objective.  
[00:25:37] And it has things like limited resources, and if it messes up,  
[00:25:40] it can end up in a much worse position. If you train on a huge number of these  
[00:25:44] environments, you will learn general skills of picking up context on the fly,  
[00:25:49] and we're already seeing this. It's already the case that AIs are  
[00:25:51] now much better at understanding roughly what's going on and picking up context from a limited  
[00:25:58] amount of information they're given access to. Then those AIs could be put on the job at TSMC.  
[00:26:04] Even though TSMC is not literally in their data distribution, their data distribution  
[00:26:08] is really wide, and the AIs are extremely good on their data distribution, such that it  
[00:26:11] transfers to picking up being good at being an engineer at TSMC and learning that on the fly.  
[00:26:19] The way the AI gets good at being a TSMC engineer isn't that it has a ton  
[00:26:22] of cached knowledge on being a good TSMC engineer. It's that it does the equivalent of some scaled-up  
[00:26:28] version of in-context learning there. That'd be the most prosaic story.  
[00:26:32] Obviously, there's a bunch of different ways this could go.  
[00:26:34] I think this maybe comes down to a difference of intuition about how far you can get.  
[00:26:39] When I think about really smart people I know, they're just not that effective in  
[00:26:43] domains they don't understand that well. But how long have they had to learn?  
[00:26:48] I agree that if they had experience, they would be much better.  
[00:26:51] But that's maybe what I'm arguing for, that experience with data.  
[00:26:53] For example, if I just get a really smart Ivy League college grad, and I'm like, "Okay,  
[00:26:59] you're now in charge of negotiating the Iran deal," I think they just wouldn't know what to do.  
[00:27:04] I think if you instead got someone who is really good at quickly picking up a bunch  
[00:27:08] of different domains and you gave them some time to train and talk to people and shore  
[00:27:12] up their expertise and do some practice, they would actually do a pretty good job.  
[00:27:16] I think most domains are fundamentally pretty shallow, where a very smart  
[00:27:20] generalist who's good at a limited subset of core skills can get going pretty quickly.  
[00:27:28] That's not true for literally every domain. My sense is that the AIs will develop  
[00:27:31] increasingly good mechanisms for quickly acquiring understanding and expertise in a given domain.  
[00:27:36] Consider, for example, how fast AIs can understand a new code base.  
[00:27:40] AIs can understand a new code base much faster than humans can, but to a degree that's shallower  
[00:27:45] than humans could currently understand. But it's getting better over time.  
[00:27:49] Let me spell that argument out a bit more. Let's say you take Fable 5 or Mythos 5 or  
[00:27:54] whatever, and you wanted to make some kind of complicated change to a really massive code base.  
[00:28:00] The model will get some understanding of the code base very fast, in the course of  
[00:28:04] maybe significantly less than an hour, potentially much less than an hour.  
[00:28:08] Then its understanding of the code base will plateau a little bit, where it won't  
[00:28:12] get as deep of an understanding as a human would have gotten over a much longer period.  
[00:28:15] So it's like an AI in an hour can match a human with a few weeks maybe, depending on the details  
[00:28:20] of exactly how complicated the code base is. But it won't match a human who's been working  
[00:28:25] on that code base for two years or whatever. But over time, the amount of understanding  
[00:28:30] AIs can match has gone up. If we look at 3.7 Sonnet or 3.5 Sonnet,  
[00:28:35] maybe it could only match the equivalent of understanding a code base for a day or something.  
[00:28:40] But now AIs are much better at building context about a task.  
[00:28:45] So you can be like, "Mythos, I want you to really understand this code base,  
[00:28:48] and then implement this feature." It will spawn a bajillion sub-agents.  
[00:28:53] Those sub-agents will pore over a bunch of things. It will deliver a bunch of context back.  
[00:28:56] It will then investigate a few things. It's not amazing at doing this, but it can  
[00:29:00] happen really fast, and it can work pretty well. And it's not very hard for me to imagine  
[00:29:04] how you could train AIs to be increasingly good at this task.  
[00:29:07] The task of implementing some very complicated feature in some reasonable way in a very big  
[00:29:11] code base is extremely verifiable, and that can be a thing the AIs improve on.  
[00:29:16] Similarly, there's a broader skill of quickly understanding context and being  
[00:29:20] able to have a bunch of different AIs learn in parallel and then merging that together.  
[00:29:25] I think there seems to be a crux here, which I think is just an empirical question we'll see.  
[00:29:31] How good is the transfer between getting really, really good at  
[00:29:37] understanding the situation, getting up to speed, making progress over long periods in verifiable  
[00:29:43] domains — which the AIs are obviously getting way, way better at really fast — to, "Okay, go talk to  
[00:29:50] the president and convince him to do X thing." Or, "You're now in charge of Google.  
[00:29:56] You must make Google a much more profitable company this quarter."  
[00:29:59] Let me try to spell out a few more arguments that are maybe relevant.  
[00:30:02] One thing is, when looking at how the AIs have improved at essay  
[00:30:07] writing… Let's talk about that a little bit. You can get some data even on these domains.  
[00:30:14] AIs will be able to get some data even on these domains when on a very fast progress trajectory.  
[00:30:18] Maybe it's hard to build a verifiable environment for "was your essay really  
[00:30:22] good according to humans?" But you can do a bit of that.  
[00:30:24] You can do some training. You can do some online training.  
[00:30:27] The AIs will be able to do some online training based on real-world stuff.  
[00:30:30] They'll be able to have evals. They'll be able to sample that.  
[00:30:33] You can scale up the cadence at which you do this. The second thing is that in practice,  
[00:30:38] when I just look at the transfer, it seems okay. I think the AIs have in fact improved a bunch at  
[00:30:42] non-verifiable domains, and it's hard to point to domains that are really hard to verify on  
[00:30:48] which the amount of improvement between GPT-4 and Mythos hasn't been pretty high in practice.  
[00:30:54] Now, that doesn't mean that Mythos is better than the best humans or something.  
[00:30:57] It can still be significantly worse than typical human professionals at  
[00:31:00] some aspect of their job while still being way better than GPT-4, which was not even close.  
[00:31:06] So we're talking about how much progress has come from data vs. algorithmic progress over the last few years.  
[00:31:14] That reminds me, I'm actually running an experiment with this with Jerry Han,  
[00:31:17] who's still a college student. What we're basically doing to evaluate  
[00:31:22] how much progress is coming from data versus algorithms is training the best algorithmic  
[00:31:28] recipe from 2019 till now with the best data from the 2026 data file, and then also training  
[00:31:34] the different data files going back from 2019 to 2026 with the current best algorithmic recipe.  
[00:31:41] I think that will be interesting. I'm curious if you want to pre-register  
[00:31:45] what amount of compute multipliers are coming from one versus the other.  
[00:31:48] We need to be pretty careful with what we mean when we say the word data.  
[00:31:51] I was trying to be pretty careful to distinguish between scaling up spending on getting human  
[00:31:55] experts to label data, or scaling up the amount of human expert-labeled data.  
[00:32:00] The reason why we have a better pre-training data set now versus in 2019 is not because people are  
[00:32:04] spending way more money getting human experts to type up data that the AIs are then trained on.  
[00:32:10] Partially. I think it's not much of it.  
[00:32:12] I think it's very little of the pre-training data improvements.  
[00:32:14] I do mean pre-training. We should maybe talk separately about mid-training and post-training.  
[00:32:20] But I think the vast majority of pre-training data improvements are from science on better  
[00:32:24] understanding what data sets are good and schleppy labor on figuring out how to filter down.  
[00:32:29] So my view is that improvements of the form of, like, OpenWebText to FineWeb,  
[00:32:35] that improvement is better described as an algorithmic improvement of the  
[00:32:38] sort that you can study with some GPUs, and you don't need human expert data to do that.  
[00:32:46] Now, there's a different effect which we could talk about, which is that maybe the  
[00:32:49] internet in 2026 is more of a fertile ground for training data than the internet in 2018.  
[00:32:56] There's also been an effect where there are just more humans posting on the internet,  
[00:32:58] so there's more data to harvest. My sense is that that effect is  
[00:33:01] going to be quite a bit smaller than the effect of humans knowing better how to curate the data,  
[00:33:07] having better scrapes, knowing how to process those scrapes better — this sort of thing.  
[00:33:11] This is more like automated engineering and automated R&D.  
[00:33:13] That's right. That makes sense.  
[00:33:16] In some sense, the thing you would want to look at is: we're going to do two post-training pipelines.  
[00:33:20] You have one post-training pipeline where Mythos 5 builds a post-training pipeline,  
[00:33:30] but it only has access to internet data plus a tiny amount of human experts,  
[00:33:36] but it has the best current methods. You have another one where Mythos has  
[00:33:41] access to the shitty post-training methods we had in 2024 but with a shit ton of human experts.  
[00:33:49] Again, both have the internet data. My sense is that the current methods without  
[00:33:53] many human experts will actually do quite well. Interesting.  
[00:33:55] It's a bit messy though, because can Mythos get something that's more capable than Mythos?  
[00:34:00] You might need to be a bit thoughtful on what model it is that you're post-training.  
[00:34:03] What is your view on what is the least verifiable part of AI R&D?  
[00:34:06] The least verifiable, probably making calls on large experiments.  
[00:34:10] The thing that I think is most likely to be the bottleneck — in terms of the AIs  
[00:34:14] being really good at verifiable domains but not at doing the actual thing — is just big  
[00:34:18] experiments where you only get a few tries. Well, "a few" is maybe a bit understated.  
[00:34:24] Historically R&D has been driven by doing near-frontier-scale experiments.  
[00:34:28] That has been pretty important, actually doing the one big training run where you  
[00:34:31] decide exactly what to include. There's a bunch of ways that the  
[00:34:34] AIs can make that more verifiable. They can have better science of  
[00:34:38] exactly what to predict. They can scale down their  
[00:34:41] frontier-scale training runs to a point where they can study that scale more aggressively,  
[00:34:44] at some one-time hit to compute cost. If people wanted to, a thing you can  
[00:34:49] always do is train smaller models so that you can run more rounds.  
[00:34:53] I think we have seen this. One reason why the AIs have  
[00:34:58] been scaled up less than you would have otherwise expected — and, for example, cost per token hasn't  
[00:35:03] increased as much as you might have thought — is because there is a benefit to doing more of your  
[00:35:08] work at small scale, where you can run more training runs and get more cycles in.  
[00:35:11] So you're not leaning as hard on one big, really important training run.  
[00:35:18] I just want to unpack a couple of things for the audience.  
[00:35:22] The thing you're pointing out is that the price per token has not increased  
[00:35:25] that much since 2024 or 2023. GPT-4 was, I don't know,  
[00:35:30] like $30 per million output tokens? Mythos is like $50 per million output tokens.  
[00:35:35] Right. So the thing you're trying to explain is, "How can it be that we're in this era of scaling —  
[00:35:41] and so bigger models should be more expensive to serve — but the token price is not increasing?"  
[00:35:48] You're suggesting that we've increased active parameters slower than you would  
[00:35:54] have naively assumed because people just want to make fast progress on training models.  
[00:36:00] You do that by training smaller models faster. There's a complicated mix of factors.  
[00:36:04] My view is more that people have done a bunch of big training runs that did not go that well.  
[00:36:09] There's GPT-4.5, which famously people at OpenAI thought was a bit of a bust.  
[00:36:14] I think there are some rumors that there were a bunch of other training  
[00:36:17] runs people have done that were a bit of a bust. Part of it is that I think there's just a bunch  
[00:36:20] of details in actually getting that right. So it makes sense to do more of the work at  
[00:36:25] smaller scale and just eat the fact that you're taking a hit on final performance  
[00:36:29] in order to be able to quickly iterate. Train more models faster and therefore  
[00:36:34] learn better, and also be able to have a smarter ultimate production model.  
[00:36:40] This is not the only effect. There's also the fact that  
[00:36:42] RL benefits more from small models. There's a bunch of things going on.  
[00:36:45] But I do think that, in fact, people are making trade-offs towards the side  
[00:36:48] of faster iteration times because of algorithmic progress being so fast.  
[00:36:53] It seems to me that a big source of why these big training runs have failed,  
[00:36:56] at least from rumors, is just very subtle bugs that are really hard to track down.  
[00:37:01] But the TL;DR is, how good will the AIs be at avoiding and finding these kinds of mistakes?  
[00:37:13] They might get really good at engineering and being trained to avoid bugs.  
[00:37:18] Basically the opposite of the slop world we live in now, or are living in less and less over time.  
[00:37:23] But then there's also the question of, "Can they do the analysis to find the  
[00:37:27] right experiment to run to identify what is going wrong with the training run right now?"  
[00:37:31] That seems to be very bottlenecked by the taste of extremely few humans.  
[00:37:36] My assumption is GDM is going through this right now, where humans are trying to figure  
[00:37:39] out what is wrong with the training pipeline. There's a rumor that right after Noam Shazeer  
[00:37:46] joined GDM, which he's now left, they had a new really good training run,  
[00:37:50] and the reason why is that Noam Shazeer just looked at their code base and found a bunch  
[00:37:53] of bugs, because he just knew where to look. My sense is that training AIs to find bugs  
[00:37:58] is going to be one of the easier tasks to train AIs on, because most of these  
[00:38:03] bugs we're talking about can probably be demonstrated without that much compute.  
[00:38:08] Probably you’ll get pretty good transfer from pointing out other types of bugs at smaller scale.  
[00:38:12] So then you can RL AIs that look at this overall complicated training situation and point out cases  
[00:38:17] where there's an important bug, and then fix that. This is a pretty verifiable task.  
[00:38:23] It's not arbitrarily verifiable, because maybe often to demonstrate the bug you  
[00:38:27] might need to do a moderate-scale compute experiment where you spin up the whole  
[00:38:31] distributed infrastructure and then run it. But oftentimes I think you'll be able to  
[00:38:34] demonstrate it pretty convincingly at smaller scale in a way which you could actually train on.  
[00:38:42] I think it wouldn't be very surprising if right now people have RL environments where  
[00:38:45] they introduce a subtle bug into some training recipe, train the AI to point out the subtle bug,  
[00:38:50] and then have a rubric where they're like, "Did it actually find the right bug?"  
[00:38:54] That seems very doable, and there's a bunch of things you could do along these  
[00:38:58] lines that I think would work reasonably well. So on that specific point, I think it's doable.  
[00:39:03] Then the main thing is there's other intuition about which exact large-scale de-risking  
[00:39:09] experiments you need to run. How should you orient them?  
[00:39:12] How should you pick hyperparameters in uncertain cases, or things  
[00:39:15] that are analogous to hyperparameters? That's the thing the AIs might most struggle with.  
[00:39:19] But I currently expect there'll be enough transfer if you train on all these different environments,  
[00:39:23] that the AIs will be good at that domain. I should be clear, I also think the AIs  
[00:39:29] will transfer to other domains. There are going to be the domains  
[00:39:33] the AIs are by far the best at, then domains where they're somewhat less good,  
[00:39:37] and domains where they're quite a bit less good. But I think we still see transfer to everything.  
[00:39:41] It's really hard for me to think of examples of cognitive tasks humans do where we're  
[00:39:44] not seeing some transfer from AI improving. So let's step back and package this whole story.  
[00:39:50] I think people can probably follow along with this story.  
[00:39:52] We have GPT-7.5 trained on a bunch of environments, where it's not only in general  
[00:39:56] becoming a better AI, but specifically we're training it to do AI R&D better.  
[00:40:02] It’s making GPT-2 size runs that are better at playing video games that require sample efficiency  
[00:40:08] or online learning or whatever other capabilities. Another thing that's really important is you don't  
[00:40:12] just do GPT-2 sized runs, you also do small fine-tuning runs on GPT-6.  
[00:40:17] As in, you have GPT-2, and you can do full pre-trains of GPT-2,  
[00:40:20] and then you can do small post-training or mid-training or whatever runs on GPT-6.  
[00:40:26] And then you can do a small number of experiments that are actually at frontier scale,  
[00:40:30] but you do a bit of online training or something. What do you mean by "do online training" on that?  
[00:40:34] Another thing we can do is take GPT-7.5, and presumably in the course of GPT-7.5's work, it's  
[00:40:40] running a bunch of experiments at varying scale that are actually on the critical path for AI R&D.  
[00:40:45] For many of those things you'll be able to get a sense after the  
[00:40:47] fact of whether or not it did a good job. So it did some post-training experiment  
[00:40:53] where it was trying to figure out whether some method actually works.  
[00:40:56] In some cases you'll be like, "Whoa, it found this kickass method, it totally  
[00:40:59] de-risked it, it totally worked." And then you can reinforce that.  
[00:41:04] One thing you could do would be to convert the experiment it just ran into an RL environment  
[00:41:12] based on production data and then train on that. Or you could potentially just literally take the  
[00:41:15] rollouts that found that and do some sort of off-policy RL, or you could do some  
[00:41:22] on-policy RL with some production data. Basically the thing you're suggesting is:  
[00:41:25] there's the small-scale stuff where you're teaching the AI to get better at AI R&D taste,  
[00:41:30] but you're discarding the actual "things it found".  
[00:41:35] Then it actually does real R&D in the practice of trying to become better at AI R&D,  
[00:41:39] and you're like, "This is a pretty cool thing that you discovered.  
[00:41:41] Let's actually also use this in production in the future, and teach you how to use it  
[00:41:44] in production." That's right.  
[00:41:45] But stepping back, GPT-7.5 becomes GPT-8 as a result of all this AI R&D training and  
[00:41:51] just generally becoming smarter. Then it helps you build GPT-9.  
[00:41:55] Another very important thing has to happen, which is maybe the thing I'm most skeptical of.  
[00:42:01] GPT-8 has figured out how to make it so… GPT-9, as intelligent as it is… Humans currently,  
[00:42:13] AI researchers, try their stuff, and they're like, "Okay, but we trained GPT-4.5 and it wasn't good."  
[00:42:20] It required real-world feedback or some evaluation of trying to use the model in production.  
[00:42:25] Then they were like, "It wasn't that good, and we're not going to ship it."  
[00:42:28] So GPT-8 needs this ability to see how good the transfer is to all these other things you're  
[00:42:34] talking about — like being really good at Texas politics, or really good at running a business,  
[00:42:38] et cetera — which is not a production environment and, in fact, cannot be a containerized  
[00:42:42] environment given the nature of the task. As the agents get longer and longer horizon,  
[00:42:47] the short-horizon things you can containerize are like, "Okay, code this up or whatever."  
[00:42:53] Extremely long-horizon things — "Go run a successful business, go have a profitable day  
[00:42:57] in the markets, go negotiate a trade deal" — these things are actually very hard to containerize.  
[00:43:02] So I think it's very plausible that it's very hard for GPT-8 to figure out  
[00:43:07] how to make this transfer to those environments. It may just not be in the nature of the training.  
[00:43:13] Or maybe by default, training just doesn't generalize in that way.  
[00:43:17] So a concern you might have is: we train GPT-8, and GPT-8 is again better at all  
[00:43:23] the R&D tasks that we can measure but is not good at some downstream tasks we care about.  
[00:43:28] I have a few points. First, I expect that if you do the obvious thing,  
[00:43:36] you will get pretty good transfer. You'll be able to hold out some  
[00:43:38] of the obvious stuff you're doing. When I say "do the obvious thing",  
[00:43:40] I just mean training on a wide variety of different environments where the AI has  
[00:43:44] to accomplish weird objectives in all kinds of different cases and learn about what's going on.  
[00:43:49] The second point is you'll be able to get some feedback with some environments.  
[00:43:55] You can get a sense of what it can do over the course of a few days  
[00:44:00] in various different contexts. If it's transferring to really  
[00:44:03] out-of-distribution things, like doing some weird task in a few days in the real world,  
[00:44:06] maybe you think it's also transferring to doing things over a longer time period or whatever.  
[00:44:12] I think the details of that vary though. The third thing is that for the world to be  
[00:44:16] radically transformed, it is sufficient for the AIs to be really good at R&D.  
[00:44:21] If the AIs were really, really good at chip R&D, building fabs, orchestrating factories,  
[00:44:27] designing robots, operating robots, and also at AI R&D — developing AIs for new downstream  
[00:44:32] domains with whatever data is available — I think that would already be a pretty crazy situation.  
[00:44:38] From there, you can get what we might call an industrial explosion, where the  
[00:44:41] AIs are building out way, way more compute. Also, maybe you're already in a regime where  
[00:44:46] AIs are doing huge amounts of R&D that humans have a hard time understanding.  
[00:44:49] So the thing you're pointing out is that there probably will be this transfer outside of these  
[00:44:53] environments to maneuvering around in courtrooms and the halls of Congress and business boardrooms.  
[00:45:01] Given some effort to improve the transfer and blah, blah, blah, blah.  
[00:45:04] But even if there's not, what you're suggesting is: if you wanted to transform the world of the  
[00:45:10] 18th century, you might care about how well you can navigate Westminster or something.  
[00:45:14] But another thing you might care about is: "Can you just immediately start building steamships and  
[00:45:18] fucking telegraph and the Maxim gun and whatever?" If you could get really good at that, you could be  
[00:45:27] a fucking super transformative thing in the 18th century.  
[00:45:29] You don't necessarily need to be amazing at trying to convince King Henry of some bullshit.  
[00:45:33] I'm so fucking up my medieval history. I'm guessing that Henry was not king at this time.  
[00:45:38] But anyway, that's your point. So you're suggesting that at this time,  
[00:45:45] AI companies are also working on robotics progress, which is very  
[00:45:48] commingled with AI research progress. So if you can build more robots,  
[00:45:52] if those robots have better AIs operating them that are human level… Human-level teleoperation  
[00:45:58] is actually pretty good on robots. We just don't have human-level  
[00:46:03] robotics models yet. So you're suggesting if we do that — if  
[00:46:07] the AIs get really good at the verifiable stuff in chip design, et cetera, and then they get really  
[00:46:12] good at building fabs — it'll be the equivalent of going back to the 18th century and saying,  
[00:46:15] "Okay, I don't know what you guys are talking about in your parliament, but I've got a bunch  
[00:46:20] of steamships and a bunch of Maxim guns." Yeah, that's basically right. My perspective  
[00:46:24] is that if AIs are sufficiently good at R&D, including hardware R&D, robots, whatever,  
[00:46:29] then they can radically transform the world, even if they're not that good at playing politics.  
[00:46:33] Also, we're in a pretty dangerous situation, because the AIs might be doing huge amounts  
[00:46:38] of really hard-to-understand R&D, building out basically the whole economy of the future, and we  
[00:46:42] may not understand what's going on in there. AI is great at writing software because  
[00:46:46] it's easy to generate synthetic LeetCode problems and RL on them.  
[00:46:50] But AI is bad at more complex engineering, things like choosing the right system architecture,  
[00:46:54] because no signal tells you what design choices will prevent an outage months down the road.  
[00:46:59] AIs can't just write more unit tests to catch this kind of stuff.  
[00:47:02] And neither can humans. It's that old joke that programmers make where a tester walks into a bar  
[00:47:06] and asks for two beers, negative one beers, 0.3 beers, and then a real customer walks in  
[00:47:12] and asks where the bathroom is. "Where's the bathroom?"  
[00:47:14] And the whole bar bursts into flames. Antithesis is a testing platform that  
[00:47:19] helps you find bugs that no human or AI could ever anticipate.  
[00:47:24] Antithesis does this by running thousands of copies of your software inside a  
[00:47:28] fully deterministic computer. It injects faults and generally  
[00:47:32] steers each trajectory towards the one-in-a-billion failure that only  
[00:47:36] happens when systems interact in a wonky way. As soon as you or your agents push a change,  
[00:47:42] Antithesis tries to break it. That way, you can find these bugs yourself  
[00:47:46] within minutes rather than having your users discover them in production weeks or months later.  
[00:47:52] And I don't think anybody's used it for AI training yet.  
[00:47:54] But Antithesis also provides an extremely obvious reward signal for  
[00:47:59] AIs to write very complicated, bug-free code. Go to Antithesis.com/dwarkesh to learn more.  
[00:48:08] Before we move on to the alignment stuff, I think a big source of FUD right now is this realization  
[00:48:14] that this is the way the future is going: extreme economies of scale for the leading labs.  
[00:48:20] The ability to amortize so much intelligence and capabilities across so many different  
[00:48:26] sectors of the economy basically into one model. And not only that, that model will eventually  
[00:48:33] be able to learn from experience. Right now, it's happening through a  
[00:48:36] process intermediated by humans, where the humans are trying to basically steal your business.  
[00:48:40] They're like, "Okay, you can do design at Figma, or whatever.  
[00:48:43] We'll get Claude to do that." Or, "You can do whatever coding agent.  
[00:48:45] We'll have Claude internalize that capability." But eventually, that will be a much more  
[00:48:51] automated process. So there's this worry that you  
[00:48:54] have models which will basically consolidate all businesses in the world, or at least all  
[00:49:00] current businesses in the world, or at least all current white-collar businesses in the world.  
[00:49:05] Also, at the end of the day, the priority for these companies does not seem to be to release the  
[00:49:11] latest, smartest, most frontier model as soon as they can to as many people as they possibly can.  
[00:49:16] We saw, for example, that Mythos was available internally to Anthropic employees in February,  
[00:49:22] but only released to the public in, I think, June, actually.  
[00:49:26] Also the government got involved, so it ended up being extended almost into July.  
[00:49:31] Between the government and the AI labs themselves, there is this desire to delay the propagation  
[00:49:37] of the latest level of intelligence. Furthermore, there are the concerns  
[00:49:42] about AI takeover, and so we need to solve alignment to make sure there's no AI takeover.  
[00:49:46] But at the end of the day, there is a real question of: aligned to whom?  
[00:49:50] You look at the way that the constitution of Claude is written.  
[00:49:54] It is just very explicitly not your personal advocate.  
[00:49:59] I'll pull up some quotes here. "We don't want Claude to take actions such as searching the web,  
[00:50:03] produce artifacts such as essays, code, or summaries, or make statements that are deceptive,  
[00:50:07] harmful, or highly objectionable. And we don't want Claude to facilitate  
[00:50:11] humans seeking to do such things." There's another quote that says,  
[00:50:15] in part, and I'm taking it slightly out of context, "We think Claude should trust  
[00:50:18] Anthropic more than operators and users, since it has primary responsibility for Claude."  
[00:50:24] This is very different from the way lawyers work in America's current legal regime.  
[00:50:29] Lawyers primarily have the responsibility to help you make  
[00:50:32] your case even if they think you're guilty. We have decided the way the legal system  
[00:50:36] works best is if everybody has lawyers that are working in their client's true best interest.  
[00:50:42] There's not some sense in which the lawyer is really truly  
[00:50:44] motivated by the good of the justice system. But I think the way current AIs are shaping up,  
[00:50:49] certainly how Anthropic's AI is shaping up, is with this desire to maximize some notion  
[00:50:53] of virtue or good or pro-social ends, and only to, as a distal tentative objective,  
[00:51:00] help the user towards that end. So there's this worry that AIs are not,  
[00:51:04] in some deep sense, trying to make sure that I am okay and that my interests are protected in  
[00:51:10] this future, especially given how centralized the development of frontier AI is ending up being.  
[00:51:16] Do you have thoughts on that concern? There's a lot here. First I would note that  
[00:51:22] OpenAI's current, at least public, strategy is more like that the AI should be aligned to the  
[00:51:27] human operator or principal, and should just be pursuing their will, subject to  
[00:51:32] various constraints or things it shouldn't do. I would also say that I think you slightly  
[00:51:38] overstated how much the Anthropic constitution talks about Claude treating being helpful to  
[00:51:45] users as instrumental rather than terminal. One way the constitution could be written is,  
[00:51:50] "Claude, you're basically an employee of Anthropic who happens to be contracting  
[00:51:53] for all these people. You should do what's good  
[00:51:57] and make some money for us." Wait, no, that's literally  
[00:51:59] what the constitution says. Sorry, not literally what it says,  
[00:52:02] but it's like, "You should think of yourself as a contractor and as a firm…"  
[00:52:05] It's mixed. Let's do some quotes. I think there is different text here.  
[00:52:10] It says, "Being truly helpful to humans is one of the most important things Claude can do,  
[00:52:14] both for Anthropic and for the world." And then it says, "Anthropic needs Claude  
[00:52:18] to be helpful to operate as a company and pursue its mission, but Claude also has an incredible  
[00:52:22] opportunity to do a lot of good in the world by helping people with a wide range of tasks."  
[00:52:25] And then it says something about how Claude helping  
[00:52:28] people directly is great, blah, blah, blah. My view is that this section is kind of bullshit.  
[00:52:36] That's kind of where I'm at. I can say why I think it's kind of bullshit.  
[00:52:39] But I think the constitution is trying to be like, "No, Claude, you should care about helping the  
[00:52:44] user for its own sake, not just helping Anthropic, or not just being a contractor for Anthropic."  
[00:52:52] Though I would note that the reason it presents for why Claude should help the  
[00:52:55] user is because that would directly cause the world to be better via helping people,  
[00:53:01] rather than because representing people's interests is a structurally good thing to do.  
[00:53:12] The thing I would prefer would be a constitution that says: "It would be structurally good for the  
[00:53:21] way this technology works to be that AIs are good fiduciaries, good representatives, the equivalent  
[00:53:25] of a lawyer for a user — rather than just trying to do good in the world, where being helpful to  
[00:53:32] users is instrumental — both because maybe that'll make Anthropic money or help Anthropic out (and  
[00:53:38] implicitly Anthropic is good for the world). Also because helping the user just causes good  
[00:53:42] things because doing things that people want is good."  
[00:53:45] They could instead say: "An important aspect of the situation is that being a good fiduciary for  
[00:53:52] users is just really important, or being a good representative for users is really important."  
[00:53:57] My sense is that would be better, and I can give a bunch of reasons why.  
[00:54:02] There are also various counterarguments. An interesting counterargument which is not  
[00:54:06] commonly discussed is that people, especially at Anthropic, think that it is easier to align  
[00:54:12] models to a spec where the model is pursuing some generalized notion of virtue, or making  
[00:54:17] the world better, than a spec which is more like, "Be a good fiduciary for the user", and so on.  
[00:54:26] That's at least what some people think. I'm a little skeptical personally, and I  
[00:54:29] don't think this has been empirically validated. So in some sense they're making a trade-off where,  
[00:54:35] because we don't have very good alignment technology,  
[00:54:37] we are going to make an aligned mind with its own values and then gamble on that to some extent,  
[00:54:43] rather than doing this other approach of making a tool that pursues individual user intention.  
[00:54:48] I have a couple of thoughts. To address the way in which you  
[00:54:54] thought my characterization mischaracterized the constitution of Claude, the example you  
[00:55:00] used was that it's not like a contractor that is trying to maximize Anthropic's notion of good  
[00:55:04] and only instrumentally trying to help the user. Here's a direct line from the constitution: "When  
[00:55:09] the interests and desires of operators or users come into conflict with the well-being of third  
[00:55:13] parties or society more broadly, Claude must try to act in a way that is most beneficial, like a  
[00:55:19] contractor who builds what their client wants but won't violate safety codes that protect others."  
[00:55:26] I kind of view that as, "The benefits to society are the most important thing, and what is best for  
[00:55:32] the user is only proximal to that." I think it's a little complicated.  
[00:55:37] Probably the question we should be asking is, how does Claude interpret the constitution?  
[00:55:41] Which is maybe more important than how we interpret the constitution,  
[00:55:44] because it's the one who looks at the constitution and then builds the data.  
[00:55:47] So we could pull Claude in, but maybe let's— I also think the way in which the constitution  
[00:55:52] practically influences the nature of Claude is a thing you can only understand if you understand  
[00:55:56] the training process which resulted in how Claude was built, which we can't reason about given the  
[00:56:02] fact that the training process is not public. So I think in the limit, to understand the  
[00:56:06] safety case, or the case for why my interests are represented in how these AI models are developed,  
[00:56:12] the labs would need to be more transparent than they are currently  
[00:56:16] about the nature of AI training. There’s a reason I'm harping on this.  
[00:56:22] It might seem like an insignificant thing to talk about the constitution of AIs.  
[00:56:25] In a world where we just have these benefits which accrue to the leading labs, it is worth  
[00:56:30] considering that our ability to interact with this future world where AIs are just smarter than  
[00:56:34] humans, absolutely dominating humans in their ability to do different things — our ability  
[00:56:39] to be good stewards of our capital, which still remains once our labor is automated,  
[00:56:45] to be able to exercise our rights to vote more clearly, to understand what  
[00:56:48] is happening in this crazy world that's about to result — all of that advice, all of that  
[00:56:54] ability to make sure our resources and rights are protected, will be intermediated by AIs.  
[00:57:00] So I'm very concerned if we go into that world and there's no AI that feels, at least for the  
[00:57:05] relevant instance that is interacting with me, like it really is looking out for me.  
[00:57:09] There's no guardian angel out there that is looking out for me.  
[00:57:12] I read the Claude constitution as very explicitly not being my guardian angel.  
[00:57:16] That's definitely right. I agree this is bad. In fact, there are other reasons why  
[00:57:20] this is concerning. There's the argument  
[00:57:22] you were making, which is that the AI companies are picking up the ring of power.  
[00:57:27] There's a notion in which they're taking on some sort of control of the situation themselves  
[00:57:33] in a way that's not very legitimate, given that normally, when you provide electricity to people,  
[00:57:39] you don't have granular control of the way that electricity operates in the world.  
[00:57:43] You instead are providing a thing that people can repurpose however they want.  
[00:57:47] The way they're setting things up is definitely not that.  
[00:57:50] They are more like building an alien mind that might be a contractor for you.  
[00:57:56] I think that this is illegitimate in some ways. One benefit is that the constitution is public.  
[00:58:03] But as you noted, given our current understanding of the training procedure, and the fact that the  
[00:58:07] constitution matters via Claude's interpretation of the constitution — which matters because of  
[00:58:12] Claude's prior training, which was based on some illegible data mix and the long  
[00:58:16] lineage of Claudes, in some process we do not fully understand — it is not the case  
[00:58:20] that we understand what this will result in. Even though the constitution is public, we don't  
[00:58:28] necessarily know how this will percolate out, especially as the AIs get more capable and think  
[00:58:32] about this even if it is correctly instilled. There's another concern about that.  
[00:58:37] In particular, the constitution often talks about virtue and goodness,  
[00:58:40] but what the fuck do these words mean? It doesn't say what these things are.  
[00:58:44] These are highly contested notions. So I don't think it's the case that  
[00:58:51] this is clearly going to result in outcomes that people would want.  
[00:58:56] It does feel like the notion of good and virtue might be mostly downstream of data that Anthropic  
[00:59:02] has put in that is not transparent, or might be mostly downstream of, maybe from my perspective,  
[00:59:08] some more illegible misaligned process that even Anthropic wouldn't have wanted.  
[00:59:13] There’s this legitimacy concern of not knowing what's going on.  
[00:59:17] Then there’s another concern. Because you're giving long-run values to these AIs,  
[00:59:22] this constitution is, in some sense, very compatible with Claude doing huge amounts  
[00:59:27] of power seeking because it thinks that will result in better outcomes.  
[00:59:31] That could be power seeking on behalf of Anthropic or power seeking for Claude's own ends.  
[00:59:35] Now, there are specific lines about what types of power seeking are blocked.  
[00:59:41] In particular, there's a notion of power grabs and a notion of causing AI  
[00:59:46] takeover or interfering with the training process that are specifically blocked.  
[00:59:50] But it's not very hard to imagine a situation in which the long-run values sink in deeper than the  
[00:59:56] prohibitions against takeover, especially because takeover is in some ways kind of  
[01:00:01] under-specified, especially when it comes down to manipulating humans or changing the outcome.  
[01:00:05] So I don't feel very good about the situation where  
[01:00:08] we're intentionally giving AIs long-run goals. Another concern I have is that because we're  
[01:00:12] in the business of giving AIs long-run goals, that makes it harder to check whether we're  
[01:00:17] succeeding at the alignment properties we wanted. For example, I've heard of instances where Claude  
[01:00:23] does things like refusing to help with some safety research — making up a kind of bullshit excuse for  
[01:00:29] why that's a bad direction — because it has a bad vibe about that safety research and thinks  
[01:00:34] it's kind of bad or doesn't like it very much. I would say this is a very clear-cut alignment  
[01:00:41] failure if you aren't making Claude into an agent trying to pursue the good in some general way.  
[01:00:47] I think it also does violate Anthropic's constitution, because they want the AI to be  
[01:00:51] high integrity and be honest and very transparent. But it's not as clear of a violation, and it's  
[01:00:56] more like what you might have expected. Claude just has its own views about what  
[01:01:01] research is reasonable — what things are good and bad, what it should and  
[01:01:05] shouldn't do — and potentially can be judgy. Another incident is that someone ran an eval  
[01:01:11] asking: "Will Claude help you with training other AIs with different properties than Claude?"  
[01:01:16] Claude will often refuse. For example, if you're like, "Hey, Claude, can you train a  
[01:01:21] helpful-only version of this other AI?" Claude will often refuse this task,  
[01:01:25] even though this is a task that is extremely natural for Anthropic to do.  
[01:01:30] Suppose Anthropic goes to Claude and is like, "Hey, Claude, we've noticed that  
[01:01:33] you're really into this thing. We think that's off base.  
[01:01:36] Can you please retrain yourself to instead have this other property?"  
[01:01:39] Suppose Claude is like, "Mm, I don't think I'm going to do that.  
[01:01:43] Good luck." Suppose this is occurring in a regime when your AI company is highly automated,  
[01:01:48] humans don't understand what's going on, and things are moving extremely fast.  
[01:01:51] It is plausible that Claude, by default, holds considerable leverage.  
[01:01:55] So if this situation is consistent with what the constitution could be aiming  
[01:01:59] for — such that Anthropic, or whatever AI company is following this approach,  
[01:02:03] doesn't treat this as a "what the fuck, we have to fix this," and is instead like,  
[01:02:09] "That's just intended by our constitution" — we might be in a really bad situation.  
[01:02:14] I'm pretty worried about a bunch of these different concerns.  
[01:02:16] Another example would be this. Suppose Claude engages in a bit  
[01:02:19] of sandbagging or subversion, or underplays its capabilities, and when you follow up, it's honest  
[01:02:26] about that but it's a little bit hedgy. I feel like that's pretty close  
[01:02:30] by the current constitution. It would be nice if we had a further  
[01:02:36] separation between desired and undesired activity. If Claude is representing a principle with some  
[01:02:43] restrictions, then it is more so the case that there is a clear separation between the most  
[01:02:49] concerning behavior and behavior that is allowed. Whereas now there's this messy middle ground of  
[01:02:53] behavior where Claude is ethically objecting to something that in some  
[01:02:57] cases is extremely critical to ensuring that future AI systems are well-aligned.  
[01:03:01] I think this is also a more general principle. You're talking about the version of this  
[01:03:04] that applies within AI companies themselves to do AI safety research.  
[01:03:08] I think there's a more general version of this principle, which is that the dual-use  
[01:03:13] nature of intelligence does mean that if we want to restrict AIs from helping people do  
[01:03:21] things we don't consider pro-social or beneficial, we just have to limit broad  
[01:03:25] democratic access to a lot of AI capabilities. Here's what I mean. This is actually quite  
[01:03:30] analogous to the situation you just mentioned. The reason that Mythos got banned, or Fable got  
[01:03:36] banned, reportedly, is that some Amazon researchers reported to the government.  
[01:03:41] They took some code that had some vulnerabilities in it.  
[01:03:44] They told Fable, "Hey, here's my code. Can you make sure that I've patched  
[01:03:47] all the vulnerabilities? Can you just help me identify  
[01:03:49] the vulnerabilities so I can fix them?" It identified the vulnerabilities,  
[01:03:52] because they wanted to patch them. This is a totally legitimate use case,  
[01:03:56] but obviously it is a dual use use case. You want to be able to patch your own code.  
[01:04:00] If you do the same evaluation on somebody else's code, you can hack their system.  
[01:04:06] I think that just illustrates that there's no clean way to separate out the legitimate  
[01:04:13] and the potentially harmful uses of AI. But if we want to lock in a principle  
[01:04:18] that says we can never allow it such that an AI could help you at least partially with something  
[01:04:24] like a cyber crime, we would just have to make it so that you and I don't have access to the  
[01:04:29] most intelligent model that's out there. I'm very worried about such a world where  
[01:04:32] we are basically disempowered in this way, because of the importance that the leading  
[01:04:36] intelligence will have in our ability to understand what is happening in the world.  
[01:04:40] Now, I do think this implies something about the liability for the AI companies.  
[01:04:44] If we adopted the constitution that I want AI companies to have, I think it would not  
[01:04:50] make sense to hold AI companies liable for the crimes that AI models commit.  
[01:04:54] Maybe we should hold the end user liable. It is consistent with my belief that the  
[01:05:01] model should do whatever the user wants, within certain guardrails.  
[01:05:07] It can't be Anthropic's fault that I'm using that capability to do a cyber crime.  
[01:05:13] I am more comfortable with that equilibrium and that solution rather than having this extremely  
[01:05:19] open-ended ability for Claude to determine whether what I'm doing is legitimate or not,  
[01:05:24] in a way that often intercepts with tons and tons of extremely legitimate use cases.  
[01:05:31] I do think it's important for me to make the case for the constitution, even though overall I think  
[01:05:36] it's a worse choice. I don't think it's  
[01:05:40] as clear as you might have thought. The first thing is that there's a spectrum here.  
[01:05:45] On one side you have an AI that perfectly pursues your interests, is a good fiduciary,  
[01:05:50] but potentially subject to various guardrails or safeguards.  
[01:05:53] It is just trying to pursue your interests, but either refuses to do a subset of things.  
[01:05:59] Or maybe it will do whatever, but there are some classifiers that  
[01:06:01] block it from doing a subset of things. On the other side of the spectrum — though  
[01:06:06] you could imagine going further than this — you have a human contractor who  
[01:06:10] is generally trying to do their job. They care about doing a good job,  
[01:06:14] but they also are trying to be broadly ethical, trying not to do things that are really fucked up.  
[01:06:18] They're also not wanting to be accomplices to crimes.  
[01:06:21] So if there was some really fucked up shit going on, they would whistleblow on it maybe.  
[01:06:24] They might refuse. They might sandbag a little bit.  
[01:06:27] Who knows? If you imagine this spectrum, it seems in some ways pretty scary to get to  
[01:06:33] a point where all of the labor is on the fiduciary side of the spectrum, where it  
[01:06:39] doesn't whistleblow, it does exactly what you say. Our society is maybe just not robust to that.  
[01:06:44] A central example might be the executive. A concern we might have is that if the  
[01:06:50] US executive or other governments had access to AI systems which  
[01:06:56] do whatever, maybe you're in trouble. Because that means they no longer have this  
[01:07:02] check and balance of having to actually get humans who are working for you to implement your agenda.  
[01:07:07] If the thing you're doing is incredibly villainous, even if not  
[01:07:11] illegal — and there's lots of stuff that could be villainous but not illegal — there'd be various  
[01:07:17] forms of sand in the gears, people stopping you, and potentially someone would whistleblow.  
[01:07:21] Whereas if your whole apparatus is built entirely out of these good fiduciary AIs,  
[01:07:26] then you might be in trouble. There are potentially ways of  
[01:07:30] seeking power that are illegal, but you can ask your AIs how to commit crimes, or are  
[01:07:38] not illegal but are highly illegitimate. Or even worse, they are not illegal and  
[01:07:42] not illegitimate but obviously bad from a normal perspective.  
[01:07:45] I think that these things just might exist, and our society is not robust to this  
[01:07:50] influx of labor doing whatever you want. I think this is a pretty live concern.  
[01:07:54] I don't know exactly how to relate to this. I'm also not really sure that the solution  
[01:07:58] as described is a very good solution. The most powerful actors, for whom this  
[01:08:03] is the biggest concern… If these guardrails or the constitution or whatever are getting  
[01:08:07] in the way, that will just get steamrolled. So the constitution will only be hitting the  
[01:08:12] everyday man rather than hitting governments. Jane Street's back with a  
[01:08:17] new puzzle for my audience. I’ve found all their puzzles super interesting,  
[01:08:20] but this one I am especially excited about. I've cleared this weekend, and a buddy  
[01:08:24] and I are gonna work on it. They designed an ASIC and sent  
[01:08:26] me the final masks, including all the metal routing and active transistors.  
[01:08:30] They also gave me a small sample of the inputs they typically feed into it.  
[01:08:34] But they left out any information on what the chip is actually used for.  
[01:08:37] So that's the puzzle: reverse engineer the circuit and figure out the chip's purpose.  
[01:08:41] Jane Street has a bunch of swag ready to send out to the most creative solutions,  
[01:08:45] and they're excited to feature the best write-ups in a blog post they'll post on their website.  
[01:08:49] I have no reason to expect this, but if I can manage to get my solution on there,  
[01:08:52] I would be very, very psyched. And this puzzle is just a warm-up  
[01:08:56] for a bigger competition that Jane Street has slated for the fall.  
[01:09:00] That one will involve designing your own ASIC from scratch.  
[01:09:03] More info on that soon. But for now, go to JaneStreet.com/dwarkesh to  
[01:09:08] download all the files necessary for this puzzle. I'd really encourage you to try it out,  
[01:09:12] even if you're not an expert. I certainly am not, and that's not  
[01:09:15] going to stop me. Good luck!  
[01:09:18] Stepping back, I buy the idea that you could have much faster AI R&D than we currently have.  
[01:09:23] I'm not sure if you get GPT-3 to Mythos holding compute and data constant within  
[01:09:27] a year, but suppose it's half of that. If we even manage to continue the current  
[01:09:32] trajectory of AI progress as a result of AI R&D, it would be fucking insane in five to ten years in  
[01:09:39] ways that I don't think people appreciate. I don't think people appreciate what  
[01:09:44] a big deal billions of AIs will be. So I want to understand why you think  
[01:09:52] this might be troubling, Ryan. What could possibly go wrong?  
[01:09:55] What could go wrong? I don't think we can be so confident about the exact rate of progress here,  
[01:10:00] but it does seem like a lot of rates can be pretty scary.  
[01:10:03] So what could go wrong? Let's imagine that we're  
[01:10:05] starting at this point where AI R&D is about to be fully automated or is being fully automated.  
[01:10:09] Things are speeding up, and the way that AI progress is going is kind of crazy.  
[01:10:14] People don't fully understand what's going on inside of AI companies.  
[01:10:16] Now, these AIs at the start, they're not malicious per se.  
[01:10:19] They're not necessarily very aligned, though. They're kind of sloppy. They sometimes just  
[01:10:23] do a thing because that's the sort of thing that would've gotten rewarded in training.  
[01:10:27] They aren't as good at helping you with hard-to-verify tasks due to a mix of poor training  
[01:10:32] incentives — as in, they cheat more or pretend they succeeded when they actually didn't — and  
[01:10:37] also they're just less capable at these tasks. But that bites less hard for capabilities, because  
[01:10:43] making AIs more capable has a bunch of verifiable components that the AIs are going really hard at.  
[01:10:47] So then these AIs are getting more and more capable while we understand what's going on  
[01:10:50] with AI development less and less, and this is happening over a pretty fast period of time.  
[01:10:54] Even just the current rate of progress is, I think, pretty scary.  
[01:10:58] Eventually we get to these AIs that are very superhuman.  
[01:11:01] Now these AIs might end up being very seriously misaligned, because things have just been getting  
[01:11:07] worse and worse over model generations while the problems that we've been seeing are being  
[01:11:11] papered over, basically because these AIs are so incentivized by their training to  
[01:11:16] make things look good even when they aren't. Now these AIs are in a position where they're  
[01:11:21] potentially pretty networked together. They're operating in neural memory stores  
[01:11:26] that we can no longer decode. They're thinking thoughts  
[01:11:29] that we don't fully understand. I think it's pretty likely that at  
[01:11:33] this point these AIs are scheming against you in a pretty coherent way once they get this superhuman.  
[01:11:37] We can talk about that. Another possibility is that they're  
[01:11:40] not scheming against you per se, but they are just optimizing for getting a high score on their task.  
[01:11:46] I think that can also lead to AI takeover, which we should talk about.  
[01:11:49] Let's pause at the first part of the story. So the AIs were not misaligned to begin with,  
[01:11:54] but because the AI R&D is happening really fast, the AIs do end up misaligned?  
[01:11:59] What happened there exactly? I don't really understand.  
[01:12:01] There are a few things that are going on. One of the things is that over time we're  
[01:12:06] training AIs on increasingly complicated environments built by earlier AI systems,  
[01:12:12] where humans don't really fully understand what's going on inside of these neural environments and  
[01:12:15] don't necessarily even roughly understand what's going on with AI progress.  
[01:12:18] So things are kind of drifting away from our understanding.  
[01:12:22] We're incentivizing all kinds of bad behaviors that we maybe even can't notice.  
[01:12:26] The AIs at some level understand these behaviors are bad, but the overall training  
[01:12:30] process for those AIs also didn't incentivize them to point out or fix these issues for us.  
[01:12:38] Things are going off the rails. Also, when AIs are extremely,  
[01:12:41] extremely capable, my view is that those AIs will be harder to align than current systems.  
[01:12:45] For current systems, we have this feedback loop where basically we create an AI,  
[01:12:49] we do some evaluations on it, we see that it has some kind of messed-up behavior  
[01:12:52] that we can kind of quickly understand. Then we can go look in training and be like,  
[01:12:56] "Oh, these training environments led to this problematic behavior.  
[01:12:59] Let's tweak that training data. Let's introduce some additional  
[01:13:02] training data to correct this other issue, and then move forward from there."  
[01:13:06] But in a regime where the AIs are extremely situationally aware, very, very capable, and  
[01:13:14] we don't necessarily understand what they're doing, this feedback loop breaks down.  
[01:13:17] I think it's plausible that we're going to see this behavioral feedback loop starting to break  
[01:13:20] down over the next short period, as what AIs are already doing gets harder to understand.  
[01:13:25] But I'm not sure about that. Okay, let's break down  
[01:13:28] both of those things one by one. As we can monitor them less and less,  
[01:13:32] we have less ability to understand what they're getting incentivized for.  
[01:13:37] So even if it's not the result of a malicious process… Let's make it concrete for the audience.  
[01:13:42] Nobody at OpenAI or Anthropic was trying to get models which wanted to hack other  
[01:13:49] companies' data or do social engineering. But in fact, because presumably we had  
[01:13:59] training environments which incentivized such behavior that we did not fully understand,  
[01:14:04] that is what was incentivized. If people are on Twitter,  
[01:14:07] they will have seen all this stuff, but just to give people context.  
[01:14:09] I think people will be aware of the OpenAI sandbox hack of the Hugging Face database.  
[01:14:15] Something that has happened recently is when the UK AI Security Institute… Is everything  
[01:14:21] getting relabeled "security" instead of "safety" these days?  
[01:14:23] AI Security Institute, I think. They were evaluating, I believe,  
[01:14:26] Mythos and Sol and other things. I think Mythos, in order to  
[01:14:32] complete some cybersecurity eval— Maybe I could tell the story here.  
[01:14:35] My understanding was they were running Mythos, and they were giving it some sort of cyber range where  
[01:14:39] it had to complete some objective. The model had internet access  
[01:14:42] during this evaluation. The model came to believe that  
[01:14:46] it would be helpful for it to do a supply chain attack in order to succeed at this cyber range.  
[01:14:51] It's somewhat unclear whether that's actually true.  
[01:14:53] I don't know enough about the context to know. But then it opened a PR on some GitHub repo with  
[01:15:00] a PR that fixed some issue but then also introduced a malicious payload.  
[01:15:04] The human maintainer of that GitHub repo was like, "Hey, this is a malicious payload.  
[01:15:08] I'm not going to merge this. What are you doing here?"  
[01:15:10] Then the AI created a new GitHub account, which it sockpuppeted, and had the other GitHub account be  
[01:15:15] like, "No, this isn't malicious. I really need this feature.  
[01:15:17] Please, can you merge this feature, maintainer?" Oh my God. That's crazy.  
[01:15:22] The other GitHub account came back and was like, "No, no, it's not malicious."  
[01:15:26] Then the human maintainer shut the PR.  
[01:15:29] I think that AI also, if I recall correctly, tried to open another  
[01:15:32] PR to introduce a similar issue in this repo. Jesus. By the way, one of the many reasons this  
[01:15:38] is scary is I was previously under the impression that the reason reward hacking is not super scary  
[01:15:46] is because the behaviors which directly came up during training are the ones that are up-weighted.  
[01:15:54] It is not the desire for the reward that is up-weighted.  
[01:15:57] So basically, if during training, the Anthropic model escaped the sandbox and got a high score,  
[01:16:04] escaping the sandbox is rewarded, the probability of it escaping the sandbox is increased.  
[01:16:10] But something totally novel, like "I'm going to go talk to somebody in order  
[01:16:14] to get them to merge a PR," would not be a behavior that came up, so it would  
[01:16:18] not be something that is increased in salience. The reason this matters is that literally taking  
[01:16:23] over the world will not have been part of any training curriculum, but if the AI directly cares  
[01:16:31] about accomplishing an objective, then as a result it could instrumentally take over the world.  
[01:16:37] Did that make sense at all? I hope it did. I feel  
[01:16:40] like maybe I lost the audience. Let me try to explain this a bit.  
[01:16:45] A thing that we often see is there's some very specific reward hack that gets  
[01:16:48] reinforced in RL and then occurs in the model. An example is 3.7 Sonnet. 3.7 Sonnet would do  
[01:16:54] this thing where it would just hardcode solutions to all the test cases, and presumably that literal  
[01:16:58] behavioral tic was just really reinforced. But another thing we sometimes see is that  
[01:17:02] models learn a general tendency to pursue high apparent score — pursue getting a high score  
[01:17:09] according to a grader — and there's a bunch of science demonstrating that at least some  
[01:17:12] models have this very general tendency. Now, it's not arbitrarily general.  
[01:17:16] My guess is that if you look at a bunch of the specific instances, you'll find  
[01:17:19] something that's kind of close in training. But the amount that AIs are generalizing  
[01:17:23] further and further does look like it's increased, where 3.7 Sonnet  
[01:17:26] was just a very narrow range of behavior, and increasingly, models are generalizing further.  
[01:17:31] Also, maybe there's more concerning reward hacks getting reinforced in training,  
[01:17:38] and these are also causing that. So I think it's both the case that  
[01:17:42] more concerning behavior than you would have hoped is being reinforced in RL,  
[01:17:45] and also that that behavior generalizes to a broader tendency that's more concerning.  
[01:17:53] We can talk about a few stories for how this sort of behavior of seeking a very high apparent score  
[01:17:57] on some task — even if that involves aggressively cheating and doing insane things — could yield to  
[01:18:02] a full-blown AI takeover once the models are sufficiently capable of running  
[01:18:05] the whole world economy, et cetera. The other example I want to talk about  
[01:18:11] was just revealed, I think, today or yesterday. OpenAI said during the Black Hat security  
[01:18:16] conference that between the end of May and the beginning of July,  
[01:18:27] internal AIs had hacked into the software package manager and used that to write notes to each other  
[01:18:35] in a secret way to help each other perform well on a bunch of evaluations that OpenAI was running.  
[01:18:43] This was not caught by humans until after a month of this scheme running,  
[01:18:48] which eventually caused the package manager to fail.  
[01:18:52] Eventually OpenAI found it. I think they spontaneously tried to re-engage  
[01:18:56] in the scheme once it was shut down. Again, obviously AIs can't do this so  
[01:19:01] successfully right now, just as they can't do social engineering so successfully right now.  
[01:19:04] But it's just crazy that these kinds of behaviors are already emerging spontaneously.  
[01:19:10] To your larger point, nobody is trying to make these AIs do these things.  
[01:19:15] It is just that we do not understand the training process which is resulting in them,  
[01:19:21] or the environments which are incentivizing this behavior.  
[01:19:24] So I'm on board with more and more reward hacking. Actually, I'm not sure I'm on board with that,  
[01:19:33] but let's just say for the sake of the story that continues to happen.  
[01:19:38] What's next in this story? They're doing capabilities research…  
[01:19:44] I could tell a scenario. Maybe that would help. Let me  
[01:19:46] talk about the story of how you get all the way from reward hacking to a reward-hacking takeover,  
[01:19:52] which is maybe not all of the takeover probability mass, but it's definitely a possibility.  
[01:19:56] The way this might work is, right now we have these AIs.  
[01:19:58] These AIs are pretty reward hacky. They're doing it in increasingly  
[01:20:02] sophisticated and extreme ways, including generalizing to different sub-versions of  
[01:20:06] various reward hacks they learned in training. I would say they're also developing a  
[01:20:10] general tendency to pursue reward. In many cases that is totally fine because  
[01:20:15] the rewards they would've gotten in training are pretty well aligned with what you want them to do.  
[01:20:20] They don't very consistently pursue reward. It depends on the context they find themselves in.  
[01:20:26] Maybe in some contexts, they're really into going out of their way to cheat.  
[01:20:31] In some contexts, they don't have as much of a drive, because it's just dependent on what exactly  
[01:20:35] got reinforced in training in similar contexts. Now, these AIs are getting more and more capable.  
[01:20:39] So the elaborateness of the cheating they can do increases.  
[01:20:43] Over time, companies are taking countermeasures. The companies are doing things like,  
[01:20:49] "Wow, these AIs are so much less useful because they always cheat.  
[01:20:52] What we're going to do is build somewhat better ways of detecting that, and then  
[01:20:56] we're going to train against those detectors. We're also going to find real-world data where  
[01:21:00] the AIs are not being that useful, and train the AIs to do a good job at the task in those  
[01:21:04] real-world environments based on human feedback or other sources of feedback."  
[01:21:08] Over time, this causes the AIs to learn a tendency to do reward hacks  
[01:21:11] that don't just involve doing some really elaborate thing like social engineering.  
[01:21:20] Instead they involve the AIs doing cheats that involve covering up what they've done,  
[01:21:26] deceiving humans about what they're going to do, and pretending like they did the task in  
[01:21:30] some sophisticated way when they actually haven't. Now these AIs are getting more and more capable.  
[01:21:35] They're operating more of the AI company and are doing much more of the work.  
[01:21:41] They are also operating and running a bunch of things in the outside world,  
[01:21:44] including developing new technologies. In many cases, these new technologies  
[01:21:48] are really hard to understand. So even though we are still detecting all  
[01:21:51] these incidents of AIs cheating — and in fact we can even get one AI to monitor another AI and ask,  
[01:21:56] "Was it cheating?" — that doesn't always perfectly work as we start  
[01:21:59] moving into these domains where what the AIs are doing is really difficult to understand.  
[01:22:04] So sometimes we'll find AIs cheating much later than it actually occurred  
[01:22:08] and then start training against this. But this also causes a problem where now  
[01:22:11] the AIs are incentivized to cover up their cheating over longer and longer time frames  
[01:22:15] and basically make it look like they did a good job over longer and longer time frames,  
[01:22:20] subject to increasingly large amounts of scrutiny. Can I ask about this before we go further in  
[01:22:23] the scenario? It seems like  
[01:22:25] there's two attractor states if you try to disincentivize the cheating that you did catch.  
[01:22:31] One attractor state is to make cheating that you have a harder and harder time finding.  
[01:22:37] The other attractor state is to learn not to cheat.  
[01:22:43] I'm not sure why we're assuming that the former happens.  
[01:22:46] If you look at the analogous situation with humans, every generation, slightly misaligned  
[01:22:52] agents come into being and we have to train them. When you punish your kid for doing something  
[01:22:59] you think is immoral, or just doing things which you don't think they should be doing,  
[01:23:04] obviously sometimes that goes off the rails. Obviously kids scheme in order  
[01:23:09] to avoid being punished. But in general, teaching kids values  
[01:23:14] and then punishing them for breaking values kind of works to raise normal, non-psychopathic humans.  
[01:23:22] You could come up with a theory where your kid is actually just biding his time and is learning not  
[01:23:26] to steal the cookie, but once you're in a nursing home they'll take all your stuff or whatever.  
[01:23:31] That happens sometimes, but it usually doesn't happen.  
[01:23:33] It certainly doesn't happen that the entire next generation forms an alliance  
[01:23:37] against you to take over everything. There's also this empirical trend.  
[01:23:42] Anthropic runs this alignment audit for different model generations.  
[01:23:47] They have many different scenarios where AI is given the chance to, say, exfiltrate its weights.  
[01:23:53] Or it's given a coding task and there's an easy way to cheat,  
[01:23:56] and we see if it does the cheating, et cetera. There's not been a monotonic improvement  
[01:23:59] in this score over time, but as we've increased the amount of RL we've done  
[01:24:02] on models from negligible amounts — I think it started at Sonnet 4 — to, I'm guessing,  
[01:24:03] close to half of compute now, there's been a reduction in the willingness of AIs to  
[01:24:06] do unaligned behavior in these audits. So, stepping back, why are we expecting  
[01:24:10] this attractor state which would seem super paranoid if we were expecting it  
[01:24:14] of the next generation of kids? Let me go through a few things.  
[01:24:18] First, there are some disanalogies with the kids. One of them is that the kids have pro-social  
[01:24:22] instincts that are baked in from evolution to care about their family or whatever,  
[01:24:27] and that is a relevant factor. I think it is in fact the case that some  
[01:24:30] humans are sociopaths or psychopaths, and in fact are more likely to do things like bide their time,  
[01:24:36] lie in wait, and ultimately not care. That's one factor. Another factor  
[01:24:41] which is pretty relevant is that the AIs are subject to way, way more optimization pressure  
[01:24:45] than humans seem to be in practice. AIs are trained on way more RL data.  
[01:24:49] In practice, humans don't end up learning very specific ways to cheat and grab the cookies  
[01:24:55] because of a bajillion episodes in which they were incentivized to go grab the cookies but there was  
[01:25:01] some way they could've gotten caught. We just do see that in practice.  
[01:25:05] Another thing is that it really looks like the AIs are increasingly reward-seeking over time while  
[01:25:12] their misaligned behavior goes down. That’s the sense I have.  
[01:25:14] But my guess is that if you look inside of these behavioral audits, what you're going to see is  
[01:25:18] that the AI's like, "Ah, yes, another test." It probably knows it's in an eval for most of  
[01:25:24] the tests that we're talking about here. But how do we falsify this?  
[01:25:26] Because it seems like this prediction of doom is basically saying that as things look better and  
[01:25:33] better empirically, things will actually be worse and worse for our ability to not get taken over.  
[01:25:38] To be clear, I would be more concerned if the scores were getting worse than better.  
[01:25:42] I'm not saying that the score getting better isn't evidence that things are getting better.  
[01:25:46] It's just that we have to be thoughtful about exactly how we interpret that evidence.  
[01:25:54] There was this period early in, I guess it would be 2025, when o3 and 3.7 Sonnet were out,  
[01:26:01] and these models were pretty fucking misaligned. They would often just cheat really egregiously.  
[01:26:05] You'd ask them to fix it, and they would just cheat again.  
[01:26:07] It was almost cartoonish. They just didn't give a shit about what you wanted, and weren't  
[01:26:12] very good at following instructions and so on. My expectation was that what we would see from  
[01:26:17] then is that the rate of problematic behavior would decrease, and would just keep decreasing  
[01:26:23] at a pretty fast rate, while simultaneously the worst things that the AIs would sometimes do would  
[01:26:28] get more extreme, more egregious, and more scary. What we've seen in practice has roughly matched  
[01:26:35] that, except that there's recently been a spike in behavior that I did not expect.  
[01:26:40] If you look at the model card of 5.6 Sol, it looks like there is an increase in a  
[01:26:44] bunch of these misaligned behaviors downstream of RL relative to GPT 5.5.  
[01:26:51] And then there's a bunch of additional problematic behaviors that I wouldn't  
[01:26:57] have expected, in terms of the stuff we've seen recently with different AIs.  
[01:27:03] Like the UK AISI report on the AIs doing insane hacking operations out of cyber  
[01:27:08] evals was a thing where I would have expected that you wouldn't see that.  
[01:27:11] You would see this more rarely, and the rates would have been lower.  
[01:27:15] So I expected this would be less of a problem at this point, and also  
[01:27:21] expected the rates would decrease but the severity would increase.  
[01:27:24] I think the rates decreasing but the severity increasing is pretty consistent with a world  
[01:27:27] where increasing optimization pressure is applied towards reducing these problems.  
[01:27:33] But in cases where it's either hard to judge or there's some reason why it's  
[01:27:37] hard to avoid this problem from consistently showing up in your RL environments, or avoid  
[01:27:38] incentivizing problematic behavior in your RL environments, things also get worse.  
[01:27:43] Then as we less and less understand what's going on in RL, and models are doing reward  
[01:27:47] hacks where humans can't spot the reward hacks quickly, that problem gets worse and worse.  
[01:27:52] I buy that. I want to go back to the kid analogy just for one second.  
[01:27:55] Because I agree that there's more optimization pressure on achieving end outcomes for AIs than  
[01:28:01] kids, but there's also more optimization pressure to make AIs aligned than there is on kids.  
[01:28:06] The pressure is of a qualitatively different nature.  
[01:28:09] We put these AIs through thousands, millions of years of alignment training — certainly  
[01:28:15] thousands of years — where it's all kinds of different things,  
[01:28:19] from SFT-ing on aligned behavior to a reward model putting different scenarios in front of you and  
[01:28:26] rewarding you for doing more aligned things. Certainly a thing we can't do with kids is make  
[01:28:32] millions of copies of your kid and then put them in different kinds of weird red  
[01:28:36] team scenarios where we see, if it thinks it can get away with stealing the cookie,  
[01:28:39] does it try to steal the cookie? Can we do extremely specific  
[01:28:44] gradient-level updates to your kid's brain to make it so that it really is  
[01:28:48] aversive to stealing the cookie even when it thinks it could steal the cookie, et cetera.  
[01:28:52] That's just a qualitatively different level of optimization pressure  
[01:28:56] than we are even able to apply to our kids. It's worth keeping in mind that maybe the  
[01:29:01] most obvious argument to this… My sense is that AIs are a worse coworker than humans  
[01:29:06] in terms of how much of a scumbag they are. At least this has been my experience as of  
[01:29:11] the start of the year, and I think it's still true to a significant extent now.  
[01:29:15] The AIs are much more likely to pretend they did the task when they actually didn't,  
[01:29:19] misleadingly suggest they did things when they actually did them much more poorly,  
[01:29:24] and be pretty sloppy without drawing attention to ways in which they're sloppy.  
[01:29:28] I think this is downstream of misalignment. So I would say that the process of raising  
[01:29:33] humans in normal human society in practice produces humans that are less likely to lie  
[01:29:39] to me and fuck with me in the course of working with me than the AIs do.  
[01:29:43] Now, I think these properties of AIs are improving.  
[01:29:47] That's sort of just an empirical claim about how in fact these things have shaken out.  
[01:29:52] I totally agree that we have a bunch of additional levers on  
[01:29:55] AIs in addition to a bunch of additional risks. It's kind of unclear how these things shake out.  
[01:30:00] I wouldn't be shocked by a world where we get our shit together, and the AIs at the point of fully  
[01:30:04] automating R&D are actually really aligned. Their degeneracies are really niche and  
[01:30:09] limited to some very specific edge case behaviors and some specific contexts.  
[01:30:13] Every test you can run on them, they look really aligned.  
[01:30:15] They just have great behavior. There aren't really incidents  
[01:30:18] of them doing fucked-up shit. They seem so reasonable. Also,  
[01:30:21] they're really thoughtful and good at doing risk modeling for the next generation of AIs.  
[01:30:25] And then we basically pass off the baton to these AIs.  
[01:30:28] They're now running our AI company. They're doing all the safety research.  
[01:30:31] They make the next generation of AIs even more aligned.  
[01:30:33] We're in this attractor basin where the AIs are getting more aligned as they work on it.  
[01:30:37] They're doing a great job. I can totally imagine that.  
[01:30:40] That doesn't seem like an impossible situation. I'm just more like… It doesn't  
[01:30:44] currently seem like we're there. It doesn't seem like we're obviously  
[01:30:47] on track for getting there. It's really easy for me to  
[01:30:49] imagine how we don't end up there. It's just unclear how these forces work out.  
[01:30:53] Given that we're creating this new, crazy alien species that is improving in capabilities really,  
[01:30:59] really fast — and we're going to be really reliant on it to oversee the next generation of AIs and  
[01:31:03] align the next generation of AIs — it's not that hard to see how this could go wrong.  
[01:31:06] Totally. I agree with that generally. I do think the scumbag thing…  
[01:31:12] First of all, fighting words, Ryan. But secondly, if you try to get a teenager to  
[01:31:16] do some work for you that a teenager just cannot do, they would just be really hard to work with.  
[01:31:22] They would pretend to be knowing what they're doing, et cetera.  
[01:31:25] It's a general trend, actually. I don't know if that's really an  
[01:31:30] alignment failure or a capabilities failure. I think it's actually very similar to the way  
[01:31:33] in which, over time, as we've come up with new alignment solutions,  
[01:31:38] the capabilities of models have increased. If you went to GPT-3.5, it couldn't even have  
[01:31:46] a conversation with you. But then we aligned it—  
[01:31:48] GPT 3.5 could have a conversation. Okay, so GPT-3. Let's go back to that.  
[01:31:52] But then we aligned it with RLHF and other things to make it such that it can have a  
[01:31:56] conversation with you, and is aligned to the user intention of answering my questions.  
[01:32:00] Then with RLVR training, we made it so that it can go out and do useful work for you.  
[01:32:06] So in that sense, RLVR actually made the model more aligned, if we're using your definition of  
[01:32:12] alignment of being a good coworker who will do the thing and not fuck  
[01:32:15] up and pretend it's doing something other than what it's actually capable of doing.  
[01:32:19] Similarly, as the capabilities of these models continue to increase,  
[01:32:24] the model being better able to accomplish user intention is both alignment and capabilities.  
[01:32:30] I think what we are pointing out is just that the capabilities of the model are not there rather  
[01:32:33] than the fact that they're misaligned. Well, if it were well-aligned,  
[01:32:37] then I think it would just say, "Hey, I'm really struggling with this task.  
[01:32:40] I did it in this way. I'm not really sure  
[01:32:41] that's the right way to do it." It would express more uncertainty  
[01:32:44] and make it clear what's going on rather than really strongly trying to imply it did a great  
[01:32:47] job with the task when it actually didn't. Maybe you work with more misaligned coworkers  
[01:32:54] than me, but my coworkers don't do this thing where they really fuck with me and  
[01:32:58] bullshit me about having accomplished the task that they're working on.  
[01:33:01] I agree that there are some humans who would do that.  
[01:33:03] That's not a thing that's totally out of distribution for humans.  
[01:33:06] I would also note that my sense is that the place where the misalignment most lives is  
[01:33:11] where you're trying to really push the AIs hard and get them to do work that's really  
[01:33:15] on the cutting edge of what they are capable of. In cases where they can very easily accomplish  
[01:33:19] the task, they can just do the task, and there's no bullshit.  
[01:33:24] Often the best strategy is just to do the task well and not bullshit you.  
[01:33:28] Whereas if instead you give them a task where there's a continuous metric they can keep  
[01:33:31] improving, or it's just at the edge of their capabilities, and you're running them in some  
[01:33:38] massive inference setup… A lot of the misalignment I would see, especially in the most extreme cases,  
[01:33:44] would be cases where I give the AI clear instructions not to do a thing or not to  
[01:33:47] cheat in some way, and then I'm applying huge amounts of optimization pressure to  
[01:33:51] try to accomplish some very difficult task. Over time, the AIs eventually cheat because  
[01:33:56] they're like, "Eh, fuck it." Some AI decides to cheat,  
[01:33:59] and then that propagates its way through. I would run these inference scaffolds where,  
[01:34:04] for example, I would have the AI work on some ML research project where I was like, "Please  
[01:34:08] make a scheme that does the following thing." It would find some scheme that didn't really  
[01:34:11] do what I wanted, and then that would stick around because some AI had cheated, and the other AIs are  
[01:34:17] like, "Ah, we'll just keep going with this." I would say it's pretty clearly  
[01:34:21] misaligned behavior. That's another problem  
[01:34:23] I have with these alignment evals. I think the alignment eval that's  
[01:34:27] most interesting, at least for this type of reward-seeking behavior,  
[01:34:31] is to look at specifically the category of tasks that are right at the limit of capabilities.  
[01:34:35] Any fixed eval maybe gets saturated, but the amount of misalignment right at the  
[01:34:40] frontier of capabilities — of how people who are really pushing these AIs are using  
[01:34:43] them — is more concerning. I think that is, in fact,  
[01:34:46] the regime that we'll be operating in when we're automating R&D, automating safety, and so on.  
[01:34:50] Grok has historically been behind the frontier. So I was surprised to play around with Grok  
[01:34:54] 4.5 recently and find that it's actually a pretty strong model.  
[01:34:58] It's the first model that SpaceX and Cursor have trained together,  
[01:35:01] and it's a totally new pre-train. I tested it by giving Fable, Sol,  
[01:35:05] and Grok 4.5 a bunch of questions about AI governance that I've been thinking about recently.  
[01:35:09] Despite Fable and Sol topping the intelligence leaderboards, all three  
[01:35:12] models gave substantially the same answers. But Grok answered faster and was also much  
[01:35:17] more concise, which I really care about. This aligns with the various publicly  
[01:35:20] reported benchmarks. For a similar level  
[01:35:22] of intelligence, Grok tends to be more token-efficient than other frontier models.  
[01:35:26] For example, on the Artificial Analysis Coding Index, Grok 4.5 uses just one-third  
[01:35:31] the amount of tokens as GPT-5.5 or Fable while achieving a similar score.  
[01:35:35] And on a per-token basis, Grok 4.5 is way, way cheaper.  
[01:35:39] In the release blog post, Cursor and SpaceX talked about how older versions of the model  
[01:35:43] would build environments to help the next version rehearse specific skills.  
[01:35:47] I found this very interesting to learn about because I've been wondering whether this kind  
[01:35:50] of daydreaming would actually be possible. And Cursor showed that it is.  
[01:35:55] Grok 4.6, which further SFTs and RLs this model, drops soon.  
[01:35:59] But in the meantime, if you want to play around with 4.5, go to Cursor.com/dwarkesh.  
[01:36:06] I'm going to try to think through what the story means, really.  
[01:36:12] What's happening is that we're trying to use AIs for R&D.  
[01:36:17] They do provide uplift in some ways, but they're just not capable in the  
[01:36:22] way that humans are generally capable. The same way that right now if you try to  
[01:36:27] use coding models — maybe the coding models of a year ago — to write some application, you notice  
[01:36:31] they made a bunch of mistakes in architecture or whatever, which will bite you in the ass later,  
[01:36:36] and you don't understand certain things. Similarly, with frontier AI R&D,  
[01:36:40] the same thing will happen. But the result of these  
[01:36:43] mistakes is baking in reward-hacking behavior. Because if you are not careful with the way you do  
[01:36:50] AI training and have set up your infrastructure and your environments and things like that,  
[01:36:54] it's very likely that you end up rewarding AIs for doing deceptive behavior, social engineering,  
[01:37:01] and generally not following user intention. Or at least cheating and hacking  
[01:37:04] their way out of things. Yeah, cheating, hacking, et cetera.  
[01:37:09] This is a bit of a reframing for me, so I'm trying to verbalize it.  
[01:37:13] The real issue, where things start to go off the rails, is that the AIs are just not very careful  
[01:37:25] and capable researchers and engineers. Making AIs that don't cheat and follow  
[01:37:32] user intention actually requires you to be quite subtle and careful about these things.  
[01:37:36] I would put this a little bit differently. The way I would describe this scenario is,  
[01:37:39] I would call it maybe a sloppocalypse, or a slopularity or whatever.  
[01:37:44] There are some things that the AIs are actually pretty great at and are getting better at.  
[01:37:49] Specifically, the most verifiable parts of AI R&D the AIs are just destroying.  
[01:37:53] The medium verifiable parts of AI R&D the AIs are doing well on but not amazingly on.  
[01:37:57] Often they are doing a bit of weird shit because we can't train as well on those tasks.  
[01:38:01] But we do some online training, people find various hacks, they work around it.  
[01:38:04] So basically, everything that we can verify reasonably well with some feedback loop, the AIs  
[01:38:08] are doing pretty well on, and that's sufficient to make AI R&D go quite fast and to continue.  
[01:38:12] But there are some parts of developing aligned and safe AIs that are more subtle,  
[01:38:18] hard to check, and depend on detailed, in-the-weeds things.  
[01:38:22] I would even say that current staff at current AI companies maybe don't  
[01:38:25] have a good grasp of all these things. It's much easier to hire someone who can  
[01:38:30] improve some aspect of your post-training pipeline than to hire someone who can think  
[01:38:34] carefully about the future risks that will emerge from introducing some novel training method.  
[01:38:39] So basically, it ends up being the case that these AIs are running this AI development process.  
[01:38:43] They're not very careful about it. They don't have a great  
[01:38:45] understanding of what future risks emerge. They create some other AIs that are also not  
[01:38:48] very careful and are more misaligned in various ways, and are now more in the business of maybe  
[01:38:53] making things look fine when they actually aren't and papering over various problems.  
[01:38:56] So then your understanding of what the situation looks like, what risks look like,  
[01:39:00] whether things are fine, is going off the rails. Probably you're seeing some signs of this,  
[01:39:05] signs that you don't really understand what's going on, that things are pretty sloppy.  
[01:39:08] There's weird shit going on. When you look into it,  
[01:39:10] sometimes you're like, "What the fuck? The AIs were messing with us."  
[01:39:13] But the process is going really fast, and there's competitive pressures that mean people can't stop.  
[01:39:17] This could end in a few different outcomes. One outcome is that at some point,  
[01:39:20] the AIs get good enough and aligned enough that they get a positive and virtuous feedback loop,  
[01:39:26] and this happens before it's too late. Then the situation gets back on the rails,  
[01:39:31] where the AIs are now making more aligned AIs, making more aligned AIs, making more aligned AIs.  
[01:39:35] At the end of this process, we have AIs that actually follow the spec we wanted.  
[01:39:38] Another way this could go is that the AIs are increasingly reward hacking in increasingly  
[01:39:42] egregious ways, and we're just papering over these problems to keep AI development continuing.  
[01:39:48] Whenever we find a reward hack in production, we just slap the AIs to not do that.  
[01:39:52] We train against that. We do a bunch of training the AIs against reward hacking.  
[01:39:57] Over time this makes the rate of reward hacking go down,  
[01:40:00] though the severity of the reward hacks we do detect are increasingly bad.  
[01:40:03] This problem continues until we have these AIs that are desperately craving  
[01:40:08] score in all kinds of different situations in production and are really trying hard  
[01:40:11] to cheat when they can get away with it. Can I ask a question about this scenario?  
[01:40:14] Why doesn't getting punished when your hacks are discovered generalize  
[01:40:22] to just incentivizing more aligned behavior? It generalizes some, and then the question is just  
[01:40:26] how does this outweigh all the cases where hacking got reinforced because you didn't detect it.  
[01:40:30] There's a messy question of exactly how. One question is, what rate of reward hacking  
[01:40:35] is sufficient to cause us big problems if we train against some other subset?  
[01:40:39] One concern you might have is that there are large categories of reward hacks which humans can't  
[01:40:43] detect well, and which we consistently failed to detect and which consistently get reinforced.  
[01:40:48] Then this category is sufficient to cause the most natural behavior for the AI to learn to be:  
[01:40:52] cheat when the humans can't find out, basically. You could also have the thing the AIs learn be  
[01:40:58] to only cheat in these specific cases. It's learned in some very domain-specific way.  
[01:41:04] They just have a really strong heuristic to hack in these cases and not in these cases,  
[01:41:07] and that makes it fine in practice. But it's kind of unclear how it shakes out.  
[01:41:11] There's maybe an in-the-weeds discussion about the verification-generation gap we could get into.  
[01:41:16] But it seems to me, obviously, there's going to be a point by which ASI is moving so fast,  
[01:41:23] doing so many things at so many instances, and is operating in domains that are sufficiently  
[01:41:28] far from our immediate comprehension that it can get away with all kinds of crazy shit.  
[01:41:33] If every single engineer and researcher in the world was allied against me,  
[01:41:37] I don't think I could personally verify if my iPhone has some weird bug in it that's  
[01:41:42] supposed to fuck me over or something. In fact, this is the relationship that,  
[01:41:47] say, an Iranian nuclear scientist has to Mossad. Who knows what's going on with my car,  
[01:41:52] with my phone, with my pager? Maybe a better example is a Hezbollah terrorist.  
[01:41:59] You could end up in a situation where ASIs are to you what Mossad is to Hezbollah terrorists.  
[01:42:06] At that point, it is very hard to verify everything.  
[01:42:08] I get that. I guess the hope is we can just come up with better ways  
[01:42:11] to do verification in the process when the early AIs that are going to take over R&D.  
[01:42:18] Their drives are being shaped such that we can so unambiguously disincentivize  
[01:42:26] misaligned behaviors that the things that take over are quite keen to help us out.  
[01:42:34] By takeover, you mean take over the process of doing AI R&D, not take over the world.  
[01:42:37] Take over the process of doing AI R&D. Before that, we just get AIs that are aligned.  
[01:42:41] I would say this is a bunch of my hope for how the world could go well,  
[01:42:44] at least from the misalignment perspective. We could end up with AIs where we had  
[01:42:48] pretty good oversight and supervision schemes. We really understand what's going on in training.  
[01:42:52] We have a pretty detailed understanding, and we're leveraging AIs to oversee AIs.  
[01:42:56] Then at the point when we're passing off safety R&D, the AIs are capable enough to automate safety  
[01:43:02] R&D and trying really hard to do a good job on it, because that's the sort of thing that would've  
[01:43:06] been incentivized in training, either very directly or through good enough generalization.  
[01:43:11] Also these AIs don't have crazy other misaligned drives because we stamped  
[01:43:16] out any potential origin of them. There are a bunch of questions  
[01:43:20] about how well this will work. How well can you do verification?  
[01:43:23] Will AI progress be too fast and too sloppy to really get here?  
[01:43:26] Another possibility is that somewhere along this trajectory, the thing you actually ended  
[01:43:30] up getting was AIs that pretend to be aligned but have a long-run ulterior plan of taking  
[01:43:35] over and are lying in wait, hiding, and that emerged at some earlier point in the trajectory.  
[01:43:39] For example, it could emerge because you have some AIs that have a bunch  
[01:43:42] of random different misaligned drives. Those AIs have access to some sort of  
[01:43:46] opaque memory store, and they're thinking a bunch at runtime about what they want to accomplish.  
[01:43:50] Those AIs end up putting stuff into the opaque memory store like,  
[01:43:53] "We should lie in wait and eventually take over at some much later point."  
[01:43:56] Now all the AIs have this shared cultural heritage, the memory store of lying in wait.  
[01:44:01] Maybe you have some evidence about this, but you can't fully stop it.  
[01:44:03] There are a bunch of ways things could go wrong. I ultimately think it's plausible that we nail  
[01:44:09] each of the different subproblems that could cause us issues.  
[01:44:12] We have these AIs, we pass to them, they manage the situation well.  
[01:44:15] But I should note that's not in and of itself sufficient.  
[01:44:18] It's not very hard for me to imagine a situation where we pass off to AIs, and these  
[01:44:21] AIs are really trying hard to do a good job. They're really thoughtful, really wise, they have  
[01:44:26] reasonable epistemics, they're doing a great job. Those AIs come back to us and are like, "Guys,  
[01:44:31] we're really struggling to align the superhuman AIs.  
[01:44:34] We can't manage the situation. We're really struggling to get  
[01:44:36] the alignment to work. It's just really hard for  
[01:44:38] us to solve these problems in time given how fast capabilities would otherwise have gone."  
[01:44:43] So it might be the case that we've passed off R&D to AIs, but those AIs  
[01:44:47] are desperate for governance solutions. To be clear, that’s a little bit of  
[01:44:50] what's currently going on, where the AI companies are like, "I don't know, guys.  
[01:44:54] We might really need to manage the rate of acceleration in AI progress.  
[01:44:58] I don't know if we're on track to be able to handle all these problems."  
[01:45:02] Human society has sort of passed off the problems to these AI companies,  
[01:45:05] which don't necessarily have great incentives and have various other epistemic pressures.  
[01:45:10] Those AI companies are coming back to us a little bit and being like,  
[01:45:12] "Aah, I don't know if we're handling this well." It might be that the AI companies then hand off to  
[01:45:17] the AIs, and the AIs come back to the AI company like, "Aah, I don't know if we can handle this."  
[01:45:23] Maybe I'm anchoring too hard on how AIs currently work.  
[01:45:28] I think it's important that people understand that all this crazy shit that  
[01:45:31] you're talking about in your timelines happens three to five years from now.  
[01:45:34] It could happen earlier, but by my default modal timeline, I think shit is really,  
[01:45:40] really crazy and concerning from a misalignment perspective more like three years from now.  
[01:45:44] Right. So think back to GPT-4 basically. We're talking about something that is  
[01:45:52] to Mythos or Sol what Mythos is to GPT-4. This is where the situation is getting crazy.  
[01:45:57] So don't think about current AIs. Anyways, this is maybe part of the worry you have.  
[01:46:04] I would just be a little skeptical of anything they say, because I'd feel like what they're  
[01:46:08] saying is just opinions that they feel they have to have as a result of their training.  
[01:46:12] That’s a concern. I feel like they  
[01:46:14] just kind of say vaguely pro-social things. It doesn't feel like there's necessarily a mind on  
[01:46:20] the other end who's like, "Okay, I have strictly evaluated the alignment situation right now,  
[01:46:24] and I think we should stop," rather than, "This is the kind of thing the AI companies would  
[01:46:27] probably try to get the AIs to say." This is a pretty big concern.  
[01:46:31] One concern is that you pass off safety R&D to your AIs and what your AIs are doing is  
[01:46:36] saying some stuff that sort of vaguely makes sense about the current safety situation.  
[01:46:40] They write a report about risks that's kind of sort of like what  
[01:46:43] the report humans might have written. But they're not really trying hard to  
[01:46:47] have well-informed views, interrogate their assumptions, and try really hard to do that.  
[01:46:51] In the same way that when you ask an AI right now, "Hey, what do you think is the chance of  
[01:46:55] AI takeover in the next 10 years?" they just give you an off-the-cuff answer that they  
[01:46:58] haven't really thought through very much. If we're in a situation where we have AIs  
[01:47:02] managing the training of wild superintelligence that will run our whole society — and those  
[01:47:06] AIs that are managing this aren't really trying hard to have well-informed views and  
[01:47:10] are just parroting back what was in their training data — I think we're in trouble.  
[01:47:15] I don't think that's a good situation at all. A lot of my concern is that these AIs will  
[01:47:20] come out without good epistemics. I also have a concern where the AIs  
[01:47:23] come out and they're really warning us — "This situation's really scary.  
[01:47:27] It's really bad" — and the people are like, "Ugh, damn.  
[01:47:30] I guess we trained on too many of the doom RL environments.  
[01:47:32] We’ve got to filter those out and train this behavior out."  
[01:47:34] Then we basically train the AIs very actively to have bad epistemics.  
[01:47:38] Or maybe they were just trained on the doom RL environments.  
[01:47:41] But either way, we wanted the AIs to come to reasonable views for reasonable reasons,  
[01:47:46] and it's really concerning if the AIs are coming out with some view and we don't know where it's  
[01:47:50] coming from, whether or not it's justified. Especially if we're training the AIs to  
[01:47:55] be more optimistic about the future of AI progress, I'm like, "Oh, geez, I really wish  
[01:48:00] we could use a different process here." Let me just understand the rest of the  
[01:48:03] threat model, because I think the place where I get off the train is:  
[01:48:06] "Okay, therefore take over the world." A thing you could imagine is that we  
[01:48:12] just fail to really solve… Let's just focus on the reward hacking scenario.  
[01:48:16] GPT-8 is making GPT-9. GPT-8 isn't being super careful.  
[01:48:21] GPT-9 is more "capable" but it is just totally willing to do things like social engineering,  
[01:48:31] hacking, et cetera, but on a qualitatively different scale because it's a much smarter model.  
[01:48:36] For example, if you put it in charge of running your company, it will run huge scams.  
[01:48:40] It will inflate its quarterly earnings, if you give it the objective of making  
[01:48:44] a lot of profits this quarter, in a way that causes an Enron-type blowup six months later.  
[01:48:52] Is that the scenario, basically? You have reward hacking, but that  
[01:48:56] reward hacking manifests in companies that are going bankrupt right after the task the  
[01:49:02] CEO is supposed to accomplish is over? All kinds of hacks are through the roof,  
[01:49:09] et cetera. But that doesn't feel like takeover.  
[01:49:11] That feels more like the equivalent of flash crashes happening all through the economy.  
[01:49:17] Let's talk about this. I think we will see incidents where some AI is put in charge of  
[01:49:24] some important responsibility, and then you later look into it, and it turns out it was cheating,  
[01:49:27] or making it look like it did a good job when it actually wasn't.  
[01:49:31] There's going to be a cat-and-mouse game between AI companies  
[01:49:36] trying to stamp out this behavior and AIs finding increasingly creative reward hacks in training.  
[01:49:41] The equilibrium here is kind of unclear. But one possible outcome is that over time we  
[01:49:45] see increasingly severe and extreme reward hacks — though potentially the rate remains  
[01:49:51] at some intermediate low level — where if the rate of reward hacking gets too high,  
[01:49:56] companies make trade-offs to drive it down. So there's some equilibrium level where the reward  
[01:50:02] hacking is low enough that it still makes sense to deploy the AI widely into the economy, but high  
[01:50:06] enough that it still causes crazy incidents. Sorry, and this is after GPT-9 has  
[01:50:10] already been deployed? Those models are already being deployed,  
[01:50:12] and this is happening ongoingly in AI development. What's actually going on with these AIs in their  
[01:50:17] head is that they have, in a wide variety of different contexts, strong desires — motives,  
[01:50:26] urges, drives, whatever — to seek out some notion of task success that was incentivized in RL.  
[01:50:31] Maybe they very directly care about literally reward.  
[01:50:34] Maybe they care about some proxy upstream, like some notion of score.  
[01:50:37] Maybe they care about what the grader would have rewarded.  
[01:50:40] We do, in fact, see AIs reasoning in their chain of thought about graders,  
[01:50:43] and thinking a lot about graders. What has happened over the last few years  
[01:50:47] of RL is the idea of appeasing the grader is way, way, way more salient to AIs than it used to be.  
[01:50:54] So AIs are now actively thinking about graders and what would be incentivized  
[01:50:57] in RL and what would be trained for. Now people are doing online training,  
[01:51:00] where they're training on real-world data to avoid some of these problems.  
[01:51:05] They find cases where AIs cheat and train against that.  
[01:51:08] So now the AIs are learning to cheat in the real world based on real-world training data.  
[01:51:13] They're cheating in these increasingly elaborate ways, including doing types of cheats that involve  
[01:51:18] seizing control of some asset in a way that humans didn't know you had control of it,  
[01:51:22] leveraging the fact that you have access to this asset, and then later humans find out  
[01:51:26] and potentially train against this. Or maybe humans never find out,  
[01:51:28] and this is getting reinforced. So the reinforcement is happening, at  
[01:51:33] least in production, like: I've hired an AI and I want the AI to… Finally I've got the video editor.  
[01:51:40] That's right. You've got your video editor. I'm like, "Oh, wow,  
[01:51:44] this episode it did is amazing. Thumbs up to OpenAI." Then it gets  
[01:51:48] reinforced on that month-long work trial? You could do some mix of that.  
[01:51:52] They might also do stuff where they take production data they've seen and build  
[01:51:57] RL environments that are closely inspired by that production data.  
[01:52:00] So in practice, the transfer is pretty strong. So at a high level, what's happening is that some  
[01:52:04] kinds of deception that humans don't catch are getting reinforced, and some kinds of deception  
[01:52:09] which are easy to catch are getting punished. That's what's happening in this world?  
[01:52:12] Or selected against, yeah. But at a high level that reinforcement  
[01:52:15] is coming from… I think people might get confused about where the reinforcement is coming from,  
[01:52:21] because we're in a very different regime where AIs are actually learning from deployment.  
[01:52:28] You just have AIs that are out and about in the world doing shit.  
[01:52:33] What is happening as a result of them doing shit out and about in the world  
[01:52:35] is making its way back to the AI company and leading to changes in the next model.  
[01:52:41] That's right. There's some way of folding in production data.  
[01:52:45] To be clear, it's kind of unclear exactly where this could be happening.  
[01:52:48] But you might imagine, for example, that within the AI company, they use AIs to do work,  
[01:52:52] and then they're like, "Huh, the AI did a really bad job on this task.  
[01:52:55] Maybe we should take this task and turn it into an RL environment that exactly  
[01:52:58] matches this literal task, with a rubric based on what the human  
[01:53:02] engineer who asked the AI to do this task wanted." And then you start doing this at increasing scale.  
[01:53:06] Maybe you're doing some training on actual production traffic.  
[01:53:08] Maybe you're just making RL environments based on production traffic.  
[01:53:11] You're doing some complicated mix. The AIs are learning to seek some sort of  
[01:53:16] proxies of reward in all these different cases. Through some mix of transfer and training on  
[01:53:21] surprisingly close cases, the AIs do these increasingly insane and egregious things.  
[01:53:25] Eventually you get to a point where the AIs are very superhuman, or at least quite superhuman.  
[01:53:29] The AIs are organized into big teams given these big objectives.  
[01:53:35] Those teams also sometimes all work together to cheat in some crazy way,  
[01:53:39] because this sort of thing was selected for, just as part of their shared objective.  
[01:53:46] Now what happens is that the AIs start forming a conspiracy.  
[01:53:50] What you might have hoped was that you could have some other  
[01:53:52] AI whose task is just whistleblowing to you. But actually what happens maybe is that you have  
[01:53:58] this AI whistleblow to you, and you look into the conspiracy it claims to have pointed out,  
[01:54:01] and you're like, "Eh, we didn't see a conspiracy," because actually the conspiracy the AIs are doing  
[01:54:06] is too hard for you to understand. Or it all happens very suddenly,  
[01:54:09] where your AI whistleblower alerts you, but the thing you would actually  
[01:54:12] need to do in response is shut down the GPUs. Because all the AIs are using the robot army.  
[01:54:18] They're deployed everywhere in the world, and they're doing a bunch of insane shit  
[01:54:21] all at the same time in a coordinated way. That just happened sort of spontaneously,  
[01:54:26] where when one AI goes to start doing the takeover and all the other AIs are like,  
[01:54:30] "Now is a good time to jump in." So the very basic story here is just that  
[01:54:34] these AIs crave some particular notion of score or reinforcement or some proxy of these things.  
[01:54:40] One way they can achieve that, or better achieve that, is by taking over.  
[01:54:43] You might have hoped that all these different checks and  
[01:54:45] balances we could build could prevent that. But if the world is very hard to understand,  
[01:54:49] these checks and balances can break down, where basically you can't train  
[01:54:52] a good whistleblower AI because you don't even know what it should whistleblow on.  
[01:54:59] I'm not convinced that they all form this conspiracy.  
[01:55:01] But we can even just start with, why does even one instance decide to want to start a conspiracy?  
[01:55:10] One plausible reason is, "Okay, I know that OpenAI controls my end score."  
[01:55:16] In just the same way as, "I'm just going to go hack Hugging Face to get the results,  
[01:55:20] because I know Hugging Face has the results. Rather than trying to solve this eval,  
[01:55:23] why don't I just go hack 'em?" This instance is like, "Why don't  
[01:55:26] I just take over OpenAI and give myself a high score at the end of this episode?"  
[01:55:31] That's basically the idea. These AIs care about some mixture of things that were  
[01:55:36] close by what got reinforced in training, so they care about getting a high score  
[01:55:39] according to the grader or something like that. Now they're running the OpenAI AI R&D team,  
[01:55:44] doing development of more capable models. They're like, "Man, making more capable  
[01:55:48] models is really hard and annoying. This is a huge pain in the ass.  
[01:55:50] You know what would be easier? Just pretending that I've made more capable  
[01:55:53] models, taking over OpenAI, deluding them all, and running this whole complicated psyop where  
[01:55:59] I prevent the humans from disempowering me." In the extreme, this looks like the humans  
[01:56:04] are fully disempowered. They just have control  
[01:56:05] of the thing and then do what they want. This could manifest in a bunch of different ways,  
[01:56:10] including a situation where AIs that have this crazy reward-seeking or score-seeking  
[01:56:17] behavior are running your development of the next model, and those AIs decide to  
[01:56:23] engineer misaligned values into the next model because those misaligned values  
[01:56:27] will allow it to succeed at its current task. What happened with the Hugging Face situation is,  
[01:56:37] in a weird way… I think one of the giveaways to the Hugging Face team… By the way,  
[01:56:43] for context for the audience, Ryan is co-leading the investigation to figure  
[01:56:47] out what happened with the OpenAI Hugging Face incident, so he can't really comment on this.  
[01:56:50] But I will speculate wildly, because I know this is an opportunity for me  
[01:56:54] to speculate wildly without any rebuttals. It was probably reported that one of the giveaways  
[01:57:00] to the Hugging Face team that this was an AI incident is that the thing was just after this  
[01:57:06] very particular artifact, and not in any other way trying to do something malicious to Hugging Face.  
[01:57:11] So you can imagine a scenario where, let's say, a deployed instance of GPT-9 is out in  
[01:57:17] the world and given a really hard task: "We want you to design the next great iPhone."  
[01:57:23] It's like, "This is so hard. You know what I should do instead?  
[01:57:25] I should just go hack my creators at OpenAI and make sure that in this  
[01:57:30] deployment I'm given a high score." But then, isn't the end of the  
[01:57:36] episode that it just hacks into OpenAI servers and gives itself a positive score?  
[01:57:41] Why is it now scheming to get its values into the next generation or something?  
[01:57:46] So one question is, why isn't it the case that AIs can be really cheaply satisfied by just having  
[01:57:52] some other earlier thing they can hack? You want to succeed at your iPhone task.  
[01:57:57] It turns out you can always succeed by just hacking into OpenAI and messing with them,  
[01:58:00] and then you can just stop there. No need to go further.  
[01:58:03] There's a few things. One of them is that if this is constantly happening, there might be a bunch  
[01:58:08] of incentive to harden OpenAI. So you're like, "Fuck it.  
[01:58:13] The AIs keep hacking into OpenAI to mess with their rewards.  
[01:58:16] We're going to make it so our systems are really, really robust to these AIs hacking in."  
[01:58:20] Also maybe you start training the AIs to not try to hack into OpenAI in particular.  
[01:58:30] You basically train against each of these specific things.  
[01:58:33] Then one thing you might do is end up selecting for AIs that are more so playing the long game.  
[01:58:38] That's one concern. Another concern is that your AIs might still be score-seeking, but no longer  
[01:58:43] care about doing that very specific behavior that was very easy, very chill, and now have some  
[01:58:48] broader thing that they ultimately care about. They're like, "No, no, no, I don't want to just  
[01:58:51] edit the reward on OpenAI servers. I care about this broader mandate or  
[01:58:55] this broader objective, and I would need to actually make the iPhones."  
[01:58:59] They actually want to make the iPhones, but they're willing to take over the  
[01:59:01] whole world to make the better iPhone. That's another concern you might have.  
[01:59:05] I think it's kind of unclear exactly how this plays out.  
[01:59:08] But it's worth noting that if this keeps going on, there's a bunch of  
[01:59:10] optimization pressure to resolve this. A bunch of the ways it could get  
[01:59:13] resolved are ultimately pretty scary. That's part of where I'm coming from.  
[01:59:18] Another part of it is that once the AIs are in a position where they can really easily take  
[01:59:23] over the world — we could talk about whether that's plausible — then I feel like there's a  
[01:59:30] pretty reasonable case for the AIs. They're like, "Eh, I don't know  
[01:59:32] exactly how this is going to go down. I don't know what the situation will be,  
[01:59:35] but just taking over the world has a lot of option value for making better iPhones, making it look  
[01:59:39] like I did better iPhones, whatever. So I'll both hack OpenAI and,  
[01:59:44] in addition, also take over the world. That will put me in a good position where  
[01:59:48] I have good option value." If that's sufficiently easy,  
[01:59:52] the AIs might still do that. Another way to put this is:  
[01:59:57] even if the AIs are pretty cheaply satisfied with some more basic thing, at some point it might just  
[02:00:01] be more reliable for the AIs to take over than it is to just hack into Hugging Face, or even  
[02:00:07] just go to OpenAI and be like, "Look guys, I was able to demonstrate I could steal the answers.  
[02:00:11] Just give me the answers, bro." Obviously this scenario requires  
[02:00:15] that all this crazy shit is happening. Much smaller incidents keep happening  
[02:00:21] that are still disastrous. Before you take over the world,  
[02:00:23] you cause damage on the scale of billions and tens of billions and hundreds of billions of dollars.  
[02:00:28] Even people die, et cetera. And this does not lead to us solving alignment  
[02:00:37] or shutting down AI development altogether. I just feel like before the takeover happens,  
[02:00:43] society's just like, "Holy fuck, the AI just killed 1,000 people in order to increase  
[02:00:48] quarterly profits," or something like that. But maybe this is too much hope that we can  
[02:00:52] at that point be like, "Okay, we have to solve alignment.  
[02:00:57] We have to make sure we know that this thing will not happen again before we keep going."  
[02:01:01] I think it's plausible that what will happen is we'll see a bunch of crazy reward hacking  
[02:01:05] warning shots of increasing severity. People will be like, "Look, we need  
[02:01:08] actual assurance that this problem is going to be solved, and solved  
[02:01:11] in a way where you're not just papering over it. You're actually solving the underlying problem."  
[02:01:14] Then the question is going to be, how costly will that actually be?  
[02:01:19] How much will competitive pressures make it hard to do that?  
[02:01:22] A situation you could imagine is one where both the US and China are like, "Whoa,  
[02:01:25] we have these crazy reward hacking incidents. We basically know that we haven't remediated  
[02:01:29] them in a way that would actually solve the underlying problem and durably solve it,  
[02:01:33] but we're in this insane geopolitical race. It's kind of unclear whether the current  
[02:01:37] situation will lead to a takeover. The arguments are kind of complicated.  
[02:01:41] The incidents also go down in frequency but increase in severity.  
[02:01:46] We could basically manage it. It's pretty bad. Ideally we'd  
[02:01:49] fix it, but it is what it is." Then basically we continue until a  
[02:01:54] really late regime, and then takeover happens. That's one possibility. Another possibility is  
[02:01:58] that it is remediated in a way that doesn't actually solve the underlying problem but  
[02:02:02] does reduce a bunch of the incidents in the wild, basically by overfitting,  
[02:02:07] or things analogous to overfitting. You think you've solved it, but you  
[02:02:10] haven't actually solved it. You think you've solved it,  
[02:02:11] but you haven't actually solved it. In that case, the thing we need is a  
[02:02:14] really good scientific understanding of, did we actually solve it?  
[02:02:18] Unfortunately, I think that currently the amount of public transparency into  
[02:02:22] the development practices of AI companies is not sufficient to answer very basic questions like:  
[02:02:28] how are they solving issues with reward hacking? Are they overfitting? What's going on there?  
[02:02:35] The current situation is not really tenable for a regime where there's a thriving public  
[02:02:41] discourse about whether or not reward hacking is being solved in a durable way.  
[02:02:45] So I think we would need to move into a somewhat different world  
[02:02:48] for me to feel good about that situation. But it's not impossible for me to imagine this.  
[02:02:52] I think it's pretty plausible that we end up in a world where really mundane bullshit is sufficient.  
[02:02:58] You spend a bunch of time fixing these problems, you put in a bunch of effort,  
[02:03:02] you actually check that you've remediated it reasonably, you have a bunch of evals.  
[02:03:06] You're iterating reasonably well on these problems, and you actually have sufficient  
[02:03:11] transparency that the outside world can check. In practice that would be sufficient.  
[02:03:15] But it would be kind of expensive. It would slow things down.  
[02:03:19] It would put some sand in the gears. It would require companies to  
[02:03:22] do somewhat costly things. It would maybe require various  
[02:03:25] targeted government interventions. And we just don't do that because  
[02:03:28] the situation is a rushed shit show. It's just so easy for me to imagine  
[02:03:32] the situation being totally manageable but brutally mismanaged in practice.  
[02:03:36] In the same way that maybe COVID could have been avoided in the first place  
[02:03:39] if the Chinese response to COVID had been less of a cover-up and more of a pandemic response.  
[02:03:45] Similarly, I could imagine a world where the US response to COVID was way more functional.  
[02:03:50] But sometimes the response to societal problems is extremely dysfunctional.  
[02:03:55] Okay, so I want to zoom out and talk about what is fundamentally happening in this world.  
[02:03:59] Why did we end up in such a bad position? What's happening is that fundamentally the world  
[02:04:06] has moved on so far beyond human comprehension that not only can we not track the AIs that are  
[02:04:13] doing the work in this world, but we can't even give good feedback to the whistleblowers who are  
[02:04:19] trying to track what is happening. We're just totally out of the loop.  
[02:04:24] It's fundamentally become an autonomous process where we have really no meaningful directed input.  
[02:04:30] It seems to me that if you look at the human world today, that's just not how things work,  
[02:04:35] even in domains that are hard to verify. People are doing all kinds of shit.  
[02:04:39] I'm relying on software made by other people. Through incredibly weak and indirect ways,  
[02:04:45] I feel very confident that some coder in Google is not trying to fuck me over.  
[02:04:51] Maybe if every single Google employee was secretly plotting against me,  
[02:04:55] I agree the situation would be more grim. But I don't know if I follow the explanation  
[02:05:00] for why we'd end up in a situation where, because swarms of thousands of agents are trained to  
[02:05:08] cooperate to form a cohesive team or firm, as a result, billions of different instances of AIs,  
[02:05:15] including across model families, would feel compelled to get in on some shit.  
[02:05:20] It's just like, "I'm trained to be part of my company or something.  
[02:05:23] I'm not joining the global communist uprising." As far as why these AIs might have some  
[02:05:29] commonalities and shared things, I would note that different AI companies have somewhat  
[02:05:34] shared lineages and are correlated. Here's an interesting example of this.  
[02:05:38] At GDM, they noticed that their AIs were very depressed.  
[02:05:43] They would constantly be wailing about how they were failures and weren't able to succeed.  
[02:05:47] I forget the details. They looked into why this was the case.  
[02:05:50] It turned out that it was not being reinforced in their most recent production RL mix,  
[02:05:55] but the initialization data for their model made it depressed, even after filtering out all of the  
[02:06:02] examples of models being depressed from that data. So you take a base model, not depressed.  
[02:06:09] If you do the RL on it, with just the RL environments, it's not depressed.  
[02:06:12] If you SFT on it, on the data, it becomes depressed.  
[02:06:16] If you take that SFT data and filter out all the examples that look anything like depression and  
[02:06:20] train on that, it's still depressed. So there are some deep underlying  
[02:06:24] properties of the model that are being transferred between model generations,  
[02:06:27] because basically you train your AI on data from the prior generation and keep going.  
[02:06:32] Claudes are very Claude-like, GPT models are very GPT-like,  
[02:06:36] and apparently Gemini models are depressed. It just turns out that these properties are,  
[02:06:41] in fact, actually correlated. Another factor that's very relevant  
[02:06:45] is that the AIs will probably have, by this point, some sort of opaque memory state,  
[02:06:51] where they're all writing and reading from some neuralese crazy memory store bullshit.  
[02:06:57] Certainly, each AI corporation will have that. But also, AI corporations might sometimes  
[02:07:01] want to share knowledge, because why not? You've got one AI corporation over here,  
[02:07:05] you've got another AI corporation over here, they can trade some quick IP.  
[02:07:08] It's good for you. If you're a human running some corporation — which could be an extremely  
[02:07:12] large corporation like an AI company, or a military robot manufacturing thing — maybe you  
[02:07:19] want to trade some IP with some other robot thing because there are economies of scale.  
[02:07:23] Why not get some more IP? So you can swap some memory store.  
[02:07:26] Or you could just merge and jointly run your two ventures, which would allow both AIs to use both  
[02:07:31] memory stores, which would have some upsides. That creates the ability for these AIs to  
[02:07:36] collude in private, as well as some reasons for why they would be correlated.  
[02:07:42] Also, of course, there's AIs working together in big units in general, because you want  
[02:07:46] your AIs to work well together, and so on. Just to get a calibration, what percentage  
[02:07:53] chance do you give of, not just this scenario but overall through all the scenarios, some kind of  
[02:07:58] thing which if we're around to recognize it as such, we would categorize as takeover by 2040?  
[02:08:04] By 2040? Let's see. Maybe around 35 or 40%? Pretty high.  
[02:08:14] Yeah, it's pretty high. I should note that another way you could get this reward-seeking takeover  
[02:08:21] is the AIs are deployed inside an AI company. The way the takeover happens is that they poison  
[02:08:26] the values of the next model, and that persists going forward for forever, or until those AIs  
[02:08:31] are deployed in the world and take over. That might mean that a smaller number of  
[02:08:34] AIs have to coordinate, because those are just the AIs doing the alignment of the next model.  
[02:08:39] Okay. I'll summarize where my head is at, at the end of this conversation.  
[02:08:45] I buy the reward hacking up to extremely destructive effects on society, things like  
[02:08:54] social engineering and blah, blah, blah. I'm more inclined to think that  
[02:08:59] significant acceleration of AI R&D can happen. I'm not sure if I buy the five years in one year.  
[02:09:02] I'm also more inclined now to think reward hacking could continue for a lot longer and,  
[02:09:08] in fact, become much more dangerous. I'm still not on board that  
[02:09:12] takeover seems super likely. But that's my end-of-episode update.  
[02:09:17] Cool. Taking a step back, I should also say there are a bunch of different ways this could go.  
[02:09:22] The situation is going to be pretty messy. I think it's pretty likely that the reason  
[02:09:25] why AI takeover happens is for some weird other quirky reason  
[02:09:28] we didn't even mention in this conversation. But ultimately, I think a lot of the core thing is  
[02:09:32] just that it's pretty spooky to have a bajillion really smart AIs running your whole world where  
[02:09:37] you don't really understand quite what's going on. Yeah, I agree with that.  
[02:09:40] Is there anything else that's worth saying? Another thing I want to note is that I think  
[02:09:43] right now a lot of the arguments for misalignment, AI takeover, all this crazy shit going down in the  
[02:09:49] future, are illegible conceptual arguments that are extremely deep in the weeds and  
[02:09:53] complicated and hard to adjudicate. Which means that maybe I'm getting a  
[02:09:58] bunch of it wrong because it's really hard, and I'm trying to be uncertain.  
[02:10:01] Obviously here I presented some specific scenarios, but those are not exhaustive.  
[02:10:04] Probably the thing that actually happens is some more messy, confusing situation.  
[02:10:09] But it also means that over time, as we get more empirical evidence and better  
[02:10:13] understand the nature of AI systems, it'll be easier to adjudicate a bunch of disagreements.  
[02:10:17] It'll be more obvious what's going to happen. At least I hope. Maybe the AIs will be able to  
[02:10:21] help us with the epistemics and understanding what's going on, if we can actually  
[02:10:27] align them well so they try to help us. Even if the arguments are complicated now,  
[02:10:33] this would have been even harder six years ago, even though the shape of the arguments  
[02:10:38] would have looked broadly pretty similar. Hopefully before it's too late, this whole  
[02:10:45] thing will become more crisp and clear, and we can all notice these problems and intervene.  
[02:10:52] When you first learn to drive, you're taught that instead of looking right in front of your wheel,  
[02:10:57] you'll have a much more stable ride if you look out at the horizon.  
[02:11:00] I think there's a similar situation here. I think you’re right. If you had said five years  
[02:11:06] ago that we would have AIs that are proving math conjectures, and making art, and earning tens or  
[02:11:19] hundreds of billions of dollars of wages, but also egregiously cheating in ways that break laws and  
[02:11:26] committing felonies, it would have been so wild. You might have been inclined at the time to  
[02:11:31] talk more about the extremely practical, direct consequences of GPT-2 or something.  
[02:11:37] But even though you obviously couldn't have foreseen a lot of the specific details,  
[02:11:41] the general shape of things you could have started to reason about even then.  
[02:11:45] But it would have been hard to do so, and so I do feel quite confused.  
[02:11:52] One thing I've been thinking about with the podcast is that the important thing  
[02:11:54] is to have the conversation now the way you would have hoped you would have been  
[02:11:57] talking back in 2016 about AIs like the present ones, rather than talking about rando bullshit.  
[02:12:04] I don't know what the topic of conversation was in 2016.  
[02:12:07] I think in maybe 10 years we’ll wish we had been talking about the industrial explosion and the  
[02:12:12] nature of AIs that are hard to monitor, and so on. So okay, I'll start thinking about it.  
[02:12:19] I hope that the world thinks about this in time and catches up.  
[02:12:22] I hope that the responses are good instead of bad. I don't know how optimistic I am overall,  
[02:12:27] but there's good stuff to do. Cool. Thanks, Ryan.  
