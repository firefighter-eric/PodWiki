# Demis Hassabis — Scaling, superhuman AIs, AlphaZero atop LLMs, AlphaFold

[00:00:44] Today it is a true honor to speak with Demis Hassabis, who is the CEO of DeepMind. Demis,  
[00:00:50] welcome to the podcast. Thanks for having me.  
[00:00:52] First question, given your neuroscience background, how do you think about intelligence?  
[00:00:56] Specifically, do you think it’s one higher-level general reasoning circuit, or do you think it’s  
[00:01:01] thousands of independent subskills and heuristics? It’s interesting because intelligence is so  
[00:01:09] broad and what we use it for is so generally applicable. I think that suggests there must  
[00:01:17] be high-level common algorithmic themes around how the brain processes the world  
[00:01:26] around us. Of course, there are specialized parts of the brain that do specific things,  
[00:01:34] but I think there are probably some underlying principles that underpin all of that.  
[00:01:38] How do you make sense of the fact that in these LLMs, when you give them a lot  
[00:01:42] of data in any specific domain, they tend to get asymmetrically better in  
[00:01:45] that domain. Wouldn’t we expect a general improvement across all the different areas?  
[00:01:51] First of all, I think you do sometimes get surprising improvement in other domains when  
[00:01:56] you improve in a specific domain. For example, when these large models improve at coding,  
[00:02:02] that can actually improve their general reasoning. So there is evidence of some transfer although we  
[00:02:08] would like a lot more evidence of that. But that’s how the human brain learns too. If  
[00:02:14] we experience and practice a lot of things like chess, creative writing, or whatever,  
[00:02:20] we also tend to specialize and get better at that specific thing even though we’re using  
[00:02:25] general learning techniques and general learning systems in order to get good at that domain.  
[00:02:31] What’s been the most surprising example of this kind of transfer for you? Will you  
[00:02:35] see language and code, or images and text? I’m hoping we’re going to see a lot more of  
[00:02:41] this kind of transfer, but I think things like getting better at coding and math,  
[00:02:46] and then generally improving your reasoning. That is how it works with us as human learners.  
[00:02:51] But I think it’s interesting seeing that in these artificial systems.  
[00:02:55] And can you see the sort of mechanistic way, in the language and code example,  
[00:03:01] in which you’ve found the place in a neural network that’s getting better  
[00:03:03] with both the language and the code? Or is that too far down the weeds?  
[00:03:07] I don’t think our analysis techniques are quite sophisticated enough to be able to hone in on  
[00:03:12] that. I think that’s actually one of the areas where a lot more research needs to be done,  
[00:03:17] the kind of mechanistic analysis of the representations that these systems build  
[00:03:21] up. I sometimes like to call it virtual brain analytics. In a way, it’s a bit like doing fMRI,  
[00:03:28] or single-cell recording from a real brain. What are the analogous analysis techniques for these  
[00:03:34] artificial minds? There’s a lot of great work going on in this sort of stuff. People like  
[00:03:39] Chris Olah, I really like his work. I think a lot of computational neuroscience techniques can be  
[00:03:44] brought to bear on analyzing the current systems we’re building. In fact, I try to  
[00:03:49] encourage a lot of my computational neuroscience friends to start thinking in that direction and  
[00:03:54] applying their know-how to the large models. What do other AI researchers not understand  
[00:04:01] about human intelligence that you have some sort of insight on, given your neuroscience background?  
[00:04:06] I think neuroscience has added a lot, if you look at the last 10-20 years that we’ve been at it.  
[00:04:14] I’ve been thinking about this for 30+ years. In the earlier days of the new wave of AI,  
[00:04:21] neuroscience was providing a lot of interesting directional clues,  
[00:04:26] things like reinforcement learning and combining that with deep learning. Some of our pioneering  
[00:04:30] work we did there were things like experience replay and even the notion of attention,  
[00:04:35] which has become super important. A lot of those original inspirations came from some understanding  
[00:04:42] about how the brain works, although not the exact specifics of course. One is an engineered  
[00:04:46] system and the other one’s a natural system. It’s not so much about a one-to-one mapping  
[00:04:50] of a specific algorithm, but more so inspirational direction. Maybe it’s some ideas for architecture,  
[00:04:55] or algorithmic ideas, or representational ideas. The brain is an existence proof that  
[00:05:01] general intelligence is possible at all. I think the history of human endeavors has been such that  
[00:05:07] once you know something’s possible it’s easier to push hard in that direction, because you know it’s  
[00:05:12] a question of effort, a question of when and not if. That allows you to make progress a lot more  
[00:05:19] quickly. So I think neuroscience has inspired a lot of the thinking, at least in a soft way,  
[00:05:28] behind where we are today. As for going forward, I think there’s still a lot of interesting things  
[00:05:36] to be resolved around planning. How does the brain construct the right world models? I  
[00:05:43] studied how the brain does imagination, or you can think of it as mental simulation. How do we  
[00:05:50] create very rich visual spatial simulations of the world in order for us to plan better?  
[00:05:56] Actually, I’m curious how you think that will interface with LLMs. Obviously, DeepMind is  
[00:06:00] at the frontier and has been for many years with systems like AlphaZero and so forth, having these  
[00:06:05] agents which can think through different steps to get to an end outcome. Is there a path for  
[00:06:11] LLMs to have this tree search kind of thing on top of them? How do you think about this?  
[00:06:15] I think that’s a super promising direction. We’ve got to carry on improving the large models. We’ve  
[00:06:22] got to carry on making them more and more accurate predictors of the world, making them more and  
[00:06:29] more reliable world models. That’s clearly a necessary, but probably insufficient component  
[00:06:34] of an AGI system. On top of that, we’re working on things like AlphaZero-like planning mechanisms  
[00:06:42] on top that make use of that model in order to make concrete plans to achieve certain goals  
[00:06:47] in the world. Perhaps chaining thought, lines of reasoning, together and using search to explore  
[00:06:56] massive spaces of possibility. I think that’s kind of missing from our current large models.  
[00:07:01] How do you get past the immense amount of compute that these approaches tend to  
[00:07:06] require? Even the AlphaGo system was a pretty expensive system because you sort of had to run  
[00:07:12] an LLM on each node of the tree. How do you anticipate that’ll get made more efficient?  
[00:07:18] One thing is Moore’s law tends to help. Over every year more computation comes in. But we focus a lot  
[00:07:28] on sample-efficient methods and reusing existing data, things like experience replay and also just  
[00:07:37] looking at more efficient ways. The better your world model is, the more efficient your search  
[00:07:42] can be. One example I always give is AlphaZero, our system to play Go and chess and any game.  
[00:07:48] It’s stronger than human world champion level in all these games and it uses a lot less search than  
[00:07:56] a brute force method like Deep Blue to play chess. One of these traditional Stockfish or  
[00:08:02] Deep Blue systems would maybe look at millions of possible moves for every decision it’s going  
[00:08:07] to make. AlphaZero and AlphaGo may look at around tens of thousands of possible positions in order  
[00:08:16] to make a decision about what to move next. A human grandmaster or world champion probably  
[00:08:21] only looks at a few hundred moves, even the top ones, in order to make their very good decision  
[00:08:27] about what to play next. So that suggests that the brute force systems don’t have any  
[00:08:32] real model other than the heuristics about the game. AlphaGo has quite a decent model but the  
[00:08:41] top human players have a much richer, much more accurate model of Go or chess. That allows them  
[00:08:47] to make world-class decisions on a very small amount of search. So I think there’s a sort of  
[00:08:53] trade-off there. If you improve the models, then I think your search can be more efficient and  
[00:08:58] therefore you can get further with your search. I have two questions based on that. With AlphaGo,  
[00:09:04] you had a very concrete win condition: at the end of the day, do I win this game of Go or not? You  
[00:09:08] can reinforce on that. When you’re thinking of an LLM putting out thought, do you think there  
[00:09:14] will be this ability to discriminate in the end, whether that was a good thing to reward or not?  
[00:09:20] Of course that’s why we pioneered, and what DeepMind is sort of famous for,  
[00:09:24] using games as a proving ground. That’s partly because it’s efficient to research in that domain.  
[00:09:30] The other reason is, obviously, it’s extremely easy to specify a reward function. Winning the  
[00:09:34] game or improving the score, something like that is built into most games. So that is one of the  
[00:09:40] challenges of real-world systems. How does one define the right objective function, the right  
[00:09:44] reward function, and the right goals? How does one specify them in a general way, but specific enough  
[00:09:52] that one actually points the system in the right direction? For real-world problems, that can be a  
[00:09:58] lot harder. But actually, if you think about it in even scientific problems, there are usually ways  
[00:10:04] that you can specify the goal that you’re after. When you think about human intelligence,  
[00:10:08] you were just saying that humans thinking about these thoughts are just super sample-efficient.  
[00:10:13] Einstein coming up with relativity, right? There’s thousands of possible permutations  
[00:10:16] of the equations. Do you think it’s also this sense of different heuristics like,  
[00:10:20] “I’m going to try out this approach instead of this”? Or is it a totally different way of  
[00:10:24] approaching and coming up with that solution than what AlphaGo does to plan the next move?  
[00:10:29] I think it’s different because our brains are not built for doing Monte Carlo tree search. It’s  
[00:10:35] just not the way our organic brains work. I think that people like Einstein, in order to compensate  
[00:10:42] for that, have used their intuition—and maybe we can come to what intuition is—and their knowledge  
[00:10:51] and their experience to build in Einstein’s case, extremely accurate models of physics that include  
[00:10:58] mental simulations. If you read about Einstein and how he came up with things, he used to visualize  
[00:11:03] and really feel what these physical systems should be like, not just the mathematics of  
[00:11:10] it. He had a really intuitive feel for what they would be like in reality. That allowed him to  
[00:11:15] think these thoughts that were very outlandish at the time. So I think that that gets to the  
[00:11:20] sophistication of the world models that we’re building. Imagine your world model can get you  
[00:11:26] to a certain node in a tree that you’re searching, and then you just do a little bit of search around  
[00:11:31] that leaf node and that gets you to these original places. Obviously, if your model and your judgment  
[00:11:38] on that model is very, very good, then you can pick which leaf nodes you should expand  
[00:11:43] with search much more accurately. So overall, you therefore do a lot less search. I mean, there’s  
[00:11:48] no way that any human could do a kind of brute force search over any kind of significant space.  
[00:11:56] A big open question right now is whether RL will allow these models to use the self-play  
[00:12:00] synthetic data to get over data bottlenecks. It sounds like you’re optimistic about this?  
[00:12:04] I’m very optimistic about that. First of all, there’s still a lot more data that can be used,  
[00:12:09] especially if one views multimodal and video and these kinds of things. Obviously,  
[00:12:15] society is adding more data all the time to the Internet and things like that. I think that  
[00:12:22] there’s a lot of scope for creating synthetic data. We’re looking at that in different ways,  
[00:12:28] partly through simulation, using very realistic game environments, for example,  
[00:12:32] to generate realistic data, but also self-play. That’s where systems interact with each other  
[00:12:41] or converse with each other. It worked very well for us with AlphaGo and AlphaZero where we got the  
[00:12:47] systems to play against each other and actually learn from each other’s mistakes and build up a  
[00:12:51] knowledge base that way. I think there are some good analogies for that. It’s a little bit more  
[00:12:55] complicated to build a general kind of world data. How do you get to the point with these  
[00:13:01] models where the synthetic data they’re outputting on the self-play they’re doing  
[00:13:05] is not just more of what’s already in their data set, but something they haven’t seen  
[00:13:09] before? To actually improve the abilities. I think there’s a whole science needed there.  
[00:13:16] I think we’re still in the nascent stage of this, of data curation and data analysis and  
[00:13:20] actually analyzing the holes that you have in your data distribution. This is important for  
[00:13:25] things like fairness and bias and other stuff. To remove that from the system is to really make  
[00:13:30] sure that your data set is representative of the distribution you’re trying to learn.  
[00:13:35] There are many tricks there one can use, like overweighting or replaying certain parts of the  
[00:13:39] data. Or if you identify some gap in your data set, you could imagine that’s where you put your  
[00:13:45] synthetic generation capabilities to work on. Nowadays, people are paying attention to the RL  
[00:13:52] stuff that DeepMind did many years before. What are the early research directions, or something  
[00:13:58] that was done way back in the past, that you think will be a big deal but people just haven’t been  
[00:14:02] paying attention to it? There was a time where people weren’t paying attention to scaling. What’s  
[00:14:05] the thing now that is totally underrated? Well, I think that the history of the last  
[00:14:10] couple of decades has been things coming in and out of fashion, right? A while ago,  
[00:14:16] maybe five-plus years ago, we were pioneering with AlphaGo and before that DQN. It was the  
[00:14:21] first system that worked on Atari, our first big system really more than ten years ago now,  
[00:14:26] that scaled up Q-learning and reinforcement learning techniques and combined that with deep  
[00:14:31] learning to create deep reinforcement learning. We used that to scale up to master some pretty  
[00:14:38] complex tasks like playing Atari games just from the pixels. I do actually think a lot of those  
[00:14:44] ideas need to come back in again and, as we talked about earlier, combine them with the new advances  
[00:14:50] in large models and large multimodal models, which are obviously very exciting as well. So I do think  
[00:14:54] there’s a lot of potential for combining some of those older ideas together with the newer ones.  
[00:15:00] Is there any potential for the AGI to eventually come from a pure RL approach? The way we’re  
[00:15:07] talking about it, it sounds like the LLM will form the right prior and then this sort of tree search  
[00:15:13] will go on top of that. Or is it a possibility that it comes completely out of the dark?  
[00:15:17] Theoretically, I think there’s no reason why you couldn’t go full AlphaZero-like on it. There are  
[00:15:21] some people here at Google DeepMind and in the RL community who work on that, fully assuming no  
[00:15:30] priors, no data, and just building all knowledge from scratch. I think that’s valuable because  
[00:15:39] those ideas and those algorithms should also work when you have some knowledge too. Having  
[00:15:43] said that, I think by far the quickest way to get to AGI, and the most plausible way,  
[00:15:49] is to use all the knowledge that’s existing in the world right now that we’ve collected from things  
[00:15:53] like the Web. We have these scalable algorithms, like transformers, that are capable of ingesting  
[00:16:01] all of that information. So I don’t see why you wouldn’t start with a model as a kind of prior,  
[00:16:07] or to build on it and to make predictions that help bootstrap your learning. I just think it  
[00:16:13] doesn’t make sense not to make use of that. So my betting would be that the final AGI system will  
[00:16:20] have these large multimodal models as part of the overall solution, but they probably  
[00:16:27] won’t be enough on their own. You’ll need this additional planning search on top.  
[00:16:31] This sounds like the answer to the question I’m about to ask. As somebody who’s been in  
[00:16:36] this field for a long time and seen different trends come and go, what do you think the  
[00:16:40] strong version of the scaling hypothesis gets right and what does it get wrong? The idea that  
[00:16:44] you just throw enough compute at a wide enough distribution of data and you get intelligence.  
[00:16:47] My view is that this is kind of an empirical question right now. I think it was pretty  
[00:16:51] surprising to almost everyone, including the people who first worked on the scaling hypotheses,  
[00:16:56] how far it’s gone. In a way, I look at the large models today and I think they’re almost  
[00:17:02] unreasonably effective for what they are. I think it’s pretty surprising some of the properties that  
[00:17:07] emerge. In my opinion, they’ve clearly got some form of concepts and abstractions and things  
[00:17:14] like that. I think if we were talking five-plus years ago, I would have said to you that maybe  
[00:17:18] we need an additional algorithmic breakthrough in order to do that, maybe more like how the  
[00:17:24] brain works. I think that’s still true if we want explicit abstract concepts, neat concepts,  
[00:17:29] but it seems that these systems can implicitly learn that. Another really interesting, unexpected  
[00:17:34] thing was that these systems have some sort of grounding even though they don’t experience the  
[00:17:39] world multimodally, at least until more recently when we have the multimodal models. The amount of  
[00:17:46] information and models that can be built up just from language is surprising. I think that I’d  
[00:17:51] have some hypotheses about why that is. I think we get some grounding through the RLHF feedback  
[00:17:56] systems because obviously the human raters are by definition, grounded people. We’re grounded in  
[00:18:03] reality, so our feedback is also grounded. Perhaps there’s some grounding coming in through there.  
[00:18:08] Also if you’re able to ingest all of it, maybe language contains more grounding than linguists  
[00:18:16] thought before. So it actually raises some very interesting philosophical questions that people  
[00:18:20] haven’t even really scratched the surface of yet. Looking at the advances that have been made,  
[00:18:27] it’s quite interesting to think about where it’s going to go next. In terms of your question of  
[00:18:31] large models, I think we’ve got to push scaling as hard as we can and that’s what we’re doing here.  
[00:18:38] It’s an empirical question, whether that will hit an asymptote or a brick wall, and there are  
[00:18:42] different people who argue about that. I think we should just test it. I think no one knows.  
[00:18:47] In the meantime, we should also double down on innovation and invention. This is something where  
[00:18:54] Google Research and DeepMind and Google Brain have pioneered many, many things over the last decade.  
[00:19:00] That’s our bread and butter. You can think of half our effort as having to do with scaling and  
[00:19:06] half our efforts having to do with inventing the next architectures and the next algorithms that  
[00:19:10] will be needed, knowing that larger and larger scaled models are coming down the line. So my  
[00:19:17] betting right now, but it’s a loose betting, is that you need both. I think you’ve got to push  
[00:19:24] both of them as hard as possible and we’re in a lucky position that we can do that.  
[00:19:27] I want to ask more about the grounding. You can imagine two things that might change which would  
[00:19:31] make the grounding more difficult. One is that as these models get smarter, they are going to  
[00:19:35] be able to operate in domains where we just can’t generate enough human labels, just because we’re  
[00:19:39] not smart enough. If it does a million-line pull request, how do we tell it, for example,  
[00:19:44] this is within the constraints of our morality and the end goal we wanted and this isn’t? The  
[00:19:49] other thing has to do with what you were saying about compute. So far we’ve been doing next token  
[00:19:53] prediction and in some sense it’s a guardrail, because you have to talk as a human would talk  
[00:19:57] and think as a human would think. Now, additional compute is maybe going to come in the form of  
[00:20:03] reinforcement learning where it’s just getting to the objective and we can’t really trace how  
[00:20:06] you got there. When you combine those two, how worried are you that the grounding goes away?  
[00:20:13] I think if it’s not properly grounded, the system won’t be able to achieve those goals properly. In  
[00:20:22] a sense, you have to have some grounding for a system to actually achieve goals in the real  
[00:20:27] world. I do actually think that these systems, and things like Gemini, are becoming more multimodal.  
[00:20:34] As we start ingesting things like video and audiovisual data as well as text data, then the  
[00:20:42] system starts correlating those things together. I think that is a form of proper grounding. So  
[00:20:50] I do think our systems are going to start to understand the physics of the real world better.  
[00:20:56] Then one could imagine the active version of that as a very realistic simulation or  
[00:21:00] game environment where you’re starting to learn about what your actions do in the world and how  
[00:21:07] that affects the world itself. The world stays itself, but it also affects what next learning  
[00:21:12] episode you’re getting. So these RL agents we’ve always been working on and pioneered,  
[00:21:17] like AlphaZero and AlphaGo, actually are active learners. What they decide to do  
[00:21:22] next affects what next learning piece of data or experience they’re going to get. So there’s  
[00:21:27] this very interesting sort of feedback loop. And of course, if we ever want to be good at  
[00:21:30] things like robotics, we’re going to have to understand how to act in the real world.  
[00:21:35] So there’s grounding in terms of whether the capabilities will be able to proceed,  
[00:21:39] whether they will be enough in touch with reality to do the things we want. There’s  
[00:21:43] another sense of grounding in that we’ve gotten lucky that since they’re trained on human thought,  
[00:21:47] they maybe think like a human. To what extent does that stay true when more of the compute for  
[00:21:52] training comes from just “did you get the right outcome” and it’s not guardrailed by “are you  
[00:21:57] proceeding on the next token as a human would?” Maybe the broader question I’ll pose to you is,  
[00:22:01] and this is what I asked Shane as well, what would it take to align a system that’s smarter  
[00:22:04] than a human? Maybe it thinks in alien concepts and you can’t really monitor the million-line pull  
[00:22:09] request because you can’t really understand the whole thing and you can’t give labels.  
[00:22:13] This is something Shane and I, and many others here, have had at the forefront of our minds since  
[00:22:17] before we started DeepMind because we planned for success. In 2010, no one was thinking about AI let  
[00:22:23] alone AGI. But we already knew that if we could make progress with these systems and these ideas,  
[00:22:30] the technology created would be unbelievably transformative. So we were already thinking  
[00:22:35] 20 years ago about what the consequences of that would be, both positive and negative. Of course,  
[00:22:40] the positive direction is amazing science, things like AlphaFold,  
[00:22:44] incredible breakthroughs in health and science, and mathematical and scientific discovery. But we  
[00:22:50] also have to make sure these systems are sort of understandable and controllable.  
[00:22:56] This will be a whole discussion in itself, but there are many, many ideas that people have  
[00:23:01] such as more stringent eval systems. I think we don’t have good enough evaluations and benchmarks  
[00:23:06] for things like if the system can deceive you. Can it exfiltrate its own code or do other undesirable  
[00:23:11] behaviors? There are also ideas of using AI, not general learning ones but maybe narrow AIs that  
[00:23:22] are specialized for a domain, to help us as the human scientists to analyze and summarize what the  
[00:23:29] more general system is doing. So there’s narrow AI tools. I think that there’s a lot of promise  
[00:23:35] in creating hardened sandboxes or simulations that are hardened with cybersecurity arrangements  
[00:23:44] around the simulation, both to keep the AI in and to keep hackers out. You could experiment  
[00:23:52] a lot more freely within that sandbox domain. There’s many, many other ideas, including the  
[00:24:00] analysis stuff we talked about earlier, where we can analyze and understand what the concepts  
[00:24:05] are that this system is building and what the representations are. So maybe then they’re not  
[00:24:08] so alien to us and we can actually keep track of the kind of knowledge that it’s building.  
[00:24:14] Stepping back a bit, I’m curious what your timelines are. So Shane  
[00:24:17] said his modal outcome is 2028. I think that’s maybe his median. What is yours?  
[00:24:23] I don’t have prescribed specific numbers to it because I think there’s so many unknowns  
[00:24:28] and uncertainties. Human ingenuity and endeavor comes up with surprises all the time. So that  
[00:24:35] could meaningfully move the timelines. I will say that when we started DeepMind back in 2010,  
[00:24:41] we thought of it as a 20-year project. And I think we’re on track actually, which is kind  
[00:24:46] of amazing for 20-year projects because usually they’re always 20 years away. That’s the joke  
[00:24:50] about whatever, quantum, AI, take your pick. But I think we’re on track. So I wouldn’t be surprised  
[00:24:58] if we had AGI-like systems within the next decade. Do you buy the model that once you have an AGI,  
[00:25:04] you have a system that basically speeds up further AI research? Maybe not in an overnight sense,  
[00:25:09] but over the course of months and years you would have much faster  
[00:25:11] progress than you would have otherwise had? I think that’s potentially possible. I think  
[00:25:15] it partly depends on what we, as a society, decide to use the first nascent AGI systems or  
[00:25:22] proto-AGI systems for. Even the current LLMs seem to be pretty good at coding and we have systems  
[00:25:31] like AlphaCode. We also have theorem proving systems. So one could imagine combining these  
[00:25:37] ideas together and making them a lot better. I could imagine these systems being quite good at  
[00:25:44] designing and helping us build future versions of themselves, but we also have to think about  
[00:25:49] the safety implications of that of course. I’m curious what you think about that. I’m  
[00:25:53] not saying this is happening this year, but eventually you’ll be developing a model where  
[00:25:58] you think there’s some chance that it’ll be capable of an intelligence explosion-like  
[00:26:03] dynamic once it’s fully developed. What would have to be true of that model at that point where  
[00:26:07] you’re comfortable continuing the development of the system? Something like, “I’ve seen these  
[00:26:10] specific evals, I’ve understood its internal thinking and its future thinking enough.”  
[00:26:18] We need a lot more understanding of the systems than we do today before I would even be confident  
[00:26:23] of explaining to you what we’d need to tick box there. I think what we’ve got to do in the next  
[00:26:28] few years, in the time before those systems start arriving, is come up with the right evaluations  
[00:26:35] and metrics. Ideally formal proofs, but it’s going to be hard for these types of systems, so at least  
[00:26:41] empirical bounds around what these systems can do. That’s why I think about things like deception as  
[00:26:49] being quite root node traits that you don’t want. If you’re confident that your system is exposing  
[00:26:57] what it actually thinks, then that opens up possibilities of using the system itself to  
[00:27:03] explain aspects of itself to you. The way I think about that is like this. If I were to play a game  
[00:27:09] of chess against Garry Kasparov, which I’ve played in the past, Magnus Carlsen, or the amazing chess  
[00:27:14] players of all time, I wouldn’t be able to come up with a move that they could. But they could  
[00:27:19] explain to me why they came up with that move and I could understand it post hoc, right? That’s the  
[00:27:27] sort of thing one could imagine. One of the capabilities that we could make use of these  
[00:27:34] systems is for them to explain it to us and even maybe get the proofs behind why they’re thinking  
[00:27:39] something, certainly in a mathematical problem. Got it. Do you have a sense of what the converse  
[00:27:45] answer would be? So what would have to be true where tomorrow morning you’re like “oh,  
[00:27:49] man, I didn’t anticipate this.” You see some specific observation tomorrow morning that  
[00:27:52] makes you say “we got to stop Gemini 2 training.” I could imagine that. This is where things like  
[00:27:59] the sandbox simulations are important. I would hope we’re experimenting in a safe,  
[00:28:04] secure environment when something very unexpected happens. There’s a new unexpected capability or  
[00:28:13] something that we didn’t want. We explicitly told the system we didn’t want it but then it  
[00:28:16] did and it lied about it. These are the kinds of things where one would want to then dig in  
[00:28:22] carefully. The systems that are around today are not dangerous, in my opinion, but in a few years  
[00:28:29] they might have potential. Then you would ideally pause and really get to the bottom of why it was  
[00:28:40] doing those things before one continued. Going back to Gemini, I’m curious what the  
[00:28:45] bottlenecks were in the development. Why not immediately make it one order  
[00:28:48] of magnitude bigger if scaling works? First of all, there are practical limits.  
[00:28:54] How much compute can you actually fit in one data center? You’re also bumping up against  
[00:29:00] very interesting distributed computing kind of challenges. Fortunately, we have some of  
[00:29:07] the best people in the world working on those challenges and cross data center training,  
[00:29:11] all of these kinds of things. There are very interesting hardware challenges and we have our  
[00:29:15] TPUs that we’re building and designing all the time as well as using GPUs. So there’s all of  
[00:29:22] that. Scaling laws also don’t just work by magic. You still need to scale up the hyperparameters,  
[00:29:30] and various innovations are going in all the time with each new scale. It’s not just about repeating  
[00:29:34] the same recipe at each new scale. You have to adjust the recipe and that’s a bit of an art  
[00:29:39] form. You have to sort of get new data points. If you try to extend your predictions and extrapolate  
[00:29:45] them several orders of magnitude out, sometimes they don’t hold anymore. There can be step  
[00:29:53] functions in terms of new capabilities and some things hold, other things don’t. Often you do need  
[00:30:00] those intermediate data points to correct some of your hyperparameter optimization and other things,  
[00:30:06] so that the scaling law continues to be true. So there are various practical limitations to that.  
[00:30:16] One order of magnitude is probably about the maximum that you want to do between each era.  
[00:30:24] That’s so fascinating. In the GPT-4 technical report, they say that they  
[00:30:27] were able to predict the training loss with a model with tens of thousands of times less  
[00:30:32] compute than GPT-4. They could see the curve. But the point you’re making is that the actual  
[00:30:36] capabilities that loss implies may not be so. Yeah, the downstream capabilities sometimes  
[00:30:40] don’t follow. You can often predict the core metrics like training loss or something like that,  
[00:30:45] but then it doesn’t actually translate into MMLU, or math, or some other actual capability that you  
[00:30:52] care about. They’re not necessarily linear all the time. There are non-linear effects there.  
[00:30:57] What was the biggest surprise to you during the development of  
[00:30:59] Gemini in terms of something like this happening? I wouldn’t say there was one big surprise. It was  
[00:31:06] very interesting trying to train things at that size and learning about all sorts of  
[00:31:12] things from an organizational standpoint, like how to babysit such a system and to  
[00:31:16] track it. There’s also things like getting a better understanding of the metrics you’re  
[00:31:22] optimizing versus the final capabilities that you want. I would say that’s still not a perfectly  
[00:31:28] understood mapping, but it’s an interesting one that we’re getting better and better at.  
[00:31:33] There’s a perception that maybe other labs are more compute-efficient than  
[00:31:38] DeepMind has been with Gemini. I don’t know what you make of that perception.  
[00:31:40] I don’t think that’s the case. I think that actually Gemini 1 used roughly the same amount  
[00:31:47] of compute, maybe slightly more, than what was rumored for GPT-4. I don’t know exactly what was  
[00:31:51] used but I think it was in the same ballpark. I think we’re very efficient with our compute  
[00:31:57] and we use our compute for many things. One is not just the scaling but, going back to earlier, more  
[00:32:02] innovations and ideas. A new innovation, a new invention, is only useful if it can also scale.  
[00:32:10] So you need quite a lot of compute to do new invention because you’ve got to test many things,  
[00:32:17] at least some reasonable scale, and make sure that they work at that scale. Also,  
[00:32:21] some new ideas may not work at a toy scale but do work at a larger scale. In fact,  
[00:32:26] those are the more valuable ones. So if you think about that exploration process,  
[00:32:30] you need quite a lot of compute to be able to do that. The good news is we’re pretty lucky  
[00:32:37] at Google. I think this year we’re going to have the most compute by far of any sort of research  
[00:32:42] lab. We hope to make very efficient and good use of that in terms of both scaling and the  
[00:32:47] capability of our systems and also new inventions. What’s been the biggest surprise to you, if you go  
[00:32:53] back to yourself in 2010 when you were starting DeepMind, in terms of what AI progress has looked  
[00:32:58] like? Did you anticipate back then that it would, in some large sense, amount to spending billions  
[00:33:03] of dollars into these models? Or did you have a different sense of what it would look like?  
[00:33:05] We thought that actually, and I know you’ve interviewed my colleague Shane. He always  
[00:33:11] thought in terms of compute curves and comparing it roughly to the brain,  
[00:33:17] how many neurons and synapses there are very loosely. Interestingly, we’re actually in that  
[00:33:21] kind of regime now with roughly the right order of magnitude of number of synapses in the brain  
[00:33:26] and the sort of compute that we have. But I think more fundamentally, we always thought that we bet  
[00:33:33] on generality and learning. So those were always at the core of any technique we would use. That’s  
[00:33:39] why we triangulated on reinforcement learning, and search, and deep learning as three types of  
[00:33:46] algorithms that would scale, be very general, and not require a lot of handcrafted human priors. We  
[00:33:55] thought that was the sort of failure mode of the efforts to build AI in the 90s in places like  
[00:34:01] MIT. There were very logic-based systems, expert systems, and masses of hand-coded,  
[00:34:07] handcrafted human information going into them that turned out to be wrong or too rigid. So we  
[00:34:12] wanted to move away from that and I think we spotted that trend early. Obviously, we used  
[00:34:18] games as our proving ground and we did very well with that. I think all of that was very successful  
[00:34:23] and maybe inspired others. AlphaGo, I think, was a big moment for inspiring many others to think “oh,  
[00:34:30] actually, these systems are ready to scale.” Of course then, with the advent of transformers,  
[00:34:34] invented by our colleagues at Google Research and Brain, that was the type of deep learning  
[00:34:40] that allowed us to ingest masses of amounts of information. That has really turbocharged where  
[00:34:47] we are today. So I think that’s all part of the same lineage. We couldn’t have predicted every  
[00:34:51] twist and turn there, but I think the general direction we were going in was the right one.  
[00:34:58] It’s fascinating if you read your old papers or Shane’s old papers. In Shane’s thesis in 2009,  
[00:35:03] he said “well, the way we would test for AI is, can you compress Wikipedia?” And that’s literally,  
[00:35:07] the loss function for LLMs. Or in your own paper in 2016 before transformers,  
[00:35:12] you were comparing neuroscience and AI and you said attention is what is needed.  
[00:35:17] Exactly. So we had these things called out and we had some early attention papers,  
[00:35:22] but they weren’t as elegant as transformers in the end, neural Turing machines and things  
[00:35:25] like this. Transformers were the nicer and more general architecture of that.  
[00:35:32] When you extrapolate all this out forward and you think about superhuman intelligence,  
[00:35:38] what does that landscape look like to you? Is it still controlled by a private company? What should  
[00:35:42] the governance of that look like concretely? I think that this is so consequential,  
[00:35:51] this technology. I think it’s much bigger than any one company or even industry in general.  
[00:35:57] I think it has to be a big collaboration with many stakeholders from civil society, academia,  
[00:36:03] government, etc. The good news is that with the popularity of the recent chatbot systems, I think  
[00:36:09] that has woken up many of these other parts of society to the fact that this is coming and what  
[00:36:13] it will be like to interact with these systems. And that’s great. It’s opened up lots of doors for  
[00:36:18] very good conversations. An example of that was the safety summit the UK hosted a few months ago,  
[00:36:24] which I thought was a big success in getting this international dialogue going. I think the whole of  
[00:36:30] society needs to be involved in deciding what we want to deploy these models for? How do we  
[00:36:35] want to use them and what do we not want to use them for? I think we’ve got to try and get some  
[00:36:38] international consensus around that and also make sure that these systems benefit everyone, for the  
[00:36:46] good of society in general. That’s why I push so hard for things like AI for science. I hope that  
[00:36:53] with things like our spin-out, Isomorphic, we’re going to start curing terrible diseases with AI,  
[00:36:58] accelerate drug discovery, tackle climate change, and do other amazing things. There are big  
[00:37:02] challenges that face humanity, massive challenges. I’m actually optimistic we can solve them because  
[00:37:09] we’ve got this incredibly powerful tool of AI coming down the line that we can apply to  
[00:37:15] help us solve many of these problems. Ideally, we would have a big consensus around that and a big  
[00:37:23] discussion at sort of the UN level if possible. One interesting thing is if you look at these  
[00:37:29] systems and chat with them, they’re immensely powerful and intelligent. But it’s interesting  
[00:37:35] the extent to which they haven’t automated large sections of the economy yet. Whereas if five years  
[00:37:39] ago I showed you Gemini, you’d be like “wow, this is totally coming for a lot of things.”  
[00:37:43] So how do you account for that? What’s going on that it hasn’t had the broader impact yet?  
[00:37:49] I think that just shows we’re still at the beginning of this new era. I think there are  
[00:37:55] some interesting use cases where you can use these chatbot systems to summarize stuff for you and do  
[00:38:05] some simple writing, maybe more boilerplate-type writing. But that’s only a small part of what we  
[00:38:12] all do every day. I think for more general use cases we still need new capabilities,  
[00:38:19] things like planning and search but also things like personalization and episodic memory. That’s  
[00:38:26] not just long context windows, but actually remembering what we spoke about 100 conversations  
[00:38:31] ago. I’m really looking forward to things like recommendation systems that help me find better,  
[00:38:39] more enriching material, whether that’s books or films or music and so on. I would use that type of  
[00:38:44] system every day. So I think we’re just scratching the surface of what these AI assistants could  
[00:38:51] actually do for us in our general, everyday lives and also in our work context as well. I think  
[00:38:57] they’re not reliable yet enough to do things like science with them. But I think one day,  
[00:39:01] once we fix factuality and grounding and other things, I think they could end up  
[00:39:05] becoming the world’s best research assistant for you as a scientist or as a clinician.  
[00:39:13] I want to ask about memory. You had this fascinating paper in 2007 where you talked  
[00:39:18] about the links between memory and imagination and how they, in some sense, are very similar. People  
[00:39:24] often claim that these models are just memorizing. How do you think about that claim? Is memorization  
[00:39:30] all you need because in some deep sense, that’s compression? What’s your intuition here?  
[00:39:35] At the limit, one maybe could try and memorize everything but it wouldn’t generalize out of your  
[00:39:39] distribution. The early criticisms of these early systems were that they were just regurgitating  
[00:39:48] and memorizing. I think clearly in the Gemini, GPT-4 type era, they are definitely generalizing  
[00:39:54] to new constructs. Actually my thesis, and that paper particularly that started that  
[00:40:02] area of imagination in neuroscience, was showing that first of all memory, at least human memory,  
[00:40:07] is a reconstructive process. It’s not a videotape. We sort of put it together back from components  
[00:40:12] that seem familiar to us, the ensemble. That’s what made me think that imagination might be the  
[00:40:17] same thing. Except in this case you’re using the same semantic components, but now you’re putting  
[00:40:21] it together in a way that your brain thinks is novel, for a particular purpose like planning. I  
[00:40:27] do think that that kind of idea is still probably missing from our current systems, pulling together  
[00:40:34] different parts of your world model to simulate something new that then helps with your planning,  
[00:40:41] which is what I would call imagination. For sure. Now you guys have the best models  
[00:40:45] in the world with the Gemini models. Do you plan on putting out some sort of framework  
[00:40:52] like the other two major AI labs have? Something like “once we see these specific capabilities,  
[00:40:56] unless we have these specific safeguards, we’re not going to continue development  
[00:41:00] or we’re not going to ship the product out.” Yes, we already have lots of internal checks  
[00:41:05] and balances but we’re going to start publishing. Actually, watch this space. We’re working on a  
[00:41:10] whole bunch of blog posts and technical papers that we’ll be putting out in the next few months  
[00:41:17] along similar lines of things like responsible scaling laws and so on. We have those implicitly  
[00:41:22] internally in various safety councils that people like Shane chair and so on. But it’s time for us  
[00:41:29] to talk about that more publicly I think. So we’ll be doing that throughout the course of the year.  
[00:41:33] That’s great to hear. Another thing I’m curious about is, there’s not only the risk  
[00:41:37] of the deployed model being something that people can use to do bad things,  
[00:41:41] but there’s also rogue actors, foreign agents, and so forth, being able to steal the weights  
[00:41:46] and then fine-tune them to do crazy things. How do you think about securing the weights to make sure  
[00:41:52] something like this doesn’t happen, making sure a very key group of people has access to them?  
[00:41:57] It’s interesting. First of all, there’s two parts. One is security, one is open source, which maybe  
[00:42:01] we can discuss. The security is super key just as normal cybersecurity type things. I think  
[00:42:08] we’re lucky at Google DeepMind. We’re behind Google’s firewall and cloud protection which I  
[00:42:14] think is best in class in the world corporately. So we already have that protection. Behind that,  
[00:42:20] we have specific DeepMind protections within our code base. It’s sort of a double layer  
[00:42:26] of protection. So I feel pretty good about that. You can never be complacent on that  
[00:42:31] but I feel it’s already the best in the world in terms of cyber defenses. We’ve got to carry  
[00:42:38] on improving that and again, things like the hardened sandboxes could be a way of doing that  
[00:42:43] as well. Maybe there are even specifically secure data centers or hardware solutions  
[00:42:49] to this too that we’re thinking about. I think that maybe in the next three, four, five years,  
[00:42:53] we would also want air gaps and various other things that are known in the security community.  
[00:42:58] So I think that’s key and I think all frontier labs should be doing that because otherwise for  
[00:43:02] rogue nation-states and other dangerous actors, there would obviously be a lot of incentive for  
[00:43:10] them to steal things like the weights. Of course, open source is another interesting question. We’re  
[00:43:16] huge proponents of open source and open science. We’ve published thousands of papers, things like  
[00:43:22] AlphaFold and transformers and AlphaGo. All of these things we put out there into the world,  
[00:43:28] published and open source, most recently GraphCast, our weather prediction system. But  
[00:43:33] when it comes to the general-purpose foundational technology, I think the question I would have for  
[00:43:44] open source proponents is, how does one stop bad actors, individuals or up to rogue states,  
[00:43:53] taking those same open source systems and repurposing them for harmful ends? We have to  
[00:44:00] answer that question. I don’t know what the answer is to that, but I haven’t heard a compelling,  
[00:44:07] clear answer to that from proponents of just open sourcing everything. So I think there  
[00:44:13] has to be some balance there. Obviously, it’s a complex question of what that is.  
[00:44:18] I feel like tech doesn’t get the credit it deserves for funding hundreds of billions of  
[00:44:22] dollars’ worth of R&D, obviously you have DeepMind with systems like AlphaFold and so on. When we  
[00:44:28] talk about securing the weights, as we said maybe right now it’s not something that is going to  
[00:44:33] cause the end of the world or anything, but as these systems get better and better, there’s the  
[00:44:36] worry that a foreign agent or something gets access to them. Presumably right now there’s  
[00:44:40] dozens to hundreds of researchers who have access to the weights. What’s a plan for getting the  
[00:44:46] weights in a situation room where if you need to access them it’s some extremely strenuous process  
[00:44:52] and no individual can really take them out? One has to balance that with allowing for  
[00:44:57] collaboration and speed of progress. Another interesting thing is that of course you want  
[00:45:03] brilliant independent researchers from academia or things like the UK AI Safety Institute and the US  
[00:45:08] one to be able to red team these systems. So one has to expose them to a certain extent,  
[00:45:16] although that’s not necessarily the weights. We have a lot of processes in place about making  
[00:45:22] sure that only if you need them, those people who need access have access. Right now, I think  
[00:45:31] we’re still in the early days of those kinds of systems being at risk. As these systems become  
[00:45:37] more powerful and more general and more capable, I think one has to look at the access question.  
[00:45:42] Some of these other labs have specialized in different things relative to safety,  
[00:45:46] Anthropic for example with interpretability. Do you have some sense of where you guys might  
[00:45:51] have an edge? Now that you have the frontier model, where are you guys going to be able to  
[00:45:57] put out the best frontier research on safety? I think we helped pioneer RLHF and other things  
[00:46:02] like that which can obviously be used for performance but also for safety. I think that  
[00:46:08] a lot of the self-play ideas and these kinds of things could also be used to auto-test a  
[00:46:15] lot of the boundary conditions that you have with the new systems. Part of the issue is  
[00:46:20] that with these very general systems, there’s so much surface area to cover about how these  
[00:46:27] systems behave. So I think we are going to need some automated testing. Again,  
[00:46:33] with things like simulations and games, very realistic virtual environments, I think we  
[00:46:39] have a long history of using those kinds of systems and making use of them for building  
[00:46:45] AI algorithms. I think we can leverage all of that history. And then around Google, we’re very lucky  
[00:46:51] to have some of the world’s best cybersecurity experts, hardware designers. I think we can bring  
[00:46:57] that to bear for security and safety as well. Let’s talk about Gemini. So now you guys have  
[00:47:04] the best model in the world. I’m curious. The default way to interact with these systems has  
[00:47:09] been through chat so far. Now that we have multimodal and all these new capabilities,  
[00:47:14] how do you anticipate that changing? Do you think that’ll still be the case?  
[00:47:17] I think we’re just at the beginning of actually understanding how exciting that might be to  
[00:47:25] interact with a full multimodal model system. It’ll be quite different from what we’re used  
[00:47:28] to today with the chatbots. I think the next versions of this over the next year, 18 months,  
[00:47:35] we’ll maybe have some contextual understanding of the environment around you through a camera  
[00:47:39] or a phone or some glasses. I could imagine that as the next step. And then I think we’ll  
[00:47:47] start becoming more fluid in understanding “let’s sample from a video, let’s use voice.” Maybe even  
[00:47:56] eventually things like touch and if you think about robotics, other types of sensors. So I  
[00:48:03] think the world’s about to become very exciting in the next few years as we start getting used  
[00:48:07] to the idea of what true multimodality means. On the robotics subject, when he was on the  
[00:48:14] podcast Ilya said that the reason OpenAI gave up on robotics was because they didn’t have enough  
[00:48:18] data in that domain, at least at the time they were pursuing it. You guys have put out  
[00:48:22] different things like Robo-Transformer and other things. Do you think that’s still a bottleneck  
[00:48:26] for robotics progress, or will we see progress in the world of atoms as well as the world of bits?  
[00:48:30] We’re very excited about our progress with things like Gato and RT-2. We’ve always liked robotics  
[00:48:40] and we’ve had amazing research in that. We still have that going now because we like the fact that  
[00:48:45] it’s a data-poor regime. That pushes us in very interesting research directions that we think  
[00:48:51] are going to be useful anyway: sampling efficiency and data efficiency in general, transfer learning,  
[00:48:57] learning from simulation and transferring that to reality, sim-to-real. All of these are very  
[00:49:02] interesting general challenges that we would like to solve. The control problem. So, we’ve always  
[00:49:10] pushed hard on that. I think Ilya is right. It is more challenging because of the data problem. But  
[00:49:18] I think we’re starting to see the beginnings of these large models being transferable to  
[00:49:24] the robotics regime. They can learn in the general domain, language domain and other things, and then  
[00:49:28] just treat tokens like Gato as any type of token. The token could be an action, it could be a word,  
[00:49:34] it could be part of an image, a pixel, or whatever it is. That’s what I think true multimodality is.  
[00:49:39] To begin with, it’s harder to train a system like that than a straightforward language  
[00:49:45] system. But going back to our early conversation on transfer learning, you start seeing that with a  
[00:49:52] true multimodal system, the other modalities benefit some different modalities. You get  
[00:49:58] better at language because you now understand a little bit about video. So I do think it’s  
[00:50:04] harder to get going, but ultimately we’ll have a more general, more capable system like that.  
[00:50:10] What ever happened to Gato? That was super fascinating that you could have it  
[00:50:13] play games and also do video and also do text. We’re still working on those kinds of systems,  
[00:50:18] but you can imagine we’re trying to build those ideas into our future generations of  
[00:50:24] Gemini to be able to do all of those things. Robotics, transformers, and things like that,  
[00:50:30] you can think of them as follow-ups to that. Will we see asymmetric progress in the domains in  
[00:50:36] which the self-play kinds of things you’re talking about will be especially powerful? So math and  
[00:50:40] code. Recently, you have these papers out about this. You can use these things to do really cool,  
[00:50:47] novel things. Will they be superhuman coders, but in other ways they might still be worse  
[00:50:51] than humans? How do you think about that? I think that we’re making great progress  
[00:50:57] with math and things like theorem proving and coding. But it’s still interesting if one looks  
[00:51:04] at creativity in general, and scientific endeavor in general. I think we’re getting to the stage  
[00:51:09] where our systems could help the best human scientists make their breakthroughs quicker,  
[00:51:14] almost triage the search space in some ways. Perhaps find a solution like AlphaFold does  
[00:51:19] with a protein structure. They’re not at the level where they can create the hypothesis themselves or  
[00:51:27] ask the right question. As any top scientist will tell you, the hardest part of science is actually  
[00:51:33] asking the right question. It’s boiling down that space to the critical question we should  
[00:51:37] go after and then formulating the problem in the right way to attack it. That’s not something our  
[00:51:44] systems really have any idea how to do, but they are suitable for searching large combinatorial  
[00:51:53] spaces if one can specify the problem with a clear objective function. So that’s very useful already  
[00:51:59] for many of the problems we deal with today, but not the most high-level creative problems.  
[00:52:06] DeepMind has published all kinds of interesting stuff in speeding  
[00:52:10] up science in different areas. If you think AGI is going to happen in the next 10 to 20 years,  
[00:52:17] why not just wait for the AGI to do it for you? Why build these domain-specific solutions?  
[00:52:21] I think we don’t know how long AGI is going to be. We always used to say, back even when  
[00:52:28] we started DeepMind, that we don’t have to wait for AGI in order to bring incredible benefits to  
[00:52:36] the world. My personal passion especially has been AI for science and health. You can see  
[00:52:45] that with things like AlphaFold and all of our various Nature papers on different domains and  
[00:52:49] material science work and so on. I think there’s lots of exciting directions and also impact in  
[00:52:54] the world through products too. I think it’s very exciting and a huge unique opportunity we  
[00:52:58] have as part of Google. They’ve got dozens of billion-user products that we can immediately  
[00:53:07] ship our advances into and then billions of people can improve, enrich, and enhance  
[00:53:16] their daily lives. I think it’s a fantastic opportunity for impact on all those fronts.  
[00:53:21] I think the other reason from the point of view of AGI specifically is that it battle tests  
[00:53:28] your ideas. You don’t want to be in a research bunker where you theoretically are pushing things  
[00:53:35] forward, but then actually your internal metrics start deviating from real-world things that people  
[00:53:42] would care about, or real-world impact. So you get a lot of direct feedback from these real-world  
[00:53:48] applications that then tells you whether your systems really are scaling or if we need to be  
[00:53:54] more data efficient or sample efficient. Because most real-world challenges require that. So it  
[00:54:01] kind of keeps you honest and pushes you to keep nudging and steering your research directions  
[00:54:07] to make sure they’re on the right path. So I think it’s fantastic. Of course, the world  
[00:54:11] benefits from that. Society benefits from that on the way, maybe many years before AGI arrives.  
[00:54:19] The development of Gemini is super interesting because it comes right at the heels of merging  
[00:54:23] these different organizations, Brain and DeepMind. I’m curious, what have been the challenges  
[00:54:28] there? What have been the synergies? It’s been successful in the sense that you have the best  
[00:54:31] model in the world now. What’s that been like? It’s been fantastic actually, over the last year.  
[00:54:36] Of course it’s been challenging to do, like any big integration coming together. You’re talking  
[00:54:41] about two world-class organizations with long, storied histories of inventing many  
[00:54:47] important things from deep reinforcement learning to transformers. So it’s very exciting to actually  
[00:54:52] pool all of that together and collaborate much more closely. We always used to be collaborating,  
[00:54:57] but more on a project-by-project basis versus a much deeper, broader collaboration like we  
[00:55:05] have now. Gemini is the first fruit of that collaboration, including the name Gemini  
[00:55:12] implying twins. Of course, a lot of other things are made more efficient like pooling compute  
[00:55:17] resources together and ideas and engineering. I think at the stage we’re at now, there are huge  
[00:55:23] amounts of world-class engineering that have to go into building the frontier systems. I  
[00:55:27] think it makes sense to coordinate that more. You and Shane started DeepMind partly because  
[00:55:34] you were concerned about safety. You saw AGI coming as a live possibility. Do you think  
[00:55:40] the people who were formerly part of Brain, that half of Google DeepMind now, approach  
[00:55:44] it in the same way? Have there been cultural differences there in terms of that question?  
[00:55:48] This is one of the reasons we joined forces with Google back in 2014. I think the entirety of  
[00:55:55] Google and Alphabet, not just Brain and DeepMind, takes these questions of responsibility very  
[00:55:58] seriously. Our kind of mantra is to try and be bold and responsible with these systems. I’m  
[00:56:06] obviously a huge techno-optimist but I want us to be cautious given the transformative power of  
[00:56:12] what we’re bringing into the world collectively. I think it’s important. It’s going to be one of  
[00:56:19] the most important technologies humanity will ever invent. So we’ve got to put all our efforts into  
[00:56:25] getting this right and be thoughtful and also humble about what we know and don’t  
[00:56:30] know about the systems that are coming and the uncertainties around that. In my view,  
[00:56:35] the only sensible approach when you have huge uncertainty is to be cautiously optimistic and  
[00:56:40] use the scientific method to try and have as much foresight and understanding about what’s coming  
[00:56:45] down the line and the consequences of that before it happens. You don’t want to be live A/B testing  
[00:56:50] out in the world with these very consequential systems because unintended consequences may be  
[00:56:55] quite severe. So I want us to move away, as a field, from a sort of “move fast and break things  
[00:57:02] attitude” which has maybe served the Valley very well in the past and obviously created important  
[00:57:07] innovations. I think in this case we want to be bold with the positive things that it can do  
[00:57:15] and make sure we advance things like medicine and science whilst being as responsible and  
[00:57:23] thoughtful as possible with mitigating the risks. That’s why it seems like the responsible scaling  
[00:57:30] policies are something that are a very good empirical way to pre-commit to these  
[00:57:34] kinds of things. Yes, exactly.  
[00:57:38] When you’re doing these evaluations and for example it turns out your next model could  
[00:57:41] help a layperson build a pandemic-class bioweapon or something, how would you think first of all  
[00:57:46] about making sure those weights are secure so that they don't get out? And second, what  
[00:57:51] would have to be true for you to be comfortable deploying that system? How would you make sure  
[00:57:55] that this latent capability isn’t exposed? The secure model part I think we’ve covered  
[00:58:01] with the cybersecurity and making sure that’s world-class and you’re monitoring all those  
[00:58:05] things. I think if a capability like that was discovered through red teaming or external  
[00:58:12] testing, independent testers like government institutes or academia or whatever, then we  
[00:58:19] would have to fix that loophole. Depending on what it was, that might require a different kind of  
[00:58:27] constitution perhaps, or different guardrails, or more RLHF to avoid that. Or you could remove some  
[00:58:33] training data, depending on what the problem is. I think there could be a number of mitigations. The  
[00:58:40] first part is making sure you detect it ahead of time. So that’s about the right evaluations  
[00:58:45] and right benchmarking and right testing. Then the question is how one would fix that before  
[00:58:50] you deployed it. But I think it would need to be fixed before it was deployed generally,  
[00:58:54] for sure, if that was an exposure surface. Final question. You’ve been thinking in terms  
[00:59:02] of the end goal of AGI at a time when other people thought it was ridiculous in 2010. Now  
[00:59:06] that we’re seeing this slow takeoff where we’re actually seeing generalization and intelligence,  
[00:59:12] what is like psychologically seeing this? What has that been like? Has it just been  
[00:59:15] sort of priced into your world model so it’s not new news for you? Or actually just  
[00:59:19] seeing it live, are you like “wow, something’s really changed”? What does it feel like?  
[00:59:24] For me, yes, it’s already priced into my world model of how things were going to go,  
[00:59:28] at least from the technology side. But obviously, we didn’t necessarily anticipate that the general  
[00:59:35] public would be so interested this early in the sequence. If ChatGPT and chatbots hadn’t gotten  
[00:59:47] the interest they ended up getting—which I think was quite surprising to everyone  
[00:59:50] that people were ready to use these things even though they were lacking in certain directions,  
[00:59:55] impressive though they are—then we would have produced more specialized systems built off  
[01:00:00] of the main track, like AlphaFold and AlphaGo, our scientific work. I think then the general  
[01:00:09] public maybe would have only paid attention later down the road when in a few years’ time,  
[01:00:14] we have more generally useful assistant-type systems. So that’s been interesting. That’s  
[01:00:19] created a different type of environment that we’re now all operating in as a field.  
[01:00:26] It’s a little bit more chaotic because there’s so many more things going on,  
[01:00:29] and there’s so much VC money going into it, and everyone’s sort of almost losing their minds over  
[01:00:34] it. The only thing I worry about is that I want to make sure that, as a field, we act responsibly  
[01:00:41] and thoughtfully and scientifically about this and use the scientific method to approach this  
[01:00:46] in an optimistic but careful way. I think I’ve always believed that that’s the right  
[01:00:52] approach for something like AI, and I just hope that doesn’t get lost in this huge rush.  
[01:01:00] Well, I think that’s a great place to close. Demis, thank you so much for your  
[01:01:03] time and for coming on the podcast. Thanks. It’s been a real pleasure.  
