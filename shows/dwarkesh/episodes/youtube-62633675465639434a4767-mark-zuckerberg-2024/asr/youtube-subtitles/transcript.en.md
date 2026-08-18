# Mark Zuckerberg — Llama 3, $10B models, Caesar Augustus, & 1 GW datacenters

[00:00:00] That's not even a question for me - whether we're going to go take a swing at building  
[00:00:03] the next thing. I'm just incapable of not doing that. There's a bunch of times when we wanted to  
[00:00:08] launch features and then Apple's just like nope you're not launching that I was like  
[00:00:12] that sucks. Are we set up for that with AI where you're going to get a handful of companies that  
[00:00:19] run these closed models that are going to be in control of the apis and therefore are going to be  
[00:00:22] able to tell you what you can build? Then when you start getting into building a data center  
[00:00:27] that's like 300 Megawatts or 500 Megawatts or a Gigawatt - just no one has built a single Gigawatt  
[00:00:33] data center yet. From wherever you sit there's going to be some actor who you don't trust - if  
[00:00:37] they're the ones who have the super strong AI I think that that's potentially a much bigger risk  
[00:00:43] Mark, welcome to the podcast. Thanks for having me. Big fan of your podcast.  
[00:00:47] Thank you, that's very nice of you to say. Let's start by talking about the releases  
[00:00:52] that will go out when this interview goes out. Tell me about the models and  
[00:00:57] Meta AI. What’s new and exciting about them? I think the main thing that most people in the  
[00:01:02] world are going to see is the new version of Meta AI. The most important thing that we're  
[00:01:08] doing is the upgrade to the model. We're rolling out Llama-3. We're doing it both  
[00:01:12] as open source for the dev community and it is now going to be powering Meta AI. There's a lot  
[00:01:19] that I'm sure we'll get into around Llama-3, but I think the bottom line on this is that  
[00:01:24] we think now that Meta AI is the most intelligent, freely-available AI assistant that people can use.  
[00:01:30] We're also integrating Google and Bing for real-time knowledge.  
[00:01:34] We're going to make it a lot more prominent across our apps. At the top of Facebook and Messenger,  
[00:01:42] you'll be able to just use the search box right there to ask any question. There's a bunch of new  
[00:01:48] creation features that we added that I think are pretty cool and that I think people will enjoy.  
[00:01:54] I think animations is a good one. You can basically take any image and just animate it.  
[00:02:00] One that people are going to find pretty wild is that it now generates high quality images  
[00:02:07] so quickly that it actually generates it as you're typing and updates it in real time.  
[00:02:12] So you're typing your query and it's honing in. It’s like “show me a picture of a cow in  
[00:02:21] a field with mountains in the background, eating macadamia nuts, drinking beer” and it's updating  
[00:02:29] the image in real time. It's pretty wild. I think people are going to enjoy that. So I  
[00:02:35] think that's what most people are going to see in the world. We're rolling that out, not everywhere,  
[00:02:39] but we're starting in a handful of countries and we'll do more over the coming weeks and months.  
[00:02:46] I think that’s going to be a pretty big deal and I'm really excited to get that in people's  
[00:02:50] hands. It's a big step forward for Meta AI. But I think if you want to get under the hood  
[00:02:57] a bit, the Llama-3 stuff is obviously the most technically interesting. We're training three  
[00:03:05] versions: an 8 billion parameter model and a 70 billion, which we're releasing today, and a 405  
[00:03:11] billion dense model, which is still training. So we're not releasing that today, but I'm pretty  
[00:03:20] excited about how the 8B and the 70B turned out. They're leading for their scale. We'll release a  
[00:03:31] blog post with all the benchmarks so people can check it out themselves. Obviously it's open  
[00:03:34] source so people get a chance to play with it. We have a roadmap of new releases coming that  
[00:03:41] are going to bring multimodality, more multi-linguality, and bigger context  
[00:03:46] windows as well. Hopefully, sometime later in the year we'll get to roll out the 405B. For where it  
[00:03:59] is right now in training, it is already at around 85 MMLU and we expect that it's  
[00:04:09] going to have leading benchmarks on a bunch of the benchmarks. I'm pretty excited about all of that.  
[00:04:14] The 70 billion is great too. We're releasing that today. It's around 82 MMLU and has leading scores  
[00:04:22] on math and reasoning. I think just getting this in people's hands is going to be pretty wild.  
[00:04:26] Oh, interesting. That's the first I’m hearing of it as a benchmark. That's super impressive.  
[00:04:30] The 8 billion is nearly as powerful as the biggest version of Llama-2 that we released.  
[00:04:38] So the smallest Llama-3 is basically as powerful as the biggest Llama-2.  
[00:04:43] Before we dig into these models, I want to go back in time. I'm assuming 2022 is when you  
[00:04:49] started acquiring these H100s, or you can tell me when. The stock price is getting hammered. People  
[00:04:56] are asking what's happening with all this capex. People aren't buying the metaverse.  
[00:05:00] Presumably you're spending that capex to get these H100s. How did you know back then to get the  
[00:05:04] H100s? How did you know that you’d need the GPUs? I think it was because we were working on Reels.  
[00:05:14] We always want to have enough capacity to build something that we can't quite see on the horizon  
[00:05:23] yet. We got into this position with Reels where we needed more GPUs to train the models. It was this  
[00:05:31] big evolution for our services. Instead of just ranking content from people or pages you follow,  
[00:05:41] we made this big push to start recommending what we call unconnected content, content from people  
[00:05:49] or pages that you're not following. The corpus of content candidates that  
[00:05:56] we could potentially show you expanded from on the order of thousands to on the order of  
[00:06:01] hundreds of millions. It needed a completely different infrastructure. We started working  
[00:06:08] on doing that and we were constrained on the infrastructure in catching up to what  
[00:06:14] TikTok was doing as quickly as we wanted to. I basically looked at that and I was like “hey,  
[00:06:19] we have to make sure that we're never in this situation again. So let's order enough GPUs to do  
[00:06:25] what we need to do on Reels and ranking content and feed. But let's also double that.” Again,  
[00:06:31] our normal principle is that there's going to be something on the horizon that we can't see yet.  
[00:06:35] Did you know it would be AI? We thought it was going to be something that  
[00:06:40] had to do with training large models. At the time I thought it was probably going to be something  
[00:06:44] that had to do with content. It’s just the pattern matching of running the company, there's always  
[00:06:52] another thing. At that time I was so deep into trying to get the recommendations working for  
[00:07:00] Reels and other content. That’s just such a big unlock for Instagram and Facebook now, being  
[00:07:05] able to show people content that's interesting to them from people that they're not even following.  
[00:07:09] But that ended up being a very good decision in retrospect. And it came from being behind.  
[00:07:18] It wasn't like “oh, I was so far ahead.” Actually, most of the times where we make  
[00:07:25] some decision that ends up seeming good is because we messed something up before  
[00:07:29] and just didn't want to repeat the mistake. This is a total detour, but I want to ask  
[00:07:32] about this while we're on this. We'll get back to AI in a second. In 2006 you didn't sell for  
[00:07:37] $1 billion but presumably there's some amount you would have sold for, right? Did you write down  
[00:07:41] in your head like “I think the actual valuation of Facebook at the time is this and they're not  
[00:07:45] actually getting the valuation right”? If they’d offered you $5 trillion, of course you would have  
[00:07:48] sold. So how did you think about that choice? I think some of these things are just personal.  
[00:07:58] I don't know that at the time I was sophisticated enough to do that analysis. I had all these people  
[00:08:03] around me who were making all these arguments for a billion dollars like “here's the revenue that  
[00:08:10] we need to make and here's how big we need to be. It's clearly so many years in the future.” It was  
[00:08:16] very far ahead of where we were at the time. I didn't really have the financial sophistication  
[00:08:23] to really engage with that kind of debate. Deep down I believed in what we were doing.  
[00:08:30] I did some analysis like “what would I do if I weren’t doing this? Well, I really like building  
[00:08:40] things and I like helping people communicate. I like understanding what's going on with people and  
[00:08:46] the dynamics between people. So I think if I sold this company, I'd just go build another company  
[00:08:51] like this and I kind of like the one I have. So why?” I think a lot of the biggest bets that  
[00:09:03] people make are often just based on conviction and values. It's actually usually very hard to do the  
[00:09:12] analyses trying to connect the dots forward. You've had Facebook AI Research for a long  
[00:09:18] time. Now it's become seemingly central to your company. At what point did making AGI,  
[00:09:26] or however you consider that mission, become a key priority of what Meta is doing?  
[00:09:33] It's been a big deal for a while. We started FAIR about 10 years ago. The idea was that,  
[00:09:41] along the way to general intelligence or whatever you wanna call it, there are going to be all these  
[00:09:48] different innovations and that's going to just improve everything that we do. So we  
[00:09:52] didn't conceive of it as a product. It was more of a research group. Over the last 10  
[00:10:00] years it has created a lot of different things that have improved all of our products. It’s  
[00:10:07] advanced the field and allowed other people in the field to create things that have improved our  
[00:10:11] products too. I think that that's been great. There's obviously a big change in the last  
[00:10:17] few years with ChatGPT and the diffusion models around image creation coming out.  
[00:10:24] This is some pretty wild stuff that is pretty clearly going to affect how people  
[00:10:29] interact with every app that's out there. At that point we started a second group, the gen AI group,  
[00:10:40] with the goal of bringing that stuff into our products and building leading foundation models  
[00:10:46] that would power all these different products. When we started doing that the theory initially  
[00:10:54] was that a lot of the stuff we're doing is pretty social. It's helping people interact  
[00:11:01] with creators, helping people interact with businesses, helping businesses sell things or  
[00:11:07] do customer support. There’s also basic assistant functionality, whether it's for our apps or the  
[00:11:13] smart glasses or VR. So it wasn't completely clear at first that you were going to need full  
[00:11:24] AGI to be able to support those use cases. But in all these subtle ways, through working on them,  
[00:11:29] I think it's actually become clear that you do. For example, when we were working on Llama-2,  
[00:11:37] we didn't prioritize coding because people aren't going to ask Meta AI a lot of coding  
[00:11:42] questions in WhatsApp. Now they will, right?  
[00:11:44] I don't know. I'm not sure that WhatsApp, or Facebook or Instagram, is the UI where people are  
[00:11:47] going to be doing a lot of coding questions. Maybe the website, meta.ai, that we’re launching. But  
[00:12:00] the thing that has been a somewhat surprising result over the last 18 months is that it turns  
[00:12:08] out that coding is important for a lot of domains, not just coding. Even if people aren't asking  
[00:12:14] coding questions, training the models on coding helps them become more rigorous in answering the  
[00:12:21] question and helps them reason across a lot of different types of domains. That's one example  
[00:12:26] where for Llama-3, we really focused on training it with a lot of coding because that's going  
[00:12:30] to make it better on all these things even if people aren't asking primarily coding questions.  
[00:12:36] Reasoning is another example. Maybe you want to chat with a creator or you're a business and  
[00:12:43] you're trying to interact with a customer. That interaction is not just like “okay,  
[00:12:47] the person sends you a message and you just reply.” It's a multi-step interaction  
[00:12:53] where you're trying to think through “how do I accomplish the person's goals?” A lot of times  
[00:12:57] when a customer comes, they don't necessarily know exactly what they're looking for or how  
[00:13:01] to ask their questions. So it's not really the job of the AI to just respond to the question.  
[00:13:06] You need to kind of think about it more holistically. It really becomes  
[00:13:09] a reasoning problem. So if someone else solves reasoning, or makes good advances on reasoning,  
[00:13:14] and we're sitting here with a basic chat bot, then our product is lame compared to what other  
[00:13:19] people are building. At the end of the day, we basically realized we've got to solve general  
[00:13:26] intelligence and we just upped the ante and the investment to make sure that we could do that.  
[00:13:32] So the version of Llama that's going to solve all these use cases for users, is that the  
[00:13:41] version that will be powerful enough to replace a programmer you might have in this building?  
[00:13:46] I just think that all this stuff is going to be progressive over time.  
[00:13:49] But in the end case: Llama-10. I think that there's a lot baked  
[00:13:55] into that question. I'm not sure that we're replacing people as much as we’re giving  
[00:14:00] people tools to do more stuff. Is the programmer in this building  
[00:14:03] 10x more productive after Llama-10? I would hope more. I don't believe that  
[00:14:09] there's a single threshold of intelligence for humanity because people have different skills.  
[00:14:14] I think that at some point AI is probably going to surpass people at most of those things, depending  
[00:14:21] on how powerful the models are. But I think it's progressive and I don't think AGI is one thing.  
[00:14:29] You're basically adding different capabilities. Multimodality is a key one that we're focused on  
[00:14:34] now, initially with photos and images and text but eventually with videos. Because we're so focused  
[00:14:40] on the metaverse, 3D type stuff is important too. One modality that I'm pretty focused on,  
[00:14:46] that I haven't seen as many other people in the industry focus on, is emotional understanding. So  
[00:14:54] much of the human brain is just dedicated to understanding people and understanding  
[00:15:00] expressions and emotions. I think that's its own whole modality, right? You could  
[00:15:06] say that maybe it's just video or image, but it's clearly a very specialized version of those two.  
[00:15:10] So there are all these different capabilities that you want to train the models to focus  
[00:15:17] on, in addition to getting a lot better at reasoning and memory, which is its own whole  
[00:15:22] thing. I don't think in the future we're going to be primarily shoving things into a query context  
[00:15:29] window to ask more complicated questions. There will be different stores of memory or different  
[00:15:35] custom models that are more personalized to people. These are all just different capabilities.  
[00:15:42] Obviously then there’s making them big and small. We care about both. If you're running something  
[00:15:47] like Meta AI, that's pretty server-based. We also want it running on smart glasses and there's not  
[00:15:55] a lot of space in smart glasses. So you want to have something that's very efficient for that.  
[00:16:01] If you're doing $10Bs worth of inference or even eventually $100Bs,  
[00:16:06] if you're using intelligence in an industrial scale what is the use case? Is it simulations?  
[00:16:11] Is it the AIs that will be in the metaverse? What will we be using the data centers for?  
[00:16:19] Our bet is that it's going to basically change all of the products. I think that there's going  
[00:16:24] to be a kind of Meta AI general assistant product. I think that that will shift from  
[00:16:32] something that feels more like a chatbot, where you ask a question and it formulates an answer,  
[00:16:37] to things where you're giving it more complicated tasks and then it goes away and does them. That's  
[00:16:43] going to take a lot of inference and it's going to take a lot of compute in other ways too.  
[00:16:48] Then I think interacting with other agents for other people is going to be a big part of what  
[00:16:56] we do, whether it's for businesses or creators. A big part of my theory on this is that there's not  
[00:17:02] going to be just one singular AI that you interact with. Every business is going to want an AI that  
[00:17:09] represents their interests. They're not going to want to primarily interact with you through an AI  
[00:17:13] that is going to sell their competitors’ products. I think creators is going to be a big one. There  
[00:17:25] are about 200 million creators on our platforms. They basically all have the pattern where they  
[00:17:31] want to engage their community but they're limited by the hours in the day. Their community generally  
[00:17:35] wants to engage them, but they don't know that they're limited by the hours in the day. If  
[00:17:40] you could create something where that creator can basically own the AI, train it in the way  
[00:17:47] they want, and engage their community, I think that's going to be super powerful. There's going  
[00:17:55] to be a ton of engagement across all these things. These are just the consumer use cases. My wife and  
[00:18:04] I run our foundation, Chan Zuckerberg Initiative. We're doing a bunch of stuff on science and  
[00:18:12] there's obviously a lot of AI work that is going to advance science and healthcare and all these  
[00:18:17] things. So it will end up affecting basically every area of the products and the economy.  
[00:18:25] You mentioned AI that can just go out and do something for you that's multi-step. Is that  
[00:18:30] a bigger model? With Llama-4 for example, will there still be a version that's 70B but you'll  
[00:18:36] just train it on the right data and that will be super powerful? What does the progression  
[00:18:40] look like? Is it scaling? Is it just the same size but different banks like you were talking about?  
[00:18:49] I don't know that we know the answer to that. I think one thing that seems to be a pattern is that  
[00:18:56] you have the Llama model and then you build some kind of other application specific code around it.  
[00:19:06] Some of it is the fine-tuning for the use case, but some of it is, for example, logic for how  
[00:19:14] Meta AI should work with tools like Google or Bing to bring in real-time knowledge. That's not part  
[00:19:21] of the base Llama model. For Llama-2, we had some of that and it was a little more hand-engineered.  
[00:19:30] Part of our goal for Llama-3 was to bring more of that into the model itself. For Llama-3,  
[00:19:36] as we start getting into more of these agent-like behaviors, I think some of that is going to be  
[00:19:41] more hand-engineered. Our goal for Llama-4 will be to bring more of that into the model.  
[00:19:48] At each step along the way you have a sense of what's going to be possible on the horizon. You  
[00:19:54] start messing with it and hacking around it. I think that helps you then hone your intuition  
[00:19:59] for what you want to try to train into the next version of the model itself. That makes it more  
[00:20:04] general because obviously for anything that you're hand-coding you can unlock some use cases, but  
[00:20:10] it's just inherently brittle and non-general. When you say “into the model itself,” you train it  
[00:21:21] on the thing that you want in the model itself? What do you mean by “into the model itself”?  
[00:21:33] For Llama- 2, the tool use was very specific, whereas Llama-3 has much better tool use. We  
[00:21:41] don't have to hand code all the stuff to have it use Google and go do a search. It can just do  
[00:21:49] that. Similarly for coding and running code and a bunch of stuff like that. Once you kind of get  
[00:22:00] that capability, then you get a peek at what we can start doing next. We don't necessarily want  
[00:22:06] to wait until Llama-4 is around to start building those capabilities, so we can start hacking around  
[00:22:10] it. You do a bunch of hand coding and that makes the products better, if only for the  
[00:22:16] interim. That helps show the way then of what we want to build into the next version of the model.  
[00:22:21] What is the community fine tune of Llama-3 that you're most excited for? Maybe not the  
[00:22:25] one that will be most useful to you, but the one you'll just enjoy playing with the most.  
[00:22:29] They fine-tune it on antiquity and you'll just be talking to Virgil  
[00:22:32] or something. What are you excited about? I think the nature of the stuff is that you  
[00:22:39] get surprised. Any specific thing that I thought would be valuable, we'd probably be building. I  
[00:22:53] think you'll get distilled versions. I think you'll get smaller versions. One  
[00:22:58] thing is that I think 8B isn’t quite small enough for a bunch of use cases. Over time I'd  
[00:23:07] love to get a 1-2B parameter model, or even a 500M parameter model and see what you can do with that.  
[00:23:18] If with 8B parameters we’re nearly as powerful as the largest Llama-2 model,  
[00:23:23] then with a billion parameters you should be able to do something that's interesting, and faster.  
[00:23:28] It’d be good for classification, or a lot of basic things that people do before understanding  
[00:23:35] the intent of a user query and feeding it to the most powerful model to hone in on  
[00:23:41] what the prompt should be. I think that's one thing that maybe the community can help fill  
[00:23:46] in. We're also thinking about getting around to distilling some of these ourselves but right now  
[00:23:52] the GPUs are pegged training the 405B. So you have all these GPUs. I think you  
[00:24:00] said 350,000 by the end of the year. That's the whole fleet. We built two,  
[00:24:06] I think 22,000 or 24,000 clusters that are the single clusters that we have for training the big  
[00:24:13] models, obviously across a lot of the stuff that we do. A lot of our stuff goes towards training  
[00:24:18] Reels models and Facebook News Feed and Instagram Feed. Inference is a huge thing for us because we  
[00:24:24] serve a ton of people. Our ratio of inference compute required to training is probably much  
[00:24:33] higher than most other companies that are doing this stuff just because of the sheer volume of  
[00:24:37] the community that we're serving. In the material they shared with  
[00:24:41] me before, it was really interesting that you trained it on more data than is compute optimal  
[00:24:45] just for training. The inference is such a big deal for you guys, and also for the community,  
[00:24:49] that it makes sense to just have this thing and have trillions of tokens in there.  
[00:24:53] Although one of the interesting things about it, even with the 70B,  
[00:24:57] is that we thought it would get more saturated. We trained it on around 15 trillion tokens. I guess  
[00:25:06] our prediction going in was that it was going to asymptote more, but even by the end it was  
[00:25:12] still learning. We probably could have fed it more tokens and it would have gotten somewhat better.  
[00:25:19] At some point you're running a company and you need to do these meta reasoning questions. Do I  
[00:25:24] want to spend our GPUs on training the 70B model further? Do we want to get on with it so we can  
[00:25:31] start testing hypotheses for Llama-4? We needed to make that call and I think we got a reasonable  
[00:25:39] balance for this version of the 70B. There'll be others in the future, the 70B multimodal one,  
[00:25:45] that'll come over the next period. But that was fascinating that the architectures at  
[00:25:53] this point can just take so much data. That's really interesting. What does this  
[00:25:57] imply about future models? You mentioned that the Llama-3 8B is better than the Llama-2 70B.  
[00:26:03] No, no, it's nearly as good. I don’t want to overstate  
[00:26:06] it. It’s in a similar order of magnitude. Does that mean the Llama-4 70B will be  
[00:26:10] as good as the Llama-3 405B? What does the future of this look like?  
[00:26:14] This is one of the great questions, right? I think no one knows. One of the trickiest things in the  
[00:26:22] world to plan around is an exponential curve. How long does it keep going for?  
[00:26:29] I think it's likely enough that we'll keep going. I think it’s worth investing the $10Bs or $100B+  
[00:26:37] in building the infrastructure and assuming that if it keeps going you're going to get some really  
[00:26:43] amazing things that are going to make amazing products. I don't think anyone in the industry  
[00:26:49] can really tell you that it will continue scaling at that rate for sure. In general in history,  
[00:26:56] you hit bottlenecks at certain points. Now there's so much energy on this that  
[00:27:01] maybe those bottlenecks get knocked over pretty quickly. I think that’s an interesting question.  
[00:27:08] What does the world look like where there aren't these bottlenecks? Suppose progress just continues  
[00:27:13] at this pace, which seems plausible. Zooming out and forgetting about Llamas…  
[00:27:18] Well, there are going to be different bottlenecks. Over the last few years, I think there was this  
[00:27:28] issue of GPU production. Even companies that had the money to pay for the GPUs couldn't necessarily  
[00:27:39] get as many as they wanted because there were all these supply constraints. Now I think that's sort  
[00:27:44] of getting less. So you're seeing a bunch of companies thinking now about investing a lot  
[00:27:52] of money in building out these things. I think that that will go on for some period of time.  
[00:28:00] There is a capital question. At what point does it stop being worth it to put the capital in?  
[00:28:06] I actually think before we hit that, you're going to run into energy constraints. I don't  
[00:28:14] think anyone's built a gigawatt single training cluster yet. You run into these things that just  
[00:28:21] end up being slower in the world. Getting energy permitted is a very heavily regulated government  
[00:28:30] function. You're going from software, which is somewhat regulated and I'd argue it’s more  
[00:28:37] regulated than a lot of people in the tech community feel. Obviously it’s different if  
[00:28:42] you're starting a small company, maybe you feel that less. We interact with different  
[00:28:47] governments and regulators and we have lots of rules that we need to follow and make sure  
[00:28:53] we do a good job with around the world. But I think that there's no doubt about energy.  
[00:28:59] If you're talking about building large new power plants or large build-outs and then  
[00:29:04] building transmission lines that cross other private or public land, that’s just a heavily  
[00:29:11] regulated thing. You're talking about many years of lead time. If we wanted to stand up  
[00:29:17] some massive facility, powering that is a very long-term project. I think people do it but I  
[00:29:31] don't think this is something that can be quite as magical as just getting to a level of AI,  
[00:29:36] getting a bunch of capital and putting it in, and then all of a sudden the models are just going to…  
[00:29:42] You do hit different bottlenecks along the way. Is there something, maybe an AI-related project or  
[00:29:47] maybe not, that even a company like Meta doesn't have the resources for? Something where if your  
[00:29:51] R&D budget or capex budget were 10x what it is now, then you could pursue it? Something that’s  
[00:29:56] in the back of your mind but with Meta today, you can't even issue stock or bonds for it?  
[00:30:01] It's just like 10x bigger than your budget? I think energy is one piece. I think we  
[00:30:07] would probably build out bigger clusters than we currently can if we could get the energy to do it.  
[00:30:18] That's fundamentally money-bottlenecked in the limit? If you had $1 trillion…  
[00:30:23] I think it’s time. It depends on how far the exponential curves go. Right now a lot of  
[00:30:36] data centers are on the order of 50 megawatts or 100MW, or a big one might be 150MW. Take a whole  
[00:30:42] data center and fill it up with all the stuff that you need to do for training and you build  
[00:30:46] the biggest cluster you can. I think a bunch of companies are running at stuff like that.  
[00:30:53] But when you start getting into building a data center that's like 300MW or 500MW or 1 GW,  
[00:31:04] no one has built a 1GW data center yet. I think it will happen. This is only a matter of time but  
[00:31:09] it's not going to be next year. Some of these things will take some number of years to build  
[00:31:18] out. Just to put this in perspective, I think a gigawatt would be the size of a meaningful nuclear  
[00:31:31] power plant only going towards training a model. Didn't Amazon do this? They have a 950MW–  
[00:31:39] I'm not exactly sure what they did. You'd have to ask them.  
[00:31:44] But it doesn’t have to be in the same place, right? If distributed  
[00:31:45] training works, it can be distributed. Well, I think that is a big question, how  
[00:31:49] that's going to work. It seems quite possible that in the future, more of what we call training for  
[00:31:56] these big models is actually more along the lines of inference generating synthetic data to then go  
[00:32:05] feed into the model. I don't know what that ratio is going to be but I consider the generation of  
[00:32:11] synthetic data to be more inference than training today. Obviously if you're doing it in order  
[00:32:16] to train a model, it's part of the broader training process. So that's an open question,  
[00:32:24] the balance of that and how that plays out. Would that potentially also be the case with  
[00:32:30] Llama-3, and maybe Llama-4 onwards? As in, you put this out and if somebody has a ton of compute,  
[00:32:36] then they can just keep making these things arbitrarily smarter using the models that  
[00:32:37] you've put out. Let’s say there’s some random country, like Kuwait or the UAE,  
[00:32:43] that has a ton of compute and they can actually just use Llama-4 to make something much smarter.  
[00:32:52] I do think there are going to be dynamics like that, but I also think  
[00:32:59] there is a fundamental limitation on the model architecture. I think like a 70B model that we  
[00:33:13] trained with a Llama-3 architecture can get better, it can keep going. As I was saying,  
[00:33:18] we felt that if we kept on feeding it more data or rotated the high value tokens through again,  
[00:33:24] then it would continue getting better. We've seen a bunch of different companies around  
[00:33:31] the world basically take the Llama-2 70B model architecture and then build a new model. But it's  
[00:33:41] still the case that when you make a generational improvement to something like the Llama-3 70B or  
[00:33:46] the Llama-3 405B, there isn’t anything like that open source today. I think that's a big  
[00:33:54] step function. What people are going to be able to build on top of that I think can’t go infinitely  
[00:33:59] from there. There can be some optimization in that until you get to the next step function.  
[00:34:05] Let's zoom out a little bit from specific models and even the multi-year lead times  
[00:34:11] you would need to get energy approvals and so on. Big picture, what's happening with AI these  
[00:34:15] next couple of decades? Does it feel like another technology like the metaverse or  
[00:34:21] social, or does it feel like a fundamentally different thing in the course of human history?  
[00:34:29] I think it's going to be pretty fundamental. I think it's going to be more like the creation  
[00:34:34] of computing in the first place. You'll get all these new apps in the same way as when you got  
[00:34:44] the web or you got mobile phones. People basically rethought all these experiences as a lot of things  
[00:34:50] that weren't possible before became possible. So I think that will happen, but I think it's  
[00:34:56] a much lower-level innovation. My sense is that it's going to be more like people going  
[00:35:01] from not having computers to having computers. It’s very hard to reason about exactly how this  
[00:35:16] goes. In the cosmic scale obviously it'll happen quickly, over a couple of decades or something.  
[00:35:27] There is some set of people who are afraid of it really spinning out and going from being somewhat  
[00:35:33] intelligent to extremely intelligent overnight. I just think that there's all these physical  
[00:35:37] constraints that make that unlikely to happen. I just don't really see that playing out. I think  
[00:35:45] we'll have time to acclimate a bit. But it will really change the way that we work and give people  
[00:35:51] all these creative tools to do different things. I think it's going to really enable people to do  
[00:36:00] the things that they want a lot more. So maybe not overnight, but is it your  
[00:36:05] view that on a cosmic scale we can think of these milestones in this way? Humans evolved,  
[00:36:09] and then AI happened, and then they went out into the galaxy. Maybe it takes many decades,  
[00:36:15] maybe it takes a century, but is that the grand scheme of what's happening right now in history?  
[00:36:22] Sorry, in what sense? In the sense that there were  
[00:36:25] other technologies, like computers and even fire, but the development of AI itself is as  
[00:36:29] significant as humans evolving in the first place. I think that's tricky. The history of humanity  
[00:36:39] has been people basically thinking that certain aspects of humanity are really unique in different  
[00:36:50] ways and then coming to grips with the fact that that's not true, but that humanity is actually  
[00:36:57] still super special. We thought that the earth was the center of the universe and it's not,  
[00:37:06] but humans are still pretty awesome and pretty unique, right?  
[00:37:12] I think another bias that people tend to have is thinking that intelligence  
[00:37:17] is somehow fundamentally connected to life. It's not actually clear that it is. I don't  
[00:37:32] know that we have a clear enough definition of consciousness or life to fully interrogate this.  
[00:37:42] There's all this science fiction about creating intelligence where it starts to take on all these  
[00:37:47] human-like behaviors and things like that. The current incarnation of all this stuff feels like  
[00:37:54] it's going in a direction where intelligence can be pretty separated from consciousness,  
[00:37:59] agency, and things like that, which I think just makes it a super valuable tool.  
[00:38:06] Obviously it's very difficult to predict what direction this stuff goes in over time,  
[00:38:10] which is why I don't think anyone should be dogmatic about how they plan to develop it  
[00:38:16] or what they plan to do. You want to look at it with each release. We're obviously  
[00:38:20] very pro open source, but I haven't committed to releasing every single thing that we do.  
[00:38:27] I’m basically very inclined to think that open sourcing is going to be good for the  
[00:38:32] community and also good for us because we'll benefit from the innovations. If at some point  
[00:38:38] however there's some qualitative change in what the thing is capable of, and we feel like it's  
[00:38:43] not responsible to open source it, then we won't. It's all very difficult to predict.  
[00:38:52] What is a kind of specific qualitative change where you'd be training Llama-5 or Llama-4,  
[00:38:57] and if you see it, it’d make you think “you know what, I'm not sure about open sourcing it”?  
[00:39:05] It's a little hard to answer that in the abstract because there are negative  
[00:39:09] behaviors that any product can exhibit where as long as you can mitigate it,  
[00:39:15] it's okay. There’s bad things about social media that we work to mitigate. There's bad things about  
[00:39:23] Llama-2 where we spend a lot of time trying to make sure that it's not like helping people  
[00:39:28] commit violent acts or things like that. That doesn't mean that it's a kind of autonomous or  
[00:39:34] intelligent agent. It just means that it's learned a lot about the world and it can answer a set of  
[00:39:38] questions that we think would be unhelpful for it to answer. I think the question isn't really what  
[00:39:49] behaviors would it show, it's what things would we not be able to mitigate after it shows that.  
[00:39:59] I think that there's so many ways in which something can be good or bad that it's hard  
[00:40:03] to actually enumerate them all up front. Look at what we've had to deal with in social media and  
[00:40:10] the different types of harms. We've basically gotten to like 18 or 19 categories of harmful  
[00:40:15] things that people do and we've basically built AI systems to identify what those things are and  
[00:40:23] to make sure that doesn't happen on our network as much as possible. Over time I think you'll  
[00:40:29] be able to break this down into more of a taxonomy too. I think this is a thing that  
[00:40:34] we spend time researching as well, because we want to make sure that we understand that.  
[00:41:46] It seems to me that it would be a good idea. I would be disappointed in a future where AI  
[00:41:50] systems aren't broadly deployed and everybody doesn't have access to them. At the same time,  
[00:41:55] I want to better understand the mitigations. If the mitigation is the fine-tuning,  
[00:42:00] the whole thing about open weights is that you can then remove the fine-tuning, which is often  
[00:42:06] superficial on top of these capabilities. If it's like talking on Slack with a biology researcher…  
[00:42:12] I think models are very far from this. Right now, they’re like Google search. But if I can  
[00:42:17] show them my Petri dish and they can explain why my smallpox sample didn’t grow and what to change,  
[00:42:23] how do you mitigate that? Because somebody can just fine-tune that in there, right?  
[00:42:29] That's true. I think a lot of people will basically use the off-the-shelf model and some  
[00:42:35] people who have basically bad faith are going to try to strip out all the bad stuff. So I do think  
[00:42:41] that's an issue. On the flip side, one of the reasons why I'm philosophically so pro open source  
[00:42:52] is that I do think that a concentration of AI in the future has the potential to be as dangerous as  
[00:43:02] it being widespread. I think a lot of people think about the questions of “if we can do this stuff,  
[00:43:08] is it bad for it to be out in the wild and just widely available?” I think another version of  
[00:43:15] this is that it's probably also pretty bad for one institution to have an AI that is  
[00:43:25] way more powerful than everyone else's AI. There’s one security analogy that I think  
[00:43:31] of. There are so many security holes in so many different things. If you could travel back in  
[00:43:42] time a year or two years, let's say you just have one or two years more knowledge of the security  
[00:43:50] holes. You can pretty much hack into any system. That’s not AI. So it's not that far-fetched to  
[00:43:55] believe that a very intelligent AI probably would be able to identify some holes and basically  
[00:44:03] be like a human who could go back in time a year or two and compromise all these systems.  
[00:44:07] So how have we dealt with that as a society? One big part is open source software that  
[00:44:13] makes it so that when improvements are made to the software, it doesn't just get stuck in one  
[00:44:18] company's products but can be broadly deployed to a lot of different systems, whether they’re banks  
[00:44:24] or hospitals or government stuff. As the software gets hardened, which happens because more people  
[00:44:31] can see it and more people can bang on it, there are standards on how this stuff works. The world  
[00:44:37] can get upgraded together pretty quickly. I think that a world where AI is very widely  
[00:44:44] deployed, in a way where it's gotten hardened progressively over time, is one where all the  
[00:44:52] different systems will be in check in a way. That seems fundamentally more healthy to me than one  
[00:44:58] where this is more concentrated. So there are risks on all sides, but I think that's a risk  
[00:45:05] that I don't hear people talking about quite as much. There's the risk of the AI system doing  
[00:45:13] something bad. But I stay up at night worrying more about an untrustworthy actor having the super  
[00:45:27] strong AI, whether it's an adversarial government or an untrustworthy company or whatever. I think  
[00:45:39] that that's potentially a much bigger risk. As in, they could overthrow our government because  
[00:45:47] they have a weapon that nobody else has? Or just cause a lot of mayhem. I think the  
[00:45:55] intuition is that this stuff ends up being pretty important and valuable for both  
[00:46:01] economic and security reasons and other things. If someone whom you don't trust or an adversary  
[00:46:11] gets something more powerful, then I think that that could be an issue. Probably the best way  
[00:46:16] to mitigate that is to have good open source AI that becomes the standard and in a lot of  
[00:46:24] ways can become the leader. It just ensures that it's a much more even and balanced playing field.  
[00:46:33] That seems plausible to me. If that works out, that would be the future I prefer. I want to  
[00:46:38] understand mechanistically how the fact that there are open source AI systems in the world  
[00:46:47] prevents somebody causing mayhem with their AI system? With the specific example of somebody  
[00:46:50] coming with a bioweapon, is it just that we'll do a bunch of R&D in the rest of the world to figure  
[00:46:55] out vaccines really fast? What's happening? If you take the security one that I was  
[00:46:59] talking about, I think someone with a weaker AI trying to hack into a  
[00:47:03] system that is protected by a stronger AI will succeed less. In terms of software security–  
[00:47:12] How do we know everything in the world is like that? What if bioweapons aren't like that?  
[00:47:16] I mean, I don't know that everything in the world is like that. Bioweapons are one of the  
[00:47:25] areas where the people who are most worried about this stuff are focused and I think it makes a lot  
[00:47:33] of sense. There are certain mitigations. You can try to not train certain knowledge into  
[00:47:42] the model. There are different things but at some level if you get a sufficiently bad actor,  
[00:47:51] and you don't have other AI that can balance them and understand what the threats are,  
[00:48:00] then that could be a risk. That's one of the things that we need to watch out for.  
[00:48:05] Is there something you could see in the deployment of these systems where you're training Llama-4 and  
[00:48:12] it lied to you because it thought you weren't noticing or something and you're like “whoa  
[00:48:17] what's going on here?” This is probably not likely with a Llama-4 type system, but is  
[00:48:22] there something you can imagine like that where you'd be really concerned about deceptiveness and  
[00:48:27] billions of copies of this being out in the wild? I mean right now we see a lot of hallucinations.  
[00:48:37] It's more so that. I think it's an interesting question, how you would tell the difference  
[00:48:43] between hallucination and deception. There are a lot of risks and things to think about. I try,  
[00:48:57] in running our company at least, to balance these longer-term theoretical risks with  
[00:49:07] what I actually think are quite real risks that exist today. So when you talk about deception,  
[00:49:14] the form of that that I worry about most is people using this to generate misinformation  
[00:49:18] and then pump that through our networks or others. The way that we've combated this type  
[00:49:26] of harmful content is by building AI systems that are smarter than the adversarial ones.  
[00:49:33] This informs part of my theory on this. If you look at the different types of harm that people  
[00:49:38] do or try to do through social networks, there are ones that are not very adversarial. For example,  
[00:49:50] hate speech is not super adversarial in the sense that people aren't getting better at being racist.  
[00:50:03] That's one where I think the AIs are generally getting way more sophisticated faster than people  
[00:50:08] are at those issues. And we have issues both ways. People do bad things, whether they're  
[00:50:15] trying to incite violence or something, but we also have a lot of false positives where we  
[00:50:20] basically censor stuff that we shouldn't. I think that understandably makes a lot of people annoyed.  
[00:50:25] So I think having an AI that gets increasingly precise on that is going to be good over time.  
[00:50:30] But let me give you another example: nation states trying to interfere in elections. That's  
[00:50:35] an example where they absolutely have cutting edge technology and absolutely get better each year. So  
[00:50:41] we block some technique, they learn what we did and come at us with a different technique. It's  
[00:50:46] not like a person trying to say mean things, They have a goal. They're sophisticated. They have a  
[00:50:56] lot of technology. In those cases, I still think about the ability to have our AI systems grow in  
[00:51:04] sophistication at a faster rate than theirs do. It's an arms race but I think we're at least  
[00:51:09] winning that arms race currently. This is a lot of the stuff that I spend time thinking about.  
[00:51:18] Yes, whether it's Llama-4 or Llama-6, we need to think about what behaviors we're observing and  
[00:51:26] it's not just us. Part of the reason why you make this open source is that there are a lot of other  
[00:51:29] people who study this too. So we want to see what other people are observing, what we’re observing,  
[00:51:35] what we can mitigate, and then we'll make our assessment on whether we can make it  
[00:51:40] open source. For the foreseeable future I'm optimistic we will be able to. In the near term,  
[00:51:49] I don't want to take our eye off the ball in terms of what are actual bad things that  
[00:51:53] people are trying to use the models for today. Even if they're not existential, there are  
[00:51:58] pretty bad day-to-day harms that we're familiar with in running our services. That's actually a  
[00:52:05] lot of what we have to spend our time on as well. I found the synthetic data thing really curious.  
[00:52:14] With current models it makes sense why there might be an asymptote with just doing the synthetic data  
[00:52:19] again and again. But let’s say they get smarter and you use the kinds of techniques—you talk about  
[00:52:23] in the paper or the blog posts that are coming out on the day this will be released—where it goes to  
[00:52:29] the thought chain that is the most correct. Why do you think this wouldn't lead to a loop  
[00:52:36] where it gets smarter, makes better output, gets smarter and so forth. Of course it wouldn't be  
[00:52:36] overnight, but over many months or years of training potentially with a smarter model.  
[00:52:45] I think it could, within the parameters of whatever the model architecture is. It's just  
[00:52:49] that with today's 8B parameter models, I don't think you're going to get to be as good as the  
[00:53:04] state-of-the-art multi-hundred billion parameter models that are incorporating  
[00:53:08] new research into the architecture itself. But those will be open source as well, right?  
[00:53:15] Well yeah, subject to all the questions that we just talked about but yes. We would hope that  
[00:53:23] that'll be the case. But I think that at each point, when you're building software there's a  
[00:53:29] ton of stuff that you can do with software but then at some level you're constrained by the  
[00:53:34] chips that it's running on. So there are always going to be different physical constraints. How  
[00:53:42] big the models are is going to be constrained by how much energy you can get and use for  
[00:53:49] inference. I'm simultaneously very optimistic that this stuff will continue to improve quickly  
[00:53:59] and also a little more measured than I think some people are about it. I don’t think the  
[00:54:11] runaway case is a particularly likely one. I think it makes sense to keep your options  
[00:54:17] open. There's so much we don't know. There's a case in which it's really important to keep the  
[00:54:22] balance of power so nobody becomes a totalitarian dictator. There's a case in which you don't want  
[00:54:26] to open source the architecture because China can use it to catch up to America's AIs and there is  
[00:54:32] an intelligence explosion and they win that. A lot of things seem possible. Keeping your options open  
[00:54:38] considering all of them seems reasonable. Yeah.  
[00:54:42] Let's talk about some other things. Metaverse. What time period in human history would you be  
[00:54:48] most interested in going into? 100,000 BCE to now, you just want to see what it was like?  
[00:54:53] It has to be the past? Oh yeah, it has to be the past.  
[00:55:04] I'm really interested in American history and classical history. I'm really interested in the  
[00:55:10] history of science too. I actually think seeing and trying to understand more about how some of  
[00:55:19] the big advances came about would be interesting. All we have are somewhat limited writings about  
[00:55:24] some of that stuff. I'm not sure the metaverse is going to let you do that because it's going  
[00:55:29] to be hard to go back in time for things that we don't have records of. I'm actually not sure  
[00:55:38] that going back in time is going to be that important of a thing. I think it's going to  
[00:55:42] be cool for like history classes and stuff, but that's probably not the use case that I'm  
[00:55:47] most excited about for the metaverse overall. The main thing is just the ability to feel  
[00:55:53] present with people, no matter where you are. I think that's going to be killer. In the AI  
[00:56:00] conversation that we were having, so much of it is about physical constraints that underlie all  
[00:56:08] of this. I think one lesson of technology is that you want to move things from the physical  
[00:56:14] constraint realm into software as much as possible because software is so much easier to build and  
[00:56:20] evolve. You can democratize it more because not everyone is going to have a data center but  
[00:56:26] a lot of people can write code and take open source code and modify it. Τhe metaverse  
[00:56:33] version of this is enabling realistic digital presence. That’s going to be an absolutely huge  
[00:56:43] difference so people don't feel like they have to be physically together for as many things.  
[00:56:51] Now I think that there can be things that are better about being physically together. These  
[00:56:57] things aren't binary. It's not going to be like “okay, now you don't need to do that anymore.”  
[00:57:01] But overall, I think it's just going to be really powerful for socializing, for feeling  
[00:57:11] connected with people, for working, for parts of industry, for medicine, for so many things.  
[00:57:20] I want to go back to something you said at the beginning of the conversation. You didn't sell  
[00:57:23] the company for a billion dollars. And with the metaverse, you knew you were going to  
[00:57:26] do this even though the market was hammering you for it. I'm curious. What is the source  
[00:57:31] of that edge? You said “oh, values, I have this intuition,” but everybody says that. If  
[00:57:37] you had to say something that's specific to you, how would you express what that is? Why  
[00:57:41] were you so convinced about the metaverse? I think that those are different questions.  
[00:57:52] What are the things that power me? We've talked about a bunch of the themes. I just  
[00:58:02] really like building things. I specifically like building things around how people communicate and  
[00:58:10] understanding how people express themselves and how people work. When I was in college  
[00:58:13] I studied computer science and psychology. I think a lot of other people in the industry  
[00:58:18] studied computer science. So, it's always been the intersection of those two things for me.  
[00:58:27] It’s also sort of this really deep drive. I don't know how to explain it but I just feel  
[00:58:36] constitutionally that I'm doing something wrong if I'm not building something new. Even when we were  
[00:58:50] putting together the business case for investing a $100 billion in AI or some huge amount in the  
[00:58:58] metaverse, we have plans that I think made it pretty clear that if our stuff works,  
[00:59:03] it'll be a good investment. But you can't know for certain from the outset. There are all these  
[00:59:10] arguments that people have, with advisors or different folks. It's like, “how are you  
[00:59:19] confident enough to do this?” Well the day I stop trying to build new things, I'm just done. I'm  
[00:59:26] going to go build new things somewhere else. I'm fundamentally incapable of running something,  
[00:59:37] or in my own life, and not trying to build new things that I think are interesting. That's not  
[00:59:43] even a question for me, whether we're going to take a swing at building the next thing. I'm  
[00:59:51] just incapable of not doing that. I don't know. I'm kind of like this in all the different aspects  
[01:00:01] of my life. Our family built this ranch in Kauai and I worked on designing all these buildings. We  
[01:00:14] started raising cattle and I'm like “alright, I want to make the best cattle in the world so how  
[01:00:19] do we architect this so that way we can figure this out and build all the stuff up that we  
[01:00:24] need to try to do that.” I don't know, that's me. What was the other part of the question?  
[01:01:37] I'm not sure but I'm actually curious about something else. So a 19-year-old  
[01:01:42] Mark reads a bunch of antiquity and classics in high school and college.  
[01:01:48] What important lesson did you learn from it? Not just interesting things you found,  
[01:01:50] but there aren't that many tokens you consume by the time you're 19. A bunch of them were about the  
[01:01:55] classics. Clearly that was important in some way. There aren't that many tokens you consume...  
[01:02:06] That's a good question. Here’s one of the things I thought was really fascinating. Augustus became  
[01:02:19] emperor and he was trying to establish peace. There was no real conception of peace at the  
[01:02:30] time. The people's understanding of peace was peace as the temporary time between when your  
[01:02:36] enemies inevitably attack you. So you get a short rest. He had this view of changing the  
[01:02:44] economy from being something mercenary and militaristic to this actually positive-sum  
[01:02:53] thing. It was a very novel idea at the time. That’s something that's really fundamental:  
[01:03:07] the bounds on what people can conceive of at the time as rational ways to work.  
[01:03:17] This applies to both the metaverse and the AI stuff. A lot of investors, and other people,  
[01:03:22] can't wrap their head around why we would open source this. It’s like “I don't understand, it’s  
[01:03:29] open source. That must just be the temporary time between which you're making things proprietary,  
[01:03:34] right?” I think it's this very profound thing in tech that it actually creates a lot of winners.  
[01:03:49] I don't want to strain the analogy too much but I do think that a lot of the time,  
[01:03:56] there are models for building things that people often can't even wrap their head  
[01:04:06] around. They can’t understand how that would be a valuable thing for people to do or how it would be  
[01:04:11] a reasonable state of the world. I think there are more reasonable things than people think.  
[01:04:20] That's super fascinating. Can I give you what I was thinking in terms of what you might have  
[01:04:24] gotten from it? This is probably totally off, but I think it’s just how young some of these  
[01:04:29] people are, who have very important roles in the empire. For example, Caesar Augustus,  
[01:04:33] by the time he’s 19, is already one of the most important people in Roman politics. He's leading  
[01:04:39] battles and forming the Second Triumvirate. I wonder if the 19-year-old you was thinking “I  
[01:04:42] can do this because Caesar Augustus did this.” That's an interesting example, both from a lot  
[01:04:48] of history and American history too. One of my favorite quotes is this Picasso quote that all  
[01:04:56] children are artists and the challenge is to remain an artist as you grow up. When you’re  
[01:05:02] younger, it’s just easier to have wild ideas. There are all these analogies to the innovator’s  
[01:05:14] dilemma that exist in your life as well as for your company or whatever you’ve built. You’re  
[01:05:20] earlier on in your trajectory so it's easier to pivot and take in new ideas without disrupting  
[01:05:26] other commitments to different things. I think that's an interesting part of  
[01:05:33] running a company. How do you stay dynamic? Let’s go back to the investors and open source.  
[01:05:41] The $10B model, suppose it's totally safe. You've done these evaluations and unlike in this case  
[01:05:47] the evaluators can also fine-tune the model, which hopefully will be the case in future models. Would  
[01:05:52] you open source the $10 billion model? As long as it's helping us then yeah.  
[01:05:57] But would it? $10 billion of R&D and now it's open source.  
[01:06:01] That’s a question which we’ll have to evaluate as time goes on too. We have a long history of  
[01:06:11] open sourcing software. We don’t tend to open source our product. We don't take the code for  
[01:06:18] Instagram and make it open source. We take a lot of the low-level infrastructure and  
[01:06:24] we make that open source. Probably the biggest one in our history was our Open Compute Project  
[01:06:29] where we took the designs for all of our servers, network switches, and data centers, and made it  
[01:06:36] open source and it ended up being super helpful. Although a lot of people can design servers the  
[01:06:42] industry now standardized on our design, which meant that the supply chains basically all got  
[01:06:46] built out around our design. So volumes went up, it got cheaper for everyone, and it saved  
[01:06:50] us billions of dollars which was awesome. So there's multiple ways where open source  
[01:06:56] could be helpful for us. One is if people figure out how to run the models more cheaply. We're  
[01:07:01] going to be spending tens, or a hundred billion dollars or more over time on all this stuff. So  
[01:07:08] if we can do that 10% more efficiently, we're saving billions or tens of billions of dollars.  
[01:07:12] That's probably worth a lot by itself. Especially if there are other competitive models out there,  
[01:07:17] it's not like our thing is giving away some kind of crazy advantage.  
[01:07:22] So is your view that the training will be commodified?  
[01:07:29] I think there's a bunch of ways that this could play out and that's one. So “commodity” implies  
[01:07:39] that it's going to get very cheap because there are lots of options. The other direction that this  
[01:07:44] could go in is qualitative improvements. You mentioned fine-tuning. Right now it's pretty  
[01:07:51] limited what you can do with fine-tuning major other models out there. There are some options  
[01:07:56] but generally not for the biggest models. There’s being able to do that, different app specific  
[01:08:05] things or use case specific things or building them into specific tool chains. I think that will  
[01:08:11] not only enable more efficient development, but it could enable qualitatively different things.  
[01:08:18] Here's one analogy on this. One thing that I think generally sucks about the mobile ecosystem is that  
[01:08:27] you have these two gatekeeper companies, Apple and Google, that can tell you what you're allowed to  
[01:08:32] build. There's the economic version of that which is like when we build something and they just  
[01:08:38] take a bunch of your money. But then there's the qualitative version, which is actually what upsets  
[01:08:45] me more. There's a bunch of times when we've launched or wanted to launch features and Apple's  
[01:08:51] just like “nope, you're not launching that.” That sucks, right? So the question is, are we set up  
[01:09:01] for a world like that with AI? You're going to get a handful of companies that run these closed  
[01:09:08] models that are going to be in control of the APIs and therefore able to tell you what you can build?  
[01:09:13] For us I can say it is worth it to go build a model ourselves to make sure that we're not  
[01:09:19] in that position. I don't want any of those other companies telling us what we can build.  
[01:09:26] From an open source perspective, I think a lot of developers don't want those companies telling them  
[01:09:30] what they can build either. So the question is, what is the ecosystem that gets built out around  
[01:09:36] that? What are interesting new things? How much does that improve our products? I think there  
[01:09:43] are lots of cases where if this ends up being like our databases or caching systems or architecture,  
[01:09:50] we'll get valuable contributions from the community that will make our stuff better.  
[01:09:54] Our app specific work that we do will then still be so differentiated that it won't really matter.  
[01:10:00] We'll be able to do what we do. We'll benefit and all the systems, ours and the communities’,  
[01:10:03] will be better because it's open source. There is one world where maybe  
[01:10:10] that’s not the case. Maybe the model ends up being more of the product itself. I think it's  
[01:10:16] a trickier economic calculation then, whether you open source that. You are commoditizing  
[01:10:22] yourself then a lot. But from what I can see so far, it doesn't seem like we're in that zone.  
[01:10:26] Do you expect to earn significant revenue from licensing your model to the cloud  
[01:10:30] providers? So they have to pay you a fee to actually serve the model.  
[01:10:36] We want to have an arrangement like that but I don't know how significant it'll be. This is  
[01:10:42] basically our license for Llama. In a lot of ways it's a very permissive open source license, except  
[01:10:51] that we have a limit for the largest companies using it. This is why we put that limit in. We're  
[01:10:56] not trying to prevent them from using it. We just want them to come talk to us if they're going to  
[01:11:00] just basically take what we built and resell it and make money off of it. If you're like Microsoft  
[01:11:07] Azure or Amazon, if you're going to be reselling the model then we should have some revenue share  
[01:11:12] on that. So just come talk to us before you go do that. That's how that's played out.  
[01:11:15] So for Llama-2, we just have deals with basically all these major cloud companies and Llama-2 is  
[01:11:23] available as a hosted service on all those clouds. I assume that as we release bigger  
[01:11:30] and bigger models, that will become a bigger thing. It's not the main thing that we're doing,  
[01:11:33] but I think if those companies are going to be selling our models it just makes sense that we  
[01:11:37] should share the upside of that somehow. Regarding other open source dangers,  
[01:11:42] I think you have genuine legitimate points about the balance of power stuff and potentially the  
[01:11:48] harms you can get rid of because we have better alignment techniques or something. I wish there  
[01:11:52] were some sort of framework that Meta had. Other labs have this where they say “if we see this  
[01:11:57] concrete thing, then that's a no go on the open source or even potentially on deployment.” Just  
[01:12:03] writing it down so the company is ready for it and people have expectations around it and so forth.  
[01:12:09] That's a fair point on the existential risk side. Right now we focus more on the types of  
[01:12:14] risks that we see today, which are more of these content risks. We don't want the model to be doing  
[01:12:24] things that are helping people commit violence or fraud or just harming people in different  
[01:12:30] ways. While it is maybe more intellectually interesting to talk about the existential risks,  
[01:12:30] I actually think the real harms that need more energy in being mitigated are things where someone  
[01:12:31] takes a model and does something to hurt a person. In practice for the current models,  
[01:12:35] and I would guess the next generation and maybe even the generation after that,  
[01:12:42] those are the types of more mundane harms that we see today, people committing fraud against each  
[01:13:07] other or things like that. I just don't want to shortchange that. I think we have a responsibility  
[01:13:15] to make sure we do a good job on that. Meta's a big company. You can handle both.  
[01:13:22] As far as open source goes, I'm actually curious if you think the impact of open source,  
[01:13:25] from PyTorch, React, Open Compute and other things, has been bigger for the world than  
[01:13:30] even the social media aspects of Meta. I've talked to people who use these services  
[01:13:33] and they think that it's plausible because a big part of the internet runs on these things.  
[01:13:39] It's an interesting question. I mean almost half the world uses our consumer products so  
[01:13:48] it's hard to beat that. But I think open source is really powerful as a new way of  
[01:13:56] building things. I mean, it's possible. It may be one of these things like Bell Labs,  
[01:14:08] where they were working on the transistor because they wanted to enable long-distance calling. They  
[01:14:17] did and it ended up being really profitable for them that they were able to enable long-distance  
[01:14:20] calling. 5 to 10 years out from that, if you asked them what was the most useful thing  
[01:14:29] that they invented it's like “okay, we enabled long distance calling and now all these people  
[01:14:32] are long-distance calling.” But if you asked a hundred years later maybe it's a different answer.  
[01:14:38] I think that's true of a lot of the things that we're building: Reality Labs, some of the AI  
[01:14:44] stuff, some of the open source stuff. The specific products evolve, and to some degree come and go,  
[01:14:50] but the advances for humanity persist and that's a cool part of what we all get to do.  
[01:14:58] By when will the Llama models be trained on your own custom silicon?  
[01:15:06] Soon, not Llama-4. The approach that we took is we first built custom silicon that could handle  
[01:15:16] inference for our ranking and recommendation type stuff, so Reels, News Feed ads, etc. That  
[01:15:24] was consuming a lot of GPUs. When we were able to move that to our own silicon, we're now able  
[01:15:31] to use the more expensive NVIDIA GPUs only for training. At some point we will hopefully have  
[01:15:43] silicon ourselves that we can be using for at first training some of the simpler things, then  
[01:15:48] eventually training these really large models. In the meantime, I'd say the program is going quite  
[01:15:57] well and we're just rolling it out methodically and we have a long-term roadmap for it.  
[01:16:02] Final question. This is totally out of left field. If you were made CEO of Google+  
[01:16:07] could you have made it work? Google+? Oof. I don't know.  
[01:16:14] That's a very difficult counterfactual. Okay, then the real final question will be:  
[01:16:21] when Gemini was launched, was there any chance that somebody  
[01:16:24] in the office uttered: “Carthago delenda est”. No, I think we're tamer now. It's a good question.  
[01:16:38] The problem is there was no CEO of Google+. It was just a division within a company. You asked  
[01:16:45] before about what are the scarcest commodities but you asked about it in terms of dollars. I  
[01:16:51] actually think for most companies, of this scale at least, it's focus. When you're a startup maybe  
[01:16:58] you're more constrained on capital. You’re just working on one idea and you might not have all  
[01:17:04] the resources. You cross some threshold at some point with the nature of what you're doing. You're  
[01:17:10] building multiple things. You're creating more value across them but you become more  
[01:17:14] constrained on what you can direct to go well. There are always the cases where something  
[01:17:22] random awesome happens in the organization and I don't even know about it. Those are great. But I  
[01:17:28] think in general, the organization's capacity is largely limited by what the CEO and the  
[01:17:37] management team are able to oversee and manage. That's been a big focus for us. As Ben Horowitz  
[01:17:49] says “keep the main thing, the main thing” and try to stay focused on your key priorities.  
[01:17:59] Awesome, that was excellent, Mark. Thanks so much. That was a lot of fun.  
[01:18:01] Yeah, really fun. Thanks for having me. Absolutely.  
