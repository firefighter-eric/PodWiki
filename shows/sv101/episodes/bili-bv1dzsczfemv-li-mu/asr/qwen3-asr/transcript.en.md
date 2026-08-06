# 语音智能体商业落地的教训、经验与实践｜李沐硅谷101年度线下大会演讲（全英）

[00:00:00] Yeah, today I'm gonna talk about voice agent.  
[00:00:02] That's a very top hot topic this year.  
[00:00:05] And the reason is like people think, okay, that's technology is ready to use, and it's like it's ready to landing.  
[00:00:12] So today I'm gonna share two of our past projects based on voice agent, show some lessons and best practice how to help customers use it.  
[00:00:24] And so let's get started.  
[00:00:27] So first of all, what's a voice agent?  
[00:00:30] Basically, that's just an agent with a voice.  
[00:00:33] So user interact with agent with a voice interface.  
[00:00:37] So we hope that you have a more nature way to interact with large language model.  
[00:00:43] So two things here is that first of all, it's real time.  
[00:00:49] It's a little bit different to video generation.  
[00:00:51] It can be off off time off time like offline.  
[00:00:56] Right now, you must be the response must be within one second, for example, the end to end latency.  
[00:01:02] The second one is like most cases people don't do chit chat.  
[00:01:07] Like chit chat is kind of companion, but in most cases you have particular particular task.  
[00:01:12] For example, you want to do customer support, you want to do information retrieval, or you want to sell something.  
[00:01:18] Companion sometimes is it's a task.  
[00:01:21] It's not just chit chat.  
[00:01:22] You have some particular goals.  
[00:01:24] Maybe you want to tell story.  
[00:01:26] Maybe you want to do something else.  
[00:01:28] So this is basically what's a voice agent.  
[00:01:31] Then in the rest of the talk, we're gonna have two examples show we how build it and what lessons we have.  
[00:01:39] Here's the first example.  
[00:01:41] And I really need to find a way out of here fast.  
[00:01:47] Okay, I guess you're cutting straight to the chase here, but at least can you tell me a little bit more about yourself, like?  
[00:01:56] Okay, let's see.  
[00:01:57] All right, I'm a sophomore at Mariana University studying astrophysics.  
[00:02:03] So this is a game we started like two and a half year ago.  
[00:02:09] So this is the app.  
[00:02:11] This is the user.  
[00:02:13] So this app is like this guy's called Stella.  
[00:02:16] The user gonna do voice interaction with Stella to help her.  
[00:02:21] So you can see that the whole storyline is driving by how the user's inputs.  
[00:02:26] The task here is open world game.  
[00:02:30] So like this, this sentence is copy from the game which is already launched two two months ago.  
[00:02:37] So basically, Stella landed on a alien planet.  
[00:02:43] So it's that the aircraft is crashed here.  
[00:02:46] So then she asking the players to help.  
[00:02:50] Like okay, so like so strange world, so many options, and I feel a lot of emotions here.  
[00:02:58] So using voice to interact with player to let the player to help her to escape the planets.  
[00:03:05] So that's a very large world setting.  
[00:03:08] That's only the first game.  
[00:03:10] It's a kind of trial game in a very large series.  
[00:03:14] So what voice agent play here?  
[00:03:17] The role here, you you need to be a both agent designer and actor.  
[00:03:23] The game designer means that you want to design the the story which is make sense, is fun to play.  
[00:03:31] So then the agent one, you want to create the dialogue that match the character setting.  
[00:03:39] So this Stella have a particular character setting, like all the background she has, or all the things she has, like kinds of maybe twenty pages of setting.  
[00:03:50] Then that's the actor side.  
[00:03:52] Then for the game designer, you need guide the when when the user interact with the game, you want to guide the storyline, which is if it's just a single line story,  
[00:04:03] is not agent.  
[00:04:04] Right now, kinds of complex structure or even graph structure, and some something have free here.  
[00:04:11] The the issue here is that you want to have really good game.  
[00:04:15] Like if if if how to write a book, how to write a game plot, it have a lot of principle there.  
[00:04:22] Like you want to have the order stage, order pace, all all of the things make the the story looks interesting.  
[00:04:29] The other things like it's a game.  
[00:04:31] You expect people to have actual thing, to actual input with you, like the test and the player to try all the boundaries.  
[00:04:39] The agent must be within their setting.  
[00:04:43] Sometimes like this game is on a sci-fi world, like two maybe two thousand year later, and you have random chat setting.  
[00:04:51] If you say okay, what's a movie you you you you watch recently?  
[00:04:56] If you pick up a movie right now, it maybe wow you watch the movie like one thousand years ago.  
[00:05:02] So and but the things like all the language model trained on the current data.  
[00:05:07] Now you want to how to move all the setting to your future worlds.  
[00:05:12] So I share a particular like earlier log here and show how some challenging task.  
[00:05:21] So this is the log on a very early earlier stage, still in Chinese.  
[00:05:26] So the idea here is Stella find some food, asking the player to say okay, which food I gonna choose?  
[00:05:32] The player the the player setting here, I will help you.  
[00:05:35] So I think it cannot eatable.  
[00:05:37] You cannot eat anything.  
[00:05:39] So then oh, the Stella first thing like you need to find some meat to eat.  
[00:05:44] So you have a rack to search how to play how to catch animals here.  
[00:05:48] But the the the answer is you cannot.  
[00:05:50] This you didn't see any animal yet.  
[00:05:53] So the Stella response like okay, I want to eat meat, but I can only have vegetable here.  
[00:05:58] And the player don't want to help.  
[00:06:00] Stella say okay, I really need your help.  
[00:06:03] Okay, player still like I don't want to help.  
[00:06:06] The things like if you stuck here, the the story can not move on.  
[00:06:11] So the prompt is saying like okay, after three trials, just move choose something by yourself.  
[00:06:19] And so but then it's a random choice.  
[00:06:24] Stella is dying.  
[00:06:25] So say okay, it's dying.  
[00:06:26] But the the the player saying okay, you're gonna die.  
[00:06:32] It's not a nice guy here, but you need be nice here.  
[00:06:35] So the challenge here is like it's open the game, but your response should be make sense.  
[00:06:44] Like it's an open world game.  
[00:06:46] It's like three or maybe one two thousand year later.  
[00:06:50] Not every world setting specified.  
[00:06:53] Lot of thing like you can when you develop the game, the game designer cannot write anything for you.  
[00:06:58] You need to think okay, that thing make maybe make sense make sense in a two thousand year later.  
[00:07:04] Also need be engaging and fun.  
[00:07:05] So that's that's a game.  
[00:07:07] That's not a chatbot.  
[00:07:08] So that's all the um all the challenges here.  
[00:07:12] So what do we do is like the project launched two two years ago.  
[00:07:17] At that time, you have GPT four, but it's very expensive.  
[00:07:21] And we did some calculations, think if you use GPT four, like okay, that's a huge loss of the revenue.  
[00:07:26] And and that time the best model is Llama two right now.  
[00:07:30] At that time, Llama two is not strong enough.  
[00:07:32] So what we did at that time is we actually pre train thirty B model with kind of five trillion tokens.  
[00:07:40] So but these tokens enriched on the fiction game role play data.  
[00:07:45] The performance kind of match on the Llama two on general task, little better on the role playing, and but the the lesson we got is like okay, pre train the model take a few months,  
[00:07:57] and even that you kind of outperform Llama two, but you have Llama two seventy B.  
[00:08:03] So, like, if spend too much time on pre-training, you maybe the the progress isn't so great.  
[00:08:10] So that's kind of the lesson we got.  
[00:08:11] That's we're gonna say why that's maybe a bad choice.  
[00:08:16] Another thing we did is like, okay, because GPU is so expensive, that's two years ago, and we we spent a lot of effort to actually build data center by ourselves.  
[00:08:24] So if you own a data center, the cost is much lower.  
[00:08:27] And then we move to post-training.  
[00:08:30] The post-training is that the key thing here, you have very complex storyline workflow.  
[00:08:35] That's an example.  
[00:08:36] That's not a real one.  
[00:08:37] And the real was much more complicated.  
[00:08:40] And then we have kind of twenty laborers.  
[00:08:43] We need train the laborer to be a good game designer because like this particular way how you response.  
[00:08:49] Um, then ranking and evaluating all the model preference.  
[00:08:53] So using these two, we spend kind of quarter here, and can outperform GPT four on this particular scenario.  
[00:09:01] For all other game, we use human to play, so you can outperform GPT four.  
[00:09:06] But the question here is like, okay, that's a single game.  
[00:09:09] That's the tiny bit of a whole open world game.  
[00:09:13] I how what if you want to do multiple games?  
[00:09:17] Then we get another phase is that we want to expand to a broader range of games and characters.  
[00:09:23] So you can less rely on prompt engineer at that time.  
[00:09:26] Prompt engineer is very complicated right now.  
[00:09:28] It's like and even different versions of GPT four is very sensitive to prompt engineer.  
[00:09:35] So the thing is like, yes, we can help, but you want to design game designer to write prompt engineer.  
[00:09:41] So the idea here at that time is like it's still like one and a half year ago.  
[00:09:46] The idea at that time is like you need pre-train a real world model, can distinguish which one is good, which one is bad, and because you cannot rely on humans to do it.  
[00:09:56] So at that time, we first train a reward model to tell you which response is good, in this game setting.  
[00:10:04] Then you can post train another model for it.  
[00:10:08] The one important lesson we got is like even this is for game sounds like simple, but it's still a lot of things like instruction following you need to make sense.  
[00:10:19] So the model still need to be very general enough.  
[00:10:22] So even that you train the in domain model, the model must be good in general task.  
[00:10:29] If you think okay, the best open AI or best like closed API is like the score is ninety, but in your application, the general task need to be eighty five.  
[00:10:40] If you lower than that one, you're gonna think you have a you have a ceiling flaw on on your task.  
[00:10:46] So that's the you first guarantee the general task is good.  
[00:10:50] Then for your particular task, we kind of create a in domain evaluation.  
[00:10:56] So you have a lot of character settings, a lot of thing settings, and for different game settings, you want to make sure like under this setting, you follow all the settings and the response is good,  
[00:11:08] follow the instruction, follow the thing.  
[00:11:10] And then once you have this benchmark, you can tune the model so that you can be be the best compared to others.  
[00:11:18] I think that's a very general pattern that you care about the in domain performance.  
[00:11:23] The key thing here like you really want to develop a really good in domain evaluation task, so you can say I I can see the model improve on this one, but at the same time guarantee your model performs well on all these other general tasks.  
[00:11:37] So the lessons we got is like the intelligence came from pre-training.  
[00:11:42] So after we finish the whole projects, but then we think backwards, all the all the big improvements from pre-training on massive data.  
[00:11:52] So it makes us rethink maybe we give give up on the pre-training, maybe a bad idea.  
[00:11:57] We maybe spend another quarter on pre-training.  
[00:12:00] So that's kind of the lesson we got.  
[00:12:02] And  
[00:12:03] But still, like it's it's still limited.  
[00:12:06] The dialogue quality declines after 50 turns.  
[00:12:09] It's still right now, like given a complex setting after 50 turns conversation, then we think that maybe the model can'ts of become the intelligence much lowered.  
[00:12:19] Also, the models nowadays still still struggle with complex word setting, and you have multiple characters.  
[00:12:28] So it's still hard right now.  
[00:12:29] Even like if you look at all this voice model, all this video model, can'ts of two to three characters.  
[00:12:36] That's limit.  
[00:12:37] Even for the the text part, like if you have four set four characters, it's very challenging right now.  
[00:12:44] The other things like in the demo you see the latency is big.  
[00:12:48] It's term by term based.  
[00:12:50] So all the projects we hear is focus on the large language model itself.  
[00:12:55] Then the lesson we got is like if you really want to truly human like interactions, you can'ts of need to tune the architecture a little bit.  
[00:13:03] Not by the traditional like three component and architecture.  
[00:13:07] So that's become our next projects.  
[00:13:10] Is this a good time to talk?  
[00:13:12] Actually, I'm just about to head out the door.  
[00:13:16] No problem, John.  
[00:13:17] I know how busy things get.  
[00:13:19] If you'd prefer, I can give you a call back at a time that's better for you.  
[00:13:23] To be honest, I think I'm all set.  
[00:13:26] I already have health insurance through my job.  
[00:13:29] That's great, and I'm glad you're covered.  
[00:13:31] A lot of folks I talk to do have something through work, but many don't realize there are options that could lower their out of pocket costs.  
[00:13:39] Okay, that's a very different one.  
[00:13:41] It's sell insurance.  
[00:13:42] So before it's again, right now we sell insurance.  
[00:13:45] At the first time, I think maybe sell insurance like you can be very creative.  
[00:13:50] Creative, you can do whatever you want to sell something.  
[00:13:53] But in reality, it's pretty very formal.  
[00:13:55] Like first of all, you cannot call anyone you want to call.  
[00:14:00] The the user you call must be submit some information, so shows their interest on your product.  
[00:14:06] Secondly, it's very highly regulated the whole insurance industry.  
[00:14:11] So let me explain this problem.  
[00:14:14] So right now we do AI telemarketer.  
[00:14:17] The agent role is like a telemarketer.  
[00:14:20] So right now this particular example is like we sell health insurance through phone, and but on multiple countries.  
[00:14:28] The thing, the requirement you have two requirement.  
[00:14:31] You must you must pass the telemarketing certification.  
[00:14:35] Like the human you have 80 score to pass.  
[00:14:39] This one must be pass this certification before you can launch.  
[00:14:43] Secondly, you have some performance metrics.  
[00:14:46] You you're able to sell at a particular threshold.  
[00:14:49] Like giving you like 1,000 customers, you call them.  
[00:14:53] You must be able to sell a particular number of sales.  
[00:14:57] Also, the complaints must below particular number.  
[00:15:00] If the people say, okay, I feel so bad.  
[00:15:02] Like like you sell not true information or the experience is bad, they they're gonna complain that insurance company really care about it.  
[00:15:11] So the capacity you need here, first of all, you need to be intelligent.  
[00:15:15] You need follow the sales playbook with precise answer.  
[00:15:19] We're gonna show what is precise answer means.  
[00:15:22] You need to able to use tools because insurance you have a lot of internal tools to query and some math.  
[00:15:28] Like you need a lot of combinations here.  
[00:15:30] Also, you need to be very human like.  
[00:15:33] And if you call someone, maybe this guy's out of door like a lot of noise and maybe have some accent.  
[00:15:40] And also you need have some and the the voice need to be realistic.  
[00:15:45] It's not so robotic.  
[00:15:48] And the last one is like entering the latency.  
[00:15:50] When I finish my sentence, your response must be within one second.  
[00:15:55] Otherwise, you feel like it's a little not so responsive.  
[00:15:58] So the precise  
[00:16:00] Response like, for example, if you response you can cover up to six hundred dollar, that's wrong, totally wrong.  
[00:16:07] You failed this exam because the precise answer, the precise one is like cover four hundred dollars for some common one, and like the six hundred dollar only for the front teeth.  
[00:16:18] So that's it's on their play product information.  
[00:16:22] So if you have any issue with your teeth, that's not right.  
[00:16:24] If you have particular like A B diseases with with your teeth, that's the right answer.  
[00:16:29] If you respond this one, it's gonna be you you failed the exam.  
[00:16:33] The other thing, the other more challenging thing here, similar to the gaming, like when some customer and try to asking, okay, can you can we grab times to talk about some the things?  
[00:16:45] You're gonna try three times.  
[00:16:47] If you cannot hand out, you cannot reschedule before three times, or you can reschedule later.  
[00:16:53] So for example, I try the MR try first one, the tenderbox try first one, no, thank you.  
[00:16:59] Then you try second time, no.  
[00:17:02] Then you you try the third one.  
[00:17:03] If the user say, uh huh.  
[00:17:07] So you maybe think, uh huh, maybe interesting.  
[00:17:10] Like if you think the emotions interesting, because you you change the world, uh, you change like, can you tell you, okay, like explain how it can could benefit your uh person personality,  
[00:17:21] a person a personal.  
[00:17:24] Then you maybe think, okay, it's uh huh, maybe the user is interest, but in in reality is like you need to think, you need to find out the voice is impatient.  
[00:17:33] Then given the contact, you can think, okay, I already have tried three times, I need to reschedule.  
[00:17:38] So that's the whole that's the tricky when you have the audio has inputs.  
[00:17:44] So then one key question here, how we do real time?  
[00:17:48] So I kind of um show examples how different model architecture we have right now.  
[00:17:54] The first one is the more the fancy is the one is called end to end full duplex.  
[00:17:58] It means like you have user, you have your model is single model.  
[00:18:03] The user speak to you, which is all the waveform come in.  
[00:18:06] Then you listen to the waveform and response anything during the thing during um the interactions.  
[00:18:13] So in this case, it's easy for user to interrupt.  
[00:18:18] Also easy for the model to do some filling words like user say something, a say a long sentence, you can say yes, yes, that's right.  
[00:18:26] Oh, so that's the most natural way.  
[00:18:28] Um, but now this system is in deployed right now.  
[00:18:33] There's one or two that most you can try, but very few, so not so controllable.  
[00:18:37] So in most cases, like if using even GPT 4.0, I think they're using the end to end half duplex.  
[00:18:44] It means that when the user speak, you have a voice active detector detect detect if the user speak or not.  
[00:18:52] So you have chunk the chunks go to the model, and the model gonna response the previous one.  
[00:18:59] So that's the um um that's the half duplex.  
[00:19:03] The another one is a chain solution.  
[00:19:06] Still similarly, you have turns, but here you have two models, not just single model.  
[00:19:11] So these two models, the first is understanding model, give the audio in, generate the text response.  
[00:19:17] Then the text goes to the generation, generate the audio outside.  
[00:19:22] The last one um is the called uh chain three components, like you have um just do ASR, which is transcribed audio, go to the large language model, and just and then get the response,  
[00:19:37] go to the TTS, which which is generate audio.  
[00:19:41] So for this different one, this one's human like, very human like, you because because the model can interrupt you, and the last one is like uh if you go that direction,  
[00:19:55] it's easy to customize because like you can much easier to adding a new capacity into the agent.  
[00:20:02] So, what we typically use for customers is using the two-component chain solution.  
[00:20:09] So you have, for example, we using thirty B understanding model to generate response.  
[00:20:17] But if the if the user query is complex, maybe using a fine-tuned larger model to do thinking as a tool use.  
[00:20:25] So then it goes to one B generation model to generate the response.  
[00:20:32] Nowadays, all these model is based on single is the same large language model, all based on the same LLM.  
[00:20:39] But you kind of either continue pretrain or fine-tuned with different data mixture.  
[00:20:45] For example, for the understanding, you need have minutes hours of really different quality of audios.  
[00:20:52] You maybe want to have a lot of low quality audios.  
[00:20:55] Also, because you want to the understanding model generate the response, you want to have a lot of text tokens to to to continue pretrain as well.  
[00:21:02] Otherwise, it's just the audio model.  
[00:21:04] The generation model you want to have an even more high quality hours of audios.  
[00:21:13] The large language model you kind of want to train on some domain specific data.  
[00:21:18] So this this architecture makes easy to customize because this is kind of like understanding and generation is kind of general purpose one.  
[00:21:30] You you have this model, you can maybe can use in different scenario.  
[00:21:34] But if you go to particular scenario, you just fine tune this model.  
[00:21:38] That how to get both intelligence and low latency.  
[00:21:41] That's a key for voice agent.  
[00:21:43] Once there's a bunch of idea here.  
[00:21:45] First of all, you want to listen, talk, and think at the same time.  
[00:21:48] Like you you listen and you generate a response sentence sentence, and then between that while you call the large language model to think.  
[00:21:56] Maybe I want to respond better.  
[00:21:58] Maybe I want to do some search better.  
[00:22:00] But all the thing can be asynchronously.  
[00:22:04] The other ones like you want to do context engineers, like it's a one step beyond prompt engineer.  
[00:22:10] That's because for your problem, you maybe have very non context like the product information, also other playbooks, kind of like maybe 100 K tokens.  
[00:22:21] You want to do engineer.  
[00:22:22] You want to dynamically generate construct the content the content context generate the prompt.  
[00:22:29] The other thing like you have you have organizer, which is handle different strategy.  
[00:22:35] Like okay, this kind of what kind of user you think this user is, and then think about different strategy and also do intent analysis.  
[00:22:42] For example, how to count the and some do live task tracking.  
[00:22:48] So all the thing lot together, you can get both intelligence and low latency.  
[00:22:54] So that's kind of the project progress we did.  
[00:22:57] Like started this year, we partner with Fortune 500 leaders.  
[00:23:01] So we start here January, February.  
[00:23:06] You have using ChatGPT before you get this like kind of 55 score.  
[00:23:12] But the the thing is that you need pass this line.  
[00:23:15] This human is a human performance.  
[00:23:17] It's 80.  
[00:23:17] You must pass this line to be launched.  
[00:23:19] You can see like struggle a lot, and then you have steadily progress into and how you you can match human.  
[00:23:27] It take kind of half year or three quarters actually.  
[00:23:31] The lesson here is that the evaluation of the end-to-end voice agents pretty challenge.  
[00:23:36] Like because you need have a real human to make a call.  
[00:23:41] Once you have a call, it's much harder to do like like automatic evaluation.  
[00:23:46] And but that's a key.  
[00:23:47] If you don't have this one, it's it's really hard to know the whole end-to-end performance.  
[00:23:52] And this is ongoing in that handling complex product compilation in real time still pretty.  
[00:23:59] Difficult.  
[00:24:00] Like for insurance, you have a lot of product combinations.  
[00:24:04] How to handle them?  
[00:24:04] The price is different.  
[00:24:05] Maybe I, I okay, that's too expensive for me, and I want a cheap solution.  
[00:24:10] Then you need to pick up the right one for that.  
[00:24:12] The last one, the high security setting make the cost higher.  
[00:24:16] We have dependent discussion talk about if there's only open AI maybe dominate the world, and the to B area is not.  
[00:24:23] The reason is because for insurance, if you launch in different country, the model cannot go, the data cannot go out of this country, or even more, the data cannot go outside the security group of the the company.  
[00:24:37] So either way, you can rent GPT model off on your account, running on your account, or you need you need to develop your own model.  
[00:24:48] So that's why all the things struggling here.  
[00:24:51] And so also that's that's why we spend so many so many efforts to develop the whole models by ourselves rather than just maybe proper engineer open source just API.  
[00:25:02] So I show two examples how we develop voice agent in the past kind of two years.  
[00:25:10] The lesson we got is like the voice agent are pretty highly scalable.  
[00:25:15] Even that the game setting, the insurance settings are very different, but the technology wise, same model architecture, same technologies here.  
[00:25:24] Only things like maybe data is a little bit different, and the evaluation is a little bit different.  
[00:25:28] You need to spend a lot of people on that one.  
[00:25:31] But the model architecture and also the methods, how you post train, how you pre train, how you like all the things, it's the same same thing from game to telemarketing.  
[00:25:42] It's very different one.  
[00:25:43] Game want to be fun.  
[00:25:44] Telemarketing you want to be very precise, but handle the user input very carefully.  
[00:25:49] But still like I think right now it's able to land landing in these areas, but still on the day one setting.  
[00:25:56] The reason is like for game, it's just a very simple game right now, single character, a small world setting.  
[00:26:05] And but how about you want to do a really multiple character, really large world settings?  
[00:26:10] That's really hard right now.  
[00:26:12] For telemarketing, right now we can maybe sell kind of five different health insurance for particular company with some certain of combination combinations.  
[00:26:23] It's hard to sell general purpose.  
[00:26:25] I think in generally this telemarketing is really good for any products between five hundred dollar to five thousand dollar.  
[00:26:31] That's range is really good for this telemarketing to sell.  
[00:26:34] But right now, if you use this trend model to sell any arbitrary new products, you still need a lot of tuning right now.  
[00:26:42] Also there are a lot of other scenarios like before it's like customer service, all the things based on large large language just text large language model.  
[00:26:50] Right now you can adding a voice interface to this application.  
[00:26:53] So there are a lot of applications here.  
[00:26:56] So I think that's why I think we can we are able to land to product right now, but still on day one.  
[00:27:04] So we have maybe another few exciting years to go.  
[00:27:08] The lastly, if you're interested to work with us or partner with us, just contact us.  
[00:27:12] We have a booth.  
[00:27:13] You're gonna be here.  
[00:27:13] Our co-founder will be here.  
[00:27:15] Welcome to talk to us.  
[00:27:16] Yeah, that's all.  
[00:27:17] Thanks everyone.  
