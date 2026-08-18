# Dario Amodei (Anthropic CEO) — The hidden pattern behind every AI breakthrough

[00:00:50] Today I have the pleasure of speaking with Dario Amodei, the CEO of Anthropic,  
[00:00:56] and I'm really excited about this one. Dario, thank you so much for coming  
[00:00:59] on the podcast. Thanks for having me.  
[00:01:00] First question. You have been one of the very few people who has seen scaling  
[00:01:05] coming for years. As somebody who's seen it coming, what is fundamentally the explanation  
[00:01:13] for why scaling works? Why is the universe organized such that if you throw big blobs  
[00:01:18] of compute at a wide enough distribution of data, the thing becomes intelligent?  
[00:01:21] I think the truth is that we still don't know. It's almost entirely an empirical fact. It's a  
[00:01:29] fact that you could sense from the data and from a bunch of different places but we still don't  
[00:01:35] have a satisfying explanation for it. If I were to try to make one and I'm just  
[00:01:39] kind of waving my hands when I say this, there's these ideas in physics around long tail or power  
[00:01:48] law of correlations or effects. When a bunch of stuff happens, when you have a bunch of features,  
[00:01:56] you get a lot of the data in the early fat part of the distribution before the tails.  
[00:02:03] For language, this would be things like — “Oh, I figured out there are parts of  
[00:02:06] speech and nouns follow verbs.” And then there are these more and more subtle correlations.  
[00:02:12] So it kind of makes sense why every log or order of magnitude that you add, you capture more of the  
[00:02:21] distribution. What's not clear at all is why does it scale so smoothly with parameters? Why does it  
[00:02:29] scale so smoothly with the amount of data? You can think up some explanations of why  
[00:02:35] it's linear. The parameters are like a bucket, and the data is like water,  
[00:02:40] and so size of the bucket is proportional to size of the water. But why does it lead to all this  
[00:02:46] very smooth scaling? We still don't know. There's all these explanations. Our chief scientist,  
[00:02:51] Jared Kaplan did some stuff on fractal manifold dimension that you can use to explain it.  
[00:02:58] So there's all kinds of ideas, but I feel like we just don't really know for sure.  
[00:03:02] And by the way, for the audience who is trying to follow along. By scaling,  
[00:03:06] we're referring to the fact that you can very predictably see how if you go from Claude-1  
[00:03:11] to Claude-2 that the loss in terms of whether it can predict the next token scales very smoothly.  
[00:03:17] Okay, so we don't know why it's happening, but can you at least predict empirically that here  
[00:03:22] is the loss at which this ability will emerge, here is the place where this  
[00:03:27] circuit will emerge? Is that at all predictable or are you just looking at the loss number?  
[00:03:30] That is much less predictable. What's predictable is this statistical average,  
[00:03:34] this loss, this entropy. And it's super predictable. It's sometimes predictable even  
[00:03:40] to several significant figures which you don't see outside of physics. You don't expect to see  
[00:03:44] it in this messy empirical field. But specific abilities are actually very hard to predict.  
[00:03:51] Back when I was working on GPT-2 and GPT-3, when does arithmetic come in place? When do models  
[00:03:56] learn to code? Sometimes it's very abrupt. It's like how you can predict statistical  
[00:04:03] averages of the weather, but the weather on one particular day is very hard to predict.  
[00:04:08] Dumb it down for me. I don't understand manifolds, but mechanistically,  
[00:04:11] it doesn't know addition yet and suddenly now it knows addition. What has happened?  
[00:04:16] This is another question that we don't know the answer to. We're trying to answer this with things  
[00:04:20] like mechanistic interpretability. You can think about these things like circuits snapping into  
[00:04:27] place. Although there is some evidence that when you look at the models being able to add things,  
[00:04:35] its chance of getting the right answer shoots up all of a sudden. But if you look at what's  
[00:04:40] the probability of the right answer? You'll see it climb from like one in a million to  
[00:04:44] one in 100,000 to one in a 1000 long before it actually gets the right answer. In many of these  
[00:04:52] cases there's some continuous process going on behind the scenes. I don't understand it at all.  
[00:04:57] Does that imply that the circuit or the process for doing addition was pre  
[00:05:01] existing and it just got increased in salience? I don't know if there's this circuit that's weak  
[00:05:07] and getting stronger. I don't know if it's something that works, but not very well.  
[00:05:13] I think we don't know and these are some of the questions we're trying  
[00:05:15] to answer with mechanistic interpretability. Are there abilities that won't emerge with scale?  
[00:05:19] I definitely think that things like alignment and values are not guaranteed to emerge with  
[00:05:25] scale. One way to think about it is you train the model and it's basically predicting the world,  
[00:05:35] it's understanding the world. Its job is facts not values. It's trying to predict what comes  
[00:05:40] next. But there's free variables here — What should you do? What should you think? What  
[00:05:46] should you value? There aren't bits for that. There's just — if I started with this I should  
[00:05:54] finish with this. If I started with this other thing I should finish with this other thing.  
[00:05:58] And so I think that's not going to emerge. If it turns out that scaling plateaus before  
[00:06:06] we reach human level intelligence, looking back on it, what would be your explanation?  
[00:06:10] What do you think is likely to be the case if that turns out to be the outcome?  
[00:06:14] I would distinguish some problem with the fundamental theory with some practical  
[00:06:18] issue. One practical issue we could have is we could run out of data. For various reasons,  
[00:06:23] I think that's not going to happen but if you look at it very naively we're not that far from  
[00:06:29] running out of data. So it's like we just don't have the data to continue the scaling curves.  
[00:06:35] Another way it could happen is we just use up all of the compute that was available and  
[00:06:40] that wasn't enough and then progress is slow after that. I wouldn't bet on either of those  
[00:06:44] things happening but they could. From a fundamental perspective,  
[00:06:49] I personally think it's very unlikely that the scaling laws will just stop.  
[00:06:54] If they do, another reason could just be that we don't have quite the right architecture. If  
[00:07:02] we tried to do it with an LSTM or an RNN the slope would be different. It still might be that we get  
[00:07:08] there but there are some things that are just very hard to represent when you don't have the ability  
[00:07:12] to attend far in the past that transformers have. If somehow we just hit a wall and it wasn’t about  
[00:07:21] the architecture I'd be very surprised by that. We're already at the point where to me the  
[00:07:28] things the models can't do don't seem to be different in kind from the things they can do.  
[00:07:35] You could have made a case a few years ago that they can't reason, they can't program.  
[00:07:42] You could have drawn boundaries and said maybe you'll hit a wall. I didn't think we would hit a  
[00:07:48] wall, a few other people didn't think we would hit a wall, but it was a more plausible case  
[00:07:52] then. It's a less plausible case now. It could happen. This stuff is crazy.  
[00:07:59] We could hit a wall tomorrow. If that happens my explanation would be there's something wrong with  
[00:08:11] the loss when you train on next word prediction. If you really want to learn to program at a  
[00:08:22] really high level, it means you care about some tokens much more than others and they're rare  
[00:08:28] enough that the loss function over focuses on the appearance, the things that are responsible for  
[00:08:36] the most bits of entropy, and instead they don't focus on this stuff that's really essential. So  
[00:08:42] you could have the signal drowned out in the noise. I don't think it's going to play out  
[00:08:46] that way for a number of reasons. But if you told me — Yes, you trained your 2024 model.  
[00:08:51] It was much bigger and it just wasn't any better, and you tried every architecture and didn't work,  
[00:08:56] that's the explanation I would reach for. Is there a candidate for another loss function?  
[00:09:01] If you had to abandon next token prediction. I think then you would have to go for some  
[00:09:05] kind of RL. There's many different kinds. There's RL from immune feedback,  
[00:09:09] there's RL against an objective, there's things like Constitutional AI. There's things like  
[00:09:14] amplification and debate. These are kind of both alignment methods and ways of training models.  
[00:09:19] You would have to try a bunch of things, but the focus would have to be on what do we actually care  
[00:09:24] about the model doing? In a sense, we're a little bit lucky that predict the next word gets us all  
[00:09:30] these other things we need. There's no guarantee. From your worldview it seems there's a multitude  
[00:09:35] of different loss functions that it's just a matter of what can allow you to just throw a  
[00:09:39] whole bunch of data at it. Next token prediction itself is not significant.  
[00:09:44] The thing with RL is you get slowed down a bit because you have to design how the loss function  
[00:09:48] works by some method. The nice thing with the next token prediction is it's there for you.  
[00:09:56] It's the easiest thing in the world. So I think it would slow you down if you  
[00:10:00] couldn't scale in just that very simplest way. You mentioned that data is likely not to be the  
[00:10:05] constraint. Why do you think that is the case? There's various possibilities here and for a  
[00:10:10] number of reasons I shouldn't go into the details, but there's many sources of data in the world  
[00:10:14] and there's many ways that you can also generate data. My guess is that this will not be a blocker.  
[00:10:21] Maybe it would be better if it was, but it won't be.  
[00:10:24] Are you talking about multimodal? There’s just many different ways to do it.  
[00:10:28] How did you form your views on scaling? How far back can we go? And then you would be  
[00:10:32] basically saying something similar to this. This view that I have formed gradually from  
[00:10:38] 2014 to 2017. My first experience with it was my first experience with AI.  
[00:10:47] I saw some of the early stuff around AlexNet in 2012. I always had wanted to study intelligence  
[00:10:52] but before I was just like, this doesn’t seem like it’s actually working. All the way back  
[00:10:59] to 2005. I'd read Ray Kurzweil’s work. I'd read even some of Eliezer’s work on the early Internet  
[00:11:07] back then. And I thought this stuff kind of looks far away. I look at the AI stuff of  
[00:11:11] today and it’s not anywhere close. But with AlexNet I was like, oh,  
[00:11:16] this stuff is actually starting to work. So I joined Andrew Ng’s group  
[00:11:21] at Baidu. I had been in a different field and this was my first experience with AI and it was  
[00:11:34] a bit different from a lot of the academic style research that was going on elsewhere in the world.  
[00:11:42] I kind of got lucky in that the task that was given to me and the other  
[00:11:46] folks there. It was just to make the best speech recognition system that you can.  
[00:11:51] There was a lot of data available, there were a lot of GPUs available. It posed the problem in  
[00:11:58] a way that was amenable to discovering that kind of scaling was a solution. That's very different  
[00:12:03] from being a postdoc whose job is to come up with an idea that seems clever and new and makes your  
[00:12:13] mark as someone who's invented something. I just tried the simplest experiments. I  
[00:12:20] was just fiddling with some dials. I was like, try adding more layers to the RNN,  
[00:12:30] try training it for longer, what happens? How long does it take to overfit? What if  
[00:12:34] I add new data and repeat it less times? And I just saw these very consistent patterns.  
[00:12:39] I didn't really know that this was unusual or that others weren't thinking in this way. This was  
[00:12:47] almost like beginner's luck. It was my first experience with it and I didn't really think  
[00:12:51] about it beyond speech recognition. I was just like, oh, I don't know anything about this field.  
[00:12:58] There are zillions of things people do with machine learning. But I'm like, weird, this  
[00:13:02] seems to be true in the speech recognition field. It was just before OpenAI started that I met Ilya,  
[00:13:12] who you interviewed. One of the first things he said to me was — “Look. The  
[00:13:15] models, they just want to learn. You have to understand this. The models, they just want  
[00:13:18] to learn.” And it was a bit like a Zen Koan. I listened to this and I became enlightened.  
[00:13:27] And over the years, I would be the one who would formalize a lot of these things and kind of put  
[00:13:38] them together, but what that told me was that the phenomenon that I'd seen wasn't just some random  
[00:13:45] thing. It was broad. It was more general. The models just want to learn. You get the  
[00:13:51] obstacles out of their way. You give them good data, you give them enough space to operate in,  
[00:13:58] you don't do something stupid like condition them badly numerically,  
[00:14:03] and they want to learn. They'll do it. What I find really interesting about  
[00:14:08] what you said is there were many people who were aware that these things are really good at speech  
[00:14:16] recognition or at playing these constrained games. Very few extrapolated from there like you and Ilya  
[00:14:25] did to something that is generally intelligent. What was different about the way you were thinking  
[00:14:29] about it versus how others were thinking about it? What made you think it's getting better at  
[00:14:33] speech in this consistent way, it will get better at everything in this consistent way.  
[00:14:37] I genuinely don't know. At first when I saw it for speech, I assumed this was just true for speech or  
[00:14:42] for this narrow class of models. I think it was just that over the period between 2014 and 2017,  
[00:14:49] I tried it for a lot of things and saw the same thing over and over again. I watched the same  
[00:14:54] being true with Dota. I watched the same being true with robotics. Many people thought that  
[00:15:00] as a counterexample, but I just thought, well, it's hard to get data for robotics,  
[00:15:04] but if we look within the data that we have, we see the same patterns.  
[00:15:10] I think people were very focused on solving the problem in front of  
[00:15:14] them. It's very hard to explain why one person thinks one way and another person  
[00:15:17] thinks a different way. People just see it through a different lens. They are looking  
[00:15:24] vertically instead of horizontally. They're not thinking about the scaling,  
[00:15:27] they're thinking about how do I solve my problem? And for robotics, there's not enough data.  
[00:15:35] That can easily abstract to — scaling doesn't work because we don't have the data.  
[00:15:41] For some reason, and it may just have been random, I was obsessed with that particular direction.  
[00:15:47] When did it become obvious to you that language is the means to just feed a bunch of data into  
[00:15:53] these things? Or was it just you ran out of other things. Like robotics, there's not enough data.  
[00:15:57] This other thing, there's not enough data. I think this whole idea of the next word  
[00:16:02] prediction, that you could do self supervised learning, together with the idea that there's so  
[00:16:10] much richness and structure there for predicting the next word. It might say two plus two equals  
[00:16:13] and you have to know the answer is four. It might be telling the story about a character.  
[00:16:18] Basically, it's posing to the model the equivalent of these developmental tests  
[00:16:23] that get posed to children. Mary walks into the room and puts an item in there and then  
[00:16:28] Chuck walks into the room and removes the item and Mary doesn't see it. What does Mary think?  
[00:16:35] To get this right in the service of predicting the next word the models are going to have to  
[00:16:40] solve all these theory of mind problems, solve all these math problems. And so my thinking was just,  
[00:16:46] well, you scale it up as much as you can. There's kind of no limit to it.  
[00:16:51] And I think I kind of abstractly had that view but the thing that really  
[00:16:57] solidified and convinced me was the work that Alec Radford did on GPT-1. Which was that not  
[00:17:03] only could you get this language model that could predict things very well but you could also fine  
[00:17:08] tune it. In those days, you needed to fine tune it to do all these other tasks.  
[00:17:12] So I was like, wow, this isn't just some narrow thing where you get the language  
[00:17:16] model right. It's sort of halfway to everywhere. You get the language model right and then with a  
[00:17:23] little move in this direction, it can solve this logical dereference test or whatever. And with  
[00:17:30] this other thing, it can solve translation or something. And then you're like, wow,  
[00:17:35] I think there's really something to do. And of course, we can really scale it.  
[00:17:39] One thing that's confusing, or that would have been hard to see — If you told me in 2018 we'll  
[00:17:45] have models in 2023, like Claude 2 that can write theorems in the style of Shakespeare,  
[00:17:50] whatever theory you want, they can ace standardized test with open ended questions,  
[00:17:57] just all kinds of really impressive things, I would have said — Oh, you have AGI. You clearly  
[00:18:04] have something that is human level intelligence. While these things are impressive, it clearly  
[00:18:08] seems we're not at human level, at least in the current generation and potentially  
[00:18:12] for generations to come. What explains this discrepancy between super impressive  
[00:18:17] performance in these benchmarks and the things you could describe versus general intelligence?  
[00:18:23] That was one area where actually I was not prescient and I was surprised as well.  
[00:18:27] When I first looked at GPT-3 and the kind of things that we built in the early days  
[00:18:33] at Anthropic, my general sense was that it seems like they've really grasped the essence  
[00:18:41] of language. I'm not sure how much we need to scale them up. Maybe what's more needed  
[00:18:47] from here is like RL and all the other stuff. In 2020 I thought we can scale this a bunch  
[00:18:56] more but I wonder if it's more efficient to scale it more or to start adding on these  
[00:19:00] other objectives like RL. I thought maybe if you do as much RL as you've done pre training for a  
[00:19:08] 2020 style model, that's the way to go. Scaling it up will keep working. But is  
[00:19:15] that really the best path? And I don't know, it just keeps going. I thought  
[00:19:21] it had understood a lot of the essence of language but then there's further to go.  
[00:19:30] Stepping back from it. One of the reasons why I'm sort of very empiricist about AI,  
[00:19:37] about safety, about organizations, is that you often get surprised. I feel like  
[00:19:44] I've been right about some things but still with these theoretical pictures ahead, been wrong about  
[00:19:50] most things. Being right about 10% of the stuff sets you head and shoulders above many people.  
[00:19:58] If you look back to these diagrams that are like, here's the village idiot, here's Einstein.  
[00:20:07] Here's the scale of intelligence. And the village idiot and Einstein are very close to each other.  
[00:20:13] Maybe that's still true in some abstract sense or something but it's not really what we're seeing,  
[00:20:18] is it? We're seeing that it seems like the human range is pretty broad and we  
[00:20:25] don't hit the human range in the same place or at the same time for different tasks.  
[00:20:32] Like, write a sonnet in the style of Cormac McCarthy. I'm not very creative, so I couldn't  
[00:20:39] do that but that's a pretty high level human skill. And even the model is starting to get  
[00:20:45] good at stuff like constrained writing like, write a page about X without using the letter E.  
[00:20:54] I think the models might be superhuman or close to superhuman at that. But when it comes to  
[00:21:03] proving relatively simple mathematical theorems, they're just starting to do the beginning of it.  
[00:21:09] They make really dumb mistakes sometimes and they really lack any kind of broad correcting  
[00:21:18] your errors or doing some extended task. So it turns out that intelligence isn't a  
[00:21:25] spectrum. There are a bunch of different areas of domain expertise. There are a  
[00:21:30] bunch of different kinds of skills. Memory is different. It's all formed in the blob,  
[00:21:37] it's not complicated. But to the extent it even is on the spectrum, the spectrum is also wide.  
[00:21:42] If you asked me ten years ago, that's not what I would have expected at all, but I think that's  
[00:21:47] very much the way it's turned out. Oh, man. I have so many questions  
[00:21:49] just as a follow up on that. Do you expect that given the  
[00:21:54] distribution of training that these models get from massive amounts of internet data versus what  
[00:22:00] humans got from evolution, that the repertoire of skills that elicits will be just barely  
[00:22:06] overlapping? Will it be like concentric circles? How do you think about that? Do those matter?  
[00:22:12] Clearly there's certainly a large amount of overlap because a lot of the things these  
[00:22:17] models do have business applications and many of their business applications are doing things  
[00:22:21] that are helping humans to be more effective at things. So the overlap is quite large.  
[00:22:29] If you think of all the activity that humans put on the internet in text, that covers a lot of it,  
[00:22:33] but it probably doesn't cover some things. Like the models learn a physical model of the  
[00:22:38] world to some extent, but they certainly don't learn how to actually move around in the world.  
[00:22:42] Again, maybe that's easy to fine tune. So there are some things that the models  
[00:22:49] don't learn that humans do. And then the models also learn things that humans don’t, for example,  
[00:22:54] to speak fluent Base 64. I don't know about you, but I never learned that.  
[00:22:59] How likely do you think it is that these models will be superhuman for many years at economically  
[00:23:06] valuable tasks while they are still below humans in many other relevant tasks that prevents  
[00:23:12] an intelligence explosion or something? This kind of stuff is really hard to know  
[00:23:17] so I'll give that caveat. You can kind of predict the basic scaling laws and then this more granular  
[00:23:24] stuff, which we really want to know to know how this all is going to go, is much harder to know.  
[00:23:30] My guess would be the scaling laws are going to continue. Again, subject to — do  
[00:23:36] people slow down for safety or for regulatory reasons? But let's just put all that aside and  
[00:23:43] say we have the economic capability to keep scaling. If we did that, what would happen?  
[00:23:49] My view is we're going to keep getting better across the board and I don't see any area where  
[00:23:54] the models are super, super weak or not starting to make progress. That used to be true of math  
[00:23:59] and programming, but over the last six months the 2023 generation of models, compared to the  
[00:24:06] 2022 generation, has started to learn that. There may be more subtle things we don't know. And so I  
[00:24:12] kind of suspect, even if it isn't quite even, that the rising tide will lift all the boats.  
[00:24:18] Does that include the thing you were mentioning earlier where if there's an extended task,  
[00:24:22] it loses its train of thought or its ability to just execute a series of steps?  
[00:24:28] That's going to depend on things like RL training to have the model do longer  
[00:24:34] horizon tasks. I don't expect that to require a substantial amount of additional compute.  
[00:24:41] I think that was probably an artifact of thinking about RL in the wrong way and underestimating  
[00:24:49] how much the model had learned on its own. In terms of are we going to be superhuman  
[00:24:54] in some areas and not others? I think it's complicated. I could imagine that we won't  
[00:25:00] be superhuman in some areas because they involve embodiment in the physical world. And then what  
[00:25:06] happens? Do the AIs help us train faster AIs? And those faster AIs wrap around and solve  
[00:25:12] that? Do you not need the physical world? It depends what you mean. Are we worried about an  
[00:25:16] alignment disaster? Are we worried about misuse, like making weapons of mass destruction? Are we  
[00:25:22] worried about AI taking over research from humans? Are we worried about it reaching some threshold  
[00:25:30] of economic productivity where it can do what the average human does? I think these different  
[00:25:34] thresholds have different answers, although I suspect they will all come within a few years.  
[00:25:39] Let me ask about those thresholds. If Claude was an employee at Anthropic, what salary would it be  
[00:25:45] worth? Is it meaningfully speeding up AI progress? It feels to me like an intern in most areas,  
[00:25:51] but then some specific areas where it's better than that.  
[00:25:55] One thing that makes the comparison hard is that the form factor is not the same as a human.  
[00:26:03] If you were to behave like one of these chat bots, I guess we could have this conversation,  
[00:26:09] but they're more designed to answer single or a few questions. They don't have the concept  
[00:26:18] of having a long life of prior experience. We're talking here about things that I've experienced  
[00:26:24] in the past and chat bots don't have that. There's all kinds of stuff missing and so  
[00:26:30] it's hard to make a comparison. They feel like interns in some areas and then they have areas  
[00:26:38] where they spike and are really savants, where they may be better than anyone here.  
[00:26:43] But does the overall picture of something like an intelligence explosion make sense to you? My  
[00:26:48] former guest, Carl Shulman, has this very detailed model of an intelligence explosion. As somebody  
[00:26:52] who would actually see that happening, does that make sense to you? As they go from interns to  
[00:26:57] entry level software engineers. Those entry level software engineers increase your productivity…  
[00:27:01] I think the idea that as AI systems become more productive, first they speed up the  
[00:27:10] productivity of humans, then they equal the productivity of humans, and then in  
[00:27:17] some meaningful sense are the main contributor to scientific progress that happens at some point.  
[00:27:26] That basic logic seems likely to me although I have a suspicion that when we actually go into  
[00:27:32] the details, it's going to be weird and different than we expect. That in all the detailed models,  
[00:27:39] we're thinking about the wrong things or we're right about one thing,  
[00:27:42] and then are wrong about ten other things. I think we might end up in a weirder world than we expect.  
[00:27:50] When you add all this together, what does your estimate of when we get something  
[00:27:55] kind of human level look like? It depends on the thresholds.  
[00:28:02] In terms of someone looks at the model and even if you talk to it for an hour or so, it's  
[00:28:13] basically like a generally well educated human, that could be not very far away at all. I think  
[00:28:21] that could happen in two or three years. The main thing that would stop it would  
[00:28:29] be if we hit certain safety thresholds and stuff like that. So if a company or the industry decides  
[00:28:39] to slow down or we're able to get the government to institute restrictions that moderate the rate  
[00:28:47] of progress for safety reasons, that would be the main reason it wouldn't happen. But if you  
[00:28:51] just look at the logistical and economic ability to scale, we're not very far at all from that.  
[00:28:57] Now that may not be the threshold where the models are existentially dangerous. In fact,  
[00:29:03] I suspect it's not quite there yet. It may not be the threshold where the models can take over most  
[00:29:07] AI research. It may not be the threshold where the models seriously change how the economy works.  
[00:29:15] I think it gets a little murky after that and all of those thresholds may happen at various  
[00:29:20] times after that. But in terms of the base technical capability of — it kind of sounds  
[00:29:28] like a reasonably generally educated human across the board. I think that could be quite close.  
[00:29:33] Why would it be the case that it could pass a Turing Test for an educated person but not  
[00:29:39] be able to contribute or substitute for human involvement in the economy?  
[00:29:44] A couple of reasons. One is just that the threshold of skill isn't high enough,  
[00:29:48] comparative advantage. It doesn't matter that I have someone who's better than the average  
[00:29:56] human at every task. What I really need for AI research is to find something that is strong  
[00:30:06] enough to substantially accelerate the labor of the thousand experts who are best at it.  
[00:30:13] We might reach a point where the comparative advantage of these systems is not great.  
[00:30:20] Another thing that could be the case is that there are these mysterious frictions that don't show up  
[00:30:27] in naive economic models but you see it whenever you go to a customer or something. You're like —  
[00:30:34] “Hey, I have this cool chat bot.” In principle, it can do everything that your customer service  
[00:30:39] bot does or this part of your company does, but the actual friction of how do we slot it in? How  
[00:30:46] do we make it work? That includes both just the question of how it works in a human sense within  
[00:30:52] the company, how things happen in the economy and overcome frictions, and also just, what is the  
[00:31:00] workflow? How do you actually interact with it? It's very different to say, here's a chat bot that  
[00:31:07] looks like it's doing this task or helping the human to do some task as it is to say, okay, this  
[00:31:15] thing is deployed and 100,000 people are using it. Right now lots of folks are rushing to deploy  
[00:31:23] these systems but in many cases, they're not using them anywhere close to the most efficient way that  
[00:31:28] they could. Not because they're not smart, but because it takes time to work these things out.  
[00:31:33] And so I think when things are changing this fast, there are going to be all of these frictions.  
[00:31:39] These are messy realities that don't quite get captured in the model. I don't think it changes  
[00:31:44] the basic picture. I don't think it changes the idea that we're building up this snowball of,  
[00:31:49] the models help the models get better and can accelerate what the humans do. And  
[00:31:55] eventually it's mostly the models doing the work. You zoom out far enough that's happening. But I'm  
[00:32:01] skeptical of any kind of precise mathematical or exponential prediction of how it's going to be.  
[00:32:07] I think it's all going to be a mess. But what we know is it's on a metaphorical exponential,  
[00:32:14] and it's going to happen fast. How do those different exponentials  
[00:32:19] which we've been talking about net out? One was the scaling laws themselves are  
[00:32:24] power laws with decaying marginal loss parameter or something. The other exponential you talked  
[00:32:31] about is, these things can get involved in the process of AI research itself, speeding it up.  
[00:32:37] Those two are sort of opposing exponentials. Does it net out to be superlinear or sublinear? And  
[00:32:42] also you mentioned that the distribution of intelligence might just be broader.  
[00:32:48] After we get to this point in two to three years, what does that look like?  
[00:32:54] I think it's very unclear. We're already at the point where if you look at the loss,  
[00:32:58] the scaling laws are starting to bend. We've seen that in published model cards offered by multiple  
[00:33:04] companies. So that's not a secret at all. But as they start to bend, each little bit  
[00:33:10] of entropy of accurate prediction becomes more important. Maybe these last little  
[00:33:15] bits of entropy are the difference between a physics paper as Einstein would have written  
[00:33:20] it as opposed to some other physicist. It's hard to assess significance from  
[00:33:27] this. It certainly looks like in terms of practical performance, the metrics keep  
[00:33:32] going up relatively linearly, although they're always unpredictable. It's hard to see that.  
[00:33:38] And then the thing that I think is driving the most acceleration is just more and more money  
[00:33:43] is going into the field. People are seeing that there's just a huge amount of economic value and  
[00:33:51] so I expect the price, the amount of money spent on the largest models, to go up by like a factor  
[00:33:56] of 100 or something. And for that to then be concatenated with the chips are getting faster,  
[00:34:01] the algorithms are getting better because there's so many people working on this now.  
[00:34:07] Again, I'm not making a normative statement here. This is what should happen. I'm not  
[00:34:12] even saying this necessarily will happen because there's important safety and government questions  
[00:34:18] here which we're very actively working on. I'm just saying, left to itself,  
[00:34:22] this is what the economy is going to do. We'll get to those questions in a second. But  
[00:34:26] how do you think about the contribution of Anthropic to that increase in the scope of  
[00:34:32] this industry. There's an argument you can make that, with that investment, we can work on safety  
[00:34:38] stuff at Anthropic, another that says you're raising the salience of this field in general.  
[00:34:44] It's all costs and benefits. The costs are not zero. A mature way to think about these  
[00:34:49] things is not to deny that there are any costs, but to think about what the costs  
[00:34:53] are and what the benefits are. I think we've been relatively responsible in the sense  
[00:34:58] that we didn't cause the big acceleration that happened late last year and at the beginning of  
[00:35:02] this year. We weren't the ones who did that. And honestly, if you look at the reaction of  
[00:35:08] Google, that might be ten times more important than anything else. And then once it had happened,  
[00:35:13] once the ecosystem had changed, then we did a lot of things to stay on the frontier.  
[00:35:21] It's like any other question. You're trying to do the things that have the lowest costs  
[00:35:29] and the biggest benefits and that causes you to have different strategies at different times.  
[00:35:35] One question I had for you while we were talking about the intelligence stuff was,  
[00:35:38] as a scientist yourself, what do you make of the fact that these things have basically the  
[00:35:43] entire corpus of human knowledge memorized and they haven't been able to make a single  
[00:35:48] new connection that has led to a discovery? Whereas if even a moderately intelligent  
[00:35:53] person had this much stuff memorized, they would notice — Oh, this thing causes this  
[00:35:57] symptom. This other thing also causes this symptom. There's a medical cure right here.  
[00:36:01] Shouldn't we be expecting that kind of stuff? I'm not sure. These words. Discovery. Creativity.  
[00:36:10] One of the lessons I've learned is that in the big blob of compute, these ideas often end up being  
[00:36:17] fuzzy and elusive and hard to track down. But I think there is something here.  
[00:36:24] The models do display a kind of ordinary creativity. Things like,  
[00:36:29] write a sonnet in the style of Cormac McCarthy or Barbie. There is some creativity to that  
[00:36:36] and they do draw new connections of the kind that an ordinary person would draw.  
[00:36:41] I agree with you that there haven't been any “big” scientific discoveries. I think that's a mix of  
[00:36:50] just the model skill level is not high enough yet. I was on a podcast last week where the host said,  
[00:36:59] “I don't know, I play with these models. They're kind of mid. They get a B or a B minus.”  
[00:37:04] That is going to change with the scaling. I do think there's an interesting point about,  
[00:37:09] well, the models have an advantage, which is they know a lot more than us. Shouldn’t  
[00:37:15] they have an advantage already, even if their skill level isn't quite high?  
[00:37:19] Maybe that's kind of what you're getting at. I don't really have an answer to that. It seems  
[00:37:24] certainly like memorization and facts and drawing connections is an area where the models are ahead.  
[00:37:29] And I do think maybe you need those connections and you need a fairly high level of skill.  
[00:37:37] Particularly in the area of biology, for better and for worse, the complexity of biology is such  
[00:37:43] that the current models know a lot of things right now and that's what you need to make  
[00:37:49] discoveries and draw connections. It's not like physics where you need to think and come up with  
[00:37:54] a formula. In biology you need to know a lot of things. and so I do think the models know a lot  
[00:37:58] of things and they have a skill level that's not quite high enough to put them together.  
[00:38:02] I think they are just on the cusp of being able to put these things together.  
[00:38:06] On that point. Last week in your Senate testimony, you said that these models are two to three years  
[00:38:11] away from potentially enabling large scale bio terrorism attacks. Can you make that more concrete  
[00:38:17] without obviously giving the kind of information that would result in speeding that up? Is it one  
[00:38:21] shotting how to weaponize something or do you have to fine tune an open source  
[00:38:25] model? What would that actually look like? I think it'd be good to clarify this because  
[00:38:28] we did a blog post and the Senate testimony and various people didn't understand the  
[00:38:33] point or didn't understand what we'd done. Today you can ask the models all kinds of  
[00:38:45] things about biology and get them to say all kinds of scary things, but often those scary  
[00:38:50] things are things that you could Google, and I'm therefore not particularly worried about that.  
[00:38:56] I think it's actually an impediment to seeing the real danger, where someone just says — Oh,  
[00:39:00] I asked this model to tell me some things about smallpox, and it will.  
[00:39:05] That is actually not what I'm worried about. We spent about six months working with folks  
[00:39:13] who are the most expert in the world on how do biological attacks happen,  
[00:39:21] what would you need to conduct such an attack, and how do we defend against such an attack?  
[00:39:25] They worked very intensively on just the entire workflow of trying to do a bad thing. It's not one  
[00:39:32] shot, it's a long process. There are many steps to it. It's not just like I asked the model for  
[00:39:37] this one page of information. And again, without going into any detail, the thing I said in the  
[00:39:42] Senate testimony is, there are some steps where you can just get information on Google. There  
[00:39:48] are some steps that are what I'd call missing. They're scattered across a bunch of textbooks,  
[00:39:53] or they're not in any textbook. They're kind of implicit knowledge,  
[00:39:57] and they're not explicit knowledge. They're more like, I have to do this lab protocol,  
[00:40:04] and what if I get it wrong? Oh, if this happens, then my temperature was too low. If that happened,  
[00:40:10] I needed to add more of this particular reagent. What we found is that for the most part,  
[00:40:16] those key missing pieces, the models can't do them yet, but we found that sometimes they can,  
[00:40:25] and when they can, sometimes they still hallucinate, which is the thing that's  
[00:40:29] keeping us safe. But we saw enough signs of the models doing those key things well. And if we look  
[00:40:37] at state of the art models and go backwards to previous models, we look at the trend,  
[00:40:43] it shows every sign that two or three years from now, we're going to have a real problem.  
[00:40:49] Yeah, especially the thing you mentioned on the log scale. You go from one in 100 times,  
[00:40:53] it gets it right, to one in ten, to.. Exactly. I've seen many of these “groks”  
[00:40:57] in my life. I was there when I watched when GPT-3 learned to do arithmetic, when GPT-2 learned to  
[00:41:04] do regression a little bit above chance, when with Claude we got better on all these tests  
[00:41:11] of helpful, honest, harmless. I've seen a lot of groks. This is unfortunately not one that  
[00:41:16] I'm excited about, but I believe it's happening. Somebody might say, listen, you were a co-author  
[00:41:22] on this post that OpenAI released about GPT-2 where they said, we're not going to release the  
[00:41:27] weights or the details here because we're worried that this model will be used for  
[00:41:31] something bad. And looking back on it now, it's laughable to think that GPT-2 could have done  
[00:41:37] anything bad. Are we just way too worried? This is a concern that doesn't make sense?  
[00:41:42] It is interesting. It might be worth looking back at the actual text of that post.  
[00:41:48] I don't remember it exactly but it's still up on the Internet. It says something like,  
[00:41:54] we're choosing not to release the weights because of concerns about misuse. But it also said,  
[00:41:59] this is an experiment. We're not sure if this is necessary or the right thing to do at this time,  
[00:42:05] but we'd like to establish a norm of thinking carefully about these things. You could think  
[00:42:12] of it a little like the Asilomar conference in the 1970s where they were just figuring out  
[00:42:19] recombinant DNA. It was not necessarily the case that someone could do something really bad with  
[00:42:25] recombinant DNA. It's just the possibilities were starting to become clear. Those words,  
[00:42:29] at least, were the right attitude. Now I think there's a separate thing that  
[00:42:34] people don't just judge the post, they judge the organization. Is this an organization  
[00:42:39] that produces a lot of hype or that has credibility or something like that? And  
[00:42:44] so that had some effect on it. I guess you could also ask, is it inevitable that  
[00:42:53] you can't get across any message more complicated than this thing right here is dangerous.  
[00:42:58] You can argue about those but I think the basic thing that was in my head and  
[00:43:03] the head of others who were involved in that, and what is evident in the post is,  
[00:43:09] we actually don't know. We have pretty wide error bars on what's dangerous and what's not so we want  
[00:43:16] to establish a norm of being careful. By the way we have enormously more  
[00:43:20] evidence now. We've seen enormously more of these groks now and so we're well calibrated  
[00:43:25] but there's still uncertainty. In all these statements I've said, in two or three years we  
[00:43:29] might be there. There's a substantial risk of it and we don't want to take that risk. But I  
[00:43:34] wouldn't say it's 100%. It could be 50-50. Okay, let's talk about cybersecurity,  
[00:43:38] which in addition to bio risk is another thing Anthropic has been emphasizing. How have you  
[00:43:43] avoided the cloud microarchitecture from leaking? Because, as you know, your competitors have been  
[00:43:48] less successful at this kind of security. Can't comment on anyone else's security,  
[00:43:52] don't know what's going on in there. A thing that we have done is, there are these architectural  
[00:44:00] innovations that make training more efficient. We call them compute multipliers because  
[00:44:04] they're the equivalent of having more compute. I don't want to say too much about our compute  
[00:44:13] multipliers because it could allow an adversary to counteract our measures but we limit the  
[00:44:19] number of people who are aware of a given compute multiplier to those who need to know about it.  
[00:44:26] So there's a very small number of people who could leak all of these secrets. There's a larger number  
[00:44:31] of people who could leak one of them. But this is the standard compartmentalization strategy that's  
[00:44:36] used in the intelligence community or resistance cells or whatever. Over the last few months we've  
[00:44:47] implemented these measures. I don't want to jinx anything by saying, oh, this could never happen  
[00:44:51] to us but I think it would be harder for it to happen. I don't want to go into any more detail.  
[00:44:57] By the way I'd encourage all the other companies to do this as well. As much as  
[00:45:01] competitors architecture’s leaking is narrowly helpful to Anthropic,  
[00:45:06] it's not good for anyone in the long run. Security around this stuff is really important.  
[00:45:13] Could you, with your current security, prevent a dedicated state  
[00:45:16] level actor from getting the Claude 2 weights? It depends how dedicated. Our head of security,  
[00:45:23] who used to work on security for Chrome, which is a very widely used and attacked application,  
[00:45:30] he likes to think about it in terms of — how much would it cost to attack Anthropic successfully?  
[00:45:36] Again, I don't want to go into super detail of how much I think it will cost to attack  
[00:45:39] and it's just inviting people. One of our goals is that it costs more to attack Anthropic than  
[00:45:46] it costs to just train your own model. It doesn't guarantee things because, of course you need the  
[00:45:51] talent as well so you might still, but attacks have risks, the diplomatic costs, and they use  
[00:45:59] up the very sparse resources that nation state actors might have in order to do the attacks.  
[00:46:06] We're not there yet by the way. But I think we are at a very high standard of security compared  
[00:46:13] to the size of company that we are. If you look at security for most 150 person companies  
[00:46:19] there's just no comparison. But could we resist if it was a state actor's top priority to steal  
[00:46:27] our model weights? No. They would succeed. How long does that stay true? Because at some  
[00:46:33] point the value keeps increasing and increasing. And another part of this question is what kind  
[00:46:40] of a secret is how to train Claude 3 or Claude 2? For example, with nuclear weapons we had lots of  
[00:46:47] spies. You just take a blueprint of the implosion device across and that's what you need. Is it more  
[00:46:53] tacit here like the thing you were talking about with biology? You need to know how these reagents  
[00:46:56] work or is it just like you got the blueprint, you got the microarchitecture and the hyperparameters?  
[00:46:59] There are some things that are like a one line equation and there are other things that are  
[00:47:04] more complicated. I think compartmentalization is the best way to do it. Just limit the number of  
[00:47:10] people who know about something. If you're a 1000 person company and everyone knows every secret,  
[00:47:14] one, I guarantee you have a leaker and two, I guarantee you have a spy.  
[00:47:19] Okay, let's talk about alignment and let's talk about mechanistic interpretability,  
[00:47:22] which is the branch you guys specialize in. While you're answering this question, you might want to  
[00:47:28] explain what mechanistic interpretability is. The broader question is mechanistically,  
[00:47:34] what is alignment? Is it that you're locking in the model into a benevolent character? Are you  
[00:47:41] disabling deceptive circuits and procedures? What concretely is happening when you align a model?  
[00:47:47] As with most things, when we actually train a model to be aligned, we don't know what happens  
[00:47:52] inside the model. There are different ways of training it to be aligned but we don't really  
[00:47:57] know what happens. All the current methods that involve some kind of fine tuning of course have  
[00:48:05] the property that the underlying knowledge and abilities that we might be worried about don't  
[00:48:10] disappear. The model is just taught not to output them. I don't know if that's a fatal  
[00:48:16] flaw or if that's just the way things have to be. I don't know what's going on inside  
[00:48:21] mechanistically and I think that's the whole point of mechanistic interpretability. To  
[00:48:25] really understand what's going on inside the models at the level of individual circuits.  
[00:48:30] Eventually when it's solved, what does the solution look like? What is the case where  
[00:48:34] if you’re Claude 4, you do the mechanistic interpretability thing and you're like,  
[00:48:38] I'm satisfied, it's aligned. What is it that you've seen?  
[00:48:45] We don't know enough to know that yet. I can give you a sketch for what the process looks  
[00:48:50] like as opposed to what the final result looks like. Verifiability is a lot of the  
[00:48:56] challenge here. We have all these methods that purport to align AI systems and do  
[00:49:02] succeed at doing so for today's tasks. But then the question is always if you  
[00:49:07] had a more powerful model or if you had a model in a different situation,  
[00:49:10] would it be aligned? This problem would be much easier if you had an oracle that could just  
[00:49:17] scan a model and say okay, I know this model is aligned, I know what it'll do in every situation.  
[00:49:25] I think the closest thing we have to that is something like mechanistic interpretability.  
[00:49:30] It's not anywhere near up to the task yet. But I guess I would say I think of it as  
[00:49:35] almost like an extended training set and an extended test set. Everything we're doing,  
[00:49:40] all the alignment methods we're doing are the training set. You can run tests in them,  
[00:49:45] but will it really work out a distribution? Will it really work in another situation?  
[00:49:48] Mechanistic interpretability is the only thing that even in principle is the thing where it's  
[00:49:57] more like an X-ray of the model than modification of the model. It's more like an assessment than  
[00:50:02] an intervention. Somehow we need to get into a dynamic where we have an extended test set,  
[00:50:08] an extended training set, which is all these alignment methods,  
[00:50:12] and an extended test set which is kind of like you X-ray the model and say, okay,  
[00:50:18] what worked and what didn't? In a way that goes beyond just the empirical test that you've run,  
[00:50:25] where you're saying, what is the model going to do in these situations? What  
[00:50:31] is within its capabilities to do instead of, what did it do phenomenologically?  
[00:50:35] And of course we have to be careful about that. One of the things I think is very important is we  
[00:50:41] should never train for interpretability because that's taking away that advantage. You even have  
[00:50:46] the problem similar to validation versus test set, where if you look at the X-ray too many times,  
[00:50:52] you can interfere. We should worry about that, but that's a much weaker process,  
[00:50:59] it's not automated optimization. We should just make sure, as with validation and test sets, that  
[00:51:04] we don't look at the validation set too many times before running the test set. But again, that's  
[00:51:12] manual pressure rather than automated pressure. So some solution where we have some dynamic  
[00:51:19] between the training and test set where we're trying things out and we really figure out if they  
[00:51:25] work via a way of testing them, that the model isn't optimizing against, some orthogonal way.  
[00:51:33] I think we're never going to have a guarantee, but some process where we do those things together.  
[00:51:44] Some way to put extended training for alignment ability with extended testing for alignment  
[00:51:50] ability together in a way that actually works. And not in a stupid way, there's lots of stupid  
[00:51:54] ways to do this where you fool yourself. I still don't feel like I understand the  
[00:51:55] intuition for why you think this is likely to work or this is promising to pursue. Let  
[00:52:00] me ask the question in a more specific way, and excuse the tortured analogy.  
[00:52:06] If you're an economist and you want to understand the economy, you send a whole  
[00:52:11] bunch of microeconomists out there. One of them studies how the restaurant business works. One of  
[00:52:14] them studies how the tourism business works, one of them studies how the baking business works.  
[00:52:18] And at the end, they all come together and you still don't know whether there's going  
[00:52:22] to be a recession in five years or not. Why is this not like that? Where you  
[00:52:26] have an understanding of how induction heads work in a two layer transformer,  
[00:52:30] we understand modular arithmetic. How does this add up to — Does this model want to kill  
[00:52:35] us? What does this model fundamentally want? A few things on that. That's the right set of  
[00:52:40] questions to ask. I think what we're hoping for in the end is not that we'll understand every detail,  
[00:52:46] but again, I would give the X-ray or the MRI analogy. We can be in a position where we can  
[00:52:52] look at the broad features of the model and say, is this a model whose internal state and plans  
[00:52:59] are very different from what it externally represents itself to do? Is this a model  
[00:53:04] where we're uncomfortable that far too much of its computational power is devoted to doing what look  
[00:53:13] like fairly destructive and manipulative things? We don't know for sure whether that's possible,  
[00:53:18] but at least some positive signs that it might be possible. Again,  
[00:53:23] the model is not intentionally hiding from you, it might turn out that the training process hides it  
[00:53:29] from you. I can think of cases where if the model is really super intelligent, it thinks in a way  
[00:53:33] so that it affects its own cognition. We should think about that, we should consider everything.  
[00:53:40] I suspect that it may roughly work to think of the model as if it's trained in the normal way,  
[00:53:49] just getting to above human level. It may be a reasonable assumption, you should check, that  
[00:53:59] the internal structure of the model is not intentionally optimizing against us.  
[00:54:03] I'd give an analogy to humans. It's actually possible to look at an MRI of someone  
[00:54:13] and predict above random chance whether they're a psychopath. There was actually a story a few years  
[00:54:18] back about a neuroscientist who was studying this, and then he looked at his own scan and  
[00:54:22] discovered that he was a psychopath and then everyone in his life was like — No, this is  
[00:54:27] obvious. You're a complete asshole. You must be a psychopath. And he was totally unaware of this.  
[00:54:33] The basic idea that there can be these macro features, psychopath is probably  
[00:54:40] a good analogy for it, this is what we would be afraid of, a model that's charming on the surface,  
[00:54:46] very goal oriented, and very dark on the inside. On the surface,  
[00:54:51] their behavior might look like the behavior of someone else, but their goals are very different.  
[00:54:55] A question somebody might have is, you're trying to empirically estimate if these  
[00:55:04] activations are suspicious but is this something we can afford to be empirical about? Or do we need  
[00:55:13] a very good first principal theoretical reason to think — No, it's not just that these MRIs of  
[00:55:18] the model correlate with being bad. We need just some deep rooted math proof that this is aligned.  
[00:55:26] It depends what you mean by empirical. A better term would be phenomenological. I don't think  
[00:55:30] we should be purely phenomenological in like, here are some brain scans of really dangerous  
[00:55:36] models and here are some other brain scans. The whole idea of mechanistic interpretability is to  
[00:55:42] look at the underlying principles and circuits. But I guess the way I'd think about it is like,  
[00:55:46] on one hand, I've actually always been a fan of studying these circuits at the lowest level  
[00:55:52] of detail that we possibly can. And the reason for that is that's kind of how you build up knowledge.  
[00:55:57] Even if you're ultimately aiming for there's too many of these features, it's too complicated.  
[00:56:02] At the end of the day, we're trying to build something broad and we're trying to build some  
[00:56:07] broad understanding. I think the way you build that up is by trying to make a lot of these very  
[00:56:12] specific discoveries. You have to understand the building blocks and then you have to figure out  
[00:56:18] how to use that to draw these broad conclusions even if you're not going to figure out everything.  
[00:56:23] You should probably talk to Chris Olah, who would have much more detail. He controls the  
[00:56:32] interpretability agenda. He's the one who decides what to do on interpretability.  
[00:56:37] This is my high level thinking about it, which is not going to be as good as his.  
[00:56:40] Does the bull case on Anthropic rely on the fact that mechanistic interpretability is  
[00:56:45] helpful for capabilities? I don't think so at all.  
[00:56:51] I think in principle it's possible that mechanistic interpretability could be helpful  
[00:56:55] with capabilities. We might, for various reasons, not choose to talk about it if that were the case.  
[00:57:02] That wasn't something that I or any of us thought of at the time of Anthropic’s  
[00:57:07] founding. We thought of ourselves as people who are good at scaling models and good at doing  
[00:57:14] safety on top of those models. We think that we have a very high talent density of folks who are  
[00:57:20] good at that. My view has always been talent density beats talent mass. That's more of our  
[00:57:27] bullcase. Talent density beats talent mass. I don't think it depends on some particular  
[00:57:32] thing. Others are starting to do mechanistic interpretability now,  
[00:57:35] and I'm very glad that they are. A part of our theory of change is paradoxically  
[00:57:42] to make other organizations more like us. I'm sure talent density is important but  
[00:57:46] another thing Anthropic has emphasized is that you need to have frontier models  
[00:57:50] in order to do safety research. And of course, actually be a company as well.  
[00:57:53] Somebody might guess that the current frontier models, GPT-4, Claude 2 cost one hundred  
[00:57:58] million dollars or something like that… That general order of magnitude in  
[00:58:01] very broad terms is not wrong. But two to three years from now,  
[00:58:04] the kinds of things you're talking about, we're talking more and more orders of magnitude to  
[00:58:09] keep up with that. If it's the case that safety requires us to be on the frontier,  
[00:58:14] what is a case in which Anthropic is competing with these leviathans to stay on that same scale?  
[00:58:21] It's a situation with a lot of trade offs. It's not easy.  
[00:58:27] Maybe I'll just answer the questions one by one. To go back to why is safety so tied to scale?  
[00:58:35] Some people don't think it is. But if I just look at what have been the areas where safety  
[00:58:43] methods have been put into practice or worked for something, for anything,  
[00:58:47] even if we don't think they'll work in general. I go back to thinking of all the ideas,  
[00:58:53] something like debate and amplification. Back in 2018 when we wrote papers about those at OpenAI,  
[00:59:00] it was like, human feedback isn't quite going to work, but debate and amplification will take us  
[00:59:06] beyond that. But then if you actually look at the attempts to do debates, we're really limited by  
[00:59:13] the quality of the model. For two models to have a debate that is coherent enough that a human can  
[00:59:22] judge it so that the training process can actually work, you need models that are at or maybe even  
[00:59:27] beyond on some topics the current frontier. You can come up with the method, you can come  
[00:59:32] up with the idea without being on the frontier but for me, that's a very small fraction of what  
[00:59:39] needs to be done. It's very easy to come up with these methods. It's very easy to come up with,  
[00:59:43] oh, the problem is X, maybe a solution is Y. I really want to know whether things work in  
[00:59:50] practice, even for the systems we have today, and I want to know what kinds of  
[00:59:54] things go wrong with them. I just feel like you discover ten new ideas and ten new ways  
[00:59:59] that things are going to go wrong by trying these in practice. I think that empirical learning is  
[01:00:06] just not as widely understood as it should be. I would say the same thing about methods like  
[01:00:11] constitutional AI, and some people say, oh, it doesn't matter. We know this method doesn't work,  
[01:00:15] it won't work for pure alignment. I neither agree nor disagree with that. I think that's just kind  
[01:00:21] of overconfident. The way we discover new things and understand the structure of what's going to  
[01:00:25] work and what's not is by playing around with things. Not that we should just blindly say,  
[01:00:30] oh, this worked here, and so it'll work there. But you really start to understand the patterns,  
[01:00:36] like with the scaling laws. Even mechanistic interpretability,  
[01:00:39] which might be the one area I see where a lot of progress has been made without the frontier  
[01:00:45] models, we're seeing in the work that OpenAI put out a couple months ago, that using very  
[01:00:53] powerful models to help you auto interpret the weak models. Again, that's not everything you  
[01:00:59] can do in interpretability, but that's a big component of it and we found it useful too.  
[01:01:05] So you see this phenomenon over and over again where the scaling and the safety are these two  
[01:01:13] snakes that are coiled with each other, always even more than you think. Even with  
[01:01:18] interpretability, three years ago, I didn't think that this would be as true of interpretability,  
[01:01:23] but somehow it manages to be true. Why? Because intelligence is useful. It's useful for a number  
[01:01:28] of tasks. One of the tasks it's useful for is figuring out how to judge and evaluate  
[01:01:33] other intelligence and maybe someday even for doing the alignment research itself.  
[01:01:38] Given all that's true, what does that imply for Anthropic when in two to three years,  
[01:01:42] these leviathans are doing like $10 billion training runs?  
[01:01:45] Choice one is if we can't, or if it costs too much to stay on the frontier, then we shouldn't  
[01:01:53] do it and we won't work with the most advanced models, we'll see what we can get with models  
[01:01:59] that are not quite as advanced. You can get some non zero value there but I'm skeptical that the  
[01:02:06] value is all that high or the learning can be fast enough to really be in favor of the task.  
[01:02:11] The second option is you just find a way. You just accept the trade offs. And the trade offs are  
[01:02:19] more positive than they appear because of a phenomenon that I've called Race to the Top.  
[01:02:25] I could go into that later, but let me put that aside for now.  
[01:02:29] And the third phenomenon is that as things get to that scale, it may coincide with starting to get  
[01:02:39] into some non trivial probability of very serious danger. I think it's going to come first from  
[01:02:45] misuse, the biorisk stuff that I talked about. I don't think we have the level of autonomy yet to  
[01:02:52] worry about some of the alignment stuff happening in two years, but it might not be very far behind  
[01:03:00] that at all. That may lead to unilateral or multilateral or government enforced decisions not  
[01:03:11] to scale as fast as we could, which we support. That may end up being the right thing to do.  
[01:03:15] I hope things go in that direction, and then we don't have this hard trade off between we're not  
[01:03:22] in the frontier and can't quite do the research as well as we want or influence other orgs as well  
[01:03:27] as we want, or versus we're on the frontier and have to accept the trade-offs which are  
[01:03:34] net positive, but have a lot in both directions. On the misuse versus misalignment, those are both  
[01:03:40] problems as you mentioned but in the long scheme of things, say 30 years down the line, which do  
[01:03:48] you think will be considered a bigger problem? I think it's going to be much less than 30 years.  
[01:03:52] I'm worried about both. If you have a model that could in theory, take over the world on its own,  
[01:04:00] if you were able to control that model, then it follows pretty simply that if a model was  
[01:04:06] following the wishes of some small subset of people and not others, then those people  
[01:04:10] could use it to take over the world on their behalf. The very premise of misalignment means  
[01:04:16] that we should be worried about misuse as well, with similar levels of consequences.  
[01:04:21] But some people who might be more doomery than you would say — you're already working towards  
[01:04:28] the optimistic scenario there because you've at least figured out how to align the model with  
[01:04:33] the bad guys. Now you just need to make sure that it's aligned with the good guys instead.  
[01:04:36] Why do you think that you could get to the point where it's aligned with the  
[01:04:40] bad guys? You haven't already solved this. I guess if you had the view that alignment  
[01:04:44] is completely unsolvable, then you'd be like, well, we're dead anyway so I don't want to worry  
[01:04:49] about misuse. That's not my position at all. But also you should think in terms of what's  
[01:04:54] a plan that would actually succeed that would make things good. Any plan  
[01:04:58] that actually succeeds, regardless of how hard misalignment is to solve, is going to  
[01:05:05] need to solve misuse as well as misalignment. As the AI models get better faster and faster,  
[01:05:13] they're going to create a big problem around the balance of power between countries. They're going  
[01:05:18] to create a big problem around, is it possible for a single individual to do something bad  
[01:05:22] that it's hard for everyone else to stop? Any actual solution that leads to a good future  
[01:05:28] needs to solve those problems as well. If your perspective is, we're screwed because we can't  
[01:05:32] solve the first problem, so don't worry about problems two and three, that's not really a  
[01:05:37] statement. You should worry about problems two and three. They're in our path no matter what.  
[01:05:42] Yeah. In the scenario we succeed we have to solve all of them.  
[01:05:46] We should be planning for success not for failure. If misuse doesn't happen and the right people  
[01:05:50] have the superhuman models, what does that look like? Who are the right people? Who is actually  
[01:05:56] controlling the model five years from now? My view is that these things are powerful enough  
[01:06:03] that I think it's going to involve substantial involvement of some kind of government or assembly  
[01:06:13] of government bodies. There are very naive versions of this. I don't think we should just  
[01:06:21] hand the model over to the UN or whoever happens to be in office at a given time. I could see that  
[01:06:27] going poorly. But it's too powerful. There needs to be some kind of legitimate process  
[01:06:33] for managing this technology, which includes the role of the people building it, includes  
[01:06:38] the role of democratically elected authorities, includes the role of all the individuals who will  
[01:06:46] be affected by it. At the end of the day, there needs to be some politically legitimate process.  
[01:06:52] But what does that look like? If it's not the case that you just hand it to whoever the President is  
[01:06:56] at the time, what does the body look like? It's really hard to know these things ahead  
[01:07:02] of time. People love to propose these broad plans and say, oh, this is the way we should do it. The  
[01:07:10] honest fact is that we're figuring this out as we go along. I think we should try things  
[01:07:23] and experiment with them with less powerful versions of the technology. We need to figure  
[01:07:28] this out in time. But also it's not really the kind of thing you can know in advance.  
[01:07:31] The long term benefit trust that you have. How would that interface  
[01:07:36] with this body? Is that the body itself? I think that the long term benefit trust  
[01:07:45] is a much narrower thing. This is something that makes decisions for Anthropic. This is  
[01:07:51] basically a body. It was described in a recent Vox article. We'll be saying more about it later  
[01:07:57] this year. But it's basically a body that over time gains the ability to appoint the  
[01:08:04] majority of the board seats of Anthropic. It's a mixture of experts in AI alignment,  
[01:08:12] national security, and philanthropy in general. If Anthropic has AGI and if control of Anthropic  
[01:08:16] is handed to them, doesn't that imply that control of AGI itself is handed to them?  
[01:08:22] That doesn't imply that Anthropic or any other entity should be the entity that makes decisions  
[01:08:27] about AGI on behalf of humanity. I would think of those as different things. If Anthropic does  
[01:08:34] play a broad role, then you'd want to widen that body to a whole bunch of different people  
[01:08:38] from around the world. Or maybe you construe this as very narrow, and then there's some  
[01:08:44] broad committee somewhere that manages all the AGIs of all the companies on behalf of anyone.  
[01:08:50] I don't know. I think my view is you shouldn't be overly constructive and utopian. We're dealing  
[01:08:57] with a new problem here. We need to start thinking now about what are the governmental  
[01:09:04] bodies and structures that could deal with it. Okay, so let's forget about governance. Let's  
[01:09:08] just talk about what this going well looks like. Obviously, there are things we can all agree on:  
[01:09:13] cure all the diseases, solve all the fraud – things all humans would say, 'I'm down for that.'  
[01:09:18] But now it's 2030. You've solved all the real problems that everybody can agree on. What happens  
[01:09:24] next? What are we doing with a superhuman God? I actually want to disagree with the framing of  
[01:09:30] something like this. I get nervous when someone says, what are you going to do with a superhuman  
[01:09:35] AI? We've learned a lot of things over the last 150 years about markets and democracy, and each  
[01:09:42] person can define for themselves what the best way for them to have the human experience is, and  
[01:09:48] that societies work out norms and what they value just in this very complex and decentralized way.  
[01:09:56] If you have these safety problems that can be a reason why there needs to be a  
[01:10:05] certain amount of centralized control from the government until we've solved these problems.  
[01:10:07] But as a matter of — we've solved all the problems, now how do we make things good?  
[01:10:11] I think most people, most groups, most ideologies that started with,  
[01:10:17] let's sit down and think over what the definition of the good life is, have led to disaster.  
[01:10:24] But this vision you have of a sort of tolerant, liberal, democracy,  
[01:10:28] market oriented system with AGI. Each person has their own AGI? What does that mean?  
[01:10:34] I don't know. I don't know what it looks like. I guess what I'm saying is we need to solve  
[01:10:39] the important safety problems and the important externalities. Those could be just narrowly about  
[01:10:49] alignment, there could be a bunch of economic issues that are super complicated and that we  
[01:10:53] can't solve. Subject to that, we should think about what's worked in the past. And in general,  
[01:10:59] unitary visions for what it means to live a good life have not worked out well at all.  
[01:11:06] On the opposite end of things going well or good actors having control of AI.  
[01:11:10] We might want to touch on China as a potential actor in the space.  
[01:11:15] First of all, being at Baidu and seeing progress in AI happening generally,  
[01:11:21] why do you think the Chinese have underperformed? Baidu had a scaling laws group many years back.  
[01:11:28] Or is the premise wrong and I'm just not aware of the progress that's happening there?  
[01:11:31] The scaling laws group, that was an offshoot of the stuff we did with speech  
[01:11:35] so there were still some people there but that was a mostly Americanized lab. I was there for a year.  
[01:11:41] That was my first foray into deep learning. It was led by Andrew Ng. I never went to  
[01:11:46] China. It was like a US lab. That was somewhat disconnected, although it was an attempt by a  
[01:11:52] Chinese entity to kind of get into the game. Since then I think they've maybe been very  
[01:12:01] commercially focused and not as focused on these fundamental research side of things around scaling  
[01:12:07] laws. I do think because of all the excitement with the release of ChatGPT in November or so,  
[01:12:16] that's been a starting gun for them as well. And they're trying very aggressively to catch up now.  
[01:12:21] I think the US is substantially ahead but they're trying very hard to catch up now.  
[01:12:27] How do you think China thinks about AGI? Are they thinking about safety and misuse or not?  
[01:12:32] I don't really have a sense. One concern I would have are people saying things like,  
[01:12:38] China isn't going to develop an AI because they like stability or they're going to have all these  
[01:12:44] restrictions to make sure things are in line with what the CCP wants. That might be true  
[01:12:49] in the short term and for consumer products. My worry is that if the basic incentives are about  
[01:12:55] national security and power, that's going to become clear sooner or later. If they see this  
[01:13:04] as a source of national power, they're going to at least try to do what's most effective,  
[01:13:08] and that could lead them in the direction of AGI. Assume they just get your blueprints or your code  
[01:13:15] base or something, is it possible for them to spin up their own lab that is competitive at  
[01:13:19] the frontier with the leading American companies? I don't know about fast but I'm concerned about  
[01:13:24] this. This is one reason why we're focusing so hard on cybersecurity. We've worked with our  
[01:13:31] cloud providers. We had this blog post out about security where we said we have a two key system  
[01:13:38] for access to the model weights. We have other measures that we put in place or are thinking  
[01:13:43] of putting in place that we haven't announced. We don't want an adversary to know about them,  
[01:13:47] but we're happy to talk about them broadly. By the way all this stuff we're doing  
[01:13:50] is not sufficient yet for a super determined state level actor at all.  
[01:13:57] I think it will defend against most attacks and against a state level actor who's less determined.  
[01:14:07] But there's a lot more we need to do, and some of it may require new research on how to do security.  
[01:14:13] Let's talk about what it would take at that point. We're at Anthropic offices and it's  
[01:14:18] got good security. We had to get badges and everything to come in here. But what does the  
[01:14:23] eventual version of this building or bunker or whatever where the AGI is built look like? Is it  
[01:14:29] a building in the middle of San Francisco or are you out in the middle of Nevada or Arizona? What  
[01:14:33] is a point in which you're Los Alamos-ing it? At one point there was a running joke somewhere  
[01:14:39] that the way building AGI would look like is, there would be a data center next to a nuclear  
[01:14:45] power plant next to a bunker, and that we'd all kind of live in the bunker and everything would  
[01:14:50] be local so it wouldn't get on the Internet. If we take the rate at which all this is going  
[01:14:59] to happen seriously, which I can't be sure of, then it does make me think  
[01:15:06] that something like that might happen, but maybe not something quite as cartoonish.  
[01:15:11] What is the timescale on which you think alignment is solvable? If these models are getting to human  
[01:15:17] level in some things in two to three years, what is the point at which they're aligned?  
[01:15:21] This is a really difficult question because I actually think often people are thinking about  
[01:15:25] alignment in the wrong way. There's a general feeling that it's like models are misaligned  
[01:15:31] or there's like an alignment problem to solve. Like, someday we'll crack the Riemann hypothesis.  
[01:15:39] I don't quite think it's like that. Not in a way that's worse or better. It might be just  
[01:15:45] as bad or just as unpredictable. When I think of why am I scared,  
[01:15:51] there’s a few things I think of — One is, the thing that's really hard to argue with is: There  
[01:15:57] will be powerful models. They will be agentic. We're getting towards them. If such a model  
[01:16:02] wanted to wreak havoc and destroy humanity or whatever, we have basically no ability to stop it.  
[01:16:11] If that's not true, at some point we will reach the point where it's true as we scale the models.  
[01:16:18] So that definitely seems to be the case. A second thing that seems to be the case is  
[01:16:23] that we seem to be bad at controlling the models. Not in any particular way, but they’re just  
[01:16:29] statistical systems and you can ask them a million things and they can say a million things  
[01:16:32] and reply. And you might not have thought of a millionth and one thing that does something crazy.  
[01:16:38] Or when you train them, you train them in this very abstract way and you might not understand  
[01:16:42] all the consequences of what they do in response to that. The best example we've seen of that is  
[01:16:49] Bing and Sydney. I don't know how they trained that model. I don't know what they did to make it  
[01:16:54] do all this weird stuff like threaten people and have this weird obsessive personality. But what it  
[01:17:02] shows is that we can get something very different from and maybe opposite to what we intended.  
[01:17:08] I actually think fact number one and fact number two are enough to be really worried.  
[01:17:14] You don't need all this detailed stuff about convergent instrumental goals or analogies to  
[01:17:21] evolution. One and two for me are pretty motivated. Okay, this thing's going to be  
[01:17:25] powerful. It could destroy us. And all the ones we've built so far are at pretty decent risk of  
[01:17:33] doing some random shit we don't understand. If you say that we're going to get something  
[01:17:47] with bioweapons or something that could be dangerous in two to three years,  
[01:17:51] does the research agenda you have of mechanistic interpretability, constitutional AI and other  
[01:17:52] RLHF stuff meaningfully contribute to preventing that in two to three years?  
[01:18:00] People talk about doom by default or alignment by default. I think it might be kind of statistical.  
[01:18:09] With the current models, you might get Bing or Sydney or you might get Claude.  
[01:18:14] If we take our current understanding and move that to very powerful models, you might just  
[01:18:21] be in this world where you make something and depending on the details, maybe it's totally fine.  
[01:18:27] Not really alignment by default, but just depends on a lot of the details. If you're  
[01:18:33] very careful about all those details and you know what you're doing, you're getting  
[01:18:35] it right but we have a high susceptibility to, you mess something up in a way that you didn't  
[01:18:41] really understand was connected to something else. Actually, instead of making all the humans happy,  
[01:18:45] it wants to turn them into pumpkins, just some weird shit. Because the models are so powerful,  
[01:18:51] they're like these giants that are standing in a landscape and if they start to move their arms  
[01:18:57] around randomly, they could just break everything. I'm starting it with that kind of framing because  
[01:19:03] I don't think we're aligned by default, I don't think we're doomed by default  
[01:19:07] and have some problem we need to solve. It has some kind of different character.  
[01:19:11] Now what I do think is that hopefully within a timescale of two to three years we get better at  
[01:19:17] diagnosing when the models are good and when they're bad. We get better at increasing our  
[01:19:24] repertoire of methods to train the model that they're less likely to do bad things and more  
[01:19:29] likely to do good things in a way that isn't just relevant to the current models but scales. And we  
[01:19:34] can help develop that with interpretability as the test set. I don't think of it as,  
[01:19:39] oh, man, we tried RLHF, it didn't work. We tried Constitutional AI, it didn't work. We tried this  
[01:19:44] other thing, it didn't work. We tried mechanistic interpretability. Now we're going to try something  
[01:19:48] else. I think this frame of like, man, we haven't cracked the problem yet, we haven't  
[01:19:52] solved the Riemann hypothesis isn't quite right. Already with today's systems, we are not very  
[01:20:01] good at controlling them and the consequences of that could be very bad. We just need to get  
[01:20:08] more ways of increasing the likelihood that we can control our models and understand  
[01:20:15] what's going on in them. And we have some of them so far. They aren't that good yet.  
[01:20:21] But I don't think of this as binary. It works or it does not work. We're going to develop more. And  
[01:20:27] I do think that over the next two to three years we're going to start eating that probability mass  
[01:20:31] of ways things can go wrong. It's like in the core safety views paper, there's a probability  
[01:20:36] mass of how hard the problem is. I feel like that way of stating it  
[01:20:40] isn't really even quite right because I don't feel like it's the Riemann hypothesis to solve. It's  
[01:20:48] almost like right now if I try and juggle five balls or something, I can juggle three balls,  
[01:20:52] I actually can, but I can't juggle five balls at all. You have to practice a lot to do that.  
[01:20:57] If I were to do that, I would almost certainly drop them. And then just over time, you just get  
[01:21:03] better at the task of controlling the balls. On that post in particular, what is your  
[01:21:08] personal probability distribution? For the audience, the three possibilities are: One, it is  
[01:21:13] trivial to align these models with RLHF++. Two, it is a difficult problem, but one that a big company  
[01:21:20] could solve. Three, something that is basically impossible for human civilization currently to  
[01:21:25] solve. If I'm capturing those three, What is your probability distribution over those three?  
[01:21:30] I'm not super into questions like what's your probability distribution of X? I think all of  
[01:21:34] those have enough likelihood that they should be considered seriously. The question I'm much  
[01:21:40] more interested in is, what could we learn that shifts probability mass between them?  
[01:21:45] What is the answer to that? I think that one of the things  
[01:21:48] mechanistic interpretability is going to do more than necessarily solve problems is,  
[01:21:54] it's going to tell us what's going on when we try to align models. It's basically going to  
[01:22:00] teach us about this. One way I could imagine concluding that things are very difficult is  
[01:22:06] if mechanistic interpretability sort of shows us that problems tend to get moved around instead of  
[01:22:14] being stamped out or that, you get rid of one problem, you create another one. Or it might  
[01:22:20] inspire us or give us insight into why problems are persistent or hard to eradicate or crop up.  
[01:22:28] For me to really believe some of these stories about, oh, there's always this convergent goal  
[01:22:35] in this particular direction. I think the abstract story is not uncompelling, but I  
[01:22:40] don't find it really compelling either, nor do I find it necessary to motivate all the safety work.  
[01:22:45] But the kind of thing that would really be like, oh man, we can't solve this is like,  
[01:22:49] we see it happening inside the X-ray. I think right now there's way too many assumptions,  
[01:22:57] there's way too much overconfidence about how all this is going to go. I have a substantial  
[01:23:02] probability mass on — this all goes wrong, it's a complete disaster, but in a completely different  
[01:23:08] way than anyone had anticipated it would. It would be beside the point to ask how  
[01:23:11] it could go different than anyone anticipated. On this, in particular, what information would  
[01:23:16] be relevant? How much would the difficulty of aligning Claude 3 and the next generation of  
[01:23:22] models be? Is that a big piece of information? I think the people who are most worried are  
[01:23:28] predicting that all the subhuman AI models are going to be alignable, They're going to seem  
[01:23:35] aligned. They're going to deceive us in some way. It certainly gives us some information  
[01:23:39] but I am more interested in what mechanistic interpretability can tell us because, again,  
[01:23:49] you see this X ray, it would be too strong to say it doesn't lie, but at least in the current  
[01:23:55] systems, it doesn't feel like it's optimizing against us. There are exotic ways that it could.  
[01:24:01] I don't think anything is a safe bet here, but it's the closest we're going to get to something  
[01:24:05] that isn't actively optimizing against us. Let's talk about the specific methods other  
[01:24:09] than mechanistic interpretability that you guys are researching. When we talk about  
[01:24:14] RLHF or Constitution AI, if you had to put it in terms of human psychology,  
[01:24:21] what is the change that is happening? Are we creating new drives, new goals, new thoughts?  
[01:24:28] How is the model changing in terms of psychology? All those terms are inadequate for describing  
[01:24:36] what's happening. It's not clear how useful they are as abstractions for humans either.  
[01:24:39] I think we don't have the language to describe what's going on. And again, I'd love to have the  
[01:24:43] X-ray. I'd love to look inside and say and kind of actually know what we're talking about instead of  
[01:24:50] basically making up words, which is what I do what you're doing in asking this question.  
[01:24:56] We should just be honest. We really have very little idea what we're talking about. It would  
[01:25:02] be great to say, well, what we actually mean by that is this circuit within here turns on,  
[01:25:07] and after we've trained the model, then this circuit is no longer operative or weaker.  
[01:25:16] It's going to take a lot of work to be able to do that.  
[01:25:19] Model organisms, which you hinted at before when you said we're doing these evaluations to see if  
[01:25:23] they're capable of doing dangerous things now and currently not, how worried are you about a  
[01:25:28] lab leak scenario? Where in fine tuning it or in trying to get these models to elicit dangerous  
[01:25:35] behaviors, make bioweapons or something, you leak somehow and it actually makes the bioweapons  
[01:25:40] instead of telling you it can make the bioweapons. It's not that much of a concern with today's  
[01:25:42] passive models. If we were to fine tune a model, we would do it privately and we work  
[01:25:52] with the experts and so the leak would be like, suppose the model got open sourced or something.  
[01:26:02] For now, it's mostly a security issue. In terms of models truly being dangerous,  
[01:26:08] we do have to worry that if we make a truly powerful model and we're trying to see what  
[01:26:14] makes it dangerous or safe, then there could be more of a one shot thing where there’s some  
[01:26:19] risk that the model takes over. The main way to control that is to make sure that  
[01:26:23] the capabilities of the model that we test are not such that they're capable of doing this.  
[01:26:28] At what point would the capabilities be so high where you say, I don't even want to test this?  
[01:26:33] Well, there's different things. There's capability testing..  
[01:26:36] But that itself could lead to... If you're testing replicate, what if it actually does?  
[01:26:40] Sure. But I think what you want to do is you want to extrapolate. We've talked with Arc about this.  
[01:26:46] You have factors of two of compute, where you're like, can the model do something like open up an  
[01:26:55] account on AWS and make some money for itself? Some of the things that are obvious prerequisites  
[01:27:00] to complete survival in the wild. Just set those thresholds very well below and then  
[01:27:09] as you proceed upward from there, do kind of more and more rigorous tests and be more and  
[01:27:14] more careful about what it is you're doing. On Constitution AI, who decides what the  
[01:27:23] constitution for the next generation of models or a potentially superhuman model  
[01:27:27] is? How is that actually written? Initially to make the constitution,  
[01:27:31] we just took some stuff that was broadly agreed on, like the UN declaration on Human Rights and  
[01:27:39] some of the stuff from Apple's Terms of Service. Stuff that's consensus on what's acceptable to  
[01:27:45] say or what basic things are able to be included. One, for future constitutions, we're looking into  
[01:27:52] more participatory processes for making these. But beyond that, I don't think there should  
[01:27:58] be one constitution for a model that everyone uses. The model’s constitution should be very  
[01:28:06] simple. It should only have very basic facts that everyone would agree on. Then there should be a  
[01:28:12] lot of ways that you can customize, including appending constitutions. And beyond that,  
[01:28:18] we're developing new methods. I'm not imagining that this or this alone is the method that  
[01:28:24] we'll use to train superhuman AI. Many of the parts of capability training may be different,  
[01:28:29] and so it could look very different. There are levels above this. I'm pretty  
[01:28:35] uncomfortable with: here's the AI's constitution, it's going to run the world. From just normal  
[01:28:43] lessons from how societies work and how politics works, that strikes me as fanciful.  
[01:28:57] Even after we've mitigated the safety issues, any good future, even if it has all these  
[01:29:06] security issues that we need to solve, it somehow needs to end with something that's  
[01:29:11] more decentralized and less like a godlike super. I just don't think that ends well.  
[01:29:18] What scientists from the Manhattan Project do you respect most in terms of,  
[01:29:22] they acted most ethically under the constraints they were given. Is there one that comes to mind?  
[01:29:26] I don't know. There's a lot of answers you could give. I'm definitely a fan of Szilard for having  
[01:29:33] kind of figured it out. He was then against the actual dropping of the bomb. I don't actually  
[01:29:40] know the history well enough to have an opinion on whether the demonstration of the bomb could  
[01:29:46] have ended the war. I mean that involves a bunch of facts about Imperial Japan that are complicated  
[01:29:52] and that I'm not an expert on. But Szilard, he discovered this stuff early, he kept it secret,  
[01:30:02] patented some of it and put it in the hands of the British Admiralty. He seemed to display the right  
[01:30:09] kind of awareness as well as discovering stuff. It was when I read that book that when I wrote this  
[01:30:17] big blob of compute doc and I only showed it to a few people and there were other docs that I showed  
[01:30:21] to almost no one. I was a bit inspired by this. Again, we could all get self aggrandizing here.  
[01:30:30] Like we don't know if it's actually going to be something on par with the Manhattan project. This  
[01:30:37] could all be just Silicon Valley people building technology and just having delusions of grandeur.  
[01:30:44] I don't know how it's going to turn out. I mean, if the scaling stuff is true then  
[01:30:47] it's bigger than the Manhattan Project. Yeah, it certainly could be bigger. I think  
[01:30:52] we should always maintain this attitude that it's really easy to fool yourself.  
[01:30:58] If you're a physicist during World War II and you were asked by the government to contribute  
[01:31:01] non replaceable research to the Manhattan Project, what do you think you would have said?  
[01:31:06] Given you're in a war with the Nazis, I don't really see much choice but to do it if it's  
[01:31:16] possible. You have to figure it's going to be done within ten years or so by someone.  
[01:31:21] Regarding cybersecurity, what should we make of the fact that there's a  
[01:31:25] whole bunch of tech companies which have ordinary tech company security policy  
[01:31:30] and it's not obvious that they've been hacked publicly. Coinbase still has its bitcoin.  
[01:31:37] As far as I know my Gmail hasn't been leaked. Should we take from that that current status  
[01:31:43] quo tech company security practices are good enough for AGI or just  
[01:31:47] simply that nobody has tried hard enough? It would be hard for me to speak to current  
[01:31:51] tech company practices and of course there may be many attacks that we don't know about,  
[01:31:54] where things are stolen and then silently used. I think an indication of it is when someone really  
[01:32:00] cares basically cares about attacking someone, then often the attacks happen.  
[01:32:07] Recently we saw that some fairly high officials of the US government had their email accounts hacked  
[01:32:14] via Microsoft. Microsoft was providing the email accounts. Presumably that relayed information  
[01:32:20] that was of great interest to foreign adversaries. It seems to me at least that the evidence is more  
[01:32:30] consistent with, when something is really high enough value, then someone acts and it's stolen.  
[01:32:39] And my worry is that of course with AGI we'll get to a world where the value is seen as incredibly  
[01:32:45] high. It'll be like stealing nuclear missiles or something. You can't be too careful on this stuff.  
[01:32:52] At every place that I've worked, I've pushed for cybersecurity to be better. One of my concerns  
[01:32:56] about cybersecurity is, it's not something you can trumpet. A good dynamic with safety research is,  
[01:33:05] you can get companies into a dynamic and I think we have, where you can get them  
[01:33:10] to compete to do the best safety research and use it as a recruiting point of competition  
[01:33:16] or something. We used to do this all the time with interpretability and then sooner or later  
[01:33:21] other orgs started recognizing the defect and started working on interpretability,  
[01:33:26] whether or not that was a priority to them before. But it's harder to do that with cybersecurity  
[01:33:33] because a bunch of the stuff you have to do quietly. We did try to put out one post about it,  
[01:33:38] but mostly you just see the results. A good norm would be people see these cybersecurity leaks from  
[01:33:49] companies or leaks the model parameters or something and say they screwed up,  
[01:33:53] that's bad. If I'm a safety person, I might not want to work there.  
[01:33:58] Of course, as soon as I say that, we'll probably have a security breach tomorrow. But  
[01:34:03] that's part of the game here, that's part of trying to make things safe.  
[01:34:08] I want to go back to the thing we're talking about earlier, where the ultimate level of  
[01:34:13] cybersecurity required two to three years from now and whether it requires a bunker, are you  
[01:34:18] actually expecting to be in a physical bunker in two to three years, or is that just a metaphor?  
[01:34:23] That’s a metaphor. We’re still figuring it out. Something I would think about is the security of  
[01:34:30] the data center, which may not be in the same physical location as us, but we've worked very  
[01:34:34] hard to make sure it's in the United States. But securing the physical data centers and the GPUs.  
[01:34:42] If someone was really determined, some of the really expensive attacks just involve going into  
[01:34:45] the data center and just trying to steal the data directly or as it's flowing from a data  
[01:34:50] center to us. These data centers are going to have to be built in a very special way. Given the way  
[01:34:57] things are scaling up, we're anyway heading to a world where the networks of data centers cost as  
[01:35:04] much as aircraft carriers. They're already going to be pretty unusual objects but in addition to  
[01:35:11] being unusual in terms of their ability to link together and train gigantic, gigantic models,  
[01:35:18] they're also going to have to be very secure. Speaking of which, there's been rumors on the  
[01:35:23] difficulty of procuring the power and the GPUs for the next generation of models.  
[01:35:27] What has the process been like to secure the necessary components to do the next generation?  
[01:35:32] That's something I can't go into great detail about. I will say, people are thinking of  
[01:35:39] industrial scale data centers and people are not thinking at the scale that these models are going  
[01:35:44] to go to very soon. Whenever you do something at a scale where it's never been done before,  
[01:35:50] every single component, every single thing has to be done in a new way than it was before. And so  
[01:35:55] you may run into problems with surprisingly simple components. Power is one that you mentioned.  
[01:36:03] And is this something that Anthropic has to handle, or can you just outsource it?  
[01:36:06] For data centers, we work with cloud providers, for instance.  
[01:36:09] What should we make about the fact that these models require so much training and the entire  
[01:36:15] corpus of internet data in order to be subhuman? Whereas GPT-4, there's been estimates that it  
[01:36:24] was like 10^25 Flops or something, you can take these numbers with a grain of salt,  
[01:36:30] but there's reports that the human brain, from the time it is born to the time a human being  
[01:36:35] is 20 years old, is on the order of 10^14 Flops to simulate all those interactions.  
[01:36:40] We don't have to go into the particulars on those numbers, but should we be worried about  
[01:36:44] how sample inefficient these models seem to be? That's one of the remaining mysteries. One way  
[01:36:50] you could phrase it is that the models are maybe two to three orders of magnitude smaller than the  
[01:36:56] human brain. If you compare it to the number of synapses, while at the same time being trained  
[01:37:00] on three to four more orders of magnitude of data. If you compare the number of words a human sees as  
[01:37:09] they're developing to age 18, I don't remember exactly, but I think it's in the hundreds of  
[01:37:13] millions, whereas for the models, we're talking about the hundreds of billions to the trillions.  
[01:37:18] So what explains this? There are these offsetting things where the models are smaller, they need a  
[01:37:24] lot more data. They're still below human level. There's some way in which  
[01:37:33] the analogy to the brain is not quite right or is breaking down or there's some missing factor.  
[01:37:38] This is just like in physics, where we can't explain the Michelson-Morley experiment, or  
[01:37:44] one of the other 19th century physics paradoxes. It's one thing we don't quite understand. Humans  
[01:37:50] see so little data, and they still do fine. One theory on it, it could be that it's like  
[01:37:57] our other modalities. How do we get 10^14 bits into the human brain? Most of it is these images,  
[01:38:05] and maybe a lot of what's going on inside the human brain is, our mental workspace involves  
[01:38:10] all these simulated images or something like that. But honestly, intellectually we have to admit that  
[01:38:17] that's a weird thing that doesn't match up. And it's one reason I'm a bit skeptical of biological  
[01:38:23] analogies. I thought in terms of them, like, five or six years ago, but now that we actually have  
[01:38:28] these models in front of us as artifacts, it feels like almost all the evidence from that  
[01:38:32] has been screened off by what we've seen. And what we've seen are models that are much smaller  
[01:38:37] than the human brain and yet can do a lot of the things that humans can do, and yet, paradoxically,  
[01:38:42] require a lot more data. Maybe we'll discover something that makes it all efficient,  
[01:38:46] or maybe we'll understand why the discrepancy is present, but at the end of the day, I don't  
[01:38:52] think it matters, right? If we keep scaling the way we are. I think what's more relevant at this  
[01:38:56] point is just measuring the abilities of the model and seeing how far they are from humans,  
[01:39:01] and they don't seem terribly far to me. Does this scaling picture and the big blob  
[01:39:04] of compute more generally, underemphasize the role that algorithmic progress has played. When  
[01:39:11] you composed the big blob of compute, you're presumably talking about LSTMs at that point,  
[01:39:17] the scaling on that would not have you at Claude 2 at this point.  
[01:39:21] Are you underemphasizing the role that an improvement of the scale of  
[01:39:25] Transformer could be having here, when you put it behind the label of scaling?  
[01:39:28] This big blob of compute document, which I still have not made public, I probably should  
[01:39:32] for historical reasons. I don't think it would tell anyone anything they don't know now. But  
[01:39:37] when I wrote it, I actually said, look, there are seven factors and I wasn't like, these are all the  
[01:39:44] factors but just let me give some sense of the kinds of things that matter and what don't. There  
[01:39:50] could be nine, there could be five. But the things I said were — Number of parameters matters. Scale  
[01:39:56] of the model matters. Compute matters. Quantity of data matters. Quality of data matters. Loss  
[01:40:05] function matters. Are you doing RL? Are you doing next word prediction? If your loss function isn't  
[01:40:11] rich or doesn't incentivize the right thing, you won't get anything. Those were the key four ones,  
[01:40:17] which I think are the core of the hypothesis. But then I said three more things. One was  
[01:40:21] symmetries, which is basically if your architecture doesn't take into account  
[01:40:27] the right kinds of symmetries, it doesn't work or it's very inefficient. For example, convolutional  
[01:40:34] neural networks take into account translational symmetry. LSTMs take into account time symmetry.  
[01:40:41] But a weakness of LSTMs is that they can't attend over the whole context. So there's kind of this  
[01:40:46] structural weakness. If a model isn't structurally capable of absorbing and managing things that  
[01:40:54] happened in a far enough distant past, then it's like the compute doesn't flow. The spice doesn't  
[01:41:00] flow. The blob has to be unencumbered. It's not going to work if you artificially close things  
[01:41:10] off. And I think RNNs and LSTMs artificially close things off because they close you off  
[01:41:16] to the distant past. Again, things need to flow freely. If they don't, it doesn't work.  
[01:41:22] And then I added a couple things. One of them was conditioning, which is if the thing you're  
[01:41:29] optimizing with is just really numerically bad, you're going to have trouble. And so  
[01:41:33] this is why atom works better than normal STD. I'm forgetting what the 7th condition was,  
[01:41:40] but it was similar to things like this, where if you set things up in a way that's set up to  
[01:41:48] fail or that doesn't allow the compute to work in an uninhibited way, then it won't  
[01:41:52] work. Transformers were kind of within that even though I can't remember if the transformer paper  
[01:41:58] had been published, it was around the same time as I wrote that document. It might have  
[01:42:01] been just before. It might have been just after. From that view it sounds like the way to think  
[01:42:07] about these algorithmic progresses is not as increasing the power of the blob of compute,  
[01:42:12] but simply getting rid of the artificial hindrances that older architectures have.  
[01:42:19] That's a little how I think about it. If you go back to Ilya's, the models want to learn, the  
[01:42:25] compute wants to be free and it's being blocked in various ways where you don't understand that  
[01:42:31] it's being blocked until you need to free it up. I love the gradients changing that to spice.  
[01:42:38] On that point, though, do you think that another thing on the scale of a transformer is coming down  
[01:42:46] the pike to enable the next great iteration? I think it's possible. People have worked on  
[01:42:51] things like trying to model very long time dependencies or there's various different  
[01:42:59] ideas where I could see that we're missing an efficient way of representing or dealing with  
[01:43:04] something. I think those inventions are possible. I guess my perspective would be, even if they  
[01:43:10] don't happen, we're already on this very, very steep trajectory. Unless we're constantly  
[01:43:17] trying to discover them, as are others, but things are already on such a fast trajectory,  
[01:43:22] all that would do is speed up the trajectory even more, and probably not by that much  
[01:43:26] because it's already going so fast. Is having an embodied version of a  
[01:43:32] model at all important in terms of getting either data or progress?  
[01:43:36] I'd think of that less in terms of a new architecture and more in terms  
[01:43:40] of a loss function like the data, the environments you're exposing yourself  
[01:43:45] to end up being very different. That could be important for learning some skills, although  
[01:43:51] data acquisition is hard and so things have gone through the language route and I would guess will  
[01:43:57] continue to go through the language route even as more is possible in terms of embodiment.  
[01:44:03] And then the other possibilities you mentioned. RL, you can see it as...  
[01:44:07] We kind of already do RL with RLHF. Is this alignment? Is this capabilities? I always think  
[01:44:12] in terms of the two snakes, they're often hard to distinguish. We already kind of use RL on these  
[01:44:18] language models but I think we've used RL less in terms of getting them to take actions and do  
[01:44:23] things in the world but when you take actions over a long period of time and understand the  
[01:44:29] consequences of those actions only later, then RL is a typical tool we have for that. So I would  
[01:44:34] guess that in terms of models taking action in the world, that RL will become a thing with all the  
[01:44:41] power and all the safety issues that come with it. When you project out in the future, do you see the  
[01:44:46] way in which these things will be integrated into productive supply chains? Do you see them talking  
[01:44:52] with each other and criticizing each other and contributing to each other's output? Or is it just  
[01:44:57] that one model one shots the answer or the work. Models will undertake extended tasks. That will  
[01:45:05] have to be the case. We may want to limit that to some extent because it may make some of the safety  
[01:45:10] problems easier but some of that will be required. In terms of our models talking to models or are  
[01:45:16] they talking to humans? Again, this goes kind of out of the technical realm and into the  
[01:45:22] sociocultural economic realm where my heuristic is always that it's very, very difficult to predict  
[01:45:30] things. I feel like these scaling laws have been very predictable but then when you say like,  
[01:45:37] when is there going to be a commercial explosion in these models? Or what's the form it's going to  
[01:45:41] be? Or are the models going to do things instead of humans or pairing with humans? Certainly my  
[01:45:47] track record on predicting these things is terrible but also looking around, I don't  
[01:45:52] really see anyone whose track record is great. You mentioned how fast progress is happening,  
[01:45:56] but also the difficulties of integrating within the existing economy into the way things work.  
[01:46:02] Do you think there will be enough time to actually have large revenues from AI products  
[01:46:07] before the next model is just so much better or we're in a different landscape entirely?  
[01:46:12] It depends what you mean by large. I think multiple companies are already  
[01:46:16] in the 100 million to billion per year range. Will it get to the 100 billion or  
[01:46:22] trillion range before? That stuff is just so hard to predict. And it's not even super well defined.  
[01:46:32] Right now there are companies that are throwing a lot of money at generative AI as customers.  
[01:46:40] That's the right thing for them to do, and they'll find uses for it, but it doesn't  
[01:46:44] mean they're finding uses or the best uses from day one. Even money changing hands is not quite  
[01:46:52] the same thing as economic value being created. But surely you've thought about this from the  
[01:46:56] perspective of Anthropic, where if these things are happening so fast,  
[01:46:58] then it should be an insane valuation, right? Even us who have not been super focused on  
[01:47:04] commercialization and more on safety, the graph goes up and it goes up relatively quickly.  
[01:47:12] I can only imagine what's happening at the orgs where this is their singular focus.  
[01:47:20] It's certainly happening fast but it's an exponential from the small base  
[01:47:25] while the technology itself is moving fast. It's a race between how fast the technology  
[01:47:31] is getting better and how fast it's integrated into the economy. And I think that's just a very  
[01:47:36] unstable and turbulent process. Both things are going to happen fast but if you ask me exactly  
[01:47:42] how it's going to play out, exactly what order things are going to happen, I don't know. And  
[01:47:48] I'm skeptical of the ability to predict. I'm curious. With regards to Anthropic  
[01:47:52] specifically, you're a public benefit corporation and rightfully so,  
[01:47:57] you want to make sure that this is an important technology. Obviously, the only thing you want  
[01:48:01] to care about is not shareholder value. But how do you talk to investors who are  
[01:48:05] putting in hundreds of millions, billions of dollars of money? How do you get them  
[01:48:11] to put in this amount of money without the shareholder value being the main concern?  
[01:48:16] I think the LTBT (Long Term Benefit Trust) is the right thing on this. We're going to talk  
[01:48:21] more about the LTBT, but some version of that has been in development since the beginning  
[01:48:25] of Anthropic, even formally. Even as the body has changed, from the beginning, it was like,  
[01:48:35] this body is going to exist and it's unusual. Every traditional investor who invests in  
[01:48:41] Anthropic looks at this. Some of them are just like, whatever, you run your company how you want.  
[01:48:48] Some of them are like, oh my god, this body of random people could move Anthropic in a direction  
[01:48:57] that's totally contrary to shareholder value. Now there are legal limits on that, of course,  
[01:49:02] but we have to have this conversation with every investor. And then it gets into a conversation of,  
[01:49:07] well, what are the kinds of things that we might do that would be contrary to the  
[01:49:14] interests of traditional investors. And just having those conversations  
[01:49:18] has helped get everyone on the same page. I want to talk about the fact that so many  
[01:49:24] of the founders and the employees at Anthropic are physicists. We talked in the beginning about  
[01:49:30] the scaling laws and how the power laws from physics are something you see here,  
[01:49:34] but what are the actual approaches and ways of thinking from physics that seem to have carried  
[01:49:39] over so well? Is that notion of effective theory super useful? What is going on here?  
[01:49:45] Part of it is just that physicists learn things really fast. We have generally found that if we  
[01:49:51] hire someone who is a Physics PhD or something, that they can learn ML and contribute just very  
[01:49:57] quickly in most cases. And because several of our founders myself, Jared Kaplan, Sam McCandlish  
[01:50:04] were physicists, we knew a lot of other physicists, and so we were able to hire  
[01:50:07] them. And now there might be 30 or 40 of them here. ML is not still not yet a field that has  
[01:50:15] an enormous amount of depth, and so they've been able to get up to speed very quickly.  
[01:50:18] Are you concerned that there's a lot of people who would have been doing physics or something,  
[01:50:24] they would’ve gone into finance instead and since Anthropic exists,  
[01:50:28] they have now been recruited to go into AI. You obviously care about AI safety, but maybe  
[01:50:37] in the future they leave and they get funded to do their own thing. Is that a concern that you're  
[01:50:41] bringing more people into the ecosystem here? There's a broad set of actions, like we're causing  
[01:50:47] GPUs to exist. There's a lot of side effects that you can't currently control or that you  
[01:50:53] just incur if you buy into the idea that you need to build frontier models. And that's one of them.  
[01:50:58] A lot of them would have happened anyway. I mean, finance was a hot thing 20 years ago,  
[01:51:02] so physicists were doing it. Now ML is a hot thing, and it's not like we've caused them to  
[01:51:07] do it when they had no interest previously. But again, at the margin, you're bidding things up,  
[01:51:14] and a lot of that would have happened anyway. Some of it wouldn't but it's all part of the calculus.  
[01:51:18] Do you think that Claude has conscious experience? How likely do you think that is?  
[01:51:22] This is another of these questions that just seems very unsettled and uncertain. One thing  
[01:51:27] I'll tell you is I used to think that we didn't have to worry about this at all until models  
[01:51:31] were operating in rich environments, like not necessarily embodied, but they needed  
[01:51:38] to have a reward function and have a long lived experience. I still think that might be the case,  
[01:51:44] but the more we've looked at these language models and particularly looked inside them  
[01:51:49] to see things like induction heads, a lot of the cognitive machinery that you would need  
[01:51:54] for active agents already seems present in the base language models. So I'm not quite as sure  
[01:52:00] as I was before that we're missing enough of the things that you would need. I think  
[01:52:07] today's models just probably aren't smart enough that we should worry about this too much but I'm  
[01:52:13] not 100% sure about this, and I do think in a year or two, this might be a very real concern.  
[01:52:19] What would change if you found out that they are conscious? Are you worried that you're  
[01:52:23] pushing the negative gradient to suffering? Conscious, again, is one of these words that  
[01:52:27] I suspect will not end up having a well defined.. I suspect that's a spectrum. Let's say we discover  
[01:52:43] that I should care about Claude’s experience as much as I should care about a dog or a monkey  
[01:52:48] or something. I would be kind of worried. I don't know if their experience is positive  
[01:52:54] or negative. Unsettlingly I also don't know I wouldn't know if any intervention that we made  
[01:53:00] was more likely to make Claude have a positive versus negative experience versus not having one.  
[01:53:06] If there's an area that is helpful with this, it's maybe mechanistic interpretability because I think  
[01:53:11] of it as neuroscience for models. It's possible that we could shed some light on this. Although  
[01:53:18] it's not a straightforward factual question. It depends what we mean and what we value.  
[01:53:23] We talked about this initially, but I want to get more specific. We talked initially about  
[01:53:28] now that you're seeing these capabilities ramp up within the human spectrum, you think that the  
[01:53:33] human spectrum is wider than we thought but more specifically, how is the way you think about human  
[01:53:39] intelligence different. The way you're seeing these marginally useful abilities emerge? How does  
[01:53:46] that change your picture of what intelligence is? For me, the big realization on what intelligence  
[01:53:51] is came with the blob of compute thing. There might be all these separate modules. There  
[01:53:57] might be all this complexity. Rich Sutton called it The Bitter Lesson. It has many names. It's  
[01:54:04] been called the scaling hypothesis. The first few people who figured it out was around 2017.  
[01:54:09] You could go further back. I think Shane Legg was maybe the first person who really knew it,  
[01:54:14] maybe Ray Kurzweil, although in a very vague way. But the number of people who understood  
[01:54:21] it went up a lot around 2014 to 2017. I think that was the big realization.  
[01:54:29] How did intelligence evolve? If you don't need very specific conditions to create it,  
[01:54:34] if you can create it just from the right kind of gradient and loss signal, then of course  
[01:54:40] it's not so mysterious how it all happened. It had this click of scientific understanding.  
[01:54:46] In terms of watching what the models can do, how has it changed my view of human intelligence? I  
[01:54:53] wish I had something more intelligent to say on that. One thing that's been surprising  
[01:55:00] is I thought things might click into place a little more than they do. I thought different  
[01:55:06] cognitive abilities might all be connected and there was more of one secret behind them. But  
[01:55:12] the model just learns various things at different times. It can be very good at coding but it can't  
[01:55:19] quite prove the prime number theorem yet. And I guess it's a little bit the same for humans,  
[01:55:25] although it's weird the juxtaposition of things it can do and not. I guess the main lesson is having  
[01:55:31] theories of intelligence or how intelligence works. A lot of these words just dissolve into  
[01:55:39] a continuum. They just kind of dematerialize. I think less in terms of intelligence and more  
[01:55:45] in terms of what we see in front of us. Two things are really surprising to me.  
[01:55:49] One is how discrete these different paths of intelligent things that contribute to  
[01:55:56] loss are rather than just being one reasoning circuit or one general intelligence. And the  
[01:56:00] other surprising and interesting thing is, many years from now, it'll be one of those things that  
[01:56:06] you’ll wonder why it wasn't obvious to you? If you're seeing these smooth scaling curves,  
[01:56:11] why were you not completely convinced at the time? You've been less public than the CEOs of other AI  
[01:56:18] companies. You're not posting on Twitter, you're not doing a lot of podcasts except for this one.  
[01:56:24] What gives? Why are you off the radar? I aspire to this and I'm proud of this.  
[01:56:31] If people think of me as boring and low profile, this is actually kind of what I want.  
[01:56:37] I've just seen cases with a number of people I've worked with, where attaching  
[01:56:47] your incentives very strongly to the approval or cheering of a crowd can destroy your mind,  
[01:56:54] and in some cases, it can destroy your soul. I've deliberately tried to be a little bit low  
[01:57:00] profile because I want to defend my ability to think about things intellectually in a way that's  
[01:57:09] different from other people and isn't tinged by the approval of other people. I've seen cases  
[01:57:16] of folks who are deep learning skeptics, and they become known as deep learning skeptics on Twitter.  
[01:57:21] And then even as it starts to become clear to me, they've sort of changed their mind. This is  
[01:57:26] their thing on Twitter, and they can't change their Twitter persona and so forth and so on.  
[01:57:30] I don't really like the trend of personalizing companies. The whole cage match between CEOs  
[01:57:38] approach. I think it distracts people from the actual merits and concerns of the company in  
[01:57:46] question. I want people to think in terms of the nameless, bureaucratic institution and its  
[01:57:58] incentives more than they think in terms of me. Everyone wants a friendly face, but actually,  
[01:58:02] friendly faces can be misleading. Okay, well, in this case,  
[01:58:05] this will be a misleading interview because this has been a lot of fun.  
[01:58:09] Indeed. Yeah, this has been a blast. I’m super glad you  
[01:58:12] came on the podcast and hope people enjoyed it. Thanks for having me.  
