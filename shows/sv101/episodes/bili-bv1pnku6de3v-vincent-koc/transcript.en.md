# 对话Vincent Koc：OpenClaw的反思与进化，与Agent的下一步 | B站 x WAIC AI会客厅【101视频播客】

[00:00:00] OpenCL 在今年年初爆火之后，在全球是掀起了龙虾热，宣告正式迈进 AI agent 时代。  
[00:00:07] OpenCL is the number one, is the most popular, the single most important release of software probably ever.  
[00:00:13] Lobster-themed installation events have popped up around the globe, especially in China.  
[00:00:17] 众多科技企业纷纷推出 CLA 产品，开启全民龙虾热潮。  
[00:00:22] 然而呢，很快人们发现没有想象中好用，以及安全考虑，又是出现了卸载风潮。  
[00:00:28] 同时，OpenCL 的发明者 Peter Steinberg 加入 OpenAI Hermes agent 等等其他竞品架构相继出现。  
[00:00:35] We had a lot of problems because the existing tools out there just weren't designed for us scale.  
[00:00:40] But now it's getting better.  
[00:00:41] A few weeks ago, we had like four point something million downloads a week.  
[00:00:44] They are saying only startups can make things happen faster during the AI era.  
[00:00:49] Peter's wishes were like he thinks the only way the OpenCL survives and is fair to everyone is that it remains as in a foundation.  
[00:00:57] 那么个人 agent 架构的下一步是什么？  
[00:00:59] OpenCL 成立基金会之后会如何运行？  
[00:01:02] 以及 agent 的阿哈 moment 什么时候会出现呢？  
[00:01:06] 在上海 W A I C 现场啊，我是采访到了 OpenCL Foundation 的首席架构师 Vincent Koch。  
[00:01:12] 那么以下就是我与 Vincent 的视频播客对话。  
[00:01:16] Hi Vincent, thanks so much for your time to joining us here at W A I C 2026 in Shanghai.  
[00:01:21] Let's start by introducing yourself a bit and explain your current role at the OpenCL Foundation.  
[00:01:27] Yes, so my name is Vincent Koch.  
[00:01:29] I'm Chief Architect at OpenCL Foundation, essentially looking after product and engineering.  
[00:01:34] And how did you first become involved with the OpenCL community?  
[00:01:38] So I've been an open source contributor for basically the start of my career.  
[00:01:43] I kind of noticed this project in early December, and this was on on X on Twitter.  
[00:01:51] A lot of I think poly market traders were using it, and I got really excited.  
[00:01:56] I was like, what is this?  
[00:01:56] Let me check out the project.  
[00:01:58] And then it was like, wow, this is this is crazy.  
[00:02:00] This is exciting.  
[00:02:01] I started testing it, and then I wanted to help, so I started contributing back to the project in like late December, early January, and then eventually that kind of snowballed,  
[00:02:10] became a maintainer, and then from maintainer to my current job now.  
[00:02:14] Do you still remember the day when OpenCL got really viral?  
[00:02:19] I don't know if there was like a particular point.  
[00:02:21] I think for me, in San Francisco, was in February where there was like a first ClawCon sort of event, and I think there was like a few hundred people guest list,  
[00:02:36] but the event started at seven.  
[00:02:38] But if you arrived at five o'clock, you were late, and the queue was like around the building.  
[00:02:42] Yeah, I remember that one.  
[00:02:43] My business partner was there.  
[00:02:45] Yeah, it was crazy.  
[00:02:46] Yeah, she told me the queue is like a few blocks away already.  
[00:02:49] Yeah, and it was, and we hadn't seen anything like that sort of viral.  
[00:02:54] Everyone is there, everyone's listening in San Francisco in quite some time.  
[00:02:58] It kind of had that magic to it, like you felt like something is going to happen.  
[00:03:00] So for me, like that was like the the peak sort of hype cycle, and I think after then it just started taking off quite a bit.  
[00:03:08] But did you guys expect that you know the OpenCL would got really really crazy in China?  
[00:03:14] No, I was uh obviously still a maintainer, but we're in the team on Discord, and I'm seeing like the aunties using it outside Tencent's offices in Shenzhen.  
[00:03:24] I'm seeing rap artists on Twitter talking about OpenCL.  
[00:03:28] It's just crazy, and I'm just like everywhere.  
[00:03:30] It's just going completely viral in China, but also outside of China as well.  
[00:03:33] China especially, and a lot of people like this is fake, and I was like, no, it's not fake.  
[00:03:37] It's definitely definitely real.  
[00:03:39] Tell us how it looks like to work with Peter Steinberger, the creator of OpenCL.  
[00:03:45] I think there's a only a few people I've had the chance to work with that have like a very special way of seeing the world and really seeing the possibilities of what you can do.  
[00:03:56] I think his attitude to life around, you know, make sure you put fun and energy into everything that you do.  
[00:04:01] Definitely comes across in the work, like you look at the fun little lobster and all of this.  
[00:04:05] So, I think for me has been not only just about you know creating what's new, what's on the bleeding edge, but also like that process of discovering something exciting has to be fun.  
[00:04:15] You have to think like a child.  
[00:04:17] You have to kind of like push yourself and your thinking a little bit.  
[00:04:19] So, I think for me, it's no no two days are different.  
[00:04:23] Every day is kind of very exciting as well.  
[00:04:25] And you said you joined the community in December last year.  
[00:04:29] Only half a year away, we saw OpenCLaw, you know, growing from like perhaps a small project into a global sensation, a global open source community.  
[00:04:39] What were some of the biggest challenges that you guys have been through?  
[00:04:43] I think the biggest challenges, like as with anything, is like anything of this scale becomes quite hard not to manage, but to grapple with.  
[00:04:52] You've built some software that's designed for developers or tinkerers, and now suddenly you have enterprise companies deploying this or trying to use it to build their businesses,  
[00:05:01] right?  
[00:05:02] So then you start getting people screaming like, "Is it safe?  
[00:05:04] Or how do we deploy this at scale?  
[00:05:07] Why is this using so many tokens and things like that?  
[00:05:10] " So you start realizing there's other challenges, and everyone's like expecting you to fix this when actually it's just an open source product, and we need to sort of like educate people,  
[00:05:19] like, "Hey, look, we're going to do our best.  
[00:05:21] We're going to try and help and solve this.  
[00:05:22] " But the frustrations that we got and the challenges that we faced ended up becoming the things that we started building for as well.  
[00:05:30] So, for example, we ended up with I don't know at one point we had like thirteen thousand PRs open, pull requests, like changes to OpenCLaw, and we developed our own review using AI agents to like manage this workload.  
[00:05:45] So then we started building the other agentic tools to help us with the scaling problems that we're having, and I think that was like the unlock for us, and that was like the more exciting part.  
[00:05:54] So we had a lot of problems because the existing tools out there just weren't designed for our scale.  
[00:06:00] Yeah, but now it's getting better.  
[00:06:02] Yeah, like we've had to essentially build entire infrastructure.  
[00:06:05] So if you if you look on the OpenCLaw website, there's a little link called ecosystem.  
[00:06:10] We have over, I think, close to a hundred repos.  
[00:06:14] So a lot of people know OpenCLaw the agent, but also we have different libraries, we have different automation tools, testing infrastructure, and we've had to build all of these.  
[00:06:25] And there's a joke that each one of these tools are basically like a startup in themselves that we manage and enables us to build OpenCLaw to scale.  
[00:06:34] If you have to describe OpenCLaw in a few sentences today, what would it be?  
[00:06:38] For us, OpenCLaw and especially the OpenCLaw Foundation is not.  
[00:06:43] I think it's more than just this AI agent or personal AI agent.  
[00:06:47] For us, it's like how do we empower the whole AI ecosystem, agentic use, be open and accessible to everyone.  
[00:06:54] That could be for enterprises, that could be for small businesses, it could be for mums and dads, it could be people that want to run local models at home as well.  
[00:07:01] So for us, the mission is to really empower humanity with AI.  
[00:07:05] Did that mission change at all during the past six months?  
[00:07:09] I think that that was pretty clear.  
[00:07:11] You know, when it started growing legs of its own, the foundation was already being set up in the background.  
[00:07:17] Obviously, it's been announced recently, so the mission statement was, I think, as a collective, was somewhat already there.  
[00:07:24] And the idea has always been like we want to keep Peter's wishes were to like you know he wants to keep it an open and independent product and put it into a foundation.  
[00:07:32] And for the same reasons, it's like we want to make sure it's accessible to everyone.  
[00:07:36] It's continues to remain open source, continues to remain in the hands of the community, which was very important.  
[00:07:44] And before we dive into the technical questions, let's talk about the China situation in the first quarter.  
[00:07:50] As you described, the OpenCLaw got extremely popular in China.  
[00:07:53] I would say even more popular than Silicon Valley, and there were long queues of people lining up to install OpenCLaw.  
[00:08:01] Apple Mac.  
[00:08:02] Was totally sold out back then.  
[00:08:04] So why in China, though?  
[00:08:06] I think there's a mindset thing that I've noticed, especially in China.  
[00:08:09] It's like, hey, we see that there's this new thing.  
[00:08:12] It's going to empower us.  
[00:08:13] It's going to help us.  
[00:08:15] Let's embrace it.  
[00:08:16] I think the the the Western sort of tech ecosystem was like, wow, this is scary.  
[00:08:23] It can do so many things.  
[00:08:25] Let's block this and let's understand what's happening.  
[00:08:28] And we saw this sort of behavior like back in 2023, 24 with like ChatGPT as well, where enterprises were like, we have to block this AI because like it's too scary,  
[00:08:36] it's too dangerous.  
[00:08:38] And then eventually they opened up and adopted it.  
[00:08:40] But I think for China has been very much like I want to adopt it at speed.  
[00:08:44] I think and some of the stories I was hearing was like employees were given like KPIs like you need to automate this many things with OpenClaw.  
[00:08:51] Whereas if you install OpenClaw in some enterprises in in other markets, like you get in trouble because it's like security risk, right?  
[00:08:58] So I think the mindset is very different around like I want to experiment, learn and and build fast.  
[00:09:04] But I think it's just a just a difference in the technology culture and sort of the speed in which China has been moving, especially with open source.  
[00:09:12] Is it possible because you know like a Codex or a Claude code is not that popular in China?  
[00:09:19] That's actually a a good point.  
[00:09:22] Yeah, it's not something I really actually thought about because the market penetration of these other products, uh, you know, they they can't be really used easily or use the tool within within the China ecosystem.  
[00:09:32] So I think having something that's open source and available that people can adopt could have been obviously one of the key catalysts as well for this.  
[00:09:40] For people who are not familiar with OpenClaw, can you tell them the difference between OpenClaw and the coding agent?  
[00:09:47] So a lot of these coding agents are starting to become like OpenClaw as well.  
[00:09:50] So it's kind of interesting.  
[00:09:52] But if we rewind back to the start of the year, the coding agents were very much like, hey, I have like a terminal or an app.  
[00:09:59] I want to build, I don't, I want to build a website or something.  
[00:10:02] So you have a conversation and it goes off and builds it.  
[00:10:04] The difference between now like OpenClaw, OpenClaw could yes build your website, but the whole idea was that like it acts as your personal agent.  
[00:10:12] So it would learn, it will have a memory, it would start to build skills, it would go and do things for you.  
[00:10:19] But the beauty is that like those things could also be in secret code.  
[00:10:22] So oh, can you buy my groceries from this website?  
[00:10:26] There's API, it finds it, so then it creates the code to do it.  
[00:10:29] Or for example, let's just say tomorrow one of the labs releases a new model and there's no support.  
[00:10:35] So you ask OpenClaw, hey, can you add this feature?  
[00:10:37] And it can change its own code and adapt itself and and add that feature for you.  
[00:10:41] So I think the difference between the coding agents is like it's creating code and it's it's blocked like the harness or the tool.  
[00:10:48] Whereas the OpenClaw agent can change its own code.  
[00:10:51] The agent can modify itself, which I think is the difference here.  
[00:10:54] Smarter.  
[00:10:55] Yeah.  
[00:10:55] Well, so many people had to uninstall OpenClaw after a while.  
[00:10:59] Setting number one, it's not so easy to use.  
[00:11:02] Number two, security concerns.  
[00:11:04] How do you see the cool down of the interest?  
[00:11:06] So one of the two things with that that's actually interesting is that there was definitely a cool down of the hype cycle, like the the craziness sort of died out a little bit,  
[00:11:15] which was kind of good.  
[00:11:16] But the second thing is like we did mess it up a little bit where we were trying to build this thing really fast using agents, you know, really trying to push the frontier here,  
[00:11:25] and we learned some good lessons on like how not to build software with agents.  
[00:11:29] So we did make some mistakes and we did lose a lot of users because it wasn't stable.  
[00:11:33] But ironically, we overcame those challenges a couple months ago, and if you look at our download numbers now, they're actually better than they ever were.  
[00:11:41] So before the at the craziness of the hype, I think we were hitting like two and a half, three million downloads a week on npm.  
[00:11:47] So obviously there's Chinese mirror websites, there's all these other sources.  
[00:11:51] So download numbers are probably way larger, but just based on npm.  
[00:11:54] And a few weeks ago, we had like four point something million downloads a week.  
[00:11:58] So so yes, it it did sort of die out a little bit the hype, but actually.  
[00:12:03] The adoption is actually scaling even more now, so it's kind of interesting to see.  
[00:12:08] So from that perspective, I'm like really excited to see that like you know, users are like responding to the like the stability and the features that we're releasing into the market.  
[00:12:18] Can you give us a few examples?  
[00:12:19] What are some of the really good use examples that you see across different industries?  
[00:12:25] So one of the things here is that like I think we talk about industry specific use cases.  
[00:12:30] I like to think of it as like it's just like having another employee or intern or personal assistant.  
[00:12:35] So yes, it can be vertical specific use cases, but realistically, it's like a case of if a model is good at doing some code or has understand some task really well,  
[00:12:46] and it has the tools or it can create the tools, I think it can do a lot of things now.  
[00:12:50] So it can now browse websites, it can have a phone number, it can connect a messaging app.  
[00:12:55] So really, the the possibilities are kind of endless, but depends on the task, right?  
[00:13:00] So maybe some design tasks are really hard, or video editing might be hard, but as people develop agentic tools for those, your agent can then use it.  
[00:13:08] For example, our agent creates soundtracks for our team every every few days, and it makes it kind of fun for us, right?  
[00:13:15] Whereas AI for music was kind of not so good before, but now it's good, so then we can give that tool to our agent.  
[00:13:20] So for us, it's like less about use case, and I think it's more about you kind of discovering what's possible.  
[00:13:26] One thing I do see that's interesting inside of enterprises and large sort of small to medium sized enterprises is also like employees having Open Claw in their kind of day to day job or projects having them,  
[00:13:38] and I think that's changing the way employees work with agents because previously, if I was an employee like an engineer, I would use my own AI coding assistants,  
[00:13:48] and I would work and then share that with the team.  
[00:13:50] Whereas now the it's not a coding assistant anymore; it's an agent, but it lives with the team, right?  
[00:13:54] So it can talk to my colleagues, and my colleagues can talk to my agent, and it has like a different kind of agents to the colleagues.  
[00:14:00] Yeah, so I think that's creating like a different dynamic for us in terms of workplaces and and how we operate.  
[00:14:06] And I think some organizations here in China and globally are starting to experiment with this, and some are kind of pushing the boundaries around that.  
[00:14:13] Obviously, we internally use agents and part of our workflow and talk to agents on a regular basis, but it's um I think that's where it starts to get really interesting because it's less about use case,  
[00:14:24] but it's changing the way we work actually.  
[00:14:26] Back to the first quarter, many Chinese companies released agent products on the top of the Open Claw framework, including Tencent Q Claw, Volcano Engine, Art Claw,  
[00:14:37] Alibaba, Wukong, Baidu, Duo Claw, etc.  
[00:14:40] So many.  
[00:14:41] Do you think that's the right approach for the to see consumers?  
[00:14:44] I mean, like these big companies, they actually launched their own Claw products.  
[00:14:49] Yeah, so a couple of things here for for especially for us, like we we were just pushing this open source product.  
[00:14:55] China was running at fast speed.  
[00:14:58] They wanted to get it to the market.  
[00:14:59] They wanted to get it in the hands of users and their customers really quickly.  
[00:15:02] So they developed on top of it.  
[00:15:04] Right, we didn't have the capability to do it at the time.  
[00:15:06] Now, fast forward a little bit.  
[00:15:09] Do we want to go straight to consumers with Open Claw?  
[00:15:11] Like we kind of do that at the moment, but realistically, like at the end of the day, we we just want to empower the ecosystem, right?  
[00:15:19] And if that means that other companies are building on top of Open Claw and getting that in the hands of users and empowering their users, I think that's a great outcome for us.  
[00:15:27] But also at the same time, the the other key thing here is that like if we wanted to build infrastructure and servers and host it for people, it kind of feels like it's taking us away from like what we're trying to achieve,  
[00:15:40] which is actually building this software that works really well and helping the ecosystem sort of get that in the hands of everyone else.  
[00:15:46] That might change in the future, but that's kind of like where where we see things at the moment.  
[00:15:51] So you would have seen also recent in the US, we've had Microsoft Scout, which is Microsoft's version of Open Claw that's sort of out there, and other companies are going to continue to do this.  
[00:16:01] And for us, it's like how do we support the ecosystem?  
[00:16:03] Where they want to build on top of it, that could be a large technology company, but it could also be a small enterprise that wants to do something internally as well.  
[00:16:10] A lot of the products I mentioned, unfortunately, did not work out pretty well.  
[00:16:16] What's the reason, in your opinion?  
[00:16:18] I haven't had a chance to actually experiment with them, so a bit hard for me to sort of answer that question.  
[00:16:25] But I would say that possibly, you know, I don't know if it was features or if it was cost or what those things were, but with anything, it's probably worth sort of digging into.  
[00:16:34] But yeah, I haven't had a chance to really dig into those products in detail.  
[00:16:38] Now, China tech companies later developed their own agent products.  
[00:16:41] For example, Tencent Work Buddy, now very popular, but it's not directly built on OpenCL.  
[00:16:48] However, it is fully compatible with OpenCL skills and frameworks.  
[00:16:52] How does OpenCL actually mean to these latest rounds of agent products?  
[00:16:58] So for us, like I kind of see this is like this post claw era.  
[00:17:01] I believe that like OpenCL really ushered like this next generation of agentic frameworks into the ecosystem.  
[00:17:07] It kind of created this explosion of model labs and token usage.  
[00:17:12] So you know, at the end of the day, in terms of what we're trying to achieve, I think it's good to have other solutions out there in the market, and that kind of enables like a really good ecosystem.  
[00:17:23] So I think it's a positive thing for the consumer and the users and the ecosystem as a whole.  
[00:17:29] And how do you continue to work with the big corp partnerships?  
[00:17:33] That one's a bit more interesting, but I think currently our model is very much the case of like on a case by case basis.  
[00:17:42] But realistically, we try to create one solution that fits most people, and that's where you know we have to bring a lot of differences of opinion.  
[00:17:50] We have to bring a lot of different technological ideas into the same place and get everyone to sort of agree on like what's the right way to do something.  
[00:17:57] And I think as we solve these problems, could be security or whatever it may be, we kind of bringing the ecosystem together to like come up with like okay, this is how we should solve this problem and this is how it should be designed.  
[00:18:07] And by doing so, we kind of help propelling the industry forward as well.  
[00:18:11] I know you've been traveling a lot these days, Japan, Singapore, and of course, come to China a lot.  
[00:18:18] So when you do the partnership with the big corps in different countries, are the partnerships different?  
[00:18:25] Are the requests demand different in your observation?  
[00:18:28] I would say less so partnerships, but the companies that I've spoken to, and this goes beyond just like talking partnerships specifically, but just I like to spend a lot of time with developers,  
[00:18:39] with enterprises, with the ecosystem as a whole.  
[00:18:41] I would say sometimes the challenges may seem different, but I noticed that as a whole, they're all pretty much the same, right?  
[00:18:48] And for example, you know, if you're in a country that has a large financial sector, you might be worried about what happens if your financial sector starts adopting something like OpenCL.  
[00:18:59] Is that going to be a risk?  
[00:19:00] Is there some security concern?  
[00:19:01] So a lot of the challenges, a lot of organizations and governments and policymakers and other people are talking about, are going to be relatively the same thing.  
[00:19:10] But depending on where they are with their digital maturity, it's probably going to change the the lens of of the sort of the complexities of the questions.  
[00:19:18] But majority of it sort of revolves around, you know, how do we get value out of this?  
[00:19:24] How do we manage costs?  
[00:19:27] How do we make sure this is safe?  
[00:19:29] How do we scale this properly?  
[00:19:30] Like I think this is not an OpenCL specific thing, but just AI in general.  
[00:19:36] When you speak to anyone, right?  
[00:19:37] So I think any enterprise right now, or any sort of large organization, or any anyone who's technical is sort of thinking through these things when it comes to AI strategy.  
[00:19:48] What did the China market bring to the OpenCL community?  
[00:19:51] Is there a lot of contributors, a lot of users, big corp partnerships, or continuous feedback?  
[00:19:57] I think it's a combination of all of those.  
[00:19:59] The benefit with the Chinese market is obviously it's been faster adopting OpenCL faster than anywhere else.  
[00:20:04] So for us, it's like.  
[00:20:06] It's kind of a window into what's going to happen next, in a way as well.  
[00:20:10] But also, there's large enterprises here that are using it, right?  
[00:20:14] I know of many enterprises here that have like every employee is using OpenCLaw.  
[00:20:18] The projects are running on OpenCLaw, and it's just interesting to see the dynamics and to work with those companies and just understand like what are some of their challenges,  
[00:20:27] what are their learnings, how can we share some of those.  
[00:20:28] So, I think that's definitely the case.  
[00:20:30] And and we have some maintainers on the team that actually are situated here in China as well.  
[00:20:35] So we have that kind of mix, global mix when it comes to our team and our roadmap and the features that we work on, and also the developers that we that we listen to as well.  
[00:20:46] And next, I want to spend a few minutes to walk through some of the architecture and the really important technology questions.  
[00:20:55] It was OpenCLaw's architecture that made it stand out.  
[00:20:58] The gateway agent, runtime sessions, memory scale, plug-in models, messaging channels, and connected devices work together in order to have the agent complete a task.  
[00:21:10] So if you look back half a year since the beginning of the sensation, what really made OpenCLaw work?  
[00:21:17] What is still the challenge, and what needs to be improving to make OpenCLaw work better?  
[00:21:25] I think what what was missing, and you can ask anyone this, is like there was this promise of AI agents that would do things for you, that you could talk to, and it would understand you,  
[00:21:34] and it could do things to an extent, and that promise just never came to life, right?  
[00:21:39] You know, yeah, we had coding agents, but like a coding agent is not the same as like my personal AI.  
[00:21:43] Everyone wants personal AI, and Peter was just like frustrated that it didn't happen, so he started building for himself, and eventually a community formed around it,  
[00:21:51] and then it became OpenCLaw, you know, now.  
[00:21:54] So I think that the fundamental needs of the users with like what people wanted were just like missing.  
[00:22:00] So I think that's the critical difference I think that kind of came about, and I think maybe it was a combination of timing, the community, maybe a different number of factors that sort of helped bring that to life.  
[00:22:11] And when we think about some of the challenges now, I think for us specifically, it's we know that the models are getting better, open source frontier models are getting better.  
[00:22:20] So knowing that the models are going to get better, what are some of the other challenges that we need to face?  
[00:22:24] I think a lot of it comes down to things like scaling within an enterprise.  
[00:22:29] There's going to be some specific technological requirements.  
[00:22:31] So for example, recently we've rearchitected the way we store information in OpenCLaw.  
[00:22:38] Before we used to write everything into files, so all your session conversations, that's now put into a database that's in a little file.  
[00:22:47] What that means is that if you're an enterprise building this at scale, you can replace that file with a database system.  
[00:22:52] You can take backups.  
[00:22:53] It makes this a lot more scalable, right, and easier to deploy.  
[00:22:56] So yes, it improves the the performance for consumer use for like personal use, but also at the same time it means that for enterprises like or technology companies like you mentioned that are like building on top of these makes it really easy to build on top of OpenCLaw.  
[00:23:11] So a lot of what we're building now is like focused on functionality around like how do we build this thing in a way that enables more people to build on top of OpenCLaw for whatever their use cases might be or their business challenges might be.  
[00:23:22] Let's talk some of the tech details.  
[00:23:25] So first of all, gateway.  
[00:23:27] Gateway is the central part of OpenCLaw's design.  
[00:23:30] Appears to be the central nerve system of OpenCLaw, connecting messaging channels, models, memory, and tools.  
[00:23:37] Why did OpenCLaw choose this always on gateway architecture, and what can it do that a conventional agent framework cannot?  
[00:23:46] So the difference with why did this happen?  
[00:23:49] You'd have to ask Peter this question.  
[00:23:51] I think it was his design, or maybe his agent came up with this design, or back and forth they came up with this design.  
[00:23:56] I'm sure there's a story.  
[00:23:57] I just can't remember off the top of my head, but I would say the difference at the time was that existing coding agents were basically turn based, right?  
[00:24:05] You had a thread.  
[00:24:07] And they were turn-based.  
[00:24:08] The difference with this sort of gateway concept is that, like, it was always on.  
[00:24:12] So it's like working like a service essentially on your machine, and it would connect to the messaging channels, and then that's where the concept of the heartbeat came in.  
[00:24:19] So it's like every 30 minutes or every 10 minutes, it's going to trigger a conversation chain.  
[00:24:24] It's going to check if it needs to do anything.  
[00:24:26] If it needs to do anything, it'll go off and do that thing.  
[00:24:28] So it kind of created this like human-like sort of like I'm going to go and do things in the background for you, and have a way to like schedule tasks and with the agent and do things.  
[00:24:39] I think that's what started giving this OpenCLaw a little bit of its magic as well.  
[00:24:45] And also, the gateway may hold credentials and execute actions across the user system, right?  
[00:24:51] It is also OpenCLaw's biggest security boundary.  
[00:24:55] So what has OpenCLaw community done to enforce the production layer?  
[00:25:00] Yeah, so a few things there.  
[00:25:01] When it comes to credential storage, like we've we've implemented some some security features where the credentials are not stored plain text, like they're in a sort of vault sort of concept.  
[00:25:11] But essentially, one of the key things that we are working towards is like containerization, right?  
[00:25:16] So you can run OpenCLaw in a container now.  
[00:25:19] So you can say that OpenCLaw, the that agent, this is it can only have access to these files, this internet connection, things like that.  
[00:25:26] But we're we're taking that a step further, and we're sort of like working with industry partners to like bring that as like a more native feature, without sort of saying too much,  
[00:25:35] but where if you say it can only access these files, there's a way that the operating system and OpenCLaw can kind of know 100 percent it's only accessing these files,  
[00:25:46] and if it needs to, it goes back to the user and it asks for permission, right?  
[00:25:50] We're creating these sort of security boundaries outside of OpenCLaw as well, and working with industry to make that a reality.  
[00:25:57] So that's definitely definitely in place, and parts of this already exist now, but parts of this will roll out as other technologies around security also happen.  
[00:26:05] Because you also got to remember, right?  
[00:26:06] Like OpenCLaw is like one piece of the puzzle.  
[00:26:08] You have the models, you have the operating system, you have the, you know, we have to work across industry to sort of like solve this problem.  
[00:26:14] It's not like exclusively us.  
[00:26:16] But then you would have the same security concerns with any other coding agent.  
[00:26:21] If you gave a coding agent like full admin access to your machine, it can also delete files and go to the internet and do all these things.  
[00:26:28] So I think a lot of times, a lot of people direct towards us.  
[00:26:32] We're more than happy to sort of help solve the problem as well.  
[00:26:35] But I would say it's like still a agent-specific sort of challenge.  
[00:26:39] But we are solving this more from like a containerization perspective.  
[00:26:42] So working out ways that you can kind of put it in a box safely and say, hey, you can only do these things, and when a user accepts it or doesn't accept it, like it's very clear and we we know that that's actually happened.  
[00:26:54] Yeah, I think you briefly mentioned this before, but what actions should an agent be permitted to take autonomously, and what kind of actions actually require them to ask for approval?  
[00:27:08] I think that's really hard to answer because like it's going to come down to what your intentions are, what use case you're working with.  
[00:27:15] You know, you might decide, hey, deleting files on my machine is dangerous.  
[00:27:19] Okay.  
[00:27:19] But you might be working on another project where it's just a test machine, whatever, and you're like, delete them, I don't care.  
[00:27:24] But like they're not the same thing, but they are like your intentions of like what you're trying to achieve is like going to be quite important.  
[00:27:30] So if you look at other coding agents, they've rolled out things like automatic sort of approval using large language model to understand the conversation thread and do this.  
[00:27:39] So we've implemented a similar feature called auto mode.  
[00:27:42] So instead of having on or off, we have like this in between where an agent will look at your conversation and then decide based on your intent is this safe or unsafe,  
[00:27:52] and then ask for approval.  
[00:27:54] So we've sort of implemented that at a at a at the OpenCLaw level, which means that if you're using an open source model or some other model, you still get this feature.  
[00:28:02] Now the other benefit with this as well, I might be using an open source model that might not have maybe some of the security guardrails.  
[00:28:09] The auto mode thing could come from like a frontier lab model, so I could pay for that access and just have like that safekeeping what my agent is doing.  
[00:28:20] But then I could run all my inference on, say, like a local model, so then I kind of get a hybrid of these two worlds as well.  
[00:28:26] Yeah.  
[00:28:27] So it looks like a lot can be done actually through like different layers.  
[00:28:32] And you talk about models, and we're now experiencing another round of SOTA model racing in Silicon Valley, very intense, and in China, and also in China.  
[00:28:42] That's right.  
[00:28:42] How much does model update actually impact the agent framework?  
[00:28:47] Or like, if I have to reframe the question, when an OpenCLaw agent performs well, how much of that performance comes from the underlying foundation model, and how much does that capability comes from OpenCLaw agent harness,  
[00:29:00] memory tools, or execution environment?  
[00:29:03] I think it's a combination of both.  
[00:29:04] Yeah.  
[00:29:05] I would also say that some models have also been trained, post-trained on OpenCLaw.  
[00:29:11] I know of some open source models, especially some of the ones in China, have definitely been post-trained on OpenCLaw, which means that those models then perform better because they understand,  
[00:29:19] like the model just knows that it's inside of OpenCLaw and the memory and the tools and things like that.  
[00:29:23] So there's definitely like a combination of the two.  
[00:29:25] But we also know that some models don't work that well, so which tells us that like the model needs to be at a certain level of intelligence or size.  
[00:29:34] We're currently working through a process of running a benchmark and evaluation that we're going to make public about 120 tasks, 100 tasks.  
[00:29:43] We're working with some research teams and some labs, and we're going to release that over the next few weeks.  
[00:29:47] Hopefully, it's been taking some time, and that's going to help us understand where the gaps are, and we're going to kind of release that to the market.  
[00:29:54] But then we're going to work on okay, where we know that the certain models or certain tasks are failing.  
[00:29:59] What can we do to improve that?  
[00:30:01] Like, can we improve the context, or can we change something with the memory when it's a smaller model to like make sure that that performance works really well?  
[00:30:09] So I think there's a combination of the model, but also how the model works in the harness.  
[00:30:12] And we're seeing this with the frontier model labs; they're all releasing harnesses as well to complement their model.  
[00:30:19] And I think it's the combination of the two, right?  
[00:30:22] Because those harnesses come with tools and memory and other things, and those models have been trained to explicitly use those tools.  
[00:30:29] And I think that's what making them powerful.  
[00:30:30] And OpenCLaw supports models from different providers.  
[00:30:34] Correct.  
[00:30:34] How can you guarantee the model independence?  
[00:30:38] In what way?  
[00:30:39] So that you treat actually models fairly, not to favor certain models.  
[00:30:45] Yeah.  
[00:30:45] So we support any model release that comes out.  
[00:30:47] We try our best to like get zero day support.  
[00:30:50] We work with all the different model providers and labs like that.  
[00:30:53] And yeah, we we don't specifically push one company or another company.  
[00:30:58] We make sure that feature parity exists as well, and we do testing as well.  
[00:31:03] So I think it just comes down to the capability.  
[00:31:06] We're also kind of built some features in there which allows model companies when they release new models, they don't need to run an update on our side.  
[00:31:13] They can push some changes on their end.  
[00:31:17] So that makes it sort of fair and a little bit more easier for everyone else.  
[00:31:21] But I think the benchmarking process and the tuning is going to help us, like especially with some of the smaller models, make sure that there's like a better experience for users as well in OpenCLaw.  
[00:31:32] Are smaller models important for the agent work?  
[00:31:35] I'd say more for the local, like the local model, open source sort of community specific tasks.  
[00:31:43] People are obviously concerned around token usage.  
[00:31:46] So for us, it's like how do we make sure that you get some experience?  
[00:31:51] Yeah.  
[00:31:51] It might not be the best, but like you might be able to carry out some autonomous tasks with OpenCLaw.  
[00:31:56] So for us, it's like a really good learning experience to sort of figure out how do we then architect.  
[00:32:02] Parts of OpenCLaw to then be fair for all of these models, right?  
[00:32:05] Small, large, medium.  
[00:32:06] So that's kind of part of the process as well.  
[00:32:09] Memory, persistent memory is one of the features that can make a personal agent genuinely useful and personalized.  
[00:32:16] But it can also introduce errors, privacy concerns, and unwanted assumptions.  
[00:32:22] How to balance these two sides?  
[00:32:26] I would say the interesting thing with memory is like a lot of people might say this like a solved problem.  
[00:32:30] In my mind, this is like one hundred percent not a solved problem.  
[00:32:33] I think memory is like one of these things where it's like really complex space.  
[00:32:37] Like you've even answered it right.  
[00:32:38] Like for example, let's just say I'm using one model, and the memory files get created, and then I switch to another model.  
[00:32:44] How do we know that that model understands?  
[00:32:46] There's all these like complicated factors, right?  
[00:32:49] Other issues arise when you use like multi-tenancy.  
[00:32:51] Like what happens if you're sharing one claw in a team?  
[00:32:55] Which memories can be shared with which people?  
[00:32:56] And that's why we we for now basically say with multi-tenancy is like that claw.  
[00:33:01] Assume everything is interchangeable.  
[00:33:03] Like there's ways we're working on like solving this sort of multi-tenancy thing at the moment.  
[00:33:09] But you know that that's why it's like not a solved problem, and we're actively working on this and looking at different ways of solving it.  
[00:33:17] That's probably like one of the more interesting, harder problem spaces right now for sure.  
[00:33:22] Yeah, yeah.  
[00:33:22] Because I think that's what gives it the the capability to do what it needs to do.  
[00:33:26] Right.  
[00:33:27] Yeah.  
[00:33:28] And also long horizon tasks are pretty challenging but necessary.  
[00:33:32] Correct.  
[00:33:33] For the next chapter, or what's your approach for long horizon tasks?  
[00:33:37] I believe a lot of the newer SOTA models are like getting better at long horizon tasks in general.  
[00:33:43] We're also seeing that industry is building just for context.  
[00:33:47] Like prior prior to my work on OpenCLaw, I was working on self optimizing agents.  
[00:33:51] So essentially, how do we get agents to like recursively improve themselves for like a particular long horizon task?  
[00:33:57] Yeah.  
[00:33:58] So I think frameworks and approaches are going to come out from industry around that, and and I personally believe they're just going to become capabilities that we can just give to agents as like tools or some sort of features that we can build into it and let it manage it.  
[00:34:13] So I think best way to describe it is that OpenCLaw could act as like an orchestrator and keep on top of your work and you know do all of that and use different models to like orchestrate that work.  
[00:34:25] But like I I don't see us solving long horizon as a problem, right?  
[00:34:28] Whereas like different model companies and systems might, and then we find a way to kind of like bring that into the OpenCLaw system.  
[00:34:34] And for the multi-agent design within OpenCLaw, when is it useful to route work to isolated agents or specialist agents, and when does that adding more agents simply create additional cost,  
[00:34:49] latency, as well as coordination problems?  
[00:34:52] I think it's less about costs and latency, but more of a case of like context.  
[00:34:55] Like most nine times out of ten, for most people, one single agent is like more than sufficient to like handle a lot of complicated stuff.  
[00:35:03] Where it happens is like oh, there's this other very particular task I want to run every couple of days, do a certain thing.  
[00:35:10] It has its own system prompt.  
[00:35:11] Once you start like carving that out, then you're like, okay, I can just make that a separate agent.  
[00:35:17] The best way to think about is like I have one person and one employee working for me.  
[00:35:21] Now their workload is a lot, and I know certain workloads is like very repeatable.  
[00:35:25] Okay, how do I take that work off them and then give that to someone else?  
[00:35:28] So kind of think more like I'm managing someone.  
[00:35:31] How do I break this workload up between people?  
[00:35:33] Is like a better sort of mindset to sort of apply to this when you're thinking about this.  
[00:35:39] And we are seeing some agent systems are moving towards a more complex structure involving managers, planners, subagents, and nested team of agents.  
[00:35:51] However, OpenCLaw actually continues to keep its like simple worm.  
[00:35:58] So-called pragmatic approach.  
[00:36:00] Why is that?  
[00:36:01] So, in engineering, we have this concept called Conway's law, which basically means that, like most organizations, their software code will map their internal organization structure.  
[00:36:11] What do I mean by this?  
[00:36:13] Let's say my marketing team had a growth team and like a retention team.  
[00:36:18] When I build the code, I might have a separate like promotion system and a separate like retention data system, right?  
[00:36:26] Just because that's how my teams work, so I want one team to manage this code, manage another.  
[00:36:30] I think complex organizations are like mirroring their internal organization design into their agents because they have a certain organizational structure.  
[00:36:39] They create agents in that way.  
[00:36:41] It doesn't mean that that's the optimum way to solve things, right?  
[00:36:44] So, I think we're inherently taking on the past challenges and not thinking from like a clean piece of paper, like what would be the ideal way, and just building from the ground up.  
[00:36:53] And I think this is why some startups and some newer organizations are like able to like build agent first and like work at rapid speed versus some other organizations that have to go through a full change management process and like really understand what does this mean.  
[00:37:09] I got a close friend of mine.  
[00:37:10] She works in like transformation, AI transformation, like like a global scale.  
[00:37:14] And we were having a conversation, and she was saying to me, "This is just sharing some personal notes, by the way.  
[00:37:19] " It was like, you know, CTOs have all these resources.  
[00:37:22] They've all this like agent designs and frameworks, but if I'm a chief operating officer, like what does the future of the workplace look like?  
[00:37:28] Like, what does the team structure and agents like?  
[00:37:30] What does that all look like?  
[00:37:31] And I think those are like the conversations that people need to have because they're just kind of taking what they have and they're just putting into an agent,  
[00:37:37] expecting it to magically work.  
[00:37:39] Is like, I think where some of the challenges are.  
[00:37:42] So, people need to have the right expectation of the agent, or the way to get that expectation is through experimentation, right?  
[00:37:49] Like, start with a blank piece of paper.  
[00:37:51] I'm going to redesign this team or this problem.  
[00:37:54] Let's build some agents.  
[00:37:56] Let's get it to.  
[00:37:56] Let's build something in a day.  
[00:37:58] Let's get it working.  
[00:37:59] It's not going to work perfectly.  
[00:38:00] What do we learn?  
[00:38:00] And let's iterate on that.  
[00:38:02] Whereas, instead of taking like small, small pieces and like trying to solve this problem and make it perfect, and I think it's more a case of like, how do we increase the maturity of of like this agentic design?  
[00:38:14] And the way I keep saying to people is like, 2026 of way of like agentic engineering is very different to like how AI and agents were being developed prior to that.  
[00:38:25] And I think a lot of organizations and individual developers and product people just haven't quite crossed to the other side yet and realized that actually, you know,  
[00:38:34] the models, like the SOTA models we're speaking about, have really good understanding of this problem, and you can just talk to it and like work with it and and build the agent together,  
[00:38:43] right, with the agent and get it to a point, and then you can learn from that and you can apply the learnings.  
[00:38:48] Instead, it's like, oh, I'm going to build all these little skills and then see what happens.  
[00:38:52] It's just you know, it's like a.  
[00:38:53] I think you can just like leapfrog basically and learn from that experience.  
[00:38:57] Yeah, as you said, there's like a surge of skills and plugins and MCPs.  
[00:39:04] So we can see like OpenCL still maintains like a small and core framework within this open source community, while the ecosystem is expanding.  
[00:39:15] Do you see OpenCL actually will keep that small core, or it will slowly expand to do more like third party ecosystems by itself?  
[00:39:25] I think it's hard to say, but like we're definitely looking at ways that we can support the wider ecosystem in different ways, and some of our plugin architectures definitely been changing and shifting to like how do we move as the industry shifts.  
[00:39:38] It's not like we have like a new concept like MCP or skills.  
[00:39:41] Like I don't think we've had one of those in a while, but it's more how do we build on top of that, right?  
[00:39:47] Like an example the other day that we're talking about internally, like what happens if one skill is dependent on another skill?  
[00:39:53] Right now, the skill spec doesn't accept that.  
[00:39:55] Like, there's no such concept of this in the industry.  
[00:39:58] So we're like, do we adopt this and build this and then force the industry to do it?  
[00:40:01] I think that's where we would work with the ecosystem and like figure out like where some of the challenges are, and how do we sort of like think about what's next?  
[00:40:08] I think you mentioned that like Peter and other like core contributors were wondering, oh, why is like agents aha moment hasn't come yet?  
[00:40:21] So is it technical bottleneck?  
[00:40:25] There's cost.  
[00:40:26] There's you you know there's how reliable is the model?  
[00:40:29] Like there's there's all kinds of factors around this, right?  
[00:40:31] So and again going back to my point, it's like it's not just an OpenCL specific issue.  
[00:40:36] It's like also the models and other things that like encompass this ecosystem, right?  
[00:40:40] And like you might have all of the companies that you're using, like the banks, for example.  
[00:40:44] Do the banks allow your agents to come in and transact and move your money around and do this thing?  
[00:40:48] So I think there's a lot of challenges with like the services that your agent wants to access and how do they access it?  
[00:40:54] And so I think like the whole industry is like sort of growing up as well.  
[00:40:58] So I think we'll start to see that becoming more reality as services are like allow agents and is safe and the models work and you know I think it's going to take a little bit of time,  
[00:41:07] but we are definitely seeing a lot of improvements.  
[00:41:10] The biggest unlock for me I've seen is the use of computer use models, where you know like any one of the agents, some agents support it and some of the harnesses.  
[00:41:19] We're also looking at like some open source computer use stuff on our harness so that you can use other models as well.  
[00:41:25] And the idea is that like it can just take over a web browser, right?  
[00:41:28] Start clicking things and doing things.  
[00:41:30] So with your permission, which might be like a way to sort of unlock the some of the challenges people are facing as well.  
[00:41:36] After the first wave of the excitement in the first quarter, we talked about the cooldown, right?  
[00:41:44] Did the team, did the OpenCL community actually learn something from the cooldown?  
[00:41:49] I think for us it was like we just need to make sure that we build reliable software that works and works really well.  
[00:41:57] But trying to do this in a way where agents are the main engineers and you're engineering the agents to do this is very very hard.  
[00:42:05] And we had to spend a lot of time building the tools for this, right?  
[00:42:08] So like one of them was building extensive testing tools.  
[00:42:11] So right now any one of our agents, any one of the maintainers can their agents can spin up any operating system on any type of hardware on most clouds in like 20 seconds,  
[00:42:22] and they can go inside, take screenshots, do video recording, click through, and that's how the agents able to test and validate the changes and make sure that it's working and allow us as maintainers to go in and see for ourselves and see proof.  
[00:42:33] So if I say, hey, attach proof to the PR, we'll see screenshot before after video recording.  
[00:42:37] Or hey, I want to access the machine, it will say, okay, here, boom, I open the web browser, I've logged you in.  
[00:42:43] You can now take over this test machine.  
[00:42:45] So we had to build a lot of these things that didn't exist, and I think that's one of our learnings was actually like to make agentic engineering work at scale.  
[00:42:52] We call it a factory.  
[00:42:53] The factory needs all the other machines to work, right?  
[00:42:55] You can't just have one conveyor belt expecting it to work.  
[00:42:58] You need the quality assurance.  
[00:42:59] You need the lights.  
[00:43:00] You need all these other things to make a factory run, and the water, electricity, right?  
[00:43:04] So for us it was like we had to build all this other mechanics in that we're missing.  
[00:43:08] And we are now seeing the adoption of individual developers and doing like personal AI.  
[00:43:14] We're also seeing the enterprise side that they're adopting a lot of Open OpenCL framework as well.  
[00:43:21] So to see and to be this two approach, which one is now moving faster from your observation?  
[00:43:28] The kind of one is feeding the other, right?  
[00:43:30] So as consumers adopt it, some of those consumers work in enterprises and they're like, okay, how do I bring this into a business setting?  
[00:43:37] But then as enterprises adopt it, it's making the product better at scale for different use cases, which makes it better for consumers to adopt it because it's more reliable because enterprises can use it.  
[00:43:47] So it's kind of creating this like really interesting flywheel for us.  
[00:43:49] And it's very different because you know traditional software, like if you build for an enterprise or a consumer, it's usually very different.  
[00:43:55] And the reason why it's very different is maybe from a go to market perspective, right?  
[00:43:58] Sales.  
[00:43:59] Promotion, pricing, and the feature sets changes, because we're not technically selling the product, it really comes down to feature differentiation, and because Open Core is quite extendable,  
[00:44:10] allows enterprises to like really make it and shape it into what they need.  
[00:44:13] So I think we're kind of in this like really good sweet spot, which kind of fits most people's needs currently.  
[00:44:19] But the challenge is obviously working with industry and working with the ecosystem to like figure out what's you know how to how to balance everyone's needs properly.  
[00:44:27] You guys actually launched the mobile app for iOS and Android.  
[00:44:31] Why did you do that?  
[00:44:32] So we actually had the apps built for a long time.  
[00:44:35] I think it was still in the code base in like January, February.  
[00:44:38] We hadn't registered an entity.  
[00:44:40] Yeah.  
[00:44:40] So the foundation got stood up as an entity, and because it was stood up, we could finally go to Apple and Google and go, "Hey, can you give us a developer account and we'll publish it?  
[00:44:49] " Right?  
[00:44:49] We didn't want to publish it under some contributor's name.  
[00:44:52] We wanted to do it officially.  
[00:44:53] So we had them, and we wanted to release them.  
[00:44:58] I think some people want a first party experience, and some people really enjoy that first party experience, and some people might not.  
[00:45:06] So I think for us, it's just giving people optionality on how they want to use it, right?  
[00:45:09] So for us, it's not any extra work because we'd already done the work building these apps.  
[00:45:14] It's just more a case of getting the hands getting into the hands of people.  
[00:45:17] And I saw some less positive feedback from some of the consumers.  
[00:45:24] What is the biggest challenge there?  
[00:45:26] I think the thing with people is on especially on the internet is like very quick to criticize.  
[00:45:30] I think for us has been we develop at speed, and the beauty with all that criticism was like great.  
[00:45:36] We now have tons of feedback that we can incorporate.  
[00:45:38] So since then, we've made a number of releases, and even within the space of two weeks since we've released the apps, if you look at what where they are now versus where they were before,  
[00:45:48] they look totally different.  
[00:45:49] Like it's like almost a complete different product.  
[00:45:50] And the beauty with open source is that like other people can contribute.  
[00:45:54] So luckily, we had people making contributions, which was good.  
[00:45:57] But then a lot of designers were, for example, sending us nice designs that they created with AI, possibly going implement this, and you're like, okay, can you do a pull request?  
[00:46:06] Can you like help us get this in?  
[00:46:07] They're like, I don't know how to do that.  
[00:46:09] So a lot of people are quite quick to like make comments about software, but I think people forget that it's like, you know, the Open Core Foundation like main engineering team is like five or six people.  
[00:46:21] You know, yeah, we have other contributors and people working across the ecosystem as well, but like we're not some 200 person startup, you know, a large enterprise,  
[00:46:29] but they're kind of expecting us to like quick, quick, quick, can you do this?  
[00:46:32] But we took on all the feedback and we and we made some some quick changes.  
[00:46:36] And we'd rather get the product into hands of people, get feedback, than to try and make it perfect and spend months and it's not what people want.  
[00:46:43] I think this is what I was saying earlier about how enterprises need to think about agentic engineering.  
[00:46:47] Is to like we can move quickly.  
[00:46:49] So if you can move quickly, you're better to just get it out there, get get some feedback, and then iterate quickly.  
[00:46:54] If people made bad comments and then we did nothing about it, then I'd be like, okay, that's bad.  
[00:46:58] But we were able to sort of like really change and shift and and make a lot of changes.  
[00:47:03] The same time, the websites got redesigned, our documentation got redesigned, like a whole bunch of stuff got redesigned.  
[00:47:09] We're still hiring for product designers as well onto the team.  
[00:47:13] But yeah.  
[00:47:14] Yeah, to be honest, I was a little bit surprised that you guys launched an app because I thought that's what a startup would do.  
[00:47:20] Yeah, I mean the testing tools have been pretty good.  
[00:47:23] We have testing tools, and they'll go and like launch it on phones and take screenshots and videos, and maintainers would just kind of compare, like, yeah, this video looks good.  
[00:47:31] It's like approved.  
[00:47:32] So it does all the work, right?  
[00:47:34] We still need to drive it, but we can do a lot more than we could before.  
[00:47:38] The apps aren't super complex, right?  
[00:47:40] Like a lot of the features already exist in the web UI, so it's more a case of like the same feature set in Android in iOS.  
[00:47:47] The other thing we've also done is we're we're not using some framework.  
[00:47:50] We've written it in fully native Android code, fully native iOS code, so we're not having to battle  
[00:47:56] Complex code because the AI agents can write native code really easily, so I think there's some architectural decisions we made that make it really easy to maintain as well.  
[00:48:04] Do you guys see Manus or JetBrains as competitor?  
[00:48:09] I haven't really used their products lately, so hard to answer.  
[00:48:13] But I don't know.  
[00:48:15] For us, it's like I don't particularly see anyone as competitors in the industry.  
[00:48:18] At the end of the day, we're trying to propel the agent industry forward.  
[00:48:23] In this case, and I would say like our adoption and growth is like just quite large, and we're building more like a harness layer, right?  
[00:48:34] We're building this sort of personal AI agent layer, and now for enterprises as well.  
[00:48:38] And it's very different from some of these other products and services.  
[00:48:41] Some of these are closed source SaaS products, which is very different from having like an open source product that you can take internally into your organization and build a business on top of as well.  
[00:48:51] I have to mention another competitor of you yours, although you don't want to call anything competitor.  
[00:48:57] Always use Hermes agent.  
[00:48:58] A lot of developers express a preference for Hermes agent, describing it as leaner or more coherent for certain user cases.  
[00:49:08] Did OpenClaud team actually learn anything from the Hermes agent?  
[00:49:12] I think for us, like some of their memory, they're very different and divergent from some of our features and the way our features work.  
[00:49:18] So they kind of give you this like very out of the box sort of experience.  
[00:49:23] I would say some of the stuff they've done around memory is very different and kind of interesting.  
[00:49:27] Some of the onboarding is kind of very interesting as well.  
[00:49:29] But I would say we're we're quite fundamentally different in terms of products.  
[00:49:34] Although on the surface, yes, they're essentially personal agents.  
[00:49:38] You can connect them up to most messaging channels, but some of the internal mechanics around is like kind of very different as well.  
[00:49:44] And do you see like more open source agent frameworks coming out to the market?  
[00:49:51] And also, do you expect the the agent framework eventually to consolidate around a few dominant platforms, which is you know similar to the operating systems?  
[00:50:04] Yeah, I mean, you could argue, yeah, maybe we will see some consolidation.  
[00:50:08] But like if we looked at any of the AI tooling out there in the market right now, like none of that's happened.  
[00:50:12] We have like hundreds and thousands of like AI software companies, right?  
[00:50:15] So hard to say what the future is going to look like.  
[00:50:18] But yeah, we're going to see more and more agent frameworks.  
[00:50:21] I think it's just going to accelerate.  
[00:50:22] Everyone's going to create like maybe there's going to be vertical specific ones or industry specific ones or whatever the needs are.  
[00:50:29] There might be niche products, obviously, to tap into that specific market.  
[00:50:33] But at the like larger scale, there's only going to be room for like a small handful, maybe.  
[00:50:37] But we'll see.  
[00:50:38] Like it's really hard to say.  
[00:50:39] Like this industry literally changes by the hour.  
[00:50:42] Like I can open up my phone and look at my newsfeed.  
[00:50:44] I'm sure some new release of something crazy is happening right now, right?  
[00:50:48] Like, and but I think that's also exciting that there's a there's a lot of opportunity there for anyone who's building, but also for us as well to be able to sort of support the community as well,  
[00:50:58] which I think is really good thing.  
[00:51:00] Next, let's talk about the foundation.  
[00:51:02] Can you explain to us how the OpenClaud Foundation operates in practice?  
[00:51:07] Essentially, it's a 501c.  
[00:51:10] It's a nonprofit registered out of the US, and because of that, we obviously don't make revenue.  
[00:51:18] If we do make any sort of revenue, it's obviously going back into the community, back into the product, and back into the ecosystem.  
[00:51:25] And our focus and our mission is essentially what I've been sort of focusing on around like making sure personal AI and AI agents is like available and accessible to everyone and is empowering sort of everyone.  
[00:51:36] The operating model, it kind of we we we kind of work like a startup when it comes to our engineering.  
[00:51:43] Yeah.  
[00:51:43] But obviously, being a sort of nonprofit organization, we have to sort of work in a sort certain way as well.  
[00:51:49] So we have like governance and all these structures and stuff like that.  
[00:51:52] But predominantly, we we get you know donations from the community.  
[00:51:56] We get donations from the tech ecosystem.  
[00:51:58] That then drives a lot of the hiring and different product initiatives that we're doing at the moment.  
[00:52:04] So you would have seen we recently made an announcement of some of the partners that have and some of the people in the industry that have been really grateful and sort of supporting our mission.  
[00:52:13] And that's usually the sort of the driving force behind it.  
[00:52:16] And it's very different from, say, like a venture-backed business that has to scale up to certain number multiple and hit a certain revenue number and things like that.  
[00:52:26] Ours is mostly focused on what impact are we doing into the ecosystem and what impact are we doing to enterprises, personal users, you know, the the whole AI community as a whole.  
[00:52:36] Which means that our mission is very different.  
[00:52:38] We we essentially want to become Switzerland for AI agents.  
[00:52:44] Yeah, is the donation enough to run the community or the the foundation?  
[00:52:50] Where you actually need a lot of talents.  
[00:52:54] It's hard to say what's enough or not enough.  
[00:52:56] Like you could argue that there's unlimited work and it's never enough.  
[00:52:59] But I would say that we're very grateful for everyone's support.  
[00:53:02] Like we get support from people giving us small, even five dollar donations on GitHub down to you know supporting us with like, hey, we want to give you some tools to use for certain things.  
[00:53:13] So I think support comes in many different shapes and forms.  
[00:53:17] And I think we're very grateful for the community and different partners out there and everyone that's kind of been supporting our mission.  
[00:53:23] Do you have the guidance of what kind of money you cannot absolutely take?  
[00:53:28] I think internally we do have some.  
[00:53:30] You know, we don't just take you know anything from anyone, but that's something I'll have to check and come back to if it's public or not.  
[00:53:36] I'm not sure.  
[00:53:37] You are now the chief architect and minister of lobster affairs.  
[00:53:41] That's a bit of a joke.  
[00:53:42] Yeah, I like this move.  
[00:53:44] And you have five members of technical staff for product and engineering.  
[00:53:50] Dave is the chairperson, and also you have four other people responsible for community partnerships, talent, and finance.  
[00:53:57] You have core maintainers, and of course, a global community behind you guys.  
[00:54:01] But are these people enough to handle today's open cloud daily operation?  
[00:54:07] I think as as we scale, we will continue to scale and would continue to sort of grow the team and continue to grow like our support system around that.  
[00:54:15] You'll notice like we have a number of job openings currently, and we're going through a hiring process to continue to scale the team.  
[00:54:21] But we're also cognizant that like we don't want to just explode and hire lots of people because we feel like we need to.  
[00:54:26] I think there's like being mindful around what that looks like.  
[00:54:30] So for example, if we hire someone into a function, it's like okay, how does an agent first look like in this role, like design or events?  
[00:54:37] Like how do we build like an agent first version of this and sort of build that up with that with that individual and then see how far we can scale that.  
[00:54:44] And it's not about not hiring people, but it's about creating efficiency and then also giving this back to the community as well.  
[00:54:50] So like everything that we do internally and the way we operate, we open source.  
[00:54:54] I mean, we give back to the community as well.  
[00:54:55] So I think there's some some interesting things like yeah, we'd love to hire like everyone we possibly can straight away, but we also have to be mindful of like cost and like what does that look like and the impact that we need to drive from that as well.  
[00:55:07] So is it hard to hire people nowadays?  
[00:55:10] Because there's apparently a talent war in Silicon Valley.  
[00:55:14] I think for us is very different.  
[00:55:16] Yes, there's definitely a talent war, but I think our project is very unique in terms of its position and its mission as well.  
[00:55:25] And I think that attracts a certain type of people into this project, which aligns with our mission and what we're trying to do.  
[00:55:33] So I think creates like a very unique sort of opportunity.  
[00:55:36] I think people that work in open source do it for the love, you know.  
[00:55:41] I think there's like a passion and you want to give back to the community.  
[00:55:43] And I think that you know we want to attract those sort of talent as well and sort of foster that sort of talent as much as we can.  
[00:55:50] Cool.  
[00:55:51] And you don't always agree with each other, I guess, within the foundation.  
[00:55:56] So when there's a disagreement, who has the final say?  
[00:56:00] We've never actually had to like put the hammer down and and and and get to a point, but I think eventually it would work out.  
[00:56:06] Like, what you know, who said what, but we have enough people and enough differences of opinion that collectively we tend to we finalize and agree towards something.  
[00:56:16] And I think a project of this size and complexity, I think disagreement is a good thing.  
[00:56:21] It means we're thinking through the changes, we're thinking through our opinions and our differences.  
[00:56:25] If we all agreed with everyone, I think we would just end up receiving product that just doesn't work well.  
[00:56:31] The fact that we have such a diverse mix of maintainers on the project and organisations we work with means that we get like very challenging opinions, right?  
[00:56:41] You know, for example, someone wants to put a feature in, you know, maybe for enterprises that helps in the in like a say US technology space, but then like maybe some Chinese maintainers like,  
[00:56:51] hey, like this isn't going to work for us, okay?  
[00:56:53] So how do we then create a feature that works for everyone, or vice versa?  
[00:56:56] It's just an example, right?  
[00:56:58] So it's like making sure that it's fair and and works well for everyone is like part of the part of the challenge.  
[00:57:02] But I think disagreements are healthy.  
[00:57:04] We haven't had any sort of stalemate or any issues with that.  
[00:57:07] I think open source communities tend to be open source projects tend to be I don't know have its own way of solving these problems.  
[00:57:17] Sometimes they can get quite heated.  
[00:57:19] Like we haven't anything had anything too crazy, but they tend to have their own sort of rhythm and flow and way of dealing with these issues, and they have done for quite some time.  
[00:57:28] So a lot of the maintainers on the project have worked in large open source projects as well.  
[00:57:33] So for a lot of us, it's like we're kind of used to dealing with these sort of situations.  
[00:57:38] I have another question I have to ask about Peter.  
[00:57:42] Of course, I know people people at the Open Cloud Foundation, also the community were happy for him after he announced that he will join Open AI.  
[00:57:51] But Open Cloud's early development tied closely to Peter, and now the foundation per se.  
[00:57:58] How can you actually guarantee the mechanism that can work well and reduce the risk of relying too much on one person individually?  
[00:58:08] I'd say we don't have like a single person risk at the moment.  
[00:58:11] We have an entire team of engineers.  
[00:58:14] If you look at the commits, for example, it's like starting to smooth out a little bit more as well.  
[00:58:18] You know, Peter's vision definitely matters a lot to us and the team as well.  
[00:58:21] But as we continue to scale the team, I think it's how do we take that vision of Peter, myself, and other people, like how do we kind of bring that together into a cohesive like strategy roadmap and get everyone aligned to the end state that we're trying to go towards?  
[00:58:34] So I think that's the sort of thing that we're working towards that reduces any sort of risk around like it's is a one person team.  
[00:58:40] I think there was a big misconception, like even when we had a huge maintainer group, a lot of the community was still thinking, hey, it's just Peter, right?  
[00:58:47] I mean, fundamentally, to to an extent, a large percentage of the the commits are still coming from like a handful of people, myself included, but it's hard to quantify because like just looking at commits is not enough because some of the changes can be quite fundamental,  
[00:59:01] let's say security related, but it's only like a small volume but could have large impact.  
[00:59:05] So we have a mixture of people contributing in different ways, and it's hard to quantify what that looks like.  
[00:59:12] But I would say that like it's it's now quite blended.  
[00:59:15] Like I might not have the full picture on everything, but not every person on the team has like the full three hundred and sixty degree view.  
[00:59:21] But we're collectively owning parts of the problem and working together to solve it.  
[00:59:25] Yeah.  
[00:59:26] Wow.  
[00:59:27] And looking ahead, what is the single biggest challenge facing the Open Cloud community today?  
[00:59:33] I wouldn't say so much challenge of the community, but I would say there is a lot of opportunity.  
[00:59:39] There is a large percentage of users in the world that are still not haven't fully adopted AI yet.  
[00:59:45] For us, it's like how do we make this more accessible to the general public, to moms, dads, uncles, aunties, whatever?  
[00:59:50] Like how do we make AI easy to understand and work with?  
[00:59:54] Because I think if people can access it, they can use it, they can understand it.  
[00:59:58] And it means that they can have a say on what their future looks like with artificial intelligence.  
[01:00:02] Whereas, if you don't get a chance to use it, I think that's like you know not fair.  
[01:00:06] So we're trying to make sure that everyone can can get access to something like this technology.  
[01:00:11] And I think there's still a huge percentage of population that still hasn't touched AI.  
[01:00:15] So how do we how do we enable that?  
[01:00:17] On top of that, I think one moment people are waiting for is Apple, and people are really hoping that the mobile agent can really work, so that people, you know,  
[01:00:29] billions of people who are having phones can most people's computer is their phone, right?  
[01:00:33] They everyone has a phone, but they don't have a computer.  
[01:00:35] So having like that on-device agent-first experience is probably going to be quite critical.  
[01:00:40] You guys have any plan to perhaps work with Apple to make the AI experience better?  
[01:00:45] Time will tell.  
[01:00:46] Yeah, but it's hard.  
[01:00:48] Like we want to integrate with every AI technology out there, but yeah, we'll see.  
[01:00:54] And open source projects can be more difficult to sustain than the traditional software projects because infrastructure, talent, maintenance, operation all takes money,  
[01:01:08] right?  
[01:01:08] Why would you guys want to keep OpenCL as open source community?  
[01:01:12] Because we can see some open source community, for example, VIM and SG Lang, the founders actually came out to start their own business, own startup to raise money.  
[01:01:24] They have very impressive fundraising, and you know they they are saying only startups can make things happen faster during the AI era.  
[01:01:34] Do you agree?  
[01:01:36] I mean, I don't know if there's a right or wrong answer for this, but I would say Peter's wishes were like he thinks the only way the OpenCL survives and is fair to everyone is that it remains in the in a foundation and it's not controlled by one company or one country or one entity,  
[01:01:52] and that way it can be truly embraced by the community.  
[01:01:55] And I think by doing this, we've been fully embraced by China, the US tech companies, moms, dads, like everyone, right?  
[01:02:03] And I think that's enabled everyone to go, okay, this is like a fair kind of like a Switzerland of AI.  
[01:02:08] We're happy to work with work with that.  
[01:02:10] And we've had people reach out to us that exclusively want to find a way to work with us because we're in the foundation model.  
[01:02:16] So I think it brings benefit.  
[01:02:18] And yes, it doesn't generate revenue or create sort of capital wealth, but I think it gives back to the community.  
[01:02:26] What we give back creates opportunity for the industry to then create more capital.  
[01:02:30] So I think it's a positive sum game for everyone at the end of the day.  
[01:02:34] It's selfless, I think, in a way for Peter to go, hey, I want to give this to the world.  
[01:02:38] But I think it's a beautiful thing that's happened.  
[01:02:40] Great to hear.  
[01:02:41] How is your experience with WIC this year so far?  
[01:02:46] Yeah, I'm just hearing lots of crazy things so far.  
[01:02:48] Yeah, I haven't had a chance to go out yet this week, but I think it's going to be great.  
[01:02:53] I'm giving a keynote about my journey through open source, which I think is going to be great, and I'm going to be like really excited to see a lot of technology companies here and get part in the conversation as well.  
[01:03:04] I think it's going to be like a very invigorating week.  
[01:03:07] I think by the time the conference is finished, I'm going to be like, yeah, I'm I'm done, but really excited.  
[01:03:14] I'm glad to be here back in Shanghai as well.  
[01:03:17] Okay, cool.  
[01:03:17] Last question.  
[01:03:18] So for the next twelve months, if you can give us some predictions, you know what are the most important three things that will happen, whether it's agent-related or not.  
[01:03:31] I don't want to give too much away.  
[01:03:32] I think the thing that people need to watch out for, I think, is kind of interesting.  
[01:03:35] Is like how do agents communicate and collaborate with other agents?  
[01:03:38] Is going to be the next sort of interesting thing.  
[01:03:41] If say so to model company comes up with a solution, another model company comes up with a solution, how do these all coexist and work together?  
[01:03:49] We're going to have like a world like phones, right?  
[01:03:51] Everyone's going to have a different phone, but they need to be able to.  
[01:03:53] Call each other, right?  
[01:03:54] It's going to be a very similar process, so I think that's going to be one that's going to be really interesting to see what happens.  
[01:03:59] We're experimenting on some ideas around that, but that's going to be really cool to see because I think that's going to be where we're going to start seeing some some really interesting unlock when I don't know my personal agent can call my work agent and share some information and get to work together and solve some problems,  
[01:04:16] right?  
[01:04:17] Yeah, I really heard some scary stories saying like the AI agents actually invent their own language that humans don't understand.  
[01:04:28] We'll see, but a lot of the mechanistic interpretability stuff is quite interesting around evaluation.  
[01:04:35] The agents will find what's mathematically most optimal or like whatever's been trained into it.  
[01:04:41] I think we just have to be careful of like seeing that because agents are doing some behavior that it becomes.  
[01:04:47] We don't want to kind of say because X is happening, it's Y.  
[01:04:51] We need to understand like what's causing it.  
[01:04:53] But I think safety is one aspect, but also like just even getting these agents to communicate with each other is going to be the the challenge, right?  
[01:05:01] Like you've got enterprise, you've got different software systems, you've got different architectures.  
[01:05:05] So I think a lot of those kind of challenges are like actually way more complicated than security, for example.  
[01:05:11] Yeah.  
[01:05:12] All right.  
[01:05:13] Okay.  
[01:05:14] Anything else you want to add?  
[01:05:15] No, I just want to say thank you for the opportunity to come and have this interview and this conversation.  
[01:05:20] So excited to be here.  
[01:05:22] Okay.  
[01:05:22] Thank you so much, Vincent.  
[01:05:23] Hope you enjoy your time here in Shanghai.  
[01:05:26] Thank you.  
[01:05:26] That's it.  
