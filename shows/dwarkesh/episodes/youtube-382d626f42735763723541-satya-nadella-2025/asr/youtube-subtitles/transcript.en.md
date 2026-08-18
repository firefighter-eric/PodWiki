# Satya Nadella – How Microsoft thinks about AGI

[00:00:54] Today we are interviewing Satya Nadella.  
[00:00:57] "We" being me and Dylan Patel, who is founder of SemiAnalysis. Satya, welcome.  
[00:01:02] Thank you. It's great. Thanks for coming over to Atlanta.  
[00:01:04] Thank you for giving us the tour of the new facility.  
[00:01:07] It's been really cool to see. Absolutely.  
[00:01:09] Satya and Scott Guthrie, Microsoft's EVP of Cloud and AI, give us a tour of  
[00:01:14] their brand new Fairwater 2 data center, the current most powerful in the world.  
[00:01:19] We've tried to 10x the training capacity every 18 to 24 months.  
[00:01:23] So this would effectively be a 10x increase from what GPT-5 was trained with.  
[00:01:28] So to put it in perspective in the number of optics, the network optics in this building  
[00:01:32] is almost as much as all of Azure across all our data centers two and a half years ago.  
[00:01:38] It's got like five million network connections. You've got all this bandwidth between different  
[00:01:43] sites in a region and between the two regions. So is this like a big bet on scaling in the  
[00:01:47] future, that you anticipate in the future that there's going to be some huge model that will  
[00:01:51] require two whole different regions to train? The goal is to be able to aggregate these  
[00:01:56] flops for a large training job and then put these things together across sites.  
[00:02:02] The reality is you'll use it for training and then you'll use it for data gen, you'll use it  
[00:02:09] for inference in all sorts of ways. It's not like it's going to be used  
[00:02:13] only for one workload forever. Fairwater 4, which you're going  
[00:02:16] to see under construction nearby, will also be on that one petabit network so that we can actually  
[00:02:22] link the two at a very high rate. Then we do the AI WAN connecting to  
[00:02:26] Milwaukee where we have multiple other Fairwaters being built.  
[00:02:29] Literally you can see the model parallelism and the data parallelism.  
[00:02:35] It's kind of built for, essentially, the training jobs, the super pods across this campus.  
[00:02:44] And then with the WAN, you can go to the Wisconsin data center.  
[00:02:49] You literally run a training job with all of them getting aggregated.  
[00:02:54] What we're seeing right here is a cell with no servers in it yet, no racks.  
[00:02:58] How many racks are in a cell? We don't necessarily share that per se, but…  
[00:03:03] That’s the reason I ask. You'll see upstairs.  
[00:03:09] I'll start counting. You can start counting.  
[00:03:10] We'll let you start counting. How many cells are there in this building?  
[00:03:11] That part also I can't tell you. Well, division is easy, right?  
[00:03:18] My God, it's kind of loud. Are you looking at this like,  
[00:03:22] "Now I see where my money is going." It's like, "I run a software company.  
[00:03:27] Welcome to the software company." How big is the design space once  
[00:03:30] you've decided to use the GB200s and the NVLink? How many other decisions are there to be made?  
[00:03:35] There is coupling from the model architecture to what is the physical plan that's optimized.  
[00:03:44] And it's also scary in that sense, which is, there's going to be a new chip that'll come  
[00:03:49] out. Take Vera Rubin Ultra. That's going to have power density that's going to be so different,  
[00:03:55] with cooling requirements that are going to be so different.  
[00:03:58] So you kind of don't want to just build all to one spec.  
[00:04:04] That goes back a little bit to the dialogue we'll have,  
[00:04:06] which is that you want to be scaling in time as opposed to scale once and then be stuck with it.  
[00:04:15] When you look at all the past technological transitions—whether it be railroads or the  
[00:04:20] Internet or replaceable parts, industrialization, the cloud, all of these things—each revolution  
[00:04:27] has gotten much faster in the time it goes from technology discovered to ramp  
[00:04:31] and pervasiveness through the economy. Many folks who have been on Dwarkesh's  
[00:04:35] podcast believe this is the final technological revolution or transition,  
[00:04:40] and that this time is very, very different. At least so far in the markets, in three years  
[00:04:46] we've already skyrocketed to hyperscalers doing $500 billion of capex next year,  
[00:04:51] which is a scale that's unmatched to prior revolutions in terms of speed.  
[00:04:56] The end state seems to be quite different. Your framing of this seems quite  
[00:05:02] different from what I would call the "AI bro" who's like, "AGI is coming."  
[00:05:09] I'd like to understand that more. I start with the excitement that I  
[00:05:15] also feel for the idea that maybe after the Industrial Revolution this is the  
[00:05:18] biggest thing. I start with that premise. But at the same time, I'm a little grounded in the  
[00:05:27] fact that this is still early innings. We've built some very useful things,  
[00:05:31] we're seeing some great properties, these scaling laws seem to be working.  
[00:05:37] I'm optimistic that they'll continue to work. Some of it does require real science  
[00:05:44] breakthroughs, but it's also a lot of engineering and what have you.  
[00:05:48] That said, I also sort of take the view that even what has been happening in the  
[00:05:53] last 70 years of computing has also been a march that has helped us move.  
[00:06:04] I like one of the things that Raj Reddy has as a metaphor for what AI is.  
[00:06:09] He's a Turing Award winner at CMU. He had this, even pre-AGI. He had this metaphor  
[00:06:18] for AI, it should either be a guardian angel or a cognitive amplifier. I love that. It's a  
[00:06:24] simple way to think about what this is. Ultimately, what is its human utility?  
[00:06:29] It is going to be a cognitive amplifier and a guardian angel.  
[00:06:34] If I view it that way, I view it as a tool. But then you can also go very mystical about  
[00:06:39] it and say this is more than a tool. It does all these things, which only  
[00:06:43] humans did before so far. But that has been the case  
[00:06:45] with many technologies in the past. Only humans did a lot of things,  
[00:06:48] and then we had tools that did them. We don't have to get wrapped up in the definition  
[00:06:53] here, but one way to think about it is, maybe it takes five years, ten years, twenty years.  
[00:06:57] At some point, eventually a machine is producing Satya tokens, and the Microsoft board thinks that  
[00:07:03] Satya tokens are worth a lot. How much are you wasting of  
[00:07:06] this economic value by interviewing Satya? I could not afford the API costs of Satya tokens.  
[00:07:14] Whatever you want to call it, are the Satya tokens a tool or an agent, whatever.  
[00:07:18] Right now, if you have models that cost on the order of dollars or cents per million tokens,  
[00:07:22] there's just an enormous room for margin expansion there,  
[00:07:27] where a million tokens of Satya are worth a lot. Where does that margin go and what level of that  
[00:07:36] margin is Microsoft involved in is the question I have.  
[00:07:41] In some sense this goes back again to, essentially, what's the economic growth  
[00:07:46] picture going to really look like? What's the firm going to look like?  
[00:07:50] What's productivity going to look like? That to me is where, again, if the Industrial  
[00:07:54] Revolution created… After 70 years of diffusion is when you started seeing the economic growth.  
[00:08:01] That's the other thing to remember. Even if the tech is diffusing fast this  
[00:08:08] time around, for true economic growth to appear it has to diffuse to a point where the work,  
[00:08:15] the work artifact, and the workflow has to change. So that's one place where I think the change  
[00:08:20] management required for a corporation to truly change is something we shouldn't discount.  
[00:08:26] Going forward, do humans and the tokens they produce get higher leverage, whether it's the  
[00:08:34] Dwarkesh or the Dylan tokens of the future? Think about the amount of technology.  
[00:08:39] Would you be able to run SemiAnalysis or this podcast without technology?  
[00:08:43] No chance, at the scale that you have been able to achieve, there’s no chance.  
[00:08:48] So the question is, what's that scale? Is it going to be 10x'ed with something  
[00:08:52] that comes through? Absolutely. Therefore, whether you're ramped to some revenue number  
[00:08:58] or you're ramped to some audience number or what have you, that I think is what's going to happen.  
[00:09:03] The point is, what took 70 years, maybe 150 years for the Industrial Revolution,  
[00:09:10] may happen in 20 years, 25 years. I would love to compress what happened  
[00:09:16] in 200 years of the Industrial Revolution into a 20-year period, if we're lucky.  
[00:09:23] Microsoft historically has been perhaps the greatest software company,  
[00:09:27] the largest software-as-a-service company. You've gone through a transition in the past  
[00:09:31] where you used to sell Windows licenses and disks of Windows or Microsoft,  
[00:09:35] and now you sell subscriptions to 365. As we go from that transition to where  
[00:09:44] your business is today, there's also a transition going on after that.  
[00:09:48] Software-as-a-service has incredibly low incremental cost per user.  
[00:09:52] There's a lot of R&D, there's a lot of customer acquisition costs.  
[00:09:55] This is sort of why, not Microsoft, but the SaaS companies have underperformed  
[00:09:58] massively in the markets, because the COGS of AI is just so high, and that just completely  
[00:10:03] breaks how these business models work. How do you, as perhaps the greatest  
[00:10:10] software-as-a-service company, transition Microsoft to this new age where COGS matters a lot  
[00:10:17] and the incremental cost per user is different? Because right now you're charging like, "Hey,  
[00:10:21] it's 20 bucks for Copilot." It's a great question because in some  
[00:10:26] sense with the business models themselves, the levers are going to remain similar.  
[00:10:32] If you look at the menu of models starting from consumer all the way, there will be some ad unit,  
[00:10:40] there will be some transaction, there will be some device gross  
[00:10:44] margin for somebody who builds an AI device. There will be subscriptions, consumer and  
[00:10:49] enterprise, and then there'll be consumption. So I still think those are all the meters.  
[00:10:56] To your point, what is a subscription? Up to now, people like subscriptions  
[00:11:01] because they can budget for them. They are essentially entitlements to  
[00:11:06] some consumption rights that come encapsulated in a subscription.  
[00:11:11] So I think that in some sense becomes a pricing decision.  
[00:11:15] How much consumption you are entitled to is, if you look at all the coding subscriptions,  
[00:11:21] kind of what they are, right? Then you have the pro tier,  
[00:11:24] the standard tier, and what have you. So I think that's how the pricing  
[00:11:30] and the margin structures will get tiered. The interesting thing is that at Microsoft,  
[00:11:36] the good news for us is we are in that business across all those meters.  
[00:11:43] At a portfolio level, we pretty much have consumption, subscriptions,  
[00:11:50] to all of the other consumer levers as well. I think time will tell which of these  
[00:11:56] models make sense in what categories. One thing on the SaaS side, since you  
[00:12:01] brought it up, which I think a lot about. Take Office 365 or Microsoft 365.  
[00:12:08] Having a low ARPU is great, because here's an interesting thing.  
[00:12:11] During the transition from server to cloud, one of the questions we used to ask ourselves is,  
[00:12:16] "Oh my God, if all we did was just basically move the same users who were using our Office  
[00:12:23] licenses and our Office servers at the time to the cloud, and we had COGS,  
[00:12:29] this is going to not only shrink our margins but we'll be fundamentally a less profitable company."  
[00:12:36] Except what happened was the move to the cloud expanded the market like crazy.  
[00:12:43] We sold a few servers in India, we didn't sell much.  
[00:12:46] Whereas in the cloud suddenly everybody in India also could  
[00:12:49] afford fractionally buying servers, the IT cost. In fact, the biggest thing I had not realized,  
[00:12:55] for example, was the amount of money people were spending buying storage underneath SharePoint.  
[00:13:03] In fact, EMC's biggest segment may have been storage servers for SharePoint.  
[00:13:09] All that sort of dropped in the cloud because nobody had to go buy.  
[00:13:13] In fact, it was working capital, meaning basically, it was cash flow out.  
[00:13:17] So it expanded the market massively. So this AI thing will be that.  
[00:13:24] If you take coding, what we built with GitHub and VS Code over decades, suddenly  
[00:13:33] the coding assistant is that big in one year. That I think is what's going to happen as well,  
[00:13:39] which is the market expands massively. There’s a question of, the market will  
[00:13:44] expand, but will the parts of the revenue that touch Microsoft expand? Copilot is an example.  
[00:13:50] If you look earlier this year, according to Dylan's numbers, GitHub Copilot revenue  
[00:13:58] was like $500 million or something like that and there were no close competitors.  
[00:14:03] Whereas now you have Claude Code, Cursor, and Copilot  
[00:14:08] with around similar revenue, around a billion. Codex is catching up around $700–800 million.  
[00:14:13] So the question is, across all the surfaces that Microsoft has access to, what is the advantage  
[00:14:17] that Microsoft's equivalents of Copilot have? By the way, I love this chart.  
[00:14:22] I love this chart for so many reasons. One is we're still on the top.  
[00:14:27] Second is all these companies that are listed here are all companies that have been born in  
[00:14:32] the last four or five years. That to me is the best sign.  
[00:14:37] You have new competitors, new existential problems.  
[00:14:39] When you say, who's it now? Claude's going to kill you,  
[00:14:42] Cursor is going to kill you, it's not Borland. Thank God. That means we are in the right  
[00:14:47] direction. This is it. The fact that we went from nothing to this scale is the market expansion.  
[00:14:55] This is like the cloud-like stuff. Fundamentally, this category of  
[00:14:59] coding and AI is probably going to be one of the biggest categories.  
[00:15:04] It is the software factory category. In fact, it may be bigger than knowledge work.  
[00:15:08] I want to keep myself open-minded about it. We're going to have tough competition.  
[00:15:13] That's your point, which is a great one. But I'm glad we have parlayed  
[00:15:20] what we had into this and now we have to compete. On the competing side, even in the last quarter we  
[00:15:27] just finished, we did our quarterly announcement and I think we grew from 20 to 26 million subs.  
[00:15:32] I feel good about our sub growth and where the direction of travel on that is.  
[00:15:37] But the more interesting thing that has happened is, guess where all the repos of all these other  
[00:15:44] guys who are generating lots and lots of code go? They go to GitHub. GitHub is at an all-time high  
[00:15:51] in terms of repo creation, PRs, everything. In some sense we want to keep that open,  
[00:15:58] by the way. That means we want to have that.  
[00:16:00] We don't want to conflate that with our own growth.  
[00:16:03] Interestingly enough, we are getting one developer joining GitHub a second  
[00:16:06] or something, that is the stat, I think. And 80% of them just fall into some GitHub  
[00:16:11] Copilot workflow, just because there are. By the way, many of these things will even  
[00:16:16] use some of our coding code review agents, which are by default on, just because you can use it.  
[00:16:21] We'll have many, many structural shots at this. The thing that we're also going  
[00:16:26] to do is what we did with Git. The primitives of GitHub, starting with Git,  
[00:16:32] to issues, to actions, these are powerful, lovely things because they kind of are all built around  
[00:16:39] your repo. We want to extend that. Last week at GitHub Universe, that's kind of what we did.  
[00:16:45] We said Agent HQ was the conceptual thing that we said we're going to build out.  
[00:16:51] This is where, for example, you have a thing called Mission Control.  
[00:16:54] You go to Mission Control, and now I can fire off. Sometimes I describe it as the cable TV of all  
[00:17:00] these AI agents because I'll have, essentially packaged into one subscription, Codex, Claude,  
[00:17:08] Cognition stuff, anyone's agents, Grok, all of them will be there.  
[00:17:13] So I get one package and then I can literally go issue a task and steer them so they'll all  
[00:17:20] be working in their independent branches. I can monitor them. I think that's going to be one of  
[00:17:27] the biggest places of innovation, because right now I want to be able to use multiple agents.  
[00:17:32] I want to be able to then digest the output of the multiple agents.  
[00:17:35] I want to be able to then keep a handle on my repo.  
[00:17:38] If there's some kind of a heads-up display that needs to be built and then for me to  
[00:17:43] quickly steer and triage what the coding agents have generated, that to me, between VS Code,  
[00:17:49] GitHub, and all of these new primitives we'll build as Mission Control with a control plane.  
[00:17:56] Observability… Just think about everyone who is going to deploy all this.  
[00:18:00] It will require a whole host of observability of what agent did what at what time to what  
[00:18:05] code base. I feel that's the opportunity. At the end of the day your point is well taken,  
[00:18:11] which is we better be competitive and innovate. If we don't, we will get toppled.  
[00:18:15] But I like the chart, at least as long as we're on the top, even with competition.  
[00:18:20] The key point here is sort of that GitHub will keep growing  
[00:18:22] regardless of whose coding agent wins. But that market only grows at say 10,  
[00:18:28] 15, 20%, which is way above GDP. It's a great compounder. But these AI coding agents have  
[00:18:33] grown from say $500 million run rate at the end of last year—which was just GitHub Copilot—to  
[00:18:39] now where the current run rate across GitHub Copilot, Claude Code, Cursor, Cognition, Windsurf,  
[00:18:45] Replit, OpenAI Codex… That’s run rating at $5–6 billion now for the Q4 of this year.  
[00:18:54] That's 10x. When you look at the TAM of software agents, is it the $2 trillion of wages you pay  
[00:19:02] people, or is it something beyond that? Because every company in the world will  
[00:19:07] now be able to develop software more? No question Microsoft takes a slice of that.  
[00:19:13] But you've gone from near 100%, or certainly way above 50%,  
[00:19:17] to sub-25% market share in just one year. What is the confidence that people can get  
[00:19:23] that Microsoft will keep winning? It goes back a little bit, Dylan,  
[00:19:27] to that there's no birthright here, that we should have any confidence  
[00:19:30] other than to say we should go innovate. Knowing the lucky break we have, in some sense,  
[00:19:37] is that this category is going to be a lot bigger than anything we had high share in.  
[00:19:42] Let me say it that way. You could say we had high  
[00:19:46] share in VS Code, we had high share in the repos with GitHub, and that was a good market.  
[00:19:52] But the point is that even having a decent share in what is a much more expansive market…  
[00:19:58] You could say we had a high share in client-server server computing.  
[00:20:02] We have much lower share than that in hyperscale. But is it a much bigger business? By orders of  
[00:20:09] magnitude. So at least it's existence proof that Microsoft has been okay even if our share position  
[00:20:15] has not been as strong as it was, as long as the markets we are competing in are creating  
[00:20:21] more value. And there are multiple winners. That's the stuff. But I take your point that ultimately  
[00:20:29] it all means you have to get competitive. I watch that every quarter. That’s why I'm very  
[00:20:34] optimistic about what we're going to do with Agent HQ, turning GitHub into a place where  
[00:20:42] all these agents come. As I said, we'll have  
[00:20:44] multiple shots on goal on there. It need not be… Some of these guys  
[00:20:49] can succeed along with us, so it doesn't need to be just one winner and one subscription.  
[00:20:56] I guess the reason to focus on this question is that it's not just about GitHub,  
[00:20:59] but fundamentally about Office and all the other software that Microsoft offers.  
[00:21:05] One vision you could have about how AI proceeds is that the models are going  
[00:21:10] to keep being hobbled and you'll need this direct visible observability all the time.  
[00:21:17] Another vision is that over time these models which are now doing tasks that take two minutes,  
[00:21:21] in the future, they'll be doing tasks that take 10, 30 minutes.  
[00:21:24] In the future, maybe they're doing days worth of work autonomously.  
[00:21:28] Then the model companies are charging thousands of dollars maybe for access to, really,  
[00:21:33] a coworker which could use any UI to communicate with their human and migrate between platforms.  
[00:21:42] If we’re getting closer to that, why aren't the model companies that are  
[00:21:46] just getting more and more profitable, the ones that are taking all the margin?  
[00:21:49] Why is the place where the scaffolding happens, which becomes less and less relevant as the AI  
[00:21:54] becomes more capable, going to be that important? That goes to Office as it exists now versus  
[00:21:59] coworkers that are just doing knowledge work. That's a great point. Does all the value  
[00:22:06] migrate just to the model? Or does it get split between  
[00:22:13] the scaffolding and the model? I think that time will tell.  
[00:22:19] But my fundamental point also is that the incentive structure gets clear.  
[00:22:26] Let’s take information work, or take even coding. Already in fact, one of my favorite settings  
[00:22:33] in GitHub Copilot is called auto, which will just optimize.  
[00:22:38] In fact I buy a subscription and the auto one will start picking and optimizing  
[00:22:44] for what I am asking it to do. It could even be fully autonomous.  
[00:22:49] It could arbitrage the tokens available across multiple models to go get a task done.  
[00:22:56] If you take that argument, the commodity there will be models.  
[00:23:01] Especially with open source models, you can pick a checkpoint and you can take a  
[00:23:05] bunch of your data and you're seeing it. I think all of us will start, whether  
[00:23:09] it's from Cursor or from Microsoft, seeing some in-house models even.  
[00:23:15] And then you'll offload most of your tasks to it. So one argument is if you win the  
[00:23:22] scaffolding—which today is dealing with all the hobbling problems or the  
[00:23:28] jaggedness of these intelligence problems, which you kind of have to—if you win that,  
[00:23:34] then you will vertically integrate yourself into the model just because you will have  
[00:23:38] the liquidity of the data and what have you. There are enough and more checkpoints that  
[00:23:42] are going to be available. That's the other thing. Structurally, I think there will always  
[00:23:47] be an open source model that will be fairly capable in the world that you could then use,  
[00:23:54] as long as you have something that you can use that with, which is data and a scaffolding.  
[00:24:00] I can make the argument that if you're a model company, you may have a winner's curse.  
[00:24:06] You may have done all the hard work, done unbelievable innovation, except  
[00:24:11] it's one copy away from that being commoditized. Then the person who has the data for grounding and  
[00:24:20] context engineering, and the liquidity of data can then go take that checkpoint and train it.  
[00:24:27] So I think the argument can be made both ways. Unpacking what you said,  
[00:24:31] there's two views of the world. One is that there are so many different  
[00:24:35] models out there. Open source exists. There will be differences between the models that  
[00:24:39] will drive some level of who wins and who doesn't. But the scaffolding is what enables you to win.  
[00:24:45] The other view is that, actually, models are the key IP.  
[00:24:49] And everyone's in a tight race and there's some, "Hey, I can use Anthropic or OpenAI."  
[00:24:55] You can see this in the revenue charts. OpenAI's revenue started skyrocketing once they  
[00:24:59] finally had a code model with similar capabilities to Anthropic, although in different ways.  
[00:25:05] There's the view that the model companies are the ones that garner all the margin.  
[00:25:10] Because if you look across this year, at least at Anthropic,  
[00:25:13] their gross margins on inference went from well below 40% to north of 60% by the end of the year.  
[00:25:20] The margins are expanding there despite more Chinese open source models than ever.  
[00:25:25] OpenAI is competitive, Google is competitive, X/Grok is now competitive.  
[00:25:29] All these companies are now competitive, and yet despite this, the margins have expanded at  
[00:25:33] the model layer significantly. How do you think about that?  
[00:25:38] It's a great question. Perhaps a few years ago people were saying, "Oh, I could just wrap a  
[00:25:45] model and build a successful company." That has probably gotten debunked just  
[00:25:51] because of the model capabilities, and the tools used, in particular.  
[00:25:56] But the interesting thing is, when I look at Office 365, let's take even this little thing we  
[00:26:01] built called Excel Agent. It's interesting. Excel Agent is not a UI-level wrapper.  
[00:26:07] It's actually a model that is in the middle tier. In this case, because we have all the IP from  
[00:26:14] the GPT family, we are taking that and putting it into the core middle tier of  
[00:26:21] the Office system to teach it what it means to natively understand Excel, everything in it.  
[00:26:30] It's not just, "Hey, I just have a pixel-level understanding."  
[00:26:33] I have a full understanding of all the native artifacts of Excel.  
[00:26:39] Because if you think about it, if I'm going to give it some reasoning task,  
[00:26:42] I need to even fix the reasoning mistakes I make. That means I need to not just see the pixels,  
[00:26:48] I need to be able to see, "Oh, I got that formula wrong," and I need to understand that.  
[00:26:53] To some degree, that's all being done not at the UI wrapper level with some prompt,  
[00:26:57] but it's being done in the middle tier by teaching it all the tools of Excel.  
[00:27:02] I'm giving it essentially a markdown to teach it the skills of what it means to  
[00:27:06] be a sophisticated Excel user. It's a weird thing that it goes  
[00:27:10] back a little bit to the AI brain. You're building not just Excel,  
[00:27:17] business logic in its traditional sense. You're taking the Excel business logic  
[00:27:21] in the traditional sense and wrapping essentially a cognitive layer to it,  
[00:27:25] using this model which knows how to use the tool. In some sense, Excel will come with an analyst  
[00:27:32] bundled in and with all the tools used. That's the type of stuff that will get  
[00:27:37] built by everybody. So even for the  
[00:27:39] model companies, they’ll have to compete. If they price stuff high, guess what, if I'm a  
[00:27:45] builder of a tool like this, I'll substitute you. I may use you for a while.  
[00:27:50] So as long as there's competition… There's always a winner-take-all thing.  
[00:27:53] If there's going to be one model that is better than everybody else with  
[00:27:56] massive distance, yes, that's a winner-take-all. But as long as there's competition where there are  
[00:28:01] multiple models, just like hyperscale competition, and there's an open source check, there is enough  
[00:28:07] room here to go build value on top of models. At Microsoft, the way I look at it is  
[00:28:14] that we are going to be in the hyperscale business, which will support multiple models.  
[00:28:19] We will have access to OpenAI models for seven more years, which we will innovate on top of.  
[00:28:27] Essentially, I think of ourselves as having a frontier-class model that we can  
[00:28:31] use and innovate on with full flexibility. And we'll build our own models with MAI.  
[00:28:39] So we will always have a model level. And then we'll build—whether it's in security,  
[00:28:44] whether it's in knowledge work, whether it's in coding, or in science—our own application  
[00:28:49] scaffolding, which will be model-forward.  
[00:28:52] It won't be a wrapper on a model, but the model will be wrapped into the application.  
[00:28:58] I have so many questions about the other things you mentioned.  
[00:29:01] But before we move onto those topics, I still wonder whether this is not  
[00:29:06] forward-looking on AI capabilities, where you're imagining models like they exist today.  
[00:29:13] It takes a screenshot of your screen, but it can't look inside each cell and what the formula is.  
[00:29:17] I think the better mental model here is just imagining that these models will be  
[00:29:22] able to use a computer as well as a human. A human knowledge worker who is using Excel  
[00:29:27] can look into the formulas, can use alternative software, can migrate data between Office 365  
[00:29:33] and another piece of software if the migration is necessary, et cetera.  
[00:29:37] That's kind of what I'm saying. But if that's the case, then the  
[00:29:40] integration with Excel doesn't matter that much. No, no, don't worry about the Excel integration.  
[00:29:46] After all, Excel was built as a tool for analysts. Great. So whoever is this AI that  
[00:29:52] is an analyst should have tools that they can use. They have the computer. Just the way a human can  
[00:29:58] use a computer. That's their tool. The tool is the computer. So all  
[00:30:02] I’m saying is that I'm building an analyst as essentially an AI agent,  
[00:30:08] which happens to come with an a priori knowledge of how to use all of these analytical tools.  
[00:30:16] Just to make sure we're talking about the same thing, is it a thing  
[00:30:19] that a human like me using Excel… No, it's completely autonomous. So  
[00:30:27] we should now maybe lay out what I think the future of the company is.  
[00:30:32] The future of the company would be the tools business in which I have a computer, I use Excel.  
[00:30:37] In fact, in the future I'll even have a Copilot, and that Copilot will also have agents.  
[00:30:42] But it's still me steering everything, and everything is coming back. That's one world.  
[00:30:50] The second world is the company just literally provisions a computing resource for an AI agent,  
[00:30:57] and that is working fully autonomously. That fully autonomous agent will have  
[00:31:03] essentially an embodied set of those same tools that are available to it.  
[00:31:08] So this AI tool that comes in also has not just a raw computer,  
[00:31:14] because it's going to be more token-efficient to use tools to get stuff done.  
[00:31:19] In fact, I kind of look at it and say that our business,  
[00:31:21] which today is an end-user tools business, will become essentially an infrastructure  
[00:31:26] business in support of agents doing work. It's another way to think about it.  
[00:31:33] In fact, all the stuff we built underneath M365 still is going to be very relevant.  
[00:31:41] You need some place to store it, some place to do archival, some place to do discovery,  
[00:31:46] some place to manage all of these activities, even if you're an AI agent. It's a new infrastructure.  
[00:31:55] To make sure I understand, you're saying theoretically a future AI that  
[00:31:59] has actual computer use—which all these model companies are working on right now—could use,  
[00:32:04] even if it's not partnered with Microsoft or under our umbrella, Microsoft software.  
[00:32:09] But you're saying, if you're working with our infrastructure, we're going  
[00:32:14] to give them lower-level access that makes it more efficient for you to do the same things  
[00:32:18] you could have otherwise done anyways? 100%. What happened is we had servers,  
[00:32:26] then there was virtualization, and then we had many more servers.  
[00:32:30] That's another way to think about this. Don't think of the tool as the end thing.  
[00:32:36] What is the entire substrate underneath that tool that humans use?  
[00:32:41] That entire substrate is the bootstrap for the AI agent as well,  
[00:32:45] because the AI agent needs a computer. In fact, one of the fascinating  
[00:32:49] things where we're seeing a significant amount of growth is all these guys who are doing these  
[00:32:54] Office artifacts and what have you, as autonomous agents and so on want to provision Windows 365.  
[00:33:00] They really want to be able to provision a computer for these agents. Absolutely.  
[00:33:07] That's why we're going to have essentially an end-user computing infrastructure business,  
[00:33:12] which is going to just keep growing because it's going to grow faster than the number of users.  
[00:33:18] That's one of the other questions people ask me, "Hey, what happens to the per-user business?"  
[00:33:22] At least the early signs maybe, the way to think about the per-user business  
[00:33:25] is not just per user, it's per agent. And if you say it's per user and per agent,  
[00:33:31] the key is what's the stuff to provision for every agent?  
[00:33:35] A computer, a set of security things around it, an identity around it.  
[00:33:42] All those things, observability and so on, are the management layers.  
[00:33:46] That's all going to get baked into that. The way to frame it—at least the way I currently  
[00:33:50] think about it and I’d like to hear your view—is that these model companies are all building  
[00:33:55] environments to train their models to use Excel or Amazon shopping or whatever it is, book flights.  
[00:34:03] But at the same time, they're also training these models to do migration.  
[00:34:08] Because that is probably the most immediately valuable thing: converting mainframe-based  
[00:34:13] systems to standard cloud systems, converting Excel databases into real databases with SQL,  
[00:34:21] or converting what is done in Word and Excel to something that is more programmatic and  
[00:34:28] more efficient in a classical sense that can be done by humans as well.  
[00:34:32] It's just not cost-effective for the software developer to do that.  
[00:34:35] That seems to be what everyone is going to do with AI, for the next few years at  
[00:34:39] least, to massively drive value. How does Microsoft fit into that  
[00:34:44] if the models can utilize the tools themselves to migrate to something?  
[00:34:49] Yes, Microsoft has a leadership position in databases and in storage and in all  
[00:34:54] these other categories, but the use of an Office ecosystem is going to  
[00:35:01] be significantly less just like the use of a mainframe ecosystem could be potentially less.  
[00:35:05] Now mainframes have grown for the last two decades actually, even though no one talks about them  
[00:35:08] anymore. They've still grown. 100%, I agree with that.  
[00:35:11] How does that flow? At the end of the day, there  
[00:35:16] is going to be a significant amount of time where there's going to be a hybrid world, because people  
[00:35:20] are going to be using the tools that are going to be working with agents that have to use tools,  
[00:35:24] and they have to communicate with each other. What's the artifact I generate that  
[00:35:29] then a human needs to see? All of these things will be real  
[00:35:32] considerations in any place, the outputs, inputs. I don't think it'll just be about,  
[00:35:36] "Oh, I migrated off." The bottom line is that I  
[00:35:38] have to live in this hybrid world. But that doesn't fully answer your  
[00:35:42] question because there can be a real new efficient frontier where it's just agents  
[00:35:47] working with agents and completely optimized. Even when agents are working with agents,  
[00:35:52] what are the primitives that are needed? Do you need a storage system?  
[00:35:57] Does that storage system need to have e-discovery? Do you need to have observability?  
[00:36:03] Do you need to have an identity system that is going to use multiple models  
[00:36:07] with all having one identity system? These are all the core underlying rails  
[00:36:12] we have today for what are the Office systems or what have you.  
[00:36:16] And that's what we will have in the future as well. You've talked about databases. I mean man,  
[00:36:22] I would love all of Excel to have a database backend.  
[00:36:25] I would love for all that to happen immediately. And that database is a good database.  
[00:36:30] Databases in fact will be a big thing that will grow.  
[00:36:33] If I think about all of the Office artifacts being structured better, the ability to do the  
[00:36:40] joins between structured and unstructured better because of the agentic world, that will grow the  
[00:36:44] underlying infrastructure business. It happens that the consumption  
[00:36:48] of that is all being driven by agents. You could say all that is just-in-time generated  
[00:36:52] software by a model company. That could also be true. We will be one such model company too. We  
[00:36:59] will build in... The competition could be that we will build a model plus all the infrastructure and  
[00:37:06] provision it, and then there will be competition between a bunch of those folks who can do that.  
[00:37:12] Speaking of model companies, you say not only will you have the infrastructure,  
[00:37:16] you'll have the model itself. Right now, Microsoft AI's most  
[00:37:20] recent model that was released two months ago is 36 in Chatbot Arena.  
[00:37:25] You obviously have the IP rights to OpenAI. To the extent you agree with that,  
[00:37:30] it seems to be behind. Why is that the case, especially given  
[00:37:33] the fact that you theoretically have the right to fork OpenAI's monorepo or distill their models,  
[00:37:41] especially if it's a big part of your strategy that you need to have a leading model company?  
[00:37:46] First of all, we are absolutely going to use the OpenAI models  
[00:37:51] to the maximum across all of our products. That's the core thing that we're going to continue  
[00:37:57] to do all the way for the next seven years, and not just use it but then add value to it.  
[00:38:03] That's where the analyst and this Excel agent, these are all things that we will  
[00:38:08] do where we'll do RL fine-tuning. We'll do some mid-training runs  
[00:38:13] on top of a GPT family where we have unique data assets and build capability.  
[00:38:18] With the MAI model, the way that I think we’re going to think about it is that the  
[00:38:24] good news here with the new agreement is we can be very, very clear that we're going  
[00:38:28] to build a world-class superintelligence team and go after it with a high ambition.  
[00:38:32] But at the same time, we're also going to use this time to be smart  
[00:38:35] about how to use both these things. That means we will, on one end,  
[00:38:39] be very product-focused, and on the other end, be very research-focused.  
[00:38:45] Because we have access to the GPT family, the last thing I want to do is use my flops in a way that  
[00:38:52] is just duplicative and doesn't add much value. I want to be able to take the flops that we use  
[00:38:58] to generate a GPT family and maximize its value, while my MAI flops are being used for… Let's take  
[00:39:06] the image model that we launched, which I think is at number nine in the image arena.  
[00:39:12] We're using it both for cost optimization, it's on Copilot,  
[00:39:16] it's in Bing, and we're going to use that. We have an audio model in Copilot.  
[00:39:21] It's got personality and what have you. We optimized it for our product. So we will  
[00:39:25] do those. Even on the LMArena, we started on the text one and it debuted at like 13.  
[00:39:31] By the way, it was done only on around 15,000 H100s.  
[00:39:35] It was a very small model. So it was, again, to prove out  
[00:39:40] the core capability, the instruction following, and everything else.  
[00:39:44] We wanted to make sure we could match what was state of the art.  
[00:39:48] That shows us, given scaling laws, what we are capable of doing if we gave more flops to it.  
[00:39:53] The next thing we will do is an omni-model where we will take the work we have done in audio,  
[00:39:58] what we have done in image, and what we have done in text.  
[00:40:01] That will be the next pit stop on the MAI side. So when I think about the MAI roadmap, we are  
[00:40:06] going to build a first-class superintelligence team.  
[00:40:08] We are going to continue to drop, and do it in the open, some of these models.  
[00:40:12] They will either be used in our products, because they're going to be latency-friendly,  
[00:40:17] cost-friendly, or what have you, or they'll have some special capability.  
[00:40:21] And we will do real research in order to be ready for the next five, six, seven,  
[00:40:26] eight breakthroughs that are all needed on this march towards superintelligence—while  
[00:40:32] exploiting the advantage we have of having the GPT family that we can work on top of as well.  
[00:40:39] Say we roll forward seven years, you no longer have access to OpenAI models.  
[00:40:46] What does Microsoft do to make sure they are leading, or have a leading AI lab?  
[00:40:51] Today, OpenAI has developed many of the breakthroughs, whether it be scaling or reasoning.  
[00:40:56] Or Google's developed all the breakthroughs like transformers.  
[00:41:00] But it is also a big talent game. You've seen Meta spend north  
[00:41:04] of $20 billion on talent. You've seen Anthropic poach the entire  
[00:41:09] Blueshift reasoning team from Google last year. You've seen Meta poach a large reasoning and  
[00:41:14] post-training team from Google more recently. These sorts of talent wars are  
[00:41:18] very capital intensive. Arguably, if you're spending  
[00:41:22] $100 billion on infrastructure, you should also spend X amount of money on the people  
[00:41:28] using the infrastructure so that they're more efficiently making these new breakthroughs.  
[00:41:32] What confidence can one get that Microsoft will have a team that's world-class that  
[00:41:37] can make these breakthroughs? Once you decide to turn on  
[00:41:40] the money faucet—you're being a bit capital efficient right now, which is smart it seems,  
[00:41:44] to not waste money doing duplicative work—but once you decide you need to, how can one say, "Oh yeah,  
[00:41:51] now you can shoot up to the top five model?" At the end of the day, we're going to build  
[00:41:56] a world-class team and we already have a world-class team that's beginning to be assembled.  
[00:42:01] We have Mustafa coming in, we have Karen. We have Amar Subramanya who did a lot of the  
[00:42:05] post-training at Gemini 2.5 who's at Microsoft. Nando, who did a lot of the multimedia  
[00:42:11] work at DeepMind, is there. We're going to build a world-class team.  
[00:42:15] In fact, later this week even, Mustafa will publish something with a little  
[00:42:19] more clarity on what our lab is going to go do. The thing that I want the world to know, perhaps,  
[00:42:27] is that we are going to build the infrastructure that will support multiple models.  
[00:42:34] Because from a hyperscale perspective, we want to build the most scaled infrastructure fleet  
[00:42:40] that's capable of supporting all the models the world needs, whether it's from open source or  
[00:42:45] obviously from OpenAI and others. That's one job. Secondly, in our own model capability,  
[00:42:51] we will absolutely use the OpenAI model in our products and we'll start building our own model.  
[00:42:56] And we may—like in GitHub Copilot where Anthropic is used—even have other frontier models that are  
[00:43:02] going to be wrapped into our products, as well. I think that’s how each time… At the end of the  
[00:43:08] day, the eval of the product as it meets a particular task or a job is what matters.  
[00:43:13] We'll start back from there into the vertical integration needed, knowing that as long as  
[00:43:19] you're serving the market well with the product, you can always cost-optimize.  
[00:43:25] There's a question going forward. Right now, we have models that have  
[00:43:29] this distinction between training and inference. One could argue that there's a smaller and smaller  
[00:43:35] difference between the different models. Going forward, if you're really  
[00:43:38] expecting something like human-level intelligence, humans learn on the job.  
[00:43:42] If you think about your last 30 years, what makes Satya tokens so valuable?  
[00:43:45] It's the last 30 years of wisdom and experience you've gained in Microsoft.  
[00:43:49] We will eventually have models, if they get to human level, which will have  
[00:43:52] this ability to continuously learn on the job. That will drive so much value to the model company  
[00:43:57] that is ahead, at least in my view, because you have copies of one model broadly deployed through  
[00:44:02] the economy learning how to do every single job. And unlike humans, they can amalgamate  
[00:44:06] their learnings to that model. So there's this sort of continuous  
[00:44:10] learning exponential feedback loop, which almost looks like a sort of intelligence explosion.  
[00:44:16] If that happens and Microsoft isn't the leading model company by that time…  
[00:44:25] You're saying that well, we substitute one model for another, et cetera. Doesn’t that then matter  
[00:44:27] less? Because it's like this one model knows how to do every single job in  
[00:44:30] the economy, the others in the long tail don't. Your point, if there's one model that is the only  
[00:44:36] model that's most broadly deployed in the world and it sees all the data and it does continuous  
[00:44:41] learning, that's game set match and you stop shop. The reality that at least I see is that in the  
[00:44:51] world today, for all the dominance of any one model, that is not the case.  
[00:45:00] Take coding, there are multiple models. In fact, everyday it's less the case.  
[00:45:06] There is not one model that is getting deployed broadly.  
[00:45:09] There are multiple models that are getting deployed. It's like databases. It's always  
[00:45:13] the thing, "Can one database be the one that is just used everywhere?" Except it's not.  
[00:45:18] There are multiple types of databases that are getting deployed for different use cases.  
[00:45:23] I think that there are going to be some network effects of continual learning—I  
[00:45:29] call it data liquidity—that any one model has. Is it going to happen in all domains? I don't  
[00:45:35] think so. Is it going to happen in all geos? I don't think so. Is it going to happen in all  
[00:45:39] segments? I don't think so. It'll happen in all categories at the same time? I don't think so.  
[00:45:43] So therefore I feel like the design space is so large that there's plenty of opportunity.  
[00:45:49] But your fundamental point is having a capability which is at the infrastructure layer, model layer,  
[00:45:55] and at the scaffolding layer, and then being able to compose these things not  
[00:46:00] just as a vertical stack, but to be able to compose each thing for what its purpose is.  
[00:46:05] You can't build an infrastructure that's optimized for one model.  
[00:46:08] If you do that, what if you fall behind? In fact, all the infrastructure  
[00:46:12] you built will be a waste. You kind of need to build an  
[00:46:16] infrastructure that's capable of supporting multiple families and lineages of models.  
[00:46:21] Otherwise the capital you put in, which is optimized for one model architecture, means  
[00:46:26] you're one tweak away, some MoE-like breakthrough that happens, and your entire network topology  
[00:46:32] goes out of the window. That's a scary thing. Therefore you kind of want the infrastructure  
[00:46:37] to support whatever may come in your own model family and other model families. You've got to  
[00:46:42] be open. If you're serious about the hyperscale business, you've got to be serious about that.  
[00:46:47] If you're serious about being a model company, you have to basically say,  
[00:46:52] "What are the ways people can do things on top of the model so that I can have an ISV ecosystem?"  
[00:46:58] Unless I'm thinking I'll own every category, that just can't be that.  
[00:47:01] Then you won't have an API business and that, by definition, will mean you'll never be a platform  
[00:47:06] company that's successfully deployed everywhere. Therefore the industry structure is such that  
[00:47:13] it will really force people to specialize. In that specialization, a company like Microsoft  
[00:47:23] should compete in each layer by its merits, but not think that this is all about the road to game  
[00:47:31] set match, where I just compose vertically all these layers. That just doesn't happen.  
[00:48:42] So last year Microsoft was on path to be the largest infrastructure provider by far.  
[00:48:47] You were the earliest in 2023, so you went out there, you acquired all the resources  
[00:48:50] in terms of leasing data centers, starting construction, securing power, everything.  
[00:48:54] You guys were on pace to beat Amazon in 2026 or 2027.  
[00:48:59] Certainly by 2028 you were going to beat them. Since then, let’s call it, in the second half  
[00:49:04] of last year, Microsoft did this big pause, where they let go of a bunch of leasing sites that they  
[00:49:10] were going to take, which then Google, Meta, Amazon in some cases, Oracle, took these sites.  
[00:49:17] We're sitting in one of the largest data centers in the world, so obviously it's not everything,  
[00:49:20] you guys are expanding like crazy. But there are sites that you just stopped  
[00:49:23] working on. Why did you do this? This goes back a little bit to,  
[00:49:31] what is the hyperscale business all about? One of the key decisions we made was that  
[00:49:38] if we're going to build out Azure to be fantastic for all stages of AI—from  
[00:49:47] training to mid-training to data gen to inference—we just need fungibility of the fleet.  
[00:49:57] So that entire thing caused us basically not to go build a whole lot of capacity  
[00:50:03] with a particular set of generations. Because the other thing you have to  
[00:50:08] realize is that having up to now 10x'ed every 18 months enough training capacity  
[00:50:14] for the various OpenAI models, we realized that the key is to stay on that path.  
[00:50:22] But the more important thing is to have a balance, to not just train, but to be able to serve these  
[00:50:28] models all around the world. Because at the end of the day,  
[00:50:31] the rate of monetization is what will then allow us to keep funding.  
[00:50:35] And then the infrastructure was going to need us to support multiple models.  
[00:50:41] So once we said that that's the case, we just course-corrected to the path we're on.  
[00:50:47] If I look at the path we're on, we are doing a lot more starts now.  
[00:50:52] We are also buying up as much managed capacity as we can, whether it's to build,  
[00:50:56] whether it's to lease, or even GPUs as a service. But we're building it for where we see the demand  
[00:51:02] and the serving needs and our training needs. We didn't want to just be a hoster for one company  
[00:51:10] and have just a massive book of business with one customer.  
[00:51:14] That's not a business, you should be vertically integrated with that company.  
[00:51:20] Given that OpenAI was going to be a successful independent company,  
[00:51:25] which is fantastic. It makes sense. And even Meta may use third-party capacity, but ultimately  
[00:51:31] they're all going to be first-party. For anyone who has large scale,  
[00:51:36] they'll be a hyperscaler on their own. To me, it was to build out a hyperscale  
[00:51:42] fleet and our own research compute. That's what the adjustment was. So I feel very, very good.  
[00:51:49] By the way, the other thing is that I didn't want to get stuck with massive scale of one generation.  
[00:51:56] We just saw the GB200s, the GB300s are coming. By the time I get to Vera Rubin, Vera Rubin Ultra,  
[00:52:04] the data center is going to look very different because the power per rack, power per row,  
[00:52:09] is going to be so different. The cooling requirements are  
[00:52:12] going to be so different. That means I don't want to  
[00:52:15] just go build out a whole number of gigawatts that are only for a one-generation, one family.  
[00:52:22] So I think the pacing matters, the fungibility and the location matters,  
[00:52:28] the workload diversity matters, customer diversity matters and that's what we’re building towards.  
[00:52:33] The other thing that we've learned a lot is that every AI workload does  
[00:52:38] require not only the AI accelerator, but it requires a whole lot of other things.  
[00:52:42] In fact, a lot of the margin structure for us will be in those other things.  
[00:52:46] Therefore, we want to build out Azure as being fantastic for the long tail of the workloads,  
[00:52:53] because that's the hyperscale business, while knowing that we've got to be super competitive  
[00:52:58] starting with the bare-metal for the highest end training.  
[00:53:02] But that can't crowd out the rest of the business, because we're not in the business  
[00:53:07] of just doing five contracts with five customers being their bare-metal service. That's not a  
[00:53:13] Microsoft business. That may be a business for someone else, and that's a good thing.  
[00:53:17] What we have said is that we're in the hyperscale business, which is at the end  
[00:53:20] of the day a long tail business for AI workloads. And in order to do that, we will have some leading  
[00:53:28] bare-metal-as-a-service capabilities for a set of models, including our own.  
[00:53:33] And that, I think, is the balance you see. Another question that comes around  
[00:53:37] this whole fungibility topic. Okay, it's not where you want it, you would  
[00:53:42] rather have it in a good population center, like Atlanta. We're here. There's also the question of,  
[00:53:48] how much does that matter as the horizon of AI tasks grows? 30 seconds for a reasoning prompt,  
[00:53:56] or 30 minutes for a deep research, or it's going to be hours for software agents at some point  
[00:54:02] and days and so on and so forth, the time to human interaction.  
[00:54:05] Why does it matter if it's location A, B, or C? It’s a great question. That's exactly it. In fact,  
[00:54:11] that's one of the other reasons why we want to think about what an Azure region looks like and  
[00:54:15] what is the networking between Azure regions. This is where I think as the model capabilities  
[00:54:20] evolve and the usage of these tokens evolves, whether it's synchronously or asynchronously,  
[00:54:27] you don't want to be out of position. Then on top of that, by the way,  
[00:54:32] what are the data residency laws? There’s the entire EU thing, where  
[00:54:37] we literally had to create an EU Data Boundary. That basically meant that you can't just roundtrip  
[00:54:43] a call to wherever, even if it's asynchronous. Therefore you need to have maybe regional  
[00:54:48] things that are high density, and then the power costs and so on.  
[00:54:51] But you're 100% right in bringing up that the topology as we build out will have to evolve.  
[00:55:00] One, for tokens per dollar per watt. What are the economics? Overlay that with,  
[00:55:07] what is the usage pattern? Usage pattern in terms  
[00:55:10] of synchronous, asynchronous. But also what is the compute storage?  
[00:55:14] Because the latencies may matter for certain things. The storage better be there. If I have  
[00:55:18] a Cosmos DB close to this for session data or even for an autonomous thing, then that also has to be  
[00:55:24] somewhere close to it, and so on. All of those considerations are  
[00:55:28] what will shape the hyperscale business. Prior to the pause, what we had forecasted for  
[00:55:36] you, by 2028 you were going to be 12–13 gigawatts. Now we're at nine and a half or so.  
[00:55:42] But something that's even more relevant—and I just want you to more concretely state that  
[00:55:48] this is the business you don't want to be in—is that Oracle's going from 1/5th your  
[00:55:52] size to bigger than you by the end of 2027. While it's not a Microsoft-level quality of  
[00:55:59] return on invested capital, they're still making 35% gross margins.  
[00:56:03] So the question is, maybe it's not Microsoft's business to do this, but you've created a  
[00:56:11] hyperscaler now by refusing this business, by giving away the right of first refusal, et cetera.  
[00:56:16] First of all, I don't want to take away anything from the success Oracle has had in  
[00:56:22] building their business and I wish them well. The thing that I think I've answered for you  
[00:56:26] is that it didn't make sense for us to go be a hoster for one model company  
[00:56:34] with limited time horizon RPO. Let's just put it that way.  
[00:56:39] The thing that you have to think through is not what you do in the next five years,  
[00:56:42] but what you do for the next 50. We made our set of decisions.  
[00:56:49] I feel very good about our OpenAI partnership and what we're doing.  
[00:56:53] We have a decent book of business. We wish them a lot of success.  
[00:56:57] In fact, we are buyers of Oracle capacity. We wish them success. But at this point,  
[00:57:02] I think the industrial logic for what we are trying to do is pretty clear, which is that it's  
[00:57:07] not about chasing… First of all, I track, by the way, your things whether it's AWS or Google  
[00:57:13] and ours, which I think is super useful. But it doesn't mean I have to chase those.  
[00:57:20] I have to chase them for not just the gross margin that they may represent in a period of time.  
[00:57:27] What is this book of business that Microsoft uniquely can go clear, which  
[00:57:32] makes sense for us to clear? That's what we'll do. I have a question even stepping back from this,  
[00:57:37] I take your point that it's a better business to be in, all else equal, to have a long tail  
[00:57:43] of customers you can have higher margin from rather than serving bare metal to a few labs.  
[00:57:49] But then there's a question of, which way is the industry evolving?  
[00:57:51] If we believe we're on the path to smarter and smarter AIs, then why isn't the shape of  
[00:57:57] the industry that the OpenAIs and Anthropics and DeepMinds are the platform on which the long tail  
[00:58:04] of enterprises are actually doing business? They need bare metal, but they are the platform.  
[00:58:09] What is the long tail that is directly using Azure?  
[00:58:14] Because you want to use the general cognitive core.  
[00:58:17] But those models are all going to be available on Azure, so any workload that says, "Hey,  
[00:58:20] I want to use some open source model and an OpenAI model," if you go to Azure Foundry today,  
[00:58:27] you have all these models that you can provision, buy PTUs, get a Cosmos DB,  
[00:58:32] get a SQL DB, get some storage, get some compute. That's what a real workload looks like.  
[00:58:36] A real workload is not just an API call to a model.  
[00:58:40] A real workload needs all of these things to go build an app or instantiate an application.  
[00:58:47] In fact, the model companies need that to build anything.  
[00:58:50] It's not just like, "I have a token factory." I have to have all of these things. That's  
[00:58:54] the hyperscale business. And it's not on any one model, but all of these models.  
[00:59:00] So if you want Grok plus, say, OpenAI plus an open source model, come to Azure Foundry,  
[00:59:06] provision them, build your application. Here is a database. That's kind of what the business is.  
[00:59:13] There is a separate business called just selling raw bare-metal services to model companies.  
[00:59:17] And that's the argument about how much of that business you  
[00:59:20] want to be in and not be in and what that is. It's a very different segment of the business,  
[00:59:25] which we are in, and we also have limits to how much of it is going to crowd out the rest of it.  
[00:59:31] But that's kind of at least the way I look at it.  
[00:59:34] There are sort of two questions here. One is, why couldn't you just do both?  
[00:59:38] The other one is, given our estimates on what your capacity is in 2028,  
[00:59:44] it's three and a half gigawatts lower. Sure, you could have dedicated that to  
[00:59:48] OpenAI training and inference capacity, but you could have also dedicated that  
[00:59:52] to actually just running Azure, running Microsoft 365, running GitHub Copilot.  
[01:00:00] I could have just built it and not given it to OpenAI.  
[01:00:02] Or I may want to build it in a different location. I may want to build it in the UAE,  
[01:00:06] I may want to build it in India, I may want to build it in Europe.  
[01:00:09] One of the things is, as I said, where we have real capacity constraints right now, given  
[01:00:14] the regulatory needs and the data sovereignty needs, we've got to build all over the world.  
[01:00:18] First of all, stateside capacity is super important, and we want to build everything.  
[01:00:21] But when I look out to 2030, I have a global view of what is Microsoft's shape  
[01:00:28] of business by first-party and third-party. Third-party segmented by the frontier labs  
[01:00:33] and how much they want versus the inference capacity we want to build for multiple models,  
[01:00:40] and our own research compute needs. That's all going into my calculus.  
[01:00:48] You're rightfully pointing out the pause, but the pause was not done because we said,  
[01:00:53] "Oh my God, we don't want to build that." We realized that we want to build what we want  
[01:00:59] to build slightly differently by both workload type as well as geo-type and timing as well.  
[01:01:07] We'll keep ramping up our gigawatts, and the question is at what pace and in what location.  
[01:01:13] And how do I ride Moore's law on it, which is, do I really want to overbuild three and a half  
[01:01:19] in 2027 or do I want to spread that in 2027-28 knowing even… One of the biggest learnings we had  
[01:01:25] even with Nvidia is that their pace increased in terms of their migrations. That was a big  
[01:01:32] factor. I didn't want to go get stuck for four or five years of depreciation on one generation.  
[01:01:41] In fact, Jensen's advice to me was two things. One is, get on the speed-of-light execution.  
[01:01:45] That's why the execution in this Atlanta data center....  
[01:01:48] I mean, it's like 90 days between when we get it and to hand off to a real workload.  
[01:01:53] That's real speed-of-light execution on that front.  
[01:01:57] I wanted to get good on that. And then that way I'm building  
[01:02:01] each generation in scaling. And then every five years,  
[01:02:05] you have something much more balanced. So it becomes literally like a flow  
[01:02:11] for a large-scale industrial operation like this where you're suddenly not lopsided,  
[01:02:15] where you've built up a lot in one time and then you take a massive hiatus because you're stuck  
[01:02:20] with all this, to your point, in one location which may be great for training, or it may not  
[01:02:24] be great for inference because I can't serve, even if it's all asynchronous, because Europe  
[01:02:28] won't let me round-trip to Texas. So that's all of the things.  
[01:02:32] How do I rationalize this statement with what you've done over the last few weeks?  
[01:02:36] You've announced deals with Iris Energy, with Nebius, and Lambda Labs,  
[01:02:41] and there's a few more coming as well. You're going out there and securing capacity  
[01:02:46] that you're renting from the neoclouds rather than having built it yourself.  
[01:02:52] It's fine for us because now when you have line of sight to demand, which can be served where  
[01:02:58] people are building, it's great. In fact we will take leases,  
[01:03:04] we will take build-to-suit, we'll even take GPUs-as-a-service where we don't have capacity  
[01:03:09] but we need capacity and someone else has that. And by the way, I would even sort of welcome every  
[01:03:14] neocloud to just be part of our marketplace. Because guess what? If they go bring their  
[01:03:20] capacity into our marketplace, that customer who comes through Azure will use the neocloud, which  
[01:03:25] is a great win for them, and will use compute, storage, databases, all the rest from Azure.  
[01:03:31] So I'm not at all thinking of this as, "Hey, I should just go gobble up all of that myself."  
[01:03:38] You mentioned how this depreciating asset, in five or six years, is 75% of the TCO of a data center.  
[01:03:49] And Jensen is taking a 75% margin on that. So what all the hyperscalers are trying to  
[01:03:55] do is develop their own accelerator so that they can reduce this overwhelming cost for  
[01:04:02] equipment, to increase their margins. And when you look at where they are,  
[01:04:06] Google's way ahead of everyone else. They've been doing it for the longest.  
[01:04:09] They're going to make something like five to seven million chips of their own TPUs.  
[01:04:13] You look at Amazon and they're trying to make three to five million [Lifetime shipment units].  
[01:04:16] But when we look at what Microsoft is ordering of their own chips, it's way below that number.  
[01:04:22] You've had a program for just as long. What's going on with your internal chips?  
[01:04:26] It’s a good question. A couple of things. One is that the thing that is the biggest  
[01:04:31] competitor for any new accelerator is kind of even the previous generation of Nvidia.  
[01:04:36] In a fleet, what I'm going to look at is the overall TCO.  
[01:04:39] The bar I have, even for our own… By the way, I was just looking at the data for  
[01:04:44] Maia 200 which looks great, except that one of the things that we learned even on the  
[01:04:50] compute side… We had a lot of Intel, then we introduced AMD, and then we introduced  
[01:04:55] Cobalt. That's how we scaled it. We have good existence proof of, at least in core compute,  
[01:05:02] how to build your own silicon and then manage a fleet where all three are at play in some balance.  
[01:05:08] Because by the way, even Google's buying Nvidia, and so is Amazon.  
[01:05:11] It makes sense because Nvidia is innovating and it's the general-purpose thing.  
[01:05:16] All models run on it and customer demand is there. Because if you build your own vertical thing,  
[01:05:22] you better have your own model, which is either going to use it for training or inference,  
[01:05:27] and you have to generate your own demand for it or subsidize the demand for it.  
[01:05:30] So therefore you want to make sure you scale it appropriately.  
[01:05:35] The way we are going to do it is to have a close loop between our own MAI models and our silicon,  
[01:05:43] because I feel like that's what gives you the birthright to do your own silicon,  
[01:05:49] where you literally have designed the microarchitecture with what you're doing,  
[01:05:55] and then you keep pace with your own models. In our case, the good news here is that OpenAI  
[01:06:02] has a program which we have access to. So therefore to think that Microsoft  
[01:06:07] is not going to have something that's— What level of access do you have to that?  
[01:06:10] All of it. You just get the IP for all of that?  
[01:06:12] So the only IP you don't have is consumer hardware?  
[01:06:14] That's it. Oh, okay. Interesting.  
[01:06:20] By the way, we gave them a bunch of IP as well to bootstrap them.  
[01:06:25] This is one of the reasons why they… Because we built all these supercomputers together.  
[01:06:30] We built it for them and they benefited from it, rightfully so.  
[01:06:35] And now as they innovate, even at the system level, we get access to all of it.  
[01:06:40] And we first want to instantiate what they build, for them, but then we'll extend it.  
[01:06:50] So if anything, the way I think about your question is, Microsoft wants to be a fantastic,  
[01:06:56] I'll call it, speed-of-light execution partner for Nvidia.  
[01:07:00] Because quite frankly that fleet is life itself. Obviously Jensen's doing super well with his  
[01:07:08] margins, but the TCO has many dimensions to it and I want to be great at that TCO.  
[01:07:13] On top of that, I want to be able to really work with the OpenAI lineage  
[01:07:19] and the MAI lineage and the system design, knowing that we have the IP rights on both ends.  
[01:07:26] Speaking of rights, you had an interview a couple days ago where you said that in the  
[01:07:35] new agreement you made with OpenAI you have rights, the exclusivity, to the stateless  
[01:07:40] API calls that OpenAI makes. We were sort of confused about  
[01:07:45] if there's any state whatsoever. You were just mentioning a second  
[01:07:47] ago that all these complicated workloads that are coming up are going to require memory and  
[01:07:51] databases and storage and so forth. Is that now not stateless if  
[01:07:56] ChatGPT is storing stuff on sessions? That's the reason why. The strategic decision we  
[01:08:01] made, and also accommodating for the flexibility OpenAI needed in order to be able to procure  
[01:08:07] compute for… Essentially think of OpenAI having a PaaS business and a SaaS business. The SaaS  
[01:08:14] business is ChatGPT. Their PaaS business is their API. That API is Azure-exclusive. The  
[01:08:23] SaaS business, they can run it anywhere. And they can partner with anyone they  
[01:08:26] want to to build SaaS products? If they want a partner and that  
[01:08:30] partner wants to use a stateless API, then Azure is the place where they can get the stateless API.  
[01:08:36] It seems like there's a way for them to build the product together and it's a stateful thing…  
[01:08:42] No, for even that they'll have to come to Azure. Again, this is done in the spirit of "what is it  
[01:08:51] that we value as part of our partnership." And we made sure that, at the same time,  
[01:08:56] we were good partners to OpenAI given all the flexibility they needed.  
[01:08:59] So for example, Salesforce wants to integrate OpenAI. It's not through an API. They actually  
[01:09:03] work together, train a model together and deploy it on, let's say, Amazon now.  
[01:09:07] Is that allowed or do they have to use your… For any custom agreement like that, they will have  
[01:09:13] to come run it… There are some few exceptions, the US government and so on, that we made,  
[01:09:17] but other than that, they'd have to come to Azure. Stepping back, when we were walking back and forth  
[01:10:33] through the factory, one of the things you were talking about is that Microsoft,  
[01:10:38] you can think of it as a software business, but now it's really becoming an industrial business.  
[01:10:42] There's all this capex, there's all this construction.  
[01:10:45] If you just look over the last two years, your capex has sort of tripled.  
[01:10:50] Maybe you extrapolate that forward, it actually just becomes this huge industrial explosion.  
[01:10:56] Other hyperscalers are taking loans. Meta has done a $20 billion loan at Louisiana.  
[01:11:01] They've done a corporate loan. It seems clear everyone's free cash flow is going to zero,  
[01:11:06] which I'm sure Amy is going to beat you up if you even try to do that, but what's happening?  
[01:11:12] I think the structural change is what you're referencing, which is massive.  
[01:11:21] I describe it as we are now a capital-intensive business and a knowledge-intensive business.  
[01:11:27] In fact, we have to use our knowledge to increase the ROIC on the capital spend.  
[01:11:33] The hardware guys have done a great job of marketing Moore's Law,  
[01:11:37] which I think is unbelievable and it's great.  
[01:11:39] But if you even look at some of the stats I even did in my earnings call, for a given GPT family,  
[01:11:46] the software improvements of really throughput in terms of tokens-per-dollar-per-watt that we're  
[01:11:52] able to get quarter-over-quarter, year-over-year, it’s massive.  
[01:11:58] It's 5x, 10x, maybe 40x in some of these cases, just because of how you can optimize.  
[01:12:04] That's knowledge intensity coming to bring out capital efficiency.  
[01:12:11] That, at some level, is what we have to master. Some people ask me, what is the difference between  
[01:12:19] a classic old-time hoster and a hyperscaler? Software. Yes, it is capital intensive,  
[01:12:26] but as long as you have systems know-how, software capability to optimize by workload, by fleet...  
[01:12:34] That's why when we say fungibility, there's so much software in it.  
[01:12:38] It's not just about the fleet. It's the ability to evict a  
[01:12:41] workload and then schedule another workload. Can I manage that algorithm of scheduling around?  
[01:12:51] That is the type of stuff that we have to be world-class at.  
[01:12:54] So yes, I think we'll still remain a software company, but yes, this is a different business  
[01:12:59] and we're going to manage. At the end of the day,  
[01:13:02] the cash flow that Microsoft has allows us to have both these arms firing well.  
[01:13:12] It seems like in the short term you have more credence  
[01:13:15] on things taking a while, being more jagged. But maybe in the long term you think the people  
[01:13:20] who talk about AGI and ASI are correct. Sam will be right, eventually. I have a broader  
[01:13:27] question about what makes sense for a hyperscaler to do, given that you have to invest massively in  
[01:13:33] this thing which depreciates over five years. So if you have 2040 timelines to the kind of  
[01:13:39] thing that somebody like Sam anticipates in three years, what is a reasonable  
[01:13:44] thing for you to do in that world? There needs to be an allocation to,  
[01:13:49] I'll call it, research compute. That needs to be done like you did R&D.  
[01:13:57] That's the best way to even account for it, quite frankly.  
[01:13:59] We should think of it as just R&D expense and you should say, "What's the research compute  
[01:14:03] and how do you want to scale it?" Let's even say it's an order of  
[01:14:09] magnitude scale in some period. Pick your thing, is it two years?  
[01:14:14] Is it 16 months? What have you. That's sort of one piece, which is table stakes, that's R&D expenses.  
[01:14:22] The rest is all demand driven. Ultimately, you're allowed to build  
[01:14:26] ahead of demand, but you better have a demand plan that doesn't go completely off kilter.  
[01:14:33] Do you buy… These labs are now projecting revenues of $100 billion in 2027–28  
[01:14:39] and they're projecting revenue to keep growing at this rate of 3x, 2x a year…  
[01:14:44] In the marketplace there's all kinds of incentives right now, and rightfully so.  
[01:14:50] What do you expect an independent lab that is sort of trying to raise money to do?  
[01:14:54] They have to put some numbers out there such that they can actually go raise  
[01:14:59] money so that they can pay their bills for compute and what have you. And it's  
[01:15:02] a good thing. Someone's going to take some risk and put it in there, and they've shown traction.  
[01:15:08] It's not like it's all risk without seeing the fact that they've been performing,  
[01:15:13] whether it's OpenAI, or whether it's Anthropic. So I feel great about what they've done,  
[01:15:17] and we have a massive book of business with these chaps. So therefore that's all good. But overall  
[01:15:24] ultimately, there's two simple things. One is you have to allocate for R&D.  
[01:15:28] You brought up talent. The talent for AI is at a premium. You have to spend  
[01:15:33] there. You've got to spend on compute. So in some sense researcher-to-GPU  
[01:15:38] ratios have to be high. That is sort of what it takes  
[01:15:42] to be a leading R&D company in this world. And that's something that needs to scale,  
[01:15:48] and you have to have a balance sheet that allows you to scale that long before it's conventional  
[01:15:53] wisdom and so on. That's kind of one thing. But the other is all about knowing how to forecast.  
[01:16:01] As we look across the world, America has dominated many tech stacks.  
[01:16:06] The US owns Windows through Microsoft, which is deployed even in China,  
[01:16:11] that's the main operating system. Of course, there's Linux,  
[01:16:13] which is open source, but Windows is deployed everywhere in China on personal computers.  
[01:16:19] You look at Word, it's deployed everywhere. You look at all these various technologies,  
[01:16:22] it's deployed everywhere. And Microsoft and other  
[01:16:27] companies have grown elsewhere. They're building data centers  
[01:16:29] in Europe and in India and in all these other places, in Southeast Asia and LatAm and Africa.  
[01:16:35] In all of these different places, you're building capacity. But this seems quite different. Today,  
[01:16:41] the political aspect of technology, of compute… The US administration  
[01:16:48] didn't care about the dot-com bubble. It seems like the US administration,  
[01:16:52] as well as every other administration around the world, cares a lot about AI.  
[01:16:57] The question is, we're sort of in a bipolar world, at least with the US and China, but Europe and  
[01:17:03] India and all these other countries are saying, "No, we're going to have sovereign AI as well."  
[01:17:07] How does Microsoft navigate the difference to the 90s—where there's one country in the world that  
[01:17:12] matters, it's America, and our companies sell everywhere and therefore Microsoft  
[01:17:16] benefits massively—to a world where it is bipolar? Where Microsoft can't just necessarily have the  
[01:17:22] right to win all of Europe or India or Singapore. There are actually sovereign AI efforts.  
[01:17:28] What is your thought process here and how do you think about this?  
[01:17:30] It's a super critical piece. I think that the key, key priority for the US tech sector  
[01:17:41] and the US government is to ensure that we not only do leading innovative work,  
[01:17:48] but that we also collectively build trust around the world on our tech stack.  
[01:17:55] Because I always say the United States is just an unbelievable place. It's just unique in  
[01:18:01] history. It's 4% of the world's population, 25% of the GDP, and 50% of the market cap.  
[01:18:07] I think you should think about those ratios and reflect on it.  
[01:18:12] That 50% happens because quite frankly the trust the world has in the United States,  
[01:18:18] whether it's its capital markets or whether it's its technology and  
[01:18:22] its stewardship of what matters at any given time in terms of leading sector.  
[01:18:30] If that is broken, then that's not a good day for the United States.  
[01:18:34] We start with that, which I think President Trump gets, the White House, David Sacks,  
[01:18:40] everyone really, I think, gets it. So therefore I applaud anything  
[01:18:47] that the United States government and the tech sector jointly does to, for example,  
[01:18:54] put our own capital at risk, collectively as an industry, in every part of the world.  
[01:18:59] I would like the USG to take credit for foreign direct investment by  
[01:19:05] American companies all over the world. It's the least talked about, but the best  
[01:19:10] marketing that the United States should be doing is that it's not just about all the foreign direct  
[01:19:15] investment coming into the United States, but the most leading sector, which is these AI factories,  
[01:19:21] are all being created all over the world. By whom? By America and American companies. And  
[01:19:27] so you start there, and then you even build other agreements around it, which are around  
[01:19:33] their continuity, their legitimate sovereignty concerns, around whether it's data residency,  
[01:19:42] for them to have real agency and guarantees on privacy, and so on.  
[01:19:49] In fact, our European commitments are worth reading.  
[01:19:52] We made a series of commitments to Europe on how we will govern our hyperscale investment there  
[01:20:01] such that the European Union and the European countries have sovereignty.  
[01:20:06] We're also building sovereign clouds in France and in Germany.  
[01:20:10] We have something called Sovereign Services on Azure, which literally gives people key management  
[01:20:17] services along with confidential computing, including confidential computing in GPUs, which  
[01:20:22] we've done great innovative work with Nvidia. So I feel very, very good about being able to  
[01:20:29] build, both technically and through policy, this trust in the American tech stack.  
[01:20:36] How do you see this shaking out as you have this network effect with continual learning  
[01:20:41] and things on the model level? Maybe you have equivalent  
[01:20:44] things at the hyperscaler level as well. Do you expect that the countries will say,  
[01:20:49] "Look, it's clear one model or a couple models are the best, and so we're going to use them,  
[01:20:53] but we're going to have some laws around the weights having to be hosted in our country"?  
[01:20:56] Or do you expect that there will be this push so that it has to be a model trained in our country?  
[01:21:03] Maybe an analogy here is that semiconductors are very important to the economy,  
[01:21:06] and people would like to have their sovereign semiconductors, but TSMC is just better.  
[01:21:11] And semiconductors are so important to the economy that you will just go to  
[01:21:15] Taiwan and buy the semiconductors. You have to. Will it be like that with AI?  
[01:21:20] Ultimately, what matters is the use of AI in their economy to create economic value.  
[01:21:28] That's the diffusion theory, which ultimately, it's not the leading sector,  
[01:21:33] but it's the ability to use the leading technology to create your own comparative advantage.  
[01:21:38] So I think that will fundamentally be the core driver.  
[01:21:42] But that said, they will want continuity of that. So in some sense, that's one of the reasons why,  
[01:21:47] I believe, there's always going to be a check to "Hey, can this one model have all  
[01:21:55] the runaway deployment?" That's why open source  
[01:21:57] is always going to be there. There will be, by definition, multiple  
[01:22:02] models. That'll be one way. That's one way for people to sort of demand continuity and not have  
[01:22:09] concentration risk, that’s another way to say it. And so you say, "Hey, I want multiple models,  
[01:22:14] and then I want an open source." I feel that as long as that's there,  
[01:22:18] every country will feel like, "Okay, I don't have to worry about deploying the best model  
[01:22:23] and broadly diffusing because I can always take what is my data and my liquidity and move it  
[01:22:30] to another model, whether it's open source or from another country or what have you."  
[01:22:35] Concentration risk and sovereignty, which is really agency, those are the two things that  
[01:22:42] will drive the market structure. The thing about this is that  
[01:22:45] this doesn't exist for semiconductors. All refrigerators, cars have chips made in Taiwan.  
[01:22:50] It didn't exist until now. Even then, if Taiwan is cut off,  
[01:22:57] there are no more cars or no more refrigerators. TSMC Arizona is not replacing any  
[01:23:02] real fraction of the production. The sovereignty is a bit of a scam, if you will.  
[01:23:08] It's worthwhile having it, it's important to have it, but it's not  
[01:23:12] real sovereignty. We're a global economy. I think it’s kind of like saying, "Hey,  
[01:23:17] at this point, we've not learned anything about what resilience means and what one needs to do."  
[01:23:28] Any nation state, including the United States, at this point will do what it  
[01:23:33] takes to be more self-sufficient on some of these critical supply chains.  
[01:23:39] So I, as a multinational company, have to think about that as a first-class requirement.  
[01:23:46] If I don't, then I'm not respecting what is in the policy interests of that country long-term.  
[01:23:55] I'm not saying they won't make practical decisions in the short term.  
[01:23:59] Absolutely, globalization can't just be rewound. All these capital investments cannot be made  
[01:24:06] in a way, at the pace at which… But at the same time, think about it, if somebody showed up in  
[01:24:12] Washington and said, "Hey, we're not going to build any semiconductor plants," they're going  
[01:24:17] to be kicked out of the United States. The same thing is going to be  
[01:24:21] true in every other country, too. So therefore we have to, as companies,  
[01:24:26] respect what the lessons learned are, whether it's that the pandemic woke us up or whatever.  
[01:24:34] But nevertheless people are saying, "Look, globalization was fantastic.  
[01:24:38] It helped supply chains be globalized and be super efficient.  
[01:24:42] But there's such a thing called resilience, and we want resilience."  
[01:24:47] So therefore that feature will get built. At what pace, I think,  
[01:24:51] is the point you are making. You can't snap your fingers  
[01:24:54] and say all the TSMC plants now are all in Arizona with all their capability. They're  
[01:24:59] not going to be. But is there a plan? There will be a plan. And should we respect that?  
[01:25:04] Absolutely. So I feel that that’s the world. I want to meet the world where it is and on what  
[01:25:11] it wants to do going forward, as opposed to saying, "Hey, we have a point of view  
[01:25:16] that doesn't respect your view." Just to make sure I understand,  
[01:25:19] the idea here is that each country will want some kind of data residency, privacy, et cetera.  
[01:25:26] And Microsoft is especially privileged here because you have relationships with these  
[01:25:30] countries, you have expertise in setting up these kinds of sovereign data centers.  
[01:25:36] Therefore Microsoft is uniquely fit for a world with more sovereignty requirements.  
[01:25:42] I don't want to sort of describe it as somehow we're uniquely privileged.  
[01:25:46] I would just say I think of that as a business requirement that we have been doing all the hard  
[01:25:51] work all these decades, and we plan to. So my answer to Dylan's previous question  
[01:25:56] was that I take—whether it's in the United States, or when the White House and the USG says,  
[01:26:06] "We want you to allocate more of your wafer starts to fabs in the US"—we take that seriously.  
[01:26:16] Or whether it is data centers and the EU boundary, we take that seriously.  
[01:26:20] So to me, respecting what are legitimate reasons why countries care about sovereignty,  
[01:26:28] building for it as a software and a physical plant, is what we'll do.  
[01:26:34] As we go to the bipolar world—US, China—it's not just you versus Amazon,  
[01:26:45] or you versus Anthropic, or you versus Google. There is a whole host of competition.  
[01:26:52] How does America rebuild the trust? What do you do to rebuild the trust?  
[01:26:56] To say, "Actually, no, American companies will be the main provider for you."  
[01:27:00] And how do you think about competition with up and coming Chinese companies, whether it  
[01:27:04] be ByteDance and Alibaba or Deepseek and Moonshot? To add to that question, one concern is how we're  
[01:27:10] talking about how AI is becoming this industrial capex race where you're rapidly having to build  
[01:27:15] quickly across all loads of supply chain. When you hear that, at least up until now,  
[01:27:19] you just think about China. This is their comparative advantage. And especially if we're not  
[01:27:25] going to moonshot to ASI next year, but it's going to be decades of buildouts and infrastructure,  
[01:27:33] how do you deal with Chinese competition? Are they privileged in that world?  
[01:27:37] It’s a great question. In fact, you just made the point of why trust in American  
[01:27:43] tech is probably the most important feature. It's not even the model capability, maybe.  
[01:27:51] It is, "can I trust you, the company, can I trust you, your country, and its  
[01:27:58] institutions to be a long-term supplier?" That may be the thing that wins the world.  
[01:28:04] That's a good note to end on. Satya, thank you for doing this.  
[01:28:07] Thank you so much. Thank you. Thank you.  
[01:28:09] It's awesome. You two guys are quite the team.  
