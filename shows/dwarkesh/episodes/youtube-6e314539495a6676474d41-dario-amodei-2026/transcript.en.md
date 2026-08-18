# Dario Amodei — “We are near the end of the exponential”

[00:00:00] We talked three years ago. In your view, what has been the biggest update over the last three years?  
[00:00:05] What has been the biggest difference between what it felt like then versus now?  
[00:00:10] Broadly speaking, the exponential of the underlying technology has gone about as  
[00:00:18] I expected it to go. There's plus or minus  
[00:00:23] a year or two here and there. I don't know that I would've  
[00:00:27] predicted the specific direction of code. But when I look at the exponential,  
[00:00:34] it is roughly what I expected in terms of the march of the models from smart high  
[00:00:39] school student to smart college student to beginning to do PhD and professional stuff,  
[00:00:44] and in the case of code reaching beyond that. The frontier is a little bit uneven, but it's  
[00:00:49] roughly what I expected. What has been the most surprising  
[00:00:55] thing is the lack of public recognition of how close we are to the end of the exponential.  
[00:01:02] To me, it is absolutely wild that you have people — within the bubble and outside the  
[00:01:09] bubble — talking about the same tired, old hot-button political issues, when we are  
[00:01:19] near the end of the exponential. I want to understand what that  
[00:01:24] exponential looks like right now. The first question I asked you when  
[00:01:27] we recorded three years ago was, "what’s up with scaling and why does it work?"  
[00:01:31] I have a similar question now, but it feels more complicated.  
[00:01:35] At least from the public's point of view, three years ago there were well-known public trends  
[00:01:41] across many orders of magnitude of compute where you could see how the loss improves.  
[00:01:45] Now we have RL scaling and there's no publicly known scaling law for it.  
[00:01:49] It's not even clear what the story is. Is this supposed to be teaching the model skills?  
[00:01:54] Is it supposed to be teaching meta-learning? What is the scaling hypothesis at this point?  
[00:01:59] I actually have the same hypothesis I had even all the way back in 2017.  
[00:02:06] I think I talked about it last time, but I wrote a doc called "The Big Blob of Compute Hypothesis".  
[00:02:12] It wasn't about the scaling of language models in particular.  
[00:02:15] When I wrote it GPT-1 had just come out. That was one among many things.  
[00:02:22] Back in those days there was robotics. People tried to work on reasoning as  
[00:02:26] a separate thing from language models, and there was scaling of the kind of RL  
[00:02:30] that happened in AlphaGo and in Dota at OpenAI. People remember StarCraft at DeepMind, AlphaStar.  
[00:02:43] It was written as a more general document. Rich Sutton put out "The Bitter  
[00:02:52] Lesson" a couple years later. The hypothesis is basically the same.  
[00:02:57] What it says is that all the cleverness, all the techniques, all the "we need a new method to do  
[00:03:04] something", that doesn't matter very much. There are only a few things that matter.  
[00:03:08] I think I listed seven of them. One is how much raw compute you have.  
[00:03:13] The second is the quantity of data. The third is the quality and distribution of data.  
[00:03:20] It needs to be a broad distribution. The fourth is how long you train for.  
[00:03:27] The fifth is that you need an objective function that can scale to the moon.  
[00:03:32] The pre-training objective function is one such objective function.  
[00:03:36] Another is the RL objective function that says you have a goal,  
[00:03:42] you're going to go out and reach the goal. Within that, there's objective rewards like  
[00:03:48] you see in math and coding, and there's more subjective rewards like you see in  
[00:03:52] RLHF or higher-order versions of that. Then the sixth and seventh were things  
[00:03:59] around normalization or conditioning, just getting the numerical stability  
[00:04:04] so that the big blob of compute flows in this laminar way instead of running into problems.  
[00:04:11] That was the hypothesis, and it's a hypothesis I still hold.  
[00:04:15] I don't think I've seen very much that is not in line with it.  
[00:04:21] The pre-training scaling laws were one example of what we see there. Those have continued going.  
[00:04:31] Now it's been widely reported, we feel good about pre-training.  
[00:04:35] It’s continuing to give us gains. What has changed is that now we're  
[00:04:41] also seeing the same thing for RL. We're seeing a pre-training phase  
[00:04:46] and then an RL phase on top of that. With RL, it’s actually just the same.  
[00:04:55] Even other companies have published things in some of their releases that say, "We train the  
[00:05:05] model on math contests — AIME or other things — and how well the model does is log-linear in  
[00:05:14] how long we've trained it." We see that as well,  
[00:05:17] and it's not just math contests. It's a wide variety of RL tasks.  
[00:05:21] We're seeing the same scaling in RL that we saw for pre-training.  
[00:05:27] You mentioned Rich Sutton and "The Bitter Lesson". I interviewed him last year,  
[00:05:31] and he's actually very non-LLM-pilled. I don’t know if this is his perspective,  
[00:05:38] but one way to paraphrase his objection is: Something which possesses the true core of human  
[00:05:44] learning would not require all these billions of dollars of data and compute and these bespoke  
[00:05:51] environments, to learn how to use Excel, how to use PowerPoint, how to navigate a web browser.  
[00:05:57] The fact that we have to build in these skills using these RL environments hints that we are  
[00:06:04] actually lacking a core human learning algorithm. So we're scaling the wrong thing. That does raise  
[00:06:13] the question. Why are we doing all this RL scaling if we think there's something that's going to be  
[00:06:16] human-like in its ability to learn on the fly? I think this puts together several things that  
[00:06:23] should be thought of differently. There is a genuine puzzle here,  
[00:06:29] but it may not matter. In fact, I would guess it probably  
[00:06:33] doesn't matter. There is an interesting thing. Let me take the RL out of it for a second, because I  
[00:06:37] actually think it's a red herring to say that RL is any different from pre-training in this matter.  
[00:06:43] If we look at pre-training scaling, it was very interesting  
[00:06:47] back in 2017 when Alec Radford was doing GPT-1. The models before GPT-1 were trained on datasets  
[00:06:59] that didn't represent a wide distribution of text. You had very standard language  
[00:07:08] modeling benchmarks. GPT-1 itself was trained on  
[00:07:11] a bunch of fanfiction, I think actually. It was literary text, which is a very  
[00:07:17] small fraction of the text you can get. In those days it was like a billion words  
[00:07:23] or something, so small datasets representing a pretty narrow distribution of what you can  
[00:07:32] see in the world. It didn't generalize well. If you did better on some fanfiction corpus,  
[00:07:43] it wouldn't generalize that well to other tasks. We had all these measures. We had  
[00:07:47] all these measures of how well it did at predicting all these other kinds of texts.  
[00:07:55] It was only when you trained over all the tasks on the internet — when you did a general internet  
[00:08:01] scrape from something like Common Crawl or scraping links in Reddit, which is what we did for  
[00:08:06] GPT-2 — that you started to get generalization. I think we're seeing the same thing on RL.  
[00:08:15] We're starting first with simple RL tasks like training on math competitions, then moving to  
[00:08:24] broader training that involves things like code. Now we're moving to many other tasks.  
[00:08:31] I think then we're going to increasingly get generalization.  
[00:08:35] So that kind of takes out the RL vs. pre-training side of it.  
[00:08:39] But there is a puzzle either way, which is that in pre-training we use trillions of tokens.  
[00:08:50] Humans don't see trillions of words. So there is an actual sample  
[00:08:54] efficiency difference here. There is actually something different here.  
[00:08:59] The models start from scratch and they need much more training.  
[00:09:06] But we also see that once they're trained, if we give them a long context length of  
[00:09:15] a million — the only thing blocking long context is inference — they're very good at  
[00:09:17] learning and adapting within that context. So I don’t know the full answer to this.  
[00:09:24] I think there's something going on where pre-training is not like  
[00:09:28] the process of humans learning, but it's somewhere between the process of humans  
[00:09:32] learning and the process of human evolution. We get many of our priors from evolution.  
[00:09:38] Our brain isn't just a blank slate. Whole books have been written about this.  
[00:09:43] The language models are much more like blank slates.  
[00:09:45] They literally start as random weights, whereas the human brain starts with all these regions  
[00:09:50] connected to all these inputs and outputs. Maybe we should think of pre-training — and  
[00:09:56] for that matter, RL as well — as something that exists in the middle space between  
[00:10:02] human evolution and human on-the-spot learning. And we should think of the in-context learning  
[00:10:10] that the models do as something between long-term human learning and short-term human learning.  
[00:10:17] So there's this hierarchy. There’s evolution, there's long-term learning, there's short-term  
[00:10:22] learning, and there's just human reaction. The LLM phases exist along this spectrum,  
[00:10:28] but not necessarily at exactly the same points. There’s no analog to some of the human modes  
[00:10:34] of learning the LLMs are falling in between the points. Does that make sense?  
[00:10:40] Yes, although some things are still a bit confusing.  
[00:10:42] For example, if the analogy is that this is like evolution so it's fine that it's  
[00:10:45] not sample efficient, then if we're going to get super sample-efficient  
[00:10:51] agent from in-context learning, why are we bothering to build all these RL environments?  
[00:10:56] There are companies whose work seems to be teaching models how to use this API,  
[00:11:00] how to use Slack, how to use whatever. It's confusing to me why there's so much emphasis  
[00:11:04] on that if the kind of agent that can just learn on the fly is emerging or has already emerged.  
[00:11:11] I can't speak for the emphasis of anyone else. I can only talk about how we think about it.  
[00:11:20] The goal is not to teach the model every possible skill within RL,  
[00:11:25] just as we don't do that within pre-training. Within pre-training, we're not trying to expose  
[00:11:29] the model to every possible way that words could be put together.  
[00:11:37] Rather, the model trains on a lot of things and then reaches generalization across pre-training.  
[00:11:43] That was the transition from GPT-1 to GPT-2 that I saw up close. The model reaches a point. I had  
[00:11:53] these moments where I was like, "Oh yeah, you just give the model a list of numbers — this is  
[00:12:01] the cost of the house, this is the square feet of the house — and the model completes the pattern  
[00:12:05] and does linear regression." Not great, but it does it,  
[00:12:08] and it's never seen that exact thing before. So to the extent that we are building these  
[00:12:16] RL environments, the goal is very similar to what was done five or ten years ago with pre-training.  
[00:12:26] We're trying to get a whole bunch of data, not because we want to cover a specific document or a  
[00:12:32] specific skill, but because we want to generalize. I think the framework you're laying down obviously  
[00:12:39] makes sense. We're making progress toward AGI. Nobody at this point disagrees we're going to  
[00:12:46] achieve AGI this century. The crux is you say we're  
[00:12:49] hitting the end of the exponential. Somebody else looks at this and says,  
[00:12:55] "We've been making progress since 2012, and by 2035 we'll have a human-like agent."  
[00:13:04] Obviously we’re seeing in these models the kinds of things that evolution did,  
[00:13:07] or that learning within a human lifetime does. I want to understand what you’re seeing  
[00:13:11] that makes you think it's one year away and not ten years away.  
[00:13:17] There are two claims you could make here, one stronger and one weaker.  
[00:13:26] Starting with the weaker claim, when I first saw the scaling back in 2019,  
[00:13:35] I wasn’t sure. This was a 50/50 thing. I thought I saw something. My claim was that this  
[00:13:43] was much more likely than anyone thinks. Maybe there's a 50% chance this happens.  
[00:13:51] On the basic hypothesis of, as you put it, within ten years we'll get to what I call a "country of  
[00:14:00] geniuses in a data center", I'm at 90% on that. It's hard to go much higher than 90%  
[00:14:06] because the world is so unpredictable. Maybe the irreducible uncertainty puts us at 95%,  
[00:14:13] where you get to things like multiple companies having internal turmoil, Taiwan gets invaded,  
[00:14:24] all the fabs get blown up by missiles. Now you've jinxed us, Dario.  
[00:14:30] You could construct a 5% world where things get delayed for ten years.  
[00:14:43] There's another 5% which is that I'm very confident on tasks that can be verified.  
[00:14:50] With coding, except for that irreducible uncertainty,  
[00:14:54] I think we'll be there in one or two years. There's no way we will not be there in ten years  
[00:14:58] in terms of being able to do end-to-end coding. My one little bit of fundamental uncertainty,  
[00:15:05] even on long timescales, is about tasks that aren't verifiable: planning a mission to Mars;  
[00:15:14] doing some fundamental scientific discovery like CRISPR; writing a novel.  
[00:15:21] It’s hard to verify those tasks. I am almost certain we have a  
[00:15:27] reliable path to get there, but if there's a little bit of uncertainty it's there.  
[00:15:34] On the ten-year timeline I'm at 90%, which is about as certain as you can be.  
[00:15:40] I think it's crazy to say that this won't happen by 2035.  
[00:15:46] In some sane world, it would be outside the mainstream.  
[00:15:48] But the emphasis on verification hints to me a lack of belief that these models are generalized.  
[00:15:58] If you think about humans, we're both good at things for which we get verifiable reward  
[00:16:03] and things for which we don't. No, this is why I’m almost sure.  
[00:16:07] We already see substantial generalization from things that verify to things that  
[00:16:12] don't. We're already seeing that. But it seems like you were emphasizing  
[00:16:15] this as a spectrum which will split apart which domains in which we see more progress.  
[00:16:21] That doesn't seem like how humans get better. The world in which we don't get there is the world  
[00:16:27] in which we do all the verifiable things. Many of them generalize,  
[00:16:34] but we don't fully get there. We don’t fully color in the other side  
[00:16:40] of the box. It's not a binary thing. Even if generalization is weak and you can only do  
[00:16:47] verifiable domains, it's not clear to me you could automate software engineering in such a world.  
[00:16:49] You are "a software engineer" in some sense, but part of being a software engineer for you involves  
[00:16:58] writing long memos about your grand vision. I don’t think that’s part of the job of SWE.  
[00:17:03] That's part of the job of the company, not SWE specifically.  
[00:17:04] But SWE does involve design documents and other things like that.  
[00:17:10] The models are already pretty good at writing comments.  
[00:17:14] Again, I’m making much weaker claims here than I believe, to distinguish between two things.  
[00:17:24] We're already almost there for software engineering.  
[00:17:28] By what metric? There's one metric which is how many lines of code are written by AI.  
[00:17:32] If you consider other productivity improvements in the history of software engineering,  
[00:17:36] compilers write all the lines of software. There's a difference between how many lines  
[00:17:40] are written and how big the productivity improvement is. "We’re almost there" meaning…  
[00:17:47] How big is the productivity improvement, not just how many lines are written by AI?  
[00:17:52] I actually agree with you on this. I've made a series of predictions on  
[00:17:57] code and software engineering. I think people have repeatedly misunderstood them.  
[00:18:03] Let me lay out the spectrum. About eight or nine months ago,  
[00:18:09] I said the AI model will be writing 90% of the lines of code in three to six months.  
[00:18:16] That happened, at least at some places. It happened at Anthropic, happened with  
[00:18:21] many people downstream using our models. But that's actually a very weak criterion.  
[00:18:27] People thought I was saying that we won't need 90% of the software engineers. Those things are worlds  
[00:18:32] apart. The spectrum is: 90% of code is written by the model, 100% of code is written by the model.  
[00:18:41] That's a big difference in productivity. 90% of the end-to-end SWE tasks — including  
[00:18:47] things like compiling, setting up clusters and environments, testing features,  
[00:18:54] writing memos — are done by the models. 100% of today's SWE tasks are done by the models.  
[00:19:02] Even when that happens, it doesn't mean software engineers are out of a job.  
[00:19:06] There are new higher-level things they can do, where they can manage.  
[00:19:10] Then further down the spectrum, there's 90% less demand for SWEs, which I think  
[00:19:15] will happen but this is a spectrum. I wrote about it in "The Adolescence  
[00:19:21] of Technology" where I went through this kind of spectrum with farming.  
[00:19:26] I actually totally agree with you on that.  
[00:19:29] These are very different benchmarks from each other,  
[00:19:32] but we're proceeding through them super fast. Part of your vision is that going from 90 to 100  
[00:19:38] is going to happen fast, and that it leads to huge productivity improvements.  
[00:19:45] But what I notice is that even in greenfield projects people start with Claude Code or  
[00:19:49] something, people report starting a lot of projects… Do we see in the world out there  
[00:19:54] a renaissance of software, all these new features that wouldn't exist otherwise?  
[00:19:58] At least so far, it doesn't seem like we see that. So that does make me wonder.  
[00:20:02] Even if I never had to intervene with Claude Code, the world is complicated.  
[00:20:09] Jobs are complicated. Closing the loop on self-contained systems, whether it’s just  
[00:20:14] writing software or something, how much broader gains would we see just from that?  
[00:20:20] Maybe that should dilute our estimation of the "country of geniuses".  
[00:20:24] I simultaneously agree with you that it's a reason why these things don't happen instantly,  
[00:20:35] but at the same time, I think the effect is gonna be very fast.  
[00:20:41] You could have these two poles. One is that AI is not going to make  
[00:20:47] progress. It's slow. It's going to take forever to diffuse within the economy.  
[00:20:52] Economic diffusion has become one of these buzzwords that's a reason why  
[00:20:56] we're not going to make AI progress, or why AI progress doesn't matter.  
[00:21:00] The other axis is that we'll get recursive self-improvement, the whole thing.  
[00:21:05] Can't you just draw an exponential line on the curve?  
[00:21:08] We're going to have Dyson spheres around the sun so many nanoseconds after we get recursive.  
[00:21:17] I'm completely caricaturing the view here, but there are these two extremes.  
[00:21:23] But what we've seen from the beginning, at least if you look within Anthropic, there's this bizarre  
[00:21:30] 10x per year growth in revenue that we've seen. So in 2023, it was zero to $100 million.  
[00:21:38] In 2024, it was $100 million to $1 billion. In 2025, it was $1 billion to $ 9-10 billion.  
[00:21:46] You guys should have just bought a billion dollars of your own products so you could just…  
[00:21:50] And the first month of this year, that exponential is...  
[00:21:54] You would think it would slow down, but we added another few billion to revenue in January.  
[00:22:05] Obviously that curve can't go on forever. The GDP is only so large.  
[00:22:10] I would even guess that it bends somewhat this year, but that is a fast curve. That's a really  
[00:22:20] fast curve. I would bet it stays pretty fast even as the scale goes to the entire economy.  
[00:22:25] So I think we should be thinking about this middle world where things are extremely fast, but not  
[00:22:34] instant, where they take time because of economic diffusion, because of the need to close the loop.  
[00:22:39] Because it's fiddly: "I have to do change management within my enterprise… I set this up,  
[00:22:50] but I have to change the security permissions on this in order to make it actually work…  
[00:22:55] I had this old piece of software that checks the model before it's compiled  
[00:23:01] and released and I have to rewrite it. Yes, the model can do that, but I have  
[00:23:05] to tell the model to do that. It has to take time to do that."  
[00:23:10] So I think everything we've seen so far is compatible with the idea that there's one fast  
[00:23:17] exponential that's the capability of the model. Then there's another fast exponential  
[00:23:22] that's downstream of that, which is the diffusion of the model into the economy.  
[00:23:26] Not instant, not slow, much faster than any previous technology, but it has its limits.  
[00:23:37] When I look inside Anthropic, when I look at our customers: fast adoption, but not infinitely fast.  
[00:23:44] Can I try a hot take on you? Yeah.  
[00:23:45] I feel like diffusion is cope that people say. When the model isn't able to do something,  
[00:23:51] they're like, "oh, but it's a diffusion issue." But then you should use the comparison to humans.  
[00:23:56] You would think that the inherent advantages that AIs have would make diffusion a much easier  
[00:24:01] problem for new AIs getting onboarded than new humans getting onboarded.  
[00:24:06] An AI can read your entire Slack and your drive in minutes.  
[00:24:08] They can share all the knowledge that the other copies of the same instance have.  
[00:24:12] You don't have this adverse selection problem when you're hiring AI, so you  
[00:24:14] can just hire copies of a vetted AI model. Hiring a human is so much more of a hassle.  
[00:24:20] People hire humans all the time. We pay humans upwards of $50 trillion  
[00:24:23] in wages because they're useful, even though in principle it would be much easier to integrate  
[00:24:29] AIs into the economy than it is to hire humans. The diffusion doesn't really explain.  
[00:24:34] I think diffusion is very real and doesn't exclusively have  
[00:24:41] to do with limitations on the AI models. Again, there are people who use diffusion  
[00:24:49] as kind of a buzzword to say this isn't a big deal. I'm not talking about that. I'm  
[00:24:54] not talking about how AI will diffuse at the speed of previous technologies.  
[00:24:58] I think AI will diffuse much faster than previous technologies have, but not infinitely fast.  
[00:25:04] I'll just give an example of this. There's Claude Code. Claude Code is extremely easy to set up.  
[00:25:10] If you're a developer, you can just start using Claude Code.  
[00:25:14] There is no reason why a developer at a large enterprise should not be adopting  
[00:25:19] Claude Code as quickly as an individual developer or developer at a startup.  
[00:25:25] We do everything we can to promote it. We sell Claude Code to enterprises.  
[00:25:31] Big enterprises, big financial companies, big pharmaceutical companies, all of them are adopting  
[00:25:38] Claude Code much faster than enterprises typically adopt new technology. But again,  
[00:25:46] it takes time. Any given feature or any given product, like Claude Code or Cowork, will get  
[00:25:54] adopted by the individual developers who are on Twitter all the time, by the Series A startups,  
[00:26:02] many months faster than they will get adopted by a large enterprise that does food sales.  
[00:26:11] There are just a number of factors. You have to go through legal,  
[00:26:14] you have to provision it for everyone. It has to pass security and compliance.  
[00:26:20] The leaders of the company who are further away from the AI revolution are forward-looking,  
[00:26:26] but they have to say, "Oh, it makes sense for us to spend 50 million.  
[00:26:31] This is what this Claude Code thing is. This is why it helps our company.  
[00:26:35] This is why it makes us more productive." Then they have to explain  
[00:26:37] to the people two levels below. They have to say, "Okay, we have 3,000 developers.  
[00:26:42] Here's how we're going to roll it out to our developers."  
[00:26:45] We have conversations like this every day. We are doing everything we can to make  
[00:26:50] Anthropic's revenue grow 20 or 30x a year instead of 10x a year.  
[00:26:57] Again, many enterprises are just saying, "This is so productive.  
[00:27:02] We're going to take shortcuts in our usual procurement process."  
[00:27:05] They're moving much faster than when we tried to sell them just  
[00:27:08] the ordinary API, which many of them use. Claude Code is a more compelling product,  
[00:27:13] but it's not an infinitely compelling product. I don't think even AGI or powerful AI or  
[00:27:19] "country of geniuses in a data center" will be an infinitely compelling product.  
[00:27:22] It will be a compelling product enough maybe to get 3-5x, or 10x, a year of growth, even when  
[00:27:28] you're in the hundreds of billions of dollars, which is extremely hard to do and has never been  
[00:27:32] done in history before, but not infinitely fast. I buy that it would be a slight slowdown.  
[00:27:36] Maybe this is not your claim, but sometimes people talk about this like,  
[00:27:39] "Oh, the capabilities are there, but because of diffusion... otherwise we're basically at AGI".  
[00:27:46] I don't believe we're basically at AGI. I think if you had the "country  
[00:27:49] of geniuses in a data center"... If we had the "country of geniuses  
[00:27:53] in a data center", we would know it. We would know it if you had the  
[00:27:57] "country of geniuses in a data center". Everyone in this room would know it.  
[00:28:01] Everyone in Washington would know it. People in rural parts might not know it,  
[00:28:07] but we would know it. We don't have that now. That is very clear.  
[00:29:42] Coming back to concrete prediction… Because there are so many different things to disambiguate,  
[00:29:47] it can be easy to talk past each other when we're talking about capabilities.  
[00:29:50] For example, when I interviewed you three years ago, I asked you a prediction about what  
[00:29:54] we should expect three years from now. You were right. You said, "We should expect systems which,  
[00:30:00] if you talk to them for the course of an hour, it's hard to tell them apart from  
[00:30:04] a generally well-educated human." I think you were right about that.  
[00:30:07] I think spiritually I feel unsatisfied because my internal expectation was that such a system could  
[00:30:13] automate large parts of white-collar work. So it might be more productive to talk about  
[00:30:17] the actual end capabilities you want from such a system.  
[00:30:21] I will basically tell you where I think we are. Let me ask a very specific question so that  
[00:30:28] we can figure out exactly what kinds of capabilities we should think about soon.  
[00:30:32] Maybe I'll ask about it in the context of a job I understand well, not because it's the most  
[00:30:36] relevant job, but just because I can evaluate the claims about it. Take video editors. I have  
[00:30:42] video editors. Part of their job involves learning about our audience's preferences,  
[00:30:47] learning about my preferences and tastes, and the different trade-offs we have.  
[00:30:50] They’re, over the course of many months, building up this understanding of context.  
[00:30:55] The skill and ability they have six months into the job, a model that can  
[00:30:58] pick up that skill on the job on the fly, when should we expect such an AI system?  
[00:31:04] I guess what you're talking about is that we're doing this interview for three hours.  
[00:31:09] Someone's going to come in, someone's going to edit it.  
[00:31:11] They're going to be like, "Oh, I don't know, Dario scratched his head and we could edit that out."  
[00:31:19] "Magnify that." "There was this long  
[00:31:22] discussion that is less interesting to people. There's another thing that's more interesting  
[00:31:27] to people, so let's make this edit." I think the "country of geniuses in  
[00:31:33] a data center" will be able to do that. The way it will be able to do that is it will  
[00:31:38] have general control of a computer screen. You'll be able to feed this in.  
[00:31:43] It'll be able to also use the computer screen to go on the web, look at all your previous  
[00:31:49] interviews, look at what people are saying on Twitter in response to your interviews,  
[00:31:54] talk to you, ask you questions, talk to your staff, look at the history of edits  
[00:31:59] that you did, and from that, do the job. I think that's dependent on several things.  
[00:32:06] I think this is one of the things that's actually blocking deployment:  
[00:32:10] getting to the point on computer use where the models are really masters at using the computer.  
[00:32:16] We've seen this climb in benchmarks, and benchmarks are always imperfect measures.  
[00:32:20] But I think when we first released computer use a year and a quarter ago, OSWorld was at maybe 15%.  
[00:32:33] I don't remember exactly, but we've climbed from that to 65-70%.  
[00:32:40] There may be harder measures as well, but I think computer use has to pass a point of reliability.  
[00:32:46] Can I just follow up on that before you move on to the next point?  
[00:32:50] For years, I've been trying to build different internal LLM tools for myself.  
[00:32:54] Often I have these text-in, text-out tasks, which should be dead center  
[00:32:59] in the repertoire of these models. Yet I still hire humans to do them.  
[00:33:03] If it's something like, "identify what the best clips would be in this transcript",  
[00:33:07] maybe the LLMs do a seven-out-of-ten job on them. But there's not this ongoing way I can engage  
[00:33:12] with them to help them get better at the job the way I could with a human employee.  
[00:33:16] That missing ability, even if you solve computer use, would still block  
[00:33:20] my ability to offload an actual job to them. This gets back to what we were talking about  
[00:33:28] before with learning on the job. It's very interesting. I think with the coding agents,  
[00:33:34] I don't think people would say that learning on the job is what is preventing the coding agents  
[00:33:39] from doing everything end to end. They keep getting better. We have engineers  
[00:33:46] at Anthropic who don't write any code. When I look at the productivity, to your  
[00:33:51] previous question, we have folks who say, "This GPU kernel, this chip, I used to write it myself.  
[00:33:58] I just have Claude do it." There's this enormous improvement in productivity.  
[00:34:04] When I see Claude Code, familiarity with the codebase or a feeling that the model  
[00:34:13] hasn't worked at the company for a year, that's not high up on the list of complaints I see.  
[00:34:18] I think what I'm saying is that we're kind of taking a different path.  
[00:34:22] Don't you think with coding that's because there  
[00:34:24] is an external scaffold of memory which exists instantiated in the codebase?  
[00:34:28] I don't know how many other jobs have that. Coding made fast progress precisely because  
[00:34:33] it has this unique advantage that other economic activity doesn't.  
[00:34:37] But when you say that, what you're implying is that by reading the codebase into the context,  
[00:34:44] I have everything that the human needed to learn on the job.  
[00:34:48] So that would be an example of—whether it's written or not, whether it's available or  
[00:34:54] not—a case where everything you needed to know you got from the context window.  
[00:35:00] What we think of as learning—"I started this job, it's going to take me six months to understand the  
[00:35:05] code base"—the model just did it in the context. I honestly don't know how to think about  
[00:35:09] this because there are people who qualitatively report what you're saying.  
[00:35:16] I'm sure you saw last year, there was a major study where they had experienced developers try  
[00:35:21] to close pull requests in repositories that they were familiar with. Those developers reported an  
[00:35:28] uplift. They reported that they felt more productive with the use of these models.  
[00:35:31] But in fact, if you look at their output and how much was actually merged back in,  
[00:35:35] there was a 20% downlift. They were less productive  
[00:35:37] as a result of using these models. So I'm trying to square the qualitative  
[00:35:40] feeling that people feel with these models versus, 1) in a macro level,  
[00:35:44] where is this renaissance of software? And then 2) when people do these independent  
[00:35:48] evaluations, why are we not seeing the productivity benefits we would expect?  
[00:35:53] Within Anthropic, this is just really unambiguous. We're under an incredible amount of commercial  
[00:35:59] pressure and make it even harder for ourselves because we have all this safety stuff we do that  
[00:36:03] I think we do more than other companies. The pressure to survive economically  
[00:36:11] while also keeping our values is just incredible. We're trying to keep this 10x revenue curve going.  
[00:36:18] There is zero time for bullshit. There is zero time for feeling  
[00:36:23] like we're productive when we're not. These tools make us a lot more productive.  
[00:36:30] Why do you think we're concerned about competitors using the tools?  
[00:36:34] Because we think we're ahead of the competitors. We wouldn't be going through all this trouble if  
[00:36:43] this were secretly reducing our productivity. We see the end productivity every few  
[00:36:49] months in the form of model launches. There's no kidding yourself about this.  
[00:36:54] The models make you more productive. 1) People feeling like they're productive is  
[00:37:00] qualitatively predicted by studies like this. But 2) if I just look at the end output,  
[00:37:04] obviously you guys are making fast progress. But the idea was supposed to be that with  
[00:37:10] recursive self-improvement, you make a better AI, the AI helps you build a  
[00:37:14] better next AI, et cetera, et cetera. What I see instead—if I look at you,  
[00:37:18] OpenAI, DeepMind—is that people are just shifting around the podium every few months.  
[00:37:22] Maybe you think that stops because you've won or whatever.  
[00:37:25] But why are we not seeing the person with the best coding model have this lasting  
[00:37:31] advantage if in fact there are these enormous productivity gains from the last coding model.  
[00:37:38] I think my model of the situation is that there's an advantage that's gradually growing.  
[00:37:45] I would say right now the coding models give maybe, I don't know,  
[00:37:51] a 15-20% total factor speed up. That's my view. Six months ago, it was maybe 5%.  
[00:38:01] So it didn't matter. 5% doesn't register. It's now just getting to the point where it's  
[00:38:06] one of several factors that kind of matters. That's going to keep speeding up.  
[00:38:12] I think six months ago, there were several companies that were at roughly the same  
[00:38:18] point because this wasn't a notable factor, but I think it's starting to speed up more and more.  
[00:38:25] I would also say there are multiple companies that write models that are used for code and we're not  
[00:38:32] perfectly good at preventing some of these other companies from using our models internally.  
[00:38:41] So I think everything we're seeing is consistent with this kind of snowball model.  
[00:38:52] Again, my theme in all of this is all of this is soft takeoff, soft, smooth exponentials,  
[00:39:00] although the exponentials are relatively steep. So we're seeing this snowball gather momentum  
[00:39:05] where it's like 10%, 20%, 25%, 40%. As you go, Amdahl's law, you have  
[00:39:13] to get all the things that are preventing you from closing the loop out of the way.  
[00:39:17] But this is one of the biggest priorities within Anthropic.  
[00:39:22] Stepping back, before in the stack we were talking about when do we get this on-the-job learning?  
[00:39:29] It seems like the point you were making on the coding thing is that we actually  
[00:39:32] don't need on-the-job learning. You can have tremendous productivity  
[00:39:36] improvements, you can have potentially trillions of dollars of revenue for AI companies, without  
[00:39:40] this basic human ability to learn on the job. Maybe that's not your claim, you should clarify.  
[00:39:47] But in most domains of economic activity, people say, "I hired somebody, they weren't that useful  
[00:39:53] for the first few months, and then over time they built up the context, understanding."  
[00:39:58] It's actually hard to define what we're talking about here.  
[00:40:00] But they got something and then now they're a powerhorse and they're so valuable to us.  
[00:40:05] If AI doesn't develop this ability to learn on the fly, I'm a bit skeptical that we're going to see  
[00:40:12] huge changes to the world without that ability. I think two things here. There's the state  
[00:40:17] of the technology right now. Again, we have these two stages.  
[00:40:22] We have the pre-training and RL stage where you throw a bunch of data and tasks into  
[00:40:27] the models and then they generalize. So it's like learning, but it's like  
[00:40:31] learning from more data and not learning over one human or one model's lifetime.  
[00:40:38] So again, this is situated between evolution and human learning.  
[00:40:42] But once you learn all those skills, you have them.  
[00:40:45] Just like with pre-training, just how the models know more, if I look at a pre-trained model,  
[00:40:52] it knows more about the history of samurai in Japan than I do.  
[00:40:55] It knows more about baseball than I do. It knows more about low-pass filters  
[00:41:03] and electronics, all of these things. Its knowledge is way broader than mine.  
[00:41:08] So I think even just that may get us to the point where the models are better at everything.  
[00:41:18] We also have, again, just with scaling the kind of existing setup, the in-context learning.  
[00:41:24] I would describe it as kind of like human on-the-job learning,  
[00:41:27] but a little weaker and a little short term. You look at in-context learning and if you give  
[00:41:33] the model a bunch of examples it does get it. There's real learning that happens in context.  
[00:41:38] A million tokens is a lot. That can be days of human learning.  
[00:41:42] If you think about the model reading a million words, how long would it  
[00:41:50] take me to read a million? Days or weeks at least. So you have these two things.  
[00:41:57] I think these two things within the existing paradigm may just be enough to get you the  
[00:42:01] "country of geniuses in a data center". I don't know for sure, but I think  
[00:42:04] they're going to get you a large fraction of it. There may be gaps, but I certainly think that just  
[00:42:10] as things are, this is enough to generate trillions of dollars of revenue. That's one. Two,  
[00:42:17] is this idea of continual learning, this idea of a single model learning on the job.  
[00:42:24] I think we're working on that too. There's a good chance that in the next  
[00:42:29] year or two, we also solve that. Again, I think you get most  
[00:42:36] of the way there without it. The trillions of dollars a year market,  
[00:42:45] maybe all of the national security implications and the safety implications that I wrote about in  
[00:42:49] "Adolescence of Technology" can happen without it. But we, and I imagine others, are working on it.  
[00:42:57] There's a good chance that we will get there within the next year or two.  
[00:43:03] There are a bunch of ideas. I won't go into all of them in detail, but  
[00:43:07] one is just to make the context longer. There's nothing preventing  
[00:43:10] longer contexts from working. You just have to train at longer contexts  
[00:43:14] and then learn to serve them at inference. Both of those are engineering problems that  
[00:43:18] we are working on and I would assume others are working on them as well.  
[00:43:22] This context length increase, it seemed like there was a period from 2020 to 2023  
[00:43:26] where from GPT-3 to GPT-4 Turbo, there was an increase from 2000 context lengths to 128K.  
[00:43:31] I feel like for the two-ish years since then, we've been in the same-ish ballpark.  
[00:43:37] When context lengths get much longer than that, people report qualitative  
[00:43:41] degradation in the ability of the model to consider that full context.  
[00:43:47] So I'm curious what you're internally seeing that makes you think, "10 million contexts,  
[00:43:50] 100 million contexts to get six months of human learning and building context".  
[00:43:54] This isn't a research problem. This is an engineering and inference problem.  
[00:43:58] If you want to serve long context, you have to store your entire KV cache.  
[00:44:06] It's difficult to store all the memory in the GPUs, to juggle the memory around.  
[00:44:11] I don't even know the details. At this point, this is at a level of detail  
[00:44:15] that I'm no longer able to follow, although I knew it in the GPT-3 era. "These are the weights,  
[00:44:21] these are the activations you have to store…" But these days the whole thing is flipped  
[00:44:26] because we have MoE models and all of that. Regarding this degradation you're talking about,  
[00:44:34] without getting too specific, there's two things. There's the context length you train at and  
[00:44:41] there's a context length that you serve at. If you train at a small context length  
[00:44:45] and then try to serve at a long context length, maybe you get these degradations.  
[00:44:49] It's better than nothing, you might still offer it, but you get these degradations.  
[00:44:52] Maybe it's harder to train at a long context length.  
[00:44:56] I want to, at the same time, ask about maybe some rabbit holes.  
[00:45:01] Wouldn't you expect that if you had to train on longer context length,  
[00:45:04] that would mean that you're able to get less samples in for the same amount of compute?  
[00:45:10] Maybe it's not worth diving deep on that. I want to get an answer to the  
[00:45:14] bigger picture question. I don't feel a preference  
[00:45:20] for a human editor that's been working for me for six months versus an AI that's been  
[00:45:25] working with me for six months, what year do you predict that that will be the case?  
[00:45:33] My guess for that is there's a lot of problems where basically we can do this when we have  
[00:45:38] the "country of geniuses in a data center". My picture for that, if you made me guess, is  
[00:45:48] one to two years, maybe one to three years. It's really hard to tell. I have a strong view—99%,  
[00:45:54] 95%—that all this will happen in 10 years. I think that's just a super safe bet.  
[00:46:00] I have a hunch—this is more like a 50/50 thing—that it's going to be more like  
[00:46:04] one to two, maybe more like one to three. So one to three years. Country of geniuses,  
[00:46:10] and the slightly less economically valuable task of editing videos.  
[00:46:14] It seems pretty economically valuable, let me tell you.  
[00:46:17] It's just there are a lot of use cases like that. There are a lot of similar ones.  
[00:46:20] So you're predicting that within one to three years.  
[00:46:23] And then, generally, Anthropic has predicted that by late '26 or early '27 we will have AI systems  
[00:46:28] that "have the ability to navigate interfaces available to humans doing digital work today,  
[00:46:34] intellectual capabilities matching or exceeding that of Nobel Prize winners, and the ability to  
[00:46:38] interface with the physical world". You gave an interview two months ago  
[00:46:42] with DealBook where you were emphasizing your company's more responsible compute  
[00:46:48] scaling as compared to your competitors. I'm trying to square these two views.  
[00:46:52] If you really believe that we're going to have a country of geniuses, you want as  
[00:46:57] big a data center as you can get. There's no reason to slow down.  
[00:47:00] The TAM of a Nobel Prize winner, that can actually do everything a Nobel Prize  
[00:47:04] winner can do, is trillions of dollars. So I'm trying to square this conservatism,  
[00:47:10] which seems rational if you have more moderate timelines, with your stated views about progress.  
[00:47:16] It actually all fits together. We go back to this fast, but not infinitely fast, diffusion.  
[00:47:23] Let's say that we're making progress at this rate. The technology is making progress this fast.  
[00:47:29] I have very high conviction that we're going to get there within a few years.  
[00:47:39] I have a hunch that we're going to get there within a year or two.  
[00:47:41] So there’s a little uncertainty on the technical side, but pretty strong  
[00:47:46] confidence that it won't be off by much. What I'm less certain about is, again,  
[00:47:51] the economic diffusion side. I really do believe that we could  
[00:47:56] have models that are a country of geniuses in the data center in one to two years.  
[00:48:03] One question is: How many years after that do the trillions in revenue start rolling in?  
[00:48:14] I don't think it's guaranteed that it's going to be immediate.  
[00:48:19] It could be one year, it could be two years, I could even stretch it to five  
[00:48:27] years although I'm skeptical of that. So we have this uncertainty. Even if the technology goes as  
[00:48:35] fast as I suspect that it will, we don't know exactly how fast it's going to drive revenue.  
[00:48:41] We know it's coming, but with the way you buy these data centers, if you're off by a couple  
[00:48:47] years, that can be ruinous. It is just like how I  
[00:48:50] wrote in "Machines of Loving Grace". I said I think we might get this powerful AI,  
[00:48:55] this "country of genius in the data center". That description you gave comes  
[00:48:57] from "Machines of Loving Grace". I said we'll get that in 2026, maybe 2027. Again,  
[00:49:02] that is my hunch. I wouldn't be surprised if I'm off by a year or two, but that is my hunch.  
[00:49:08] Let's say that happens. That's the starting gun. How long does it take to cure all the diseases?  
[00:49:13] That's one of the ways that drives a huge amount of economic value. You cure every disease. There's  
[00:49:21] a question of how much of that goes to the pharmaceutical company or the AI company,  
[00:49:24] but there's an enormous consumer surplus because —assuming we can get access for everyone,  
[00:49:29] which I care about greatly—we cure all of these diseases. How long does it take? You  
[00:49:34] have to do the biological discovery, you have to manufacture the new drug,  
[00:49:40] you have to go through the regulatory process. We saw this with vaccines and COVID.  
[00:49:47] We got the vaccine out to everyone, but it took a year and a half.  
[00:49:52] My question is: How long does it take to get the cure for everything—which AI is the genius  
[00:49:58] that can in theory invent—out to everyone? How long from when that AI first exists  
[00:50:03] in the lab to when diseases have actually been cured for everyone?  
[00:50:09] We've had a polio vaccine for 50 years. We're still trying to eradicate it in the  
[00:50:14] most remote corners of Africa. The Gates Foundation is trying  
[00:50:18] as hard as they can. Others are trying as hard  
[00:50:20] as they can. But that's difficult. Again, I don't expect most of the economic diffusion  
[00:50:25] to be as difficult as that. That's the most difficult case. But there's a real dilemma here.  
[00:50:32] Where I've settled on it is that it will be faster than anything we've seen in the  
[00:50:39] world, but it still has its limits. So when we go to buying data centers,  
[00:50:47] again, the curve I'm looking at is: we've had a 10x a year increase every year.  
[00:50:54] At the beginning of this year, we're looking at $10 billion in annualized revenue.  
[00:51:02] We have to decide how much compute to buy. It takes a year or two to actually build out  
[00:51:10] the data centers, to reserve the data center. Basically I'm saying, "In 2027,  
[00:51:16] how much compute do I get?" I could assume that the  
[00:51:24] revenue will continue growing 10x a year, so it'll be $100 billion at the end of  
[00:51:31] 2026 and $1 trillion at the end of 2027. Actually it would be $5 trillion dollars  
[00:51:39] of compute because it would be $1 trillion a year for five years.  
[00:51:43] I could buy $1 trillion of compute that starts at the end of 2027.  
[00:51:49] If my revenue is not $1 trillion dollars, if it's even $800 billion, there's no force on earth,  
[00:51:56] there's no hedge on earth that could stop me from going bankrupt if I buy that much compute.  
[00:52:03] Even though a part of my brain wonders if it's going to keep growing 10x,  
[00:52:07] I can't buy $1 trillion a year of compute in 2027. If I'm just off by a year in that rate of growth,  
[00:52:17] or if the growth rate is 5x a year instead of 10x a year, then you go bankrupt.  
[00:52:25] So you end up in a world where you're supporting hundreds of billions, not trillions.  
[00:52:33] You accept some risk that there's so much demand that you can't support the revenue,  
[00:52:38] and you accept some risk that you got it wrong and it's still slow.  
[00:52:43] When I talked about behaving responsibly, what I meant actually was not the absolute amount.  
[00:52:51] I think it is true we're spending somewhat less than some of the other players.  
[00:52:55] It's actually the other things, like have we been thoughtful about it or are we YOLOing and saying,  
[00:53:01] "We're going to do $100 billion here or $100 billion there"?  
[00:53:05] I get the impression that some of the other companies have not written down  
[00:53:09] the spreadsheet, that they don't really understand the risks they're taking.  
[00:53:12] They're just doing stuff because it sounds cool. We've thought carefully about it. We're  
[00:53:19] an enterprise business. Therefore, we can rely more on revenue. It's less fickle than consumer.  
[00:53:26] We have better margins, which is the buffer between buying too much and buying too little.  
[00:53:31] I think we bought an amount that allows us to capture pretty strong upside worlds.  
[00:53:37] It won't capture the full 10x a year. Things would have to go pretty badly for  
[00:53:42] us to be in financial trouble. So we've thought carefully and  
[00:53:46] we've made that balance. That's what I mean when  
[00:53:48] I say that we're being responsible. So it seems like it's possible that we  
[00:53:54] actually just have different definitions of the "country of a genius in a data center".  
[00:53:56] Because when I think of actual human geniuses, an actual country of human geniuses in a data center,  
[00:54:02] I would happily buy $5 trillion worth of compute to run an actual country of  
[00:54:08] human geniuses in a data center. Let's say JPMorgan or Moderna or  
[00:54:11] whatever doesn't want to use them. I've got a country of geniuses.  
[00:54:14] They'll start their own company. If they can't start their own company and they're bottlenecked  
[00:54:18] by clinical trials… It is worth stating that with clinical trials, most clinical trials fail because  
[00:54:22] the drug doesn't work. There's not efficacy. I make exactly that point in "Machines of  
[00:54:27] Loving Grace", I say the clinical trials are going to go much faster  
[00:54:30] than we're used to, but not infinitely fast. Okay, and then suppose it takes a year for  
[00:54:35] the clinical trials to work out so that you're getting revenue from that and can make more drugs.  
[00:54:39] Okay, well, you've got a country of geniuses and you're an AI lab.  
[00:54:44] You could use many more AI researchers. You also think there are these self-reinforcing  
[00:54:50] gains from smart people working on AI tech. You can have the data center  
[00:54:56] working on AI progress. Are there substantially  
[00:55:01] more gains from buying $1 trillion a year of compute versus $300 billion a year of compute?  
[00:55:07] If your competitor is buying a trillion, yes there is.  
[00:55:09] Well, no, there's some gain, but then again, there's this chance that they go bankrupt before.  
[00:55:17] Again, if you're off by only a year, you destroy yourselves. That's the balance. We're  
[00:55:23] buying a lot. We're buying a hell of a lot. We're buying an amount that's comparable to  
[00:55:30] what the biggest players in the game are buying. But if you're asking me, "Why haven't we signed  
[00:55:39] $10 trillion of compute starting in mid-2027?"... First of all, it can't be produced.  
[00:55:44] There isn't that much in the world. But second, what if the country of  
[00:55:50] geniuses comes, but it comes in mid-2028 instead of mid-2027? You go bankrupt.  
[00:55:56] So if your projection is one to three years, it seems like you should want  
[00:56:00] $10 trillion of compute by 2029 at the latest? Even in the longest version of the timelines  
[00:56:11] you state, the compute you are ramping up to build doesn't seem in accordance.  
[00:56:16] What makes you think that? Human wages, let's say,  
[00:56:21] are on the order of $50 trillion a year— So I won't talk about Anthropic in particular,  
[00:56:27] but if you talk about the industry, the amount of compute the industry is building this year is  
[00:56:38] probably, call it, 10-15 gigawatts. It goes up by roughly 3x a year.  
[00:56:48] So next year's 30-40 gigawatts. 2028 might be 100 gigawatts. 2029 might be like 300 gigawatts.  
[00:57:03] I'm doing the math in my head, but each gigawatt costs maybe $10 billion,  
[00:57:07] on the order of $10-15 billion a year. You put that all together and you're  
[00:57:14] getting about what you described. You’re getting exactly that. You're getting multiple  
[00:57:16] trillions a year by 2028 or 2029. You're getting exactly what you predict.  
[00:57:23] That's for the industry. That's for the industry, that’s right.  
[00:57:26] Suppose Anthropic's compute keeps 3x-ing a year, and then by 2027-28, you have 10 gigawatts.  
[00:57:34] Multiply that by, as you say, $10 billion. So then it's like $100 billion a year.  
[00:57:40] But then you're saying the TAM by 2028 is $200 billion.  
[00:57:43] Again, I don't want to give exact numbers for Anthropic, but these numbers are too small.  
[00:57:48] Okay, interesting. You've told investors  
[00:58:49] that you plan to be profitable starting in 2028. This is the year when we're potentially getting  
[00:58:55] the country of geniuses as a data center. This is now going to unlock all this progress  
[00:59:02] in medicine and health and new technologies. Wouldn't this be exactly the time where you'd  
[00:59:11] want to reinvest in the business and build bigger "countries" so they can make more discoveries?  
[00:59:16] Profitability is this kind of weird thing in this field.  
[00:59:21] I don't think in this field profitability is actually a measure of spending down  
[00:59:32] versus investing in the business. Let's just take a model of this.  
[00:59:36] I actually think profitability happens when you underestimated the amount of demand you were going  
[00:59:41] to get and loss happens when you overestimated the amount of demand you were going to get,  
[00:59:46] because you're buying the data centers ahead of time. Think about it this way. Again,  
[00:59:52] these are stylized facts. These numbers are not exact. I'm just trying to make a toy model here.  
[00:59:56] Let's say half of your compute is for training and half of your compute is for inference.  
[01:00:02] The inference has some gross margin that's more than 50%.  
[01:00:07] So what that means is that if you were in steady-state, you build a data center and if  
[01:00:12] you knew exactly the demand you were getting, you would get a certain amount of revenue.  
[01:00:23] Let’s say you pay $100 billion a year for compute. On $50 billion a year you support  
[01:00:28] $150 billion of revenue. The other $50 billion is used for training.  
[01:00:36] Basically you’re profitable and you make $50 billion of profit.  
[01:00:40] Those are the economics of the industry today, or not today but where we’re  
[01:00:45] projecting forward in a year or two. The only thing that makes that not the  
[01:00:49] case is if you get less demand than $50 billion. Then you have more than 50% of your data center  
[01:00:57] for research and you're not profitable. So you train stronger models,  
[01:01:01] but you're not profitable. If you get more demand than you thought, then  
[01:01:07] research gets squeezed, but you're kind of able to support more inference and you're more profitable.  
[01:01:16] Maybe I'm not explaining it well, but the thing I'm trying to say is that you  
[01:01:19] decide the amount of compute first. Then you have some target desire of  
[01:01:24] inference versus training, but that gets determined by demand.  
[01:01:28] It doesn't get determined by you. What I'm hearing is the reason  
[01:01:30] you're predicting profit is that you are systematically underinvesting in compute?  
[01:01:37] No, no, no. I'm saying it's hard to predict. These things about 2028 and when it will happen,  
[01:01:43] that's our attempt to do the best we can with investors.  
[01:01:46] All of this stuff is really uncertain because of the cone of uncertainty.  
[01:01:50] We could be profitable in 2026 if the revenue grows fast enough.  
[01:01:58] If we overestimate or underestimate the next year, that could swing wildly.  
[01:02:04] What I'm trying to get at is that you have a model in your head of a business that invests,  
[01:02:09] invests, invests, gets scale and then becomes profitable.  
[01:02:14] There's a single point at which things turn around.  
[01:02:16] I don't think the economics of this industry work that way.  
[01:02:19] I see. So if I'm understanding correctly, you're saying that because of the discrepancy  
[01:02:24] between the amount of compute we should have gotten and the amount of compute we got,  
[01:02:27] we were sort of forced to make profit. But that doesn't mean we're going  
[01:02:30] to continue making profit. We're going to reinvest the money  
[01:02:33] because now AI has made so much progress and we want a bigger country of geniuses.  
[01:02:37] So back into revenue is high, but losses are also high.  
[01:02:44] If every year we predict exactly what the demand is going to be, we'll be profitable every year.  
[01:02:50] Because spending 50% of your compute on research, roughly, plus a gross margin that's higher than  
[01:03:00] 50% and correct demand prediction leads to profit. That's the profitable business model that I think  
[01:03:07] is kind of there, but obscured by these building ahead and prediction errors.  
[01:03:13] I guess you're treating the 50% as a sort of given constant, whereas in fact,  
[01:03:21] if AI progress is fast and you can increase the progress by scaling up more, you should just have  
[01:03:24] more than 50% and not make profit. But here's what I'll say. You  
[01:03:26] might want to scale it up more. Remember the log returns to scale.  
[01:03:34] If 70% would get you a very little bit of a smaller model through a factor of 1.4x...  
[01:03:42] That extra $20 billion, each dollar there is worth much less to you because of the log-linear setup.  
[01:03:51] So you might find that it's better to invest that $20 billion in serving  
[01:03:58] inference or in hiring engineers who are kind of better at what they're doing.  
[01:04:05] So the reason I said 50%... That's not exactly our target. It's not exactly going to be 50%.  
[01:04:10] It’ll probably vary over time. What I'm saying is the log-linear return, what it leads to is you  
[01:04:18] spend of order one fraction of the business. Like not 5%, not 95%. Then you get diminishing returns.  
[01:04:28] I feel strange that I'm convincing Dario to believe in AI progress or something.  
[01:04:34] Okay, you don't invest in research because it has diminishing returns,  
[01:04:37] but you invest in the other things you mentioned. I think profit at a sort of macro level—  
[01:04:39] Again, I'm talking about diminishing returns, but after you're spending $50 billion a year.  
[01:04:46] This is a point I'm sure you would make, but diminishing returns on a genius could  
[01:04:51] be quite high. More generally,  
[01:04:54] what is profit in a market economy? Profit is basically saying other  
[01:04:58] companies in the market can do more things with this money than I can.  
[01:05:02] Put aside Anthropic. I don't want to give information about Anthropic.  
[01:05:06] That’s why I'm giving these stylized numbers. But let's just derive the  
[01:05:10] equilibrium of the industry. Why doesn't everyone spend 100% of their  
[01:05:21] compute on training and not serve any customers? It's because if they didn't get any revenue,  
[01:05:25] they couldn't raise money, they couldn't do compute deals,  
[01:05:27] they couldn't buy more compute the next year. So there's going to be an equilibrium where every  
[01:05:31] company spends less than 100% on training and certainly less than 100% on inference.  
[01:05:38] It should be clear why you don't just serve the current models and never train another model,  
[01:05:44] because then you don't have any demand because you'll fall behind. So there's some equilibrium.  
[01:05:49] It's not gonna be 10%, it's not gonna be 90%. Let's just say as a stylized fact, it's 50%.  
[01:05:55] That's what I'm getting at. I think we're gonna be in a position where that equilibrium of how much  
[01:06:01] you spend on training is less than the gross margins that you're able to get on compute.  
[01:06:08] So the underlying economics are profitable. The problem is you have this hellish demand  
[01:06:14] prediction problem when you're buying the next year of compute and you might guess under and be  
[01:06:21] very profitable but have no compute for research. Or you might guess over and you are not  
[01:06:30] profitable and you have all the compute for research in the world. Does that make sense?  
[01:06:36] Just as a dynamic model of the industry? Maybe stepping back, I'm not saying I think  
[01:06:42] the "country of geniuses" is going to come in two years and therefore you should buy this compute.  
[01:06:47] To me, the end conclusion you're arriving at makes a lot of sense.  
[01:06:51] But that's because it seems like "country of geniuses" is hard and there's a long way to go.  
[01:06:57] So stepping back, the thing I'm trying to get at is more that it seems like your worldview  
[01:07:03] is compatible with somebody who says, "We're like 10 years away from a world in which we're  
[01:07:07] generating trillions of dollars of value." That's just not my view. So I'll make  
[01:07:14] another prediction. It is hard for me to see that there won't be trillions  
[01:07:20] of dollars in revenue before 2030. I can construct a plausible world.  
[01:07:26] It takes maybe three years. That would be the end of what I think it's plausible.  
[01:07:31] Like in 2028, we get the real "country of geniuses in the data center".  
[01:07:36] The revenue's going into the low hundreds of billions by 2028, and then the country  
[01:07:46] of geniuses accelerates it to trillions. We’re basically on the slow end of diffusion.  
[01:07:52] It takes two years to get to the trillions. That would be the world where it takes until 2030.  
[01:07:59] I suspect even composing the technical exponential and diffusion exponential,  
[01:08:05] we’ll get there before 2030. So you laid out a model where Anthropic makes  
[01:08:10] profit because it seems like fundamentally we're in a compute-constrained world.  
[01:08:14] So eventually we keep growing compute— I think the way the profit comes is… Again,  
[01:08:21] let's just abstract the whole industry here. Let's just imagine we're in an economics textbook.  
[01:08:27] We have a small number of firms. Each can invest a limited amount.  
[01:08:33] Each can invest some fraction in R&D. They have some marginal cost to serve.  
[01:08:38] The gross profit margins on that marginal cost are very high because inference is efficient.  
[01:08:47] There's some competition, but the models are also differentiated.  
[01:08:52] Companies will compete to push their research budgets up.  
[01:08:55] But because there's a small number of players, we have the... What is it called?  
[01:09:00] The Cournot equilibrium, I think, is what the small number of firm equilibrium is.  
[01:09:05] The point is it doesn't equilibrate to perfect competition with zero margins.  
[01:09:15] If there's three firms in the economy and all are kind of independently behaving rationally,  
[01:09:20] it doesn't equilibrate to zero. Help me understand that, because  
[01:09:24] right now we do have three leading firms and they're not making profit. So what is changing?  
[01:09:33] Again, the gross margins right now are very positive.  
[01:09:38] What's happening is a combination of two things. One is that we're still in the exponential  
[01:09:43] scale-up phase of compute. A model gets trained. Let's say a model got  
[01:09:53] trained that costs $1 billion last year. Then this year it produced $4 billion of  
[01:10:02] revenue and cost $1 billion to inference from. Again, I'm using stylized numbers here, but that  
[01:10:12] would be 75% gross margins and this 25% tax. So that model as a whole makes $2 billion.  
[01:10:23] But at the same time, we're spending $10 billion to train the next model because  
[01:10:27] there's an exponential scale-up. So the company loses money. Each model  
[01:10:31] makes money, but the company loses money. The equilibrium I'm talking about is an  
[01:10:35] equilibrium where we have the "country of geniuses in a data center", but that  
[01:10:43] model training scale-up has equilibrated more. Maybe it's still going up. We're still trying to  
[01:10:49] predict the demand, but it's more leveled out. I'm confused about a couple of things there.  
[01:10:56] Let's start with the current world. In the current world, you're right that,  
[01:11:00] as you said before, if you treat each individual model as a company, it's profitable.  
[01:11:05] But of course, a big part of the production function of being a frontier lab is training  
[01:11:11] the next model, right? Yes, that's right.  
[01:11:13] If you didn't do that, then you'd make profit for two months and then  
[01:11:16] you wouldn't have margins because you wouldn't have the best model.  
[01:11:19] But at some point that reaches the biggest scale that it can reach.  
[01:11:23] And then in equilibrium, we have algorithmic improvements, but we're spending roughly the  
[01:11:28] same amount to train the next model as we spend to train the current model.  
[01:11:37] At some point you run out of money in the economy. A fixed lump of labor fallacy… The economy is  
[01:11:42] going to grow, right? That's one of your predictions. We're going  
[01:11:44] to have the data centers in space. Yes, but this is another example  
[01:11:47] of the theme I was talking about. The economy will grow much faster  
[01:11:53] with AI than I think it ever has before. Right now the compute is growing 3x a year.  
[01:11:59] I don't believe the economy is gonna grow 300% a year.  
[01:12:03] I said this in "Machines of Loving Grace", I think we may get 10-20%  
[01:12:08] per year growth in the economy, but we're not gonna get 300% growth in the economy.  
[01:12:13] So I think in the end, if compute becomes the majority of what the economy produces,  
[01:12:18] it's gonna be capped by that. So let's assume a model  
[01:12:22] where compute stays capped. The world where frontier labs are making money  
[01:12:26] is one where they continue to make fast progress. Because fundamentally your margin is limited by  
[01:12:34] how good the alternative is. So you are able to make money  
[01:12:37] because you have a frontier model. If you didn't have a frontier model  
[01:12:39] you wouldn't be making money. So this model requires there  
[01:12:45] never to be a steady state. Forever and ever you keep  
[01:12:48] making more algorithmic progress. I don't think that's true. I mean,  
[01:12:51] I feel like we're in an economics class. Do you know the Tyler Cowen quote?  
[01:12:59] We never stop talking about economics. We never stop talking about economics.  
[01:13:03] So no, I don't think this field's going to be a monopoly.  
[01:13:12] All my lawyers never want me to say the word "monopoly".  
[01:13:15] But I don't think this field's going to be a monopoly.  
[01:13:17] You do get industries in which there are a small number of players.  
[01:13:21] Not one, but a small number of players. Ordinarily, the way you get monopolies  
[01:13:27] like Facebook or Meta—I always call them Facebook—is these kinds of network effects.  
[01:13:37] The way you get industries in which there are a small number of players,  
[01:13:41] is very high costs of entry. Cloud is like this. I think cloud is a good example of this.  
[01:13:49] There are three, maybe four, players within cloud. I think that's the same for AI, three, maybe four.  
[01:13:56] The reason is that it's so expensive. It requires so much expertise and so  
[01:14:02] much capital to run a cloud company. You have to put up all this capital.  
[01:14:08] In addition to putting up all this capital, you have to get all of this other stuff  
[01:14:11] that requires a lot of skill to make it happen. So if you go to someone and you're like, "I want  
[01:14:17] to disrupt this industry, here's $100 billion." You're like, "okay, I'm putting in $100 billion  
[01:14:22] and also betting that you can do all these other things that these people have been doing."  
[01:14:26] Only to decrease the profit. The effect of your entering  
[01:14:29] is that profit margins go down. So, we have equilibria like this  
[01:14:33] all the time in the economy where we have a few players. Profits are not astronomical. Margins  
[01:14:39] are not astronomical, but they're not zero. That's what we see on cloud. Cloud is very  
[01:14:47] undifferentiated. Models are more differentiated than cloud.  
[01:14:51] Everyone knows Claude is good at different things than GPT is good at, than Gemini is good at.  
[01:14:58] It's not just that Claude's good at coding, GPT is good at math and reasoning.  
[01:15:05] It's more subtle than that. Models are good at different types of coding. Models have different  
[01:15:09] styles. I think these things are actually quite different from each other, and so I would expect  
[01:15:15] more differentiation than you see in cloud. Now, there actually is one counter-argument.  
[01:15:26] That counter-argument is if the process of producing models,  
[01:15:32] if AI models can do that themselves, then that could spread throughout the economy.  
[01:15:37] But that is not an argument for commoditizing AI models in general.  
[01:15:41] That's kind of an argument for commoditizing the whole economy at once.  
[01:15:45] I don't know what quite happens in that world where basically anyone  
[01:15:48] can do anything, anyone can build anything, and there's no moat around anything at all.  
[01:15:53] I don't know, maybe we want that world. Maybe that's the end state here.  
[01:15:58] Maybe when AI models can do everything, if we've solved all the safety and security problems,  
[01:16:09] that's one of the mechanisms for the economy just flattening itself again.  
[01:16:17] But that's kind of far post-"country of geniuses in the data center."  
[01:16:23] Maybe a finer way to put that potential point is: 1) it seems like AI research is especially  
[01:16:32] loaded on raw intellectual power, which will be especially abundant in the world of AGI.  
[01:16:37] And 2) if you just look at the world today, there are very few technologies that seem to be  
[01:16:41] diffusing as fast as AI algorithmic progress. So that does hint that this industry is  
[01:16:50] sort of structurally diffusive. I think coding is going fast, but  
[01:16:54] I think AI research is a superset of coding and there are aspects of it that are not going fast.  
[01:17:00] But I do think, again, once we get coding, once we get AI models going fast, then that will speed up  
[01:17:07] the ability of AI models to do everything else. So while coding is going fast now, I think once  
[01:17:13] the AI models are building the next AI models and building everything else,  
[01:17:17] the whole economy will kind of go at the same pace. I am worried geographically, though.  
[01:17:24] I'm a little worried that just proximity to AI, having heard about AI, may be one differentiator.  
[01:17:34] So when I said the 10-20% growth rate, a worry I have is that the growth rate could be like 50%  
[01:17:42] in Silicon Valley and parts of the world that are socially connected to Silicon Valley, and not that  
[01:17:50] much faster than its current pace elsewhere. I think that'd be a pretty messed up world.  
[01:17:54] So one of the things I think about a lot is how to prevent that.  
[01:17:57] Do you think that once we have this country of geniuses in a data center, that  
[01:18:01] robotics is sort of quickly solved afterwards? Because it seems like a big problem with robotics  
[01:18:06] is that a human can learn how to teleoperate current hardware, but current AI models can't,  
[01:18:12] at least not in a way that's super productive. And so if we have this ability to learn like  
[01:18:16] a human, shouldn't it solve robotics immediately as well?  
[01:18:19] I don't think it's dependent on learning like a human.  
[01:18:21] It could happen in different ways. Again, we could have trained the model on  
[01:18:25] many different video games, which are like robotic controls, or many different simulated robotics  
[01:18:30] environments, or just train them to control computer screens, and they learn to generalize.  
[01:18:34] So it will happen... it's not necessarily dependent on human-like learning.  
[01:18:41] Human-like learning is one way it could happen. If the model's like, "Oh, I pick up a robot,  
[01:18:44] I don't know how to use it, I learn," that could happen because we discovered continual learning.  
[01:18:50] That could also happen because we trained the model on a bunch of environments and  
[01:18:54] then generalized, or it could happen because the model learns that in the context length.  
[01:18:58] It doesn't actually matter which way. If we go back to the discussion we had  
[01:19:03] an hour ago, that type of thing can happen in several different ways.  
[01:19:10] But I do think when for whatever reason the models have those skills, then robotics will be  
[01:19:16] revolutionized—both the design of robots, because the models will be much better than humans at  
[01:19:21] that, and also the ability to control robots. So we'll get better at building the physical  
[01:19:28] hardware, building the physical robots, and we'll also get better at controlling it.  
[01:19:32] Now, does that mean the robotics industry will also be generating  
[01:19:36] trillions of dollars of revenue? My answer there is yes, but there will be  
[01:19:40] the same extremely fast, but not infinitely fast diffusion. So will robotics be revolutionized?  
[01:19:46] Yeah, maybe tack on another year or two. That's the way I think about these things.  
[01:19:52] Makes sense. There's a general skepticism about extremely fast progress. Here's my view. It sounds  
[01:19:58] like you are going to solve continual learning one way or another within a matter of years.  
[01:20:02] But just as people weren't talking about continual learning a couple of years ago,  
[01:20:06] and then we realized, "Oh, why aren't these models as useful as they could be right now,  
[01:20:09] even though they are clearly passing the Turing test and are experts in so many different domains?  
[01:20:14] Maybe it's this thing." Then we solve this thing and we realize, actually, there's another thing  
[01:20:19] that human intelligence can do that's a basis of human labor that these models can't do.  
[01:20:24] So why not think there will be more things like this, where  
[01:20:28] we've found more pieces of human intelligence? Well, to be clear, I think continual learning, as  
[01:20:33] I've said before, might not be a barrier at all. I think we may just get there by pre-training  
[01:20:40] generalization and RL generalization. I think there just  
[01:20:48] might not be such a thing at all. In fact, I would point to the history  
[01:20:51] in ML of people coming up with things that are barriers that end up kind of  
[01:20:56] dissolving within the big blob of compute. People talked about, "How do your models  
[01:21:06] keep track of nouns and verbs?" "They can understand syntactically,  
[01:21:11] but they can't understand semantically? It's only statistical correlations."  
[01:21:16] "You can understand a paragraph, you can’t understand a word.  
[01:21:19] There's reasoning, you can't do reasoning." But then suddenly it turns out you can  
[01:21:23] do code and math very well. So I think there's actually a  
[01:21:27] stronger history of some of these things seeming like a big deal and then kind of dissolving. Some  
[01:21:35] of them are real. The need for data is real, maybe continual learning is a real thing.  
[01:21:42] But again, I would ground us in something like code.  
[01:21:46] I think we may get to the point in a year or two where the models can  
[01:21:50] just do SWE end-to-end. That's a whole task. That's a whole sphere of human activity that  
[01:21:56] we're just saying models can do now. When you say end-to-end, do you mean  
[01:22:02] setting technical direction, understanding the context of the problem, et cetera?  
[01:22:06] Yes. I mean all of that. Interesting. I feel like that is AGI-complete,  
[01:22:13] which maybe is internally consistent. But it's not like saying 90%  
[01:22:17] of code or 100% of code. No, I gave this spectrum:  
[01:22:22] 90% of code, 100% of code, 90% of end-to-end SWE, 100% of end-to-end SWE.  
[01:22:28] New tasks are created for SWEs. Eventually those get done as well.  
[01:22:31] It's a long spectrum there, but we're traversing the spectrum very quickly.  
[01:22:35] I do think it's funny that I've seen a couple of podcasts you've done where  
[01:22:40] the hosts will be like, "But Dwarkesh wrote the essay about the continuous learning thing."  
[01:22:43] It always makes me crack up because you've been an AI researcher for 10 years.  
[01:22:48] I'm sure there's some feeling of, "Okay, so a podcaster wrote an essay,  
[01:22:53] and every interview I get asked about it." The truth of the matter is that we're all  
[01:22:59] trying to figure this out together. There are some ways in which I'm  
[01:23:04] able to see things that others aren't. These days that probably has more to do  
[01:23:08] with seeing a bunch of stuff within Anthropic and having to make a bunch of decisions than I have  
[01:23:13] any great research insight that others don't. I'm running a 2,500 person company.  
[01:23:20] It's actually pretty hard for me to have concrete research insight, much harder than it would have  
[01:23:27] been 10 years ago or even two or three years ago. As we go towards a world of a full drop-in  
[01:23:36] remote worker replacement, does an API pricing model still make the most sense?  
[01:23:42] If not, what is the correct way to price AGI, or serve AGI?  
[01:23:45] I think there's going to be a bunch of different business models here, all at once,  
[01:23:49] that are going to be experimented with. I actually do think that the API  
[01:23:59] model is more durable than many people think. One way I think about it is if the technology  
[01:24:06] is advancing quickly, if it's advancing exponentially, what that means is there's  
[01:24:12] always a surface area of new use cases that have been developed in the last three months.  
[01:24:20] Any kind of product surface you put in place is always at risk of sort of becoming irrelevant.  
[01:24:27] Any given product surface probably makes sense for a range of capabilities of the model.  
[01:24:32] The chatbot is already running into limitations where making it smarter doesn't really help the  
[01:24:39] average consumer that much. But I don't think that's  
[01:24:41] a limitation of AI models. I don't think that's evidence  
[01:24:45] that the models are good enough and them getting better doesn't matter to the economy.  
[01:24:51] It doesn't matter to that particular product. So I think the value of the API is that the API  
[01:24:58] always offers an opportunity, very close to the bare metal, to build on what the latest thing is.  
[01:25:06] There's always going to be this front of new startups and new ideas that  
[01:25:14] weren't possible a few months ago and are possible because the model is advancing.  
[01:25:19] I actually predict that it's going to exist alongside other models, but we're always going  
[01:25:28] to have the API business model because there's always going to be a need for a thousand different  
[01:25:34] people to try experimenting with the model in a different way. 100 of them become startups and  
[01:25:40] ten of them become big successful startups. Two or three really end up being the way  
[01:25:45] that people use the model of a given generation. So I basically think it's always going to exist.  
[01:25:50] At the same time, I'm sure there's going to be other models as well.  
[01:25:55] Not every token that's output by the model is worth the same amount.  
[01:26:00] Think about what is the value of the tokens that the model outputs when someone calls  
[01:26:10] them up and says, "My Mac isn't working," or something, the model's like, "restart it."  
[01:26:16] Someone hasn't heard that before, but the model said that 10 million times.  
[01:26:23] Maybe that's worth like a dollar or a few cents or something.  
[01:26:26] Whereas if the model goes to one of the pharmaceutical companies and it says, "Oh,  
[01:26:34] you know, this molecule you're developing, you should take the aromatic ring from that end of the  
[01:26:39] molecule and put it on that end of the molecule. If you do that, wonderful things will happen."  
[01:26:46] Those tokens could be worth tens of millions of dollars.  
[01:26:52] So I think we're definitely going to see business models that recognize that.  
[01:26:56] At some point we're going to see "pay for results" in some form, or we may see forms of compensation  
[01:27:06] that are like labor, that kind of work by the hour. I don't know. I think because it's a new  
[01:27:16] industry, a lot of things are going to be tried. I don't know what will turn out to  
[01:27:19] be the right thing. I take your point that  
[01:27:24] people will have to try things to figure out what is the best way to use this blob of intelligence.  
[01:27:28] But what I find striking is Claude Code. I don't think in the history of startups  
[01:27:34] there has been a single application that has been as hotly competed in as coding agents.  
[01:27:42] Claude Code is a category leader here. That seems surprising to me. It doesn't seem  
[01:27:49] intrinsically that Anthropic had to build this. I wonder if you have an accounting of why it had  
[01:27:54] to be Anthropic or how Anthropic ended up building an application in addition  
[01:27:58] to the model underlying it that was successful. So it actually happened in a pretty simple way,  
[01:28:02] which is that we had our own coding models, which were good at coding.  
[01:28:09] Around the beginning of 2025, I said, "I think the time has come where you can have  
[01:28:14] nontrivial acceleration of your own research if you're an AI company by using these models."  
[01:28:21] Of course, you need an interface, you need a harness to use them.  
[01:28:25] So I encouraged people internally. I didn't say this is one thing that you have to use.  
[01:28:31] I just said people should experiment with this. I think it might have been originally  
[01:28:37] called Claude CLI, and then the name eventually got changed to Claude Code.  
[01:28:42] Internally, it was the thing that everyone was using and it was seeing fast internal adoption.  
[01:28:48] I looked at it and I said, "Probably we should launch this externally, right?"  
[01:28:53] It's seen such fast adoption within Anthropic. Coding is a lot of what we do.  
[01:28:59] We have an audience of many, many hundreds of people that's in some ways at least  
[01:29:04] representative of the external audience. So it looks like we already have product  
[01:29:08] market fit. Let's launch this thing. And then we launched it. I think just the fact that we  
[01:29:15] ourselves are kind of developing the model and we ourselves know what we most need to use the model,  
[01:29:21] I think it's kind of creating this feedback loop. I see. In the sense that you, let's say a  
[01:29:26] developer at Anthropic is like, "Ah, it would be better if it was better at this X thing."  
[01:29:31] Then you bake that into the next model that you build.  
[01:29:35] That's one version of it, but then there's just the ordinary product iteration.  
[01:29:41] We have a bunch of coders within Anthropic, they use Claude Code  
[01:29:47] every day and so we get fast feedback. That was more important in the early days.  
[01:29:50] Now, of course, there are millions of people using it, and so we get  
[01:29:53] a bunch of external feedback as well. But it's just great to be able to get  
[01:29:58] kind of fast internal feedback. I think this is the reason why we  
[01:30:03] launched a coding model and didn't launch a pharmaceutical company.  
[01:30:10] My background's in biology, but we don't have any of the resources that  
[01:30:14] are needed to launch a pharmaceutical company. Let me now ask you about making AI go well.  
[01:31:24] It seems like whatever vision we have about how AI goes well has to be compatible with two things:  
[01:31:30] 1) the ability to build and run AIs is diffusing extremely rapidly and 2) the  
[01:31:37] population of AIs, the amount we have and their intelligence, will also increase very rapidly.  
[01:31:44] That means that lots of people will be able to build huge populations of misaligned AIs,  
[01:31:49] or AIs which are just companies which are trying to increase their  
[01:31:53] footprint or have weird psyches like Sydney Bing, but now they're superhuman.  
[01:31:57] What is a vision for a world in which we have an equilibrium that is compatible  
[01:32:02] with lots of different AIs, some of which are misaligned, running around?  
[01:32:06] I think in "The Adolescence of Technology", I was skeptical of the balance of power.  
[01:32:13] But the thing I was specifically skeptical of is you have three or four of these companies  
[01:32:23] all building models that are derived from the same thing, that they would check each other.  
[01:32:36] Or even that any number of them would check each other.  
[01:32:40] We might live in an offense-dominant world where one person or one AI model is smart enough to do  
[01:32:47] something that causes damage for everything else. In the short run, we have a limited number  
[01:32:54] of players now. So we can start  
[01:32:56] within the limited number of players. We need to put in place the safeguards.  
[01:33:03] We need to make sure everyone does the right alignment work.  
[01:33:05] We need to make sure everyone has bioclassifiers. Those are the immediate things we need to do.  
[01:33:11] I agree that that doesn't solve the problem in the long run, particularly if the ability of  
[01:33:16] AI models to make other AI models proliferates, then the whole thing can become harder to solve.  
[01:33:26] I think in the long run we need some architecture of governance.  
[01:33:30] We need some architecture of governance that preserves human freedom,  
[01:33:35] but also allows us to govern a very large number of human systems, AI systems, hybrid  
[01:33:52] human-AI companies or economic units. So we're gonna need to think about:  
[01:34:01] how do we protect the world against bioterrorism? How do we protect the world against mirror life?  
[01:34:11] Probably we're gonna need some kind of AI monitoring system  
[01:34:15] that monitors for all of these things. But then we need to build this in a way  
[01:34:20] that preserves civil liberties and our constitutional rights.  
[01:34:24] So I think just as anything else, it's a new security landscape with a new set of  
[01:34:34] tools and a new set of vulnerabilities. My worry is, if we had 100 years for this  
[01:34:40] to happen all very slowly, we'd get used to it. We've gotten used to the presence of explosives  
[01:34:49] in society or the presence of various new weapons or the presence of video cameras.  
[01:34:58] We would get used to it over 100 years and we’d develop governance mechanisms. We'd  
[01:35:03] make our mistakes. My worry is just that this is happening all so fast.  
[01:35:07] So maybe we need to do our thinking faster about how to make these governance mechanisms work.  
[01:35:13] It seems like in an offense-dominant world, over the course of the next century—the idea is that AI  
[01:35:19] is making the progress that would happen over the next century happen in some period of five to ten  
[01:35:22] years—we would still need the same mechanisms, or balance of power would be similarly intractable,  
[01:35:29] even if humans were the only game in town. I guess we have the advice of AI.  
[01:35:36] But it fundamentally doesn't seem like a totally different ball game here.  
[01:35:41] If checks and balances were going to work, they would work with humans as well.  
[01:35:44] If they aren't going to work, they wouldn't work with AIs as well.  
[01:35:47] So maybe this just dooms human checks and balances as well.  
[01:35:51] Again, I think there's some way to make this happen.  
[01:35:58] The governments of the world may have to work together to make it happen.  
[01:36:02] We may have to talk to AIs about building societal structures in such a way that these  
[01:36:10] defenses are possible. I don't know. I don’t want to say this is so far ahead in time,  
[01:36:15] but it’s so far ahead in technological ability that may happen over a short period of time,  
[01:36:21] that it's hard for us to anticipate it in advance. Speaking of governments getting involved,  
[01:36:25] on December 26, the Tennessee legislature introduced a bill which said, "It would  
[01:36:31] be an offense for a person to knowingly train artificial intelligence to provide  
[01:36:34] emotional support, including through open-ended conversations with a user."  
[01:36:39] Of course, one of the things that Claude attempts to do is be a thoughtful, knowledgeable friend.  
[01:36:48] In general, it seems like we're going to have this patchwork of state laws.  
[01:36:52] A lot of the benefits that normal people could experience as a result of AI are going to be  
[01:36:56] curtailed, especially when we get into the kinds of things you discuss in "Machines  
[01:36:59] of Loving Grace": biological freedom, mental health improvements, et cetera.  
[01:37:02] It seems easy to imagine worlds in which these get Whac-A-Moled away by different laws, whereas  
[01:37:10] bills like this don't seem to address the actual existential threats that you're concerned about.  
[01:37:15] I'm curious to understand, in the context of things like this, Anthropic's position  
[01:37:20] against the federal moratorium on state AI laws. There are many different things going on at once.  
[01:37:28] I think that particular law is dumb. It was clearly made by legislators  
[01:37:34] who just probably had little idea what AI models could do and not do.  
[01:37:38] They're like, "AI models serving us, that just sounds scary.  
[01:37:41] I don't want that to happen." So we're not in favor of that.  
[01:37:47] But that wasn't the thing that was being voted on. The thing that was being voted on is:  
[01:37:52] we're going to ban all state regulation of AI for 10 years with no apparent plan to do any  
[01:38:00] federal regulation of AI, which would take Congress to pass, which is a very high bar.  
[01:38:05] So the idea that we'd ban states from doing anything for 10 years… People said they had  
[01:38:11] a plan for the federal government, but there was no actual proposal on the table. There was  
[01:38:15] no actual attempt. Given the serious dangers that I lay out in "Adolescence of Technology"  
[01:38:22] around things like biological weapons and bioterrorism autonomy risk, and the  
[01:38:29] timelines we've been talking about—10 years is an eternity—I think that's a crazy thing to do.  
[01:38:36] So if that's the choice, if that's what you force us to choose, then we're going  
[01:38:42] to choose not to have that moratorium. I think the benefits of that position  
[01:38:47] exceed the costs, but it's not a perfect position if that's the choice.  
[01:38:51] Now, I think the thing that we should do, the thing that I would support, is the federal  
[01:38:56] government should step in, not saying "states you can't regulate", but "Here's what we're going to  
[01:39:02] do, and states you can't differ from this." I think preemption is fine in the sense of  
[01:39:08] saying that the federal government says, "Here is our standard. This applies to everyone.  
[01:39:12] States can't do something different." That would be something I would support  
[01:39:16] if it would be done in the right way. But this idea of states, "You can't do  
[01:39:22] anything and we're not doing anything either," that struck us as very much not making sense.  
[01:39:29] I think it will not age well, it is already starting to not age well with  
[01:39:33] all the backlash that you've seen. Now, in terms of what we would want,  
[01:39:39] the things we've talked about are starting with transparency standards in order to monitor some  
[01:39:46] of these autonomy risks and bioterrorism risks. As the risks become more serious, as we get more  
[01:39:53] evidence for them, then I think we could be more aggressive in some targeted ways and say, "Hey,  
[01:39:58] AI bioterrorism is really a threat. Let's pass a law that forces  
[01:40:04] people to have classifiers." I could even imagine… It depends.  
[01:40:07] It depends how serious the threat it ends up being. We don't know for sure. We need to pursue  
[01:40:12] this in an intellectually honest way where we say that ahead of time, the risk has not emerged yet.  
[01:40:16] But I could certainly imagine, with the pace that things are going at,  
[01:40:21] a world where later this year we say, "Hey, this AI bioterrorism stuff is really serious.  
[01:40:27] We should do something about it. We should put it in a federal standard.  
[01:40:31] If the federal government won't act, we should put it in a state standard." I could totally see that.  
[01:40:36] I'm concerned about a world where if you just consider the pace of progress you're expecting,  
[01:40:42] the life cycle of legislation... The benefits are, as you say because  
[01:40:48] of diffusion lag, slow enough that I really do think this patchwork of state  
[01:40:55] laws, on the current trajectory, would prohibit. I mean if having an emotional chatbot friend is  
[01:40:59] something that freaks people out, then just imagine the kinds of actual benefits from AI  
[01:41:03] we want normal people to be able to experience. From improvements in health and healthspan and  
[01:41:08] improvements in mental health and so forth. Whereas at the same time, it seems like you  
[01:41:13] think the dangers are already on the horizon and I just don't see that much… It seems like it would  
[01:41:19] be especially injurious to the benefits of AI as compared to the dangers of AI.  
[01:41:24] So that's maybe where the cost benefit makes less sense to me.  
[01:41:27] So there's a few things here. People talk about there being  
[01:41:31] thousands of these state laws. First of all, the vast,  
[01:41:34] vast majority of them do not pass. The world works a certain way in theory,  
[01:41:41] but just because a law has been passed doesn't mean it's really enforced.  
[01:41:44] The people implementing it may be like, "Oh my God, this is stupid.  
[01:41:48] It would mean shutting off everything that's ever been built in Tennessee."  
[01:41:55] Very often, laws are interpreted in a way that makes them not as dangerous or harmful.  
[01:42:02] On the same side, of course, you have to worry if you're passing a law to stop a bad thing;  
[01:42:06] you have this problem as well. My basic view is that if we could  
[01:42:16] decide what laws were passed and how things were done—and we’re only one small input  
[01:42:21] into that—I would deregulate a lot of the stuff around the health benefits of AI.  
[01:42:29] I don't worry as much about the chatbot laws. I actually worry more about the drug approval  
[01:42:37] process, where I think AI models are going to greatly accelerate the rate at which we discover  
[01:42:45] drugs, and the pipeline will get jammed up. The pipeline will not be prepared to process  
[01:42:50] all the stuff that's going through it. I think reform of the regulatory process  
[01:42:58] should bias more towards the fact that we have a lot of things coming where the safety and  
[01:43:02] efficacy is actually going to be really crisp and clear, a beautiful thing, and really effective.  
[01:43:12] Maybe we don't need all this superstructure around it that was designed around an era of drugs that  
[01:43:21] barely work and often have serious side effects. At the same time, I think we should be  
[01:43:26] ramping up quite significantly the safety and security legislation.  
[01:43:35] Like I've said, starting with transparency is my view of trying not to hamper the industry,  
[01:43:43] trying to find the right balance. I'm worried about it. Some people criticize  
[01:43:46] my essay for saying, "That's too slow. The dangers of AI will come too soon  
[01:43:50] if we do that." Well, basically,  
[01:43:52] I think the last six months and maybe the next few months are going to be about transparency.  
[01:43:58] Then, if these risks emerge when we're more certain of them—which  
[01:44:02] I think we might be as soon as later this year—then I think we need to act very fast  
[01:44:07] in the areas where we've actually seen the risk. I think the only way to do this is to be nimble.  
[01:44:13] Now, the legislative process is normally not nimble, but we need to emphasize the  
[01:44:21] urgency of this to everyone involved. That's why I'm sending this message of urgency.  
[01:44:24] That's why I wrote Adolescence of Technology. I wanted policymakers, economists, national  
[01:44:30] security professionals, and decision-makers to read it so that they have some hope of acting  
[01:44:36] faster than they would have otherwise. Is there anything you can do or advocate  
[01:44:42] that would make it more certain that the benefits of AI are better instantiated?  
[01:44:51] I feel like you have worked with legislatures to say, "Okay,  
[01:44:54] we're going to prevent bioterrorism here. We're going to increase transparency, we're  
[01:44:57] going to increase whistleblower protection." But I think by default, the actual benefits  
[01:45:01] we're looking forward to seem very fragile to different kinds of moral panics or  
[01:45:08] political economy problems. I don't actually agree that  
[01:45:12] much regarding the developed world. I feel like in the developed world,  
[01:45:17] markets function pretty well. When there's a lot of money to  
[01:45:23] be made on something and it's clearly the best available alternative, it's actually hard for  
[01:45:27] the regulatory system to stop it. We're seeing that in AI itself.  
[01:45:33] A thing I've been trying to fight for is export controls on chips to China.  
[01:45:38] That's in the national security interest of the US.  
[01:45:42] That's squarely within the policy beliefs of almost everyone in Congress of both parties.  
[01:45:52] The case is very clear. The counterarguments against it, I'll politely call them fishy.  
[01:45:59] Yet it doesn't happen and we sell the chips because there's so much money riding on it.  
[01:46:08] That money wants to be made. In that case, in my opinion, that's a bad thing.  
[01:46:13] But it also applies when it's a good thing. So if we're talking about drugs and benefits of  
[01:46:23] the technology, I am not as worried about those benefits being hampered in the developed world.  
[01:46:30] I am a little worried about them going too slow. As I said, I do think we should work to speed  
[01:46:37] the approval process in the FDA. I do think we should fight against  
[01:46:41] these chatbot bills that you're describing. Described individually, I'm against them. I  
[01:46:46] think they're stupid. But I actually think the bigger worry is the developing world, where we  
[01:46:51] don't have functioning markets and where we often can't build on the technology that we've had.  
[01:46:58] I worry more that those folks will get left behind.  
[01:47:01] And I worry that even if the cures are developed, maybe there's someone in rural  
[01:47:04] Mississippi who doesn't get it as well. That's a smaller version of the concern  
[01:47:10] we have in the developing world. So the things we've been doing  
[01:47:14] are working with philanthropists. We work with folks who deliver medicine and  
[01:47:26] health interventions to the developing world, to sub-Saharan Africa, India, Latin America,  
[01:47:34] and other developing parts of the world. That's the thing I think that  
[01:47:39] won't happen on its own. You mentioned export controls.  
[01:47:42] Why shouldn't the US and China both have a "country of geniuses in a data center"?  
[01:47:48] Why won’t it happen or why shouldn't it happen? Why shouldn't it happen.  
[01:47:54] If this does happen, we could have a few situations.  
[01:48:02] If we have an offense-dominant situation, we could have a situation  
[01:48:05] like nuclear weapons, but more dangerous. Either side could easily destroy everything.  
[01:48:14] We could also have a world where it's unstable. The nuclear equilibrium is  
[01:48:19] stable because it's deterrence. But let's say there was uncertainty about,  
[01:48:24] if the two AIs fought, which AI would win? That could create instability. You often have  
[01:48:30] conflict when the two sides have a different assessment of their likelihood of winning.  
[01:48:34] If one side is like, "Oh yeah, there's a 90% chance I'll win," and the other side thinks  
[01:48:40] the same, then a fight is much more likely. They can't both be right,  
[01:48:43] but they can both think that. But this seems like a fully general argument  
[01:48:46] against the diffusion of AI technology. That's the implication of this world.  
[01:48:52] Let me just go on, because I think we will get diffusion eventually.  
[01:48:55] The other concern I have is that governments will oppress their own people with AI.  
[01:49:04] I'm worried about a world where you have a country in which there’s already a government that's  
[01:49:16] building a high-tech authoritarian state. To be clear, this is about the government.  
[01:49:21] This is not about the people. We need to find a way for  
[01:49:24] people everywhere to benefit. My worry here is about governments.  
[01:49:30] My worry is if the world gets carved up into two pieces, one of those two pieces  
[01:49:33] could be authoritarian or totalitarian in a way that's very difficult to displace.  
[01:49:39] Now, will governments eventually get powerful AI, and is there a risk of authoritarianism?  
[01:49:45] Yes. Will governments eventually get powerful AI, and is there a risk of  
[01:49:52] bad equilibria? Yes, I think both things. But the initial conditions matter. At some point, we're  
[01:50:00] going to need to set up the rules of the road. I'm not saying that one country, either the United  
[01:50:05] States or a coalition of democracies—which I think would be a better setup, although it  
[01:50:09] requires more international cooperation than we currently seem to want to make—should just say,  
[01:50:19] "These are the rules of the road." There's going to be some negotiation.  
[01:50:22] The world is going to have to grapple with this. What I would like is for the democratic nations of  
[01:50:31] the world—those whose governments represent closer to pro-human values—are holding the  
[01:50:39] stronger hand and have more leverage when the rules of the road are set.  
[01:50:44] So I'm very concerned about that initial condition.  
[01:50:47] I was re-listening to the interview from three years ago, and one of the ways it  
[01:50:51] aged poorly is that I kept asking questions assuming there was going to be some key  
[01:50:55] fulcrum moment two to three years from now. In fact, being that far out, it just seems  
[01:51:00] like progress continues, AI improves, AI is more diffused, and people will use it for more things.  
[01:51:05] It seems like you're imagining a world in the future where the countries get together, and  
[01:51:09] "Here's the rules of the road, here's the leverage we have, and here's the leverage you have."  
[01:51:13] But on the current trajectory, everybody will have more AI.  
[01:51:18] Some of that AI will be used by authoritarian countries.  
[01:51:20] Some of that within the authoritarian countries will be used by private  
[01:51:22] actors versus state actors. It's not clear who will benefit more.  
[01:51:26] It's always unpredictable to tell in advance. It seems like the internet privileged  
[01:51:30] authoritarian countries more than you would've expected.  
[01:51:33] Maybe AI will be the opposite way around. I want to better understand what  
[01:51:38] you're imagining here. Just to be precise about it,  
[01:51:42] I think the exponential of the underlying technology will continue as it has before.  
[01:51:47] The models get smarter and smarter, even when they get to a "country of geniuses in a data center."  
[01:51:53] I think you can continue to make the model smarter.  
[01:51:56] There's a question of getting diminishing returns on their value in the world.  
[01:52:01] How much does it matter after you've already solved human biology?  
[01:52:07] At some point you can do harder, more abstruse math problems, but nothing after that matters.  
[01:52:12] Putting that aside, I do think the exponential will continue, but there will be certain  
[01:52:18] distinguished points on the exponential. Companies, individuals, and countries  
[01:52:24] will reach those points at different times. In "The Adolescence of Technology" I talk about:  
[01:52:31] Is a nuclear deterrent still stable in the world of AI?  
[01:52:38] I don't know, but that's an example of one thing we've taken for granted.  
[01:52:42] The technology could reach such a level that we can no longer be certain of it.  
[01:52:50] Think of others. There are points where if you reach a certain level, maybe you have offensive  
[01:52:57] cyber dominance, and every computer system is transparent to you after that unless the  
[01:53:04] other side has an equivalent defense. I don't know what the critical moment  
[01:53:09] is or if there's a single critical moment. But I think there will be either a critical  
[01:53:14] moment, a small number of critical moments, or some critical window where AI confers  
[01:53:22] some large advantage from the perspective of national security, and one country or  
[01:53:30] coalition has reached it before others. I'm not advocating that they just say,  
[01:53:36] "Okay, we're in charge now." That's not how I think about it.  
[01:53:42] The other side is always catching up. There are extreme actions you're not  
[01:53:45] willing to take, and it's not right to take complete control anyway.  
[01:53:52] But at the point that happens, people are going to understand that the world has changed.  
[01:53:58] There's going to be some negotiation, implicit or explicit, about what the  
[01:54:05] post-AI world order looks like. My interest is in making that  
[01:54:14] negotiation be one in which classical liberal democracy has a strong hand.  
[01:54:24] I want to understand what that better means, because you say in the essay,  
[01:54:27] "Autocracy is simply not a form of government that people can accept in the post-powerful AI age."  
[01:54:33] That sounds like you're saying the CCP as an institution cannot exist after we get AGI.  
[01:54:41] That seems like a very strong demand, and it seems to imply a world where the leading lab  
[01:54:47] or the leading country will be able to—and by that language, should get to—determine  
[01:54:54] how the world is governed or what kinds of governments are, and are not, allowed.  
[01:55:02] I believe that paragraph said something like, "You could take it even further and say X."  
[01:55:13] I wasn't necessarily endorsing that view. I was saying,  
[01:55:18] "Here's a weaker thing that I believe. We have to worry a lot about authoritarians and  
[01:55:24] we should try to check them and limit their power. You could take this much further and have a more  
[01:55:30] interventionist view that says authoritarian countries with AI are these self-fulfilling  
[01:55:38] cycles that are very hard to displace, so you just need to get rid of them from the beginning."  
[01:55:43] That has exactly all the problems you say. If you were to make a commitment to  
[01:55:49] overthrowing every authoritarian country, they would take a bunch of actions now  
[01:55:53] that could lead to instability. That just may not be possible.  
[01:56:02] But the point I was making that I do endorse is that it is quite possible that...  
[01:56:09] Today, the view, my view, in most of the Western world is that democracy is a better form of  
[01:56:16] government than authoritarianism. But if a country’s authoritarian,  
[01:56:21] we don’t react the way we’d react if they committed a genocide or something.  
[01:56:27] I guess what I'm saying is I'm a little worried that in the age of AGI, authoritarianism will  
[01:56:32] have a different meaning. It will be a graver thing.  
[01:56:35] We have to decide one way or another how to deal with that.  
[01:56:39] The interventionist view is one possible view. I was exploring such views. It may end up being the  
[01:56:47] right view, or it may end up being too extreme. But I do have hope. One piece of hope I have is  
[01:56:55] that we have seen that as new technologies are invented, forms of government become obsolete.  
[01:57:04] I mentioned this in "Adolescence of Technology", where I said feudalism  
[01:57:10] was basically a form of government, and when we invented industrialization, feudalism was no  
[01:57:18] longer sustainable. It no longer made sense. Why is that hope? Couldn't that imply that  
[01:57:23] democracy is no longer going to be a competitive system?  
[01:57:26] Right, it could go either way. But these problems with  
[01:57:38] authoritarianism get deeper. I wonder if that's an indicator of  
[01:57:44] other problems that authoritarianism will have. In other words, because authoritarianism becomes  
[01:57:52] worse, people are more afraid of it. They work harder to stop it.  
[01:57:59] You have to think in terms of total equilibrium. I just wonder if it will motivate new ways  
[01:58:07] of thinking about how to preserve and protect freedom with the new technology.  
[01:58:13] Even more optimistically, will it lead to a collective reckoning and a more emphatic  
[01:58:22] realization of how important some of the things we take as individual rights are?  
[01:58:27] A more emphatic realization that we really can't give these away.  
[01:58:32] We've seen there's no other way to live that actually works.  
[01:58:39] I am actually hopeful that—it sounds too idealistic, but I believe it could be the  
[01:58:46] case—dictatorships become morally obsolete. They become morally unworkable forms of  
[01:58:52] government and the crisis that that creates is sufficient to force us to find another way.  
[01:59:03] I think there is genuinely a tough question here which I'm not sure how you resolve.  
[01:59:07] We've had to come out one way or another on it through history.  
[01:59:11] With China in the '70s and '80s, we decided that even though it's an  
[01:59:15] authoritarian system, we will engage with it. I think in retrospect that was the right call,  
[01:59:18] because it’s a state authoritarian system but a billion-plus people are much wealthier and  
[01:59:23] better off than they would've otherwise been. It's not clear that it would've stopped being  
[01:59:27] an authoritarian country otherwise. You can just look at North Korea  
[01:59:30] as an example of that. I don't know if it takes  
[01:59:34] that much intelligence to remain an authoritarian country that continues to coalesce its own power.  
[01:59:40] You can imagine a North Korea with an AI that's much worse than everybody else's,  
[01:59:44] but still enough to keep power. In general, it seems like we should just  
[01:59:50] have this attitude that the benefits of AI—in the form of all these empowerments  
[01:59:54] of humanity and health—will be big. Historically, we have decided it's good  
[02:00:00] to spread the benefits of technology widely, even to people whose governments are authoritarian.  
[02:00:06] It is a tough question, how to think about it with AI, but historically we have said, "yes,  
[02:00:10] this is a positive-sum world, and it's still worth diffusing the technology."  
[02:00:15] There are a number of choices we have. Framing this as a government-to-government  
[02:00:20] decision in national security terms is one lens, but there are a lot of other lenses.  
[02:00:27] You could imagine a world where we produce all these cures to diseases.  
[02:00:32] The cures are fine to sell to authoritarian countries, but the data centers just aren't.  
[02:00:38] The chips and the data centers aren't, and the AI industry itself isn't.  
[02:00:44] Another possibility I think folks should think about is this.  
[02:00:49] Could there be developments we can make—either that naturally happen as a result of AI,  
[02:00:55] or that we could make happen by building technology on AI—that  
[02:00:59] create an equilibrium where it becomes infeasible for authoritarian countries  
[02:01:05] to deny their people private use of the benefits of the technology?  
[02:01:12] Are there equilibria where we can give everyone in an authoritarian country their own AI model that  
[02:01:19] defends them from surveillance and there isn't a way for the authoritarian country to crack  
[02:01:24] down on this while retaining power? I don't know. That sounds to me like if that went far enough,  
[02:01:29] it would be a reason why authoritarian countries would disintegrate from the inside.  
[02:01:35] But maybe there's a middle world where there's an equilibrium where, if they want to hold on  
[02:01:39] to power, the authoritarians can't deny individualized access to the technology.  
[02:01:45] But I actually do have a hope for the more radical version.  
[02:01:50] Is it possible that the technology might inherently have properties—or  
[02:01:54] that by building on it in certain ways we could create properties—that have this  
[02:02:01] dissolving effect on authoritarian structures? Now, we hoped originally—think back to the  
[02:02:07] beginning of the Obama administration—that social media and the internet would have  
[02:02:13] that property, and it turns out not to. But what if we could try again with the  
[02:02:20] knowledge of how many things could go wrong, and that this is a different technology?  
[02:02:23] I don't know if it would work, but it's worth a try.  
[02:02:26] It's just very unpredictable. There are first principles reasons why  
[02:02:30] authoritarianism might be privileged. It's all very unpredictable. We just  
[02:02:35] have to recognize the problem and come up with 10 things we can try, try those,  
[02:02:40] and then assess which ones are working, if any. Then try new ones if the old ones aren't working.  
[02:02:46] But I guess that nets out to today, as you say, that we will not sell data centers,  
[02:02:51] or chips, and the ability to make chips to China. So in some sense, you are denying… There would be  
[02:02:58] some benefits to the Chinese economy, Chinese people, et cetera, because we're doing that.  
[02:03:02] Then there'd also be benefits to the American economy because it's a positive-sum world.  
[02:03:06] We could trade. They could have their country's data centers doing one thing.  
[02:03:08] We could have ours doing another. Already, you're saying it's not worth that  
[02:03:14] positive-sum stipend to empower those countries? What I would say is that we are about to be  
[02:03:22] in a world where growth and economic value will come very easily if we're  
[02:03:27] able to build these powerful AI models. What will not come easily is distribution  
[02:03:35] of benefits, distribution of wealth, political freedom.  
[02:03:40] These are the things that are going to be hard to achieve.  
[02:03:43] So when I think about policy, I think that the technology and the market will deliver all the  
[02:03:50] fundamental benefits, this is my fundamental belief, almost faster than we can take them.  
[02:03:55] These questions about distribution and political freedom and rights are the ones that will actually  
[02:04:02] matter and that policy should focus on. Speaking of distribution, as you were  
[02:04:06] mentioning, we have developing countries. In many cases, catch-up growth has been  
[02:04:12] weaker than we would have hoped for. But when catch-up growth does happen,  
[02:04:15] it's fundamentally because they have underutilized labor.  
[02:04:18] We can bring the capital and know-how from developed countries to these countries,  
[02:04:21] and then they can grow quite rapidly. Obviously, in a world where labor is no  
[02:04:26] longer the constraining factor, this mechanism no longer works.  
[02:04:30] So is the hope basically to rely on philanthropy from  
[02:04:33] the people or countries who immediately get wealthy from AI? What is the hope?  
[02:04:38] Philanthropy should obviously play some role, as it has in the past.  
[02:04:44] But I think growth is always better and stronger if we can make it endogenous.  
[02:04:50] What are the relevant industries in an AI-driven world?  
[02:04:58] I said we shouldn't build data centers in China, but there's no reason we shouldn't  
[02:05:00] build data centers in Africa. In fact, I think it'd be  
[02:05:04] great to build data centers in Africa. As long as they're not owned by China,  
[02:05:08] we should build data centers in Africa. I think that's a great thing to do.  
[02:05:16] There's no reason we can't build a pharmaceutical industry that's AI-driven.  
[02:05:22] If AI is accelerating drug discovery, then there will be a bunch of biotech startups.  
[02:05:28] Let's make sure some of those happen in the developing world.  
[02:05:31] Certainly, during the transition—we can talk about the point where humans have no  
[02:05:34] role—humans will still have some role in starting up these companies and supervising the AI models.  
[02:05:41] So let's make sure some of those humans are in the developing world  
[02:05:44] so that fast growth can happen there as well. You guys recently announced that Claude is going  
[02:05:48] to have a constitution that's aligned to a set of values, and not necessarily just to the end user.  
[02:05:53] There's a world I can imagine where if it is aligned to the end user,  
[02:05:56] it preserves the balance of power we have in the world today because everybody gets to have their  
[02:05:59] own AI that's advocating for them. The ratio of bad actors to  
[02:06:03] good actors stays constant. It seems to work out for our world today.  
[02:06:07] Why is it better not to do that, but to have a specific set of values that the  
[02:06:12] AI should carry forward? I'm not sure I'd quite  
[02:06:16] draw the distinction in that way. There may be two relevant distinctions here.  
[02:06:22] I think you're talking about a mix of the two. One is, should we give the model a set of  
[02:06:27] instructions about "do this" versus "don't do this"?  
[02:06:31] The other is, should we give the model a set of principles for how to act?  
[02:06:44] It's kind of purely a practical and empirical thing that we've observed.  
[02:06:48] By teaching the model principles, getting it to learn from principles,  
[02:06:52] its behavior is more consistent, it's easier to cover edge cases, and the model is more  
[02:06:58] likely to do what people want it to do. In other words, if you give it a list of  
[02:07:09] rules—"don't tell people how to hot-wire a car, don't speak in Korean"—it doesn't  
[02:07:10] really understand the rules, and it's hard to generalize from them.  
[02:07:15] It’s just a list of do’s and don’t’s. Whereas if you give it principles—it  
[02:07:21] has some hard guardrails like "Don't make biological weapons" but—overall you're  
[02:07:25] trying to understand what it should be aiming to do, how it should be aiming to operate.  
[02:07:31] So just from a practical perspective, that turns out to be a more effective way to train the model.  
[02:07:35] That's the rules versus principles trade-off. Then there's another thing you're talking about,  
[02:07:42] which is the corrigibility versus intrinsic motivation trade-off.  
[02:07:51] How much should the model be a kind of "skin suit" where it just directly  
[02:08:02] follows the instructions given to it by whoever is giving those instructions,  
[02:08:06] versus how much should the model have an inherent set of values and go off and do things on its own?  
[02:08:14] There I would actually say everything about the model is closer to the direction that  
[02:08:21] it should mostly do what people want. It should mostly follow instructions.  
[02:08:24] We're not trying to build something that goes off and runs the world on its own.  
[02:08:29] We're actually pretty far on the corrigible side. Now, what we do say is there are certain  
[02:08:34] things that the model won't do. I think we say it in various ways in the  
[02:08:40] constitution, that under normal circumstances, if someone asks the model to do a task, it should do  
[02:08:45] that task. That should be the default. But if you've asked it to do something dangerous, or  
[02:08:54] to harm someone else, then the model is unwilling to do that.  
[02:09:01] So I actually think of it as a mostly corrigible model that has some limits,  
[02:09:07] but those limits are based on principles. Then the fundamental question is,  
[02:09:12] how are those principles determined? This is not a special question for Anthropic.  
[02:09:15] This would be a question for any AI company. But because you have been the ones to actually  
[02:09:22] write down the principles, I get to ask you this question.  
[02:09:25] Normally, a constitution is written down, set in stone, and there's a process of  
[02:09:29] updating it and changing it and so forth. In this case, it seems like a document  
[02:09:34] that people at Anthropic write, that can be changed at any time,  
[02:09:37] that guides the behavior of systems that are going to be the basis of a lot of economic activity.  
[02:09:45] How do you think about how those principles should be set?  
[02:09:50] I think there are maybe three sizes of loop here, three ways to iterate.  
[02:09:58] One is we iterate within Anthropic. We train the model, we're not happy with it,  
[02:10:01] and we change the constitution. I think that's good to do.  
[02:10:06] Putting out public updates to the constitution every once in a while  
[02:10:10] is good because people can comment on it. The second level of loop is different companies  
[02:10:16] having different constitutions. I think it’s useful. Anthropic puts out a constitution,  
[02:10:21] Gemini puts out a constitution, and other companies put out a constitution.  
[02:10:28] People can look at them and compare. Outside observers can critique and say,  
[02:10:34] "I like this thing from this constitution and this thing from that constitution."  
[02:10:40] That creates a soft incentive and feedback for all the companies to  
[02:10:45] take the best of each element and improve. Then I think there's a third loop, which is  
[02:10:50] society beyond the AI companies and beyond just those who comment without hard power.  
[02:10:59] There we've done some experiments. A couple years ago, we did an experiment with the Collective  
[02:11:04] Intelligence Project to basically poll people and ask them what should be in our AI constitution.  
[02:11:15] At the time, we incorporated some of those changes.  
[02:11:17] So you could imagine doing something like that with the new approach we've  
[02:11:19] taken to the constitution. It's a little harder because  
[02:11:23] it was an easier approach to take when the constitution was a list of dos and don'ts.  
[02:11:29] At the level of principles, it has to have a certain amount of coherence.  
[02:11:32] But you could still imagine getting views from a wide variety of people.  
[02:11:37] You could also imagine—and this is a crazy idea, but this whole  
[02:11:42] interview is about crazy ideas—systems of representative government having input.  
[02:11:52] I wouldn't do this today because the legislative process is so slow.  
[02:11:55] This is exactly why I think we should be careful about the legislative process and AI regulation.  
[02:12:00] But there's no reason you couldn't, in principle, say, "All AI models have to have a constitution  
[02:12:06] that starts with these things, and then you can append other things after it, but there has to  
[02:12:13] be this special section that takes precedence." I wouldn't do that. That's too rigid and sounds  
[02:12:22] overly prescriptive in a way that I think overly aggressive legislation is.  
[02:12:26] But that is a thing you could try to do. Is there some much less heavy-handed  
[02:12:32] version of that? Maybe. I really like control loop two.  
[02:12:37] Obviously, this is not how constitutions of actual governments do or should work.  
[02:12:42] There's not this vague sense in which the Supreme Court will feel out how people  
[02:12:46] are feeling—what are the vibes—and update the constitution accordingly.  
[02:12:50] With actual governments, there's a more formal, procedural process.  
[02:12:55] But you have a vision of competition between constitutions, which is actually very reminiscent  
[02:13:01] of how some libertarian charter cities people used to talk, about what an archipelago of different  
[02:13:07] kinds of governments would look like. There would be selection among them of  
[02:13:10] who could operate the most effectively and where people would be the happiest.  
[02:13:15] In a sense, you're recreating that vision of a utopia of archipelagos.  
[02:13:23] I think that vision has things to recommend it and things that will go wrong with it.  
[02:13:31] It's an interesting, in some ways compelling, vision, but things will  
[02:13:34] go wrong that you hadn't imagined. So I like loop two as well,  
[02:13:40] but I feel like the whole thing has got to be some mix of loops one, two, and three,  
[02:13:46] and it's a matter of the proportions. I think that's gotta be the answer.  
[02:13:53] When somebody eventually writes the equivalent of The Making of the Atomic Bomb for this era,  
[02:13:58] what is the thing that will be hardest to glean from the historical record that  
[02:14:02] they're most likely to miss? I think a few things. One is,  
[02:14:06] at every moment of this exponential, the extent to which the world outside it didn't understand it.  
[02:14:12] This is a bias that's often present in history. Anything that actually happened looks  
[02:14:17] inevitable in retrospect. When people look back, it will  
[02:14:24] be hard for them to put themselves in the place of people who were actually making a bet on this  
[02:14:32] thing to happen that wasn't inevitable, that we had these arguments like the arguments I make for  
[02:14:38] scaling or that continual learning will be solved. Some of us internally put a high probability  
[02:14:48] on this happening, but there's a world outside us that's not acting on that at all.  
[02:14:58] I think the weirdness of it, unfortunately the insularity of it...  
[02:15:07] If we're one year or two years away from it happening,  
[02:15:10] the average person on the street has no idea. That's one of the things I'm trying to change with  
[02:15:14] the memos, with talking to policymakers. I don’t know but I think  
[02:15:19] that's just a crazy thing. Finally, I would say—and this  
[02:15:27] probably applies to almost all historical moments of crisis—how absolutely fast it was happening,  
[02:15:33] how everything was happening all at once. Decisions that you might think were  
[02:15:39] carefully calculated, well actually you have to make that decision,  
[02:15:42] and then you have to make 30 other decisions on the same day because it's all happening so fast.  
[02:15:47] You don't even know which decisions are going to turn out to be consequential.  
[02:15:52] One of my worries—although it's also an insight into what's happening—is that some  
[02:16:00] very critical decision will be some decision where someone just comes into my office and  
[02:16:05] is like, "Dario, you have two minutes. Should we do thing A or thing B on this?"  
[02:16:14] Someone gives me this random half-page memo and asks, "Should we do A or B?" I'm like, "I  
[02:16:20] don't know. I have to eat lunch. Let's do B." That ends up being the most consequential thing ever.  
[02:16:26] So final question. There aren't tech CEOs who are usually writing 50-page memos every few months.  
[02:16:35] It seems like you have managed to build a role for yourself and a company around  
[02:16:40] you which is compatible with this more intellectual-type role of CEO.  
[02:16:47] I want to understand how you construct that. How does that work? Do you just go away for  
[02:16:53] a couple of weeks and then you tell your company, "This is the memo. Here's what  
[02:16:56] we're doing"? It's also reported that you write a bunch of these internally.  
[02:16:59] For this particular one, I wrote it over winter break.  
[02:17:04] I was having a hard time finding the time to actually write it.  
[02:17:08] But I think about this in a broader way. I think it relates to the culture of the company.  
[02:17:13] I probably spend a third, maybe 40%, of my time making sure the culture of Anthropic is good.  
[02:17:19] As Anthropic has gotten larger, it's gotten harder to get directly involved in the training  
[02:17:26] of the models, the launch of the models, the building of the products. It's 2,500  
[02:17:30] people. I have certain instincts, but it's very difficult to get involved in every single detail.  
[02:17:41] I try as much as possible, but one thing that's very leveraged is making sure Anthropic is a good  
[02:17:46] place to work, people like working there, everyone thinks of themselves as team members, and everyone  
[02:17:51] works together instead of against each other. We've seen as some of the other AI companies  
[02:17:57] have grown—without naming any names—we're starting to see decoherence and people fighting each other.  
[02:18:03] I would argue there was even a lot of that from the beginning, but it's gotten worse.  
[02:18:08] I think we've done an extraordinarily good job, even if not perfect, of holding the  
[02:18:14] company together, making everyone feel the mission, that we're sincere about the mission,  
[02:18:19] and that everyone has faith that everyone else there is working for the right reason.  
[02:18:23] That we're a team, that people aren't trying to get ahead at each other's expense or  
[02:18:28] backstab each other, which again, I think happens a lot at some of the other places.  
[02:18:33] How do you make that the case? It's a lot of things. It's me,  
[02:18:36] it's Daniela, who runs the company day to day, it's the co-founders,  
[02:18:41] it's the other people we hire, it's the environment we try to create.  
[02:18:44] But I think an important thing in the culture is that the other leaders as well, but especially me,  
[02:18:53] have to articulate what the company is about, why it's doing what it's doing,  
[02:18:58] what its strategy is, what its values are, what its mission is, and what it stands for.  
[02:19:06] When you get to 2,500 people, you can't do that person by person.  
[02:19:09] You have to write, or you have to speak to the whole company.  
[02:19:12] This is why I get up in front of the whole company every two weeks and speak for an hour.  
[02:19:18] I wouldn't say I write essays internally. I do two things. One, I write this thing  
[02:19:22] called a DVQ, Dario Vision Quest. I wasn't the one who named it that.  
[02:19:27] That's the name it received, and it's one of these names that I tried to fight because it made it  
[02:19:32] sound like I was going off and smoking peyote or something. But the name just stuck. So I get up  
[02:19:38] in front of the company every two weeks. I have a three or four-page document,  
[02:19:43] and I just talk through three or four different topics about what's going on internally,  
[02:19:49] the models we're producing, the products, the outside industry, the world as a whole  
[02:19:54] as it relates to AI and geopolitically in general. Just some mix of that. I go  
[02:19:59] through very honestly and I say, "This is what I'm thinking, and this is what Anthropic leadership  
[02:20:06] is thinking," and then I answer questions. That direct connection has a lot of value that  
[02:20:13] is hard to achieve when you're passing things down the chain six levels deep.  
[02:20:19] A large fraction of the company comes to attend, either in person or virtually.  
[02:20:27] It really means that you can communicate a lot. The other thing I do is I have a channel in  
[02:20:32] Slack where I just write a bunch of things and comment a lot.  
[02:20:36] Often that's in response to things I'm seeing at the company or questions people ask.  
[02:20:44] We do internal surveys and there are things people are concerned about, and so I'll write them up.  
[02:20:50] I'm just very honest about these things. I just say them very directly.  
[02:20:56] The point is to get a reputation of telling the company the truth about what's happening, to call  
[02:21:01] things what they are, to acknowledge problems, to avoid the sort of corpo speak, the kind of  
[02:21:07] defensive communication that often is necessary in public because the world is very large and full of  
[02:21:14] people who are interpreting things in bad faith. But if you have a company of people who you trust,  
[02:21:21] and we try to hire people that we trust, then you can really just be entirely unfiltered.  
[02:21:31] I think that's an enormous strength of the company.  
[02:21:33] It makes it a better place to work, it makes people more than the sum of their parts,  
[02:21:38] and increases the likelihood that we accomplish the mission because everyone is on the same page  
[02:21:41] about the mission, and everyone is debating and discussing how best to accomplish the mission.  
[02:21:46] Well, in lieu of an external Dario Vision Quest, we have this interview.  
[02:21:50] This interview is a little like that. This has been fun, Dario. Thanks for doing it.  
[02:21:54] Thank you, Dwarkesh.  
