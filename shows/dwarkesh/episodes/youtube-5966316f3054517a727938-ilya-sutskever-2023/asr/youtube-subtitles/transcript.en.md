# Ilya Sutskever (OpenAI Chief Scientist) — Why next-token prediction could surpass human intelligence

[00:00:43] Today I have the pleasure of interviewing Ilya Sutskever,  
[00:00:47] who is the Co-founder and Chief Scientist of OpenAI. Ilya, welcome to The Lunar Society.  
[00:00:52] Thank you, happy to be here. First question and no humility  
[00:00:55] allowed. There are not that many scientists who will make a big breakthrough in their field,  
[00:01:01] there are far fewer scientists who will make multiple independent breakthroughs that define  
[00:01:05] their field throughout their career, what is the difference? What distinguishes you  
[00:01:10] from other researchers? Why have you been able to make multiple breakthroughs in your field?  
[00:01:13] Thank you for the kind words. It's hard to answer that question. I try really hard,  
[00:01:21] I give it everything I've got and that has worked so far. I think that's all there is to it.  
[00:01:30] Got it. What's the explanation for why there aren't more illicit uses of GPT?  
[00:01:35] Why aren't more foreign governments using it to spread propaganda or scam grandmothers?  
[00:01:42] Maybe they haven't really gotten to do it a lot. But it also wouldn't surprise me if some of it  
[00:01:49] was going on right now. I can certainly imagine they would be taking some of the open source  
[00:01:52] models and trying to use them for that purpose. For sure I would expect this to be something  
[00:02:00] they'd be interested in the future. It's technically possible they just  
[00:02:03] haven't thought about it enough? Or haven't done it at scale using  
[00:02:06] their technology. Or maybe it is happening, which is annoying.  
[00:02:09] Would you be able to track it if it was happening?  
[00:02:10] I think large-scale tracking is possible, yes. It requires special operations but it's possible.  
[00:02:18] Now there's some window in which AI is very economically valuable, let’s say on  
[00:02:23] the scale of airplanes, but we haven't reached AGI yet. How big is that window?  
[00:02:29] It's hard to give a precise answer and it’s definitely going to be a  
[00:02:32] good multi-year window. It's also a question of definition. Because AI, before it becomes AGI,  
[00:02:41] is going to be increasingly more valuable year after year in an exponential way.  
[00:02:51] In hindsight, it may feel like there was only one year or two years because those two years  
[00:02:55] were larger than the previous years. But I would say that already, last year, there has been a fair  
[00:03:03] amount of economic value produced by AI. Next year is going to be larger and larger after that. So  
[00:03:10] I think it's going to be a good multi-year chunk of time where that’s going to be true,  
[00:03:16] from now till AGI pretty much. Okay. Because I'm curious if there's  
[00:03:21] a startup that's using your model, at some point if you have AGI there's only one business in the  
[00:03:25] world, it's OpenAI. How much window does any business have where they're actually  
[00:03:30] producing something that AGI can’t produce? It's the same question as asking how long until  
[00:03:36] AGI. It's a hard question to answer. I hesitate to give you a number. Also because there is this  
[00:03:43] effect where optimistic people who are working on the technology tend to underestimate the time  
[00:03:50] it takes to get there. But the way I ground myself is by thinking about the self-driving  
[00:03:55] car. In particular, there is an analogy where if you look at the size of a Tesla,  
[00:04:00] and if you look at its self-driving behavior, it looks like it does everything. But it's also clear  
[00:04:09] that there is still a long way to go in terms of reliability. And we might be in a similar place  
[00:04:14] with respect to our models where it also looks like we can do everything, and at the same time,  
[00:04:20] we will need to do some more work until we really iron out all the issues and make it really good  
[00:04:26] and really reliable and robust and well behaved. By 2030, what percent of GDP is AI?  
[00:04:31] Oh gosh, very hard to answer that question. Give me an over-under.  
[00:04:36] The problem is that my error bars are in log scale. I could imagine a huge percentage,  
[00:04:41] I could imagine a really disappointing small percentage at the same time.  
[00:04:44] Okay, so let's take the counterfactual where it is a small percentage. Let's say it's 2030 and not  
[00:04:49] that much economic value has been created by these LLMs. As unlikely as you think this might be,  
[00:04:53] what would be your best explanation right now of why something like this might happen?  
[00:05:00] I really don't think that's a likely possibility, that's the preface to the comment. But  
[00:05:08] if I were to take the premise of your question, why were things disappointing in terms of  
[00:05:13] real-world impact? My answer would be reliability. If it somehow ends up being the case that  
[00:05:22] you really want them to be reliable and they ended up not being reliable, or if reliability  
[00:05:26] turned out to be harder than we expect. I really don't think that will be the case.  
[00:05:31] But if I had to pick one and you were telling me — hey, why didn't things work out? It would  
[00:05:37] be reliability. That you still have to look over the answers and double-check everything.  
[00:05:42] That just really puts a damper on the economic value that can be produced by those systems.  
[00:05:47] Got it. They will be technologically mature, it’s just the question of  
[00:05:49] whether they'll be reliable enough. Well, in some sense, not reliable means  
[00:05:53] not technologically mature. Yeah, fair enough.  
[00:05:57] What's after generative models? Before, you were working on reinforcement learning. Is this  
[00:06:02] basically it? Is this the paradigm that gets us to AGI? Or is there something after this?  
[00:06:05] I think this paradigm is gonna go really, really far and I would not underestimate it. It's quite  
[00:06:10] likely that this exact paradigm is not quite going to be the AGI form factor. I hesitate  
[00:06:17] to say precisely what the next paradigm will be but it will probably involve integration of  
[00:06:24] all the different ideas that came in the past. Is there some specific one you're referring to?  
[00:06:33] It's hard to be specific. So you could argue that  
[00:06:35] next-token prediction can only help us match human performance and maybe not surpass it?  
[00:06:40] What would it take to surpass human performance? I challenge the claim that next-token prediction  
[00:06:45] cannot surpass human performance. On the surface, it looks like it cannot. It looks like if you  
[00:06:53] just learn to imitate, to predict what people do, it means that you can only copy people.  
[00:07:00] But here is a counter argument for why it might not be quite so. If your base neural net is smart  
[00:07:07] enough, you just ask it — What would a person with great insight, wisdom, and capability do?  
[00:07:15] Maybe such a person doesn't exist, but there's a pretty good chance that the neural net will  
[00:07:19] be able to extrapolate how such a person would behave. Do you see what I mean?  
[00:07:25] Yes, although where would it get that sort of insight  
[00:07:27] about what that person would do? If not from… From the data of regular people. Because if you  
[00:07:32] think about it, what does it mean to predict the next token well enough? It's actually a  
[00:07:38] much deeper question than it seems. Predicting the next token well means that you understand  
[00:07:45] the underlying reality that led to the creation of that token.  
[00:07:52] It's not statistics. Like it is statistics but what is statistics?  
[00:07:57] In order to understand those statistics to compress them, you need to understand what  
[00:08:03] is it about the world that creates this set of statistics? And so then you say — Well, I have all  
[00:08:08] those people. What is it about people that creates their behaviors? Well they have thoughts and their  
[00:08:14] feelings, and they have ideas, and they do things in certain ways. All of those could be deduced  
[00:08:20] from next-token prediction. And I'd argue that this should make it possible, not indefinitely but  
[00:08:28] to a pretty decent degree to say — Well, can you guess what you'd do if you took a person with this  
[00:08:33] characteristic and that characteristic? Like such a person doesn't exist but because you're so good  
[00:08:39] at predicting the next token, you should still be able to guess what that person who would do.  
[00:08:42] This hypothetical, imaginary person with far greater mental ability than the rest of us.  
[00:08:51] When we're doing reinforcement learning on these models, how long before most of the  
[00:08:54] data for the reinforcement learning is coming from AI and not humans?  
[00:08:59] Already most of the default enforcement learning is coming from AIs.  
[00:09:05] The humans are being used to train the reward function. But then the reward function  
[00:09:12] and its interaction with the model is automatic and all the data that's generated during the  
[00:09:16] process of reinforcement learning is created by AI. If you look at the current technique/paradigm,  
[00:09:25] which is getting some significant attention because of chatGPT, Reinforcement Learning  
[00:09:30] from Human Feedback (RLHF). The human feedback has been used to train the reward function  
[00:09:36] and then the reward function is being used to create the data which trains the model.  
[00:09:40] Got it. And is there any hope of just removing a human from the loop and have  
[00:09:43] it improve itself in some sort of AlphaGo way? Yeah, definitely. The thing you really want is for  
[00:09:56] the human teachers that teach the AI to collaborate with an AI. You might want to  
[00:10:06] think of it as being in a world where the human teachers do 1% of the work and the AI does 99% of  
[00:10:11] the work. You don't want it to be 100% AI. But you do want it to be a human-machine collaboration,  
[00:10:17] which teaches the next machine. I've had a chance to play around  
[00:10:20] these models and they seem bad at multi-step reasoning. While they have been getting better,  
[00:10:25] what does it take to really surpass that barrier? I think dedicated training will get us there.  
[00:10:31] More and more improvements to the base models will get us there. But  
[00:10:38] fundamentally I also don't feel like they're that bad at multi-step reasoning. I actually think that  
[00:10:42] they are bad at mental multistep reasoning when they are not allowed to think out loud.  
[00:10:46] But when they are allowed to think out loud, they're quite good. And I expect  
[00:10:50] this to improve significantly, both with better models and with special training.  
[00:10:56] Are you running out of reasoning tokens on the internet? Are there enough of them?  
[00:11:02] So for context on this question, there are claims that at some point we will run out of tokens,  
[00:11:08] in general, to train those models. And yeah, I think this will happen one day and by the time  
[00:11:13] that happens, we need to have other ways of training models, other ways of productively  
[00:11:18] improving their capabilities and sharpening their behavior, making sure they're doing exactly,  
[00:11:23] precisely what you want, without more data. You haven't run out of data yet? There's more?  
[00:11:29] Yeah, I would say the data situation is still quite good. There's still lots to  
[00:11:33] go. But at some point the data will run out. What is the most valuable source of data? Is it  
[00:11:40] Reddit, Twitter, books? Where would you train many other tokens of other varieties for?  
[00:11:46] Generally speaking, you'd like tokens which are speaking about smarter things,  
[00:11:50] tokens which are more interesting.  
[00:11:55] All the sources which you mentioned are valuable. So maybe not Twitter. But do we need to go  
[00:12:01] multimodal to get more tokens? Or do we still have enough text tokens left?  
[00:12:04] I think that you can still go very far in text only but going multimodal  
[00:12:08] seems like a very fruitful direction. If you're comfortable talking about this,  
[00:12:11] where is the place where we haven't scraped the tokens yet?  
[00:12:16] Obviously I can't answer that question for us but I'm sure that for everyone  
[00:12:21] there is a different answer to that question. How many orders of magnitude improvement can  
[00:12:24] we get, not from scale or not from data, but just from algorithmic improvements?  
[00:12:30] Hard to answer but I'm sure there is some. Is some a lot or some a little?  
[00:12:35] There’s only one way to find out. Okay. Let me get your quickfire opinions  
[00:12:39] about these different research directions. Retrieval transformers. So it’s just somehow  
[00:12:43] storing the data outside of the model itself and retrieving it somehow.  
[00:12:47] Seems promising. But do you see that as a path forward?  
[00:12:51] It seems promising. Robotics. Was it the right  
[00:12:54] step for Open AI to leave that behind? Yeah, it was. Back then it really wasn't  
[00:13:01] possible to continue working in robotics because there was so little data.  
[00:13:06] Back then if you wanted to work on robotics, you needed to become a robotics company. You needed  
[00:13:11] to have a really giant group of people working on building robots and maintaining them. And  
[00:13:20] even then, if you’re gonna have 100 robots, it's a giant operation already,  
[00:13:24] but you're not going to get that much data. So in a world where most of the progress comes from the  
[00:13:31] combination of compute and data, there was no path to data on robotics. So back in the day,  
[00:13:46] when we made a decision to stop working in robotics, there was no path forward.  
[00:13:51] Is there one now? I'd say that now it is possible  
[00:13:56] to create a path forward. But one needs to really commit to the task of robotics. You really need  
[00:14:02] to say — I'm going to build many thousands, tens of thousands, hundreds of thousands of robots,  
[00:14:10] and somehow collect data from them and find a gradual path where the robots are doing something  
[00:14:15] slightly more useful. And then the data that is obtained and used to train the models, and they do  
[00:14:22] something that's slightly more useful. You could imagine it's this gradual path of improvement,  
[00:14:25] where you build more robots, they do more things, you collect more data, and so on. But  
[00:14:29] you really need to be committed to this path. If you say, I want to make robotics happen,  
[00:14:33] that's what you need to do. I believe that there are companies who are doing exactly  
[00:14:39] that. But you need to really love robots and need to be really willing to solve all  
[00:14:45] the physical and logistical problems of dealing with them. It's not the same as software at all.  
[00:14:51] I think one could make progress in robotics today, with enough motivation.  
[00:14:56] What ideas are you excited to try but you can't because they don't work well on current hardware?  
[00:15:01] I don't think current hardware is a limitation. It's just not the case.  
[00:15:05] Got it. But anything you want to try you can just spin it up?  
[00:15:09] Of course. You might wish that current hardware was cheaper or maybe it  
[00:15:18] would be better if it had higher memory processing bandwidth let’s say.  
[00:15:23] But by and large hardware is just not an issue. Let's talk about alignment. Do you think we'll  
[00:15:30] ever have a mathematical definition of alignment? A mathematical definition is unlikely. Rather than  
[00:15:42] achieving one mathematical definition, I think we will achieve multiple definitions that look at  
[00:15:48] alignment from different aspects. And that this is how we will get the assurance that we want.  
[00:15:55] By which I mean you can look at the behavior in various tests, congruence, in various adversarial  
[00:16:03] stress situations, you can look at how the neural net operates from the inside. You have to look at  
[00:16:09] several of these factors at the same time. And how sure do you have to be before you  
[00:16:14] release a model in the wild? 100%? 95%? Depends on how capable the model is.  
[00:16:18] The more capable the model, the more confident we need to be.  
[00:16:24] Alright, so let's say it's something that's almost AGI. Where is AGI?  
[00:16:27] Depends on what your AGI can do. Keep in mind that AGI is an ambiguous term.  
[00:16:32] Your average college undergrad is an AGI, right? There's significant ambiguity in terms of what is  
[00:16:42] meant by AGI. Depending on where you put this mark you need to be more or less confident.  
[00:16:49] You mentioned a few of the paths toward alignment earlier, what is the one you  
[00:16:52] think is most promising at this point? I think that it will be a combination.  
[00:16:56] I really think that you will not want to have just one approach. People want to have  
[00:17:03] a combination of approaches. Where you spend a lot of compute adversarially to find any  
[00:17:09] mismatch between the behavior you want it to teach and the behavior that it exhibits.We  
[00:17:14] look into the neural net using another neural net to understand how it operates on the inside. All  
[00:17:21] of them will be necessary. Every approach like this reduces the probability of misalignment.  
[00:17:28] And you also want to be in a world where your degree of alignment keeps increasing  
[00:17:35] faster than the capability of the models. Do you think that the approaches we’ve taken  
[00:17:38] to understand the model today will be applicable to the actual super-powerful models? Or how  
[00:17:38] applicable will they be? Is it the same kind of thing that will work on them as well or?  
[00:17:38] x It's not guaranteed. I would say  
[00:17:39] that right now, our understanding of our models is still quite rudimentary. We’ve made some progress  
[00:17:44] but much more progress is possible. And so I would expect that ultimately, the thing that will really  
[00:17:49] succeed is when we will have a small neural net that is well understood that’s been given the  
[00:17:55] task to study the behavior of a large neural net that is not understood, to verify.  
[00:17:59] By what point is most of the AI research being done by AI?  
[00:18:03] Today when you use Copilot, how do you divide it up? So I expect at some point you ask your  
[00:18:13] descendant of ChatGPT, you say — Hey, I'm thinking about this and this. Can  
[00:18:16] you suggest fruitful ideas I should try? And you would actually get fruitful ideas. I don't  
[00:18:22] think that's gonna make it possible for you to solve problems you couldn't solve before.  
[00:18:24] Got it. But it's somehow just telling the humans giving them ideas faster or something. It's  
[00:18:29] not itself interacting with the research? That was one example. You could slice it in  
[00:18:33] a variety of ways. But the bottleneck there is good ideas, good insights and that's something  
[00:18:38] that the neural nets could help us with. If you're designing a billion-dollar prize  
[00:18:42] for some sort of alignment research result or product, what is the concrete criterion you  
[00:18:47] would set for that billion-dollar prize? Is there something that makes sense for such a prize?  
[00:18:50] It's funny that you asked, I was actually thinking about this exact question. I haven't  
[00:18:55] come up with the exact criterion yet. Maybe a prize where we could say that two years later,  
[00:19:06] or three years or five years later, we look back and say like that was the main result.  
[00:19:11] So rather than say that there is a prize committee that decides right away, you wait  
[00:19:15] for five years and then award it retroactively. But there's no concrete thing we can identify  
[00:19:20] as you solve this particular problem and you’ve made a lot of progress?  
[00:19:25] A lot of progress, yes. I wouldn't say that this would be the full thing.  
[00:19:30] Do you think end-to-end training is the right architecture for bigger  
[00:19:35] and bigger models? Or do we need better ways of just connecting things together?  
[00:19:40] End-to-end training is very promising. Connecting things together is very promising.  
[00:19:43] Everything is promising. So Open AI is projecting revenues  
[00:19:47] of a billion dollars in 2024. That might very well be correct but I'm just curious, when you're  
[00:19:52] talking about a new general-purpose technology, how do you estimate how big a windfall it'll be?  
[00:19:58] Why that particular number? We've had a product  
[00:20:07] for quite a while now, back from the GPT-3 days, from two years ago through the API and we've seen  
[00:20:12] how it grew. We've seen how the response to DALL-E has grown as well and you see how the  
[00:20:17] response to ChatGPT is, and all of this gives us information that allows us to make relatively  
[00:20:23] sensible extrapolations of anything. Maybe that would be one answer. You need to have data,  
[00:20:29] you can’t come up with those things out of thin air because otherwise, your error bars  
[00:20:36] are going to be like 100x in each direction. But most exponentials don't stay exponential  
[00:20:41] especially when they get into bigger and bigger quantities, right? So how  
[00:20:45] do you determine in this case? Would you bet against AI?  
[00:20:51] Not after talking with you. Let's talk about what a post-AGI future looks like. I'm guessing  
[00:20:58] you're working 80-hour weeks towards this grand goal that you're really obsessed with. Are you  
[00:21:02] going to be satisfied in a world where you're basically living in an AI retirement home?  
[00:21:08] What are you personally doing after AGI comes? The question of what I'll be doing or what people  
[00:21:15] will be doing after AGI comes is a very tricky question. Where will people find meaning? But  
[00:21:21] I think that that's something that AI could help us with. One thing I imagine is that  
[00:21:29] we will be able to become more enlightened because we interact with an AGI which will help us  
[00:21:35] see the world more correctly, and become better on the inside as a result of interacting. Imagine  
[00:21:40] talking to the best meditation teacher in history, that will be a helpful thing. But  
[00:21:46] I also think that because the world will change a lot, it will be very hard for people to understand  
[00:21:52] what is happening precisely and how to really contribute. One thing that I think  
[00:21:59] some people will choose to do is to become part AI. In order to really expand their minds and  
[00:22:05] understanding and to really be able to solve the hardest problems that society will face then.  
[00:22:10] Are you going to become part AI? It is very tempting.  
[00:22:14] Do you think there'll be physically embodied humans in the year 3000?  
[00:22:19] 3000? How do I know what’s gonna happen in 3000? Like what does it look like? Are there still  
[00:22:23] humans walking around on Earth? Or have you guys thought concretely about what  
[00:22:26] you actually want this world to look like? Let me describe to you what I think is not quite  
[00:22:33] right about the question. It implies we get to decide how we want the world to look like.  
[00:22:40] I don't think that picture is correct. Change is the only constant. And so of course, even  
[00:22:45] after AGI is built, it doesn't mean that the world will be static. The world will continue to change,  
[00:22:50] the world will continue to evolve. And it will go through all kinds of transformations. I  
[00:22:57] don't think anyone has any idea of how the world will look like in 3000. But  
[00:23:03] I do hope that there will be a lot of descendants of human beings who will live happy, fulfilled  
[00:23:08] lives where they're free to do as they see fit. Or they are the ones who are solving their own  
[00:23:14] problems. One world which I would find very unexciting is one where we build this powerful  
[00:23:21] tool, and then the government said — Okay, so the AGI said that society should be run in such  
[00:23:27] a way and now we should run society in such a way. I'd much rather have a world where people  
[00:23:32] are still free to make their own mistakes and suffer their consequences and gradually evolve  
[00:23:38] morally and progress forward on their own, with the AGI providing more like a base safety net.  
[00:23:46] How much time do you spend thinking about these kinds of things versus just doing the research?  
[00:23:50] I do think about those things a fair bit. They are very interesting questions.  
[00:23:55] The capabilities we have today, in what ways have they surpassed where we expected them to  
[00:23:59] be in 2015? And in what ways are they still not where you'd expected them to be by this point?  
[00:24:05] In fairness, it's sort of what I expected in 2015. In 2015, my thinking was a lot more — I just don't  
[00:24:13] want to bet against deep learning. I want to make the biggest possible bet on deep learning. I don't  
[00:24:17] know how, but it will figure it out. But is there any specific way in which  
[00:24:21] it's been more than you expected or less than you expected? Like some concrete prediction  
[00:24:26] out of 2015 that's been bounced? Unfortunately, I don't remember  
[00:24:31] concrete predictions I made in 2015. But I definitely think that overall,  
[00:24:36] in 2015, I just wanted to move to make the biggest bet possible on deep learning, but  
[00:24:44] I didn't know exactly. I didn't have a specific idea of how far things will go in seven years.  
[00:24:49] Well, no in 2015, I did have all these best with people in 2016, maybe 2017, that things will go  
[00:24:55] really far. But specifics. So it's like, it's both, it's both the case that it surprised me  
[00:25:02] and I was making these aggressive predictions. But maybe I believed them only 50% on the inside.  
[00:25:10] What do you believe now that even most people at OpenAI would find far fetched?  
[00:25:16] Because we communicate a lot at OpenAI people have a pretty good sense of what I think and  
[00:25:21] we've really reached the point at OpenAI where we see eye to eye on all these questions.  
[00:25:25] Google has its custom TPU hardware, it has all this data from all its users, Gmail,  
[00:25:31] and so on. Does it give them an advantage in terms of training  
[00:25:34] bigger models and better models than you?  
[00:25:38] At first, when the TPU came out I was really impressed and I thought — wow,  
[00:25:41] this is amazing. But that's because I didn't quite understand hardware back then.  
[00:25:45] What really turned out to be the case is that TPUs and GPUs are almost the same thing.  
[00:25:52] They are very, very similar. The GPU chip is a little bit bigger,  
[00:25:59] the TPU chip is a little bit smaller, maybe a little bit cheaper. But then they make more GPUs  
[00:26:03] and TPUs so the GPUs might be cheaper after all. But fundamentally, you have a big processor,  
[00:26:10] and you have a lot of memory and there is a bottleneck between those two. And the problem  
[00:26:16] that both the TPU and the GPU are trying to solve is that the amount of time it takes you  
[00:26:21] to move one floating point from the memory to the processor, you can do several hundred floating  
[00:26:26] point operations on the processor, which means that you have to do some kind of batch processing.  
[00:26:30] And in this sense, both of these architectures are the same. So I really feel like in some sense,  
[00:26:37] the only thing that matters about hardware is cost per flop and overall systems cost.  
[00:26:44] There isn't that much difference? Actually, I don't know. I don't know  
[00:26:47] what the TPU costs are but I would suspect that if anything, TPUs are probably more  
[00:26:54] expensive because there are less of them. When you are doing your work, how much of the time  
[00:26:58] is spent configuring the right initializations? Making sure the training run goes well and getting  
[00:27:04] the right hyperparameters, and how much is it just coming up with whole new ideas?  
[00:27:07] I would say it's a combination. Coming up with whole new ideas is a modest part  
[00:27:16] of the work. Certainly coming up with new ideas is important but even more important  
[00:27:20] is to understand the results, to understand the existing ideas, to understand what's going on.  
[00:27:26] A neural net is a very complicated system, right? And you ran it, and you get some behavior,  
[00:27:31] which is hard to understand. What's going on? Understanding the results, figuring out  
[00:27:36] what next experiment to run, a lot of the time is spent on that. Understanding what could be wrong,  
[00:27:41] what could have caused the neural net to produce a result which was not expected.  
[00:27:48] I'd say a lot of time is spent coming up with new ideas as well. I don't like this  
[00:27:57] framing as much. It's not that it's false but the main activity is actually understanding.  
[00:28:03] What do you see as the difference between the two?  
[00:28:05] At least in my mind, when you say come up with new ideas, I'm like — Oh, what happens  
[00:28:09] if it did such and such? Whereas understanding it's more like — What is this whole thing? What  
[00:28:15] are the real underlying phenomena that are going on? What are the underlying effects?  
[00:28:22] Why are we doing things this way and not another way? And of course,  
[00:28:24] this is very adjacent to what can be described as coming up with ideas. But the understanding  
[00:28:30] part is where the real action takes place. Does that describe your entire career? If you  
[00:28:34] think back on something like ImageNet, was that more new idea or was that more understanding?  
[00:28:38] Well, that was definitely understanding. It was a new understanding of very old things.  
[00:28:44] What has the experience of training on Azure been like?  
[00:28:49] Fantastic. Microsoft has been a very, very good partner for us. They've really  
[00:28:56] helped take Azure and bring it to a point where it's really good for ML  
[00:29:04] and we’re super happy with it. How vulnerable is the whole AI  
[00:29:08] ecosystem to something that might happen in Taiwan? So let's say there's a tsunami in Taiwan  
[00:29:13] or something, what happens to AI in general? It's definitely going to be a significant setback.  
[00:29:24] No one will be able to get more compute for a few years. But I expect compute will spring up. For  
[00:29:29] example, I believe that Intel has fabs just like a few generations ago. So that means that if Intel  
[00:29:35] wanted to they could produce something GPU-like from four years ago. But yeah, it's not the best,  
[00:29:41] I'm actually not sure if my statement about Intel is correct, but I do know that there are fabs  
[00:29:49] outside of Taiwan, they're just not as good. But you can still use them and still go very far with  
[00:29:54] them. It's just cost, it’s just a setback. Would inference get cost prohibitive as  
[00:29:59] these models get bigger and bigger? I have a different way of looking at  
[00:30:02] this question. It's not that inference will become cost prohibitive. Inference of better  
[00:30:07] models will indeed become more expensive. But is it prohibitive? That depends on how useful it  
[00:30:15] is. If it is more useful than it is expensive then it is not prohibitive.  
[00:30:19] To give you an analogy, suppose you want to talk to a lawyer. You have some case  
[00:30:23] or need some advice or something, you're perfectly happy to spend $400 an hour.  
[00:30:29] Right? So if your neural net could give you really reliable legal advice,  
[00:30:33] you'd say — I'm happy to spend $400 for that advice. And suddenly inference becomes very much  
[00:30:39] non-prohibitive. The question is, can a neural net produce an answer good enough at this cost?  
[00:30:48] Yes. And you will just have price discrimination in different models?  
[00:30:53] It's already the case today. On our product, the API serves multiple neural nets of different sizes  
[00:31:02] and different customers use different neural nets of different sizes depending on their use case.  
[00:31:07] If someone can take a small model and fine-tune it and get something that's satisfactory for them,  
[00:31:12] they'll use that. But if someone wants to do something more complicated and more interesting,  
[00:31:16] they’ll use the biggest model. How do you prevent these models from  
[00:31:19] just becoming commodities where these different companies just bid each other's prices down  
[00:31:23] until it's basically the cost of the GPU run? Yeah, there's without question a force that's  
[00:31:28] trying to create that. And the answer is you got to keep on making progress. You got to keep  
[00:31:31] improving the models, you gotta keep on coming up with new ideas and making our models better  
[00:31:36] and more reliable, more trustworthy, so you can trust their answers. All those things.  
[00:31:43] Yeah. But let's say it's 2025 and somebody is offering the model from 2024 at cost.  
[00:31:48] And it's still pretty good. Why would people use a new one from 2025 if the  
[00:31:53] one from just a year older is even better? There are several answers there. For some  
[00:31:58] use cases that may be true. There will be a new model for 2025, which will be driving the more  
[00:32:03] interesting use cases. There is also going to be a question of inference cost. If you can do  
[00:32:07] research to serve the same model at less cost. The same model will cost different amounts to serve  
[00:32:18] for different companies. I can also imagine some degree of specialization where some companies may  
[00:32:22] try to specialize in some area and be stronger compared to other companies. And to me that may  
[00:32:30] be a response to commoditization to some degree. Over time do the research directions of these  
[00:32:36] different companies converge or diverge? Are they doing similar and similar things over time? Or are  
[00:32:41] they branching off into different areas? I’d say in the near term, it looks  
[00:32:46] like there is convergence. I expect there's going to be a convergence-divergence-convergence  
[00:32:51] behavior, where there is a lot of convergence on the near term work, there's going to be some  
[00:32:57] divergence on the longer term work. But then once the longer term work starts to fruit,  
[00:33:01] there will be convergence again, Got it. When one of them finds the  
[00:33:05] most promising area, everybody just… That's right. There is obviously less  
[00:33:10] publishing now so it will take longer before this promising direction gets rediscovered. But  
[00:33:14] that's how I would imagine the thing is going to be. Convergence, divergence, convergence.  
[00:33:18] Yeah. We talked about this a little bit at the beginning. But as foreign governments  
[00:33:22] learn about how capable these models are, are you worried about spies or some sort of  
[00:33:28] attack to get your weights or somehow abuse these models and learn about them?  
[00:33:34] Yeah, you absolutely can't discount that. Something that we try to guard against to the  
[00:33:45] best of our ability, but it's going to be a problem for everyone who's building this.  
[00:33:48] How do you prevent your weights from leaking? You have really good security people.  
[00:33:55] How many people have the ability to SSH into the machine with the weights?  
[00:34:04] The security people have done a really good job so I'm really not  
[00:34:09] worried about the weights being leaked. What kinds of emergent properties are you  
[00:34:13] expecting from these models at this scale? Is there something that just comes about de novo?  
[00:34:19] I'm sure really new surprising properties will come up, I would not be surprised. The thing which  
[00:34:24] I'm really excited about, the things which I’d like to see is — reliability and controllability.  
[00:34:28] I think that this will be a very, very important class of emergent properties. If you have  
[00:34:34] reliability and controllability that helps you solve a lot of problems. Reliability means you can  
[00:34:39] trust the model's output, controllability means you can control it. And we'll see but it will be  
[00:34:45] very cool if those emergent properties did exist. Is there some way you can predict that in advance?  
[00:34:50] What will happen in this parameter count, what will happen in that parameter count?  
[00:34:52] I think it's possible to make some predictions about specific capabilities though it's definitely  
[00:34:57] not simple and you can’t do it in a super fine-grained way, at least today. But getting  
[00:35:02] better at that is really important. And anyone who is interested and who has research ideas on how to  
[00:35:09] do that, that can be a valuable contribution. How seriously do you take these scaling laws?  
[00:35:14] There's a paper that says — You need this many orders of magnitude more to get all  
[00:35:19] the reasoning out? Do you take that seriously or do you think it breaks down at some point?  
[00:35:23] The thing is that the scaling law tells you what happens to your log of your next word prediction  
[00:35:31] accuracy, right? There is a whole separate challenge of linking next-word prediction accuracy  
[00:35:37] to reasoning capability. I do believe that there is a link but this link is complicated.  
[00:35:45] And we may find that there are other things that can give us more reasoning per unit effort.  
[00:35:54] You mentioned reasoning tokens, I think they can be helpful.  
[00:36:00] There can probably be some things that help. Are you considering just hiring humans to  
[00:36:07] generate tokens for you? Or is it all going to come from stuff that already exists out there?  
[00:36:11] I think that relying on people to teach our models to do things, especially to make sure that they  
[00:36:18] are well-behaved and they don't produce false things is an extremely sensible thing to do.  
[00:36:23] Isn't it odd that we have the data we needed exactly at the same time as we  
[00:36:27] have the transformer at the exact same time that we have these GPUs? Like is it  
[00:36:32] odd to you that all these things happened at the same time or do you not see it that way?  
[00:36:35] It is definitely an interesting situation that is the case. I will say that  
[00:36:42] it is odd and it is less odd on some level. Here's why it's less odd — what is the driving  
[00:36:48] force behind the fact that the data exists, that the GPUs exist, and that the transformers exist?  
[00:36:57] The data exists because computers became better and cheaper, we've got smaller and  
[00:37:00] smaller transistors. And suddenly, at some point, it became economical for  
[00:37:04] every person to have a personal computer. Once everyone has a personal computer,  
[00:37:07] you really want to connect them to the network, you get the internet. Once you have the internet,  
[00:37:11] you suddenly have data appearing in great quantities. The GPUs were improving concurrently  
[00:37:16] because you have smaller and smaller transistors and you're looking for things to do with them.  
[00:37:20] Gaming turned out to be a thing that you could do. And then at some point, Nvidia said — the  
[00:37:26] gaming GPU, I might turn it into a general purpose GPU computer, maybe someone will find  
[00:37:34] it useful. It turns out it's good for neural nets. It could have been the case that maybe  
[00:37:41] the GPU would have arrived five years later, ten years later. Let's suppose gaming wasn't  
[00:37:47] the thing. It's kind of hard to imagine, what does it mean if gaming isn't a thing?  
[00:37:52] But maybe there was a counterfactual world where GPUs arrived five years after the data  
[00:37:57] or five years before the data, in which case maybe things wouldn’t have been as  
[00:38:04] ready to go as they are now. But that's the picture which I imagine. All this progress in  
[00:38:09] all these dimensions is very intertwined. It's not a coincidence. You don't get to pick and  
[00:38:16] choose in which dimensions things improve. How inevitable is this kind of progress?  
[00:38:23] Let's say you and Geoffrey Hinton and a few other pioneers were never born. Does  
[00:38:28] the deep learning revolution happen around the same time? How much is it delayed?  
[00:38:32] Maybe there would have been some delay. Maybe like a year delayed?  
[00:38:34] Really? That’s it? It's really hard to  
[00:38:37] tell. I hesitate to give a longer answer because — GPUs will keep on improving.  
[00:38:45] I cannot see how someone would not have discovered it. Because here's the other thing. Let's suppose  
[00:38:51] no one has done it, computers keep getting faster and better. It becomes easier and easier to train  
[00:38:56] these neural nets because you have bigger GPUs, so it takes less engineering effort to train  
[00:39:02] one. You don't need to optimize your code as much. When the ImageNet data set came out,  
[00:39:06] it was huge and it was very, very difficult to use. Now imagine you wait for a few years,  
[00:39:11] and it becomes very easy to download and people can just tinker. A modest  
[00:39:18] number of years maximum would be my guess. I hesitate to give a lot longer answer though.  
[00:39:26] You can’t re-run the world you don’t know. Let's go back to alignment for a second. As  
[00:39:33] somebody who deeply understands these models, what is your intuition of how hard alignment will be?  
[00:39:39] At the current level of capabilities, we have a pretty good set of ideas for how to align them.  
[00:39:45] But I would not underestimate the difficulty of alignment of models that are actually  
[00:39:50] smarter than us, of models that are capable of misrepresenting their intentions. It's something  
[00:39:59] to think about a lot and do research. Oftentimes academic researchers ask me what’s the best place  
[00:40:07] where they can contribute. And alignment research is one place where academic researchers can make  
[00:40:13] very meaningful contributions. Other than that, do you think academia  
[00:40:17] will come up with important insights about actual capabilities or is that  
[00:40:19] going to be just the companies at this point? The companies will realize the capabilities.  
[00:40:23] It's very possible for academic research to come up with those insights. It doesn't seem  
[00:40:29] to happen that much for some reason but I don't think there's anything  
[00:40:34] fundamental about academia. It's not like academia can't. Maybe they're just not  
[00:40:40] thinking about the right problems or something because maybe it's just easier to see what needs  
[00:40:46] to be done inside these companies. I see. But there's a possibility that  
[00:40:50] somebody could just realize… I totally think so. Why  
[00:40:53] would I possibly rule this out? What are the concrete steps by which  
[00:40:58] these language models start actually impacting the world of atoms and not just the world of bits?  
[00:41:05] I don't think that there is a clean distinction between the world of bits and the world of atoms.  
[00:41:10] Suppose the neural net tells you — hey here's something that you should do, and it's going  
[00:41:15] to improve your life. But you need to rearrange your apartment in a certain way. And then you  
[00:41:20] go and rearrange your apartment as a result. The neural net impacted the world of atoms.  
[00:41:27] Fair enough. Do you think it'll take a couple of additional breakthroughs as important as  
[00:41:30] the Transformer to get to superhuman AI? Or do you think we basically got the insights in  
[00:41:36] the books somewhere, and we just need to implement them and connect them?  
[00:41:40] I don't really see such a big distinction between those two cases and let me explain why. One of  
[00:41:46] the ways in which progress is taking place in the past is that we've understood that something had a  
[00:41:57] desirable property all along but we didn't realize. Is that a breakthrough? You can say yes,  
[00:42:03] it is. Is that an implementation of something in the books? Also, yes.  
[00:42:08] My feeling is that a few of those are quite likely to happen. But in hindsight,  
[00:42:13] it will not feel like a breakthrough. Everybody's gonna say — Oh, well, of course. It's totally  
[00:42:18] obvious that such and such a thing can work. The reason the Transformer has been brought  
[00:42:24] up as a specific advance is because it's the kind of thing that was not obvious for almost  
[00:42:28] anyone. So people can say it's not something which they knew about. Let's consider the most  
[00:42:35] fundamental advance of deep learning, that a big neural network trained in backpropagation can do  
[00:42:40] a lot of things. Where's the novelty? Not in the neural network. It's not in the backpropagation.  
[00:42:49] But it was most definitely a giant conceptual breakthrough because for the longest time,  
[00:42:54] people just didn't see that. But then now that everyone sees, everyone’s gonna say — Well,  
[00:42:58] of course, it's totally obvious. Big neural network. Everyone knows that they can do it.  
[00:43:02] What is your opinion of your former advisor’s new forward forward algorithm?  
[00:43:06] I think that it's an attempt to train a neural network without backpropagation.  
[00:43:14] And that this is especially interesting if you are motivated to try to understand how  
[00:43:20] the brain might be learning its connections. The reason for that is that, as far as I know,  
[00:43:27] neuroscientists are really convinced that the brain cannot implement  
[00:43:31] backpropagation because the signals in the synapses only move in one direction.  
[00:43:36] And so if you have a neuroscience motivation, and you want to say — okay,  
[00:43:42] how can I come up with something that tries to approximate the good properties of backpropagation  
[00:43:50] without doing backpropagation? That's what the forward forward algorithm is trying to do. But  
[00:43:56] if you are trying to just engineer a good system there is no reason to not use backpropagation.  
[00:44:03] It's the only algorithm. I guess I've heard you  
[00:44:06] in different contexts talk about using humans as the existing example case that  
[00:44:14] AGI exists. At what point do you take the metaphor less seriously and don't feel the need to pursue  
[00:44:20] it in terms of the research? Because it is important to you as a sort of existence case.  
[00:44:25] At what point do I stop caring about humans as an existence case of intelligence?  
[00:44:29] Or as an example you want to follow in terms of pursuing intelligence in models.  
[00:44:37] I think it's good to be inspired by humans, it's good to be inspired by the brain. There  
[00:44:44] is an art into being inspired by humans in the brain correctly, because it's very easy to latch  
[00:44:50] on to a non-essential quality of humans or of the brain. And many people whose research is trying  
[00:44:58] to be inspired by humans and by the brain often get a little bit specific. People get a little  
[00:45:03] bit too — Okay, what cognitive science model should be followed? At the same time, consider  
[00:45:07] the idea of the neural network itself, the idea of the artificial neuron. This too is inspired  
[00:45:12] by the brain but it turned out to be extremely fruitful. So how do they do this? What behaviors  
[00:45:19] of human beings are essential that you say this is something that proves to us that it's possible?  
[00:45:24] What is an essential? No this is actually some emergent phenomenon of something more basic, and  
[00:45:31] we just need to focus on getting our own basics right.  
[00:45:43] One can and should be inspired by human intelligence with care.  
[00:45:47] Final question. Why is there, in your case, such a strong correlation between being first  
[00:45:53] to the deep learning revolution and still being one of the top researchers? You would  
[00:45:56] think that these two things wouldn't be that correlated. But why is there that correlation?  
[00:45:59] I don't think those things are super correlated. Honestly, it's hard to answer the question. I just  
[00:46:10] kept trying really hard and it turned out to have sufficed thus far.  
[00:46:14] So it's perseverance. It's a necessary but not  
[00:46:18] a sufficient condition. Many things need to come together in order to  
[00:46:22] really figure something out. You need to really go for it and also need to have the right way  
[00:46:29] of looking at things. It's hard to give a really meaningful answer to this question.  
[00:46:37] Ilya, it has been a true pleasure. Thank you so much for coming to The Lunar Society. I appreciate  
[00:46:40] you bringing us to the offices. Thank you. Yeah, I really enjoyed it. Thank you very much.  
