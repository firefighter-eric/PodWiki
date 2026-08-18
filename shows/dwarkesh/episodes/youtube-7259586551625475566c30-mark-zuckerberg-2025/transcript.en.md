# Mark Zuckerberg — AI will write most Meta code in 18 months

[00:00:47] Mark, thanks for coming on the podcast again. Yeah, happy to do it. Good to see you.  
[00:00:50] You too. Last time you were here, you had launched Llama 3. Now you've launched Llama 4.  
[00:00:56] Well, the first version. That's right. What's  
[00:00:58] new? What's exciting? What's changed? The whole field is so dynamic. I feel like a ton  
[00:01:04] has changed since the last time we talked. Meta AI has almost a billion people using it monthly now,  
[00:01:10] which is pretty wild. I think this is going to be a really big year for all of this, especially once  
[00:01:18] you get the personalization loop going, which we’re just starting to build in now really,  
[00:01:25] from both the context that all the algorithms have about what you’re interested in — feed, your  
[00:01:30] profile information, your social graph information — but also what you're interacting with the  
[00:01:34] AI about. That’s going to be the next thing that's super exciting. I'm really big on that.  
[00:01:41] The modeling stuff continues to make really impressive advances too. I'm pretty happy  
[00:01:50] with the first set of Llama 4 releases. We announced four models and released the  
[00:01:56] first two — the Scout and Maverick ones — which are mid-size to small models.  
[00:02:04] The most popular Llama 3 model was the 8 billion parameter one. So we’ve got one of  
[00:02:12] those coming in the Llama 4 series too. Our internal code name for it is “Little Llama.”  
[00:02:19] That’s coming probably over the next few months. Scout and Maverick are good. They have some of  
[00:02:28] the highest intelligence per cost you can get of any model out there. They’re natively multimodal,  
[00:02:37] very efficient, run on one host. They’re designed to be very efficient and low latency, for a lot  
[00:02:44] of the use cases we’re building for internally. That’s our whole thing. We build what we want,  
[00:02:50] and then we open-source it so other people can use it too. I'm excited about that.  
[00:02:55] I'm also excited about the Behemoth model, which is coming up. It's going to be our first model  
[00:03:02] that's sort of at the frontier — more than 2 trillion parameters. As the name says,  
[00:03:13] it's quite big. We’re trying to figure out how to make that useful for people. It’s so big that  
[00:03:18] we've had to build a bunch of infrastructure just to be able to post-train it ourselves.  
[00:03:23] Now we're trying to wrap our heads around, how does the average developer out there actually  
[00:03:28] use something like this? How do we make it useful — maybe by distilling it into models  
[00:03:32] that are a reasonable size to run? Because you're obviously not going to want to run  
[00:03:37] something like that in a consumer model. As you saw with the Llama 3 stuff last year,  
[00:03:45] the initial launch was exciting and then we just built on that over the year. 3.1 released  
[00:03:52] the 405 billion model, 3.2 is when we got all the multimodal stuff in. We basically have a roadmap  
[00:03:59] like that for this year too. So a lot going on. I'm interested to hear more about it. There's  
[00:04:03] this impression that the gap between the best closed-source and the best open-source models  
[00:04:09] has increased over the last year. I know the full family of Llama 4 models isn't out yet,  
[00:04:13] but Llama 4 Maverick is at #35 on Chatbot Arena. On a bunch of major benchmarks,  
[00:04:19] it seems like o4-mini or Gemini 2.5 Flash are beating Maverick, which is in the same  
[00:04:26] class. What do you make of that impression? There are a few things. First, I actually  
[00:04:30] think this has been a very good year for open source overall. If you go back to  
[00:04:35] where we were last year, Llama was the only real, super-innovative open-source model.  
[00:04:43] Now you have a bunch of them in the field. In general, the prediction that this would  
[00:04:47] be the year open source generally overtakes closed source as the most used models out there,  
[00:04:54] I think that's generally on track to be true. One interesting surprise — positive in some ways,  
[00:05:02] negative in others, but overall good — is that it’s not just Llama. There are a lot of good  
[00:05:07] ones out there. I think that's quite good. Then there's the reasoning phenomenon,  
[00:05:13] which you're alluding to talking about o3, o4, and other models. There's a specialization happening.  
[00:05:26] If you want a model that’s the best at math problems, coding, or different things  
[00:05:32] like those tasks, then reasoning models that consume more test-time or inference-time compute  
[00:05:43] in order to provide more intelligence are a really compelling paradigm. And we're building a Llama 4  
[00:05:46] reasoning model too. It'll come out at some point. But for a lot of the applications we care about,  
[00:06:01] latency and good intelligence per cost are much more important product attributes. If you're  
[00:06:10] primarily designing for a consumer product, people don't want to wait half a minute to get an answer.  
[00:06:19] If you can give them a generally good answer in half a second, that's a great tradeoff.  
[00:06:25] I think both of these are going to end up being important directions. I’m optimistic  
[00:06:31] about integrating reasoning models with the core language models over time. That's the direction  
[00:06:38] Google has gone in with some of the more recent Gemini models. I think that's really promising.  
[00:06:45] But I think there’s just going to be a bunch of different stuff that goes on.  
[00:06:49] You also mentioned the whole Chatbot Arena thing, which I think is interesting and points to the  
[00:06:55] challenge around how you do benchmarking. How do you know what models are good for which things?  
[00:07:03] One of the things we've generally tried to do over the last year is anchor more of our models in  
[00:07:10] our Meta AI product north star use cases. The issue with open source benchmarks,  
[00:07:17] and any given thing like the LM Arena stuff, is that they’re often skewed toward a very specific  
[00:07:28] set of uses cases, which are often not actually what any normal person does in your product.  
[00:07:37] The portfolio of things they’re trying to measure is often different from what  
[00:07:40] people care about in any given product. Because of that, we’ve found that trying  
[00:07:49] to optimize too much for that kind of stuff has led us astray. It’s actually not led towards the  
[00:07:56] highest quality product, the most usage, and best feedback within Meta AI as people use our stuff.  
[00:08:03] So we're trying to anchor our north star on the product value that people report to us,  
[00:08:12] what they say that they want, and what their revealed preferences are, and using  
[00:08:16] the experiences that we have. Sometimes these benchmarks just don't quite line up.  
[00:08:23] I think a lot of them are quite easily gameable. On the Arena you'll see stuff like Sonnet 3.7,  
[00:08:32] which is a great model, and it's not near the top. It was relatively easy for our team to  
[00:08:39] tune a version of Llama 4 Maverick that could be way at the top. But the version we released,  
[00:08:47] the pure model, actually has no tuning for that at all, so it's further down. So you just need  
[00:08:52] to be careful with some of these benchmarks. We're going to index primarily on the products.  
[00:08:57] Do you feel like there is some benchmark which captures what you see as a north star of value  
[00:09:03] to the user which can be be objectively measured between different models and where you'd say,  
[00:09:08] "I need Llama 4 to come out on top on this”? Our benchmark is basically user value in Meta AI.  
[00:09:17] But you can't compare that to other models. We might be able to, because we might be able  
[00:09:20] to run other models and be able to tell. That's one of the advantages of open source. You have  
[00:09:25] a good community of folks who can poke holes in your stuff and point out, "Okay, where is  
[00:09:30] your model not good, and where is it good?" The reality at this point is that all these  
[00:09:36] models are optimized for slightly different mixes of things. Everyone is trying to go  
[00:09:42] towards the same end in that all the leading labs are trying to create general intelligence,  
[00:09:48] superintelligence, whatever you call it. AI that can lead toward a world of abundance  
[00:09:53] where everyone has these superhuman tools to create whatever they want. That leads  
[00:09:58] to dramatically empowering people and creating all these economic benefits.  
[00:10:02] However you define it, that's what a lot of the labs are going for.  
[00:10:09] But there's no doubt that different folks have optimized toward different things. I think the  
[00:10:13] Anthropic folks have really focused on coding and agents around that. The OpenAI folks, I think,  
[00:10:20] have gone a little more toward reasoning recently. There’s a space which, if I had to guess,  
[00:10:29] I think will end up being the most used one: quick, very natural to interact with,  
[00:10:40] natively multimodal, fitting throughout your day in the ways you want to interact with it.  
[00:10:47] I think you got a chance to play around with the new Meta AI app that we're releasing.  
[00:10:54] One of the fun things we put in there is the demo for the full-duplex voice. It's early.  
[00:11:01] There’s a reason why we haven't made that the default voice model in the app yet. But there's  
[00:11:05] something about how naturally conversational it is that's really fun and compelling.  
[00:11:12] Being able to mix that in with the right personalization is going to lead toward a  
[00:11:19] product experience where… If you fast-forward a few years, I think we're just going to be  
[00:11:25] talking to AI throughout the day about different things we're wondering about.  
[00:11:31] You'll have your phone. You'll talk to it while browsing your feed apps. It'll give you  
[00:11:36] context about different stuff. It'll answer your questions. It'll help you as you're interacting  
[00:11:40] with people in messaging apps. Eventually, I think we'll walk through our daily lives and  
[00:11:46] have glasses or other kinds of AI devices and just seamlessly interact with it all day long.  
[00:11:56] That’s the north star. Whatever the benchmarks are that lead toward people feeling like the  
[00:12:03] quality is where they want to interact with it, that's what will ultimately matter the most to us.  
[00:12:11] I got a chance to play around with both Orion and also the Meta AI app, and the voice mode  
[00:12:16] was super smooth. It was quite impressive. On the point of what the different labs are  
[00:12:21] optimizing for — to steelman their view — I think a lot of them believe that once you fully automate  
[00:12:26] software engineering and AI research, then you can kick off an intelligence explosion. You would have  
[00:12:33] millions of copies of these software engineers replicating the research that happened between  
[00:12:37] Llama 1 and Llama 4 — that scale of improvement again — but in a matter of weeks or months rather  
[00:12:42] than years. So it really matters to just close the loop on the software engineer, and then you can be  
[00:12:48] the first to ASI. What do you make of that? I personally think that's pretty compelling.  
[00:12:54] That's why we have a big coding effort too. We're working on  
[00:12:57] a number of coding agents inside Meta. Because we're not really an enterprise software company,  
[00:13:06] we're primarily building it for ourselves. Again, we go for a specific goal. We're not trying  
[00:13:13] to build a general developer tool. We're trying to build a coding agent and an AI research agent that  
[00:13:22] advances Llama research specifically. And it's fully plugged into our toolchain and all that.  
[00:13:32] That's important and is going to end up being an important part of how this stuff gets done.  
[00:13:38] I would guess that sometime in the next 12 to 18 months, we'll reach the point where most of  
[00:13:45] the code that's going toward these efforts is written by AI. And I don't mean autocomplete.  
[00:13:50] Today you have good autocomplete. You start writing something and it can complete a section  
[00:13:57] of code. I'm talking more like: you give it a goal, it can run tests, it can improve things,  
[00:14:05] it can find issues, it writes higher quality code than the average very good person on the  
[00:14:13] team already. I think that's going to be a really important part of this for sure.  
[00:14:21] But I don't know if that's the whole game. That's going to be a big industry, and it's going to be  
[00:14:28] an important part of how AI gets developed. But I think there are still… One way to think about it  
[00:14:36] is that this is a massive space. I don't think there's just going to be one company with one  
[00:14:42] optimization function that serves everyone as best as possible. There are going to be a bunch  
[00:14:51] of different labs doing leading work in different domains. Some will be more enterprise-focused or  
[00:14:52] coding-focused. Some will be more productivity-focused. Some will be  
[00:14:56] more social or entertainment-focused. Within the assistant space, there will  
[00:15:01] be some that are more informational and productivity-focused, and some that are  
[00:15:05] more companion-focused. It’s going to be a lot of stuff that’s just fun and  
[00:15:10] entertaining and shows up in your feed. There's just a huge amount of space. Part  
[00:15:16] of what's fun about going toward this AGI future is that there are a bunch of common threads for  
[00:15:24] what needs to get invented, but also a lot of things that still need to be created. I think  
[00:15:31] you're going to start seeing more specialization between different groups, if I had to guess.  
[00:15:35] It’s really interesting to me that you basically agree with the premise that  
[00:15:39] there will be an intelligence explosion and we’ll get something like superintelligence on  
[00:15:43] the other end. Tell me if I'm misunderstanding you. If that’s the case, why even bother with  
[00:15:48] personal assistants and whatever else? Why not just get to superhuman intelligence first and  
[00:15:51] then deal with everything else later? I think that's just one aspect of the  
[00:15:55] flywheel. Part of what I generally disagree with on the fast-takeoff view is that it takes  
[00:16:02] time to build out physical infrastructure. If you want to build a gigawatt cluster of  
[00:16:08] compute, that just takes time. NVIDIA needs time to stabilize their new generation of systems. Then  
[00:16:20] you need to figure out the networking around it. Then you need to build the building. You  
[00:16:24] need to get permitting. You need to get the energy. Maybe that means gas turbines or  
[00:16:33] green energy, either way, there’s a whole supply chain of that stuff.  
[00:16:37] We talked about this a bunch the last time I was on the podcast with you. I think some  
[00:16:42] of these are just physical-world, human-time things. As you start getting more intelligence  
[00:16:48] in one part of the stack, you’re just going to run into a different set of bottlenecks.  
[00:16:54] That’s how engineering always works: solve one bottleneck, you get another bottleneck.  
[00:17:00] Another bottleneck in the system or ingredient that’s going to make this work well, is people  
[00:17:08] getting used to learning and having a feedback loop with using the system. These systems don’t  
[00:17:25] just show up fully formed with people magically knowing how to use them. There's a co-evolution  
[00:17:34] that happens where people are learning how to best use these AI assistants. At the same time, the AI  
[00:17:42] assistants are learning what people care about. Developers are making the AI assistants better.  
[00:17:51] You're building up a base of context too. You wake up a year or two into it and the  
[00:17:57] assistant can reference things you talked about two years ago and that’s pretty cool.  
[00:18:01] You couldn’t do that even if you launched the perfect thing on day one. There’s no way it  
[00:18:05] could reference what you talked about two years ago if it didn’t exist two years ago.  
[00:18:07] So I guess my view is that there's this huge intelligence growth. There’s a very rapid curve  
[00:18:17] on the uptake of people interacting with the AI assistants, and the learning feedback and  
[00:18:23] data flywheel around that. And then there is also the buildout of the supply chains and  
[00:18:34] infrastructure and regulatory frameworks to enable the scaling of a lot of the physical  
[00:18:38] infrastructure. At some level, all of those are going to be necessary, not just the coding piece.  
[00:18:47] One specific example of this that I think is interesting. Even if you go back a few years ago,  
[00:18:52] we had a project, I think it was on our ads team, to automate ranking experiments. That's a pretty  
[00:19:00] constrained environment. It's not open-ended code. It’s basically, look at the whole history of the  
[00:19:06] company — every experiment that any engineer has ever done in the ad system — and look at what  
[00:19:13] worked, what didn't, and what the results of those were. Then basically formulate new hypotheses for  
[00:19:19] different tests that we should run that could improve the performance of the ad system.  
[00:19:25] What we basically found was that we were bottlenecked on compute to run tests,  
[00:19:31] based on the number of hypotheses. It turns out, even with just the humans we have right now  
[00:19:37] on the ads team, we already have more good ideas to test than we actually have either compute or,  
[00:19:46] really, cohorts of people to test them with. Even if you have three and a half billion people  
[00:19:52] using your products, you still want each test to be statistically significant. It needs to have  
[00:20:00] hundreds of thousands or millions of people. There's only so much throughput you can get on  
[00:20:09] testing through that. So we're already at the point, even with just the people we have, that  
[00:20:18] we can't really test everything that we want. Now just being able to test more things is not  
[00:20:23] necessarily going to be additive to that. We need to get to the point where the average quality of  
[00:20:27] the hypotheses that the AI is generating is better than all the things above the  
[00:20:33] line that we’re actually able to test that the best humans on the team have been able to do,  
[00:20:37] before it will even be marginally useful for it. We'll get there I think pretty quickly. But  
[00:20:47] it's not just, “Okay, cool, the thing can write code, and now all of a sudden  
[00:20:49] everything is just improving massively.” There are real-world constraints that need to be overcome.  
[00:21:00] Then you need to have the compute and the people to test. Then over time,  
[00:21:05] as the quality creeps up, are we here in five or 10 years where no set of people  
[00:21:11] can generate a hypothesis as good as the AI system? I don't know, maybe. In that world,  
[00:21:17] obviously that's going to be how all the value is created. But that's not the first step.  
[00:22:30] So if you buy this view, that this is where intelligence is headed,  
[00:22:35] the reason to be bullish on Meta is obviously that you have all this distribution. You can  
[00:22:40] also use that to learn more things that can be useful for training. You mentioned the  
[00:22:44] Meta AI app now has a billion active users. Not the app. The app is a standalone thing  
[00:22:51] that we're just launching now. It’ll be fun for people who want to use it. It's a cool  
[00:22:55] experience. We can talk about that too because we’re experimenting with some new ideas in there  
[00:22:59] that I think are novel and worth talking through. But I’m mostly talking about our apps. Meta AI  
[00:23:04] is actually most used in WhatsApp. WhatsApp is mostly used outside of the U.S. We just passed  
[00:23:12] like a hundred million people in the US, but it's not the primary messaging system in the US,  
[00:23:15] iMessage is. So people in the U.S. probably tend to underestimate Meta AI usage somewhat.  
[00:23:25] But part of the reason the standalone app is going to be so important is because the US,  
[00:23:29] for a lot of reasons, is one of the most important countries. And the fact that WhatsApp is the main  
[00:23:35] way people are using Meta AI and that's not the main messaging system in the US means  
[00:23:39] we need another way to build a first-class experience that's really in front of people.  
[00:23:45] And I guess, to finish the question, the bearish case would be that if the future of AI is less  
[00:23:51] about just answering your questions and more about being a virtual coworker, then it's not  
[00:23:56] clear how Meta AI inside of WhatsApp gives you the relevant training data to make a  
[00:24:03] fully autonomous programmer or remote worker. In that case, does it not matter that much who  
[00:24:12] has more distribution right now with LLMs? Again, I just think there are going to be  
[00:24:15] different things. Imagine you were sitting at the beginning of the development of the  
[00:24:20] internet and you asked, "What's going to be the main internet thing? Is it going  
[00:24:24] to be knowledge work or massive consumer apps?" You got both. You don’t have to choose one. The  
[00:24:33] world is big and complicated. Does one company build all of that stuff? Normally the answer is  
[00:24:38] no. But to your question, people do not code in WhatsApp for the most part. And I don't foresee  
[00:24:47] that people starting to write code in WhatsApp is going to be a major use case. Although I do  
[00:24:54] think people are going to ask AI to do a lot of things that result in the AI coding without them  
[00:24:58] necessarily knowing it. That's a separate thing. We do have a lot of people who are writing code  
[00:25:05] at Meta and they use Meta AI. We have this internal thing called MetaMate,  
[00:25:11] and a number of different coding and AI research agents that we're building around that. That has  
[00:25:19] its own feedback loop and I think it can get quite good for accelerating those efforts.  
[00:25:23] But again, there are going to be a lot of things. AI is almost certainly going to unlock a massive  
[00:25:31] revolution in knowledge work and code. I also think it’s going to be the next generation of  
[00:25:38] search and how people get information, and do more complex information tasks.  
[00:25:44] I also think it's going to be fun. People are going to use it to be entertained. A lot of the  
[00:25:52] internet today is memes and humor. We have this amazing technology at our fingertips. It’s amazing  
[00:25:59] and funny when you think about how much of human energy just goes toward entertaining ourselves,  
[00:26:04] designing, pushing culture forward, and finding humorous ways to explain cultural  
[00:26:09] phenomena that we observe. I think that's almost certainly going to be the case in the future.  
[00:26:15] Look at the evolution of things like Instagram and Facebook. If you go back 10, 15, 20 years ago,  
[00:26:22] it was text. Then we all got phones with cameras, and most of the content became photos. Then the  
[00:26:30] mobile networks got good enough that if you wanted to watch a video on your phone, it wasn't  
[00:26:34] just buffering the whole time. So that got good. Over the last 10 years, most of the content has  
[00:26:39] moved toward video at this point. Today, most of the time spent on Facebook and Instagram  
[00:26:43] is on video. But do you think in five years we’re just going to be sitting in our feed and consuming  
[00:26:50] media that's just video? No, it's going to be interactive. You'll be scrolling through your  
[00:26:54] feed. There will be content that maybe looks like a Reel to start. But you can talk to it,  
[00:27:02] or interact with it, and it talks back, or it changes what it's doing. Or you can  
[00:27:05] jump into it like a game and interact with it. That's all going to be AI.  
[00:27:11] My point is that there are going to be all these different things. We're ambitious,  
[00:27:17] so we're working on a bunch of them. But I don't think any one company is going to do all of it.  
[00:27:22] On this point about AI-generated content and AI interactions, already people have  
[00:27:28] meaningful relationships with AI therapists, AI friends, maybe more. This is just going to  
[00:27:34] get more intense as these AIs become more unique, more personable, more intelligent,  
[00:27:40] more spontaneous, more funny, and so forth. People are going to have relationships with  
[00:27:44] AI. How do we make sure these are healthy relationships?  
[00:27:48] There are a lot of questions that you only can really answer as you start seeing the behaviors.  
[00:27:54] Probably the most important upfront thing is just to ask that question and care about it at  
[00:27:58] each step along the way. But I also think being too prescriptive upfront and saying, "We think  
[00:28:03] these things are not good" often cuts off value. People use stuff that's valuable for them. One  
[00:28:12] of my core guiding principles in designing products is that people are smart. They know  
[00:28:18] what's valuable in their lives. Every once in a while, something bad happens  
[00:28:24] in a product and you want to make sure you design your product well to minimize that.  
[00:28:29] But if you think something someone is doing is bad and they think it's really valuable,  
[00:28:36] most of the time in my experience, they're right and you're wrong. You just haven't come up with  
[00:28:41] the framework yet for understanding why the thing they're doing is valuable and helpful in their  
[00:28:45] life. That's the main way I think about it. I do think people are going to use AI for a  
[00:28:55] lot of these social tasks. Already, one of the main things we see people using Meta AI for is  
[00:29:00] talking through difficult conversations they need to have with people in their lives. "I'm  
[00:29:09] having this issue with my girlfriend. Help me have this conversation.” Or, "I need to have a  
[00:29:13] hard conversation with my boss at work. How do I have that conversation?" That's pretty helpful.  
[00:29:20] As the personalization loop kicks in and the AI starts to get to know you better and better,  
[00:29:28] that will just be really compelling. Here’s one stat from working on social media  
[00:29:35] for a long time that I always think is crazy. The average American has fewer than three friends,  
[00:29:46] fewer than three people they would consider friends. And the average person has demand for  
[00:29:51] meaningfully more. I think it's something like 15 friends or something. At some point you're like,  
[00:29:56] "All right, I'm just too busy, I can't deal with more people."  
[00:29:58] But the average person wants more connection than they have. There's a lot of concern people  
[00:30:07] raise like, "Is this going to replace real-world, in-person connections?" And my default  
[00:30:18] is that the answer to that is probably not. There are all these things that are better  
[00:30:24] about physical connections when you can have them. But the reality is that people just don't  
[00:30:30] have as much connection as they want. They feel more alone a lot of the time than they would like.  
[00:30:35] So I think a lot of these things — things that today might have a little bit of stigma around  
[00:30:43] them — over time, we'll find the vocabulary as a society to articulate why they are valuable,  
[00:30:51] why the people who are doing them are rational for doing it, and how it is actually adding value to  
[00:30:58] their lives. But also the field is very early. There are a handful of companies doing virtual  
[00:31:06] therapists, virtual girlfriend-type stuff. But it's very early. The embodiment in those things  
[00:31:15] is still pretty weak. You open it up and it's just an image of the therapist or the person  
[00:31:22] you're talking to. Sometimes there's some very rough animation, but it's not an embodiment.  
[00:31:28] You've seen the stuff we're working on in Reality Labs, where you have the Codec Avatars and it  
[00:31:32] actually feels like a real person. That's where it's going. You'll be able to have an  
[00:31:38] always-on video chat with the AI. The gestures are important too. More than half of communication,  
[00:31:49] when you're actually having a conversation, is not the words you speak. It's all the nonverbal stuff.  
[00:31:54] I did get a chance to check out Orion the other day, and I thought it was super impressive. I'm  
[00:31:59] mostly optimistic about the technology. Generally, like you mentioned, I'm pretty libertarian  
[00:32:04] about this. If people are doing something, they probably think it's good for them. Although,  
[00:32:07] I actually don't know if it's the case that if somebody is using TikTok,  
[00:32:09] they would say that they're happy with how much time they're spending on TikTok or something.  
[00:32:12] I'm mostly optimistic about it in the sense that if we're going to be living in this future world  
[00:32:16] of AGI, we need to be upgrading our capabilities too, with tools like this. And just generally,  
[00:32:23] there can be more beauty in the world if you can see Studio Ghibli everywhere or something.  
[00:32:26] I was worried about one of the flagship use cases that your team showed me. I'm sitting  
[00:32:33] at the breakfast table and on the periphery of my vision is just a bunch of Reels that are scrolling  
[00:32:37] by. Maybe in the future, my AI girlfriend is on the other side of the screen or something. So  
[00:32:43] I am worried that we're just removing all the friction between getting totally reward-hacked  
[00:32:49] by our technology. How do we make sure this is not what ends up happening in five years?  
[00:32:57] Again, I think people have a good sense of what they want. That experience you saw was just a  
[00:33:02] demo to show multitasking and holograms. I agree, I don't think the future is one where you have  
[00:33:11] stuff that's trying to compete for your attention in the corner of your vision all the time. I don't  
[00:33:15] think people would like that too much. As we're designing these glasses,  
[00:33:22] it's actually one of the things that we're really mindful of. Probably the number one thing the  
[00:33:28] glasses need to do is get out of the way and be good glasses. As an aside, I think that's part  
[00:33:36] of the reason why the Ray-Ban Meta product has done so well. It's great for listening to music,  
[00:33:44] taking phone calls, taking photos and videos. The AI is there when you want it. But when you don't,  
[00:33:51] it's just a good-looking pair of glasses that people like. It gets out of the way well.  
[00:34:00] I would guess that's going to be a very important design principle for the augmented reality future.  
[00:34:10] The main thing that I see here is this. It's kind of crazy that, for how important the digital world  
[00:34:19] is in all of our lives, the only way we access it is through these physical, digital screens. You  
[00:34:29] have your phone, your computer. You can put a big TV on your wall. It's this huge physical thing.  
[00:34:36] It just seems like we're at the point with technology where the physical and digital  
[00:34:43] world should really be fully blended. That's what holographic overlays allow you to do. But  
[00:34:50] I agree. I think a big part of the design principles around that will be around how  
[00:34:56] you'll be interacting with people. You'll be able to bring digital artifacts into those interactions  
[00:35:01] and do cool things very seamlessly. If I want to show you something,  
[00:35:06] here’s a screen. We can interact with it. It can be 3D. We can play with it. You want to  
[00:35:15] play a card game? All right, here’s a deck of cards. We can play with it. If two of us are  
[00:35:20] physically together and we have a third friend who’s hologramming in, they can participate too.  
[00:35:29] But in that world too — just as you don't want your physical space to be cluttered because it  
[00:35:39] wears on you psychologically — I don't think people are going to want their digital-physical  
[00:35:44] space to feel that way either. That's more of an aesthetic norm that will have to get worked out,  
[00:35:50] but I think we’ll figure that out. Going back to the AI conversation,  
[00:35:58] you were mentioning how big of a bottleneck the physical infrastructure can be. Related  
[00:36:03] to other open-source models, like DeepSeek and so forth, DeepSeek right now has less compute  
[00:36:08] than a lab like Meta and you could argue that it's competitive with the Llama models.  
[00:36:13] If China is better at physical infrastructure, industrial scale-ups,  
[00:36:18] getting more power and more data centers online, how worried are you that they might beat us here?  
[00:36:25] It's a real competition. You're seeing industrial policies really play out. China is bringing online  
[00:36:36] more power. Because of that, the US really needs to focus on streamlining the ability to build  
[00:36:45] data centers and produce energy. Otherwise, I think we’ll be at a significant disadvantage.  
[00:36:53] At the same time, some of the export controls on things like chips, I think you can see how  
[00:36:57] they’re clearly working in a way. There was all the conversation with DeepSeek about, "Oh,  
[00:37:04] they did all these very impressive low-level optimizations." And the  
[00:37:10] reality is, they did and that is impressive. But then you ask, "Why did they have to do that,  
[00:37:16] when none of the American labs did it?" It’s because they’re using partially nerfed chips  
[00:37:21] that are the only ones NVIDIA is allowed to sell in China because of the export  
[00:37:26] controls. DeepSeek basically had to spend a bunch of their calories and time doing  
[00:37:34] low-level infrastructure optimizations that the American labs didn’t have to do.  
[00:37:40] Now, they produced a good result on text. DeepSeek is text-only. The infrastructure is impressive.  
[00:37:49] The text result is impressive. But every new major model that comes out now is multimodal.  
[00:37:58] It's image, it's voice. Theirs isn't. Now the question is, why is that the  
[00:38:05] case? I don’t think it’s because they’re not capable of doing it. It's because they  
[00:38:09] had to spend their calories on doing these infrastructure optimizations to overcome the  
[00:38:13] fact that there were these export controls. But when you compare Llama 4 with DeepSeek —I  
[00:38:19] mean our reasoning model isn’t out yet, so the R1 comparison isn’t clear yet— but we’re basically  
[00:38:27] in the same ballpark on all the text stuff that DeepSeek is doing but with a smaller model. So  
[00:38:38] the cost-per-intelligence is lower with what we’re doing for Llama on text. On  
[00:38:42] the multimodal side we’re effectively leading at and it just doesn’t exist in their models.  
[00:38:47] So the Llama 4 models, when you compare them to what DeepSeek is doing, are good. I think  
[00:38:57] people will generally prefer to use the Llama 4 models. But there’s this interesting contour  
[00:39:03] where it’s clearly a good team doing stuff over there. And you're right to ask about the  
[00:39:10] accessibility of power, the accessibility of compute and chips, because the work that you're  
[00:39:16] seeing different labs do and the way it's playing out is somewhat downstream of that.  
[00:40:34] So Sam Altman recently tweeted that OpenAI is going to release an open-source SOTA reasoning  
[00:40:41] model. I think part of the tweet was that they won’t do anything silly, like say you can only  
[00:40:46] use it if you have less than 700 million users. DeepSeek has the MIT license, whereas I think  
[00:40:55] a couple of the contingencies in the Llama license require you to say "built with Llama"  
[00:40:58] on applications using it or any model that you train using Llama has to begin with the word  
[00:41:02] "Llama." What do you think about the license? Should it be less onerous for developers?  
[00:41:07] Look, we basically pioneered the open-source LLM thing. So I don't consider the license to  
[00:41:17] be onerous. When we were starting to push on open source, there was this big debate in the industry.  
[00:41:28] Is this even a reasonable thing to do? Can you do something that is safe and trustworthy with  
[00:41:34] open source? Will open source ever be able to be competitive enough that anyone will even care?  
[00:41:42] Basically, when we were answering those questions a lot of the hard work was  
[00:41:47] done by the teams at Meta. There were other folks in the industry but really,  
[00:41:50] the Llama models were the ones that broke open this whole open-source AI thing in a huge way.  
[00:42:00] If we’re going to put all this energy into it, then at a minimum, if you're going to have these  
[00:42:07] large cloud companies — like Microsoft and Amazon and Google — turn around and sell our model,  
[00:42:12] then we should at least be able to have a conversation with them before they do that around  
[00:42:20] what kind of business arrangement we should have. Our goal with the license, we're generally not  
[00:42:27] trying to stop people from using the model. We just think that if you're one of those companies,  
[00:42:31] or if you're Apple, just come talk to us about what you want to do. Let's find  
[00:42:38] a productive way to do it together. I think that’s generally been fine.  
[00:42:42] Now, if the whole open-source part of the industry evolves in a direction where there  
[00:42:49] are a lot of other great options and the license ends up being a reason why people don’t want to  
[00:42:56] use Llama, then we’ll have to reevaluate the strategy. What it makes sense to do  
[00:43:01] at that point. But I don’t think we’re there. That’s not, in practice, something we’ve seen,  
[00:43:08] companies coming to us and saying, “We don’t want to use this because your license says if you reach  
[00:43:15] 700 million people, you have to come talk to us.” So far, that’s been more something we’ve heard  
[00:43:21] from open-source purists like, “Is this as clean of an open-source model as you’d like it to be?”  
[00:43:32] That debate has existed since the beginning of open source. All the GPL license stuff  
[00:43:41] versus other things, do you need to make it so that anything that touches open source has  
[00:43:47] to be open source too? Or can people take it and use it in different ways? I'm sure  
[00:43:51] there will continue to be debates around this. But if you’re spending many billions of dollars  
[00:43:56] training these models, I think asking the other companies — the huge ones that are similar in size  
[00:44:03] and can easily afford to have a relationship with us — to talk to us before they use  
[00:44:08] it seems like a pretty reasonable thing. If it turns out that other models are also  
[00:44:15] really good. There’s a bunch of good open-source models. So that part of your mission is fulfilled,  
[00:44:19] and maybe other models are better at coding. Is there a world where you just say, "Look, the  
[00:44:24] open-source ecosystem is healthy. There’s plenty of competition. We're happy to just use some  
[00:44:29] other model, whether it's for internal software engineering at Meta or deploying to our apps.  
[00:44:34] We don't necessarily need to build with Llama"? Again, we do a lot of things. Let's take a step  
[00:44:44] back. The reason why we're building our own big models is because we want to be able to  
[00:44:51] build exactly what we want. None of the other models in the world are exactly what we want.  
[00:44:57] If they're open source, you can take them and fine-tune them in different ways. But you still  
[00:45:01] have to deal with the model architectures. And they make different size tradeoffs that  
[00:45:08] affect latency and inference cost. At the scale that we operate at, that stuff really matters.  
[00:45:15] We made the Llama Scout and Maverick models certain sizes for a specific reason. They  
[00:45:22] fit on a host and we wanted certain latency — especially for the voice models that we’re  
[00:45:27] working on — that we want to pervade everything we're doing from the glasses to all of our apps  
[00:45:33] to the Meta AI app and all that stuff. There's a level of control of your own  
[00:45:40] destiny that you only get when you build the stuff yourself. That said, AI is going to be used in  
[00:45:47] every single thing that every company does. When we build a big model, we also have to choose which  
[00:45:52] internal use cases we're going to optimize for. So does that mean for certain things we might say,  
[00:45:59] "Okay, maybe Claude is better for building this specific development tool that this team is  
[00:46:04] using”? All right, cool then use that. Great. We don’t want to fight with one hand tied behind our  
[00:46:09] back. We’re doing a lot of different stuff. You also asked, would it not be  
[00:46:16] important anymore because other people are doing open source? On this, I'm a little more worried.  
[00:46:24] You have to ask yourself this. For anyone who shows up now and is doing open source — now  
[00:46:29] that we have done it — would they still be doing open source if we weren’t doing it?  
[00:46:37] I think there are a handful of folks who see the trend that more and more development is  
[00:46:41] going toward open source, and they're like, "Oh crap, we need to be on this train or else we’re  
[00:46:47] going to lose." If you have a closed-model API and increasingly a lot of developers don't want that.  
[00:46:55] So you’re seeing a bunch of other players start to do some work in open source. But it's unclear  
[00:47:02] if it's dabbling, or fundamental for them the way that it has been for us. A good example is  
[00:47:08] what's going on with Android. Android started off as the open-source thing. There's not  
[00:47:14] really any open-source alternative. Over time, Android has just gotten more and more closed.  
[00:47:21] So if you're us, you need to worry that if we stop pushing the industry in this direction,  
[00:47:31] all these other people… Maybe they’re only really doing it because they're trying to compete with  
[00:47:36] us and the direction we’re pushing things. They already showed their revealed preference for what  
[00:47:43] they would do if open source didn’t exist. And it wasn’t open source. We just need to  
[00:47:50] be careful about relying on that continued behavior for the future of the technology  
[00:47:57] that we're going to build at the company. Another thing I've heard you mention is that  
[00:48:00] it's important that the standard gets built around American models like Llama. I wanted to understand  
[00:48:07] your logic there. With certain kinds of networks, it is the case that the Apple App Store just has  
[00:48:13] a big contingency around what it's built around. But it doesn't seem like if you built some sort  
[00:48:19] of scaffold for DeepSeek, you couldn't have easily just switched it over to Llama 4,  
[00:48:24] especially since between generations. Llama 3 wasn't MoE and Llama 4 is. So things are  
[00:48:28] changing between generations of models as well. What’s the reason for thinking things will get  
[00:48:31] built out in this contingent way on a specific standard?  
[00:48:34] I'm not sure, what do you mean by contingent? As in, it's important that people are building  
[00:48:38] for Llama rather than for LLMs in general, because that will determine  
[00:48:42] what the standard is in the future. Look, I think these models encode  
[00:48:47] values and ways of thinking about the world. We had this interesting experience early on, where  
[00:48:55] we took an early version of Llama and translated it. I think it was French, or some other language.  
[00:49:04] The feedback we got from French people was, "This sounds like an American who  
[00:49:12] learned to speak French. It doesn’t sound like a French person." And we were like,  
[00:49:15] “what do you mean, does it not speak French well?” No, it speaks French fine. It was just  
[00:49:19] that the way it thought about the world seemed slightly American. So I think there are these  
[00:49:27] subtle things that get built into the models. Over time, as models get more sophisticated,  
[00:49:33] they should be able to embody different value sets across the world. So maybe that's  
[00:49:40] not a particularly sophisticated example, but I think it illustrates the point.  
[00:49:48] Some of the stuff we've seen in testing some of the models, especially coming out of China,  
[00:49:55] have certain values encoded in them. And it’s not just a light fine-tune to change that. Now,  
[00:50:06] language models — or something that has a kind of world model embedded in it — have more values.  
[00:50:14] Reasoning, I guess, you could say has values too. But one of the nice things about reasoning models  
[00:50:23] is they're trained on verifiable problems. Do you need to be worried about cultural bias if your  
[00:50:29] model is doing math? Probably not. I think the chance that some reasoning model built  
[00:50:38] elsewhere is going to incept you by solving a math problem in a devious way seems low.  
[00:50:49] But there's a whole different set of issues around coding, which is the other verifiable  
[00:50:53] domain. You need to worry about waking up one day and if you're using a model that has some tie to  
[00:51:03] another government, can it embed vulnerabilities in code that their intelligence organizations  
[00:51:11] could exploit later? In some future version you're using a model that came from another country  
[00:51:25] and it's securing your systems. Then you wake up and everything is just vulnerable in a way  
[00:51:29] that that country knows about and you don’t. Or it turns on a vulnerability at some point.  
[00:51:35] Those are real issues. I'm very interested in studying this because I think one of the main  
[00:51:46] things that's interesting about open source is the ability to distill models. For most people,  
[00:51:52] the primary value isn't just taking a model off the shelf and saying, "Okay, Meta built  
[00:51:57] this version of Llama. I'm going to take it and I'm going to run it exactly in my application."  
[00:52:01] No, your application isn't doing anything different if you're just running our thing.  
[00:52:04] You're at least going to fine-tune it, or try to distill it into a different model. When we get to  
[00:52:09] stuff like the Behemoth model, the whole value is being able to take this very high amount of  
[00:52:15] intelligence and distill it down into a smaller model that you're actually going to want to run.  
[00:52:20] This is the beauty of distillation. It's one of the things that I think has really emerged as a  
[00:52:24] very powerful technique over the last year, since the last time we sat down. I think it’s worked  
[00:52:30] better than most people would have predicted. You can basically take a model that's much bigger, and  
[00:52:36] capture probably 90 or 95% of its intelligence, and run it in something that's 10% of the size.  
[00:52:41] Now, do you get 100% of the intelligence? No. But 95% of the intelligence at 10% of  
[00:52:47] the cost is pretty good for a lot of things. The other thing that's interesting is that now,  
[00:52:53] with this more varied open-source community, it's not just Llama. You have other models too. You  
[00:52:59] have the ability to distill from multiple sources. So now you can basically say, "Okay, Llama’s  
[00:53:05] really good at this. Maybe its architecture is really good because it's fundamentally multimodal,  
[00:53:10] more inference-friendly, more efficient. But let’s say this other model is better at coding." Okay,  
[00:53:17] great. You can distill from both of them and build something that's better than either  
[00:53:21] individually, for your own use case. That's cool. But you do need to solve the security problem of  
[00:53:28] knowing that you can distill it in a way that's safe and secure. This is something that we've  
[00:53:33] been researching and have put a lot of time into. What we've basically found is that anything that's  
[00:53:40] language is quite fraught. There's just a lot of values embedded into it. Unless you don't care  
[00:53:46] about taking on the values from whatever model you're distilling from, you probably don't want  
[00:53:50] to just distill a straight language world model. On reasoning, though, you can get a lot of the way  
[00:53:59] there by limiting it to verifiable domains, and running code cleanliness and security filters.  
[00:54:09] Whether it's using Llama Guard open source, or the Code Shield open source tools that  
[00:54:12] we've done, things that allow you to incorporate different input into your models and make sure  
[00:54:19] that both the input and the output are secure. Then it’s just a lot of red teaming. It’s  
[00:54:27] having experts who are looking at the model and asking, "Alright, is this model doing  
[00:54:30] anything after distillation that we don't want?" I think with the combination of those techniques,  
[00:54:37] you can probably distill on the reasoning side for verifiable domains quite securely.  
[00:54:44] That's something I'm pretty confident about and something we've done a lot of research around.  
[00:54:48] But I think this is a very big question. How do you do good distillation? Because there’s  
[00:54:54] so much value to be unlocked. But at the same time, I do think there is some fundamental  
[00:54:58] bias embedded in different models. Speaking of value to be unlocked,  
[00:55:01] what do you think the right way to monetize AI will be? Obviously digital ads are quite  
[00:55:07] lucrative. But as a fraction of total GDP, it's small compared to all remote work.  
[00:55:14] Even if you can increase productivity without replacing work, that's still worth tens of  
[00:55:18] trillions of dollars. Is it possible that ads might not be it? How do you think about this?  
[00:55:23] Like we were talking about before, there's going to be all these different applications,  
[00:55:26] and different applications tend toward different things.  
[00:55:29] Ads are great when you want to offer people a free service. Because it's free,  
[00:55:34] you need to cover it somehow. Ads solve this problem where a person does not need to pay for  
[00:55:40] something. They can get something that is amazing for free. Also by the way, with modern ad systems,  
[00:55:48] a lot of the time people think the ads add value to the thing if you do it well.  
[00:55:55] You need to be good at ranking and you need to have enough liquidity of advertising inventory.  
[00:56:01] If you only have five advertisers in the system, no matter how good you are at ranking,  
[00:56:04] you may not be able to show something to someone that they're interested in. But if  
[00:56:07] you have a million advertisers in the system, then you're probably going to be able to find  
[00:56:11] something pretty compelling, if you're good at picking out the different needles in the haystack  
[00:56:16] that that person is going to be interested in. So that definitely has its place. But there are  
[00:56:23] also clearly going to be other business models as well, including ones that  
[00:56:30] just have higher costs so it doesn't even make sense to offer them for free. By the way,  
[00:56:35] there have always been business models like this. There's a reason why social media is free and  
[00:56:39] ad-supported, but then if you want to watch Netflix or ESPN or something,  
[00:56:46] you need to pay for that. The content that's going into that, they need to produce it, and that's  
[00:56:50] very expensive for them to produce. They probably could not have enough ads in the service in order  
[00:56:55] to make up for the cost of producing the content. Basically, you just need to pay to access it.  
[00:57:02] The trade-off is fewer people do it. Instead of billions, you're talking about hundreds of  
[00:57:05] millions of people using those services. There's a value switch there. I think it's similar here. Not  
[00:57:14] everyone is going to want a software engineer, or a thousand software engineering agents,  
[00:57:19] or whatever it is. But if you do, that's something you're probably going to be willing  
[00:57:23] to pay thousands, or tens of thousands, or hundreds of thousands of dollars for.  
[00:57:30] That just speaks to the diversity of different things that need to get created.  
[00:57:35] There are going to be business models at each point along the spectrum. At Meta,  
[00:57:42] for the consumer piece we definitely want to have a free thing. I'm sure that will end up  
[00:57:46] being ad-supported. But I also think we're going to want to have a business model that supports  
[00:57:51] people using arbitrary amounts of compute to do even more amazing things than what it would make  
[00:57:58] sense to offer in the free service. For that, I'm sure we'll end up having a premium service. But  
[00:58:05] I think our basic values on this are that we want to serve as many people in the world as possible.  
[00:59:18] How do you keep track of all these different projects, some of which we've talked about  
[00:59:23] today. I'm sure there are many I don't even know about. As the CEO overseeing everything,  
[00:59:30] there's a big spectrum between going to the Llama team and saying, "Here are the  
[00:59:32] hyperparameters you should use," versus just giving a mandate like, "Go make the AI better."  
[00:59:36] And there are so many different projects. How do you think about  
[00:59:39] the way in which you can best deliver your value-add and oversee all these things?  
[00:59:45] A lot of what I spend my time on is trying to get awesome people onto the teams. There's that,  
[00:59:51] and then there's stuff that cuts across teams. You build Meta AI, and you want to  
[00:59:57] get it into WhatsApp or Instagram. Okay, now I need to get those teams to talk together.  
[01:00:03] Then there are a bunch of questions like, “do you want the thread for Meta AI in WhatsApp  
[01:00:13] to feel like other WhatsApp threads, or do you want it to feel like other AI chat experiences?”  
[01:00:19] There are different idioms for those. So there are all these interesting questions that need  
[01:00:24] to get answered around how does this stuff basically fit into everything we're doing?  
[01:00:29] Then there's a whole other part of what we're doing, which is pushing on the infrastructure.  
[01:00:33] If you want to stand up a gigawatt cluster, first of all, that has a lot of implications for  
[01:00:41] the way we're doing infrastructure buildouts. It has political implications for how you engage  
[01:00:47] with the different states where you're building that stuff. It has financial implications for  
[01:00:52] the company in terms of: "All right, there's a lot of economic uncertainty in the world. Do we  
[01:00:57] double down on infrastructure right now? If so, what other trade-offs do we want to make around  
[01:01:03] the company?" Those are the kinds of decisions that are tough for other people to really make.  
[01:01:11] Then there's this question around taste and quality. When is something good enough that  
[01:01:19] we want to ship it? In general, I'm the steward of that for the company. Although we have a lot  
[01:01:28] of other people who I think have good taste as well and are also filters for different things.  
[01:01:35] Those are basically the areas. AI is interesting because, more than some of the other stuff that we  
[01:01:42] do, it is more research and model-led than really product-led. You can't just design the product  
[01:01:48] that you want and then try to build the model to fit into it. You really need to design the model  
[01:01:55] first and the capabilities that you want, and then you get some emergent properties. Then it's,  
[01:01:59] "Oh, you can build some different stuff because this turned out in a certain way." At the end  
[01:02:04] of the day, people want to use the best model. That's partially why, when we're talking about  
[01:02:10] building the most personal AI, the best voice, the best personalization — and also a very smart  
[01:02:20] experience with very low latency — those are the things that we need to design the whole  
[01:02:25] system to build. That's why we're working on full-duplex voice. That's why we're working  
[01:02:28] on personalization to both have good memory extraction from your interactions with AI,  
[01:02:35] but also to be able to plug into all the other Meta systems. That's why we design the  
[01:02:41] specific models that we design, to have the kind of size and latency parameters that they do.  
[01:02:46] Speaking of politics, there's been this perception that some tech leaders have been  
[01:02:53] aligning with Trump. You and others donated to his inaugural event and were on stage  
[01:02:57] with him and I think you settled a lawsuit that resulted in them getting $25 million.  
[01:03:02] I wonder what's going on here? Does it feel like the cost of doing business with an administration?  
[01:03:09] What's the best way to think about this? My view on this is that he's the President  
[01:03:14] of the United States. Our default, as an American company, should be to try to have a productive  
[01:03:19] relationship with whoever is running the government. We've tried to offer support  
[01:03:26] to previous administrations as well. I've been pretty public with some of my frustrations  
[01:03:31] with the previous administration, how they basically did not engage  
[01:03:35] with us or the business community more broadly. Frankly, that’s going to be necessary to make  
[01:03:41] progress on some of these things. We're not going to be able to build the level of energy that we  
[01:03:47] need if you don't have a dialogue, and if they're not prioritizing trying to do those things.  
[01:03:54] A lot of people want to write this story about what direction people are going. We're trying  
[01:04:03] to build great stuff, and we want to have a productive relationship with people. That's how I  
[01:04:10] see it. It is also how I would guess most others see it, but obviously, I can't speak for them.  
[01:04:20] You've spoken out about how you've rethought some of the ways in which you  
[01:04:25] engage and defer to the government, in terms of moderation stuff in the past.  
[01:04:29] How are you thinking about AI governance? Because if AI is as powerful as we think it might be,  
[01:04:34] the government will want to get involved. What is the most productive approach to take there,  
[01:04:38] and what should the government be thinking about? I guess in the past, most of the comments that I  
[01:04:45] made were in the context of content moderation. It's been an interesting journey over the  
[01:04:51] last 10 years on this. It's obviously been an interesting time in history. There have been novel  
[01:04:57] questions raised about online content moderation. Some of those have led to productive new systems  
[01:05:04] getting built, like our AI systems to detect nation-states trying to interfere in each other's  
[01:05:11] elections. I think we will continue building that stuff out, and that has been net positive.  
[01:05:16] With some other stuff, we went down some bad paths. I just think the fact-checking  
[01:05:21] thing was not as effective as Community Notes because it's not an internet-scale solution.  
[01:05:26] There weren't enough fact-checkers, and people didn't trust the specific fact-checkers. You  
[01:05:30] want a more robust system. So I think what we got with Community Notes is the right one on that.  
[01:05:35] But my point on this was more that historically, I probably deferred a little too much to  
[01:05:48] either the media and their critiques, or to the government, on things that they did not really  
[01:05:56] have authority over. But just as like a central figure, I think we tried to build systems where  
[01:06:05] maybe we wouldn't have to make all of the content moderation decisions ourselves or something.  
[01:06:12] I guess part of the growth process over the last 10 years is realizing, “Okay, we're a meaningful  
[01:06:19] company. We need to own the decisions that we need to make. We should listen to feedback from people,  
[01:06:24] but we shouldn't defer too much to people who do not actually have authority over this. Because  
[01:06:29] at the end of the day, we're in the seat, and we need to own the decisions that we make.”  
[01:06:37] It's been a maturation process, and in some ways painful, but I think we're  
[01:06:43] probably a better company for it. Will tariffs increase the cost of  
[01:06:47] building data centers in the US and shift buildouts to Europe and Asia?  
[01:06:50] It is really hard to know how that plays out. I think we're probably in the early  
[01:06:55] innings on that, and it's very hard to know. What is your single highest-leverage hour in  
[01:07:04] a week? What are you doing in that hour? I don't know. Every week is a little bit  
[01:07:08] different. It's probably got to be the case that the most leveraged thing you do in a  
[01:07:13] week is not the same thing each week. Or else, by definition, you should probably spend more  
[01:07:17] than one hour doing that thing every week. I don't know. Part of the fun of this job,  
[01:07:27] and also of the industry being so dynamic, is that things really move around. The world is  
[01:07:35] very different now than it was at the beginning of the year, or even six months ago, or in the  
[01:07:40] middle of last year. I think a lot has advanced meaningfully. A lot of cards have been turned  
[01:07:46] over since the last time that we sat down. I think that was about a year ago, right?  
[01:07:48] Yeah. I guess what you were saying earlier that recruiting people is a  
[01:07:51] super high-leverage thing you do. It's very high-leverage, yeah.  
[01:07:56] You talked about these models being mid-level software engineers by the end of the year.  
[01:08:01] What would be possible if, say, software productivity increased like 100x in two  
[01:08:06] years? What kinds of things could be built that can't be built right now?  
[01:08:09] What kinds of things? That's an interesting question. One theme of this conversation is  
[01:08:18] that the amount of creativity that's going to be unlocked is going to be massive.  
[01:08:25] If you look at the overall arc of human society and the economy over 100 or 150 years,  
[01:08:35] it's basically people going from being primarily agrarian — with most human energy going toward  
[01:08:41] just feeding ourselves — to that becoming a smaller and smaller percent. And the things that  
[01:08:49] take care of our basic physical needs have become a smaller and smaller percent of human energy.  
[01:08:54] That shift has led to two impacts: one is that more people are doing creative and cultural  
[01:09:00] pursuits. The second is that more people, in general, spend less time working and more time on  
[01:09:08] entertainment and culture. I think that is almost certainly going to continue as this goes on.  
[01:09:15] This isn't the 1-2 year thing of what happens when you have a super powerful software engineer. But  
[01:09:22] over time, if everyone has these superhuman tools to create a ton of different stuff,  
[01:09:28] you're going to get incredible diversity. Part of it is going to be solving hard problems:  
[01:09:38] solving diseases, advancing science, developing new technology that makes our lives better.  
[01:09:48] But I would guess that a lot of it is going to end up being cultural and social pursuits  
[01:09:54] and entertainment. I would guess the world is going to get a lot funnier,  
[01:10:02] weirder, and quirkier, the way that memes on the internet have gotten over the last 10 years.  
[01:10:10] I think that adds a certain richness and depth. In funny ways, it actually helps you  
[01:10:17] connect better with people. Now all day long, I just find interesting stuff on the internet  
[01:10:24] and send it in group chats to the people I care about, who I think are going to find it funny.  
[01:10:29] The media that people can produce today to express very nuanced,  
[01:10:34] specific cultural ideas is really cool. That'll continue to get built out. It does  
[01:10:44] advance society in a bunch of ways, even if it's not the "hard science" way of curing a disease.  
[01:10:52] If you think about it, the Meta social media view of the world is that yeah,  
[01:10:56] people are going to spend a lot more time doing that stuff in the future. It's going to be a lot  
[01:11:01] better, and it's going to help you connect, because it'll help express different ideas.  
[01:11:06] The world is going to get more complicated, but our technology, our cultural technology, to  
[01:11:10] express these very complicated things — in a very kind of funny little clip or whatever — is going  
[01:11:17] to get so much better. I think that's all great. I don't know about next year. One other thought  
[01:11:29] that I think is interesting to cover is that I tend to think that, for at least  
[01:11:35] the foreseeable future, this is going to lead to more demand for people doing work,  
[01:11:42] not less. Now, people have a choice of how much time they want to spend working.  
[01:11:48] I'll give you one interesting example we were talking about recently. We have almost three  
[01:11:55] and a half billion people using our services every day. One question we've struggled with  
[01:11:59] forever is how do we provide customer support? Today, you can write an email, but we've never  
[01:12:06] seriously been able to contemplate having voice support where someone can just call in.  
[01:12:14] I guess that's maybe one of the artifacts of having a free service. The revenue  
[01:12:18] per person isn't high enough to have an economic model where people can call in.  
[01:12:23] But also, with three and a half billion people using your service every day,  
[01:12:26] the number of calls would be massive. It’d be like the biggest call center in the world. It would be  
[01:12:33] like $10 or $20 billion a year to staff that. So we've never thought too seriously about it,  
[01:12:42] because it always seemed like there was no way that could make sense. But now,  
[01:12:48] as AI gets better, you're going to get to a place where AI can handle a bunch of people's issues.  
[01:12:55] Not all of them — maybe 10 years from now it can handle all of them — but thinking about a 3-5 year  
[01:13:03] time horizon, it will be able to handle a bunch. It's kind of like a self-driving car. They can  
[01:13:08] handle a bunch of terrain, but they're not doing the whole route by themselves yet in  
[01:13:14] most cases. People thought truck-driving jobs were going to go away, but there's actually more  
[01:13:19] truck-driving jobs now than when we first started talking about self-driving cars 20 years ago.  
[01:13:31] Going back to the customer support thing, it wouldn't make sense to staff out calling for  
[01:13:40] everyone. But let's say AI can handle 90% of that. Then if it can't, it kicks it off to a person.  
[01:13:49] If you get the cost of providing that service down to one-tenth of what it would've otherwise been,  
[01:13:55] then maybe now it actually makes sense to do it. That would be cool. So the net  
[01:14:01] result is that I actually think we're probably going to hire more customer support people.  
[01:14:06] The common belief is that AI will automate jobs away. But that hasn't really been how  
[01:14:16] the history of technology has worked. Usually, you create things that take away 90% of the work,  
[01:14:27] Final question: Who is the one person in the world today who you most seek out for advice?  
[01:14:32] Oh, man. I feel like part of my style is that I like having a breadth of  
[01:14:38] advisors. It's not just one person. We've got a great team. There are people  
[01:14:50] at the company, people on our board. There are a lot of people in the industry who are  
[01:14:57] doing new stuff. There's not a single person. But it's fun. Also, when the world is dynamic,  
[01:15:08] just having a reason to work with people you like on cool stuff… To me, that's what life is about.  
[01:15:16] Great note to close on. Thanks for doing this. Yeah, thank you.  
