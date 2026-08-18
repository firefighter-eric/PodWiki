# Andrej Karpathy — “We’re summoning ghosts, not building animals”

[00:00:48] Today I'm speaking with Andrej Karpathy. Andrej, why do you say that this will be  
[00:00:52] the decade of agents and not the year of agents? First of all, thank you for having me here. I'm  
[00:00:58] excited to be here. The quote you've just mentioned, "It's the decade of agents,"  
[00:01:03] is actually a reaction to a pre-existing quote. I'm not actually sure who said this but they were  
[00:01:09] alluding to this being the year of agents with respect to LLMs and how they were going to evolve.  
[00:01:16] I was triggered by that because there's some over-prediction going on in the industry.  
[00:01:21] In my mind, this is more accurately described as the decade of agents.  
[00:01:25] We have some very early agents that are extremely impressive and that I  
[00:01:28] use daily—Claude and Codex and so on—but I still feel there's so much work to be done.  
[00:01:35] My reaction is we'll be working with these things for a decade.  
[00:01:38] They're going to get better, and it's going to be wonderful.  
[00:01:42] I was just reacting to the timelines of the implication.  
[00:01:46] What do you think will take a decade to accomplish? What are the bottlenecks?  
[00:01:51] Actually making it work. When you're talking about an agent, or what the labs have in mind  
[00:01:56] and maybe what I have in mind as well, you should think of it almost like an employee or  
[00:01:59] an intern that you would hire to work with you. For example, you work with some employees here.  
[00:02:04] When would you prefer to have an agent like Claude or Codex do that work? Currently,  
[00:02:08] of course they can't. What would it take for them to be able to do that?  
[00:02:11] Why don't you do it today? The reason you don't do it  
[00:02:13] today is because they just don't work. They don't have enough intelligence,  
[00:02:17] they're not multimodal enough, they can't do computer use and all this stuff.  
[00:02:20] They don't do a lot of the things you've alluded to earlier. They don't have  
[00:02:24] continual learning. You can't just tell them something and they'll remember it.  
[00:02:27] They're cognitively lacking and it's just not working.  
[00:02:30] It will take about a decade to work through all of those issues.  
[00:02:32] Interesting. As a professional podcaster and a viewer of AI from afar, it's easy  
[00:02:42] for me to identify what's lacking: continual learning is lacking, or multimodality is lacking.  
[00:02:47] But I don't really have a good way of trying to put a timeline on it.  
[00:02:52] If somebody asks how long continual learning will take, I have no prior about whether  
[00:02:57] this is a project that should take 5 years, 10 years, or 50 years. Why a  
[00:03:01] decade? Why not one year? Why not 50 years? This is where you get into a bit of my own  
[00:03:07] intuition, and doing a bit of an extrapolation with respect to my own experience in the field.  
[00:03:14] I've been in AI for almost two decades. It's going to be 15 years or so, not that long.  
[00:03:19] You had Richard Sutton here, who was around for much longer.  
[00:03:23] I do have about 15 years of experience of people making predictions, of seeing how they turned out.  
[00:03:28] Also I was in the industry for a while, I was in research,  
[00:03:30] and I've worked in the industry for a while.  
[00:03:32] I have a general intuition that I have left from that.  
[00:03:37] I feel like the problems are tractable, they're surmountable, but they're still difficult.  
[00:03:43] If I just average it out, it just feels like a decade to me.  
[00:03:47] This is quite interesting. I want to hear not only the history,  
[00:03:50] but what people in the room felt was about to happen at various different breakthrough moments.  
[00:03:58] What were the ways in which their feelings were either overly pessimistic or overly optimistic?  
[00:04:03] Should we just go through each of them one by one? That's a giant question because you're talking  
[00:04:07] about 15 years of stuff that happened. AI is so wonderful because there have been  
[00:04:10] a number of seismic shifts where the entire field has suddenly looked a different way.  
[00:04:17] I've maybe lived through two or three of those. I still think there will continue to be  
[00:04:21] some because they come with almost surprising regularity.  
[00:04:25] When my career began, when I started to work on deep learning, when I became interested in deep  
[00:04:29] learning, this was by chance of being right next to Geoff Hinton at the University of Toronto.  
[00:04:34] Geoff Hinton, of course, is the godfather figure of AI.  
[00:04:37] He was training all these neural networks. I thought it was incredible and interesting.  
[00:04:40] This was not the main thing that everyone in AI was doing by far.  
[00:04:43] This was a niche little subject on the side. That's maybe the first dramatic seismic shift  
[00:04:49] that came with the AlexNet and so on. AlexNet reoriented everyone, and everyone  
[00:04:54] started to train neural networks, but it was still very per-task, per specific task.  
[00:04:59] Maybe I have an image classifier or I have a neural machine translator or something like that.  
[00:05:04] People became very slowly interested in agents. People started to think, "Okay, maybe we have a  
[00:05:10] check mark next to the visual cortex or something like that, but what about the other parts of the  
[00:05:14] brain, and how can we get a full agent or a full entity that can interact in the world?"  
[00:05:19] The Atari deep reinforcement learning shift in 2013 or so was part of that early effort  
[00:05:26] of agents, in my mind, because it was an attempt to try to get agents that not just  
[00:05:30] perceive the world, but also take actions and interact and get rewards from environments.  
[00:05:34] At the time, this was Atari games. I feel that was a misstep.  
[00:05:39] It was a misstep that even the early OpenAI that I was a part of adopted because at that time,  
[00:05:45] the zeitgeist was reinforcement learning environments, games, game playing,  
[00:05:50] beat games, get lots of different types of games, and OpenAI was doing a lot of that.  
[00:05:54] That was another prominent part of AI where maybe for two or three or four years, everyone was doing  
[00:06:01] reinforcement learning on games. That was all a bit of a misstep.  
[00:06:06] What I was trying to do at OpenAI is I was always a bit suspicious of games  
[00:06:10] as being this thing that would lead to AGI. Because in my mind, you want something like  
[00:06:13] an accountant or something that's interacting with the real world.  
[00:06:17] I just didn't see how games add up to it. My project at OpenAI, for example, was within the  
[00:06:23] scope of the Universe project, on an agent that was using keyboard and mouse to operate web pages.  
[00:06:30] I really wanted to have something that interacts with the actual digital world  
[00:06:33] that can do knowledge work. It just so turns out that this  
[00:06:37] was extremely early, way too early, so early that we shouldn't have been working on that.  
[00:06:42] Because if you're just stumbling your way around and keyboard mashing and mouse clicking and trying  
[00:06:47] to get rewards in these environments, your reward is too sparse and you just won't learn.  
[00:06:52] You're going to burn a forest computing, and you're never  
[00:06:54] going to get something off the ground. What you're missing is this power of  
[00:06:58] representation in the neural network. For example, today people are training  
[00:07:02] those computer-using agents, but they're doing it on top of a large language model.  
[00:07:05] You have to get the language model first, you have to get the representations first,  
[00:07:08] and you have to do that by all the pre-training and all the LLM stuff.  
[00:07:11] I feel maybe loosely speaking, people kept trying to get the full thing too  
[00:07:17] early a few times, where people really try to go after agents too early, I would say.  
[00:07:22] That was Atari and Universe and even my own experience.  
[00:07:26] You actually have to do some things first before you get to those agents.  
[00:07:30] Now the agents are a lot more competent, but maybe we're still missing some parts of that stack.  
[00:07:36] I would say those are the three major buckets of what people were doing:  
[00:07:40] training neural nets per-tasks, trying the first round of agents,  
[00:07:44] and then maybe the LLMs and seeking the representation power of the neural networks  
[00:07:48] before you tack on everything else on top. Interesting. If I were to steelman the Sutton  
[00:07:54] perspective, it would be that humans can just take on everything at once,  
[00:07:57] or even animals can take on everything at once. Animals are maybe a better example because they  
[00:08:01] don't even have the scaffold of language. They just get thrown out into the world,  
[00:08:05] and they just have to make sense of everything without any labels.  
[00:08:10] The vision for AGI then should just be something which looks at sensory data,  
[00:08:14] looks at the computer screen, and it just figures out what's going on from scratch.  
[00:08:18] If a human were put in a similar situation and had to be trained from scratch… This is like a  
[00:08:22] human growing up or an animal growing up. Why shouldn't that be the vision for AI,  
[00:08:26] rather than this thing where we're doing millions of years of training?  
[00:08:29] That's a really good question. Sutton was on your podcast and I saw the podcast and I  
[00:08:35] had a write-up about that podcast that gets into a bit of how I see things.  
[00:08:41] I'm very careful to make analogies to animals because they came about by a  
[00:08:46] very different optimization process. Animals are evolved, and they come  
[00:08:49] with a huge amount of hardware that's built in. For example, my example in the post was the zebra.  
[00:08:55] A zebra gets born, and a few minutes later it's running around and following its mother.  
[00:08:59] That's an extremely complicated thing to do. That's not reinforcement learning. That's  
[00:09:03] something that's baked in. Evolution obviously has some way of encoding the weights of our  
[00:09:08] neural nets in ATCGs, and I have no idea how that works, but it apparently works.  
[00:09:14] Brains just came from a very different process, and I'm very hesitant to take inspiration from it  
[00:09:20] because we're not actually running that process. In my post, I said we're not building animals.  
[00:09:25] We're building ghosts or spirits or whatever people want to call it, because  
[00:09:31] we're not doing training by evolution. We're doing training by imitation of humans  
[00:09:37] and the data that they've put on the Internet. You end up with these ethereal spirit entities  
[00:09:42] because they're fully digital and they're mimicking humans.  
[00:09:45] It's a different kind of intelligence. If you imagine a space of intelligences,  
[00:09:48] we're starting off at a different point almost. We're not really building animals. But it's also  
[00:09:53] possible to make them a bit more animal-like over time, and I think we should be doing that.  
[00:09:58] One more point. I do feel Sutton has a very... His framework is, "We want to build animals."  
[00:10:04] I think that would be wonderful if we can get that to work. That would be amazing.  
[00:10:07] If there were a single algorithm that you can just run on the Internet and it learns  
[00:10:13] everything, that would be incredible. I'm not sure that it exists and that's  
[00:10:18] certainly not what animals do, because animals have this outer loop of evolution.  
[00:10:24] A lot of what looks like learning is more like maturation of the brain.  
[00:10:28] I think there's very little reinforcement learning for animals.  
[00:10:32] A lot of the reinforcement learning is more like motor tasks; it's not intelligence tasks.  
[00:10:37] So I actually kind of think humans don’t really use RL, roughly speaking.  
[00:10:41] Can you repeat the last sentence? A lot of that intelligence is  
[00:10:42] not motor task…it's what, sorry? A lot of the reinforcement learning, in my  
[00:10:45] perspective, would be things that are a lot more motor-like, simple tasks like throwing a hoop.  
[00:10:53] But I don't think that humans use reinforcement learning for a lot of intelligence tasks  
[00:10:57] like problem-solving and so on. That doesn't mean we shouldn't  
[00:11:01] do that for research, but I just feel like that's what animals do or don't.  
[00:11:05] I'm going to take a second to digest that because there are a lot of different ideas.  
[00:11:09] Here’s one clarifying question I can ask to understand the perspective.  
[00:11:15] You suggest that evolution is doing the kind of thing that pre-training  
[00:11:18] does in the sense of building something which can then understand the world.  
[00:11:24] The difference is that evolution has to be titrated in the case  
[00:11:28] of humans through three gigabytes of DNA. That's very unlike the weights of a model.  
[00:11:37] Literally, the weights of the model are a brain, which obviously does not exist  
[00:11:42] in the sperm and the egg. So it has to be grown.  
[00:11:46] Also, the information for every single synapse in the brain simply cannot exist  
[00:11:50] in the three gigabytes that exist in the DNA. Evolution seems closer to finding the algorithm  
[00:11:55] which then does the lifetime learning. Now, maybe the lifetime learning is  
[00:12:00] not analogous to RL, to your point. Is that compatible with the thing you  
[00:12:04] were saying, or would you disagree with that? I think so. I would agree with you that there's  
[00:12:06] some miraculous compression going on because obviously,  
[00:12:09] the weights of the neural net are not stored in ATCGs. There's some dramatic compression.  
[00:12:14] There are some learning algorithms encoded that take over and do some of the learning online.  
[00:12:18] I definitely agree with you on that. I would say I'm a lot more practically minded.  
[00:12:23] I don't come at it from the perspective of, let's build animals.  
[00:12:26] I come from it from the perspective of, let's build useful things.  
[00:12:28] I have a hard hat on, and I'm just observing that we're not going to do  
[00:12:31] evolution, because I don't know how to do that. But it does turn out we can build these ghosts,  
[00:12:36] spirit-like entities, by imitating internet documents. This works. It's a way to bring you  
[00:12:43] up to something that has a lot of built-in knowledge and intelligence in some way,  
[00:12:48] similar to maybe what evolution has done. That's why I call pre-training  
[00:12:51] this crappy evolution. It's the practically possible version  
[00:12:56] with our technology and what we have available to us to get to a starting point where we can do  
[00:13:01] things like reinforcement learning and so on. Just to steelman the other perspective,  
[00:13:05] after doing this Sutton interview and thinking about it a bit, he has an important point here.  
[00:13:09] Evolution does not give us the knowledge, really. It gives us the algorithm to find the knowledge,  
[00:13:14] and that seems different from pre-training. Perhaps the perspective is that pre-training helps  
[00:13:19] build the kind of entity which can learn better. It teaches meta-learning, and therefore  
[00:13:23] it is similar to finding an algorithm. But if it's "Evolution gives us knowledge,  
[00:13:28] pre-training gives us knowledge," that analogy seems to break down.  
[00:13:31] It's subtle and I think you're right to push back on it, but basically the thing  
[00:13:35] that pre-training is doing, you're getting the next-token predictor over the internet,  
[00:13:38] and you're training that into a neural net. It's doing two things that are unrelated.  
[00:13:43] Number one, it's picking up all this knowledge, as I call it.  
[00:13:46] Number two, it's actually becoming intelligent. By observing the algorithmic patterns in the  
[00:13:51] internet, it boots up all these little circuits and algorithms inside the neural net to do things  
[00:13:55] like in-context learning and all this stuff. You don't need or want the knowledge.  
[00:14:00] I think that's probably holding back the neural networks overall because it's getting them to rely  
[00:14:05] on the knowledge a little too much sometimes. For example, I feel agents, one thing they're  
[00:14:09] not very good at, is going off the data manifold of what exists on the internet.  
[00:14:13] If they had less knowledge or less memory, maybe they would be better.  
[00:14:17] What I think we have to do going forward—and this would be part of the research paradigms—is  
[00:14:23] figure out ways to remove some of the knowledge and to keep what I call this cognitive core.  
[00:14:28] It's this intelligent entity that is stripped from knowledge but contains the algorithms and contains  
[00:14:34] the magic of intelligence and problem-solving and the strategies of it and all this stuff.  
[00:14:39] There's so much interesting stuff there. Let's start with in-context learning. This is an  
[00:14:44] obvious point, but I think it's worth just saying it explicitly and meditating on it.  
[00:14:48] The situation in which these models seem the most intelligent—in which I talk to them and I'm like,  
[00:14:53] "Wow, there's really something on the other end that's responding to me thinking about things—is  
[00:14:58] if it makes a mistake it's like, "Oh wait, that's the wrong way to think about it. I'm backing up."  
[00:15:01] All that is happening in context. That's where I feel like the real  
[00:15:04] intelligence is that you can visibly see. That in-context learning process is  
[00:15:10] developed by gradient descent on pre-training. It spontaneously meta-learns in-context learning,  
[00:15:16] but the in-context learning itself is not gradient descent, in the same way that our  
[00:15:21] lifetime intelligence as humans to be able to do things is conditioned by evolution  
[00:15:26] but our learning during our lifetime is happening through some other process.  
[00:15:30] I don't fully agree with that, but you should continue your thought.  
[00:15:34] Well, I'm very curious to understand how that analogy breaks down.  
[00:15:36] I'm hesitant to say that in-context learning is not doing gradient descent.  
[00:15:41] It's not doing explicit gradient descent. In-context learning is pattern completion  
[00:15:47] within a token window. It just turns out that there's  
[00:15:50] a huge amount of patterns on the internet. You're right, the model learns to complete  
[00:15:53] the pattern, and that's inside the weights. The weights of the neural network are trying  
[00:15:58] to discover patterns and complete the pattern. There's some adaptation that happens inside  
[00:16:02] the neural network, which is magical and just falls out from the internet  
[00:16:06] just because there's a lot of patterns. I will say that there have been some papers  
[00:16:10] that I thought were interesting that look at the mechanisms behind in-context learning.  
[00:16:14] I do think it's possible that in-context learning runs a small gradient descent loop  
[00:16:17] internally in the layers of the neural network. I recall one paper in particular where they were  
[00:16:22] doing linear regression using in-context learning. Your inputs into the neural network are XY pairs,  
[00:16:30] XY, XY, XY that happen to be on the line. Then you do X and you expect Y.  
[00:16:35] The neural network, when you train it in this way, does linear regression.  
[00:16:41] Normally when you would run linear regression, you have a small gradient descent optimizer that looks  
[00:16:46] at XY, looks at an error, calculates the gradient of the weights and does the update a few times.  
[00:16:50] It just turns out that when they looked at the weights of that in-context learning algorithm,  
[00:16:54] they found some analogies to gradient descent mechanics.  
[00:16:59] In fact, I think the paper was even stronger because they hardcoded the weights of a neural  
[00:17:03] network to do gradient descent through attention and all the internals of the  
[00:17:10] neural network. That's just my only pushback. Who knows how in-context learning works,  
[00:17:14] but I think that it's probably doing a bit of some funky gradient descent internally. I think that  
[00:17:19] that's possible. I was only pushing back on your saying that it's not doing in-context learning.  
[00:17:24] Who knows what it's doing, but it's probably maybe doing something similar to it, but we don't know.  
[00:17:28] So then it's worth thinking okay, if in-context learning and pre-training  
[00:17:34] are both implementing something like gradient descent, why does it feel like with in-context  
[00:17:39] learning we're getting to this continual learning, real intelligence-like thing?  
[00:17:44] Whereas you don't get the analogous feeling just from pre-training. You could argue that. If it's  
[00:17:49] the same algorithm, what could be different? One way you could think about it is,  
[00:17:53] how much information does the model store per information it receives from training?  
[00:18:00] If you look at pre-training, if you look at Llama 3 for example,  
[00:18:03] I think it's trained on 15 trillion tokens. If you look at the 70B model, that would  
[00:18:10] be the equivalent of 0.07 bits per token that it sees in pre-training,  
[00:18:15] in terms of the information in the weights of the model compared to the tokens it reads.  
[00:18:18] Whereas if you look at the KV cache and how it grows per additional token  
[00:18:22] in in-context learning, it's like 320 kilobytes. So that's a 35 million-fold difference in how much  
[00:18:29] information per token is assimilated by the model. I wonder if that's relevant at all.  
[00:18:34] I kind of agree. The way I usually put this is that anything that happens during the training of  
[00:18:39] the neural network, the knowledge is only a hazy recollection of what happened in training time.  
[00:18:45] That's because the compression is dramatic. You're taking 15 trillion tokens and you're  
[00:18:48] compressing it to just your final neural network of a few billion parameters.  
[00:18:51] Obviously it's a massive amount of compression going on.  
[00:18:54] So I refer to it as a hazy recollection of the internet documents.  
[00:18:57] Whereas anything that happens in the context window of the neural network—you're  
[00:19:00] plugging in all the tokens and building up all those KV cache representations—is very  
[00:19:04] directly accessible to the neural net. So I compare the KV cache and the stuff  
[00:19:08] that happens at test time to more like a working memory.  
[00:19:11] All the stuff that's in the context window is very directly accessible to the neural net.  
[00:19:16] There's always these almost surprising analogies between LLMs and humans.  
[00:19:21] I find them surprising because we're not trying to build a human brain directly.  
[00:19:25] We're just finding that this works and we're doing it.  
[00:19:27] But I do think that anything that's in the weights, it's a  
[00:19:30] hazy recollection of what you read a year ago. Anything that you give it as a context at test  
[00:19:36] time is directly in the working memory. That's a very powerful analogy to  
[00:19:40] think through things. When you, for example,  
[00:19:42] go to an LLM and you ask it about some book and what happened in it, like Nick Lane's  
[00:19:46] book or something like that, the LLM will often give you some stuff which is roughly correct.  
[00:19:49] But if you give it the full chapter and ask it questions, you're going to get much better results  
[00:19:53] because it's now loaded in the working memory of the model.  
[00:19:56] So a very long way of saying I agree and that's why.  
[00:20:00] Stepping back, what is the part about human intelligence that we  
[00:20:03] have most failed to replicate with these models?  
[00:20:12] Just a lot of it. So maybe one way to think about it, I don't know if this is the best way,  
[00:20:17] but I almost feel like — again, making these analogies imperfect as they are — we've stumbled  
[00:20:22] by with the transformer neural network, which is extremely powerful, very general.  
[00:20:27] You can train transformers on audio, or video, or text, or whatever you want,  
[00:20:31] and it just learns patterns and they're very powerful, and it works really well.  
[00:20:35] That to me almost indicates that this is some piece of cortical tissue.  
[00:20:38] It's something like that, because the cortex is famously very plastic as well.  
[00:20:42] You can rewire parts of brains. There were the slightly gruesome experiments  
[00:20:48] with rewiring the visual cortex to the auditory cortex, and this animal learned fine, et cetera.  
[00:20:54] So I think that this is cortical tissue. I think when we're doing reasoning and  
[00:20:58] planning inside the neural networks, doing reasoning traces for thinking models,  
[00:21:04] that's kind of like the prefrontal cortex. Maybe those are like little checkmarks,  
[00:21:11] but I still think there are many brain parts and nuclei that are not explored.  
[00:21:15] For example, there's a basal ganglia doing a bit of reinforcement learning when we fine-tune  
[00:21:18] the models on reinforcement learning. But where's the hippocampus? Not obvious what that would be.  
[00:21:23] Some parts are probably not important. Maybe the cerebellum is not important  
[00:21:26] to cognition, its thoughts, so maybe we can skip some of it.  
[00:21:29] But I still think there's, for example, the amygdala, all the emotions and instincts.  
[00:21:33] There's probably a bunch of other nuclei in the brain that are very ancient that  
[00:21:36] I don't think we've really replicated. I don't know that we should be pursuing the  
[00:21:41] building of an analog of a human brain. I'm an engineer mostly at heart.  
[00:21:48] Maybe another way to answer the question is that you're not going to hire this thing as an intern.  
[00:21:52] It's missing a lot of it because it comes with a lot of these cognitive deficits that we all  
[00:21:55] intuitively feel when we talk to the models. So it's not fully there yet.  
[00:22:00] You can look at it as not all the brain parts are checked off yet.  
[00:22:04] This is maybe relevant to the question of thinking about how fast these issues will be solved.  
[00:22:10] Sometimes people will say about continual learning,  
[00:22:13] "Look, you could easily replicate this capability. Just as in-context learning emerged spontaneously  
[00:22:19] as a result of pre-training, continual learning over longer horizons will emerge  
[00:22:24] spontaneously if the model is incentivized to recollect information over longer horizons,  
[00:22:30] or horizons longer than one session." So if there's some outer loop RL which has  
[00:22:39] many sessions within that outer loop, then this continual learning where it fine-tunes itself,  
[00:22:46] or it writes to an external memory or something, will just emerge spontaneously.  
[00:22:49] Do you think things like that are plausible? I just don't have a prior over  
[00:22:53] how plausible that is. How likely is that to happen?  
[00:22:55] I don't know that I fully resonate with that. These models, when you boot them up and they have  
[00:22:59] zero tokens in the window, they're always restarting from scratch where they were.  
[00:23:03] So I don't know in that worldview what it looks like.  
[00:23:09] Maybe making some analogies to humans—just because I think it's roughly concrete and interesting to  
[00:23:13] think through—I feel like when I'm awake, I'm building up a context window of stuff that's  
[00:23:17] happening during the day. But when I go to sleep,  
[00:23:19] something magical happens where I don't think that context window stays around.  
[00:23:23] There's some process of distillation into the weights of my brain.  
[00:23:27] This happens during sleep and all this stuff. We don't have an equivalent  
[00:23:30] of that in large language models. That's to me more adjacent to when you talk  
[00:23:35] about continual learning and so on as absent. These models don't really have a distillation  
[00:23:40] phase of taking what happened, analyzing it obsessively, thinking through it, doing some  
[00:23:47] synthetic data generation process and distilling it back into the weights, and maybe having  
[00:23:51] a specific neural net per person. Maybe it's a LoRA. It's not a full-weight neural network.  
[00:24:01] It's just some small sparse subset of the weights that are changed.  
[00:24:05] But we do want to create ways of creating these individuals that have very long context.  
[00:24:10] It's not only remaining in the context window because the context windows grow very, very long.  
[00:24:14] Maybe we have some very elaborate, sparse attention over it.  
[00:24:17] But I still think that humans obviously have some process for distilling some of that knowledge  
[00:24:22] into the weights. We're missing it. I do also think that humans have some very elaborate,  
[00:24:27] sparse attention scheme, which I think we're starting to see some early hints of.  
[00:24:33] DeepSeek v3.2 just came out and I saw that they have sparse attention as an example, and this is  
[00:24:38] one way to have very, very long context windows. So I feel like we are redoing a lot of the  
[00:24:44] cognitive tricks that evolution came up with through a very different process.  
[00:24:47] But we're going to converge on a similar architecture cognitively.  
[00:24:51] In 10 years, do you think it'll still be something like a transformer, but with much more modified  
[00:24:55] attention and more sparse MLPs and so forth? The way I like to think about it is  
[00:25:00] translation invariance in time. So 10 years ago, where were we? 2015.  
[00:25:05] In 2015, we had convolutional neural networks primarily, residual networks just came out.  
[00:25:10] So remarkably similar, I guess, but quite a bit different still. The transformer was not  
[00:25:14] around. All these more modern tweaks on the transformer were not around.  
[00:25:21] Maybe some of the things that we can bet on, I think in 10 years by translational equivariance,  
[00:25:27] is that we're still training giant neural networks with a forward backward pass and  
[00:25:31] update through gradient descent, but maybe it looks a bit different,  
[00:25:36] and it's just that everything is much bigger. Recently I went back all the way to 1989 which  
[00:25:42] was a fun exercise for me, a few years ago, because I was reproducing Yann LeCun's 1989  
[00:25:48] convolutional network, which was the first neural network I'm aware of trained via gradient descent,  
[00:25:52] like modern neural network trained gradient descent on digit recognition.  
[00:25:57] I was just interested in how I could modernize this.  
[00:26:00] How much of this is algorithms? How much of this is data?  
[00:26:01] How much of this progress is compute and systems? I was able to very quickly halve the learning  
[00:26:06] just by time traveling by 33 years. So if I time travel by algorithms 33 years,  
[00:26:13] I could adjust what Yann LeCun did in 1989, and I could halve the error.  
[00:26:18] But to get further gains, I had to add a lot more data,  
[00:26:21] I had to 10x the training set, and then I had to add more computational optimizations.  
[00:26:25] I had to train for much longer with dropout and other regularization techniques.  
[00:26:30] So all these things have to improve simultaneously.  
[00:26:35] We're probably going to have a lot more data, we're probably going to have a lot  
[00:26:37] better hardware, probably going to have a lot better kernels and software, we're probably  
[00:26:40] going to have better algorithms. All of those, it's almost like  
[00:26:43] no one of them is winning too much. All of them are surprisingly equal.  
[00:26:48] This has been the trend for a while. So to answer your question, I expect differences  
[00:26:54] algorithmically to what's happening today. But I do also expect that some of the  
[00:26:58] things that have stuck around for a very long time will probably still be there.  
[00:27:01] It's probably still a giant neural network trained with gradient descent. That would be my guess.  
[00:27:05] It's surprising that all of those things together only halved the error, 30 years  
[00:27:13] of progress…. Maybe half is a lot. Because if you halve the error, that actually means that…  
[00:27:18] Half is a lot. But I guess what was shocking to me is everything needs to improve across the board:  
[00:27:24] architecture, optimizer, loss function. It also has improved across the board forever.  
[00:27:28] So I expect all those changes to be alive and well.  
[00:27:31] Yeah. I was about to ask you a very similar question about nanochat.  
[00:27:35] Since you just coded it up recently, every single step in the process of  
[00:27:40] building a chatbot is fresh in your RAM. I'm curious if you had similar thoughts about,  
[00:27:46] "Oh, there was no one thing that was relevant to going from GPT-2 to nanochat."  
[00:27:52] What are some surprising takeaways from the experience?  
[00:27:55] Of building nanochat? So nanochat is a repository I released.  
[00:27:59] Was it yesterday or the day before? I can't remember.  
[00:28:03] We can see the sleep deprivation that went into the…  
[00:28:09] It's trying to be the simplest complete repository that covers the whole pipeline  
[00:28:12] end-to-end of building a ChatGPT clone. So you have all of the steps, not just  
[00:28:18] any individual step, which is a bunch. I worked on all the individual steps  
[00:28:22] in the past and released small pieces of code that show you how that's done  
[00:28:25] in an algorithmic sense, in simple code. But this handles the entire pipeline.  
[00:28:32] In terms of learning, I don't know that I necessarily found  
[00:28:36] something that I learned from it. I already had in my mind how you build it.  
[00:28:40] This is just the process of mechanically building it and making it clean enough so that people can  
[00:28:48] learn from it and that they find it useful. What is the best way for somebody  
[00:28:53] to learn from it? Is it to just delete  
[00:28:54] all the code and try to reimplement from scratch, try to add modifications to it?  
[00:28:59] That's a great question. Basically it's about 8,000 lines of code  
[00:29:03] that takes you through the entire pipeline. I would probably put it on the right monitor.  
[00:29:07] If you have two monitors, you put it on the right. You want to build it from scratch,  
[00:29:11] you build it from the start. You're not allowed to copy-paste, you're allowed  
[00:29:14] to reference, you're not allowed to copy-paste. Maybe that's how I would do it.  
[00:29:18] But I also think the repository by itself is a pretty large beast.  
[00:29:23] When you write this code, you don't go from top to bottom, you go from chunks and you grow the  
[00:29:27] chunks, and that information is absent. You wouldn't know where to start.  
[00:29:31] So it's not just a final repository that's needed, it's the building of the repository,  
[00:29:35] which is a complicated chunk-growing process. So that part is not there yet.  
[00:29:40] I would love to add that probably later this week. It's probably a video or something like that.  
[00:29:49] Roughly speaking, that's what I would try to do. Build the stuff yourself, but don't allow  
[00:29:53] yourself copy-paste. I do think that  
[00:29:55] there's two types of knowledge, almost. There's the high-level surface knowledge, but when  
[00:29:59] you build something from scratch, you're forced to come to terms with what you don't understand and  
[00:30:04] you don't know that you don't understand it. It always leads to a deeper understanding.  
[00:30:09] It's the only way to build. If I can't build it, I don't understand it.  
[00:30:13] That’s a Feynman quote, I believe. I 100% have always believed this very  
[00:30:19] strongly, because there are all these micro things that are just not properly arranged  
[00:30:23] and you don't really have the knowledge. You just think you have the knowledge.  
[00:30:25] So don't write blog posts, don't do slides, don't do any of that.  
[00:30:28] Build the code, arrange it, get it to work. It's the only way to go. Otherwise,  
[00:30:31] you're missing knowledge. You tweeted out that coding models  
[00:30:35] were of very little help to you in assembling this repository. I'm curious why that was.  
[00:30:43] I guess I built the repository over a period of a bit more than a month.  
[00:30:46] I would say there are three major classes of how people interact with code right now.  
[00:30:50] Some people completely reject all of LLMs and they are just writing by scratch.  
[00:30:54] This is probably not the right thing to do anymore.  
[00:30:58] The intermediate part, which is where I am, is you still write a lot of things from scratch,  
[00:31:02] but you use the autocomplete that's available now from these models.  
[00:31:06] So when you start writing out a little piece of it, it will autocomplete for  
[00:31:10] you and you can just tap through. Most of the time it's correct,  
[00:31:12] sometimes it's not, and you edit it. But you're still very much the  
[00:31:16] architect of what you're writing. Then there's the vibe coding: "Hi,  
[00:31:21] please implement this or that," enter, and then let the model do it. That's the agents. I do feel  
[00:31:28] like the agents work in very specific settings, and I would use them in specific settings.  
[00:31:33] But these are all tools available to you and you have to learn what they're good at,  
[00:31:37] what they're not good at, and when to use them. So the agents are pretty good, for example,  
[00:31:40] if you're doing boilerplate stuff. Boilerplate code that's just  
[00:31:44] copy-paste stuff, they're very good at that. They're very good at stuff that occurs very often  
[00:31:48] on the Internet because there are lots of examples of it in the training sets of these models.  
[00:31:55] There are features of things where the models will do very well.  
[00:31:58] I would say nanochat is not an example of those because it's a fairly unique repository.  
[00:32:03] There's not that much code in the way that I've structured it. It's not boilerplate code.  
[00:32:08] It's intellectually intense code almost, and everything has to be very precisely arranged.  
[00:32:13] The models have so many cognitive deficits. One example, they kept misunderstanding the code  
[00:32:22] because they have too much memory from all the typical ways of doing things on  
[00:32:26] the Internet that I just wasn't adopting. The models, for example—I don't know if I  
[00:32:31] want to get into the full details—but they kept thinking I'm writing normal code, and I'm not.  
[00:32:36] Maybe one example? You have eight GPUs  
[00:32:41] that are all doing forward, backwards. The way to synchronize gradients between  
[00:32:44] them is to use a Distributed Data Parallel container of PyTorch, which automatically  
[00:32:49] as you're doing the backward, it will start communicating and synchronizing gradients.  
[00:32:52] I didn't use DDP because I didn't want to use it, because it's not necessary.  
[00:32:56] I threw it out and wrote my own synchronization routine that's inside the step of the optimizer.  
[00:33:02] The models were trying to get me to use the DDP container. They were very  
[00:33:06] concerned. This gets way too technical, but I wasn't using that container because  
[00:33:11] I don't need it and I have a custom implementation of something like it.  
[00:33:14] They just couldn't internalize that you had your own.  
[00:33:16] They couldn't get past that. They kept trying to mess up the style. They're way too over-defensive.  
[00:33:23] They make all these try-catch statements. They keep trying to make a production code base,  
[00:33:27] and I have a bunch of assumptions in my code, and it's okay.  
[00:33:31] I don't need all this extra stuff in there. So I feel like they're bloating the code base,  
[00:33:36] bloating the complexity, they keep misunderstanding, they're using  
[00:33:38] deprecated APIs a bunch of times. It's a total mess. It's just not net useful. I can go in,  
[00:33:46] I can clean it up, but it's not net useful. I also feel like it's annoying to have to  
[00:33:50] type out what I want in English because it's too much typing.  
[00:33:54] If I just navigate to the part of the code that I want, and I go where I know the code has to appear  
[00:33:58] and I start typing out the first few letters, autocomplete gets it and just gives you the code.  
[00:34:03] This is a very high information bandwidth to specify what you want.  
[00:34:07] You point to the code where you want it, you type out the first few pieces,  
[00:34:10] and the model will complete it. So what I mean is, these models  
[00:34:15] are good in certain parts of the stack. There are two examples where I use the  
[00:34:22] models that I think are illustrative. One was when I generated the report.  
[00:34:26] That's more boilerplate-y, so I partially vibe-coded some of that stuff.  
[00:34:30] That was fine because it's not mission-critical stuff, and it works fine.  
[00:34:34] The other part is when I was rewriting the tokenizer in Rust.  
[00:34:37] I'm not as good at Rust because I'm fairly new to Rust.  
[00:34:41] So there's a bit of vibe coding going on when I was writing some of the Rust code.  
[00:34:45] But I had a Python implementation that I fully understand, and I'm just making sure  
[00:34:49] I'm making a more efficient version of it, and I have tests so I feel safer doing that stuff.  
[00:34:56] They increase accessibility to languages or paradigms that you might not be as familiar with.  
[00:35:02] I think they're very helpful there as well. There's a ton of Rust code out there,  
[00:35:06] the models are pretty good at it. I happen to not know that much about it,  
[00:35:09] so the models are very useful there. The reason this question is so interesting  
[00:35:12] is because the main story people have about AI exploding and getting  
[00:35:19] to superintelligence pretty rapidly is AI automating AI engineering and AI research.  
[00:35:25] They'll look at the fact that you can have Claude Code and make entire applications,  
[00:35:27] CRUD applications, from scratch and think, "If you had this same capability inside of OpenAI  
[00:35:32] and DeepMind and everything, just imagine a thousand of you or a million of you in  
[00:35:38] parallel, finding little architectural tweaks." It's quite interesting to hear you say that this  
[00:35:43] is the thing they're asymmetrically worse at. It's quite relevant to forecasting whether  
[00:35:48] the AI 2027-type explosion is likely to happen anytime soon.  
[00:35:53] That's a good way of putting it, and you're getting at why my timelines are a bit longer.  
[00:35:58] You're right. They're not very good at code that has never been written before, maybe it's  
[00:36:04] one way to put it, which is what we're trying to achieve when we're building these models.  
[00:36:07] Very naive question, but the architectural tweaks that you're adding to nanochat,  
[00:36:14] they're in a paper somewhere, right? They might even be in a repo somewhere.  
[00:36:20] Is it surprising that they aren't able to integrate that into whenever you're like,  
[00:36:25] "Add RoPE embeddings" or something, they do that in the wrong way?  
[00:36:29] It's tough. They know, but they don't fully know. They don't know how to fully integrate it into  
[00:36:34] the repo and your style and your code and your place, and some of the custom things  
[00:36:37] that you're doing and how it fits with all the assumptions of the repository.  
[00:36:42] They do have some knowledge, but they haven't gotten to the place where they  
[00:36:46] can integrate it and make sense of it. A lot of the stuff continues to improve.  
[00:36:54] Currently, the state-of-the-art model that I go to is the GPT-5 Pro,  
[00:36:57] and that's a very powerful model. If I have 20 minutes,  
[00:37:01] I will copy-paste my entire repo and I go to GPT-5 Pro, the oracle, for some questions.  
[00:37:06] Often it's not too bad and surprisingly good compared to what existed a year ago.  
[00:37:11] Overall, the models are not there. I feel like the industry is making too  
[00:37:20] big of a jump and is trying to pretend like this is amazing, and it's not. It's slop. They're not  
[00:37:27] coming to terms with it, and maybe they're trying to fundraise or something like that.  
[00:37:29] I'm not sure what's going on, but we're at this intermediate stage. The models are  
[00:37:33] amazing. They still need a lot of work. For now, autocomplete is my sweet spot.  
[00:37:38] But sometimes, for some types of code, I will go to an LLM agent.  
[00:37:43] Here's another reason this is really interesting. Through the history of programming, there have  
[00:37:48] been many productivity improvements—compilers, linting, better programming languages—which  
[00:37:55] have increased programmer productivity but have not led to an explosion.  
[00:38:00] That sounds very much like the autocomplete tab, and this other  
[00:38:04] category is just automation of the programmer. It's interesting you're seeing more in the  
[00:38:09] category of the historical analogies of better compilers or something.  
[00:38:13] Maybe this gets to one other thought. I have a hard time differentiating where  
[00:38:19] AI begins and stops because I see AI as fundamentally an extension of  
[00:38:23] computing in a pretty fundamental way. I see a continuum of this recursive  
[00:38:28] self-improvement or speeding up programmers all the way from the beginning: code editors,  
[00:38:37] syntax highlighting, or checking even of the types, like data type checking—all  
[00:38:44] these tools that we've built for each other. Even search engines.  
[00:38:48] Why aren't search engines part of AI? Ranking is AI. At some point, Google, even early on,  
[00:38:55] was thinking of themselves as an AI company doing Google Search engine, which is totally fair.  
[00:38:59] I see it as a lot more of a continuum than other people do, and it's hard for me to draw the line.  
[00:39:04] I feel like we're now getting a much better autocomplete, and now we're also  
[00:39:07] getting some agents which are these loopy things, but they go off-rails sometimes.  
[00:39:13] What's going on is that the human is progressively doing a bit less and less of the low-level stuff.  
[00:39:18] We're not writing the assembly code because we have compilers.  
[00:39:20] Compilers will take my high-level language in C and write the assembly code.  
[00:39:23] We're abstracting ourselves very, very slowly. There's this what I call "autonomy slider," where  
[00:39:28] more and more stuff is automated—of the stuff that can be automated at any point in time—and we're  
[00:39:32] doing a bit less and less and raising ourselves in the layer of abstraction over the automation.  
[00:40:53] Let's talk about RL a bit. You tweeted some very  
[00:40:56] interesting things about this. Conceptually, how should we think about  
[00:41:00] the way that humans are able to build a rich world model just from interacting with our environment,  
[00:41:07] and in ways that seem almost irrespective of the final reward at the end of the episode?  
[00:41:13] If somebody is starting a business, and at the end of 10 years, she finds out whether  
[00:41:17] the business succeeded or failed, we say that she's earned a bunch of wisdom and experience.  
[00:41:22] But it's not because the log probs of every single thing that happened over the last 10  
[00:41:25] years are up-weighted or down-weighted. Something much more deliberate and  
[00:41:29] rich is happening. What is the ML analogy, and how does that  
[00:41:33] compare to what we're doing with LLMs right now? Maybe the way I would put it is that humans don't  
[00:41:36] use reinforcement learning, as I said. I think they do something different.  
[00:41:42] Reinforcement learning is a lot worse than I think the average person thinks. Reinforcement  
[00:41:48] learning is terrible. It just so happens that everything that we had before it is  
[00:41:53] much worse because previously we were just imitating people, so it has all these issues.  
[00:41:59] In reinforcement learning, say you're solving a math problem, because it's very simple.  
[00:42:04] You're given a math problem and you're trying to find the solution.  
[00:42:08] In reinforcement learning, you will try lots of things in parallel first.  
[00:42:13] You're given a problem, you try hundreds of different attempts. These attempts can be complex.  
[00:42:18] They can be like, "Oh, let me try this, let me try that, this didn't work, that didn't work," etc.  
[00:42:22] Then maybe you get an answer. Now you check the back of the book and you see,  
[00:42:25] "Okay, the correct answer is this." You can see that this one, this one,  
[00:42:30] and that one got the correct answer, but these other 97 of them didn't.  
[00:42:33] Literally what reinforcement learning does is it goes to the ones that worked really well and every  
[00:42:37] single thing you did along the way, every single token gets upweighted like, "Do more of this."  
[00:42:42] The problem with that is people will say that your estimator has high variance,  
[00:42:46] but it's just noisy. It's noisy. It almost assumes that every single little piece of the solution  
[00:42:53] that you made that arrived at the right answer was the correct thing to do, which is not true.  
[00:42:56] You may have gone down the wrong alleys until you arrived at the right solution.  
[00:43:00] Every single one of those incorrect things you did, as long as you got to the correct solution,  
[00:43:04] will be upweighted as, "Do more of this." It's terrible. It's noise. You've done all  
[00:43:08] this work only to find, at the end, you get a single number of like, "Oh, you did correct."  
[00:43:14] Based on that, you weigh that entire trajectory as like, upweight or downweight.  
[00:43:19] The way I like to put it is you're sucking supervision through a straw.  
[00:43:22] You've done all this work that could be a minute of rollout,  
[00:43:24] and you're sucking the bits of supervision of the final reward signal through a straw and you're  
[00:43:33] broadcasting that across the entire trajectory and using that to upweight or downweight that  
[00:43:37] trajectory. It's just stupid and crazy. A human would never do this.  
[00:43:39] Number one, a human would never do hundreds of rollouts.  
[00:43:43] Number two, when a person finds a solution, they will have a pretty complicated process  
[00:43:47] of review of, "Okay, I think these parts I did well, these parts I did not do that well.  
[00:43:51] I should probably do this or that." They think through things. There's  
[00:43:55] nothing in current LLMs that does this. There's no equivalent of it. But I do see  
[00:44:00] papers popping out that are trying to do this because it's obvious to everyone in the field.  
[00:44:05] The first imitation learning, by the way, was extremely surprising and miraculous and amazing,  
[00:44:09] that we can fine-tune by imitation on humans. That was incredible. Because in the beginning,  
[00:44:14] all we had was base models. Base models are autocomplete. It wasn't obvious to  
[00:44:18] me at the time, and I had to learn this. The paper that blew my mind was InstructGPT,  
[00:44:24] because it pointed out that you can take the pretrained model, which is autocomplete,  
[00:44:28] and if you just fine-tune it on text that looks like conversations, the model will very rapidly  
[00:44:32] adapt to become very conversational, and it keeps all the knowledge from pre-training.  
[00:44:36] This blew my mind because I didn't understand that stylistically, it can adjust so quickly  
[00:44:41] and become an assistant to a user through just a few loops of fine-tuning on that kind of data.  
[00:44:46] It was very miraculous to me that that worked. So incredible. That was two to three years of  
[00:44:51] work. Now came RL. And RL allows you to do a bit better than just imitation learning because you  
[00:44:58] can have these reward functions and you can hill-climb on the reward functions.  
[00:45:02] Some problems have just correct answers, you can hill-climb on that without getting expert  
[00:45:06] trajectories to imitate. So that's amazing. The model can also discover solutions that a human  
[00:45:10] might never come up with. This is incredible. Yet, it's still stupid. We need more. I saw a  
[00:45:19] paper from Google yesterday that tried to have this reflect & review idea in mind.  
[00:45:25] Was it the memory bank paper or something? I don't know. I've seen a few papers along these lines.  
[00:45:30] So I expect there to be some major update to how we do algorithms for LLMs coming in that realm.  
[00:45:37] I think we need three or four or five more, something like that.  
[00:45:42] You're so good at coming up with evocative phrases. "Sucking supervision through a  
[00:45:47] straw." It's so good. You're saying the problem with outcome-based reward is that you have this  
[00:45:56] huge trajectory, and then at the end, you're trying to learn every single possible thing  
[00:46:01] about what you should do and what you should learn about the world from that one final bit.  
[00:46:07] Given the fact that this is obvious, why hasn't process-based supervision as an alternative been  
[00:46:11] a successful way to make models more capable? What has been preventing us from using  
[00:46:15] this alternative paradigm? Process-based supervision just  
[00:46:18] refers to the fact that we're not going to have a reward function only at the very end.  
[00:46:21] After you've done 10 minutes of work, I'm not going to tell you you did well or not well.  
[00:46:24] I'm going to tell you at every single step of the way how well you're doing.  
[00:46:28] The reason we don't have that is it's tricky how you do that properly.  
[00:46:32] You have partial solutions and you don't know how to assign credit.  
[00:46:34] So when you get the right answer, it's just an equality match to the answer. It’s very  
[00:46:39] simple to implement. If you're doing process supervision, how do you assign in an automatable  
[00:46:44] way, a partial credit assignment? It's not obvious how you do it.  
[00:46:47] Lots of labs are trying to do it with these LLM judges.  
[00:46:50] You get LLMs to try to do it. You prompt an LLM, "Hey,  
[00:46:53] look at a partial solution of a student. How well do you think they're doing if the  
[00:46:56] answer is this?" and they try to tune the prompt. The reason that this is tricky is quite subtle.  
[00:47:02] It's the fact that anytime you use an LLM to assign a reward, those LLMs are giant things  
[00:47:07] with billions of parameters, and they're gameable. If you're reinforcement learning with respect to  
[00:47:11] them, you will find adversarial examples for your LLM judges, almost guaranteed.  
[00:47:15] So you can't do this for too long. You do maybe 10 steps or 20 steps, and maybe  
[00:47:18] it will work, but you can't do 100 or 1,000. I understand it's not obvious, but basically  
[00:47:25] the model will find little cracks. It will find all these spurious  
[00:47:30] things in the nooks and crannies of the giant model and find a way to cheat it.  
[00:47:34] One example that's prominently in my mind, this was probably public, if you're using an LLM judge  
[00:47:42] for a reward, you just give it a solution from a student and ask it if the student did well or not.  
[00:47:47] We were training with reinforcement learning against  
[00:47:49] that reward function, and it worked really well. Then, suddenly, the reward became extremely large.  
[00:47:55] It was a massive jump, and it did perfect. You're looking at it like, "Wow, this means  
[00:47:59] the student is perfect in all these problems. It's fully solved math." But when you look at  
[00:48:05] the completions that you're getting from the model, they are complete nonsense.  
[00:48:08] They start out okay, and then they change to "dhdhdhdh."  
[00:48:11] It's just like, "Oh, okay, let's take two plus three and we do this and this, and then dhdhdhdh."  
[00:48:15] You're looking at it, and it's like, this is crazy.  
[00:48:17] How is it getting a reward of one or 100%? You look at the LLM judge, and it turns out  
[00:48:21] that "dhdhdhdh" is an adversarial example for the model, and it assigns 100% probability to it.  
[00:48:27] It's just because this is an out-of-sample example to the LLM.  
[00:48:30] It's never seen it during training, and you're in pure generalization land.  
[00:48:34] It's never seen it during training, and in the pure generalization land, you can find  
[00:48:37] these examples that break it. You're basically training  
[00:48:42] the LLM to be a prompt injection model. Not even that. Prompt injection is way too fancy.  
[00:48:46] You're finding adversarial examples, as they're called.  
[00:48:48] These are nonsensical solutions that are obviously wrong, but the model thinks they are amazing.  
[00:48:55] To the extent you think this is the bottleneck to making RL more functional,  
[00:48:59] then that will require making LLMs better judges, if you want to do this in an automated way.  
[00:49:05] Is it just going to be some sort of GAN-like approach where you  
[00:49:07] have to train models to be more robust? The labs are probably doing all that.  
[00:49:11] The obvious thing is, "dhdhdhdh" should not get 100% reward.  
[00:49:14] Okay, well, take "dhdhdhdh," put it in the training set of the LLM judge,  
[00:49:17] and say this is not 100%, this is 0%. You can do this, but every time you do  
[00:49:21] this, you get a new LLM, and it still has adversarial examples.  
[00:49:24] There's an infinity of adversarial examples. Probably if you iterate this a few times, it'll  
[00:49:29] probably be harder and harder to find adversarial examples, but I'm not 100% sure because this thing  
[00:49:32] has a trillion parameters or whatnot. I bet you the labs are trying.  
[00:49:41] I still think we need other ideas. Interesting. Do you have some shape  
[00:49:46] of what the other idea could be? This idea of a review solution  
[00:49:54] encompassing synthetic examples such that when you train on them, you get better,  
[00:49:58] and meta-learn it in some way. I think there are some papers  
[00:50:00] that I'm starting to see pop out. I am only at a stage of reading abstracts  
[00:50:04] because a lot of these papers are just ideas. Someone has to make it work on a frontier  
[00:50:08] LLM lab scale in full generality because when you see these papers,  
[00:50:13] they pop up, and it's just a bit noisy. They're cool ideas, but I haven't seen  
[00:50:17] anyone convincingly show that this is possible. That said, the LLM labs are fairly closed,  
[00:50:23] so who knows what they're doing now. I can conceptualize how you would be able  
[00:50:33] to train on synthetic examples or synthetic problems that you have made for yourself.  
[00:50:36] But there seems to be another thing humans do—maybe sleep is this, maybe daydreaming is  
[00:50:40] this—which is not necessarily to come up with fake problems, but just to reflect.  
[00:50:47] I'm not sure what the ML analogy is for daydreaming or sleeping, or just reflecting.  
[00:50:51] I haven't come up with a new problem. Obviously, the very basic analogy would just  
[00:50:54] be fine-tuning on reflection bits, but I feel like in practice that probably wouldn't work that well.  
[00:51:00] Do you have some take on what the analogy of this thing is?  
[00:51:05] I do think that we're missing some aspects there. As an example, let’s take reading a book.  
[00:51:11] Currently when LLMs are reading a book, what that means is we stretch out the sequence of text,  
[00:51:15] and the model is predicting the next token, and it's getting some knowledge from that.  
[00:51:19] That's not really what humans do. When you're reading a book,  
[00:51:21] I don't even feel like the book is exposition I'm supposed to be attending to and training on.  
[00:51:25] The book is a set of prompts for me to do synthetic data generation,  
[00:51:30] or for you to get to a book club and talk about it with your friends.  
[00:51:33] It's by manipulating that information that you actually gain that knowledge.  
[00:51:37] We have no equivalent of that with LLMs. They don't really do that. I'd love to see during  
[00:51:42] pre-training some stage that thinks through the material and tries to reconcile it with  
[00:51:46] what it already knows, and thinks through it for some amount of time and gets that to work.  
[00:51:52] There's no equivalence of any of this. This is all research. There are some  
[00:51:54] subtle—very subtle that I think are very hard to understand—reasons why it's not trivial.  
[00:51:59] If I can just describe one: why can't we just synthetically generate and train on it?  
[00:52:04] Because every synthetic example, if I just give synthetic generation of  
[00:52:07] the model thinking about a book, you look at it and you're like, "This looks great.  
[00:52:10] Why can't I train on it?" You could try, but the model  
[00:52:12] will get much worse if you continue trying. That's because all of the samples you get  
[00:52:17] from models are silently collapsed. Silently—it is not obvious if you look  
[00:52:21] at any individual example of it—they occupy a very tiny manifold of the possible space of  
[00:52:27] thoughts about content. The LLMs, when they come off,  
[00:52:30] they're what we call "collapsed." They have a collapsed data distribution.  
[00:52:34] One easy way to see it is to go to ChatGPT and ask it, "Tell me a joke."  
[00:52:38] It only has like three jokes. It's not giving you the whole breadth  
[00:52:41] of possible jokes. It knows like three jokes. They're silently collapsed. You're not getting  
[00:52:47] the richness and the diversity and the entropy from these models as you would get from humans.  
[00:52:52] Humans are a lot noisier, but at least they're not biased,  
[00:52:56] in a statistical sense. They're not silently collapsed. They maintain a huge amount of entropy.  
[00:53:00] So how do you get synthetic data generation to work despite the collapse and while maintaining  
[00:53:05] the entropy? That’s a research problem. Just to make sure I understood, the reason  
[00:53:09] that the collapse is relevant to synthetic data generation is because you want to be able to  
[00:53:13] come up with synthetic problems or reflections which are not already in your data distribution?  
[00:53:20] I guess what I'm saying is, say we have a chapter of a book and I ask an LLM to think about it,  
[00:53:26] it will give you something that looks very reasonable.  
[00:53:28] But if I ask it 10 times, you'll notice that all of them are the same.  
[00:53:31] You can't just keep scaling "reflection" on the same amount of prompt information  
[00:53:39] and then get returns from that. Any individual sample will look okay,  
[00:53:43] but the distribution of it is quite terrible. It's quite terrible in such a way that if  
[00:53:47] you continue training on too much of your own stuff, you actually collapse.  
[00:53:50] I think that there's possibly no fundamental solution to this.  
[00:53:54] I also think humans collapse over time. These analogies are surprisingly good.  
[00:54:00] Humans collapse during the course of their lives. This is why children, they haven't overfit yet.  
[00:54:06] They will say stuff that will shock you because you can see where they're coming from,  
[00:54:09] but it's just not the thing people say, because they're not yet collapsed. But we're  
[00:54:14] collapsed. We end up revisiting the same thoughts. We end up saying more and more of the same stuff,  
[00:54:20] and the learning rates go down, and the collapse continues to get worse,  
[00:54:24] and then everything deteriorates. Have you seen this super interesting  
[00:54:28] paper that dreaming is a way of preventing this kind of overfitting and collapse?  
[00:54:34] The reason dreaming is evolutionary adaptive is to put you in weird situations that are  
[00:54:41] very unlike your day-to-day reality, so as to prevent this kind of overfitting.  
[00:54:44] It's an interesting idea. I do think that when you're generating things  
[00:54:48] in your head and then you're attending to it, you're training on your own samples,  
[00:54:51] you're training on your synthetic data. If you do it for too long,  
[00:54:53] you go off-rails and you collapse way too much. You always have to seek entropy in your life.  
[00:55:01] Talking to other people is a great source of entropy, and things like that.  
[00:55:05] So maybe the brain has also built some internal mechanisms for increasing the amount of entropy  
[00:55:11] in that process. That's an interesting idea. This is a very ill-formed thought so I’ll  
[00:55:16] just put it out and let you react to it. The best learners that we are aware of,  
[00:55:20] which are children, are extremely bad at recollecting information.  
[00:55:25] In fact, at the very earliest stages of childhood, you will forget everything.  
[00:55:29] You're just an amnesiac about everything that happens before a certain year date.  
[00:55:32] But you're extremely good at picking up new languages and learning from the world.  
[00:55:36] Maybe there's some element of being able to see the forest for the trees.  
[00:55:38] Whereas if you compare it to the opposite end of the spectrum, you have LLM pre-training,  
[00:55:44] where these models will literally be able to regurgitate word-for-word what  
[00:55:47] is the next thing in a Wikipedia page. But their ability to learn abstract  
[00:55:52] concepts really quickly, the way a child can, is much more limited.  
[00:55:55] Then adults are somewhere in between, where they don't have the flexibility of childhood  
[00:55:59] learning, but they can memorize facts and information in a way that is harder for kids.  
[00:56:05] I don't know if there's something interesting about that spectrum.  
[00:56:08] I think there's something very interesting about that, 100%.  
[00:56:10] I do think that humans have a lot more of an element, compared to LLMs, of seeing  
[00:56:16] the forest for the trees. We're not actually that good  
[00:56:19] at memorization, which is actually a feature. Because we're not that good at memorization, we're  
[00:56:25] forced to find patterns in a more general sense. LLMs in comparison are extremely good  
[00:56:33] at memorization. They will recite  
[00:56:35] passages from all these training sources. You can give them completely nonsensical data.  
[00:56:41] You can hash some amount of text or something like that, you get a completely random sequence.  
[00:56:44] If you train on it, even just for a single iteration or two, it can suddenly regurgitate  
[00:56:48] the entire thing. It will memorize it. There's no way a person can read a single  
[00:56:51] sequence of random numbers and recite it to you. That's a feature, not a bug, because it forces  
[00:56:58] you to only learn the generalizable components. Whereas LLMs are distracted by all the memory  
[00:57:03] that they have of the pre-training documents, and it's probably very  
[00:57:06] distracting to them in a certain sense. So that's why when I talk about the  
[00:57:10] cognitive core, I want to remove the memory, which is what we talked about.  
[00:57:13] I'd love to have them have less memory so that they have to look things up,  
[00:57:17] and they only maintain the algorithms for thought, and the idea of an experiment,  
[00:57:22] and all this cognitive glue of acting. And this is also relevant to preventing  
[00:57:28] model collapse? Let me think. I'm  
[00:57:35] not sure. It's almost like a separate axis. The models are way too good at memorization,  
[00:57:40] and somehow we should remove that. People are much worse, but it's a good thing.  
[00:57:46] What is a solution to model collapse? There are very naive things you could attempt.  
[00:57:52] The distribution over logits should be wider or something.  
[00:57:55] There are many naive things you could try. What ends up being the problem  
[00:57:58] with the naive approaches? That's a great question. You can imagine having  
[00:58:02] a regularization for entropy and things like that. I guess they just don't work as well empirically  
[00:58:06] because right now the models are collapsed. But I will say most of the tasks that we  
[00:58:13] want from them don't actually demand diversity. That’s probably the answer to what's going on.  
[00:58:20] The frontier labs are trying to make the models useful.  
[00:58:22] I feel like the diversity of the outputs is not so much...  
[00:58:26] Number one, it's much harder to work with and evaluate and all this stuff, but maybe it's not  
[00:58:29] what's capturing most of the value. In fact, it's actively penalized.  
[00:58:34] If you're super creative in RL, it's not good. Yeah. Or maybe if you're doing a lot of writing,  
[00:58:39] help from LLMs and stuff like that, it's probably bad because the models will silently give  
[00:58:42] you all the same stuff. They won't explore lots  
[00:58:48] of different ways of answering a question. Maybe this diversity, not as many applications  
[00:58:56] need it so the models don't have it. But then it's a problem at  
[00:58:58] synthetic data generation time, et cetera. So we're shooting ourselves in the foot by not  
[00:59:01] allowing this entropy to maintain in the model. Possibly the labs should try harder.  
[00:59:06] I think you hinted that it's a very fundamental problem, it won't be easy  
[00:59:11] to solve. What's your intuition for that? I don't know if it's super fundamental.  
[00:59:17] I don't know if I intended to say that. I do think that I haven't done these experiments,  
[00:59:23] but I do think that you could probably regularize the entropy to be higher.  
[00:59:26] So you're encouraging the model to give you more and more solutions, but you don't want it to  
[00:59:31] start deviating too much from the training data. It's going to start making up its own language.  
[00:59:34] It's going to start using words that are extremely rare, so it's going to drift too  
[00:59:38] much from the distribution. So I think controlling  
[00:59:41] the distribution is just tricky. It's probably not trivial in that sense.  
[00:59:47] How many bits should the optimal core of intelligence end up being if you  
[00:59:54] just had to make a guess? The thing we put on the  
[00:59:56] von Neumann probes, how big does it have to be? It's really interesting in the history of the  
[01:00:01] field because at one point everything was very scaling-pilled in terms of like, "Oh,  
[01:00:05] we're gonna make much bigger models, trillions of parameter models."  
[01:00:08] What the models have done in size is they've gone up and now they've  
[01:00:14] come down. State-of-the-art models are smaller. Even then, I think they memorized way too much.  
[01:00:20] So I had a prediction a while back that I almost feel like we can get cognitive cores that are  
[01:00:24] very good at even a billion parameters. If you talk to a billion parameter model,  
[01:00:30] I think in 20 years, you can have a very productive conversation.  
[01:00:34] It thinks and it's a lot more like a human. But if you ask it some factual question, it might  
[01:00:39] have to look it up, but it knows that it doesn't know and it might have to look it up and it will  
[01:00:42] just do all the reasonable things. That's surprising that you think  
[01:00:44] it'll take a billion parameters. Because already we have billion  
[01:00:47] parameter models or a couple billion parameter models that are very intelligent.  
[01:00:51] Well, state-of-the-art models are like a trillion parameters.  
[01:00:53] But they remember so much stuff. Yeah, but I'm surprised that in 10 years,  
[01:00:58] given the pace… We have gpt-oss-20b. That's way better than GPT-4 original,  
[01:01:07] which was a trillion plus parameters. Given that trend, I'm surprised you  
[01:01:11] think in 10 years the cognitive core is still a billion parameters.  
[01:01:15] I'm surprised you're not like, "Oh it's gonna be like tens of millions or millions."  
[01:01:22] Here's the issue, the training data is the internet, which is really terrible.  
[01:01:26] There's a huge amount of gains to be made because the internet is terrible.  
[01:01:29] Even the internet, when you and I think of the internet, you're thinking of like The  
[01:01:32] Wall Street Journal. That's not what this is. When you're looking at a pre-training  
[01:01:36] dataset in the frontier lab and you look at a random internet document, it's total garbage.  
[01:01:40] I don't even know how this works at all. It's some like stock tickers, symbols,  
[01:01:46] it's a huge amount of slop and garbage from like all the corners of the internet.  
[01:01:50] It's not like your Wall Street Journal article, that's extremely rare.  
[01:01:53] So because the internet is so terrible, we have to build really big models to compress all that.  
[01:02:00] Most of that compression is memory work instead of cognitive work.  
[01:02:04] But what we really want is the cognitive part, delete the memory.  
[01:02:08] I guess what I'm saying is that we need intelligent models to help us refine even  
[01:02:12] the pre-training set to just narrow it down to the cognitive components.  
[01:02:15] Then I think you get away with a much smaller model because it's a  
[01:02:18] much better dataset and you could train it on it. But probably it's not trained directly on it, it's  
[01:02:22] probably distilled from a much better model still. But why is the distilled version still a billion?  
[01:02:28] I just feel like distillation works extremely well.  
[01:02:30] So almost every small model, if you have a small model, it's almost certainly distilled.  
[01:02:35] Right, but why is the distillation in 10 years not getting below 1 billion?  
[01:02:39] Oh, you think it should be smaller than a billion? I mean, come on, right? I don't  
[01:02:43] know. At some point it should take at least a billion knobs to do something interesting.  
[01:02:49] You're thinking it should be even smaller? Yeah. If you look at the trend over the last  
[01:02:53] few years of just finding low-hanging fruit and going from trillion plus models to models that  
[01:02:57] are literally two orders of magnitude smaller in a matter of two years and having better performance,  
[01:03:03] it makes me think the sort of core of intelligence might be even way, way smaller.  
[01:03:09] Plenty of room at the bottom, to paraphrase Feynman.  
[01:03:11] I feel like I'm already contrarian by talking about a billion parameter  
[01:03:14] cognitive core and you're outdoing me. Maybe we could get a little bit smaller.  
[01:03:23] I do think that practically speaking, you want the model to have some knowledge.  
[01:03:26] You don't want it to be looking up everything because then you can't think in your head.  
[01:03:30] You're looking up way too much stuff all the time.  
[01:03:32] Some basic curriculum needs to be there for knowledge, but it doesn't have esoteric knowledge.  
[01:03:38] We're discussing what plausibly could be the cognitive core.  
[01:03:41] There's a separate question which is what will be the size of frontier models over time?  
[01:03:46] I'm curious if you have predictions. We had increasing scale up to maybe GPT 4.5 and  
[01:03:51] now we're seeing decreasing or plateauing scale. There are many reasons this could be going on.  
[01:03:56] Do you have a prediction going forward? Will the biggest models be bigger,  
[01:04:00] will they be smaller, will they be the same? I don't have a super strong prediction.  
[01:04:07] The labs are just being practical. They have a flops budget and a cost budget.  
[01:04:10] It just turns out that pre-training is not where you want to put most of your flops or your cost.  
[01:04:14] That's why the models have gotten smaller. They are a bit smaller, the pre-training  
[01:04:17] stage is smaller, but they make it up in reinforcement learning,  
[01:04:21] mid-training, and all this stuff that follows. They're just being practical in terms of all the  
[01:04:25] stages and how you get the most bang for the buck. Forecasting that trend is quite hard.  
[01:04:30] I do still expect that there's so much low-hanging fruit. That's my basic expectation.  
[01:04:38] I have a very wide distribution here. Do you expect the low-hanging fruit to be  
[01:04:42] similar in kind to the kinds of things that have been happening over the last two to five years?  
[01:04:49] If I look at nanochat versus nanoGPT and the architectural tweaks you made,  
[01:04:54] is that the flavor of things you expect to continue to keep happening?  
[01:04:58] You're not expecting any giant paradigm shifts. For the most part, yeah. I expect the  
[01:05:01] datasets to get much, much better. When you look at the average datasets,  
[01:05:03] they're extremely terrible. They’re so bad that I  
[01:05:05] don't even know how anything works. Look at the average example in the training set:  
[01:05:10] factual mistakes, errors, nonsensical things. Somehow when you do it at scale,  
[01:05:16] the noise washes away and you're left with some of the signal. Datasets will improve  
[01:05:21] a ton. Everything gets better. Our hardware, all the kernels for running the hardware and  
[01:05:29] maximizing what you get with the hardware. Nvidia is slowly tuning the hardware itself,  
[01:05:33] Tensor Cores, all that needs to happen and will continue to happen.  
[01:05:36] All the kernels will get better and utilize the chip to the max extent.  
[01:05:39] All the algorithms will probably improve over optimization, architecture, and all the modeling  
[01:05:45] components of how everything is done and what the algorithms are that we're even training with.  
[01:05:48] I do expect that nothing dominates. Everything plus 20%. This is roughly what I've seen.  
[01:07:13] People have proposed different ways of charting how much progress we've made towards full AGI.  
[01:07:21] If you can come up with some line, then you can see where that line intersects with AGI  
[01:07:25] and where that would happen on the x-axis. People have proposed it's the education level.  
[01:07:29] We had a high schooler, and then they went to college with RL, and they're going to get a Ph.D.  
[01:07:34] I don't like that one. Or they'll propose horizon  
[01:07:36] length. Maybe they can do tasks that take a minute, they can do those autonomously.  
[01:07:41] Then they can autonomously do tasks that take an hour, a human an hour, a human a week.  
[01:07:46] How do you think about the relevant y-axis here? How should we think about how  
[01:07:53] AI is making progress? I have two answers to that.  
[01:07:55] Number one, I'm almost tempted to reject the question entirely because  
[01:07:59] I see this as an extension of computing. Have we talked about how to chart progress  
[01:08:02] in computing, or how do you chart progress in computing since the 1970s or whatever?  
[01:08:06] What is the y-axis? The whole question is funny from that perspective a little bit.  
[01:08:13] When people talk about AI and the original AGI and how we spoke about it when OpenAI started,  
[01:08:18] AGI was a system you could go to that can do any economically valuable task at human performance  
[01:08:27] or better. That was the definition. I was pretty happy with that at the time.  
[01:08:32] I've stuck to that definition forever, and then people have made up all kinds of other  
[01:08:36] definitions. But I like that definition. The first concession that people make all the time is they  
[01:08:43] just take out all the physical stuff because we're just talking about digital knowledge work.  
[01:08:48] That's a pretty major concession compared to the original definition, which was any task  
[01:08:52] a human can do. I can lift things, etc. AI can't do that, obviously, but we'll take it.  
[01:08:57] What fraction of the economy are we taking away by saying, "Oh, only knowledge work?" I don't know  
[01:09:02] the numbers. I feel about 10% to 20%, if I had to guess, is only knowledge work, someone could work  
[01:09:09] from home and perform tasks, something like that. It's still a really large market.  
[01:09:16] What is the size of the economy, and what is 10% or 20%?  
[01:09:19] We're still talking about a few trillion dollars, even in the US, of market share or work.  
[01:09:26] So it's still a very massive bucket. Going back to the definition,  
[01:09:30] what I would be looking for is to what extent is that definition true?  
[01:09:35] Are there jobs or lots of tasks? If we think of tasks as not jobs but tasks.  
[01:09:40] It's difficult because the problem is society will refactor based on the tasks that make up jobs,  
[01:09:47] based on what's automatable or not. Today, what jobs are replaceable by AI?  
[01:09:52] A good example recently was Geoff Hinton's prediction that radiologists would not be  
[01:09:57] a job anymore, and this turned out to be very wrong in a bunch of ways.  
[01:10:00] Radiologists are alive and well and growing, even though computer vision is really,  
[01:10:04] really good at recognizing all the different things that they have to recognize in images.  
[01:10:07] It's just a messy, complicated job with a lot of surfaces and dealing with patients  
[01:10:11] and all this stuff in the context of it. I don't know that by that definition  
[01:10:17] AI has made a huge dent yet. Some of the jobs that I would  
[01:10:22] be looking for have some features that make it very amenable to automation earlier than later.  
[01:10:27] As an example, call center employees often come up, and I think rightly so.  
[01:10:30] Call center employees have a number of simplifying properties with respect to what's automatable  
[01:10:35] today. Their jobs are pretty simple. It's a sequence of tasks, and every task looks similar.  
[01:10:42] You take a phone call with a person, it's 10 minutes of interaction or whatever it is,  
[01:10:45] probably a bit longer. In my experience, a lot longer.  
[01:10:49] You complete some task in some scheme, and you change some database entries  
[01:10:53] around or something like that. So you keep repeating something  
[01:10:55] over and over again, and that's your job. You do want to bring in the task horizon—how  
[01:11:01] long it takes to perform a task—and then you want to also remove context.  
[01:11:05] You're not dealing with different parts of services of companies or other customers.  
[01:11:08] It's just the database, you, and a person you're serving.  
[01:11:11] It's more closed, it's more understandable, it's purely digital.  
[01:11:15] So I would be looking for those things. But even there, I'm not looking  
[01:11:18] at full automation yet. I'm looking for an autonomy slider.  
[01:11:21] I expect that we are not going to instantly replace people.  
[01:11:25] We're going to be swapping in AIs that do 80% of the volume.  
[01:11:29] They delegate 20% of the volume to humans, and humans are supervising teams of five AIs  
[01:11:33] doing the call center work that's more rote. I would be looking for new interfaces or new  
[01:11:39] companies that provide some layer that allows you to manage  
[01:11:44] some of these AIs that are not yet perfect. Then I would expect that across the economy.  
[01:11:48] A lot of jobs are a lot harder than a call center employee.  
[01:11:52] With radiologists, I'm totally speculating and I have no idea what  
[01:11:56] the actual workflow of a radiologist involves. But one analogy that might be applicable is when  
[01:12:03] Waymos were first being rolled out, there'd be a person sitting in the front seat, and you just had  
[01:12:09] to have them there to make sure that if something went really wrong, they're there to monitor.  
[01:12:12] Even today, people are still watching to make sure things are going well.  
[01:12:15] Robotaxi, which was just deployed, still has a person inside it.  
[01:12:19] Now we could be in a similar situation where if you automate 99% of a job, that last 1%  
[01:12:25] the human has to do is incredibly valuable because it's bottlenecking everything else.  
[01:12:29] If it were the case with radiologists, where the person sitting in the front of Waymo has  
[01:12:35] to be specially trained for years in order to provide the last 1%, their wages should  
[01:12:39] go up tremendously because they're the one thing bottlenecking wide deployment.  
[01:12:43] Radiologists, I think their wages have gone up for similar reasons, if you're  
[01:12:46] the last bottleneck and you're not fungible. A Waymo driver might be fungible with others.  
[01:12:53] So you might see this thing where your wages go up until you get to 99% and then fall just  
[01:12:57] like that when the last 1% is gone. And I wonder if we're seeing similar  
[01:13:02] things with radiology or salaries of call center workers or anything like that.  
[01:13:07] That's an interesting question. I don't think we're currently seeing that with radiology.  
[01:13:15] I think radiology is not a good example. I don't know why Geoff Hinton picked  
[01:13:19] on radiology because I think it's an extremely messy, complicated profession.  
[01:13:25] I would be a lot more interested in what's happening with call center employees today,  
[01:13:28] for example, because I would expect a lot of the rote stuff to be automatable today.  
[01:13:32] I don't have first-level access to it but I would be looking for trends of what's  
[01:13:36] happening with the call center employees. Some of the things I would also expect  
[01:13:40] is that maybe they are swapping in AI, but then I would still wait for a year or two  
[01:13:45] because I would potentially expect them to pull back and rehire some of the people.  
[01:13:49] There's been evidence that that's already been happening generally in companies that have been  
[01:13:53] adopting AI, which I think is quite surprising. I also found what was really surprising. AGI,  
[01:13:59] right? A thing which would do everything. We'll take out physical work,  
[01:14:04] but it should be able to do all knowledge work. What you would have naively anticipated is that  
[01:14:09] the way this progression would happen is that you take a little task that a consultant  
[01:14:14] is doing, you take that out of the bucket. You take a little task that an accountant is  
[01:14:19] doing, you take that out of the bucket. Then you're just doing this  
[01:14:22] across all knowledge work. But instead, if we do believe we're  
[01:14:25] on the path of AGI with the current paradigm, the progression is very much not like that.  
[01:14:30] It does not seem like consultants and accountants are getting huge productivity improvements.  
[01:14:34] It's very much like programmers are getting more and more chiseled away at their work.  
[01:14:39] If you look at the revenues of these companies, discounting normal chat revenue—which is similar  
[01:14:46] to Google or something—just looking at API revenues, it's dominated by coding.  
[01:14:51] So this thing which is "general", which should be able to do any knowledge work,  
[01:14:56] is just overwhelmingly doing only coding. It's a surprising way that you would  
[01:15:00] expect the AGI to be deployed. There's an interesting point  
[01:15:04] here. I do believe coding is the perfect first thing for these LLMs and agents.  
[01:15:12] That’s because coding has always fundamentally worked around text.  
[01:15:17] It's computer terminals and text, and everything is based around text.  
[01:15:20] LLMs, the way they're trained on the Internet, love text.  
[01:15:24] They're perfect text processors, and there's all this data out there. It's a perfect fit.  
[01:15:29] We also have a lot of infrastructure pre-built for handling code and text.  
[01:15:33] For example, we have Visual Studio Code or your favorite IDE showing you code,  
[01:15:41] and an agent can plug into that. If an agent has a diff where it made some change,  
[01:15:45] we suddenly have all this code already that shows all the differences to a code base using a diff.  
[01:15:51] It's almost like we've pre-built a lot of the infrastructure for code.  
[01:15:55] Contrast that with some of the things that don't enjoy that at all.  
[01:15:58] As an example, there are people trying to build automation not for coding, but for slides.  
[01:16:03] I saw a company doing slides. That's much, much harder. The reason it's  
[01:16:07] much harder is because slides are not text. Slides are little graphics, they're arranged  
[01:16:11] spatially, and there's a visual component to it. Slides don't have this pre-built infrastructure.  
[01:16:18] For example, if an agent is to make a change to your slides, how does a thing show you the diff?  
[01:16:24] How do you see the diff? There's nothing that shows diffs  
[01:16:26] for slides. Someone has to build it. Some of these things are not amenable to AIs as they are, which  
[01:16:34] are text processors, and code surprisingly is. I’m not sure that alone explains it.  
[01:16:42] I personally have tried to get LLMs to be useful in domains which are just pure language-in,  
[01:16:49] language-out, like rewriting transcripts, coming up with clips based on transcripts.  
[01:16:57] It's very plausible that I didn't do every single possible thing I could do.  
[01:17:00] I put a bunch of good examples in context, but maybe I should have done some kind of fine-tuning.  
[01:17:06] Our mutual friend, Andy Matuschak, told me that he tried 50 billion things to try to get models  
[01:17:13] to be good at writing spaced repetition prompts. Again, very much language-in, language-out tasks,  
[01:17:19] the kind of thing that should be dead center in the repertoire of these LLMs.  
[01:17:22] He tried in-context learning with a few-shot examples.  
[01:17:25] He tried supervised fine-tuning and retrieval. He could not get them to make  
[01:17:35] cards to his satisfaction. So I find it striking that even in language-out  
[01:17:39] domains, it's very hard to get a lot of economic value out of these models separate from coding.  
[01:17:45] I don't know what explains it. That makes sense. I'm not  
[01:17:52] saying that anything text is trivial. I do think that code is pretty structured.  
[01:17:58] Text is maybe a lot more flowery, and there's a lot more entropy in text, I would say.  
[01:18:04] I don't know how else to put it. Also code is hard, and so people feel quite  
[01:18:10] empowered by LLMs, even from simple knowledge. I don't know that I have a very good answer.  
[01:18:19] Obviously, text makes it much, much easier, but it doesn't mean that all text is trivial.  
[01:18:25] How do you think about superintelligence? Do you expect it to feel qualitatively different  
[01:18:29] from normal humans or human companies? I see it as a progression  
[01:18:37] of automation in society. Extrapolating the trend of computing, there will  
[01:18:42] be a gradual automation of a lot of things, and superintelligence will an extrapolation of that.  
[01:18:47] We expect more and more autonomous entities over time that are doing a lot  
[01:18:50] of the digital work and then eventually even the physical work some amount of time later.  
[01:18:56] Basically I see it as just automation, roughly speaking.  
[01:19:00] But automation includes the things humans can already do, and superintelligence  
[01:19:03] implies things humans can’t do. But one of the things that people  
[01:19:05] do is invent new things, which I would just put into the automation if that makes sense.  
[01:19:10] But I guess, less abstractly and more qualitatively, do you expect something  
[01:19:18] to feel like… Because this thing can either think so fast, or has so many copies, or the copies can  
[01:19:26] merge back into themselves, or is much smarter, any number of advantages an AI might have, will  
[01:19:36] the civilization in which these AIs exist just feel qualitatively different from humans?  
[01:19:39] I think it will. It is fundamentally automation, but it will be extremely foreign. It will look  
[01:19:44] really strange. Like you mentioned, we can run all of this on a computer cluster and much faster.  
[01:19:53] Some of the scenarios that I start to get nervous about when the world looks like  
[01:19:58] that is this gradual loss of control and understanding of what's happening.  
[01:20:01] I think that's the most likely outcome, that there will be a gradual loss of understanding.  
[01:20:07] We'll gradually layer all this stuff everywhere, and there will be fewer  
[01:20:10] and fewer people who understand it. Then there will be a gradual loss of  
[01:20:14] control and understanding of what's happening. That to me seems the most likely outcome of how  
[01:20:19] all this stuff will go down. Let me probe on that a bit.  
[01:20:22] It's not clear to me that loss of control and loss of understanding are the same things.  
[01:20:27] A board of directors at TSMC, Intel—name a random company—they're just prestigious 80-year-olds.  
[01:20:37] They have very little understanding, and maybe they don't practically actually have control.  
[01:20:43] A better example  
[01:20:43] is the President of the United States. The President has a lot of fucking power.  
[01:20:48] I'm not trying to make a good statement about the current operant, or maybe I am,  
[01:20:53] but the actual level of understanding is very different from the level of control.  
[01:20:56] I think that's fair. That's a good pushback. I think I expect loss of both.  
[01:21:05] How come? Loss of understanding is obvious, but why loss of control?  
[01:21:10] We're really far into a territory where I don't know what this looks like, but if I  
[01:21:14] were to write sci-fi novels, they would look along the lines of not even a single entity that takes  
[01:21:22] over everything, but multiple competing entities that gradually become more and more autonomous.  
[01:21:27] Some of them go rogue and the others fight them off.  
[01:21:31] It's this hot pot of completely autonomous activity that we've delegated to.  
[01:21:37] I feel it would have that flavor. It is not the fact that they are smarter  
[01:21:43] than us that is resulting in the loss of control. It's the fact that they are competing with each  
[01:21:47] other, and whatever arises out of that competition leads to the loss of control.  
[01:21:58] A lot of these things, they will be tools to people, they're acting on  
[01:22:04] behalf of people or something like that. So maybe those people are in control,  
[01:22:07] but maybe it's a loss of control overall for society in the sense of outcomes we want.  
[01:22:13] You have entities acting on behalf of individuals that are still roughly seen as out of control.  
[01:22:20] This is a question I should have asked earlier. We were talking about how currently it feels like  
[01:22:24] when you're doing AI engineering or AI research, these models are more in the category of compiler  
[01:22:29] rather than in the category of a replacement. At some point, if you have AGI,  
[01:22:34] it should be able to do what you do. Do you feel like having a million  
[01:22:38] copies of you in parallel results in some huge speed-up of AI progress?  
[01:22:43] If that does happen, do you expect to see an intelligence explosion once we have a true AGI?  
[01:22:49] I'm not talking about LLMs today. I do, but it's business as usual because  
[01:22:56] we're in an intelligence explosion already and have been for decades.  
[01:23:00] It's basically the GDP curve that is an exponential weighted sum over so  
[01:23:03] many aspects of the industry. Everything is gradually being  
[01:23:06] automated and has been for hundreds of years. The Industrial Revolution is automation and  
[01:23:10] some of the physical components and tool building and all this stuff.  
[01:23:13] Compilers are early software automation, et cetera.  
[01:23:16] We've been recursively self-improving and exploding for a long time.  
[01:23:21] Another way to see it is that Earth was a pretty boring place if you don't look at the biomechanics  
[01:23:27] and so on, and looked very similar. If you look from space, we're in the  
[01:23:33] middle of this firecracker event, but we're seeing it in slow motion.  
[01:23:38] I definitely feel like this has already happened for a very long time.  
[01:23:42] Again, I don't see AI as a distinct technology with respect to what has  
[01:23:47] already been happening for a long time. You think it's continuous with this  
[01:23:50] hyper-exponential trend? Yes. That's why this was  
[01:23:53] very interesting to me, because I was trying to find AI in the GDP for a while.  
[01:23:57] I thought that GDP should go up. But then I looked at some of the  
[01:24:01] other technologies that I thought were very transformative, like  
[01:24:04] computers or mobile phones or et cetera. You can't find them in GDP. GDP is the same  
[01:24:08] exponential. Even the early iPhone didn't have the App Store, and it didn't have a lot of the bells  
[01:24:13] and whistles that the modern iPhone has. So even though we think of 2008,  
[01:24:18] when the iPhone came out, as this major seismic change, it's actually not.  
[01:24:21] Everything is so spread out and it so slowly diffuses that everything ends up  
[01:24:25] being averaged up into the same exponential. It's the exact same thing with computers.  
[01:24:28] You can't find them in the GDP like, "Oh, we have computers now."  
[01:24:31] That's not what happened, because it's such slow progression.  
[01:24:33] With AI we're going to see the exact same thing. It's just more automation. It allows us to write  
[01:24:37] different kinds of programs that we couldn't write before, but AI is still fundamentally a program.  
[01:24:42] It's a new kind of computer and a new kind of computing system.  
[01:24:46] But it has all these problems, it's going to diffuse over time,  
[01:24:49] and it's still going to add up to the same exponential.  
[01:24:52] We're still going to have an exponential that's going to get extremely vertical.  
[01:24:56] It's going to be very foreign to live in that kind of an environment.  
[01:24:59] Are you saying that, if you look at the trend before the Industrial Revolution to now,  
[01:25:05] you have a hyper-exponential where you go from 0% growth to then 10,000 years ago,  
[01:25:11] 0.02% growth, and to now when we're at 2% growth. That's a hyper-exponential. Are you  
[01:25:15] saying if you're charting AI on there, then AI takes you to 20% growth or 200% growth?  
[01:25:20] Or are you saying that if you look at the last 300 years, what you've been  
[01:25:23] seeing is that you have technology after technology—computers, electrification,  
[01:25:27] steam engines, railways, et cetera—but the rate of growth is the exact same, it's 2%.  
[01:25:33] Are you saying the rate of growth will go up? The rate of growth has also stayed  
[01:25:38] roughly constant, right? Only over the last 200, 300 years.  
[01:25:41] But over the course of human history it's exploded.  
[01:25:44] It's gone from 0% to faster, faster, faster. Industrial explosion, 2%.  
[01:25:51] For a while I tried to find AI or look for AI in the GDP curve,  
[01:25:54] and I've convinced myself that this is false. Even when people talk about recursive  
[01:25:58] self-improvement and labs and stuff like that, this is business as usual.  
[01:26:01] Of course it's going to recursively self-improve, and it's been recursively self-improving.  
[01:26:05] LLMs allow the engineers to work much more efficiently to build the next round of LLM,  
[01:26:11] and a lot more of the components are being automated and tuned and et cetera.  
[01:26:14] All the engineers having access to Google Search is part of it.  
[01:26:19] All the engineers having an IDE, all of them having autocomplete or having Claude code,  
[01:26:23] et cetera, it's all just part of the same speed-up of the whole thing. It's just so smooth.  
[01:26:30] Just to clarify, you're saying that the rate of growth will not change.  
[01:26:35] The intelligence explosion will show up as it just enabled us to continue staying on the  
[01:26:39] 2% growth trajectory, just as the Internet helped us stay on the 2% growth trajectory.  
[01:26:42] Yes, my expectation is that it stays in the same pattern.  
[01:26:47] Just to throw the opposite argument against you, my expectation is that it blows up because I think  
[01:26:55] true AGI—and I'm not talking about LLM coding bots, I'm talking about actual replacement of a  
[01:27:00] human in a server—is qualitatively different from these other productivity-improving  
[01:27:07] technologies because it's labor itself. I think we live in a very labor-constrained world.  
[01:27:13] If you talk to any startup founder or any person, you can be like, what do you need more of? You  
[01:27:17] need really talented people. And if you have billions of extra people who are inventing stuff,  
[01:27:22] integrating themselves, making companies bottom start to finish, that feels qualitatively  
[01:27:28] different from a single technology. It's as if you get 10 billion  
[01:27:32] extra people on the planet. Maybe a counterpoint. I'm pretty willing  
[01:27:37] to be convinced one way or another on this point. But I will say, for example, computing is labor.  
[01:27:42] Computing was labor. Computers, a lot of jobs disappeared because computers  
[01:27:45] are automating a bunch of digital information processing that you now don't need a human for.  
[01:27:50] So computers are labor, and that has played out. Self-driving as an example is also computers doing  
[01:27:57] labor. That's already been playing out. It's still business as usual.  
[01:28:02] You have a machine which is spitting out more things like that at potentially faster pace.  
[01:28:08] Historically, we have examples of the growth regime changing  
[01:28:11] where you went from 0.2% growth to 2% growth. It seems very plausible to me that a machine which  
[01:28:18] is then spitting out the next self-driving car and the next Internet and whatever…  
[01:28:23] I see where it's coming from. At the same time, I do feel like  
[01:28:27] people make this assumption of, "We have God in a box, and now it can do  
[01:28:31] everything," and it just won't look like that. It's going to be able to do some of the things.  
[01:28:36] It's going to fail at some other things. It's going to be gradually put into society,  
[01:28:39] and we'll end up with the same pattern. That is my prediction. This assumption of suddenly  
[01:28:43] having a completely intelligent, fully flexible, fully general human in a box, and we can dispense  
[01:28:49] it at arbitrary problems in society, I don't think that we will have this discrete change.  
[01:28:57] I think we'll arrive at the same kind of gradual diffusion of this across the industry.  
[01:29:03] It often ends up being misleading in these conversations.  
[01:29:09] I don't like to use the word intelligence in this context because intelligence implies you  
[01:29:12] think there'll be a single superintelligence sitting in a server and it'll divine how  
[01:29:18] to come up with new technologies and inventions that cause this explosion.  
[01:29:22] That's not what I'm imagining when I'm imagining 20% growth.  
[01:29:25] I'm imagining that there are billions of very smart human-like minds, potentially,  
[01:29:33] or that's all that's required. But the fact that there's hundreds  
[01:29:36] of millions of them, billions of them, each individually making new products, figuring  
[01:29:41] out how to integrate themselves into the economy. If a highly experienced smart immigrant came to  
[01:29:46] the country, you wouldn't need to figure out how we integrate them in the economy. They figure it  
[01:29:49] out. They could start a company, they could make inventions, or increase productivity in the world.  
[01:29:55] We have examples, even in the current regime, of places that have had 10-20% economic growth.  
[01:30:01] If you just have a lot of people and less capital in comparison to the people,  
[01:30:05] you can have Hong Kong or Shenzhen or whatever with decades of 10% plus growth.  
[01:30:13] There's a lot of really smart people who are ready to make use of the resources and do  
[01:30:17] this period of catch-up because we've had this discontinuity, and I think AI might be similar.  
[01:30:24] I understand, but I still think that you're presupposing some discrete jump.  
[01:30:28] There's some unlock that we're waiting to claim. And suddenly we're going to have  
[01:30:31] geniuses in data centers. I still think you're presupposing  
[01:30:34] some discrete jump that has no historical precedent that I can't find in any of the  
[01:30:39] statistics and that I think probably won't happen. I mean, the Industrial Revolution is such a jump.  
[01:30:43] You went from 0.2% growth to 2% growth. I'm just saying you'll see another jump like that.  
[01:30:49] I'm a little bit suspicious, I would have to take a look.  
[01:30:53] For example, some of the logs are not very good from before the Industrial Revolution.  
[01:30:59] I'm a bit suspicious of it but I don't have strong opinions.  
[01:31:04] You're saying that this was a singular event that was extremely magical.  
[01:31:07] You're saying that maybe there's going to be another event that's going to  
[01:31:09] be just like that, extremely magical. It will break the paradigm, and so on.  
[01:31:12] I actually don't think… The crucial thing with the Industrial Revolution was that it was not magical.  
[01:31:18] If you just zoomed in, what you would see in 1770 or 1870 is not that there was some key invention.  
[01:31:28] But at the same time, you did move the economy to a regime where the progress  
[01:31:32] was much faster and the exponential 10x'd. I expect a similar thing from AI where it's  
[01:31:37] not like there's going to be a single moment where we've made the crucial invention.  
[01:31:42] It’s an overhang that's being unlocked. Like maybe there's a new energy source.  
[01:31:45] There's some unlock—in this case, some kind of a cognitive capacity—and there's an overhang of  
[01:31:49] cognitive work to do. That's right.  
[01:31:52] You're expecting that overhang to be filled by this new technology when it crosses the threshold.  
[01:31:56] Maybe one way to think about it is throughout history, a lot of growth  
[01:32:01] comes because people come up with ideas, and then people are out there doing stuff to  
[01:32:06] execute those ideas and make valuable output. Through most of this time, the population has  
[01:32:11] been exploding. That has been driving growth. For the last 50 years, people  
[01:32:14] have argued that growth has stagnated. The population in frontier countries  
[01:32:17] has also stagnated. I think we go back to  
[01:32:19] the exponential growth in population that causes hyper-exponential growth in output.  
[01:32:28] It's really hard to tell. I understand that viewpoint. I  
[01:32:32] don't intuitively feel that viewpoint. You recommended Nick Lane's book to me.  
[01:33:40] On that basis, I also found it super interesting and I interviewed him.  
[01:33:45] I have some questions about thinking about intelligence and evolutionary history.  
[01:33:49] Now that you, over the last 20 years of doing AI research, you maybe have a more tangible sense of  
[01:33:54] what intelligence is, what it takes to develop it. Are you more or less surprised as a result that  
[01:34:01] evolution just spontaneously stumbled upon it? I love Nick Lane's books. I was just listening  
[01:34:12] to his podcast on the way up here. With respect to intelligence and its  
[01:34:15] evolution, it's very, very recent. I am surprised that it evolved.  
[01:34:23] I find it fascinating to think about all the worlds out there.  
[01:34:25] Say there's a thousand planets like Earth and what they look like.  
[01:34:27] I think Nick Lane was here talking about some of the earliest parts.  
[01:34:30] He expects very similar life forms, roughly speaking,  
[01:34:34] and bacteria-like things in most of them. There are a few breaks in there.  
[01:34:39] The evolution of intelligence intuitively feels to me like it should be a fairly rare event.  
[01:34:45] Maybe you should base it on how long something has existed.  
[01:34:49] If bacteria were around for 2 billion years and nothing happened, then going to eukaryote  
[01:34:52] is probably pretty hard because bacteria came up quite early in Earth's evolution or history.  
[01:35:02] How long have we had animals? Maybe a couple hundred million years,  
[01:35:04] multicellular animals that run around, crawl, et cetera.  
[01:35:08] That’s maybe 10% of Earth's lifespan. Maybe on that timescale it's not too tricky.  
[01:35:18] It's still surprising to me, intuitively, that it developed.  
[01:35:20] I would maybe expect just a lot of animal-like life forms doing animal-like things.  
[01:35:24] The fact that you can get something that creates culture and knowledge  
[01:35:28] and accumulates it is surprising to me. There's a couple of interesting follow-ups.  
[01:35:35] If you buy the Sutton perspective that the crux of intelligence is animal intelligence…  
[01:35:41] The quote he said is "If you got to the squirrel, you'd be most of the way to AGI."  
[01:35:46] We got to squirrel intelligence right after the Cambrian explosion 600 million years ago.  
[01:35:51] It seems like what instigated that was the oxygenation event 600 million years ago.  
[01:35:56] But immediately the intelligence algorithm was there to make the squirrel intelligence.  
[01:36:02] It's suggestive that animal intelligence was like that.  
[01:36:06] As soon as you had the oxygen in the environment, you had the eukaryote,  
[01:36:09] you could just get the algorithm. Maybe it was an accident that  
[01:36:14] evolution stumbled upon it so fast, but I don't know if that suggests that  
[01:36:18] at the end it's going to be quite simple. It's so hard to tell with any of this stuff.  
[01:36:23] You can base it a bit on how long something has existed or how long  
[01:36:26] it feels like something has been bottlenecked. Nick Lane is very good about describing this very  
[01:36:30] apparent bottleneck in bacteria and archaea. For two billion years, nothing happened.  
[01:36:34] There’s extreme diversity of biochemistry, and yet nothing grows to become animals.  
[01:36:41] Two billion years. I don't know that we've seen exactly that kind of an equivalent with  
[01:36:46] animals and intelligence, to your point. We could also look at it with respect  
[01:36:51] to how many times we think certain intelligence has individually sprung up.  
[01:36:55] That's a really good thing to investigate. One thought on that. There's hominid intelligence,  
[01:37:03] and then there's bird intelligence. Ravens, etc., are extremely clever,  
[01:37:07] but their brain parts are quite distinct, and we don't have that much in common.  
[01:37:13] That's a slight indication of maybe intelligence springing up a few times.  
[01:37:18] In that case, you'd expect it more frequently. A former guest, Gwern, and Carl Shulman, they’ve  
[01:37:26] made a really interesting point about that. Their perspective is that the scalable algorithm  
[01:37:32] which humans have and primates have, arose in birds as well, and maybe other times as well.  
[01:37:39] But humans found an evolutionary niche which rewarded marginal increases in intelligence  
[01:37:47] and also had a scalable brain algorithm that could achieve those increases in intelligence.  
[01:37:53] For example, if a bird had a bigger brain, it would just collapse out of the air.  
[01:37:57] It's very smart for the size of its brain, but it's not in a niche  
[01:38:00] which rewards the brain getting bigger. It’s maybe similar to some really smart…  
[01:38:08] Like dolphins? Exaclty, humans, we have hands that  
[01:38:10] reward being able to learn how to do tool use. We can externalize digestion, more energy to  
[01:38:14] the brain, and that kicks off the flywheel. Also stuff to work with. I'm guessing it would  
[01:38:19] be harder if I were a dolphin. How do you have fire? The universe of things you can do in water,  
[01:38:28] inside water, is probably lower than what you can do on land, just chemically.  
[01:38:33] I do agree with this viewpoint of these niches and what's being incentivized. I still find it  
[01:38:38] miraculous. I would have expected things to get stuck on animals with bigger muscles.  
[01:38:47] Going through intelligence is a really fascinating breaking point.  
[01:38:51] The way Gwern put it is the reason it was so hard is that it's a very tight line between being in  
[01:38:56] a situation where something is so important to learn that it's not worth distilling the  
[01:39:03] exact right circuits directly back into your DNA, versus it's not important enough to learn at all.  
[01:39:10] It has to be something that incentivizes building the algorithm to learn in a lifetime.  
[01:39:17] You have to incentivize some kind of adaptability. You want environments that are unpredictable  
[01:39:21] so evolution can't bake your algorithms into your weights.  
[01:39:24] A lot of animals are pre-baked in this sense. Humans have to figure it out at test  
[01:39:30] time when they get born. You want these environments  
[01:39:35] that change really rapidly, where you can't foresee what will work well.  
[01:39:42] You create intelligence to figure it out at test time.  
[01:39:45] Quintin Pope had this interesting blog post where he's saying the reason he doesn't  
[01:39:48] expect a sharp takeoff is that humans had the sharp takeoff where 60,000 years ago we seem  
[01:39:55] to have had the cognitive architectures that we have today. 10,000 years ago,  
[01:39:59] agricultural revolution, modernity. What was happening in that 50,000 years?  
[01:40:04] You had to build this cultural scaffold where you can accumulate knowledge over generations.  
[01:40:11] This is an ability that exists for free in the way we do AI training.  
[01:40:16] In many cases they are literally distilled. If you retrain a model, they can be trained  
[01:40:21] on each other, they can be trained on the same pre-training corpus,  
[01:40:25] they don't literally have to start from scratch. There's a sense in which it took humans a long  
[01:40:31] time to get this cultural loop going, but it just comes for free with the way we do LLM training.  
[01:40:36] Yes and no. Because LLMs don't really have the equivalent of culture.  
[01:40:39] Maybe we're giving them way too much and incentivizing not to  
[01:40:42] create it or something like that. But the invention of culture and of  
[01:40:45] written record and of passing down notes between each other, I don't think there's  
[01:40:48] an equivalent of that with LLMs right now. LLMs don't really have culture right now and  
[01:40:53] it's one of the impediments I would say. Can you give me some sense of what  
[01:40:58] LLM culture might look like? In the simplest case it would be a  
[01:41:01] giant scratchpad that the LLM can edit and as it's reading stuff or as it's helping out with work,  
[01:41:06] it's editing the scratchpad for itself. Why can't an LLM write a book for the other  
[01:41:10] LLMs? That would be cool. Why can't other LLMs read this LLM's book and be inspired  
[01:41:16] by it or shocked by it or something like that? There's no equivalence for any of this stuff.  
[01:41:20] Interesting. When would you expect that kind of thing to start happening?  
[01:41:24] Also, multi-agent systems and a sort of independent AI civilization and culture?  
[01:41:31] There are two powerful ideas in the realm of multi-agent that have both  
[01:41:34] not been really claimed or so on. The first one I would say is culture  
[01:41:38] and LLMs having a growing repertoire of knowledge for their own purposes.  
[01:41:44] The second one looks a lot more like the powerful idea of self-play.  
[01:41:47] In my mind it’s extremely powerful. Evolution has a lot of competition  
[01:41:53] driving intelligence and evolution. In AlphaGo more algorithmically,  
[01:41:59] AlphaGo is playing against itself and that's how it learns to get really good at Go.  
[01:42:03] There's no equivalent of self-playing LLMs, but I would expect that to also exist.  
[01:42:07] No one has done it yet. Why can't an LLM for example, create a bunch  
[01:42:10] of problems that another LLM is learning to solve? Then the LLM is always trying to serve more and  
[01:42:16] more difficult problems, stuff like that. There's a bunch of ways to organize it.  
[01:42:22] It's a realm of research, but I haven't seen anything that convincingly claims  
[01:42:26] both of those multi-agent improvements. We're mostly in the realm of a single  
[01:42:31] individual agent, but that will change. In the realm of culture also,  
[01:42:37] I would also bucket organizations. We haven't seen anything like that convincingly  
[01:42:41] either. That's why we're still early. Can you identify the key bottleneck  
[01:42:45] that's preventing this kind of collaboration between LLMs?  
[01:42:50] Maybe the way I would put it is, some of these analogies work and  
[01:42:56] they shouldn't, but somehow, remarkably, they do. A lot of the smaller models, or the dumber models,  
[01:43:01] remarkably resemble a kindergarten student, or an elementary school student or high school student.  
[01:43:07] Somehow, we still haven't graduated enough where this stuff can take over.  
[01:43:12] My Claude Code or Codex, they still feel like this elementary-grade student.  
[01:43:17] I know that they can take PhD quizzes, but they still cognitively feel like a  
[01:43:21] kindergarten or an elementary school student. I don't think they can create culture because  
[01:43:24] they're still kids. They're savant kids. They have perfect memory of all this stuff.  
[01:43:33] They can convincingly create all kinds of slop that looks really good.  
[01:43:36] But I still think they don't really know what they're doing and they don't really  
[01:43:38] have the cognition across all these little checkboxes that we still have to collect.  
[01:43:43] You've talked about how you were at Tesla leading self-driving from 2017 to 2022.  
[01:43:50] And you firsthand saw this progress from cool demos to now thousands of cars out there actually  
[01:43:58] autonomously doing drives. Why did that take a decade?  
[01:44:01] What was happening through that time? One thing I will almost instantly push  
[01:44:06] back on is that this is not even near done, in a bunch of ways that I'm going to get to.  
[01:44:13] Self-driving is very interesting because it's definitely where I get a lot of my  
[01:44:16] intuitions because I spent five years on it. It has this entire history where the first demos  
[01:44:22] of self-driving go all the way to the 1980s. You can see a demo from CMU in 1986.  
[01:44:28] There's a truck that's driving itself on roads. Fast forward. When I was joining Tesla,  
[01:44:34] I had a very early demo of Waymo. It basically gave me a perfect drive  
[01:44:40] in 2014 or something like that, so a perfect Waymo drive a decade ago.  
[01:44:46] It took us around Palo Alto and so on because I had a friend who worked there.  
[01:44:50] I thought it was very close and then it still took a long time.  
[01:44:54] For some kinds of tasks and jobs and so on, there's a very large demo-to-product gap where the  
[01:45:02] demo is very easy, but the product is very hard. It's especially the case in cases like  
[01:45:07] self-driving where the cost of failure is too high.  
[01:45:11] Many industries, tasks, and jobs maybe don't have that property, but when you do have that property,  
[01:45:15] that definitely increases the timelines. For example, in software engineering,  
[01:45:19] I do think that property does exist. For a lot of vibe coding, it doesn't.  
[01:45:24] But if you're writing actual production-grade code, that property should exist, because any  
[01:45:28] kind of mistake leads to a security vulnerability or something like that.  
[01:45:32] Millions and hundreds of millions of people's personal Social Security numbers  
[01:45:36] get leaked or something like that. So in software, people should be careful,  
[01:45:42] kind of like in self-driving. In self-driving, if things go wrong,  
[01:45:46] you might get injured. There are worse outcomes. But in software, it's almost  
[01:45:52] unbounded how terrible something could be. I do think that they share that property.  
[01:45:59] What takes the long amount of time and the way to think about it is that it's a march of nines.  
[01:46:04] Every single nine is a constant amount of work. Every single nine is the same amount of work.  
[01:46:10] When you get a demo and something works 90% of the time, that's just the first nine.  
[01:46:16] Then you need the second nine, a third nine, a fourth nine, a fifth nine.  
[01:46:18] While I was at Tesla for five years or so, we went through maybe three nines or two nines.  
[01:46:23] I don't know what it is, but multiple nines of iteration.  
[01:46:25] There are still more nines to go. That's why these things take so long.  
[01:46:31] It's definitely formative for me, seeing something that was a demo. I'm very  
[01:46:35] unimpressed by demos. Whenever I see demos of anything, I'm extremely unimpressed by that.  
[01:46:43] If it's a demo that someone cooked up as a showing, it's worse.  
[01:46:45] If you can interact with it, it's a bit better.  
[01:46:47] But even then, you're not done. You need the actual product. It's going to face all these  
[01:46:50] challenges when it comes in contact with reality and all these different  
[01:46:53] pockets of behavior that need patching. We're going to see all this stuff play  
[01:46:57] out. It's a march of nines. Each nine is constant. Demos are encouraging. It’s still  
[01:47:01] a huge amount of work to do. It is a critical safety domain,  
[01:47:07] unless you're doing vibe coding, which is all nice and fun and so on.  
[01:47:11] That's why this also enforced my timelines from that perspective.  
[01:47:16] It's very interesting to hear you say that, that the safety guarantees you need from software  
[01:47:20] are not dissimilar to self-driving. What people will often say is that  
[01:47:24] self-driving took so long because the cost of failure is so high.  
[01:47:30] A human makes a mistake on average every 400,000 miles or every seven years.  
[01:47:34] If you had to release a coding agent that couldn't make a mistake for at least seven years,  
[01:47:39] it would be much harder to deploy. But your point is that if you made a  
[01:47:43] catastrophic coding mistake, like breaking some important system every seven years...  
[01:47:47] Very easy to do. In fact, in terms of wall clock time,  
[01:47:51] it would be much less than seven years because you're constantly outputting code like that.  
[01:47:57] In terms of tokens, it would be seven years. But in terms of wall clock time...  
[01:48:00] In some ways, it's a much harder problem. Self-driving is just one of  
[01:48:02] thousands of things that people do. It's almost like a single vertical, I suppose.  
[01:48:07] Whereas when we're talking about general software engineering,  
[01:48:08] it's even more... There's more surface area. There's another objection people make to that  
[01:48:14] analogy, which is that with self-driving, what took a big fraction of that time was solving  
[01:48:21] the problem of having basic perception that's robust, building representations,  
[01:48:27] and having a model that has some common sense so it can generalize to when it sees  
[01:48:32] something that's slightly out of distribution. If somebody's waving down the road this way,  
[01:48:37] you don't need to train for it. The thing will have some understanding  
[01:48:40] of how to respond to something like that. These are things we're getting for free  
[01:48:44] with LLMs or VLMs today, so we don't have to solve these very basic representation problems.  
[01:48:49] So now deploying AIs across different domains will sort of be like deploying a self-driving  
[01:48:54] car with current models to a different city, which is hard but not like a 10-year-long task.  
[01:48:59] I'm not 100% sure if I fully agree with that. I don't know how much we're getting for free.  
[01:49:03] There's still a lot of gaps in understanding what we are getting.  
[01:49:07] We're definitely getting more generalizable intelligence in a  
[01:49:10] single entity, whereas self-driving is a very special-purpose task that requires.  
[01:49:14] In some sense building a special-purpose task is maybe even harder in a certain sense because  
[01:49:18] it doesn't fall out from a more general thing that you're doing at scale, if that makes sense.  
[01:49:24] But the analogy still doesn't fully resonate because the LLMs are still  
[01:49:30] pretty fallible and they have a lot of gaps that still need to be filled in.  
[01:49:33] I don't think that we're getting magical generalization  
[01:49:35] completely out of the box, in a certain sense. The other aspect that I wanted to return to is  
[01:49:42] that self-driving cars are nowhere near done still. The deployments are pretty minimal.  
[01:49:51] Even Waymo and so on has very few cars. They're doing that roughly speaking  
[01:49:54] because they're not economical. They've built something that lives in the future.  
[01:50:00] They've had to pull back the future, but they had to make it uneconomical.  
[01:50:05] There are all these costs, not just marginal costs for those cars and  
[01:50:09] their operation and maintenance, but also the capex of the entire thing.  
[01:50:13] Making it economical is still going to be a slog for them.  
[01:50:17] Also, when you look at these cars and there's no one driving, I actually think  
[01:50:21] it's a little bit deceiving because there are very elaborate teleoperation centers  
[01:50:26] of people kind of in a loop with these cars. I don't have the full extent of it, but there's  
[01:50:32] more human-in-the-loop than you might expect. There are people somewhere out there  
[01:50:36] beaming in from the sky. I don't know if they're  
[01:50:39] fully in the loop with the driving. Some of the time they are, but they're  
[01:50:42] certainly involved and there are people. In some sense, we haven't actually removed  
[01:50:45] the person, we've moved them to somewhere where you can't see them.  
[01:50:48] I still think there will be some work, as you mentioned, going from environment to environment.  
[01:50:52] There are still challenges to make self-driving real.  
[01:50:55] But I do agree that it's definitely crossed a threshold where it kind of feels real,  
[01:50:59] unless it's really teleoperated. For example, Waymo can't go to  
[01:51:03] all the different parts of the city. My suspicion is that it's parts of the city  
[01:51:07] where you don't get good signal. Anyway, I don't know anything  
[01:51:11] about the stack. I'm just making stuff up. You led self-driving for five years at Tesla.  
[01:51:17] Sorry, I don't know anything about the specifics of Waymo.  
[01:51:21] By the way, I love Waymo and I take it all the time.  
[01:51:24] I just think that people are sometimes a little bit too naive about some of the progress  
[01:51:29] and there's still a huge amount of work. Tesla took in my mind a much more scalable  
[01:51:33] approach and the team is doing extremely well. I'm kind of on the record for predicting  
[01:51:39] how this thing will go. Waymo had an early start  
[01:51:42] because you can package up so many sensors. But I do think Tesla is taking the more  
[01:51:45] scalable strategy and it's going to look a lot more like that.  
[01:51:48] So this will still have to play out and hasn't. But I don't want to talk about self-driving as  
[01:51:54] something that took a decade because it didn't take it yet, if that makes sense.  
[01:51:59] Because one, the start is at 1980 and not 10 years ago, and then two, the end is not here yet.  
[01:52:05] The end is not near yet because when we're talking about self-driving,  
[01:52:08] usually in my mind it's self-driving at scale. People don't have to get a driver's license, etc.  
[01:52:13] I'm curious to bounce two other ways in which the analogy might be different.  
[01:52:19] The reason I'm especially curious about this is because the question of how fast AI is deployed,  
[01:52:24] how valuable it is when it's early on is potentially the most important  
[01:52:28] question in the world right now. If you're trying to model what the  
[01:52:31] year 2030 looks like, this is the question you ought to have some understanding of.  
[01:52:36] Another thing you might think is one, you have this latency requirement with self-driving.  
[01:52:42] I have no idea what the actual models are, but I assume it’s like tens of millions of parameters  
[01:52:45] or something, which is not the necessary constraint for knowledge work with LLMs.  
[01:52:51] Maybe it might be with computer use and stuff. But the other big one is, maybe more  
[01:52:56] importantly, on this capex question. Yes, there is additional cost to serving  
[01:53:02] up an additional copy of a model, but the opex of a session is quite low and you can amortize  
[01:53:12] the cost of AI into the training run itself, depending on how inference scaling goes and stuff.  
[01:53:17] But it's certainly not as much as building a whole new car to serve another instance of a model.  
[01:53:23] So the economics of deploying more widely are much more favorable.  
[01:53:28] I think that's right. If you're sticking to the realm of bits,  
[01:53:31] bits are a million times easier than anything that touches the physical world. I definitely  
[01:53:36] grant that. Bits are completely changeable, arbitrarily reshuffleable at a very rapid speed.  
[01:53:42] You would expect a much faster adaptation also in the industry and so on. What was the first one?  
[01:53:50] The latency requirements and its implications for model size?  
[01:53:53] I think that's roughly right. I also think that if we are talking about  
[01:53:56] knowledge work at scale, there will be some latency requirements, practically speaking,  
[01:54:00] because we're going to have to create a huge amount of compute and serve that.  
[01:54:06] The last aspect that I very briefly want to also talk about is all the rest of it.  
[01:54:13] What does society think about it? What are the legal ramifications? How is it working  
[01:54:17] legally? How is it working insurance-wise? What are those layers of it and aspects of it?  
[01:54:25] What is the equivalent of people putting a cone on a Waymo?  
[01:54:28] There are going to be equivalents of all that. So I feel like self-driving is a very nice  
[01:54:34] analogy that you can borrow things from. What is the equivalent of a cone in the car?  
[01:54:38] What is the equivalent of a teleoperating worker who's hidden away and all the aspects of it.  
[01:54:45] Do you have any opinions on what this implies about the current AI buildout,  
[01:54:49] which would 10x the amount of available compute in the world in a year or two and maybe more  
[01:54:56] than 100x it by the end of the decade. If the use of AI will be lower than  
[01:55:00] some people naively predict, does that mean that we're overbuilding  
[01:55:04] compute or is that a separate question? Kind of like what happened with railroads.  
[01:55:08] With what, sorry? Was it railroads or?  
[01:55:10] Yeah, it was. Yeah. There's historical precedent.  
[01:55:14] Or was it with the telecommunication industry? Pre-paving the internet that only came a decade  
[01:55:18] later and creating a whole bubble in the telecommunications industry in the late '90s.  
[01:55:28] I understand I'm sounding very pessimistic here. I'm actually optimistic. I think this  
[01:55:33] will work. I think it's tractable. I'm only sounding pessimistic because when  
[01:55:36] I go on my Twitter timeline, I see all this stuff that makes no sense to me.  
[01:55:42] There's a lot of reasons for why that exists. A lot of it is honestly just fundraising.  
[01:55:47] It's just incentive structures. A lot of it may be fundraising.  
[01:55:50] A lot of it is just attention, converting attention to money on the internet,  
[01:55:55] stuff like that. There's a lot of  
[01:56:00] that going on, and I'm only reacting to that. But I'm still overall very bullish on technology.  
[01:56:05] We're going to work through all this stuff. There's been a rapid amount of progress.  
[01:56:09] I don't know that there's overbuilding. I think we're going to be able to gobble up what,  
[01:56:15] in my understanding, is being built. For example, Claude Code or OpenAI Codex  
[01:56:20] and stuff like that didn't even exist a year ago. Is that right?  
[01:56:24] This is a miraculous technology that didn't exist. There's going to be a huge amount of demand,  
[01:56:29] as we see the demand in ChatGPT already and so on. So I don't know that there's overbuilding.  
[01:56:37] I'm just reacting to some of the very fast timelines that people continue to say incorrectly.  
[01:56:42] I've heard many, many times over the course of my 15 years in AI where very reputable  
[01:56:46] people keep getting this wrong all the time. I want this to be properly calibrated, and some  
[01:56:53] of this also has geopolitical ramifications and things like that with some of these questions.  
[01:56:59] I don't want people to make mistakes in that sphere of things.  
[01:57:04] I do want us to be grounded in the reality of what technology is and isn't.  
[01:57:08] Let's talk about education and Eureka. One thing you could do is start another AI  
[01:57:15] lab and then try to solve those problems. I’m curious what you're up to now,  
[01:57:21] and why not AI research itself? I guess the way I would put it  
[01:57:26] is I feel some amount of determinism around the things that AI labs are doing.  
[01:57:33] I feel like I could help out there, but I don't know that I would uniquely improve it.  
[01:57:42] My personal big fear is that a lot of this stuff happens on the side of humanity,  
[01:57:46] and that humanity gets disempowered by it. I care not just about all the Dyson spheres  
[01:57:52] that we're going to build and that AI is going to build in a fully autonomous way,  
[01:57:55] I care about what happens to humans. I want humans to be well off in the future.  
[01:58:00] I feel like that's where I can a lot more uniquely add value than  
[01:58:04] an incremental improvement in the frontier lab. I'm most afraid of something depicted in movies  
[01:58:11] like WALL-E or Idiocracy or something like that, where humanity is on the side of this stuff.  
[01:58:16] I want humans to be much, much better in this future.  
[01:58:21] To me, this is through education that you can achieve this.  
[01:58:26] So what are you working on there? The easiest way I can describe it is  
[01:58:30] we're trying to build the Starfleet Academy. I don’t know if you’ve watched Star Trek.  
[01:58:34] I haven’t. Starfleet Academy is  
[01:58:37] this elite institution for frontier technology, building spaceships, and graduating cadets to be  
[01:58:43] the pilots of these spaceships and whatnot. So I just imagine an elite institution for  
[01:58:47] technical knowledge and a kind of school that's very up-to-date and a premier institution.  
[01:58:56] A category of questions I have for you is explaining how one teaches technical or  
[01:59:03] scientific content well, because you are one of the world masters at it.  
[01:59:08] I'm curious both about how you think about it for content you've already put out there  
[01:59:11] on YouTube, but also, to the extent it's any different, how you think about it for Eureka.  
[01:59:16] With respect to Eureka, one thing that is very fascinating to me about education  
[01:59:20] is that I do think education will pretty fundamentally change with AIs on the side.  
[01:59:24] It has to be rewired and changed to some extent. I still think that we're pretty early.  
[01:59:30] There's going to be a lot of people who are going to try to do the obvious things.  
[01:59:33] Have an LLM and ask it questions. Do all the basic things that you would  
[01:59:38] do via prompting right now. It's helpful,  
[01:59:40] but it still feels to me a bit like slop. I'd like to do it properly, and I think the  
[01:59:44] capability is not there for what I would want. What I'd want is an actual tutor experience.  
[01:59:51] A prominent example in my mind is I was recently learning Korean, so language learning.  
[01:59:57] I went through a phase where I was learning Korean by myself on the internet.  
[02:00:00] I went through a phase where I was part of a small class in Korea taking Korean with a bunch of other  
[02:00:06] people, which was really funny. We had a teacher and 10  
[02:00:08] people or so taking Korean. Then I switched to a one-on-one tutor.  
[02:00:13] I guess what was fascinating to me was, I think I had a really good tutor, but just thinking  
[02:00:19] through what this tutor was doing for me and how incredible that experience was and how high the  
[02:00:25] bar is for what I want to build eventually. Instantly from a very short  
[02:00:31] conversation, she understood where I am as a student, what I know and don't know.  
[02:00:35] She was able to probe exactly the kinds of questions or things to understand my world model.  
[02:00:41] No LLM will do that for you 100% right now, not even close.  
[02:00:44] But a tutor will do that if they're good. Once she understands, she really served  
[02:00:49] me all the things that I needed at my current sliver of capability.  
[02:00:52] I need to be always appropriately challenged. I can't be faced with something too hard or  
[02:00:56] too trivial, and a tutor is really good at serving you just the right stuff.  
[02:01:01] I felt like I was the only constraint to learning. I was always given the perfect information. I'm  
[02:01:07] the only constraint. I felt good because I'm the only impediment that exists.  
[02:01:11] It's not that I can't find knowledge or that it's not properly explained or etc.  
[02:01:14] It's just my ability to memorize and so on. This is what I want for people.  
[02:01:18] How do you automate that? Very good question. At  
[02:01:21] the current capability, you don't. That's why I think it's not actually the  
[02:01:26] right time to build this kind of an AI tutor. I still think it's a useful product,  
[02:01:31] and lots of people will build it, but the bar is so high and the capability is not there.  
[02:01:40] Even today, I would say ChatGPT is an extremely valuable educational product.  
[02:01:45] But for me, it was so fascinating to see how high the bar is.  
[02:01:48] When I was with her, I almost felt like there's no way I can build this.  
[02:01:53] But you are building it, right? Anyone who's had a really good  
[02:01:55] tutor is like, "How are you going to build this?" I'm waiting for that capability. I  
[02:02:04] did some AI consulting for computer vision. A lot of times, the value that I brought to  
[02:02:09] the company was telling them not to use AI. I was the AI expert, and they described the  
[02:02:13] problem, and I said, "Don't use AI." This is my value add. I feel like it's  
[02:02:17] the same in education right now, where I feel like for what I have in mind,  
[02:02:21] it's not yet the time, but the time will come. For now, I'm building something that looks  
[02:02:26] maybe a bit more conventional that has a physical and digital component and so on.  
[02:02:30] But it's obvious how this should look in the future.  
[02:02:35] To the extent you're willing to say, what is the thing you hope  
[02:02:37] will be released this year or next year? I'm building the first course. I want to  
[02:02:43] have a really, really good course, the obvious state-of-the-art destination  
[02:02:48] you go to to learn, AI in this case. That's just what I'm familiar with, so it's  
[02:02:51] a really good first product to get to be really good at it. So that's what I'm building. Nanochat,  
[02:02:56] which you briefly mentioned, is a capstone project of LLM101N, which is a class that I'm building.  
[02:03:02] That's a really big piece of it. But now I have to build out a lot of  
[02:03:04] the intermediates, and then I have to hire a small team of TAs and so on and build the entire course.  
[02:03:11] One more thing that I would say is that many times, when people think about education,  
[02:03:15] they think more about what I would say is a softer component of diffusing knowledge.  
[02:03:21] I have something very hard and technical in mind. In my mind, education is the very difficult  
[02:03:26] technical process of building ramps to knowledge. In my mind, nanochat is a ramp to  
[02:03:33] knowledge because it's very simple. It's the super simplified full-stack thing.  
[02:03:38] If you give this artifact to someone and they look through it, they're learning a ton of stuff.  
[02:03:43] It's giving you a lot of what I call eurekas per second, which is understanding per second.  
[02:03:48] That's what I want, lots of eurekas per second. So to me, this is a technical problem of  
[02:03:52] how do we build these ramps to knowledge. So I almost think of Eureka as maybe not that  
[02:03:58] different from some of the frontier labs or some of the work that's going on there.  
[02:04:03] I want to figure out how to build these ramps very efficiently so that people are  
[02:04:07] never stuck and everything is always not too hard or not too trivial, and  
[02:04:14] you have just the right material to progress. You're imagining in the short term that instead  
[02:04:18] of a tutor being able to probe your understanding, if you have enough self-awareness to be able to  
[02:04:24] probe yourself, you're never going to be stuck. You can find the right answer between talking  
[02:04:29] to the TA or talking to an LLM and looking at the reference implementation.  
[02:04:33] It sounds like automation or AI is not a significant part.  
[02:04:38] So far, the big alpha here is your ability to explain AI codified  
[02:04:46] in the source material of the class. That's fundamentally what the course is.  
[02:04:51] You always have to be calibrated to what capability exists in the industry.  
[02:04:55] A lot of people are going to pursue just asking ChatGPT, etc.  
[02:04:59] But I think right now, for example, if you go to ChatGPT and you say, teach me AI, there's no way.  
[02:05:03] It's going to give you some slop. AI is never going to write nanochat right now.  
[02:05:09] But nanochat is a really useful intermediate point.  
[02:05:13] I'm collaborating with AI to create all this material,  
[02:05:15] so AI is still fundamentally very helpful. Earlier on, I built CS231n at Stanford,  
[02:05:21] which I think was the first deep learning class at Stanford, which became very popular.  
[02:05:27] The difference in building out 231n then and LLM101N now is quite stark.  
[02:05:33] I feel really empowered by the LLMs as they exist right now, but I'm very much in the loop.  
[02:05:37] They're helping me build the materials, I go much faster.  
[02:05:40] They're doing a lot of the boring stuff, etc. I feel like I'm developing the course much faster,  
[02:05:45] and it's LLM-infused, but it's not yet at a place where it can creatively create the content.  
[02:05:50] I'm still there to do that. The trickiness is always  
[02:05:53] calibrating yourself to what exists. When you imagine what is available  
[02:05:57] through Eureka in a couple of years, it seems like the big bottleneck is going to be  
[02:06:02] finding Karpathys in field after field who can convert their understanding into these ramps.  
[02:06:09] It would change over time. Right now, it would be hiring faculty to help work  
[02:06:14] hand-in-hand with AI and a team of people probably to build state-of-the-art courses.  
[02:06:21] Over time maybe some of the TAs can become AIs. You just take all the course materials and then  
[02:06:28] I think you could serve a very good automated TA for the student when they have more basic  
[02:06:33] questions or something like that. But I think you'll need faculty  
[02:06:36] for the overall architecture of a course and making sure that it fits.  
[02:06:40] So I see a progression of how this will evolve. Maybe at some future point I'm not even that  
[02:06:45] useful and AI is doing most of the design much better than I could.  
[02:06:47] But I still think that's going to take some time to play out.  
[02:06:50] Are you imagining that people who have expertise in other fields are then contributing courses,  
[02:06:56] or do you feel like it's quite essential to the vision that you,  
[02:07:01] given your understanding of how you want to teach, are the one designing the content?  
[02:07:07] Sal Khan is narrating all the videos on Khan Academy.  
[02:07:09] Are you imagining something like that? No, I will hire faculty because there  
[02:07:12] are domains in which I'm not an expert. That's the only way to offer the state-of-the-art  
[02:07:18] experience for the student ultimately. I do expect that I would hire faculty, but  
[02:07:24] I will probably stick around in AI for some time. I do have something more conventional in mind for  
[02:07:29] the current capability than what people would probably anticipate.  
[02:07:33] When I'm building Starfleet Academy, I do probably imagine a physical institution, and maybe a tier  
[02:07:38] below that a digital offering that is not the state-of-the-art experience you would get when  
[02:07:44] someone comes in physically full-time and we work through material from start to end and  
[02:07:48] make sure you understand it. That's the physical offering. The digital offering is a bunch of stuff  
[02:07:53] on the internet and maybe some LLM assistant. It's a bit more gimmicky in a tier below, but  
[02:07:57] at least it's accessible to 8 billion people. I think you're basically inventing college  
[02:08:04] from first principles for the tools that are available today and just selecting  
[02:08:11] for people who have the motivation and the interest of really engaging with material.  
[02:08:18] There's going to have to be a lot of not just education but also re-education.  
[02:08:21] I would love to help out there because the jobs will probably change quite a bit.  
[02:08:27] For example, today a lot of people are trying to upskill in AI specifically.  
[02:08:29] I think it's a really good course to teach in this respect.  
[02:08:34] Motivation-wise, before AGI motivation is very simple to solve because people want to make money.  
[02:08:41] This is how you make money in the industry today. Post-AGI is a lot more interesting possibly  
[02:08:46] because if everything is automated and there's nothing to do for anyone,  
[02:08:49] why would anyone go to a school? I often say that pre-AGI education  
[02:08:57] is useful. Post-AGI education is fun. In a similar way, people go to the gym today.  
[02:09:06] We don't need their physical strength to manipulate heavy objects because we  
[02:09:10] have machines that do that. They still go to the gym.  
[02:09:12] Why do they go to the gym? Because it's fun, it's healthy,  
[02:09:16] and you look hot when you have a six-pack. It's attractive for people to do that  
[02:09:24] in a very deep, psychological, evolutionary sense for humanity.  
[02:09:30] Education will play out in the same way. You'll go to school like you go to the gym.  
[02:09:36] Right now, not that many people learn because learning is hard. You bounce  
[02:09:40] from material. Some people overcome that barrier, but for most people, it's hard.  
[02:09:46] It's a technical problem to solve. It's a technical problem to do what my tutor  
[02:09:50] did for me when I was learning Korean. It's tractable and buildable,  
[02:09:53] and someone should build it. It's going to make learning  
[02:09:55] anything trivial and desirable, and people will do it for fun because it's trivial.  
[02:10:00] If I had a tutor like that for any arbitrary piece of knowledge, it's going to be so much easier to  
[02:10:05] learn anything, and people will do it. They'll do it for the same  
[02:10:07] reasons they go to the gym. That sounds different from using…  
[02:10:14] So post-AGI, you're using this as entertainment or as self-betterment.  
[02:10:21] But it sounded like you had a vision also that this education is relevant to  
[02:10:25] keeping humanity in control of AI. That sounds different. Is it entertaining for some people,  
[02:10:30] but then empowerment for some others? How do you think about that?  
[02:10:32] I do think eventually it's a bit of a losing game, if that makes sense.  
[02:10:41] It is in the long term. In the long term, which  
[02:10:44] is longer than maybe most people in the industry think about, it's a losing game.  
[02:10:47] I do think people can go so far and we've barely scratched the surface of how much a person can go.  
[02:10:53] That's just because people are bouncing off of material that's too easy or too hard.  
[02:10:59] People will be able to go much further. Anyone will speak five languages because  
[02:11:03] why not? Because it's so trivial. Anyone will know all the basic curriculum of undergrad, et cetera.  
[02:11:09] Now that I'm understanding the vision, that's very interesting.  
[02:11:14] It has a perfect analog in gym culture. I don't think 100 years  
[02:11:18] ago anybody would be ripped. Nobody would have been able to just spontaneously  
[02:11:22] bench two plates or three plates or something. It's very common now because of this idea of  
[02:11:29] systematically training and lifting weights in the gym, or systematically training to be able  
[02:11:33] to run a marathon, which is a capability most humans would not spontaneously have.  
[02:11:38] You're imagining similar things for learning across many different domains,  
[02:11:43] much more intensely, deeply, faster. Exactly. I am betting a bit implicitly  
[02:11:48] on some of the timelessness of human nature. It will be desirable to do all these things,  
[02:11:58] and I think people will look up to it as they have for millennia.  
[02:12:03] This will continue to be true. There's some evidence of that historically.  
[02:12:07] If you look at, for example, aristocrats, or you look at ancient Greece or something like that,  
[02:12:11] whenever you had little pocket environments that were post-AGI in a certain sense, people  
[02:12:15] have spent a lot of their time flourishing in a certain way, either physically or cognitively.  
[02:12:22] I feel okay about the prospects of that. If this is false and I'm wrong and we end up in a  
[02:12:29] WALL-E or Idiocracy future, then I don't even care if there are Dyson spheres. This is a terrible  
[02:12:35] outcome. I really do care about humanity. Everyone has to just be  
[02:12:41] superhuman in a certain sense. It's still a world in which that is not enabling  
[02:12:46] us to… It's like the culture world, right? You're not fundamentally going to be able  
[02:12:51] to transform the trajectory of technology or influence  
[02:12:57] decisions by your own labor or cognition alone. Maybe you can influence decisions because the AI  
[02:13:03] is asking for your approval, but it's not because I've invented something or I've come up with a new  
[02:13:10] design that I'm really influencing the future. Maybe. I think there will be a transitional  
[02:13:15] period where we are going to be able to be in the loop and advance  
[02:13:19] things if we understand a lot of stuff. In the long-term, that probably goes away.  
[02:13:25] It might even become a sport. Right now you have powerlifters  
[02:13:28] who go extreme in this direction. What is powerlifting in a cognitive era?  
[02:13:33] Maybe it's people who are really trying to make Olympics out of knowing stuff.  
[02:13:39] If you have a perfect AI tutor, maybe you can get extremely far.  
[02:13:43] I feel that the geniuses of today are barely scratching the  
[02:13:48] surface of what a human mind can do, I think. I love this vision. I also feel like the person  
[02:13:55] you have the most product-market fit with is me because my job involves having to learn different  
[02:14:02] subjects every week, and I am very excited. I'm similar, for that matter. A lot of people,  
[02:14:10] for example, hate school and want to get out of it. I really liked school. I loved  
[02:14:15] learning things, et cetera. I wanted to stay in school.  
[02:14:16] I stayed all the way until Ph.D. and then they wouldn't let me stay longer,  
[02:14:19] so I went to the industry. Roughly speaking, I love learning,  
[02:14:25] even for the sake of learning, but I also love learning because it's a form of empowerment and  
[02:14:29] being useful and productive. You also made a point that  
[02:14:32] was subtle and I want to spell it out. With what’s happened so far with online  
[02:14:36] courses, why haven't they already enabled us to enable every single human to know everything?  
[02:14:44] They're just so motivation-laden because there are no obvious on-ramps and it's so easy to get stuck.  
[02:14:52] If you had this thing instead—like a really good human tutor—it would just be such an  
[02:15:00] unlock from a motivation perspective. I think so. It feels bad to bounce from  
[02:15:04] material. It feels bad. You get negative reward from sinking an amount of time in something and it  
[02:15:09] doesn't pan out, or being completely bored because what you're getting is too easy or too hard.  
[02:15:16] When you do it properly, learning feels good. It's a technical problem to get there.  
[02:15:21] For a while, it's going to be AI plus human collab, and at some point, maybe it's just AI.  
[02:15:27] Can I ask some questions about teaching well? If you had to give advice to another educator  
[02:15:32] in another field that you're curious about to make the kinds of YouTube tutorials you've made.  
[02:15:40] Maybe it might be especially interesting to talk about domains where you can't  
[02:15:43] test someone's technical understanding by having them code something up or something.  
[02:15:47] What advice would you give them? That's a pretty broad topic. There are 10–20 tips  
[02:15:54] and tricks that I semi-consciously do probably. But a lot of this comes  
[02:16:03] from my physics background. I really, really did enjoy my physics background.  
[02:16:06] I have a whole rant on how everyone should learn physics in early school  
[02:16:10] education because early school education is not about accumulating knowledge or memory  
[02:16:15] for tasks later in the industry. It's about booting up a brain.  
[02:16:18] Physics uniquely boots up the brain the best because some of the things that they  
[02:16:22] get you to do in your brain during physics is extremely valuable later.  
[02:16:26] The idea of building models and abstractions and understanding that there's a first-order  
[02:16:31] approximation that describes most of the system, but then there're second-order, third-order,  
[02:16:34] fourth-order terms that may or may not be present. The idea that you're observing a very noisy  
[02:16:39] system, but there are these fundamental frequencies that you can abstract away.  
[02:16:43] When a physicist walks into the class and they say, "Assume there's a spherical cow,"  
[02:16:48] everyone laughs at that, but this is brilliant. It's brilliant thinking that's very generalizable  
[02:16:53] across the industry because a cow can be approximated as a sphere in a bunch of ways.  
[02:16:58] There's a really good book, for example, Scale. It's from a physicist talking about biology.  
[02:17:04] Maybe this is also a book I would recommend reading.  
[02:17:06] You can get a lot of really interesting approximations and chart scaling laws of animals.  
[02:17:11] You can look at their heartbeats and things like that, and they line up with  
[02:17:15] the size of the animal and things like that. You can talk about an animal as a volume.  
[02:17:20] You can talk about the heat dissipation of that, because your heat dissipation grows as the surface  
[02:17:25] area, which is growing as a square. But your heat creation or generation  
[02:17:29] is growing as a cube. So I just feel like physicists  
[02:17:33] have all the right cognitive tools to approach problem solving in the world.  
[02:17:36] So because of that training, I always try to find the first-order  
[02:17:39] terms or the second-order terms of everything. When I'm observing a system or a thing, I have a  
[02:17:43] tangle of a web of ideas or knowledge in my mind. I'm trying to find, what is the thing that  
[02:17:48] matters? What is the first-order component? How can I simplify it? How can I have a  
[02:17:52] simplest thing that shows that thing, shows it in action, and then I can tack on the other terms?  
[02:17:58] Maybe an example from one of my repos that I think illustrates it well is called micrograd.  
[02:18:03] I don't know if you're familiar with this. So micrograd is 100 lines of code  
[02:18:06] that shows backpropagation. You can create neural networks  
[02:18:10] out of simple operations like plus and times, et cetera. Lego blocks of neural networks. You build  
[02:18:14] up a computational graph and you do a forward pass and a backward pass to get the gradients.  
[02:18:19] Now, this is at the heart of all neural network learning.  
[02:18:21] So micrograd is a 100 lines of pretty interpretable Python code,  
[02:18:25] and it can do forward and backward arbitrary neural networks, but not efficiently.  
[02:18:29] So micrograd, these 100 lines of Python, are everything you need to understand how  
[02:18:32] neural networks train. Everything else is just efficiency. Everything else is efficiency. There's  
[02:18:38] a huge amount of work to get efficiency. You need your tensors, you lay them out,  
[02:18:41] you stride them, you make sure your kernels, orchestrating  
[02:18:43] memory movement correctly, et cetera. It's all just efficiency, roughly speaking.  
[02:18:47] But the core intellectual piece of neural network training is micrograd. It's 100 lines.  
[02:18:50] You can easily understand it. It's a recursive application of chain rule to derive the gradient,  
[02:18:55] which allows you to optimize any arbitrary differentiable function.  
[02:18:58] So I love finding these small-order terms and serving them on a platter and discovering them.  
[02:19:06] I feel like education is the most intellectually interesting thing because you have a tangle  
[02:19:11] of understanding and you're trying to lay it out in a way that creates a ramp where  
[02:19:16] everything only depends on the thing before it. I find that this untangling of knowledge is just  
[02:19:21] so intellectually interesting as a cognitive task. I love doing it personally, but I just  
[02:19:27] have a fascination with trying to lay things out in a certain way. Maybe that helps me.  
[02:19:31] It also makes the learning experience so much more motivated.  
[02:19:35] Your tutorial on the transformer begins with bigrams, literally a lookup table from,  
[02:19:42] "Here's the word right now, or here's the previous word, here's the next word."  
[02:19:46] It's literally just a lookup table. That’s the essence of it, yeah.  
[02:19:48] It’s such a brilliant way, starting with a lookup table and then going to a transformer.  
[02:19:53] Each piece is motivated. Why would you add that? Why would you add the next thing?  
[02:19:57] You could memorize the attention formula, but having an understanding of why every  
[02:20:01] single piece is relevant, what problem it solves. You're presenting the pain before you present a  
[02:20:06] solution, and how clever is that? You want to take the student  
[02:20:08] through that progression. There are a lot of other small  
[02:20:11] things that make it nice and engaging and interesting. Always prompting the student.  
[02:20:17] There's a lot of small things like that are important and a lot of good educators will do  
[02:20:22] this. How would you solve this? I'm not going to present the solution before you guess. That would  
[02:20:27] be wasteful. That's a little bit of a…I don’t want to swear but it’s a dick move towards you  
[02:20:34] to present you with the solution before I give you a shot to try to come up with it yourself.  
[02:20:38] Because if you try to come up with it yourself, you get a better understanding of what the action  
[02:20:46] space is, what the objective is, and then why only this action fulfills that objective.  
[02:20:53] You have a chance to try it yourself, and you have an appreciation when I give you the solution.  
[02:20:58] It maximizes the amount of knowledge per new fact added.  
[02:21:02] Why do you think, by default, people who are genuine experts in their field are often bad  
[02:21:10] at explaining it to somebody ramping up? It's the curse of knowledge and expertise.  
[02:21:16] This is a real phenomenon, and I suffered from it myself as much as I try not to.  
[02:21:21] But you take certain things for granted, and you can't put yourself in the shoes  
[02:21:24] of new people who are just starting out. This is pervasive and happens to me as  
[02:21:28] well. One thing that's extremely helpful. As an example, someone was trying to show  
[02:21:32] me a paper in biology recently, and I just instantly had so many terrible questions.  
[02:21:38] What I did was I used ChatGPT to ask the questions with the paper in the context window.  
[02:21:43] It worked through some of the simple things. Then I shared the thread to the person who  
[02:21:49] wrote that paper or worked on that work. I felt like if they could see the dumb  
[02:21:54] questions I had, it might help them explain better in the future.  
[02:22:00] For my material, I would love it if people shared their dumb conversations with ChatGPT  
[02:22:04] about the stuff that I've created because it really helps me put myself  
[02:22:07] again in the shoes of someone who's starting out. Another trick that just works astoundingly well.  
[02:22:16] If somebody writes a paper or a blog post or an announcement, it is in 100% of cases that just  
[02:22:25] the narration or the transcription of how they would explain it to you over lunch is way more,  
[02:22:33] not only understandable, but actually also more accurate and scientific,  
[02:22:39] in the sense that people have a bias to explain things in the most abstract,  
[02:22:44] jargon-filled way possible and to clear their throat for four paragraphs before  
[02:22:48] they explain the central idea. But there's something about  
[02:22:51] communicating one-on-one with a person which compels you to just say the thing.  
[02:22:57] Just say the thing. I saw that tweet, I thought it was really good.  
[02:23:00] I shared it with a bunch of people. I noticed this many, many times.  
[02:23:06] The most prominent example is that I remember back in my PhD days doing research.  
[02:23:11] You read someone's paper, and you work to understand what it's doing.  
[02:23:15] Then you catch them, you're having beers at the conference later, and you ask them,  
[02:23:18] "So this paper, what were you doing? What is the paper about?" They will just tell you these three  
[02:23:23] sentences that perfectly captured the essence of that paper and totally give you the idea.  
[02:23:26] And you didn't have to read the paper. It's only when you're sitting at the table  
[02:23:30] with a beer or something, and they're like, "Oh yeah, the paper is just,  
[02:23:33] you take this idea, you take that idea and try this experiment and you try out this thing."  
[02:23:37] They have a way of just putting it conversationally just perfectly.  
[02:23:40] Why isn't that the abstract? Exactly. This is coming from the  
[02:23:47] perspective of how somebody who's trying to explain an idea should formulate it better.  
[02:23:51] What is your advice as a student to other students, if you don't have a Karpathy  
[02:23:57] who is doing the exposition of an idea? If you're reading a paper from somebody  
[02:24:00] or reading a book, what strategies do you employ to learn material you're  
[02:24:07] interested in in fields you're not an expert at? I don't know that I have unique tips and tricks,  
[02:24:13] to be honest. It's a painful process. One thing that has always helped me quite a bit is—I  
[02:24:26] had a small tweet about this—learning things on demand is pretty nice. Learning depth-wise.  
[02:24:31] I do feel you need a bit of alternation of learning depth-wise, on demand—you're trying  
[02:24:35] to achieve a certain project that you're going to get a reward from—and learning breadth-wise,  
[02:24:38] which is just, "Oh, let's do whatever 101, and here's all the things you might need."  
[02:24:42] Which is a lot of school—does breadth-wise learning, like, "Oh, trust me, you'll need  
[02:24:45] this later," that kind of stuff. Okay, I trust you. I'll learn it because I guess I need it.  
[02:24:50] But I love the kind of learning where you'll get a reward out of  
[02:24:53] doing something, and you're learning on demand. The other thing that I've found extremely helpful.  
[02:24:59] This is an aspect where education is a bit more selfless, but explaining things to people is a  
[02:25:04] beautiful way to learn something more deeply. This happens to me all the time.  
[02:25:09] It probably happens to other people too because I realize if I don't really understand something,  
[02:25:13] I can't explain it. I'm trying and I'm like,  
[02:25:17] "Oh, I don't understand this." It's so annoying to come to terms with that.  
[02:25:21] You can go back and make sure you understood it. It fills these gaps of your understanding.  
[02:25:25] It forces you to come to terms with them and to reconcile them.  
[02:25:28] I love to re-explain things and people should be doing that more as well.  
[02:25:33] That forces you to manipulate the knowledge and make sure that you know what you're  
[02:25:36] talking about when you're explaining it. That's an excellent note to close on. Andrej,  
[02:25:40] that was great. Thank you.  
