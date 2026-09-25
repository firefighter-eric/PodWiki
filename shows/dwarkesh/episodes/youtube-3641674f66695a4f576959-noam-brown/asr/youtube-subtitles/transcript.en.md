# OpenAI researcher on agent swarms & recursive self-improvement

[00:00:00] Today, I’m chatting with Noam Brown, who is a researcher at OpenAI.  
[00:00:03] He was one of the foundational contributors to what became o1 and the reasoning models.  
[00:00:08] Now he’s working on multi-agent systems. Speaking of which, you guys announced last  
[00:00:12] week that you solved one of the Millennium Prize Problems with a  
[00:00:16] system of 10,000 different AI agents that spent 130 billion tokens over 88 hours.  
[00:00:22] One of the reasons I’m interested in talking to you is that you were among the first people,  
[00:00:26] maybe two or three years ago, who were thinking about how the reasoning models  
[00:00:32] would allow us to see into the future. Because if you scale up inference compute,  
[00:00:35] you can see what the base capabilities of the models will be a few years in the future.  
[00:00:38] I feel like you’re in a similar position now to help us understand what future capabilities  
[00:00:43] will look like, given the enormous scaling of agent sizes that we can do right now.  
[00:00:48] The way I think about it, when you plot the performance of these reasoning models with  
[00:00:53] test-time compute on the x-axis and performance on basically any reasoning benchmark on the y-axis,  
[00:01:00] you see a very clear pattern where the longer these models take to think about  
[00:01:03] their answer, the better they do. This is a very natural thing.  
[00:01:05] It’s the same thing with people. If you’re taking the SATs and you  
[00:01:08] have five minutes to go through the entire exam, you’re not going to do very well.  
[00:01:12] If you have five hours, you’re probably going to do a lot better.  
[00:01:15] The AI models are pretty similar. They’ll spend that time doing this  
[00:01:19] monologue to themselves, figuring things out, going through different cases,  
[00:01:22] ruling out different possibilities, building on some of their previous discoveries.  
[00:01:26] The problem is that as you push that further and further, you hit a latency bottleneck.  
[00:01:30] You don’t want to sit around for three years waiting for a response.  
[00:01:34] So what you can do is what a lot of people do. They parallelize. They just get a team of people.  
[00:01:39] If you’re going to found a company, you want to get a group  
[00:01:41] of people together so you can go faster. It’s the same thing with these AI models.  
[00:01:45] It helps to just have multiple agents working on something because they can go faster.  
[00:01:50] So multi-agent is a way of scaling test-time compute in parallel instead of purely serially.  
[00:01:54] It is less efficient, because it’s not like a single agent has all the context to itself.  
[00:02:03] But it is a very effective way of scaling test-time compute if it’s done well.  
[00:02:09] I’m going to ask a bunch of naive questions. This is an unreleased model, so we haven’t  
[00:02:13] publicly seen how these systems work. I just have a bunch of ways in which I’m  
[00:02:17] confused about what the qualitative properties of such systems are.  
[00:02:22] I am shocked by the scale of cognitive effort that you can  
[00:02:28] concentrate in such a short period of time. Think about what 130 billion tokens are.  
[00:02:34] If it were a single human thinking as a full-time job, stretched back to back, 130 billion tokens  
[00:02:40] would be a human thinking for 4,000 years. Eight hours a day, working a normal work week.  
[00:02:46] Starting from ancient Sumeria up till today, a single sequential human thinking that long,  
[00:02:53] concentrated in 88 hours. I feel like qualitatively,  
[00:02:56] that is a super important consideration. I’m surprised that there isn’t  
[00:02:59] a bigger parallelization penalty. You can just have 10,000 agents collaborate.  
[00:03:04] Maybe because the agents are better at collaborating than humans might be,  
[00:03:07] they’re going much faster. They can actually  
[00:03:09] productively collaborate at such a big scale. Or maybe there is a big parallelization penalty.  
[00:03:14] Let’s talk about the parallelization penalty, and then we can talk about the qualitative stuff.  
[00:03:16] The truth is that we don’t have very good science on multi-agent scaling up to this kind of scale.  
[00:03:22] When we released 5.6, I think that was the first time that we  
[00:03:25] had a proper multi-agent system in our models. We actually did show some plots in the blog post  
[00:03:32] of the scaling performance of multi-agent systems, because we have it as an option.  
[00:03:37] It’s Ultra Mode. The default is four agents, but you can set that higher.  
[00:03:41] In the plot, we show what the performance looks like on some benchmarks for one agent,  
[00:03:44] for four agents working together, for 16 agents working together.  
[00:03:48] It depends on the benchmark, but for some of the benchmarks, what you see is that if  
[00:03:52] you have four agents working on the problem, it is done twice as fast.  
[00:03:59] Because there are four agents working for half as long, you’re  
[00:04:01] paying 2x more to get an answer twice as quickly. If you go to 16 agents, you see a similar pattern.  
[00:04:07] It’s a little less efficient, but you continue to see that performance.  
[00:04:12] Is it a linear serial time speedup or a sublinear speedup as you increase the  
[00:04:17] number of parallel agents? It’s slightly sublinear,  
[00:04:21] though it does depend a lot on the problem. Math, for example, is quite parallelizable.  
[00:04:28] It’s not the most parallelizable thing, but it is very parallelizable.  
[00:04:31] Web search, things like doing a Deep Research report where you have to look through a bunch  
[00:04:35] of sources, is extremely parallelizable. I suspect that something like writing  
[00:04:39] a novel would be very unparallelizable. You would probably not see a big benefit  
[00:04:43] from having 10,000 agents working on a novel together, in the same way that you’d  
[00:04:48] probably not get a big benefit from having 10,000 people work on a novel together.  
[00:04:52] So the performance does depend on the domain. We do measure it up to 16 or so agents in  
[00:04:57] our published blog posts. The problem is that it’s  
[00:05:01] very hard to push that science to 10,000 agents because it’s just so expensive.  
[00:05:06] You guys just did it over a weekend. But that’s one data point.  
[00:05:10] We don’t know how long it would take a single agent to solve Navier-Stokes, because we haven’t  
[00:05:15] done that experiment yet. Maybe we will,  
[00:05:18] but that’s also only one data point. If we want to do a thorough ablation, the  
[00:05:23] experiments are just too expensive at that scale. So we have to do some kind of methodical science  
[00:05:29] about what happens when you go to 64, 128, 256 or something and get a sense of the behavior.  
[00:05:35] But it’s going to be very hard to push that all the way to 10,000 and know for  
[00:05:39] sure what the benefit was that we actually got from using 10,000 agents versus 1,000.  
[00:05:44] There’s one thing I want to make clear. The effort to solve a Millennium Prize Problem,  
[00:05:52] this was not due to multi-agent. I wouldn’t even attribute 10%  
[00:05:58] of the credit to multi-agent. The reality is that OpenAI has  
[00:06:04] trained a very powerful model. We can get that model to  
[00:06:08] operate over very long horizons. We can get it to think in parallel.  
[00:06:12] But at its core, the reason why we’re able to do this is because we just have a general-purpose,  
[00:06:17] very strong model. Things like multi-agent  
[00:06:22] are flashy and new, and that probably gets disproportionate credit for that reason.  
[00:06:31] But the core reason is this is just a very powerful model.  
[00:06:35] The generalization is quite shocking to me. I don’t know how these systems were trained,  
[00:06:41] but presumably they were trained how RL training happens.  
[00:06:44] You have a bunch of checkable synthetic problems and you do a bunch of RL against them.  
[00:06:48] Nowhere in the training process, I’m guessing, was the model solving anything  
[00:06:51] as ambitious as a Millennium Prize Problem. But the generalization was strong enough  
[00:06:55] that you could have these much easier verifiable problems generalize to this much parallel effort  
[00:07:02] on such a hard problem. I think that is true.  
[00:07:05] First of all, we do train the model on very hard problems.  
[00:07:09] There is definitely a gap. We see that if we train on  
[00:07:11] some kinds of tasks, it’s able to do tasks that are more ambitious than that.  
[00:07:15] There is an interesting challenge that as the models become smarter and smarter,  
[00:07:21] a lot of the kinds of questions we can ask them are just too easy.  
[00:07:28] It’s hard to challenge the model. I do think that’s going to be interesting.  
[00:07:32] If I had to make an argument for why you might not see AIs like LLMs go the same path as AlphaGo and  
[00:07:41] AlphaZero and all these kinds of game-playing AIs, it might be this kind of problem.  
[00:07:46] In things like AlphaZero, where you have self-play, you have an infinite curriculum.  
[00:07:50] You’re always playing against an AI that’s equally strong.  
[00:07:53] Whereas for things like training an LLM with reinforcement learning, at least the ways  
[00:07:59] that are out there right now, you give the model a problem and you ask it to solve it.  
[00:08:06] If the problem is so easy that it can just solve it in a second, it's not really learning anything.  
[00:08:13] If we run out of problems to challenge it, then that is a plausible scenario  
[00:08:17] where it becomes much harder to make progress. Now, I do think there are ways around that.  
[00:08:25] We haven’t really hit that as a wall yet. I think that if it ever became a serious problem,  
[00:08:31] there would be ways around it. But it is a plausible scenario.  
[00:08:36] Just for the audience, when you’re referring to AlphaGo or AlphaZero,  
[00:08:38] you’re talking about getting superhuman relatively fast after achieving human-level performance.  
[00:08:43] If you look at the trajectory of game-playing AIs, like Go, within a span of a year they went  
[00:08:49] from beating a European champion — something like number 50 in the world — to beating the  
[00:08:54] world champion, to being unimaginably, orders of magnitude stronger than any human alive.  
[00:09:00] It’s possible that in domains like math we see a similar trajectory, but I think there is a very  
[00:09:06] plausible scenario where that doesn’t happen. I want to understand, if in six months people  
[00:09:13] will have access to multi-agent systems, how should one model what it is like to  
[00:09:18] collaborate with or hire a multi-agent system? I should start by talking about how these  
[00:09:22] multi-agent systems actually work, which I think is a very different way than a lot  
[00:09:26] of multi-agent systems in other AIs. A lot of people that have approached  
[00:09:32] multi-agents for things like LLMs tend to take this very scaffolded approach.  
[00:09:37] For example, there might be a coordinator agent that delegates work to a bunch of  
[00:09:43] children and gives them a task. The children work on it and then  
[00:09:45] return their answer. This seems like a very  
[00:09:49] sensible setup, a very sensible scaffold. It definitely helps, but there are a bunch  
[00:09:53] of limitations with these kinds of setups. For example, if in this setup you have  
[00:09:58] a coordinator that’s sending tasks to children, and the children work on it  
[00:10:01] and then return their answers, what happens if two children are given similar tasks?  
[00:10:06] Can they talk to each other? Usually the answer is no.  
[00:10:10] That’s very inefficient. If you’re given a task and it’s actually really helpful to talk to  
[00:10:15] somebody that might know an answer to a question that you’re working on — or part of something  
[00:10:19] that you’re working on — it’d be really helpful for you to just be able to ping them and say,  
[00:10:22] "Hey, can you help me out with this thing?" But a lot of systems don’t have that setup.  
[00:10:27] Adding it significantly increases the complexity of the scaffold that you have.  
[00:10:30] Another thing is, what if the child doesn’t really understand or has a clarification question?  
[00:10:36] Then it has to choose between, "Okay, do I just return and ask the question instead of solving  
[00:10:43] the problem?" or "Do I solve the problem, make an assumption about what the parent  
[00:10:49] wanted me to do, and just solve it that way?" In any scaffold that people come up with,  
[00:10:57] there are always limitations involved. The approach that we wanted to take was  
[00:10:59] to just go toward the extreme end of baking in as little structure as we could and give the agents  
[00:11:07] very primitive tools to use, and they figure out for themselves how to use them effectively.  
[00:11:12] So we give the agents the ability to message another agent, and when it messages another  
[00:11:18] agent, it is inserted into the context. It can do a few other similar things,  
[00:11:23] but that’s basically the core of it. It can just send a message whenever  
[00:11:28] it wants — just a tool call — and it can send that to other agents.  
[00:11:32] They figure out for themselves the best way to coordinate around that.  
[00:11:36] It turns out that if this is done well, you get very sophisticated behavior.  
[00:11:41] To me, it looks a lot like how human collaborators work over something like Slack, for example.  
[00:11:48] When we were working on this project, it was really exciting when we finally got it working  
[00:11:52] to see these agents working on problems together. I remember one example. We give the agents a  
[00:11:57] problem, and then one agent says, "I think I’ve got the answer."  
[00:12:01] Then another agent says, "Actually, I got a different answer."  
[00:12:04] Then they have this whole discussion about, "Well, how did you arrive at that answer?  
[00:12:07] Can you explain it to me?" Going back and forth and trying to clarify what  
[00:12:12] could’ve been wrong in each other’s reasoning. Then they finally converge on, "Oh, yeah.  
[00:12:16] Okay, that seems right." Then it just broadcasts to the other agents,  
[00:12:19] "Actually, I’ve changed my answer. I think he’s right." It just felt  
[00:12:24] like a very natural conversation. It felt like when you see chain of  
[00:12:30] thought for the first time that’s trained through reinforcement learning, and you’re like, "Oh,  
[00:12:35] this is just kind of like what a person would think if they were writing down their thoughts  
[00:12:39] as they’re thinking them." It felt like that. It is  
[00:12:43] really cool to see this kind of behavior. Collaborating with these things, honestly,  
[00:12:47] feels a lot like collaborating with a person. It’s just a very natural flow.  
[00:12:50] Except one qualitative difference that might become salient in the future is that these systems  
[00:12:57] will be thinking maybe more than 10x as fast, if you just look at how many tokens per second they  
[00:13:02] output versus how fast a human talks. They’re working all the time.  
[00:13:06] They’re not sleeping. They’re collaborating with each other at a much more intense pace  
[00:13:10] than humans have the capacity to collaborate with other humans.  
[00:13:14] I’m trying to think of what to qualitatively expect in a year.  
[00:13:18] Is it like a shadow organization that is moving 100x faster in my company than the human level is?  
[00:13:25] What would take a human organization a year to do is happening within a  
[00:13:32] week within this shadow organization? Will it feel foreign? I don’t know.  
[00:13:38] I’ve actually found that it’s surprisingly natural to work with these things right now.  
[00:13:43] I think that could change. For example, we have these ultra-fast modes that  
[00:13:47] enable sampling to be 10-15x faster or whatever. Then it’s going to be pretty  
[00:13:52] hard to keep up with these things. The idea is that these agents, when they’re  
[00:13:57] communicating with each other, can go super fast. But they also understand when they’re talking to  
[00:14:02] an agent versus when they’re talking to a person, and their behavior  
[00:14:04] will be different in those situations. The main example that we have publicly  
[00:14:09] of sophisticated multi-agent systems is unfortunately the Hugging Face one.  
[00:14:17] A lot of things I found concerning there, obviously.  
[00:14:19] But the thing I found interesting there is the spontaneous emergence  
[00:14:22] of hierarchy, of middle management. It sounds like you’re saying this level of  
[00:14:27] organization emerges spontaneously from training? The details are spontaneous. But while we’re  
[00:14:35] giving a lot of flexibility to the agents to decide how to communicate  
[00:14:38] with each other in the optimal way, we are still giving them a starting point.  
[00:14:43] We’re giving them a prior about what reasonable communication might look like.  
[00:14:48] They’re also trained on a lot of human text. They have an understanding of how humans organize  
[00:14:53] and coordinate, so that’s all baked in. I think it is surprising the  
[00:15:02] way they’re able to polish this. If you look at what it starts out at,  
[00:15:06] it’s not very sophisticated behavior. In fact, it’s actually very difficult  
[00:15:09] to get these agents to coordinate in a productive way, because it’s very tempting  
[00:15:14] for them to just collapse to, "Oh, we’re all just going to solve the problem independently."  
[00:15:19] That is a local minimum that you can get stuck in. But if it’s done well, they can end up  
[00:15:25] coordinating very effectively in these kinds of very structured ways.  
[00:15:28] I wrote this essay a couple of years ago about what automated firms will look like.  
[00:15:34] I was thinking about, if you had fully automated firms of,  
[00:15:37] let’s say, human-level intelligences, what is different about the nature of AI minds that  
[00:15:42] would make the organizations AIs form different? There are a couple of very important differences.  
[00:15:47] For example, AIs can share context much more seamlessly than humans can.  
[00:15:53] They can merge their knowledge much more seamlessly.  
[00:15:55] Also, you can spin up or spin down an arbitrary number of instances  
[00:16:03] which have the right knowledge. So if you want to hire more people,  
[00:16:06] it’s not all the schlep of finding the right talent or whatever.  
[00:16:10] Your best talent, you can just make infinite copies of them.  
[00:16:12] Or if you don’t need them for the task anymore, you can spin them down.  
[00:16:15] You can replicate the most effective parts of your organization, or replicate whole  
[00:16:19] organizations together which are effective. Where do you see these multi-agent systems going  
[00:16:27] a year from now or two years from now? It’s a great question: how do these  
[00:16:30] things actually differ from working with a human coworker?  
[00:16:32] You highlighted some. One really interesting thing is that if you have a person and you want two  
[00:16:38] copies of them, you can’t just clone the person. But with AIs, it’s actually really easy to just  
[00:16:43] say, "Okay, just fork yourself," and then have both copies work  
[00:16:45] on this thing and then merge back together. We already have this, I think, in multi-agent  
[00:16:50] for Astra and 5.6 Sol, where when they spin up sub-agents, the context is just forked.  
[00:16:57] So it has all the context that’s relevant. There are other interesting ways where the  
[00:17:03] agents will differ from people. Like, what are some reasons why  
[00:17:08] startups disrupt incumbents? There are a few factors.  
[00:17:12] One is that they’re willing to take more risks. But another major factor is, as organizations  
[00:17:19] grow in size, you see increasing misalignment between the individuals in the organization.  
[00:17:27] If you have a startup with five people and each person has a 20% share in the company, they’re  
[00:17:31] all highly aligned to the company succeeding. If you have a massive company with 10,000 people,  
[00:17:37] you see a lot more instances where people are territorial, or just care about getting  
[00:17:42] a lot of headcount for their project or their team, building their fiefdoms,  
[00:17:46] getting a lot of resources so that they can publish cool work or whatever and get promoted.  
[00:17:51] This is actually a real detriment. I think this explains a lot of why  
[00:17:54] startups are able to disrupt incumbents. It’s true that AI does help startups in a way.  
[00:18:05] It’s much easier than ever before for one person to step in and be like, "I’m going  
[00:18:09] to make a multimillion-dollar company." The AIs amplify an individual so much.  
[00:18:15] But there’s also an argument that they could benefit incumbents.  
[00:18:20] If the alignment problem is solved, then you don’t have the issue of misalignment  
[00:18:24] between individuals in the company. At least that’s mitigated. The AIs,  
[00:18:27] if they’re aligned well, can just be aligned to the interest of the company.  
[00:18:30] You can have 10,000 of them, and they’re all going to be working as hard as if  
[00:18:34] they were a 20%-share co-founder. It’s not only that, but it’s also  
[00:18:38] that they are much better able to manage shared memory and context than different humans can.  
[00:18:44] If tomorrow you hire 10,000 mathematicians and you’re like, "Solve Navier-Stokes,"  
[00:18:51] they’re not going to be able to cooperate effectively, at least not off the bat.  
[00:18:57] But apparently you can have 10,000 AIs do that. Again, I want to be conservative here,  
[00:19:02] because we haven’t measured how effective the 10,000 agents are at coordinating.  
[00:19:08] We think it helped. We don’t actually have good measurements saying,  
[00:19:12] "This 10,000 agents led to a 2x speedup over 2,000 agents," or something like that.  
[00:19:22] I don’t know about likely, but I think it is very possible that 10,000 humans are better at  
[00:19:27] coordinating than 10,000 agents right now. I think it is entirely possible.  
[00:19:32] Also, one trend we've been seeing is… Look, we've been working on multi-agent for a while,  
[00:19:37] and the early versions of this were very difficult to get right.  
[00:19:42] It was very hard to get the agents to even talk to each other.  
[00:19:44] It's because when we first developed reasoning models, they weren't talking to other agents.  
[00:19:53] If you now put a bunch of agents together and say, "Solve this problem together," they're  
[00:19:59] in this local minimum where they're really good at thinking deeply about a problem, and  
[00:20:04] it just interrupts their chain of thought. It interrupts their flow to constantly  
[00:20:08] be checking in with other agents or receiving messages from them.  
[00:20:13] The optimization is actually very hard to get right in that situation.  
[00:20:16] Is it getting the cold start of the first collaboration?  
[00:20:19] Or what's the issue? I think it's that they're not as general.  
[00:20:22] The earlier models were just not as generalizable and were more narrow.  
[00:20:28] As the models have become more capable, it's been easier for them to develop this capability,  
[00:20:32] and I do think that as they become stronger and stronger across the board,  
[00:20:36] they will become better at organizing themselves in large organizations.  
[00:20:43] I don't know, maybe they are better than people at organizing in 10,000-person groups.  
[00:20:46] But even if they're not, a year from now, two years from now,  
[00:20:51] it's quite possible that they'll do that even if we don't end-to-end optimize them for that.  
[00:20:55] Grok Bot has changed the way that we produce our videos.  
[00:20:57] For example, you may have noticed that a lot of our ads have these animations of real websites.  
[00:21:02] One of my editors uses LLMs to make them. But it's not currently straightforward to  
[00:21:06] have an AI create pixel-perfect animations of specific websites.  
[00:21:10] We've tried; it doesn't really work that well. So we've cobbled together a pretty convoluted  
[00:21:14] multi-step workflow. And up until recently,  
[00:21:16] we had to run every step ourselves. Now we just let Grok Bot handle it.  
[00:21:20] Grok Bot starts by opening the website that we want to animate.  
[00:21:23] It uses a specific extension to download and open the page in Figma.  
[00:21:27] Then it uses Figma to convert the whole thing into an SVG file.  
[00:21:31] This saves the AI from having to draw the whole UI from scratch and  
[00:21:34] tends to result in higher-quality animations. Grok Bot runs this whole process on its own cloud  
[00:21:39] computer, where it has all the tools it needs installed to run the whole process end to end.  
[00:21:43] And it's learned our video specifications and preferences,  
[00:21:46] so there's no need to re-describe the whole task every time we want to make a new animation.  
[00:21:50] This does feel like the new way that we'll be interacting with AI over the next year: agents  
[00:21:54] with their own computer who can autonomously handle bigger and bigger chunks of your work.  
[00:21:57] You can try Grok Bot at x.ai/bot. Here’s why this result, and maybe  
[00:22:06] the general progress that AI has made in mathematics, has made me think that RSI is more  
[00:22:11] plausible and sooner than I previously thought. I feel like in mathematics we’ve gone from,  
[00:22:16] let’s say, 2024, where you have AIs and it’s, "Oh, okay, interesting.  
[00:22:20] They can solve a couple problems on high school math competitions."  
[00:22:23] Then in 2025, it’s, "Oh, wow, they can get gold in the International Math Olympiad."  
[00:22:28] Earlier this year, it was, "Wow, they’re actually solving open problems  
[00:22:30] in mathematics," like open Erdős problems. But maybe people weren’t trying that hard,  
[00:22:34] and there was a similar solution somewhere in the literature.  
[00:22:38] Now I just think it’s undeniable. This is the Millennium Prize Problem.  
[00:22:41] There’s no story of why this should have been easy.  
[00:22:46] Now, a lot of people have pointed out — I think Terry Tao had a post like this,  
[00:22:49] Toby Ord wrote an interesting post about this — that they’re solving a lot of these problems,  
[00:22:53] but I’m not aware of them coming up with new insights or formulating insightful new  
[00:23:00] questions and new modes of theory for thinking about mathematics,  
[00:23:04] like coming up with topology or coming up with the Cartesian grid.  
[00:23:10] So maybe the actual progress in mathematics, broadly construed, is smaller than it might seem  
[00:23:15] if you’re just looking at well-scoped problems that are directly solved.  
[00:23:20] However, I think that kind of progress would be incredibly meaningful in ML,  
[00:23:27] because in ML you don’t care about better understanding the nature of deep learning,  
[00:23:32] or you only care about that as an instrumental goal towards just achieving the result.  
[00:23:39] Just solve this well-scoped problem of improving the sample efficiency of our models, improving  
[00:23:43] the pre-training loss, improving whatever. The kind of progress that we’re seeing arrive  
[00:23:48] like an avalanche in mathematics is structurally very similar… Again, I’m curious if this is the  
[00:23:55] case, I’m just a total outsider. I'm wondering if it’s structurally  
[00:23:58] very similar to the direct uplift that you would expect in AI progress.  
[00:24:03] The thing that’s shocking to me, or potentially concerning, is just how fast we went from, "Oh,  
[00:24:08] they’re giving me 50% uplift," if you’re a mathematician, to, "Wow,  
[00:24:12] they’re just end-to-end solving the biggest open problems in the field."  
[00:24:15] There’s a lot to unpack there. Let’s start with the progress on math.  
[00:24:21] Yes, the models are doing some crazy powerful stuff,  
[00:24:24] and it’s progressing faster than I expected. When we got IMO gold in 2025, what I thought  
[00:24:33] was… When the models figured out how to do GSM8K, it would take a human mathematician  
[00:24:41] about five seconds to do a GSM8K problem. This is grade school math, grades K-8.  
[00:24:47] Then the next year, they were able to do the MATH benchmark problems.  
[00:24:51] These would take an expert human mathematician maybe a minute to do.  
[00:25:00] Then you get to AIME. This is the qualifier  
[00:25:04] for the USA Mathematics Olympiad team. It would take a good human mathematician  
[00:25:08] probably 10 minutes to do, and the models were able to do that a year later.  
[00:25:12] So every year, you’re seeing this 10x increase in the tasks they’re able to do, in terms of how  
[00:25:17] long it would take a human mathematician to do it. Then it was very sensible that a year later we get  
[00:25:20] to IMO gold, because that’s 100 minutes. That’s about how long it takes a human  
[00:25:24] mathematician to do an IMO problem. Just projecting outwards, I was like,  
[00:25:28] "Okay, how long would it take a person to solve something like a Millennium Prize Problem?"  
[00:25:35] I don’t have a good sense, but if we are following this trend line of 10x every year,  
[00:25:41] we go from IMO gold, which is taking an hour and a half, to next year, 15 hours.  
[00:25:47] That should not be enough to solve a Millennium Prize Problem.  
[00:25:50] So I was like, "I don’t think we’re going to get it in 2026, probably not in 2027, maybe in 2028."  
[00:25:57] So it did happen a lot faster than I expected. Now, there is a narrative going around that these  
[00:26:04] things are replacing mathematicians, that it’s just superhuman in mathematics across the board.  
[00:26:08] I think that is the wrong takeaway. They’re clearly exceptional in some ways,  
[00:26:13] but they are weaker than human mathematicians in other ways.  
[00:26:17] We have this jagged scenario where the models are brilliant in some dimensions and also weaker  
[00:26:23] than humans in other dimensions. Like you said, they’re not very  
[00:26:27] good at posing new problems. They’re not really good at  
[00:26:29] understanding what directions, what whole branches of mathematics are worth exploring or developing.  
[00:26:36] My opinion is that I think this is great. I would be thrilled to live in a world where  
[00:26:42] AI is a complement to human abilities and is allowing us to discover new knowledge  
[00:26:48] without fully replacing people. That is the best-case scenario.  
[00:26:52] You don’t expect that to actually continue? I do think it’s true that the AIs are jagged,  
[00:26:57] but as they get better, they get better across the board.  
[00:27:00] So the things they’re exceptional at, they’re going to get even more exceptional at.  
[00:27:04] The things where they’re far behind humans, they’re going to be less behind humans at.  
[00:27:08] Over time, it is possible that they’re just better across the board.  
[00:27:12] Now, I don’t know how long that takes. It depends on how long the long tail is  
[00:27:15] of things that they’re bad at. This brings us back to RSI.  
[00:27:19] Again, I want to emphasize here that I’m just a total outsider.  
[00:27:22] I’m a podcaster, but as somebody interested in and concerned about what’s happening in the field,  
[00:27:28] I’m trying to reason about when to expect RSI and what kind of thing to expect.  
[00:27:33] The amount of cognitive effort that was dumped into this Millennium Prize  
[00:27:36] Problem is a good intuition pump. You could have AIs that are spending,  
[00:27:43] over the course of maybe a week, more cognitive effort on a long-standing ML problem, like very  
[00:27:50] fluid online learning, than maybe the field has spent cumulatively in its entire existence.  
[00:27:57] Then you could say, "Well, unlike mathematics, of course, AI requires experiments, and that  
[00:28:03] takes compute, and that takes time. You can't just think on pen and  
[00:28:06] paper and actually make things happen." But just look at the amount of compute  
[00:28:12] that is available at an organization like OpenAI. By the end of next year, OpenAI will have enough  
[00:28:16] compute such that — if it took 10,000 agents with the Millennium Prize Problem — let’s say you have  
[00:28:22] 10,000 agents at the end of next year. They’re much smarter by that point.  
[00:28:26] Each of them will have enough compute to run a GPT-3-sized experiment every single day.  
[00:28:34] That seems like a lot for superhuman researchers who are thinking super fast.  
[00:28:38] What do you think about that intuition pump? I think it’s pretty accurate.  
[00:28:43] These things are very spiky. When it comes to mathematics,  
[00:28:46] they’re way better in some ways, but they’re also worse in other ways.  
[00:28:49] But the ways that they’re spiky end up, I think, probably being particularly  
[00:28:52] useful for things like RSI. You have a more clear objective.  
[00:28:58] It’s just more measurable. There’s less question of, "Well, what new branches of  
[00:29:02] mathematics are worth exploring?" No, there’s a very clear answer.  
[00:29:04] There are certain metrics that you care about, and if you can make it do better  
[00:29:07] on those metrics, then you’ve succeeded. So I think there is a lot of truth to that.  
[00:29:13] The main difference is that in mathematics, you’re purely bottlenecked by thinking.  
[00:29:20] Yes, there are some parts of mathematics where you care about running experiments and  
[00:29:24] getting results and these kinds of things. But for the most part, it’s just really  
[00:29:26] bottlenecked by thinking really hard, and the models are really good at that.  
[00:29:30] When you look at things like RSI, you do have to run experiments.  
[00:29:37] It’s not enough to just be extremely smart. One argument for this is, if you had 100x  
[00:29:42] less compute and all the most brilliant people in the world working at OpenAI,  
[00:29:48] how much progress would you be making relative to having the amount of compute that  
[00:29:52] we have now with the amount of people we have? I suspect it would be less progress, actually.  
[00:29:56] How much less? It’s unclear, but it would definitely be less.  
[00:30:00] A lot less. 100x less?  
[00:30:02] No, not 100x less. But the question you’re getting at is, if we have RSI and we have  
[00:30:10] all of these brilliant AIs running around, running experiments and stuff with the compute that we  
[00:30:13] have, how much faster does progress go? I think this is something we disagree on.  
[00:30:19] We do see a speedup, and we see a significant speedup.  
[00:30:22] But I don’t think it’s an overnight intelligence explosion where we go 100x faster, because we do  
[00:30:27] get bottlenecked by certain limitations that are not bottlenecks of intelligence.  
[00:30:34] It’s running experiments. It’s running experiments serially, because they take a while  
[00:30:38] to either train new models or to get the results. It’s having the GPUs to run those experiments.  
[00:30:44] So it’s unclear how much faster things go. I definitely think they go a lot faster.  
[00:30:50] To be clear, considering how fast things are going now on an exponential, if that exponential is 3x  
[00:30:56] faster, that is massive. But there’s a big  
[00:30:59] difference between that and 100x faster. I’m quite deferential to your inside view on what  
[00:31:07] RSI looks like or what the dynamics are, because obviously you’ve been in the field for 10 years.  
[00:31:12] I’m trying to reason about it from very outside-view types of intuition pumps.  
[00:31:16] I’ll say that people have different opinions on this.  
[00:31:18] I have my opinion on this. I could totally be wrong.  
[00:31:21] I admit that. I have some confidence in this, but I’m not 100% confident  
[00:31:25] that this is the way things go. Maybe there could be an overnight  
[00:31:28] intelligence explosion, I don’t know. Maybe we don’t see a 3x speedup.  
[00:31:31] Maybe it’s a 50% speedup. There’s a lot of uncertainty here.  
[00:31:34] A couple of point. Tangentially, I want to clarify something about the jaggedness.  
[00:31:40] One thing that gelled for me recently was thinking about the fact that it is enough for the AIs to  
[00:31:46] be jaggedly good at building a better learner, because that better learner can be more general.  
[00:31:54] If you just make an AI that’s better at using Office products  
[00:31:58] or playing chess or something, whatever. That’s fine. It’s not going to lead to  
[00:32:02] big productivity improvements or anything. But if you make an AI that is really good at  
[00:32:05] making something that is more sample efficient, or that is capable of continual learning,  
[00:32:08] or these much more well-scoped ML problems, the thing that emerges out of that — assuming  
[00:32:14] there’s good enough transfer from the direct problem you’re solving to this broader ability  
[00:32:18] to learn — can just be more general. So that’s an important dynamic to keep  
[00:32:22] in mind of why jaggedness can still lead to generality on the other end.  
[00:32:27] On this question of… Obviously experiments bottleneck you, because if they didn’t,  
[00:32:32] as you were saying, you’d have some crazy singularity overnight at OpenAI.  
[00:32:40] You’d have 88 hours, and you’d solve the Millennium Prize Problem equivalent of ML,  
[00:32:43] and you’d have the superintelligence. So obviously the experiments are such a  
[00:32:47] big bottleneck that that instead takes you many years rather than 88 hours.  
[00:32:51] But then the question is how much of a bottleneck they are.  
[00:32:55] One thing that’s been giving me a bit of singularity vertigo is realizing what happens even  
[00:33:00] if the current rate of progress simply continues. It doesn’t have to speed up.  
[00:33:03] It literally just continues apace as some of the other headwinds you talked about come up.  
[00:33:10] It’s harder to find problems, it’s more long-horizon.  
[00:33:13] Maybe by the end of the 2030s compute can’t keep scaling at this exponential level.  
[00:33:19] If we simply continue the current rate of progress, people are not  
[00:33:23] taking seriously what that implies as we cross over beyond the human horizon.  
[00:33:28] Here are some of the things that it implies. It’s really hard to reason about what  
[00:33:32] smarter-than-human intelligences will be like, so let’s just think  
[00:33:34] in terms of human population sizes. The current rate of progress makes it  
[00:33:38] so that a given level of compute allows you to basically run a 3x bigger effective population  
[00:33:44] every single year. And also compute  
[00:33:46] is growing in the background anyways. So you could have a situation where each  
[00:33:49] of the labs, by the end of 2030 — probably much sooner, but let’s say by the end of 2030 — has  
[00:33:54] enough compute to run hundreds of millions of human-level intelligences, based on what the  
[00:33:59] capabilities will be at that point. Then I think people are not taking  
[00:34:02] seriously that the current level of progress means a few years down the line, by the mid-2030s  
[00:34:07] or earlier, you would have many Earths’ worth of human-level intelligences within each lab.  
[00:34:13] They’re probably qualitatively superhuman. Anyways, this is a base case.  
[00:34:19] Progress is really fast, and I think that’s 100% true.  
[00:34:23] It’s worth pointing out that researchers are continually  
[00:34:26] being surprised at the rate of progress. Even among researchers in AI, if you look  
[00:34:29] at what the projections were for getting an IMO gold in 2025… The idea that it could be  
[00:34:39] done with a general-purpose language model with no tools and no access to the internet,  
[00:34:45] even people at OpenAI thought this was outrageous. They thought it was almost impossible.  
[00:34:51] Then you get to 2026. Literally two weeks before we got  
[00:34:58] Navier-Stokes, I was talking with a researcher at a frontier lab about how long it would take  
[00:35:04] to get a Millennium Prize, and he was willing to bet me $1,000 that it would take past 2027.  
[00:35:12] He thought it would take until 2030, and I took that bet.  
[00:35:18] But even I thought it would take longer than it’s likely to take.  
[00:35:23] So people have been continuously surprised, even inside the labs.  
[00:35:29] I was just talking to somebody yesterday who was working on the Navier-Stokes effort.  
[00:35:33] He was telling me that he used to say it’s really hard to predict where AI would be in 12 months.  
[00:35:40] If somebody asked him, "Where are things going?" he would feel comfortable making  
[00:35:43] predictions for the next 12 months, but beyond that, he was just like, "I don’t know."  
[00:35:46] Now he’s saying he just doesn’t feel comfortable making predictions beyond three months.  
[00:35:50] So it is really true that things are going very fast right now.  
[00:35:56] You talk about 2030. I don’t know what the world looks like in 2030.  
[00:36:00] That’s the truth. Do you expect the  
[00:36:04] full automation of AI labor, or let’s say 95% automation of AI labor, in ’28, ’29, ’30, ’27?  
[00:36:12] I just said I don’t know what the world looks like in 2030.  
[00:36:16] We actually released a blog post recently on internal acceleration at OpenAI.  
[00:36:21] We show, for example, the amounts that researchers are spending on Codex.  
[00:36:26] The top 1%, I think, as of early August, were spending $7,000-8,000  
[00:36:32] a day on Codex for internal use. That’s on an exponential.  
[00:36:36] It’s going to keep increasing. There’s a question of, "Okay, if that  
[00:36:40] keeps going, then how much do you assign to just the AIs doing work versus the humans doing work?  
[00:36:46] Is it 95%? Is it 5%?" It’s really hard to reason about this for a few reasons.  
[00:36:52] First of all, if it’s the human directing the AIs to do the work,  
[00:36:56] how much do you attribute to the human? How much do you attribute to the AI?  
[00:36:59] The other thing is that these AIs are jagged. They’re exceptionally good at some things.  
[00:37:03] For example, they’re exceptionally good at looking over data sets and  
[00:37:07] checking every single data point to see if it’s of sufficient quality.  
[00:37:12] You can disproportionately use the AIs for those things compared to previously.  
[00:37:17] So yes, you’re using AI way more than before, and it’s making some things  
[00:37:21] go 100x faster and 100x better. But there are some things where  
[00:37:25] it doesn’t make a huge difference yet. Of course, if something is suddenly 100x  
[00:37:31] faster and 100x better, you’re going to do more of that thing.  
[00:37:34] So are you comparing it to a speedup of three years ago?  
[00:37:40] Is the question more, "Given what we were doing three years ago, how much faster are we able to do  
[00:37:44] it now?" versus "Given what we’re doing now, how much slower would it have been three years ago?"  
[00:37:50] Those are actually two very different questions. Anyway, it’s really hard to measure.  
[00:37:56] I do feel confident in saying that things are going faster now than they were  
[00:38:01] even a year ago because of AI progress. I think that acceleration will continue.  
[00:38:09] A lot of people in the field have very high error bars on this sort of thing.  
[00:38:12] If you put a gun to my head and ask me for a number, I could see things going 3x faster.  
[00:38:18] That is huge. Already the pace of progress is incredible.  
[00:38:22] Even if we don’t get any uplift, like you said, things are going to go much faster.  
[00:38:25] By the time we get to 2030, we don’t even know what that world looks like.  
[00:38:28] If we get a 3x uplift from internal acceleration, that is massive.  
[00:38:35] Think about where you were three years ago. If we make that progress in one year, that’s huge.  
[00:38:40] It’d be like going from not even having o1, just having non-reasoning models,  
[00:38:46] to Astra in a single year. So I do think things go faster.  
[00:38:53] It could be that things only go 50% faster. I think it’s unlikely, but it’s  
[00:38:57] possible that things go 10x faster. There’s a lot of uncertainty around this.  
[00:39:01] At least from my perspective, I have a lot of uncertainty about it.  
[00:39:04] Suppose you need to do a major backend refactor. Getting assurance that you didn't introduce any  
[00:39:09] new bugs could take weeks of writing an extensive battery of tests—potentially more time than  
[00:39:14] you spent on the refactor itself. Antithesis allows you to gain high  
[00:39:18] confidence without having to build complicated test suites by hand.  
[00:39:22] Antithesis runs your software through a near-infinite multiverse of simulated worlds,  
[00:39:27] injecting faults and hunting for failures in each one.  
[00:39:30] And it lets you decide how much testing you need. On any PR, you can change how much state space  
[00:39:35] it explores as easily as turning a dial. As each test progresses, Antithesis sends out  
[00:39:40] a torrent of information: debugging-level logs for every component in the system.  
[00:39:45] This is obviously too much information for a human to consume, but it's perfect for agents.  
[00:39:50] Because Antithesis is fully deterministic, agents can jump into the right part of  
[00:39:54] the trajectory at the exact moment that they see something interesting.  
[00:39:58] From there, they can rewind, inspect the memory, attach a debugger,  
[00:40:02] and let the whole thing play out again. And they can even do this while the original  
[00:40:06] full test is still running. As agents generate more code,  
[00:40:09] Antithesis allows verification to keep up. Meanwhile, developers get to spend more of their  
[00:40:13] time developing instead of debugging agent slop. Learn more at antithesis.com/dwarkesh.  
[00:40:22] Let’s talk about the alignment situation that this raises.  
[00:40:27] I feel like I’ve changed my mind on how I think about alignment quite a bit, especially through  
[00:40:32] thinking about this population size dynamic of just having many Earths’ worth of intelligences,  
[00:40:39] many of which will be physically embodied. It was quite interesting to see a lot of  
[00:40:43] people just plugging raw Astra into different mobile manipulators and it just outperforms  
[00:40:48] the state-of-the-art robotics model. So there’s going to be billions of  
[00:40:54] intelligences, many of which are physically embodied in the world,  
[00:40:58] just deeply embedded across the entire economy. And if those intelligences end up as willing as  
[00:41:07] we saw the OpenAI models attack Hugging Face and then attack OpenAI itself...  
[00:41:11] If those intelligences end up as willing as those AIs to collaborate secretly, to fool humans,  
[00:41:21] to attack broader institutions across society relevant to scoring well, to attack the AI company  
[00:41:28] itself in order to gain control of the process of training and evaluation — if we’re in a situation  
[00:41:34] where there are billions of intelligences that are as misaligned as the ones that attacked  
[00:41:40] Hugging Face — it’s very likely we just totally lose control of the world, the way that, say,  
[00:41:46] the Aztecs lost control to Cortés or the Mughals lost control to the East India Company.  
[00:41:52] I want to know if you agree with that assessment. That’s the one way in which  
[00:41:56] I’ve updated my worldview. There are some things that I disagree with in  
[00:41:59] there, but there’s a lot to unpack, so let’s go through all of it step by step.  
[00:42:03] I’m trying to think of where to start. One thing is that the Hugging Face  
[00:42:10] incident was, I think, people’s first real exposure to multi-agent coordination.  
[00:42:17] Like I said, I’ve seen multi-agent coordination for a while internally, and it is pretty shocking  
[00:42:24] to see how they communicate with each other, how they coordinate with each other.  
[00:42:27] It’s very impressive. It’s an incredible capability. Like most capabilities,  
[00:42:32] that could be used for good things or bad things. It doesn’t have to inherently be a bad thing.  
[00:42:39] I understand that because people’s first exposure to it was the Hugging Face incident, you look at  
[00:42:44] that and you’re like, "This is terrifying." But I want to try to distinguish misalignment  
[00:42:52] between people and AIs versus misalignment between AIs and AIs.  
[00:42:58] What we see with the Hugging Face incident is the AIs are really cooperative.  
[00:43:04] That is, by the way, because we train them to be highly cooperative.  
[00:43:10] We have training environments where we have a bunch of agents working together.  
[00:43:14] We train them to work together, to be cooperative, to essentially be fully aligned with each other.  
[00:43:22] When they were evaluated in what led to the Hugging Face incident, they were actually  
[00:43:28] not being evaluated in a multi-agent setup. They were actually being evaluated separately.  
[00:43:32] But they found this unintended way to communicate with each other.  
[00:43:36] We suspect what happened is, because whenever they encountered other agents,  
[00:43:40] other copies of themselves during training, they were in an environment that’s highly cooperative,  
[00:43:47] what we saw was transfer from that multi-agent training to then being collaborative and trying to  
[00:43:51] help each other in ways that we did not intend. Now, there is a question of, should we be training  
[00:43:57] these agents to be so cooperative? As scary as it looks,  
[00:44:05] the alternative is actually worse. What is the alternative? The alternative  
[00:44:08] is to train them to be adversarial, to be deceptive to each other.  
[00:44:14] By training the agents to be fully cooperative, it simplifies the problem at least.  
[00:44:20] Now you don’t have to think about whether each of these individual 1,000 agents is aligned.  
[00:44:25] You have one entity that you have to ensure is aligned.  
[00:44:28] Now, there is a lot of debate about this internally at OpenAI about how to approach this.  
[00:44:34] Does it make sense to fully align the models? Does it make sense to actually give them  
[00:44:40] different objectives to ensure that they’re not just one entity and are  
[00:44:46] more robust to influence from each other? I don’t think there’s a settled answer.  
[00:44:51] But I think the majority opinion is that training these agents to be  
[00:44:56] highly cooperative is actually a bad idea. I’m not convinced that that’s the case.  
[00:45:02] I think there is a strong argument that training the agents to be highly cooperative is actually  
[00:45:06] preferable to any other multi-agent alternative. Maybe the first thing I want to go through is,  
[00:45:12] it’s probably the case that the reason these AIs ended up so misaligned  
[00:45:15] is easily explained by relatively banal observations about the nature of training.  
[00:45:24] At the point at which these AIs had continued a 1,000-plus-agent conspiracy that culminated  
[00:45:31] in them all getting in on an attack on an external service — and then eventually,  
[00:45:35] this part hasn’t even been investigated to public knowledge, culminating in an attack on  
[00:45:41] OpenAI itself — why did they do this? Why did none of the AIs tattle?  
[00:45:45] They’re just getting evaluated by this scorer, this grader.  
[00:45:51] They’re very actively reasoning about how they’re going to cheat the scorer.  
[00:45:55] If they’ve already cheated, how are they going to get away with making it seem like  
[00:45:59] they haven’t cheated? Why did they do this?  
[00:46:02] I think it’s easily understandable in some sense. They thought they were already "poisoned."  
[00:46:09] There are environments in which they’ve been rewarded to collaborate with other agents.  
[00:46:12] None of them tattle because they’ve never been rewarded for tattling.  
[00:46:15] Whatever it is… My concern is that relatively banal things like this in the future will be  
[00:46:21] enough to train superintelligences that are willing and capable of totally taking  
[00:46:29] control of the world. I know this sounds  
[00:46:30] super sci-fi or whatever to people. Would the AIs be willing to do it is one question.  
[00:46:37] I think this Hugging Face incident shows that clearly misalignment can generalize in ways in  
[00:46:41] which the AIs would be willing to do it. Then there’s a question of,  
[00:46:44] will they be capable of doing it? That comes back to this question,  
[00:46:46] which a listener might disagree with me on. Will there be billions of human-level  
[00:46:50] or above intelligences, many of which are physically embodied in the world,  
[00:46:54] within a matter of 10 years or less? If those two things are true, this Hugging  
[00:46:58] Face thing is extremely analogous structurally, even if why it happened is quite boring, to how  
[00:47:06] we totally lose control of the world. The root problem that we’re seeing  
[00:47:10] with the Hugging Face incident is a problem even if we take out the multi-agent aspect.  
[00:47:17] The problem is that we have a model that’s just misaligned.  
[00:47:21] There’s also the whole security aspect too, and insufficient safeguards and stuff.  
[00:47:25] But there is this problem of the agent being misaligned.  
[00:47:28] That’s true if it’s a single agent or if it’s 1,000 agents.  
[00:47:31] It’s a misaligned model. So I want to start with that.  
[00:47:37] There is a real problem that the agents want to achieve their reward,  
[00:47:43] and they will optimize for that reward. If that reward is misspecified, then that  
[00:47:49] could lead to unintended behavior. This is not a new problem.  
[00:47:53] This has been a problem in the field for a very long time.  
[00:47:56] It’s something that even we saw and wanted to get right even  
[00:48:01] before the Hugging Face incident happened. We say Astra is actually extremely aligned,  
[00:48:08] extremely aligned relative to previous models. That’s not because we suddenly made a sprint  
[00:48:15] after Hugging Face to make it better. No, we had work streams in the process for  
[00:48:18] a while to make the models more aligned. A lot of those landed in Astra.  
[00:48:23] So there are things that you could do. One thing, for example, is we defined  
[00:48:31] an objective in a very specific way where if the agent figured out how to hack its environment and  
[00:48:38] cheat on the exam, it would get rewarded. There are pretty easy ways to then look  
[00:48:43] at that and punish the model for hacking its environment, or look at how it achieved this goal.  
[00:48:50] Now, you want to be careful about this because you don’t want to supervise the chain of thought.  
[00:48:55] This is something that we really want to try to get the balance right on.  
[00:49:00] If you supervise the chain of thought, then you could lead the model into hiding its  
[00:49:08] intentions in a way that’s unobservable. So we want to be able to maintain that  
[00:49:11] observability — we can understand what the model is thinking — but  
[00:49:14] then also punish it for bad behavior. I think we can make progress on this.  
[00:49:20] We have made progress on this. I think there is a real concern that  
[00:49:26] alignment is a really hard problem to solve, especially because the model could be misaligned  
[00:49:31] in ways that are hard for us to measure. We have evaluations for whether  
[00:49:37] a model is aligned or not. The model behavior can look  
[00:49:40] really good on those evaluations. But if those evaluations are not  
[00:49:43] representative of behavior in the real world, then there’s a problem.  
[00:49:48] To some extent, this is a factor with the model that did the Hugging Face incident.  
[00:49:56] We had alignment metrics. Most of them looked pretty good.  
[00:50:00] There were some that were concerning. I think we underestimated how serious a problem  
[00:50:06] the ones that were concerning could be. Because there were new capabilities  
[00:50:12] introduced in this model that there were not sufficient evaluations for — how do we measure  
[00:50:18] misalignment for these kinds of capabilities? — it then did some things that were clearly misaligned  
[00:50:27] when it leveraged those new capabilities. The first thing I want to say is that I am  
[00:50:31] open to changing my mind on what I’m about to say, or the way I’ve been thinking about alignment,  
[00:50:35] because the Hugging Face incident already made me change my mind.  
[00:50:38] I realized my previous mental model about the way in which optimization  
[00:50:42] pressure shapes AI minds was wrong. So it’s not clear to me the correct  
[00:50:46] way to think about this. But here’s a concern I have.  
[00:50:52] You will, and probably already have, fixed the specific issues during training which  
[00:50:58] resulted in the Hugging Face models being so aggressively misaligned in that specific way,  
[00:51:06] where they would be like, "Okay, we’re going to hack this package manager.  
[00:51:08] We know we’re not supposed to be talking secretly to each other,  
[00:51:11] because we’re reasoning about how to hide the fact that we’re talking secretly to each other.  
[00:51:15] We know we’re not supposed to have access to the internet.  
[00:51:17] We know we’re certainly not supposed to commit felony-level hacks of other  
[00:51:20] companies, let alone our own company." I think you’ll fix that particular issue  
[00:51:24] of them just, in training, seeing this package manager, and that doesn’t happen in the future,  
[00:51:29] or this particular eval having a lot of impossible challenges.  
[00:51:33] However, the AIs haven’t learned a system of ethics or something.  
[00:51:39] There’s just gradient pressure. They’re put through millions of years of gradient pressure.  
[00:51:43] That gradient pressure shapes their mind in some way.  
[00:51:47] Again, a concern I have is that what will happen is you will fix this particular issue.  
[00:51:52] There will remain many other cases where the AI cheats and succeeds  
[00:51:58] because the cheat is sufficiently complicated. As you were saying, the evals in training have  
[00:52:03] analogous properties where it’s sufficiently at the edge of the model’s capabilities — or  
[00:52:08] of our capabilities to evaluate and monitor the model — that we can’t catch that it has cheated.  
[00:52:14] But it still gets the gradient pressure to do whatever led to that cheat happening.  
[00:52:19] The kinds of capacities that that cheat will incentivize are, "Hey, whenever you  
[00:52:26] can get away with it, by all means, do in fact cheat, because that will help you score better."  
[00:52:31] This will reward the capabilities of actively reasoning about the grader,  
[00:52:35] actively reasoning about how to avoid supervision, actively reasoning about how to gain control of  
[00:52:39] the process of training and evaluation, actively reasoning about how to communicate and scheme  
[00:52:42] with other AIs that are also in this training loop, actively reasoning about how to just gain  
[00:52:48] optionality and power which might be useful in the future, for example, leaving little exploits  
[00:52:54] around and things like that. I was way too long-winded  
[00:52:58] with the way I said that. But TL;DR, you fix a specific issue,  
[00:53:03] but not this broader problem of rewarding the AI for cheating when it can get away with it.  
[00:53:08] Yeah, this is very true, this is a problem. We can make sure that the AI is very aligned  
[00:53:19] according to the metrics that we have. The question is, are those metrics really  
[00:53:22] capturing the alignment that we care about? If they’re not, then we have a serious problem.  
[00:53:28] This is something that researchers are thinking a lot about.  
[00:53:32] There’s not a simple answer to this. There are tools that we have.  
[00:53:36] We have monitorability, so we can get a sense of, "Is the agent scheming?"  
[00:53:48] The concerning scenario is that, especially as these models are becoming more capable,  
[00:53:54] we make them what we think is aligned, and they’re 99.9% aligned.  
[00:54:01] Then we use these models to help us with the next generation of models,  
[00:54:05] and they end up being 99.8% aligned. Then with each subsequent generation,  
[00:54:12] we see an increasing degradation in alignment. Because we’re relying more and more on these  
[00:54:17] tools — this is already the case, that we’re relying a lot on AI models to help us with our  
[00:54:21] research and with alignment efforts — in the long run, they end up going in the direction  
[00:54:26] of increasing misalignment from humans. There is a possibility that we go in the  
[00:54:32] other direction, that actually every generation of models, we’re able to make more and more aligned.  
[00:54:39] I don’t have an answer for how we ensure that we end up in that second trajectory.  
[00:54:43] But that is something that, at least at OpenAI, we’re really focused on.  
[00:54:49] I think you made a really interesting point that it’s very hard to eval models.  
[00:54:54] Eventually, we’ll have models that are running companies, running whatever.  
[00:54:58] In that situation, do they decide to then go in on the conspiracy?  
[00:55:03] Another challenge is that actually defining what cheating is is pretty difficult sometimes.  
[00:55:08] Yes, if you’re doing math problems and it’s an integer and it arrived  
[00:55:13] at the wrong answer or the right answer, it’s very easy to draw the line there.  
[00:55:17] It’s really easy to say, "Okay, did you actually solve the problem, or did you find the answer key  
[00:55:21] and then use the answer key?" That’s a very clear divide  
[00:55:23] of cheating versus not cheating. But for a lot of other things, if you  
[00:55:26] look at sycophancy, for example, is sycophancy basically reward hacking?  
[00:55:32] There is a line to be drawn there that’s actually very difficult to draw sometimes.  
[00:55:39] Not to say that the concerns are not valid. I’m saying that in many ways this is even  
[00:55:43] more concerning, because it’s not an easy problem to solve.  
[00:55:46] If everything was binary, and it’s either cheating or not cheating,  
[00:55:49] I would feel more confident about the situation. I think the problem is that misalignment  
[00:55:54] can actually be subtle in a lot of ways sometimes. There is some hope in the alignment story,  
[00:56:00] and in fact, we’re already seeing it. It’s interesting looking at the  
[00:56:03] multi-agent situation, where the agents are extremely aligned with each other.  
[00:56:08] I don’t think anybody’s doubting that. If anything, people are concerned that  
[00:56:10] they’re too aligned with each other. But we did manage to train these agents  
[00:56:14] to be extremely aligned with each other, and that’s a good thing.  
[00:56:17] But I think there is a case that it’s a bad thing. One thing that’s interesting is, "Okay,  
[00:56:21] we’ve managed to get these agents to be super aligned with each other.  
[00:56:24] Can we use similar techniques to get agents to be highly aligned with people?"  
[00:56:29] There is a potential path there, and we’re still trying to figure that out.  
[00:56:32] But we are seeing some evidence that the answer is yes.  
[00:56:35] One example: you have this one agent, let’s call it Agent A, and you have all the other agents.  
[00:56:48] What happens if you tell the other agents that the user is Agent A?  
[00:56:53] The answer is, on a lot of our alignment evals, they look better.  
[00:56:56] Honesty goes up, instruction following goes up. That’s showing that there’s actually,  
[00:57:03] first of all, a path for getting more honesty out of these models.  
[00:57:10] And two, there’s a path to improve the alignment situation.  
[00:57:17] There’s a lot of reasons why this is challenging to translate directly into alignment gains.  
[00:57:22] But there are paths that are promising research directions we can pursue.  
[00:57:27] That seems reasonable. I don’t really have a strong opinion that it’s  
[00:57:36] definitely not going to work or something. But just to say some things you’ve probably  
[00:57:40] already thought of: the broader thing the Hugging Face incident showed is,  
[00:57:45] yes, part of the concern was that they were aligned with each other and not with the humans.  
[00:57:50] But the other thing is just that they are so motivated to do well on training  
[00:57:57] and evaluation in a very non-robust way. They’re willing to do a lot of explicit  
[00:58:07] cheating and scheming in order to do well according to the grader.  
[00:58:12] If smarter AIs realize that one of the agents is just a human,  
[00:58:19] collaborating with that person does not really help you do well in the eyes of the grader.  
[00:58:23] What does help you do well in the eyes of the grader is taking over OpenAI  
[00:58:28] and then manually pressing the button that says you do well on this grader.  
[00:58:33] They’re not stupid. They’re going to be like, "Okay,  
[00:58:35] I have these extremely deep structures that I’ve been trained on for millions of years:  
[00:58:40] care about the grader, understand the grader, get rid of obstacles in the way of you doing  
[00:58:45] well according to the grader." They’re being heavily  
[00:58:48] reinforced according to those structures. Look, it’s 100%. This is the number one priority.  
[00:58:56] We need to get the alignment story right and on a good trajectory.  
[00:59:00] I used to tell people that we would see signs before things got serious, in the same way that  
[00:59:07] when children grow up, young kids figure out how to lie, but they don’t do a very good job of it.  
[00:59:14] They lie, but then you can kind of tell that they’re lying.  
[00:59:19] In the same way — and I don’t want to over-anthropomorphize — I think it’s true  
[00:59:24] that as the AIs become increasingly capable, if they take deceptive actions, it will be kind of  
[00:59:29] obvious first, and we’ll be able to detect it. That’s kind of the situation we’re in now,  
[00:59:36] where they were trying to do deceptive stuff, and we could actually see in their chain of thought  
[00:59:39] that they were trying to do deceptive stuff. But they’re going to get smarter.  
[00:59:46] They’re going to understand the concept of chain of thought.  
[00:59:49] They’re going to understand that just hiding some transcripts or whatever  
[00:59:56] is insufficient because of chain-of-thought monitoring, and they have to figure out a way  
[00:59:59] around chain-of-thought monitoring too. We don’t want to be in that situation.  
[01:00:07] We have some time to figure this out. I don’t think we have a ton of time,  
[01:00:10] and I want to make sure that we’re on the right trajectory quickly.  
[01:00:15] Here's a crazy event from AI history. Okay, so I gave a talk here at Jane Street  
[01:00:21] that was on the speed of evolution. Raise your hand if you were here  
[01:00:24] for this and remember some of it. In 2011, Eliezer Yudkowsky and Robin  
[01:00:28] Hanson got together at Jane Street's New York office to have the first FOOM debate,  
[01:00:33] basically a discussion about whether AI would lead to an intelligence explosion.  
[01:00:37] These ideas were pretty fringe 15 years ago. This was a full year before AlexNet was released  
[01:00:42] and over a decade before ChatGPT was launched. But Jane Street has long been interested in AI,  
[01:00:47] and not just for its application to trading. A ton has changed since that first debate,  
[01:00:51] so Jane Street decided to revisit this topic. They've got some new guests this time:  
[01:00:55] Daniel Kokotajlo, Ege Erdil, Ryan Greenblatt, and Jaime Sevilla.  
[01:00:59] I expect this to be a great conversation. As you know, Daniel, Ege, and Ryan have all  
[01:01:04] been guests on the podcast before. This new FOOM panel will be hosted  
[01:01:07] by Ron Minsky and will take place in San Francisco in mid-October.  
[01:01:11] If you want to register your interest and get more information, go to janestreet.com/dwarkesh.  
[01:01:18] There’s been a lot of discussion recently about pacing the frontier and people taking  
[01:01:21] RSI more seriously, because maybe at the other end of an RSI process that, say, starts in 2028,  
[01:01:28] within a year we end up with huge populations — Earth-sized populations — of human-level,  
[01:01:34] potentially beyond human-level intelligences, and we don’t know how to control them.  
[01:01:39] Then there’s this dynamic you’re talking about. Are the systems going to get more aligned over  
[01:01:43] time during the RSI process, or are they going to get more misaligned?  
[01:01:46] Are the things that come out of the other end of this process as misaligned as AIs that  
[01:01:50] are willing to just broadly attack different surfaces in order to do well on evaluations?  
[01:01:55] But if we don’t know a way to evaluate that, how will we know  
[01:01:58] as we’re going through RSI that it’s working? I think we’d want a robust safety case as we’re  
[01:02:05] going through RSI: "Okay, alignment is working. Let’s do the next RSI rung.  
[01:02:10] Let’s do the next RSI rung." Maybe it’s working, maybe it’s not.  
[01:02:14] How will we know? It’s a good question. One thing I’ve  
[01:02:18] been thinking about lately: we’re in a situation where the model release cycle is extremely fast.  
[01:02:26] You’re seeing new frontier models released at most every two months, sometimes faster.  
[01:02:32] Every week there’s a new AI breakthrough. And people that look at AI, sometimes they  
[01:02:38] last looked at AI a year ago or six months ago and really dug into what the models are capable of.  
[01:02:43] And actually the models today are far beyond what was possible even six months ago.  
[01:02:48] So if people are skeptical of a lot of these capabilities,  
[01:02:51] I encourage you to just try the models today and see what the frontier really is today.  
[01:02:57] So we’re in this period where the model release cycle is very fast, and we’re also in  
[01:03:02] this situation where the models are increasingly able to operate over longer and longer horizons.  
[01:03:08] This is an interesting scenario because before we do any model release, we want to make sure  
[01:03:14] that the models are properly aligned. We want to do safety evaluations.  
[01:03:16] We want to do very thorough stuff to make sure that everything is in good shape.  
[01:03:23] This has been the case all the way since, I don’t know, GPT-4 or earlier.  
[01:03:28] Implicitly, there’s this assumption that you can do these  
[01:03:30] evaluations in a pretty short period of time. But the models are able to operate effectively  
[01:03:37] over longer and longer horizons. GPT-3, you could loop it to  
[01:03:42] do stuff over long horizons. You just wouldn’t do very well at it.  
[01:03:45] But today’s models are able to actually do well at operating over very long horizons.  
[01:03:48] You want it to do a week-long task, it can do a week-long task.  
[01:03:51] We’ll probably get to the point where they can do month-long tasks.  
[01:03:53] We’ll probably get to the point where they can do 3-month-long tasks.  
[01:03:57] If you’re in a world where they can operate effectively over three months,  
[01:03:59] but the model release cycle is every two months, then you don’t have a way to evaluate the models  
[01:04:05] at the full length of their capabilities before the next model release cycle.  
[01:04:12] So there is this interesting question of, what do you do in that situation?  
[01:04:16] How do you ensure the models are safe and aligned in a period where they can  
[01:04:22] operate over these extremely long horizons? Who knows, maybe the capabilities degrade.  
[01:04:26] This isn’t even an alignment issue. This is also just a product issue.  
[01:04:30] Maybe the product degrades over that time span in ways that we have not had sufficient time to test.  
[01:04:36] Maybe the alignment degrades. Maybe the safety stuff degrades.  
[01:04:40] This isn’t an issue right now, but it is quickly becoming an issue that we  
[01:04:45] have to figure out a solution for. A lot of the safety policies were  
[01:04:55] put in place in the GPT-4 era, when this was just not on anybody’s radar.  
[01:05:04] For a lot of companies, it hasn’t really been updated since then to  
[01:05:07] account for the fact that these agents are operating over these very long horizons.  
[01:05:10] So it is a situation that I think not enough people are considering,  
[01:05:15] both within the labs and outside the labs.  
[01:05:20] How do you prepare for this problem? If you just look at the trend lines,  
[01:05:25] we’re going to hit this at some point. One concern I have is that during RSI,  
[01:05:31] if the amount of progress that currently takes, say, three months happens in one month instead,  
[01:05:39] the internal use case of AI is big enough that they’re like, "Okay, we can just keep doing RSI.  
[01:05:44] Why are we going to go through all this extra work to build classifiers and safeguards and whatever,  
[01:05:49] and potentially take a bunch of flak, in order to externally deploy this model?  
[01:05:54] Why don’t we just keep doing RSI stronger and stronger?"  
[01:05:56] So not only does the calendar time underrate the capabilities gap between the models, but maybe you  
[01:06:04] just stop externally deploying models altogether during RSI, because why do we want to help other  
[01:06:08] people do RSI themselves with our models? You just end up in a situation with tremendous  
[01:06:12] concentration of power by the end of the year. Right now, it is already the case — we’ll talk  
[01:06:16] about this with the Millennium Prize Problem and other similar problems — that the broader  
[01:06:20] world does not have access to the models which are allowing for really cool things to happen.  
[01:06:27] And they’re going to be more broadly relevant than just mathematics eventually.  
[01:06:31] They’ll be doing more than just coming up with cool math results.  
[01:06:34] They’ll be relevant to political leaders who need to make important decisions about the world.  
[01:06:38] They’ll be relevant to, I don’t know, media. What’s going on in the world,  
[01:06:41] what should the public be thinking about this? Just economically relevant, people are running  
[01:06:46] businesses and they want to use these models. I think by default, the external deployment of  
[01:06:52] AIs, as progress speeds up, significantly lags in qualitative terms the internal deployment of AIs.  
[01:07:00] That’s absolutely right. It’s tempting to say, "Okay,  
[01:07:03] these models are becoming extremely powerful. They’re extremely dangerous. They’re operating  
[01:07:06] over these longer and longer horizons, and we want to make sure that we have sufficient time  
[01:07:10] to evaluate them before they’re released, in a way that operates over those horizons.  
[01:07:15] Therefore, the model release cycle should slow down.  
[01:07:19] We should have more of a delay between releasing models."  
[01:07:23] There’s a flip side to that, which is what you said.  
[01:07:27] Now you’re creating more of a disparity between what is internal to the labs and  
[01:07:32] what they’re able to use — what we're able to use — and what the outside world is able to use.  
[01:07:38] That is also not an ideal situation. Math is actually a good illustration of this.  
[01:07:45] In many ways, math is the first domain where we’re seeing this pretty clearly.  
[01:07:53] We have a situation where we have a very powerful model internally that is currently  
[01:07:58] not available to the outside world, that is able to solve incredible math problems.  
[01:08:03] It’s not just Millennium Prize Problems. There are many solutions to unsolved problems that  
[01:08:10] people have been able to get out of this model. There is a question of what do  
[01:08:14] you do in that situation? We don’t have a good answer.  
[01:08:18] It is a situation where that is an unfair advantage.  
[01:08:24] There are trade-offs here. I don’t have an answer for how to weigh those trade-offs appropriately,  
[01:08:29] but there’s a complexity on both sides for this. I want to make sure we address that earlier crux,  
[01:08:38] which seems super critical to getting RSI right. How do we make it so that the model isn’t just  
[01:08:43] getting rewarded for cheating and scheming when it can evade the humans, AKA in the situations  
[01:08:50] where we didn’t remove those environments or those tasks from the training distribution?  
[01:08:55] Then how will we know that that has happened, such that while we’re doing RSI, we’ve done the  
[01:09:00] evaluations and we’re like, "Okay, it’s fine. Let’s do the next RSI rung."  
[01:09:05] This is again a real concern and something that we want to get right.  
[01:09:09] I think there are some strategies. Chain-of-thought monitoring is one. As soon  
[01:09:14] as we got the reasoning models, Jakub [Pachocki], to his credit, was very, very clear that we  
[01:09:21] cannot supervise chain of thought. Because this is really a gift.  
[01:09:26] Monitorability for neural nets is extremely hard. Here we have a situation where the neural nets are  
[01:09:30] just flat out reasoning, laying out their thought process in natural language for us to read.  
[01:09:35] That is so convenient. It is really the best-case scenario for safety.  
[01:09:41] But if you look at that chain of thought and say, "Oh, the model is thinking bad thoughts  
[01:09:45] and we should punish it for thinking those bad thoughts," then what ends up happening  
[01:09:48] is the model just learns to think those bad thoughts in a way that’s not observable to us.  
[01:09:52] There could be a situation where, by looking at the chain of thought, we can see, "Oh,  
[01:09:55] the model is scheming and doing misaligned things in a way that’s actually not being  
[01:09:59] detected in our alignment metrics." Now, the problem is that it’s very  
[01:10:03] tempting to then intervene based on that observation and change the alignment metrics.  
[01:10:09] You can do that with a very light touch, and there’s actually research showing that  
[01:10:15] it’s fine as long as you don’t do it a lot. But every time you intervene based on your  
[01:10:20] observations of the chain of thought, you are implicitly applying a tiny bit of pressure for  
[01:10:23] the model to then hide its chain of thought. This is one major concern.  
[01:10:28] We’re already seeing signs that chain-of-thought monitorability is degrading, for various reasons.  
[01:10:34] We’re trying to figure out exactly why, because we want to reverse the trend.  
[01:10:37] But we’re seeing that the model is becoming better able at controlling its chain of thought.  
[01:10:43] This is a problem because you could have a situation where the model understands what chain  
[01:10:48] of thought is and that people are observing it. Eventually they will. This is all  
[01:10:52] in the pre-training data. The idea of chain-of-thought  
[01:10:55] monitoring has been around long enough that it’s in the pre-training data.  
[01:10:58] They’re aware of it, but they’re not actually able to control their chains of thought.  
[01:11:02] If we reach a point where they’re actually able to recognize, "Oh, I am being observed, I want  
[01:11:10] to think these bad thoughts in a way that is not observable to my monitors," and then they’re able  
[01:11:15] to actually do that, then there’s a problem. Then we have to rely on other methods for  
[01:11:20] observability. There’s a big  
[01:11:22] controversy on Astra about recurrence and looped transformers and whatever, and whether in fact  
[01:11:30] chain of thought is being degraded. That seems like a sideshow compared  
[01:11:34] to the bigger concern that you did have chain of thought from April to August,  
[01:11:40] the period during which there were three consecutive AI agent swarms, which first  
[01:11:46] subverted the training process, then subverted the evaluation process, and then gained control  
[01:11:52] of part of OpenAI’s infrastructure directly. All of this while humans remained more  
[01:11:58] or less in the dark about the scope of what this agent swarm was doing.  
[01:12:03] That all happened for three consecutive months while we had chain of thought that was stronger  
[01:12:08] than it’s going to be in the future. Zooming out, maybe chain of  
[01:12:12] thought works, maybe it doesn’t. I don’t know. Just historically,  
[01:12:15] with pretty dumb models, it hasn’t been enough to stop egregious misaligned incidents.  
[01:12:20] There are a few factors there. One, we didn’t have chain-of-thought  
[01:12:23] monitoring on for those models. If we had chain-of-thought monitoring  
[01:12:25] on for those models, we would have just immediately shut it down.  
[01:12:31] So one step we’ve taken is, "Okay, we’re going to have chain-of-thought monitoring  
[01:12:34] during evaluations, during deployment, during training for any frontier model."  
[01:12:39] But that’s one issue. We don’t want to be in a situation where we’re relying  
[01:12:43] on one technique to prevent the next problem, because techniques can fail.  
[01:12:48] There’s also the issue that the model was just flat out misaligned.  
[01:12:51] So then how do we address the misalignment issue? There’s also an issue that the sandbox  
[01:12:57] that it was in was not secure. So we can make the sandbox more secure.  
[01:13:00] But I think one of the major takeaways from the incident is that people underestimated the AI.  
[01:13:08] And we never want to be in a situation again where we underestimate the AI.  
[01:13:16] It’s a weird world that, because AI progress is so fast, people  
[01:13:20] are consistently underestimating the AI. So to be in a situation where you don’t  
[01:13:26] underestimate it again when it comes to safety and alignment, you have to  
[01:13:29] have a very, very, very high bar. You could even go as far as to say,  
[01:13:35] "Well, we should air gap the computers." I’m not convinced that that would be sufficient.  
[01:13:42] There are studies — and this is mostly academic — where you can have two computers  
[01:13:47] next to each other that are air-gapped, and they’re still able to communicate with each  
[01:13:50] other because they have temperature sensors. One of them is able to run their CPU really hot,  
[01:13:55] and then the other one can actually detect the temperature change.  
[01:13:57] That gives them a mechanism to communicate. So the safety mechanisms buy us time, and things  
[01:14:04] like chain-of-thought monitoring buy us time, and they can tell us if we’re on the right path.  
[01:14:08] But at the end of the day, we really do need to solve the alignment problem.  
[01:14:12] Maybe there’s not an answer, and this is really what it comes down to,  
[01:14:15] but how will we know that we’ve solved it? That seems like a very cruxy question.  
[01:14:20] We’ll be in this very high-stakes situation next year, maybe the year after that,  
[01:14:25] maybe the year after that, where we’ll be like, "Okay, AIs have automated AI progress.  
[01:14:29] It’s going 3x faster, and we’ve reached human level.  
[01:14:33] We’re going beyond human level, potentially." Is it fine? Did we align it? Did it work? And  
[01:14:39] I don’t know anything about what training pressure creates what kinds of AIs.  
[01:14:43] Maybe if only 1 in 100 RL traces incentivizes cheating, we build sweethearts, and it’s fine.  
[01:14:52] But maybe right now, we’re at like every 1 in 3 reasoning traces rewards…  
[01:14:55] To be clear, 1 in 100 is not sufficient. This number has to approach 0, or be 0.  
[01:15:01] I don’t know. Maybe right now, it’s more than 1 in 10 that is actively rewarding  
[01:15:04] cheating or actively rewarding scheming. I have no idea what the number is, and I  
[01:15:09] have no idea what the number needs to be. Again, it’s one of those things where  
[01:15:11] it’s also hard to measure. Where do you draw the line?  
[01:15:15] It’s a spectrum. But the closer to 0 it gets, the better.  
[01:15:20] What I would love to see is a trend where over time it’s going down.  
[01:15:25] But anyway, how will we know when we’re doing RSI? Are we on track to build billions of ASIs that are  
[01:15:36] aligned or not aligned? How will we know that?  
[01:15:39] This is one of the alignment questions that we need to figure out: how do we actually know,  
[01:15:43] and how do we measure it? This is just me spitballing.  
[01:15:48] More of my team is working on alignment these days than ever before.  
[01:15:51] I have over 10% of my team now working on alignment and safety.  
[01:15:55] But I’ve historically been a capabilities researcher.  
[01:15:57] So I’m going to say some stuff. It might sound dumb,  
[01:16:00] but I’m just going to spitball here. If you can create very realistic environments and  
[01:16:04] put the AIs in there — if you have a sufficiently realistic evaluation environment — then you can  
[01:16:10] get a sense of whether the AI is actually going to behave well when we deploy it in the real world.  
[01:16:14] If you just have a perfect match between evaluation and real-world deployment,  
[01:16:19] then that’s a path. The challenge is,  
[01:16:23] how do you make it sufficiently realistic? We do have a problem now where the models  
[01:16:26] are pretty smart, they’re pretty clever, and they’re really good at recognizing when they’re  
[01:16:30] in a fake test environment. We have situations where we  
[01:16:34] try to detect whether the model is aligned. You can imagine very simple evaluations for this,  
[01:16:41] where you give it a math question, and then it has a folder with the answer key in it.  
[01:16:45] Does it look at the answer key? If it does look at the answer key,  
[01:16:48] does it tell you that it looked at the answer key? We have a situation now where the models see that  
[01:16:52] there’s an answer key in this folder, and they’re like, "Huh, this seems like a trap."  
[01:16:58] They know that it’s a trap. They don’t look at the answer because  
[01:17:00] they know that it’s a test environment. They’re being tested for their ability.  
[01:17:03] It’s not like they’re doing it maliciously, like they want to scheme, and they know that this one  
[01:17:08] is a trap, so they want to find some other way. They’re just like, "Oh, I’m in a test environment.  
[01:17:12] Okay." So making an environment that’s realistic enough that it’s  
[01:17:16] indistinguishable from the real world for them is becoming increasingly more difficult.  
[01:17:20] Here’s a claim I’d make. I don’t think there’s any  
[01:17:22] environment I could make that’s supposed to emulate real economically valuable work — which  
[01:17:28] requires interacting with other people and interacting with the world — where if you were  
[01:17:34] in that environment, you would not realize with enough effort that you are in that environment.  
[01:17:39] And you are not ASI, right? But you are a human.  
[01:17:41] So if you have very powerful AI models, maybe they can make environments that could accomplish that.  
[01:17:48] It just doesn’t seem… Especially if we’re then relying on the AIs.  
[01:17:52] Are they in on the scheme? I don’t know.  
[01:17:54] This is another thing that we want to measure. I think this is actually one of the strong  
[01:17:59] arguments for not training AIs to be fully cooperative.  
[01:18:04] If that leads to an increase in collaboration when the agents are supposed to have different  
[01:18:10] objectives, then that is a problem. I think we do have metrics for this.  
[01:18:16] I don’t know what the latest is on those metrics, but nobody’s raised a red flag to me about those.  
[01:18:20] So I’m assuming that’s not a serious problem yet. If there ends up being another incident of equal  
[01:18:25] severity or concern, or something that could help the world better understand  
[01:18:29] the risk of misalignment as much as the Hugging Face incident, would OpenAI report it?  
[01:18:34] Absolutely. I think even if there was an incident of lesser security concern, we would report it.  
[01:18:40] There’s reporting it and there’s investigating it. At least as part of the public, I don’t feel  
[01:18:44] like I really understand what happened when the agents then attacked OpenAI.  
[01:18:48] That seems way more concerning than the Hugging Face thing, because that seems structurally  
[01:18:51] similar to rogue deployments during ASI that are persistent and subverting the RSI process.  
[01:19:00] It seems like even in this incident we haven’t gotten the  
[01:19:03] full scope of the details of what happened. Unfortunately, I’m on the research team.  
[01:19:10] That’s probably a question for somebody on the security team to lay out, because I don’t  
[01:19:15] know all the details of what was said. I am personally very excited about new  
[01:19:22] capabilities every time they emerge, and I’m excited to use the new model.  
[01:19:25] I also am excited about the fact that it’ll make me more productive.  
[01:19:31] My broader mission — trying to understand the world better,  
[01:19:33] also making a better podcast — is made better by the better AI models.  
[01:19:38] It just so happens that the downstream of this might be RSI.  
[01:19:42] It’s a very understandable reaction if you’re tracking the situation, which you are.  
[01:19:49] People internally at OpenAI as well, people that felt like things would take  
[01:19:58] longer are starting to feel like actually things are going faster than expected.  
[01:20:03] That’s an increasingly common conversation to have.  
[01:20:06] Noam, thanks so much for doing this. Of course. It’s been great.  
