# Satya Nadella — Microsoft’s AGI plan & quantum breakthrough

[00:00:44] Satya, thank you so much for coming on the podcast.  
[00:00:48] In a second, we're going to get to the two breakthroughs that Microsoft has just made,  
[00:00:52] and congratulations, same day in Nature: the Majorana zero chip, which we have in front  
[00:00:58] of us right here, and also the world human action models. But can we just continue the conversation  
[00:01:03] we were having a second ago? You're describing the ways in which the things you were seeing in  
[00:01:07] the 80s and 90s, you're seeing them happen again. The thing that is exciting for me... Dwarkesh,  
[00:01:12] first of all, it's fantastic to be on your podcast. I'm a big listener,  
[00:01:16] and I love the way that you do these interviews and the broad topics that you explore.  
[00:01:25] The thing that is exciting for me… It reminds me a little bit of my, I'd say, first few years even  
[00:01:31] in the tech industry, starting in the 90s, where there was real debate about whether it's going  
[00:01:38] to be RISC or CISC, or, "Hey, are we really going to be able to build servers using x86?"  
[00:01:46] When I joined Microsoft, that was the beginning of what was Windows NT. So,  
[00:01:51] everything from the core silicon platform to the operating system to the app tier- that full stack  
[00:02:00] approach- the entire thing is being litigated. You could say cloud did a bunch of that,  
[00:02:09] and obviously distributed computing and cloud did change client-server. The web changed  
[00:02:17] massively. But this does feel a little more like maybe more full-stack than even the past  
[00:02:24] that at least I've been involved in. When you think about which decisions  
[00:02:30] ended up being the long-term winners in the 80s and 90s, and which ones didn't, and  
[00:02:34] especially when you think about- you were at Sun Microsystems, they had an interesting experience  
[00:02:38] with the 90s dotcom bubble. People talk about this data center build-out as being a bubble,  
[00:02:43] but at the same time, we have the Internet today as a result of what was built out then.  
[00:02:46] What are the lessons about what will stand the test of time? What is an inherent  
[00:02:50] secular trend? What is just ephemeral? If I go back, the four big transformations  
[00:03:02] that I've been part of, the client and the client-server. So that's the birth of the  
[00:03:11] graphical user interface and the x86 architecture, basically allowing us to build servers.  
[00:03:19] It was very clear to me. I remember going to what is PDC in '91, in fact I was at Sun at  
[00:03:25] that time. In '91, I went to Moscone. That's when Microsoft first described the Win32 interface and  
[00:03:35] it was pretty clear to me what was going to happen, where the server was also going to be  
[00:03:40] an x86 thing. When you have the scale advantages accruing to something, that's the secular bet you  
[00:03:51] have to place. What happened in the client was going to happen on the server side, and then  
[00:03:58] you were able to actually build client-server applications. So, the app model became clear.  
[00:04:04] Then the web was the big thing for us, which we had to deal with in starting,  
[00:04:09] in fact as soon as I joined Microsoft, the Netscape browser or the Mosaic browser came out  
[00:04:16] what, I think, December or November of '93, right? I think is when Andreessen and crew had that.  
[00:04:22] So that was a big game-changer, in an interesting way, just as we were getting going on what was  
[00:04:27] the client-server wave, and it was clear that we were going to win it as well. We had the  
[00:04:33] browser moment, and so we had to adjust. And we did a pretty good job of adjusting  
[00:04:38] to it because the browser was a new app model. We were able to embrace it with everything we did,  
[00:04:50] whether it was HTML in Word or building a new thing called the browser ourselves and competing  
[00:04:56] for it, and then building a web server on our server stack and go after it. Except,  
[00:05:02] of course, we missed what turned out to be the biggest business model on the web,  
[00:05:09] because we all assumed the web is all about being distributed, who would have thought that search  
[00:05:15] would be the biggest winner in organizing the web? And so that's where we obviously didn't see it,  
[00:05:23] and Google saw it and executed super well. So that's one lesson learned for me: you have  
[00:05:29] to not only get the tech trend right, you also have to get where the value is going to be created  
[00:05:39] with that trend. These business model shifts are probably tougher than even the tech trend changes.  
[00:05:48] Where is the value going to be created in AI? That's a great one. So I think there are two  
[00:05:58] places where I can say with some confidence. One is the hyperscalers that do well,  
[00:06:02] because the fundamental thing is if you sort of go back to even how Sam and others describe it,  
[00:06:07] if intelligence is log of compute, whoever can do lots of compute is a big winner.  
[00:06:16] The other interesting thing is, if you look at underneath even any AI workload,  
[00:06:20] like take ChatGPT, it's not like everybody's excited about what's happening on the GPU side,  
[00:06:24] it's great. In fact, I think of my fleet even as a ratio of the AI accelerator to storage,  
[00:06:32] to compute. And at scale, you've got to grow it. Yeah.  
[00:06:37] And so, that infrastructure need for the world is just going to be exponentially growing.  
[00:06:46] Right. So in fact it's manna  
[00:06:47] from heaven to have these AI workloads because guess what? They're more hungry for more compute,  
[00:06:55] not just for training, but we now know, for test time. When you think of an AI agent, it  
[00:07:00] turns out the AI agent is going to exponentially increase compute usage because you're not even  
[00:07:07] bound by just one human invoking a program. It's one human invoking programs that invoke lots more  
[00:07:14] programs. That's going to create massive, massive demand and scale for compute infrastructure. So  
[00:07:20] our hyperscale business, Azure business, and other hyperscalers, I think that’s a big thing.  
[00:07:26] Then after that, it becomes a little fuzzy. You could say, hey, there is a winner-take-all model-  
[00:07:35] I just don't see it. This, by the way, is the other thing I’ve learned: being very good at  
[00:07:41] understanding what are winner-take-all markets and what are not winner-take-all markets is,  
[00:07:45] in some sense, everything. I remember even in the early days when I was getting into Azure,  
[00:07:51] Amazon had a very significant lead and people would come to me, and investors would come to me,  
[00:07:56] and say, "Oh, it's game over. You'll never make it. Amazon, it's winner-take-all."  
[00:08:01] Having competed against Oracle and IBM in client-server, I knew that the buyers  
[00:08:06] will not tolerate winner-take-all. Structurally, hyperscale will never  
[00:08:12] be a winner-take-all because buyers are smart. Consumer markets sometimes can be winner-take-all,  
[00:08:20] but anything where the buyer is a corporation, an enterprise, an IT department,  
[00:08:26] they will want multiple suppliers. And so you got to be one of the multiple suppliers.  
[00:08:32] That, I think, is what will happen even on the model side. There will be open-source. There  
[00:08:38] will be a governor. Just like on Windows, one of the big lessons learned for me was,  
[00:08:43] if you have a closed-source operating system, there will be a complement to it,  
[00:08:48] which will be open source. And so to some degree that's  
[00:08:52] a real check on what happens. I think in models there is one dimension of, maybe there will be  
[00:08:59] a few closed source, but there will definitely be an open source alternative, and the open-source  
[00:09:03] alternative will actually make sure that the closed-source, winner-take-all is mitigated.  
[00:09:10] That's my feeling on the model side. And by the way, let's not discount if this thing is really  
[00:09:16] as powerful as people make it out to be, the state is not going to sit around and wait for  
[00:09:22] private companies to go around… and all over the world. So, I don't see it as a winner-take-all.  
[00:09:29] Then above that, I think it's going to be the same old stuff, which is in consumer,  
[00:09:34] in some categories, there may be some winner-take-all network effect.  
[00:09:38] After all, ChatGPT is a great example. It's an at-scale consumer property that  
[00:09:45] has already got real escape velocity. I go to the App Store, and I see it's always there in the top  
[00:09:52] five, and I say “wow, that's pretty unbelievable”. So they were able to use that early advantage and  
[00:10:00] parlay that into an app advantage. In consumer, that could happen. In the enterprise again,  
[00:10:06] I think there will be, by category, different winners. That's sort of at least how I analyze it.  
[00:10:11] I have so many follow-up questions. We have to get to quantum in just a second, but on the idea  
[00:10:19] that maybe the models get commoditized: maybe somebody could have made a similar argument a  
[00:10:25] couple of decades ago about the cloud – that fundamentally, it's just a chip and a box.  
[00:10:30] But in the end, of course, you and many others figured out how to get amazing profit margins in  
[00:10:34] the cloud. You figured out ways to get economies of scale and add other value. Fundamentally,  
[00:10:41] even forgetting the jargon, if you've got AGI and it's helping you make better AIs – right now,  
[00:10:46] it's synthetic data and RL; maybe in the future, it's an automated AI researcher – that seems like  
[00:10:50] a good way to entrench your advantage there. I'm curious what you make of that, just the idea that  
[00:10:55] it really matters to be ahead there. At scale, nothing is commodity.  
[00:11:00] To your point about cloud, everybody would say, "Oh, cloud's a commodity." Except,  
[00:11:04] when you scale... That's why the know-how of running a hyperscaler... You could say, "Oh,  
[00:11:08] what the heck? I can just rack and stack servers." Right.  
[00:11:11] In fact, in the early days of hyperscale, most people thought “there are all these hosters,  
[00:11:16] and those are not great businesses. Will there be anything? Is there a business even in hyperscale?”  
[00:11:23] And it turns out there is a real business, just because of the know-how of running, in  
[00:11:29] the case of Azure, the world's computing of 60-plus regions with all the compute. It's  
[00:11:35] just a tough thing to duplicate. So I was more making the point,  
[00:11:41] is it one winner? Is it a winner-take-all or not? Because that you've got to get right. I  
[00:11:48] like to enter categories which are big TAMs, where you don't have to have the risk of it  
[00:11:55] all being winner-take-all. The best news to be in is a big market that can accommodate  
[00:12:03] a couple of winners, and you're one of them. That's what I meant by the hyperscale layer.  
[00:12:12] In the model layer, one is models need ultimately to run on some hyperscale compute. So that nexus,  
[00:12:20] I feel, is going to be there forever. It's not just the model; the model needs state, that means  
[00:12:27] it needs storage, and it needs regular compute for running these agents and the agent environments.  
[00:12:33] And so that's how I think about why the limit of one person running away with  
[00:12:39] one model and building it all may not happen. On the hyperscaler side, and by the way, it's also  
[00:12:48] interesting the advantage you as a hyperscaler would have in the sense that, especially with  
[00:12:52] inference time scaling and if that's involved in training future models, you can amortize  
[00:12:57] your data centers and GPUs, not only for the training, but then use them again for inference.  
[00:13:02] I'm curious what kind of hyperscaler you consider Microsoft and Azure to be. Is it on  
[00:13:07] the pre-training side? Is it on providing the O3-type inference? Or are you just,  
[00:13:11] we’re going to host and deploy any single model that's out there in the market,  
[00:13:15] and we are sort of agnostic about that? It’s a good point. The way we want to  
[00:13:23] build out the fleet is [to], in some sense ride Moore's law. I think this will be like  
[00:13:32] what we've done with everything else in the past: every year keep refreshing the fleet,  
[00:13:41] you depreciate it over whatever the lifetime value of these things are, and then get very very good  
[00:13:49] at the placement of the fleet such that you can run different jobs at it with high utilization.  
[00:13:58] Sometimes there are very big training jobs that need to have highly concentrated peak  
[00:14:05] flops that are provisioned to it that also need to cohere. That's great. We should have enough  
[00:14:11] data center footprint to be able to give that. But at the end of the day, these are all becoming  
[00:14:16] so big, even in terms of if you take pre-training scale, if it needs to keep going, even  
[00:14:22] pre-training scale at some point has to cross data center boundaries. It's all more or less there.  
[00:14:28] So, great, once you start crossing pre-training data center boundaries, is it that different than  
[00:14:35] anything else? The way I think about it is hey, distributed computing will remain distributed,  
[00:14:41] so go build out your fleet such that it's ready for large training jobs,  
[00:14:46] it's ready for test-time compute, it’s ready- in fact, if this RL thing that might happens,  
[00:14:52] you build one large model, and then after that, there’s tons of RL going on. To me,  
[00:14:59] it's kind of like more training flops, because you want to create these highly specialized,  
[00:15:04] distilled models for different tasks. So you want that fleet, and then the  
[00:15:09] serving needs. At the end of the day, speed of light is speed of light,  
[00:15:11] so you can't have one data center in Texas and say, "I'm going to serve the world from there."  
[00:15:17] You've got to serve the world based on having an inference fleet everywhere in  
[00:15:22] the world. That's how I think of our build-out of a true hyperscale fleet.  
[00:15:29] Oh, and by the way, I want my storage and compute also close to all of these things,  
[00:15:36] because it's not just AI accelerators that are stateless. My training data itself needs storage,  
[00:15:46] and then I want to be able to multiplex multiple training jobs, I want to be able to  
[00:15:50] then have memory, I want to be able to have these environments in which these agents can go execute  
[00:15:59] programs. That's kind of how I think about it. You recently reported that your yearly revenue  
[00:16:05] from AI is $13 billion. But if you look at your year-on-year growth on that, in like four years,  
[00:16:10] it'll be 10x that. You'll have $130 billion in revenue from AI, if the trend continues. If it  
[00:16:15] does, what do you anticipate doing with all that intelligence, this industrial scale use?  
[00:16:21] Is it going to be through Office? Is it going to be you deploying it for others to host?  
[00:16:26] You've got to have the AGIs to have $130 billion in revenue? What does it look like?  
[00:16:30] The way I come at it, Dwarkesh, it's a great question because at some level,  
[00:16:35] if you're going to have this explosion, abundance, whatever, commodity of intelligence available,  
[00:16:42] the first thing we have to observe is GDP growth. Before I get to what Microsoft's revenue will look  
[00:16:49] like, there's only one governor in all of this. This is where we get a little  
[00:16:53] bit ahead of ourselves with all this AGI hype. Remember the developed world, which is what? 2%  
[00:17:04] growth and if you adjust for inflation it’s zero? So in 2025, as we sit here, I'm not an economist,  
[00:17:14] at least I look at it and say we have a real growth challenge. So, the first thing that  
[00:17:19] we all have to do is, when we say this is like the Industrial Revolution, let's have  
[00:17:27] that Industrial Revolution type of growth. That means to me, 10%, 7%, developed world,  
[00:17:34] inflation-adjusted, growing at 5%. That's the real marker. It can't just be supply-side.  
[00:17:44] In fact that’s the thing, a lot of people are writing about it, and I'm glad they are,  
[00:17:48] which is the big winners here are not going to be tech companies. The winners are going to be the  
[00:17:54] broader industry that uses this commodity that, by the way, is abundant. Suddenly productivity goes  
[00:18:02] up and the economy is growing at a faster rate. When that happens, we'll be fine as an industry.  
[00:18:10] But that's to me the moment. Us self-claiming some AGI milestone,  
[00:18:15] that's just nonsensical benchmark hacking to me. The real benchmark is: the world growing at 10%.  
[00:18:24] Okay, so if the world grew at 10%, the world economy is $100 trillion or something, if the  
[00:18:27] world grew at 10%, that's like an extra $10 trillion in value produced every single year.  
[00:18:34] If that is the case, you as a hyperscaler... It seems like $80 billion is a lot of money.  
[00:18:40] Shouldn't you be doing like $800 billion? If you really think in a couple of years,  
[00:18:44] we could be really growing the world economy at this rate, and the key bottleneck would be:  
[00:18:47] do you have the compute necessary to deploy these AIs to do all this work?  
[00:18:53] That is correct. But by the way, the classic supply side is, "Hey, let me build it and they’ll  
[00:19:03] come." That's an argument, and after all we've done that, we've taken enough risk to go do it.  
[00:19:09] But at some point, the supply and demand have to map. That's why I'm tracking both sides of  
[00:19:17] it. You can go off the rails completely when you are hyping yourself with the supply-side,  
[00:19:25] versus really understanding how to translate that into real value to customers.  
[00:19:32] That's why I look at my inference revenue. That's one of the reasons why even the disclosure on the  
[00:19:36] inference revenue... It's interesting that not many people are talking about their real revenue,  
[00:19:41] but to me, that is important as a governor for how you think about it.  
[00:19:45] You're not going to say they have to symmetrically meet at any given point in time, but you need to  
[00:19:50] have existence proof that you are able to parlay yesterday's, let’s call it capital, into today's  
[00:19:58] demand, so that then you can again invest, maybe exponentially even, knowing that you're  
[00:20:05] not going to be completely rate mismatched. I wonder if there's a contradiction in these  
[00:20:09] two different viewpoints, because one of the things you've done wonderfully is make these  
[00:20:13] early bets. You invested in OpenAI in 2019, even before there was Copilot and any applications.  
[00:20:19] If you look at the Industrial Revolution, these 6%, 10% build-outs of railways and  
[00:20:25] whatever things, many of those were not like, "We've got revenue from the tickets,  
[00:20:28] and now we're going to..." There was a lot of money lost.  
[00:20:30] That's true. So, if you really think there's some potential here to 10x or 5x the growth  
[00:20:38] rate of the world, and then you're like, "Well, what is the revenue from GPT-4?"  
[00:20:44] If you really think that's the possibility from the next level up, shouldn't you just,  
[00:20:48] "Let's go crazy, let's do the hundreds of billions of dollars of compute?" I mean,  
[00:20:51] there's some chance, right? Here’s the interesting thing, right?  
[00:21:02] That's why even that balanced approach to the fleet, at least, is very important to me. It's  
[00:21:07] not about building compute. It's about building compute that can actually help me not only train  
[00:21:12] the next big model but also serve the next big model. Until you do those two things, you're not  
[00:21:18] going to be able to really be in a position to take advantage of even your investment.  
[00:21:22] So, that's kind of where it's not a race to just building a model,  
[00:21:27] it's a race to creating a commodity that is getting used in the world to drive...  
[00:21:32] You have to have a complete thought, not just one thing that you’re thinking about.  
[00:21:37] And by the way, one of the things is that there will be overbuild. To your  
[00:21:44] point about what happened in the dotcom era, the memo has gone out that, hey, you know,  
[00:21:50] you need more energy, and you need more compute. Thank God for it. So, everybody's going to race.  
[00:21:55] In fact, it's not just companies deploying, countries are going to deploy capital,  
[00:22:00] and there will be clearly... I'm so excited to be a leaser, because, by the way; I build a lot,  
[00:22:08] I lease a lot. I am thrilled that I'm going to be leasing a lot of capacity in '27,  
[00:22:14] '28 because I look at the builds, and I'm saying, "This is fantastic." The only thing  
[00:22:18] that's going to happen with all the compute builds is the prices are going to come down.  
[00:22:24] Speaking of prices coming down, you recently tweeted after the DeepSeek model came out about  
[00:22:28] Jevons’ Paradox. I'm curious if you can flesh that out. Jevons’ Paradox occurs when the demand for  
[00:22:34] something is highly elastic. Is intelligence that bottlenecked on prices going down?  
[00:22:43] Because when I think about, at least my use cases as a consumer, intelligence is already so cheap.  
[00:22:47] It's like two cents per million tokens. Do I really need it to go down to 0.02 cents? I'm just  
[00:22:52] really bottlenecked on it becoming smarter. If you need to charge me 100x, do a 100x bigger training  
[00:22:57] run. I'm happy for companies to take that. But maybe you're seeing something different  
[00:23:01] on the enterprise side or something. What is the key use case of intelligence that really requires  
[00:23:05] it to get to 0.002 cents per million tokens? I think the real thing is the utility of the  
[00:23:10] tokens. Both need to happen: One is intelligence needs to get better and cheaper. And anytime  
[00:23:20] there's a breakthrough, like even what DeepSeek did, with the efficient frontier of performance  
[00:23:26] per token changes, the curve gets bent, and the frontier moves. That just brings  
[00:23:34] more demand. That's what happened with cloud. Here’s an interesting thing: We used to think  
[00:23:40] “oh my God, we've sold all the servers in the client-server era”. Except once we started  
[00:23:45] putting servers in the cloud, suddenly people started consuming more because they could buy  
[00:23:52] it cheaper, and it was elastic, and they could buy it as a meter versus a license,  
[00:24:00] and it completely expanded. I remember going, let’s say,  
[00:24:03] to a country like India and talking about “here is SQL Server”. We sold a little,  
[00:24:09] but man, the cloud in India is so much bigger than anything that we were able to do in the  
[00:24:13] server era. I think that's going to be true. If you think about, if you want to really have,  
[00:24:19] in the Global South, in a developing country, if you had these tokens that were available  
[00:24:25] for healthcare that were really cheap, that would be the biggest change ever.  
[00:25:36] I think it's quite reasonable for somebody to hear people like me in San Francisco and think  
[00:25:40] “they're kind of silly; they don't know what it's actually like to deploy things in the real world”.  
[00:25:43] As somebody who works with these Fortune 500s and is working with them to deploy  
[00:25:48] things for hundreds of millions, billions of people, what's your sense on how fast  
[00:25:53] deployment of these capabilities will be? Even when you have working agents, even when  
[00:25:57] you have things that can do remote work for you, with all the compliance and with all the inherent  
[00:26:02] bottlenecks, is that going to be a big bottleneck, or is that going to move past pretty fast?  
[00:26:07] It is going to be a real challenge because the real issue is change management or process  
[00:26:16] change. Here's an interesting thing: one of the analogies I use is, just imagine how a  
[00:26:24] multinational corporation like us did forecasts pre-PC, and email, and spreadsheets. Faxes went  
[00:26:34] around. Somebody then got those faxes and did an interoffice memo that then went around, and people  
[00:26:42] entered numbers, and then ultimately a forecast came, maybe just in time for the next quarter.  
[00:26:51] Then somebody said, "Hey, I'm just going to take an Excel spreadsheet, put it in email,  
[00:26:55] send it around. People will go edit it, and I'll have a forecast." So, the entire  
[00:26:59] forecasting business process changed because the work artifact and the workflow changed.  
[00:27:07] That is what needs to happen with AI being introduced into knowledge work. In fact, when we  
[00:27:16] think about all these agents, the fundamental thing is there's a new work and workflow.  
[00:27:22] For example, even prepping for our podcast, I go to my copilot and I say, "Hey, I'm going to talk  
[00:27:28] to Dwarkesh about our quantum announcement and this new model that we built for game generation.  
[00:27:37] Give me a summary of all the stuff that I should read up on before going." It knew the two Nature  
[00:27:44] papers, it took that. I even said, "Hey, go give it to me in a podcast format." And so, it even  
[00:27:50] did a nice job of two of us chatting about it. So that became—and in fact, then I shared it  
[00:27:56] with my team. I took it and put it into Pages, which is our artifact,  
[00:28:00] and then shared. So the new workflow for me is I think with AI and work with my colleagues.  
[00:28:07] That's a fundamental change management of everyone who's doing knowledge work, suddenly figuring out  
[00:28:15] these new patterns of "How am I going to get my knowledge work done in new ways?" That is  
[00:28:21] going to take time. It's going to be something like in sales, and in finance, and supply chain.  
[00:28:26] For an incumbent, I think that this is going to be one of those things where—you know,  
[00:28:31] let's take one of the analogies I like to use is what manufacturers did with Lean. I love  
[00:28:36] that because, in some sense, if you look at it, Lean became a methodology of how one could take  
[00:28:41] an end-to-end process in manufacturing and become more efficient. It's that continuous improvement,  
[00:28:46] which is reduce waste and increase value. That's what's going to come to knowledge.  
[00:28:50] This is like Lean for knowledge work, in particular. And that's going to be the hard work  
[00:28:55] of management teams and individuals who are doing knowledge work, and that's going to take its time.  
[00:29:00] Can I ask you just briefly about that analogy? One of the things Lean did  
[00:29:05] is physically transform what a factory floor looks like. It revealed bottlenecks that people  
[00:29:10] didn't realize until you're really paying attention to the processes and workflows.  
[00:29:15] You mentioned briefly what your own workflow—how your own workflow has  
[00:29:18] changed as a result of AIs. I'm curious if we can add more color to what will it be like to  
[00:29:25] run a big company when you have these AI agents that are getting smarter and smarter over time?  
[00:29:29] It's interesting you ask that. I was thinking, for example, today if I look at it, we are very  
[00:29:37] email heavy. I get in in the morning, and I’m like, man my inbox is full, and I'm responding,  
[00:29:42] and so I can't wait for some of these Copilot agents to automatically populate my  
[00:29:48] drafts so that I can start reviewing and sending. But I already have in Copilot at least ten agents,  
[00:29:59] which I query them different things for different tasks. I feel like there's a new  
[00:30:06] inbox that's going to get created, which is my millions of agents that I'm working with  
[00:30:12] will have to invoke some exceptions to me, notifications to me, ask for instructions.  
[00:30:18] So at least what I'm thinking is that there's a new scaffolding, which is the agent manager.  
[00:30:24] It's not just a chat interface. I need a smarter thing than a chat interface to  
[00:30:30] manage all the agents and their dialogue. That's why I think of this Copilot,  
[00:30:35] as the UI for AI, is a big, big deal. Each of us is going to have it. So basically, think of it as:  
[00:30:43] there is knowledge work, and there's a knowledge worker. The knowledge work may be done by many,  
[00:30:50] many agents, but you still have a knowledge worker who is dealing with all the knowledge workers.  
[00:30:58] And that, I think, is the interface that one has to build.  
[00:31:04] You're one of the few people in the world who can say that you have access to 200,000… you  
[00:31:09] have this swarm of intelligence around you in the form of Microsoft the company and all its  
[00:31:13] employees. And you have to manage that, and you have to interface with that, how to make  
[00:31:19] best use of that. Hopefully, more of the world will get to have that experience in the future.  
[00:31:24] I'd be curious about how your inbox, if that means everybody's inbox,  
[00:31:28] will look like yours in the morning. Okay, before we get to that,  
[00:31:30] I want to keep asking you more about AI, but I really want to ask you about the big  
[00:31:34] breakthrough in quantum that Microsoft Research has announced. So can you explain what's going on?  
[00:31:39] This has been another 30-year journey for us. It's unbelievable. I'm the third CEO  
[00:31:48] of Microsoft who's been excited about quantum. The fundamental breakthrough here, or the vision  
[00:31:58] that we've always had is, you need a physics breakthrough in order to build a utility-scale  
[00:32:06] quantum computer that works. We took the path of saying, the one way for having a less noisy  
[00:32:23] or more reliable qubit is to bet on a physical property that by definition is more reliable and  
[00:32:32] that's what led us to the Majorana zero modes, which was theorized in the 1930s. The question  
[00:32:42] was, can we actually physically fabricate these things? Can we actually build them?  
[00:32:47] So the big breakthrough effectively, and I know you talked to Chetan, was that we now finally  
[00:32:53] have existence proof and a physics breakthrough of Majorana zero modes in a new phase of matter  
[00:33:04] effectively. This is why we like the analogy of thinking of this as the transistor moment  
[00:33:09] of quantum computing, where we effectively have a new phase, which is the topological phase, which  
[00:33:20] means we can even now reliably hide the quantum information, measure it, and we can fabricate it.  
[00:33:32] And so now that we have it, we feel like with that core foundational fabrication technique out of the  
[00:33:40] way, we can start building a Majorana chip. That Majorana One which I think is going to  
[00:33:46] basically be the first chip that will be capable of a million qubits, physical. And then on that,  
[00:33:54] thousands of logical qubits, error-corrected. And then it's game on. You suddenly have the  
[00:34:04] ability to build a real utility-scale quantum computer, and that to me is now so much more  
[00:34:10] feasible. Without something like this, you will still be able to achieve milestones,  
[00:34:19] but you'll never be able to build a utility-scale computer. That's why we're excited about it.  
[00:34:23] Amazing. And by the way, I believe this is it right here.  
[00:34:25] That is it. Yes.  
[00:34:27] I forget now, are we calling it Majorana? Yes,  
[00:34:29] that's right. Majorana One. I'm glad we named it after that.  
[00:34:34] To think that we are able to build something like a million-qubit quantum computer in a thing  
[00:34:44] of this size is just unbelievable. That's the crux of it: unless and until we could do that,  
[00:34:52] you can't dream of building a utility-scale quantum computer.  
[00:34:55] And you're saying the eventual million qubits will go on a chip this size? Okay, amazing.  
[00:35:01] Other companies have announced 100 physical qubits, Google's, IBM's, others. When you  
[00:35:08] say you've announced one, but you're saying that yours is way more scalable in the limit.  
[00:35:13] Yeah. The one thing we’ve also done is we've taken an approach where we've separated our  
[00:35:19] software and our hardware. We're building out our software stack, and we now have,  
[00:35:28] with the neutral atom folks, the ion trap folks, we're also working with others who even have  
[00:35:36] pretty good approaches with photonics and what have you, that means there'll be different types  
[00:35:40] of quantum computers. In fact, we have what, I think that the last thing that we announced was 24  
[00:35:45] logical qubits. So we have also got some fantastic breakthroughs on error correction and that's what  
[00:35:52] is allowing us, even on neutral atom and ion trap quantum computers, to build these 20 plus,  
[00:36:00] and I think that'll keep going even throughout the year; you'll see us improve that yardstick.  
[00:36:06] But we also then said, "Let's go to the first principles and build our own quantum computer  
[00:36:14] that is betting on the topological qubit." And that's what this breakthrough is about.  
[00:36:21] Amazing. The million topological qubits, thousands of logical qubits,  
[00:36:28] what is the estimated timeline to scale up to that level? What does the Moore's law here,  
[00:36:32] if you've got the first transistor, look like? We've obviously been working on this for  
[00:36:35] 30 years. I'm glad we now have the physics breakthrough and the fabrication breakthrough.  
[00:36:44] I wish we had a quantum computer because by the way, the first thing the quantum  
[00:36:47] computer will allow us to do is build quantum computers, because it's going to  
[00:36:51] be so much easier to simulate atom-by-atom construction of these new quantum gates.  
[00:36:58] But in any case, the next real thing is, now that we have the fabrication technique,  
[00:37:04] let us go build that first fault-tolerant quantum computer. And that will be the logical thing.  
[00:37:12] So, I would say now I can say, "Oh, maybe '27, '28, '29, we will be able to actually  
[00:37:19] build this." Now that we have this one gate, can I put the thing into an integrated circuit and then  
[00:37:25] actually put these integrated circuits into a real computer? That is where the next logical step is.  
[00:37:31] And what do you see as, in '27, '28, you've got it working? Is it a thing you access through  
[00:37:38] the API? Is it something you're using internally for your own research in materials and chemistry?  
[00:37:43] It’s a great question. One thing that I've been excited about is, even in today's world…  
[00:37:49] we had this quantum program, and we added some APIs to it. The breakthrough we had  
[00:37:56] maybe two years ago was to think of this HPC stack, and AI stack, and quantum together.  
[00:38:06] In fact, if you think about it, AI is like an emulator of the simulator. Quantum is like a  
[00:38:14] simulator of nature. What is quantum going to do? By the way, quantum is not going to  
[00:38:19] replace classical. Quantum is great at what quantum can do, and classical will also...  
[00:38:27] Quantum is going to be fantastic for anything that is not data-heavy but is exploration-heavy  
[00:38:33] in terms of the state space. It should be data-light but exponential states that you  
[00:38:39] want to explore. Simulation is a great one: chemical physics, what have you, biology.  
[00:38:48] One of the things that we've started doing is really using AI as the emulation engine.  
[00:38:55] But you can then train. So the way I think of it is, if you have AI plus quantum, maybe you'll use  
[00:39:02] quantum to generate synthetic data that then gets used by AI to train better models that know how to  
[00:39:08] model something like chemistry or physics or what have you. These two things will get used together.  
[00:39:13] So even today, that's effectively what we're doing with the combination of  
[00:39:18] HPC and AI. I hope to replace some of the HPC pieces with quantum computers.  
[00:40:27] Can you tell me a little bit about how you make these research decisions which,  
[00:40:31] in 20 years time, 30 years time, will actually pay dividends, especially at  
[00:40:35] a company of Microsoft's scale? Obviously, you're in great touch with the technical details in this  
[00:40:43] project. Is it feasible for you to do that with all the things Microsoft Research does?  
[00:40:47] How do you know the current bet you're making will pay out in 20 years? Does it just have to  
[00:40:52] emerge organically through the org, or how are you keeping track of all this?  
[00:40:58] The thing that I feel was fantastic is when Bill, when he started MSR back in '95 I guess. I think  
[00:41:10] in the long history of these curiosity-driven research organizations, to just do a research  
[00:41:17] org that is about fundamental research and MSR, over the years, has built up that institutional  
[00:41:24] strength so when I think about capital allocation or budgets, we first put the chips in and say,  
[00:41:32] "Here is MSR's budget." We gotta go at it each year knowing that most of these bets are not  
[00:41:41] going to pay off in any finite time frame. Maybe the sixth CEO of Microsoft will benefit from it.  
[00:41:48] And in tech that is I think a given. The real thing that I think about is,  
[00:41:56] when the time has come for something like quantum or a new model or what have you, can  
[00:42:04] you capitalize? So as an incumbent, if you look at the history of tech, it's not that people didn't  
[00:42:11] invest. It's that you need to have a culture that knows how to take an innovation and scale it.  
[00:42:21] That's the hard part, quite frankly, for CEOs and management teams. Which is kind of fascinating.  
[00:42:31] It's as much about good judgment as it is about good culture. Sometimes we've gotten it right;  
[00:42:38] sometimes we've gotten it wrong; I can tell you the thousand projects from MSR that we should have  
[00:42:45] probably led with, but we didn't. And I always ask myself why. It's because we were not able to  
[00:42:53] get enough conviction and that complete thought of how to not only take the innovation but make  
[00:43:02] it into a useful product with a business model that we can then go to market with.  
[00:43:07] That's the job of CEOs and management teams: not to just be excited about any one thing,  
[00:43:13] but to be able to actually execute on a complete thing. And that's easier said than done.  
[00:43:19] When you mentioned the possibility of three subsequent CEOs of Microsoft, if each of them  
[00:43:25] increases the market cap by an order of magnitude, by the time you've got the next breakthrough,  
[00:43:28] you'll be like the world economy or something. Or remember, the world is going to be growing  
[00:43:32] at 10%, so we'll be fine. Let's dig into the other big  
[00:43:36] breakthrough you've just made. It's amazing that you have both of them coming out the same day,  
[00:43:39] in your gaming world models. I'd love if you can tell me a little bit about that.  
[00:43:43] We're going to call it Muse. It's going to be the model of this world action, or human action model.  
[00:43:53] This is very cool. One of the things is that obviously, Dall-E and Sora have been  
[00:43:58] unbelievable in what they've been able to do in terms of generative models. One  
[00:44:02] thing that we wanted to go after was using gameplay data. Can you actually  
[00:44:10] generate games that are both consistent and then have the ability to generate the  
[00:44:16] diversity of what that game represents, and then are persistent to user mods?  
[00:44:21] That's what this is. They were able to work with one of our game studios,  
[00:44:28] and this is the other publication in Nature. The cool thing is what I'm excited about is  
[00:44:33] bringing--we're going to have a catalog of games soon that we will start using these models,  
[00:44:40] or we're going to train these models to generate, and then start playing them.  
[00:44:46] In fact, when Phil Spencer first showed it to me, he had an Xbox controller and this  
[00:44:52] model basically took the input and generated the output based on the input. And it was consistent  
[00:44:59] with the game. That to me is a massive moment of “wow”. It's kind of like the first time we  
[00:45:08] saw ChatGPT complete sentences, or Dall-E draw, or Sora. This is one such moment.  
[00:45:17] I got a chance to see some of the videos in the real-time demo this morning with  
[00:45:21] your lead researcher Katja on this. Only once I talked to her did it really hit me  
[00:45:27] how incredible this is, in the sense that we've used AI in the past to model agents,  
[00:45:31] and just using that same technique to model the world around the agent gives consistent  
[00:45:36] real-time – we'll superimpose videos of what this looks like atop this podcast so people can get a  
[00:45:40] chance to see it for themselves. I guess it'll be out by then, so they can also watch it there.  
[00:45:43] This in itself is incredible. You, through your span as CEO, have invested tens of hundreds of  
[00:45:49] billions of dollars in building up Microsoft Gaming and acquiring IP.  
[00:45:56] In retrospect, if you can just merge all of this data into one big model that can give  
[00:46:02] you this experience of visiting and going through multiple worlds at the same time,  
[00:46:08] and if this is the direction gaming is headed, it seems like a pretty good investment to have  
[00:46:13] made. Did you have any premonition about this? I wouldn't say that we invested in gaming to  
[00:46:21] build models. We invested, quite frankly, because- here's an interesting thing about our history:  
[00:46:27] We built our first game before we built Windows. Flight Simulator was a Microsoft  
[00:46:33] product long before we even built Windows. So, gaming has got a long history at the company,  
[00:46:40] and we want to be in gaming for gaming's sake. I always start by saying I hate to  
[00:46:45] be in businesses where they're means to some other end. They have to be ends unto themselves.  
[00:46:50] And then, yes, we're not a conglomerate. We are a company where we have to bring  
[00:46:54] all these assets together and be better owners by adding value. For example, cloud gaming is  
[00:47:00] a natural thing for us to invest in because that will just expand the TAM and expand the ability  
[00:47:07] for people to play games everywhere. The same thing with AI and gaming:  
[00:47:11] we definitely think that it can be helpful in maybe changing- it's kind of like the CGI moment,  
[00:47:16] even for gaming long-term. And it's great. As the biggest, world's largest publisher,  
[00:47:20] this will be helpful. But at the same time, we've got to produce great quality games. I mean,  
[00:47:24] you can't be a gaming publisher without, sort of, first and foremost being focused on that.  
[00:47:30] But the fact that this data asset is going to be interesting, not just in a gaming context,  
[00:47:36] but it's going to be a general action model and a world model, it's fantastic. I mean like,  
[00:47:42] you know, I think about gaming data as perhaps, you know, what YouTube is perhaps to Google,  
[00:47:47] gaming data is to Microsoft. And so therefore I'm excited about that.  
[00:47:52] Yeah, and that's what I meant, just in the sense of like, you can have one unified experience  
[00:47:56] across many different kinds of games. How does this fit into the other, separate from AI,  
[00:48:01] the other things that Microsoft has worked on in the past, like mixed reality? Maybe giving  
[00:48:06] smaller game studios a chance to build these AAA action games? Just like five, ten years from now,  
[00:48:11] what kinds of ways could you imagine? I've thought about these three things  
[00:48:15] as the cornerstones of, in an interesting way, even five, six, seven years ago is when I said  
[00:48:22] the three big bets that we want to place [are] AI, quantum, and mixed reality. And I still  
[00:48:28] believe in them, because in some sense, what are the big problems to be solved?  
[00:48:32] Presence. That's the dream of mixed reality. Can you create real presence?  
[00:48:42] Like you and I doing a podcast like this. I think it’s still proving to be the harder  
[00:48:48] one of those challenges, quite honestly. I thought it was going to be more solvable. It's tougher,  
[00:48:53] perhaps, just because of the social side of it: wearing things and so on.  
[00:49:00] We're excited about, in fact, what we're going to do with Anduril and Palmer, now,  
[00:49:03] with even how they'll take forward the IVAS program, because that's a fantastic  
[00:49:09] use case. And so we'll continue on that front. But also, the 2D surfaces. It turns out things  
[00:49:16] like Teams, right, thanks to the pandemic, we've really gotten the ability to create  
[00:49:22] essentially presence through even 2D. And that I think will continue. That's one secular piece.  
[00:49:29] Quantum we talked about, and AI is the other one. So these are the three things that I look at and  
[00:49:34] say, how do you bring these things together? Ultimately, not as tech for tech's sake,  
[00:49:40] but solving some of the fundamental things that we, as humans, want in our life, and more, we want  
[00:49:46] them in our economy, driving our productivity. And so if we can somehow get that right,  
[00:49:51] then I think we will have really made progress. When you write your next book, you've got to have  
[00:49:55] some explanation of why those three pieces all came together around the same time,  
[00:49:58] right? Like, there's no intrinsic reason you would think quantum and AI should happen in  
[00:50:02] 2028 and 2025 and so forth. That's right. At some level,  
[00:50:07] I look at it and say: the simple model I have is, hey is there a systems breakthrough? To me,  
[00:50:11] the systems breakthrough is the quantum thing. Is there a business logic breakthrough? That's  
[00:50:18] AI to me, which is: can the logic tier be fundamentally reasoned differently? Instead of  
[00:50:27] imperatively writing code, can you have a learning system? That's the AI one.  
[00:50:31] And then the UI side of it is presence. Going back to AI for a second, in your  
[00:50:38] 2017 book… 2019 you invest in OpenAI, very early, 2017 is even earlier, you say in your book, "One  
[00:50:45] might also say that we're birthing a new species, one whose intelligence may have no upper limits."  
[00:50:50] Now, super-early, of course, to be talking about this in 2017. We've been talking in  
[00:50:55] a granular fashion about agents, Office Copilot, capex, and so forth. But if you  
[00:51:02] zoom out and consider this statement you've made, and you think about you as a hyperscaler,  
[00:51:09] as the person doing research in these models as well, providing training, inference, and research  
[00:51:14] for building a new species, how do you think about this in the grand scheme of things?  
[00:51:19] Do you think we're headed towards superhuman intelligence in your time as CEO?  
[00:51:22] I think even Mustafa uses that term. In fact he’s used that term more recently, this “new species”.  
[00:51:32] The way I come at it is, you definitely need trust. Before we claim it is something as big  
[00:51:44] as a species, the fundamental thing that we've got to get right is that there is real trust,  
[00:51:51] whether it's personal or societal level trust, that's baked in. That's the hard problem.  
[00:51:58] I think the one biggest rate limiter to the power here will be how does our legal… call  
[00:52:06] it infrastructure, we’re talking about all the compute infrastructure, well how does  
[00:52:09] the legal infrastructure evolve to deal with this? This entire world is  
[00:52:16] constructed with things like humans owning property, having rights, and being liable.  
[00:52:28] That’s the fundamental thing that one has to first say, okay what does that mean for anything that  
[00:52:34] now humans are using as tools? And if humans are going to delegate more authority to these things,  
[00:52:41] then how does that structure evolve? Until that really gets resolved, I don't think just talking  
[00:52:48] about the tech capability is going to happen. As in, we won't be able to deploy these kinds  
[00:52:54] of intelligences until we figure out how to…? Absolutely. Because at the end of the day,  
[00:52:57] there is no way. Today, you cannot deploy these intelligences unless and  
[00:53:01] until there's someone indemnifying it as a human. To your point, I think that's one of the reasons  
[00:53:07] why I think about even the most powerful AI is essentially working with some delegated  
[00:53:12] authority from some human. You can say, oh, that's all alignment and this, that, and the other.  
[00:53:18] That's why I think you have to really get these alignments to work and be verifiable in some way,  
[00:53:25] but I just don't think that you can deploy intelligences that are out of control. For  
[00:53:29] example, this AI takeoff problem may be a real problem, but before it is a real problem, the real  
[00:53:35] problem will be in the courts. No society is going to allow for some human to say, "AI did that."  
[00:53:44] Yes. Well, there's a lot of societies in the world, and I wonder if any one of them might  
[00:53:49] not have a legal system that might be more amenable. And if you can't have a takeoff,  
[00:53:52] then you might worry. It doesn't have to happen in America, right?  
[00:54:04] We think that no society cares about it, right? There can be rogue actors, I'm not saying there  
[00:54:08] won't be rogue actors; there are cyber criminals and rogue states; they're going to be there.  
[00:54:13] But to think that human society at large doesn't care about it is also not going  
[00:54:19] to be true. I think we all will care. We know how to deal with rogue states and rogue actors  
[00:54:26] today. The world doesn't sit around and say “we’ll tolerate that”. That's why I'm glad  
[00:54:34] that we have a world order in which anyone who is a rogue actor in a rogue state has consequences.  
[00:54:41] Right. But if you have this picture where you can have 10% economic growth, I think it really  
[00:54:46] depends on getting something like AGI working, because tens of trillions of dollars of value,  
[00:54:53] that sounds closer to the total of human wages, around $60 trillion of the economy. Getting that  
[00:54:59] magnitude, you kind of have to automate labor or supplement labor in a very significant way.  
[00:55:06] If that is possible, and once we figure out the legal ramifications for it,  
[00:55:10] it seems quite plausible, even within your tenure that we figure that out. Are you  
[00:55:16] thinking about superhuman intelligence? Like, the biggest thing you do in your career is this?  
[00:55:21] You bring up another point. I know David Autor and others have talked a lot about this which is,  
[00:55:25] 60% of labor- I think the other question that needs to happen, let’s at least talk  
[00:55:29] about our democratic societies. I think that in order to have a stable social structure,  
[00:55:35] and democracies function, you can’t just have a return on capital and no return on labor. We can  
[00:55:42] talk about it, but that 60% has to be revalued. In my own simple way, maybe you can call it naive,  
[00:55:54] we'll start valuing different types of human labor. What is today considered  
[00:56:01] high-value human labor may be a commodity. There may be new things that we will value.  
[00:56:08] Including that person who comes to me and helps me with my physical therapy or whatever,  
[00:56:16] whatever is going to be the case that we value, but ultimately, if we don't have return on labor,  
[00:56:22] and there's meaning in work and dignity in work and all of that, that's another rate limiter  
[00:56:28] to any of these things being deployed. On the alignment side, two years ago,  
[00:56:32] you guys released Sydney Bing. Just to be clear, I think given the level of capabilities at the time,  
[00:56:37] it was a charming, endearing, kind of funny example of misalignment.  
[00:56:43] But that was because, at the time, it was like chatbots. They can go think for 30 seconds and  
[00:56:47] give you some funny or inappropriate response. But if you think about that kind of system--that,  
[00:56:58] I think to a New York Times reporter, tried to get him to leave his wife or something--if  
[00:57:02] you think about that going forward, and you have these agents that are for hours, weeks,  
[00:57:07] months going forward, just like autonomous swarms of AGIs, who could be in similar ways misaligned  
[00:57:14] and screwing stuff up, maybe coordinating with each other, what's your plan going forward so  
[00:57:23] that when you get the big one, you get it right? That is correct. That's one of the reasons why  
[00:57:32] when we usually allocate compute, let's allocate compute for what is that alignment challenge?  
[00:57:37] And then more importantly, what is the runtime environment in which you are really going  
[00:57:41] to be able to monitor these things? The observability around it? We do deal with  
[00:57:48] a lot of these things today in the classical side of things as well, like cyber. We don't  
[00:57:53] just write software and then just let it go. You have software and then you monitor it.  
[00:57:58] You monitor it for cyber attacks, you monitor it for fault injections, and what have you.  
[00:58:05] Therefore, I think we will have to build enough software engineering around the  
[00:58:09] deployment side of these, and then inside the model itself, what's the alignment? These are all,  
[00:58:15] some of them are real science problems. Some of them are real engineering problems,  
[00:58:19] and then we will have to tackle it. That also means taking our own  
[00:58:26] liability in all of this. So that's why I'm more interested in deploying these things in  
[00:58:30] where you can actually govern what the scope of these things is, and the scale of these things  
[00:58:36] is. You just can't unleash something out there in the world that creates harm, because the social  
[00:58:43] permission for that is not going to be there. When you get the agents that can really just do  
[00:58:51] weeks worth of tasks for you, what is the minimum assurance you want  
[00:58:56] before you can let it run a random Fortune 500? I think when I use something like Deep Research,  
[00:59:01] even, the minimum assurance I think we want is before we especially have  
[00:59:08] physical embodiment of anything, that I think is kind of one of those thresholds,  
[00:59:11] when you cross. That might be one place. Then the other one is, for example,  
[00:59:17] the permissions of the runtime environment in which this is operating. You may want guarantees  
[00:59:27] that it's sandboxed, it is not going out of that sandbox.  
[00:59:32] I mean, we already have web search and we already have it out of the sandbox.  
[00:59:37] But even what it does with web search and what it writes -- for example to your point,  
[00:59:45] if it's just going to write a bunch of code in order to do some computation,  
[00:59:49] where is that code deployed? And is that code ephemeral for just creating that output,  
[00:59:57] versus just going and springing that code out into the world?  
[01:00:01] Those are things that you could, in the action space, actually go control.  
[01:00:06] And separate from the safety issues, as you think about your own product suite, and you think about,  
[01:00:11] if you do have AIs this powerful, at some point, it's not just like Copilot- an example  
[01:00:18] you mentioned about how you were prepping for this podcast- it's more similar to how  
[01:00:21] you actually delegate work to your colleagues. What does it look like, given your current suite,  
[01:00:27] to add that in? I mean, there's one question about whether LLMs get commodified by other things.  
[01:00:34] I wonder if these databases or canvases or Excel sheets or whatever -- if the LLM is your  
[01:00:41] main gate point into accessing all these things, is it possible that the LLMs commodify Office?  
[01:00:49] It's an interesting one. The way I think about the first phase, at least, would be:  
[01:00:56] Can the LLM help me do my knowledge work using all of these tools or canvases more effectively?  
[01:01:05] One of the best demos that I've seen is a doctor getting ready for a tumor board workflow. She's  
[01:01:15] going into a tumor board meeting, and the first thing she uses Copilot for is to create an agenda  
[01:01:22] for the meeting because the LLM helps reason about all the cases, which are in some SharePoint site.  
[01:01:29] It says, "Hey, these cases -- obviously, a tumor board meeting is a high-stakes meeting where you  
[01:01:34] want to be mindful of the differences in cases so that you can then allocate the right time."  
[01:01:40] Even that reasoning task of creating an agenda that knows how to split time- super. So, I use  
[01:01:46] the LLM to do that. Then I go into the meeting, I'm in a Teams call with all my colleagues. I'm  
[01:01:53] focused on the actual case versus taking notes, because you now have this AI copilot doing a full  
[01:01:59] transcription of all of this. It's not just a transcript, but a database entry of what is in  
[01:02:08] the meeting that is recallable for all time. Then she comes out of the meeting, having  
[01:02:15] discussed the case and not been distracted by note-taking. She's a teaching doctor;  
[01:02:20] she wants to go and prep for her class. And so she goes into Copilot and says, "Take my tumor board  
[01:02:27] meeting and create a PowerPoint slide deck out of it so that I can talk to my students about it."  
[01:02:35] So that’s the type. The UI and the scaffolding that I have are canvases that are now getting  
[01:02:42] populated using LLMs. And the workflow itself is being reshaped; knowledge work is getting done.  
[01:02:51] Here's an interesting thing: If someone came to me in the late '80s and said, "You're going to have  
[01:02:58] a million documents on your desk," I would say, "What the heck is that?" I would have literally  
[01:03:05] thought there was going to be a million physical copies of things on my desk. Except, we do have a  
[01:03:11] million spreadsheets and a million documents. I don’t, you do.  
[01:03:16] They're all there. And so, that's what's going to happen with even agents. There  
[01:03:20] will be a UI layer. To me, Office is not just about the office of today; it's the  
[01:03:25] UI layer for knowledge work. It'll evolve as the workflows evolve. That's what we want to build.  
[01:03:31] I do think the SaaS applications that exist today, these CRUD applications,  
[01:03:36] are going to fundamentally be changed because the business logic will go more into this agentic  
[01:03:42] tier. In fact, one of the other cool things today in my Copilot experience is when I say,  
[01:03:47] "Hey, I'm getting ready for a meeting with a customer," I just go and say,  
[01:03:50] "Give me all the notes for it that I should know." It pulls from my CRM database, it pulls  
[01:03:56] from my Microsoft Graph, creates a composite, essentially artifact, and then it applies even  
[01:04:04] logic on it. That, to me, is going to transform the SaaS applications as we know of it today.  
[01:04:11] SaaS as an industry might be worth hundreds of billions to trillions of dollars a year,  
[01:04:15] depending on how you count. If really that can just get collapsed by AI,  
[01:04:22] is the next step up in your next decade 10X-ing the market cap of Microsoft again? Because you're  
[01:04:28] talking about trillions of dollars... It would also create a lot of value in  
[01:04:32] the SaaS. One thing we don't pay as much attention to perhaps is the amount of IT  
[01:04:42] backlog there is in the world. These code gen things, plus the  
[01:04:50] fact that I can interrogate all of your SaaS applications using agents and get more utility  
[01:04:56] will be the greatest explosion of apps, they'll be called agents, so that for every vertical,  
[01:05:05] in every industry, in every category, we're suddenly going to have the ability to be serviced.  
[01:05:12] So there's going to be a lot of value. You can't stay still. You can't just say the old thing of,  
[01:05:17] "Oh, I schematized some narrow business process, and I have a UI in the browser,  
[01:05:21] and that's my thing." That's ain’t going to be the case. You have to go up-stack and say,  
[01:05:27] "What's the task that I have to participate in?" You will want to be able to take your SaaS  
[01:05:33] application and make it a fantastic agent that participates in a multi-agent world.  
[01:05:39] As long as you can do that, then I think you can even increase the value.  
[01:05:43] Can I ask you some questions about your time at Microsoft?  
[01:05:46] Yeah. Is being a company  
[01:05:48] man underrated? So you've spent most of your career at Microsoft, and you could say that one  
[01:05:54] of the reasons you've been able to add so much value is you've seen the culture, the history,  
[01:05:58] and the technology. You have all this context by rising up through the ranks. Should more companies  
[01:06:02] be run by people who have this level of context? That's a great question. I've  
[01:06:05] not thought about it that way. Through my 34 years now of Microsoft,  
[01:06:18] each year I felt more excited about being at Microsoft versus thinking that, oh, I'm a company  
[01:06:24] person or what have you. I take that seriously, even for anybody joining Microsoft. It's not like  
[01:06:34] they're joining Microsoft as long as they feel that they can use this as a platform for their  
[01:06:39] both economic return, but also a sense of purpose and a sense of mission that they can accomplish by  
[01:06:46] using us as a platform. That's the contract. So I think yes, companies have to create a  
[01:06:53] culture that allows people to come in and become company people like me. Microsoft  
[01:07:00] got it more right than wrong, at least in my case, and I hope that remains the case.  
[01:07:07] The sixth CEO that you’re talking about, who’ll get to use the research you’re starting now,  
[01:07:12] what are you doing to retain the future Satya Nadellas so that they're  
[01:07:15] in a position to become future leaders? It's fascinating. This is our 50th year,  
[01:07:19] and I think a lot about it. The way to think about it is, longevity is not a goal; relevance is.  
[01:07:32] The thing that I have to do and all 200,000 of us have to do every day is: Are we doing things  
[01:07:38] that are useful and relevant for the world as we see it evolving, not just today, but tomorrow?  
[01:07:48] We live in an industry where there's no franchise value, so that’s the other hard part. If you take  
[01:07:55] the R&D budget that we will spend this year, it’s all speculation on what's going to happen  
[01:08:02] five years from now. You have to basically go in with that attitude, saying, "We are doing  
[01:08:08] things that we think are going to be relevant." So that's what you have to focus on. Then know  
[01:08:14] that there's a batting average, and you're not going to get- you have to have a high tolerance  
[01:08:17] for failure. You have to take enough shots on goal to be able to say, "Okay,  
[01:08:29] we will make it to the other side as a company." That's what makes it tricky in this industry.  
[01:08:35] Speaking of- you just mentioned that you're two months away from your 50th  
[01:08:39] anniversary of Microsoft’s founding. If you look at the top 10 companies by market cap,  
[01:08:45] or top 5, basically, everybody else but Microsoft is younger than Microsoft. It's  
[01:08:52] an interesting observation about why the most successful companies often  
[01:08:56] are quite young. The average Fortune 500 company will last 10 to 15 years.  
[01:09:02] What has Microsoft done to remain relevant for this many years? How do you keep refounding?  
[01:09:11] I love that, Reed Hoffman uses that term, "refounding." That's the mindset. People  
[01:09:16] talk about founder mode, but for us mere mortal CEOs, it's more like refounder mode.  
[01:09:28] To be able to see things again in a fresh way is the key. To your question: can we culturally  
[01:09:40] create an environment where refounding becomes a habit thing? Every day we come in and say,  
[01:09:48] "We feel we have a stake in this place to be able to change the core assumptions of what  
[01:09:55] we do and how we relate to the world around us. Do we give ourselves permission?” I think many times,  
[01:10:01] companies feel over-constrained by either business model or whatever. You just have  
[01:10:06] to unconstrain yourself. If you did leave Microsoft,  
[01:10:09] what company would you start? Company I would start? Man.  
[01:10:15] That’s where the company man and me sort of says, “I'll never leave Microsoft.”  
[01:10:21] If I were thinking of doing something, I think picking a domain that has... When I look at the  
[01:10:32] dream of tech, we've always said technology is about the biggest, greatest democratizing force.  
[01:10:39] I feel like finally, we have that ability. If you say those tokens per dollar per watt  
[01:10:49] is what we can generate, I would love to find some domain in which that can  
[01:10:56] be applied, where it is so underserved. That's where healthcare, education...  
[01:11:03] Public sector would be another place. If you take those domains, which are the underserved places,  
[01:11:13] where my life as a citizen of this country or a member of this society or anywhere, would I  
[01:11:19] be better off if somehow all this abundance translated into better healthcare, better  
[01:11:24] education, and better public sector institutions serving me as a citizen? That would be a place.  
[01:11:32] One thing I'm not sure about, hearing your answers on different questions,  
[01:11:35] is whether you think AGI is a thing. Will there be a thing which automates all cognitive labor,  
[01:11:44] like anything anybody can do on a computer? This is where I have a problem with the  
[01:11:48] definitions of how people talk about it. Cognitive labor is not a static thing. There is cognitive  
[01:11:55] labor today. If I have an inbox that is managing all my agents, is that new cognitive labor?  
[01:12:07] Today's cognitive labor may be automated. What about the new cognitive labor that  
[01:12:12] gets created? Both of those things have to be thought of, which is the shifting…  
[01:12:18] That's why I make this distinction, at least in my head: Don't conflate knowledge worker  
[01:12:24] with knowledge work. The knowledge work of today could probably be automated.  
[01:12:32] Who said my life's goal is to triage my email? Let an AI agent triage my email.  
[01:12:40] But after having triaged my email, give me a higher-level cognitive labor task of, "Hey,  
[01:12:45] these are the three drafts I really want you to review." That's a different abstraction.  
[01:12:50] But will AI ever get to the second thing? It may, but as soon as it gets to that  
[01:12:54] second thing, there will be a third thing. Why are we thinking that somehow, when we  
[01:13:01] have dealt with tools that have changed what cognitive labor is in history, why are we  
[01:13:07] worried that all cognitive labor will go away? I'm sure you've heard these examples before, but  
[01:13:15] the idea that horses can still be good for certain things, there are certain terrains you can't take  
[01:13:19] a car on. But the idea that you're going to see horses around the street, they’re going to employ  
[01:13:23] millions of horses, it’s just not happening. And then the idea is, could a similar  
[01:13:27] thing happen with humans? But in one very narrow dimension?  
[01:13:31] It's only 200 years of history of humans where we have valued some narrow sort of things called  
[01:13:37] "cognitive labor" as we understand it. Let's take something like chemistry. If  
[01:13:43] this thing, quantum plus AI really helped us do a lot of novel material science and so on,  
[01:13:50] that's fantastic to have novel material science being done by it. Does that take away from  
[01:13:57] all the other things that humans can do? Why can't we exist in a world where there  
[01:14:05] are powerful cognitive machines, knowing that our cognitive agency has not been taken away?  
[01:14:15] I'll ask this question, not about you, but in a different scenario, so maybe you can answer it  
[01:14:20] without embarrassment. Suppose on the Microsoft board, could you ever see adding an AI to the  
[01:14:24] board? Could it ever have the judgment, context, and holistic understanding to be a useful advisor?  
[01:14:34] It's a great example. One of the things we added was a facilitator agent in Teams. The goal there,  
[01:14:40] it's in the early stages, is can that facilitator agent use long-term memory, not just on the  
[01:14:47] context of the meeting, but with the context of projects I'm working on, and the team,  
[01:14:53] and what have you, be a great facilitator? I would love it even in a board meeting,  
[01:14:58] where it's easy to get distracted. After all, board members come once a quarter, and they're  
[01:15:02] trying to digest what is happening with a complex company like Microsoft. A facilitator agent that  
[01:15:11] actually helped human beings all stay on topic and focus on the issues that matter, that's fantastic.  
[01:15:20] That's kind of literally having, to your point about even going back to your previous question,  
[01:15:24] having something that has infinite memory that can even help us. You know, after all,  
[01:15:30] what is that Herbert Simon thing? We are all bounded rationality. So if the bounded rationality  
[01:15:37] of humans can actually be dealt with because there is a cognitive amplifier outside, that's great.  
[01:15:46] Speaking of materials and chemistry stuff, I think you said recently that you want the  
[01:15:51] next 250 years of progress in those fields to happen in the next 25 years. Now, when I  
[01:15:57] think about what's going to be possible in the next 250 years, I'm thinking like space travel,  
[01:16:01] and space elevators, and immortality, and curing all diseases. Next 25 years, you think?  
[01:16:09] One of the reasons why I brought that up was, I love that thing of, the industrial revolution was  
[01:16:15] the 250 years. We have to take this entire change from a carbon-based system to something different.  
[01:16:24] That means you have to fundamentally reinvent all of what has happened with chemistry over  
[01:16:29] the last 250 years. That's where I hope we have this quantum computer, this quantum computer  
[01:16:34] helps us get to new materials, and then we can fabricate those new materials that help us with  
[01:16:39] all of the challenges we have on this planet. And then I'm all for interplanetary travel.  
[01:16:45] Amazing. Satya, thank you so much for your time. Thank you so much. It's wonderful. Thanks.  
[01:16:48] Great, thank you.  
