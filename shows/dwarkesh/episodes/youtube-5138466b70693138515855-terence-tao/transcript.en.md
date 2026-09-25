# Terence Tao – How the world’s top mathematician uses AI

[00:00:00] Today, I'm chatting with Terence Tao, who needs no introduction.  
[00:00:04] Terence, I want to begin by having you retell the story of how Kepler discovered the laws of  
[00:00:10] planetary motion because I think this will be a great jumping off point to talk about AI for math.  
[00:00:16] I've always had an amateur interest in astronomy.  
[00:00:18] I've loved stories of how the early astronomers worked out the nature of the universe.  
[00:00:24] Kepler was building on the work of Copernicus, who was himself building on the work of Aristarchus.  
[00:00:31] Copernicus very famously proposed the heliocentric model, that instead of the  
[00:00:36] planets and the Sun going around the Earth, the Sun was at the center of the solar system and the  
[00:00:40] other planets were going around the Sun. Copernicus proposed that the orbits of  
[00:00:45] the planets were perfect circles. His theory fit the observations  
[00:00:50] that the Greeks, the Arabs, and the Indians had worked out over centuries.  
[00:00:57] Kepler learned about these theories in his studies, and he made this observation that the  
[00:01:04] ratios of the size of the orbits that Copernicus predicted seemed to have some geometric meaning.  
[00:01:12] He started proposing that if you take the orbit of the Earth and you enclose it in a cube,  
[00:01:20] the outer sphere that encloses the cube almost perfectly matched the orbit of Mars, and so forth.  
[00:01:26] There were six planets known at the time and five gaps between them, and there were five perfect  
[00:01:30] Platonic solids: the cube, the tetrahedron, icosahedron, octahedron, and dodecahedron.  
[00:01:35] So he had this theory, which he thought was absolutely beautiful,  
[00:01:38] that you could inscribe these Platonic solids between the spheres of the planets.  
[00:01:44] It seemed to fit, and it seemed to him that God's design of the planets was matching this  
[00:01:50] mathematical perfection of the Platonic solids. He needed data to confirm this theory.  
[00:01:56] At the time, there was only one really high-quality dataset in existence.  
[00:02:02] Tycho Brahe, this very wealthy, eccentric Danish astronomer,  
[00:02:08] had managed to convince the Danish government to fund this extremely expensive observatory.  
[00:02:12] In fact, it was an entire island where he had taken decades of observations of all the planets,  
[00:02:18] like Mars and Jupiter, at least every night for which the weather was clear, with the naked eye.  
[00:02:24] He was the last of the naked-eye astronomers. He had all this data which Kepler  
[00:02:28] could use to confirm his theory. Kepler started working with Tycho,  
[00:02:32] but Tycho was very jealous of the data. He only gave him little bits of it at a time.  
[00:02:38] Kepler eventually just stole the data. He copied it and had to have a fight with  
[00:02:44] Brahe's descendants. He did get the data,  
[00:02:48] and then he worked out, to his disappointment, that his beautiful theory didn't quite work.  
[00:02:53] The data was off from his Platonic solid theory by 10% or something.  
[00:02:57] He tried all kinds of fudges, moving the circles around, and it didn't quite work.  
[00:03:02] But he worked on this problem for years and years, and eventually, he figured out how to use the data  
[00:03:08] to work out the actual orbits of the planets. That was an incredibly clever,  
[00:03:15] genius amount of data analysis. And then he worked out that the  
[00:03:21] orbits were actually ellipses, not circles, which was shocking for him.  
[00:03:26] So he worked out the two laws of planetary motion: the ellipses, and also that equal  
[00:03:30] areas sweep out equal times. Then ten years later, after  
[00:03:37] collecting a lot of data—the furthest planets like Saturn and Jupiter were the hardest for  
[00:03:42] him to work out—he finally worked out this third law, that the time it takes for a  
[00:03:50] planet to complete its orbit was proportional to some power of the distance to the Sun.  
[00:03:55] These are the three famous Kepler's laws of motion.  
[00:03:59] He had no explanation for them. It was all driven by experiment,  
[00:04:04] and it took Newton a century later to give a theory that explained all three laws at once.  
[00:04:09] The take I want to try on you is that Kepler was a high-temperature LLM.  
[00:04:17] Newton comes up with this explanation of why the three laws of planetary motion must be true.  
[00:04:22] Of course, the way that Kepler discovers the laws of planetary motion, or figures  
[00:04:26] out the relative orbits of the different planets, is as you say a work of genius.  
[00:04:29] But through his career, he's just trying random relationships.  
[00:04:33] In fact, in the book in which he writes down the third law of planetary motion,  
[00:04:38] it's an aside on The Harmonics of the World, which is just a book about how all these different  
[00:04:44] planets have these different harmonies. And the reason there's so much famine  
[00:04:46] and misery on Earth is because the Earth is mi-fa-mi, that's the note of Earth.  
[00:04:50] It's all this random astrology, but in there is the cube-square law,  
[00:04:54] which tells you what relationship the period has to a planet's distance from the Sun.  
[00:05:00] As you were detailing, if you add that to Newton's F=ma and the equation for centripetal  
[00:05:08] acceleration, you get the inverse-square law. And so Newton works that out.  
[00:05:12] But the reason I think this is an interesting story is that I feel LLMs can do the kind of  
[00:05:18] thing of trying random relationships for twenty years, some of which make no sense,  
[00:05:22] as long as there's a verifiable data bank like Brahe's dataset. "Ok, I'm going to try out random  
[00:05:27] things about musical notes, Platonic objects, or different geometries, I have this bias that  
[00:05:32] there's some important thing about the geometry of these orbits." Then one thing works. As long  
[00:05:36] as you can verify it, these empirical regularities can then drive actual deep scientific progress.  
[00:05:44] Traditionally, when we talk about the history of science, idea generation has  
[00:05:48] always been the prestige part of science. A scientific problem comes with many steps.  
[00:05:53] You have to identify a problem, and then you have to identify a good, fruitful problem to work on.  
[00:05:59] Then you need to collect data, figure out a strategy to analyze  
[00:06:03] the data, and make a hypothesis. At this point, you need to propose a  
[00:06:07] good hypothesis, and then you need to validate. Then you need to write things up and explain.  
[00:06:11] There are a dozen different components. The ones we celebrate are these eureka  
[00:06:17] genius moments of idea generation. Kepler certainly had to cycle through  
[00:06:26] many ideas, several of which didn't work. I bet there were many that he didn't even  
[00:06:32] publish at all because they just didn't fit. That's an important part of the process,  
[00:06:37] trying all kinds of random things and seeing if they worked.  
[00:06:41] But as you say, it has to be matched by an equal amount of verification, otherwise it's slop.  
[00:06:50] We celebrate Kepler, but we should also celebrate Brahe for his assiduous data  
[00:06:55] collection, which was ten times more precise than any previous observation.  
[00:07:00] That extra decimal point of accuracy was essential for Kepler to get his results.  
[00:07:09] He was using Euclidean geometry and the most advanced mathematics he could use at  
[00:07:15] the time to match his models with the data. All aspects had to be in play: the data,  
[00:07:22] the theory, and the hypothesis generation. I'm not sure nowadays that hypothesis  
[00:07:29] generation is the bottleneck anymore. Science has changed in the century since.  
[00:07:38] Classically, the two big paradigms for science were theory and experiment.  
[00:07:44] Then in the 20th century, numerical simulation came along, so you can do  
[00:07:49] computer simulations to test theories. Finally, in the late 20th century,  
[00:07:54] we had big data. We had the era of data analysis.  
[00:07:59] A lot of new progress is actually driven now by analyzing massive datasets first.  
[00:08:03] You collect large datasets and then draw patterns from them to deduce thoughts.  
[00:08:09] This is a little bit different from how science used to work, where you make a  
[00:08:12] few observations or have one out-of-the-blue idea, and then collect data to test your idea.  
[00:08:17] That's the classic scientific method. Now it's almost reversed. You collect big data first,  
[00:08:21] and then you try to get hypotheses from it. Kepler was maybe one of the first early  
[00:08:27] data scientists, but even he didn't start with Tycho's dataset and then analyze it.  
[00:08:35] He had some preconceived theories first. It seems like this is less and less the  
[00:08:40] way we make progress, just because the data is so much more massive and useful.  
[00:08:48] Oh, interesting. I feel like the 20th-century science that you're describing actually very  
[00:08:54] well describes what happened with Kepler. He did have these ideas—1595 and '96 is where  
[00:09:01] he comes up with the polygons and then the Platonic objects theory—but they were wrong.  
[00:09:06] Then a few years later, he gets Brahe's data, and it's only after twenty years of trying random  
[00:09:12] things that he gets this empirical regularity. It actually feels a bit closer to Brahe's data  
[00:09:18] being analogous to some massive data bank of simulations, and now that you've got the data,  
[00:09:25] you can keep trying random things. If it wasn't for that, Kepler would be  
[00:09:28] out there just writing books about harmonics and Platonic objects, and there would be  
[00:09:33] nothing to actually verify against. The data was extremely important. The  
[00:09:39] distinction I was trying to make was that traditionally, you make a hypothesis and  
[00:09:44] then you test it against data. But now with machine learning,  
[00:09:50] data analysis, and statistics, you can start with data and through statistics  
[00:09:56] work out laws that were not present before. Kepler's third law is a little bit like this,  
[00:10:03] except that instead of having the thousand data points that Brahe had, Kepler had six data points.  
[00:10:09] For every planet, he knew the length of the orbit and the distance to the Sun.  
[00:10:13] There were five or six data points, and he did what we would now call regression.  
[00:10:19] He fit a curve to these six data points and got a square-cube law, which was amazing.  
[00:10:24] But he was quite lucky that these six data points gave him the right conclusion.  
[00:10:30] That's not enough data to be really reliable. There was a later astronomer, Johann Bode,  
[00:10:37] who took the same data—the distances to the planets—and inspired by Kepler,  
[00:10:43] he had a prediction that the distances to the planets formed a shifted geometric progression.  
[00:10:48] He also fit a curve, except there was one point missing.  
[00:10:52] There was a big gap between Mars and Jupiter. His law predicted that there was a missing planet.  
[00:10:57] It was kind of a crank theory, except when Uranus was discovered by Herschel,  
[00:11:02] the distance to Uranus fit exactly this pattern. Then Ceres was discovered in the asteroid belt,  
[00:11:11] and it also fit the pattern. People got really excited that Bode had  
[00:11:14] discovered this amazing new law of nature. But then Neptune was discovered,  
[00:11:20] and it was way off. Basically it was just a numerical fluke.  
[00:11:26] There were six data points. Maybe one reason why Kepler didn't highlight his third law as  
[00:11:34] much as the first two laws is that instinctively, even though he didn't have modern statistics,  
[00:11:38] he kind of knew that with six data points, he had to be somewhat tentative with the conclusions.  
[00:11:45] To ask the question about the analogy more explicitly, does this analogy make sense if  
[00:11:53] in the future we have smarter and smarter AIs? We'll have millions of them, and they can go out  
[00:11:58] and hunt for all these empirical irregularities. It sounds like you don't think the bottleneck  
[00:12:02] in science is finding more things that are the equivalent of the third law of  
[00:12:08] planetary motion for each given field, so that later on somebody can say, "Oh,  
[00:12:11] we need a way to explain this. Let's work out the math. Here's the inverse-square law of gravity."  
[00:12:18] I think AI has driven the cost of idea generation down to almost zero,  
[00:12:23] in a very similar way to how the internet drove the cost of communication down to almost zero.  
[00:12:27] It’s an amazing thing, but it doesn't create abundance by itself. Now the bottleneck is  
[00:12:35] different. We're now in a situation where suddenly people can generate thousands of  
[00:12:39] theories for a given scientific problem. Now we have to verify them, evaluate them.  
[00:12:46] This is something which we have to change our structures of science to actually sort this  
[00:12:51] out. Traditionally, we build walls. In the past, before we had AI slop, we had amateur scientists  
[00:13:00] have their own theories of the universe, many of which were of very little value.  
[00:13:07] We built these peer review publication systems to filter out and try to isolate  
[00:13:13] the high signal ideas to test. But now that we can generate these  
[00:13:21] possible explanations at massive scale, and some of them are good and a lot are terrible,  
[00:13:27] human reviewers are already being overwhelmed. Many journals are reporting that AI-generated  
[00:13:34] submissions are just flooding their submissions. It's great that we can generate all kinds of  
[00:13:40] things now with AI, but it means that the rest of the aspects of science have to catch up:  
[00:13:46] verification, validation, and assessing what ideas actually move the subject forward  
[00:13:53] and which ones are dead ends or red herrings. That's not something we know how to do at scale.  
[00:14:02] For each individual paper, we can have a debate among scientists  
[00:14:06] and get to a consensus in a few years. But when we're generating a thousand of  
[00:14:10] these every day, this doesn't work. There's this incredibly interesting  
[00:14:15] question. If you have billions of AI scientists, not only how do you gauge  
[00:14:19] which ones are real progress, but how do you... This is actually a question that human science  
[00:14:23] has had to face and we've solved somehow, and I’m actually not sure how we solved this.  
[00:14:29] Let's say in the 1940s, if you're at Bell Labs and there are these new technologies coming out.  
[00:14:37] Pulse-code modulation, how do you transfer signals? How do you digitize signals?  
[00:14:41] How do you transfer them over analog wires? There are all these papers about the engineering  
[00:14:45] constraints and the details, and then there's one which comes up with the idea of the bit, which has  
[00:14:50] implications across many different fields. You need some system which can then look  
[00:14:54] at that and say, "Okay, we need to apply this to probability.  
[00:14:56] We need to apply this to computer science," et cetera.  
[00:15:00] In the future, the AIs are coming up with the next version of this unifying concept.  
[00:15:06] How would you identify it among millions of papers that might actually constitute progress, but which  
[00:15:10] have much less in terms of general unifying ideas? A lot of it's the test of time.  
[00:15:16] Many great ideas didn't actually get a great reception at the time they were first proposed.  
[00:15:21] It was only after some other scientists realized that they could take it further  
[00:15:25] and apply them to their own... Deep learning itself was a  
[00:15:29] niche area of AI for a long time. The idea of getting answers entirely  
[00:15:34] through training on data and not through first principles reasoning was very controversial,  
[00:15:39] and it just took a long time before it started bearing fruit. You mentioned the bit. There were  
[00:15:46] other proposals for computer architectures than the zero-one that is universal today.  
[00:15:50] I think there were trits, three-valued logic. In an alternate universe,  
[00:15:56] maybe a different paradigm would have shown up. The transformer, for example, is the foundation of  
[00:16:03] all modern large language models, and it was the first deep learning architecture that really was  
[00:16:09] sophisticated enough to capture language. But it didn't have to be that way.  
[00:16:13] There could've been some other architecture that was the first to do it and once that was adopted,  
[00:16:20] it would become the standard. One reason why it's hard to  
[00:16:25] assess whether a given idea is going to be fruitful is that it depends on the future.  
[00:16:29] It depends also on the culture and society, which ones get adopted, which ones don't.  
[00:16:38] The base ten numeral system in mathematics is extremely useful, much better than  
[00:16:42] the Roman numeral system, for instance. But again, there's nothing special about ten.  
[00:16:48] It's a system that is useful for us because everyone else uses it. We've  
[00:16:52] standardized it. We've built all our computers and our number representation  
[00:16:57] systems around it, so we're stuck with it now. Some people occasionally push for other systems  
[00:17:02] than decimal, but there's just too much inertia. It's not something where you can look at any given  
[00:17:12] scientific achievement purely in isolation and give it an objective grade without being aware  
[00:17:19] of the context both in the past and the future. So it may never be something that you can  
[00:17:25] just reinforcement learn the same way that you can for much more localized problems.  
[00:17:33] Often in the history of science when a new theory comes up that in retrospect we realize is correct,  
[00:17:39] it seems to make implications that either make no sense because they're wrong, and we  
[00:17:45] realize later on why they're wrong, or they're correct but seem wildly implausible at the time.  
[00:17:50] As you talked about, Aristarchus had heliocentrism in the third century BC.  
[00:17:58] The ancient Athenians were like, "This can't be because if the earth is going around the sun,  
[00:18:03] we should see the relative position of the stars change as we're going around the sun, and the only  
[00:18:08] way that wouldn't be the case is if they're so far away that you don't notice any parallax,"  
[00:18:13] which is actually the correct implication. But there's times when the implication is  
[00:18:16] incorrect and we just need to graduate to a better level of understanding.  
[00:18:19] Leibniz would chide Newton and disagree with Newton's theory of gravity on the basis that  
[00:18:25] it implied action at a distance, and they didn't know the mechanism, and Newton himself  
[00:18:31] was sort of stunned that inertial mass and gravitational mass were the same quantity.  
[00:18:34] All these things later were resolved by Einstein. But it was still progress. So  
[00:18:39] the question for a system of peer review for AI would be: even if you can falsify a theory,  
[00:18:45] how would you notice that it still constitutes progress relative to the thing before?  
[00:18:49] Often, the ultimately correct theory initially is worse in many ways.  
[00:18:54] Copernicus's theory of the planets was less accurate than Ptolemy's theory.  
[00:19:00] Geocentrism had been developed for a millennium by that point, and they had  
[00:19:06] made many tweaks and increasingly complicated ad hoc fixes to make it more and more accurate.  
[00:19:13] Copernicus's theory was a lot simpler but much less accurate.  
[00:19:16] It was only Kepler that made it more accurate than Ptolemy's theory.  
[00:19:21] Science is always a work in progress. When you only get part of the solution,  
[00:19:27] it looks worse than a theory which is incorrect but somehow has been completed to the point  
[00:19:34] where it kind of answers all the questions. As you say, Newton's theory had big mysteries.  
[00:19:42] They had the equivalence of mass and action at a distance, which  
[00:19:45] were only resolved with a very conceptually different approach centuries afterwards.  
[00:19:54] Often progress has to be made not by adding more theories, but by deleting  
[00:19:59] some assumptions that you have in your mind. One reason why geocentrism held on for so long  
[00:20:06] is we had this idea that objects naturally want to stay at rest.  
[00:20:10] This is the Aristotelian notion of physics, and so the idea that the Earth was moving…  
[00:20:14] How come we weren't all falling over? Once you have Newton's laws of motion—an  
[00:20:19] object in motion remains in motion and so forth—then it makes sense.  
[00:20:25] Conceptually, it's a very big leap to realize that the Earth is in motion.  
[00:20:30] It doesn't feel like it's in motion. The biggest advances, like Darwin's  
[00:20:37] theory of evolution, is the idea that species are not static.  
[00:20:42] This is not obvious because you don't see evolution in your lifetime.  
[00:20:47] Well, now we actually can, but it seems permanent and static.  
[00:20:57] Right now we're going through a cognitive version of the Copernican revolution, where we used to  
[00:21:03] think that human intelligence is the center of the universe, and now we're seeing that there are  
[00:21:07] very different types of intelligence out there with very different strengths and weaknesses.  
[00:21:14] Our assessment of which tasks require intelligence, which ones don't,  
[00:21:18] has to be reordered quite a bit. Trying to fit AI into our theories  
[00:21:25] of scientific progress and what is hard and what is easy, we're struggling quite a lot.  
[00:21:30] We have to ask questions that we've never really had to ask before.  
[00:21:32] Or maybe the philosophers had, but now we all have to deal with it.  
[00:21:35] This brings up a topic I've been very curious about.  
[00:21:39] You mentioned Darwin's theory of evolution. There's this book, The Clockwork Universe  
[00:21:43] by Edward Dolnick, which covers a lot of this era of history we're talking about.  
[00:21:47] He has this interesting observation in there. The Origin of Species was published in 1859.  
[00:21:52] Principia Mathematica was published in 1687. So The Origin of Species comes out two centuries  
[00:21:57] after Principia. Conceptually,  
[00:21:59] it seems like Darwin's theory is simpler. There's a contemporaneous biologist to Darwin,  
[00:22:04] Thomas Huxley, who reads The Origin of Species and he says, "How stupid not to have thought of that."  
[00:22:09] Nobody ever says that about Principia, chiding themselves  
[00:22:12] for not having beaten Newton to gravity. So there's a question of why did it take longer?  
[00:22:17] It seems like a big part of the reason is what you were saying.  
[00:22:20] The evidence for natural selection is overwhelming in a certain sense, but it's cumulative and  
[00:22:23] retrospective, whereas Newton can just say, "Here are my equations.  
[00:22:27] Let me see the moon's orbital period and its distance,  
[00:22:31] and if it lines up, then we've made progress." Lucretius actually had this idea that species  
[00:22:37] adapted to their environment in the first century BC but nobody really talks about it  
[00:22:42] until Darwin because Lucretius couldn't run some experiment and force people to pay attention.  
[00:22:48] I wonder if we'll in retrospect end up seeing much more progress in domains which have this  
[00:22:54] kind of tight data loop where you can verify them quite easily, even though  
[00:23:00] they're conceptually much more difficult. I think one aspect of science is that it's not  
[00:23:04] just creating a new theory and validating it, but communicating it to others.  
[00:23:09] Darwin was an amazing science communicator. He wrote in English, in natural language. I'm  
[00:23:15] speaking like a— No Lean.  
[00:23:22] I have to get out of my technical mindset. He spoke in plain English, didn't use equations,  
[00:23:30] and he synthesized a lot of disparate facts. Little pieces of evolution had been worked out in  
[00:23:36] the past, but he had this very compelling vision. Again, he was still missing things.  
[00:23:42] He didn't know the mechanism for heredity, he didn't have DNA.  
[00:23:49] But his writing style was persuasive, and that helped a lot. Newton wrote in Latin.  
[00:23:57] He had invented entire new areas of mathematics just to explain what he was doing.  
[00:24:02] He was also from an era where scientists were much more secretive and competitive.  
[00:24:07] Academia is still competitive, but it was even worse back in Newton's day.  
[00:24:11] He held back some of his best insights because he didn't want his rivals to get any advantage.  
[00:24:17] He was also a somewhat unpleasant person from what I gather.  
[00:24:23] It was only a couple of decades after Newton when other scientists explained his work in  
[00:24:28] much simpler terms that they became widespread. The art of exposition and making a case and  
[00:24:39] creating a narrative is also a very important part of science.  
[00:24:45] If you have the data, it helps, but people need to be convinced, otherwise they will not push  
[00:24:50] it further or take the initial investment to learn your theory and really explore it.  
[00:24:58] That's another thing which is really hard to reinforcement learn on.  
[00:25:01] How can you score how persuasive you are? Well, there are entire marketing  
[00:25:05] departments trying to do this. Maybe it's good that AI is not  
[00:25:08] yet optimized to be persuasive. There's a social aspect to science.  
[00:25:19] Even though we pride ourselves on having an objective side to it, where there's data and  
[00:25:23] experiment and validation, we still have to tell stories and convince our fellow  
[00:25:28] scientists. That's a soft, squishy thing. It's a combination of data and painting a narrative,  
[00:25:41] and it's a narrative of gaps. Even with Darwin, as I said, there  
[00:25:46] were pieces of his theory he could not explain. But he could still make a case that in the future,  
[00:25:51] people would find transitional forms, that they would find the  
[00:25:54] mechanism of inheritance, and they did. I don't know how you can quantify that  
[00:26:01] in such a precise way that you can start doing reinforcement learning.  
[00:26:06] Maybe that will be forever the human side of science.  
[00:26:10] One takeaway I had from reading and watching your stuff on the cosmic distance ladder… By the way,  
[00:26:16] I highly recommend people watch your series with 3Blue1Brown on the cosmic distance ladder.  
[00:26:22] One takeaway was that the deductive overhang in many fields could be  
[00:26:30] so much bigger than people realize. If you just had the right insight about  
[00:26:33] how to study a problem, you might be surprised at how much more you could learn about the world.  
[00:26:38] I wonder if you think that's a product of astronomy at the particular times  
[00:26:43] in history that you're studying. Or is it just that based on the data  
[00:26:46] that is incident on the Earth right now, we could actually divine a lot more than we happen to know?  
[00:26:52] Astronomy was one of the first sciences to really embrace data analysis and squeezing  
[00:26:59] every last possible drop of information out of the information they had because data was  
[00:27:04] the bottleneck. It still is the bottleneck. It's really hard to collect astronomical data.  
[00:27:10] Astronomers are world-class in extracting all kinds of conclusions  
[00:27:20] from little traces of data, almost like Sherlock. I hear that for a lot of quant hedge funds, their  
[00:27:26] preferred hire is an astronomy PhD, actually. They are also very interested for other reasons  
[00:27:31] in extracting signals from various random bits of data.  
[00:27:35] Okay, speaking of clever ideas, one of my listeners, Shawn,  
[00:27:39] solved the puzzle that Jane Street made for my audience and posted a great walkthrough on X.  
[00:27:44] For context, Jane Street trained a ResNet, shuffled all 96 layers, and then challenged  
[00:27:50] people to put them back in the right order using only the model's outputs and training data.  
[00:27:54] You can't brute force this – there's more possible orderings than atoms in the universe.  
[00:27:58] So Shawn broke the problem into two different parts.  
[00:28:01] First, pair the layers into 48 different blocks. And second, put those blocks in the right order.  
[00:28:06] For pairing, Shawn realized that in a well-trained ResNet, the product of  
[00:28:11] two weight matrices in a residual block should have a distinctive negative diagonal pattern.  
[00:28:16] This arises as a way for the model to keep the residual stream from growing out of control.  
[00:28:20] From this insight, he was able to recover the right pairings.  
[00:28:23] For ordering, Shawn noticed that the model seemed to improve if he sorted the blocks by  
[00:28:28] the size of their residual contributions. Starting with that rough approximation,  
[00:28:31] he combined a clever ranking heuristic with local swaps to recover the exact right order.  
[00:28:36] His full walkthrough is linked in the description.  
[00:28:39] Don't worry if you didn't get to this puzzle in time, though.  
[00:28:40] There's still one up about backdoored LLMs that even Jane Street doesn't know how to solve.  
[00:28:44] You can find it at janestreet.com/dwarkesh. Alright, back to Terence!  
[00:28:51] We do under-explore how to extract extra information from various signals.  
[00:29:00] Just to pick one random study, I remember reading once that people were trying to measure how often  
[00:29:06] scientists actually read the papers that they cite. How do you measure  
[00:29:12] this? You could try to survey different scientists, but they had a clever trick.  
[00:29:21] Many citations have little typos, like a number is wrong or punctuation is almost wrong.  
[00:29:28] They measured how often a typo got copied from one reference to the next, and they  
[00:29:33] could infer whether an author was just copying and pasting a reference without actually checking it.  
[00:29:40] From that, they were able to infer some measure of how much attention people were paying.  
[00:29:46] So there are some clever tricks to extract… These questions you posed earlier of how  
[00:29:54] we can assess whether a scientific development is fruitful, interesting, or represents real  
[00:30:00] progress… Maybe there are really useful metrics or footprints of this phenomenon in data.  
[00:30:12] We can examine citations and how often something is mentioned in a conference.  
[00:30:17] Maybe there's a lot of sociology of science research to be done that could actually  
[00:30:25] detect these things. Maybe we should get  
[00:30:27] some astronomers on the case, actually. That brings us nicely to the progress that, from  
[00:30:36] the outside, it seems like AI for math is making. You had a post recently where you pointed out  
[00:30:41] that over the last few months, AI programs have solved fifty  
[00:30:44] out of the eleven hundred odd Erdős problems. I don’t know if it’s still correct, but as of  
[00:30:50] a month ago you said that there had been a pause because the low-hanging fruit had been picked.  
[00:30:55] First of all, I'm curious if that is still the case, that we have picked the low-hanging fruit  
[00:30:59] and now we're at this plateau currently. It does seem so. Fifty-odd problems have  
[00:31:07] been solved with AI assistance, which is great, but there's like six hundred to go.  
[00:31:12] People are still chipping away at one or two of these right now.  
[00:31:17] We're seeing a lot fewer pure AI solutions now where the AI just one-shots the problem.  
[00:31:24] There was a month where that happened and that has stopped, not for lack of trying.  
[00:31:28] I know of three separate attempts to get frontier model AIs to just attack every  
[00:31:33] single one of the problems simultaneously. They pick out some minor observations,  
[00:31:38] or maybe they find that some problem was already solved in the literature, but there hasn't been  
[00:31:43] any further purely AI-powered solution yet. People are using AI a lot currently.  
[00:31:50] Someone might use AI to generate a possible proof strategy, and then another person will  
[00:31:55] use a separate AI tool to critique it, rewrite it, generate some numerical data for it,  
[00:32:01] or do a literature survey. Some problems have been solved  
[00:32:06] by an ongoing conversation between lots of humans and lots of AI tools.  
[00:32:11] But it does seem like it was this one-off thing. Maybe one analogy for these problems is  
[00:32:22] that you're in some sort of mountain range with all kinds of cliffs and walls.  
[00:32:27] Maybe there's a little wall which is three feet high, and one that's six feet high,  
[00:32:33] and then there's fifteen feet high, and then there are some mile-high cliffs.  
[00:32:39] You're trying to climb as many of these cliffs as possible, but it's in the dark.  
[00:32:43] We don't know which ones are tall, which ones are short.  
[00:32:46] So we try to light some candles and make some maps, and slowly we  
[00:32:50] figure out some of them are climbable. Some of them we can identify a partial  
[00:32:56] track in the wall that you can reach first. These AI tools, they're like jumping  
[00:33:02] machines that can jump two meters in the air, higher than any human.  
[00:33:06] Sometimes they jump in the wrong direction, and sometimes they crash,  
[00:33:09] but sometimes they can reach the tops of the lowest walls that we couldn't reach before.  
[00:33:18] We've just set them loose in this mountain range, hopping around.  
[00:33:23] There was this exciting period where they could actually find all the low ones and reach them.  
[00:33:32] Maybe the next time there's a big advance in the models, they will  
[00:33:36] try it again, and a few more will be breached. But it's a different style of doing mathematics.  
[00:33:48] Normally we would hill climb, make little markers, and try to identify partial things.  
[00:33:56] These tools either succeed or they fail. They've been really bad at creating partial  
[00:34:02] progress or identifying intermediate stages that you should focus on first.  
[00:34:09] Going back to this previous discussion, we don't have a way of evaluating partial progress  
[00:34:14] the same way we can evaluate a one-shot success or failure of solving a problem.  
[00:34:19] There's two different ways to think through what you've just said.  
[00:34:23] One of them is more bearish on AI progress, and one of them is more bullish.  
[00:34:26] The bearish one being, "Oh, they're only getting to a certain height of wall,  
[00:34:29] which is not as high as humans are reaching." The second is that they have this powerful  
[00:34:36] property that once they achieve a certain waterline, they can fill every single problem  
[00:34:41] that is available at that waterline, which we simply can't do with humans.  
[00:34:45] We can't make a million copies of you and give each of them a million dollars  
[00:34:49] of inference compute and have you do a hundred years of subjective time research on a million  
[00:34:57] different problems at the same time. But once AIs reach Terence Tao-level,  
[00:35:00] they could do that. Once they reach intermediate levels,  
[00:35:03] they could do the intermediate version of that. The same reason that we should be bearish now is  
[00:35:09] the reason we should be especially bullish. Not even when they achieve superhuman  
[00:35:12] intelligence, but just when they achieve human-level intelligence,  
[00:35:15] because their human-level intelligence is qualitatively wider and more powerful  
[00:35:19] than our human-level intelligence. I agree. They excel at breadth,  
[00:35:24] and humans excel at depth, human experts at least. I think they're very complementary.  
[00:35:30] But our current way of doing math and science is focused on depth because that's where human  
[00:35:37] expertise is, because humans can't do breadth. We have to redesign the way we do science to take  
[00:35:45] full advantage of this breadth capability that we now have.  
[00:35:51] We should have a lot more effort in creating very broad classes of problems to work on rather  
[00:35:55] than one or two really deep, important problems. We should still have the deep, important problems,  
[00:36:01] and humans should still be working on them. But now we have this other way of doing science.  
[00:36:10] We can explore entirely new fields of science by first getting these broad,  
[00:36:16] moderately competent AIs to map it out and make all the easy observations.  
[00:36:21] And then identify certain islands of difficulty, which human experts can then come and work on.  
[00:36:29] I see very much a future of very complementary science.  
[00:36:34] Eventually, you would hope to get both breadth and depth and somehow get the best of both worlds.  
[00:36:41] But we need practice with the breadth side. It's too new. We don't even have the paradigms  
[00:36:48] to really take full advantage of it. But we will, and then science will be  
[00:36:54] unrecognizable after that, I think. To this point about complementarity,  
[00:37:00] programmers have noticed that they're way more productive as a result of these AI tools.  
[00:37:05] I don't know if you as a mathematician feel the same way, but it does seem  
[00:37:09] like one big difference between vibe coding and vibe researching is that with software,  
[00:37:16] the whole point is to have some effect on the world through your work.  
[00:37:21] If it leads to you better understanding a problem or coming up with some clean  
[00:37:25] abstraction to embody in your code, that is instrumental to the end goal.  
[00:37:29] Whereas with research, the reason we care about solving the Millennium Prize Problems  
[00:37:34] is that presumably that in the process of solving them, we discover new mathematical  
[00:37:39] objects or new techniques that advance our civilization's understanding of mathematics.  
[00:37:45] So the proof is instrumental to the intermediate work.  
[00:37:50] I don't know if you agree with that dichotomy or if that in any way will explain the relative  
[00:37:57] uplift we'll see in software versus research. Certainly in math, the process is often more  
[00:38:03] important than the problem itself. The problem is kind of a proxy  
[00:38:06] for measuring progress. I think even in software,  
[00:38:09] there are different types of software tasks. If you just create a webpage that does the same  
[00:38:15] thing that a thousand other webpages do, there's no skill to be learned.  
[00:38:19] Well, there is still some skill maybe that the individual programmer could pick up.  
[00:38:24] But for boilerplate-type code, it's something that you should definitely offload to AI.  
[00:38:35] Sometimes once you make the code, you still have to maintain it.  
[00:38:39] There are issues with upgrading it and making it compatible with other things.  
[00:38:44] I've heard programmers report that even if an AI can create the first prototype  
[00:38:50] of a tool, making it mesh with everything else and making it interact with the real  
[00:38:55] world in the way they want is an ongoing process. If you don't have the skills that you pick up from  
[00:39:03] writing the code, that may impact your ability to maintain it down the road.  
[00:39:10] So yes, certainly mathematicians, we've used problems to build intuition and to train people  
[00:39:19] to have a good idea of what's true, what to expect, what is provable, and what is difficult.  
[00:39:26] Just getting the answers right away may actually inhibit that process.  
[00:39:35] I made a distinction between theory and experiment before.  
[00:39:39] In most sciences, there's an equal division between the theoretical side  
[00:39:42] and the experimental side. Math has been unique in  
[00:39:46] that it's almost entirely theoretical. We place a premium on trying to have coherent,  
[00:39:53] clean theories of why things are true and false. We haven't done many experiments as to,  
[00:39:59] if we have two different ways to solve a problem, which is more effective.  
[00:40:04] We have some intuition, but we haven't done large-scale studies where we take a thousand  
[00:40:07] problems and just test them. But we can do that now.  
[00:40:13] I think AI-type tools will actually revolutionize the experimental side of math,  
[00:40:19] where you don't care so much about individual problems and the process of solving them,  
[00:40:24] but you want to gather large-scale data about what things work and what things don't.  
[00:40:30] The same way that if you're a software company and you want to roll out a thousand  
[00:40:36] pieces of software, you don't really want to handcraft each one and learn lessons from each.  
[00:40:39] You just want to find what workflows let you scale.  
[00:40:46] The idea of doing mathematics at scale is at its infancy.  
[00:40:49] But that's where AI is really going to revolutionize the subject.  
[00:40:53] I feel like a big crux in these conversations about how good AI will be for science is,  
[00:40:58] I think you said this, that they're using existing techniques and modifying them.  
[00:41:06] It would be interesting to understand how much progress one  
[00:41:09] can make simply from using existing techniques. If I looked at the top math journals, how many of  
[00:41:15] the papers are coming up with a new technique, whatever that means, versus using existing  
[00:41:21] techniques on new problems? What is the overhang? If you just applied every known technique to every  
[00:41:27] open problem, would that constitute a humongous uplift in our civilization's knowledge, or would  
[00:41:32] that not be that impressive and useful? This is a great question, and we don't  
[00:41:38] have the data to fully answer it yet. Certainly, a lot of work that human  
[00:41:44] mathematicians do… When you take a new problem, one of the first things we do is we look at all  
[00:41:50] the standard things that have worked on similar problems in the past, and we try them one by one.  
[00:41:54] Sometimes that works, and that's still worth publishing because the question was important.  
[00:41:59] Sometimes they almost work, and you have to add one more  
[00:42:01] wrinkle to it, and that's also interesting. But the papers that go into the top journals  
[00:42:08] are usually ones where the existing methods can kind of solve 80% of the problem, but then  
[00:42:14] there is this 20% which is resistant and a new technique has to be invented to fill in the gaps.  
[00:42:21] It's very rare now that a problem gets solved with no reliance on past literature,  
[00:42:26] where all the ideas come out of nowhere. That was more common in the past,  
[00:42:32] but math is so mature now that it's just so much of a handicap to not use the literature first.  
[00:42:44] AI tools are getting really good at the first part of that, just trying all the  
[00:42:49] standard techniques on a problem, often making fewer mistakes in applying them than humans.  
[00:42:55] They still make mistakes, but I've tested these tools on little tasks that I can do,  
[00:43:04] and sometimes they pick up errors that I make. Sometimes I pick up errors that they make.  
[00:43:07] It's about a tie right now. But I haven't yet seen them take the next step.  
[00:43:17] When there are holes in the argument where none of the things are working, then what do you do?  
[00:43:25] They can suggest random things, but often I find that trying to chase them down to  
[00:43:31] make them work, and finding they don't work, wastes more time than it saves.  
[00:43:38] I think some fraction of problems that we currently think are hard will fall  
[00:43:42] from this method, especially the ones that haven't received enough attention.  
[00:43:48] With the Erdős problems, almost all of the 50 problems that were solved by AIs were ones for  
[00:43:53] which there was basically no literature. Erdős posed the problem once or twice.  
[00:43:59] Maybe some people tried it casually and couldn't do it, but they never wrote up anything.  
[00:44:03] But it turned out that there was a solution, and it was just combining this one obscure  
[00:44:08] technique that not many people know about with some other result in the literature.  
[00:44:12] That's the median level of what AI can accomplish, and that's really great.  
[00:44:17] It clears out 50 of these problems. So I think you will see some isolated successes.  
[00:44:24] But what we found… Some people have done large-scale sweeps of these Erdős problems.  
[00:44:29] If you only focus on the success stories, the ones that get broadcast  
[00:44:32] on social media, it looks amazing. All these problems that haven't been  
[00:44:35] solved for decades, now they're falling. But whenever we do a systematic study,  
[00:44:40] on any given problem an AI tool has a success rate of maybe 1% or 2%.  
[00:44:46] It's just that they can buy scale, and you just pick the winners. It looks great. I  
[00:44:50] think there'll be a similar thing happening with the hundreds of really prestigious,  
[00:44:57] difficult math problems out there. Some AI may get lucky and actually solve them,  
[00:45:03] and there will be some backdoor to solve the problem that everyone else missed.  
[00:45:08] That will get a lot of publicity. But then people will try these fancy  
[00:45:12] tools on their own favorite problem, and they will again experience the 1% to 2% success rate.  
[00:45:18] There'll be a lot of noise amongst the signal of when they're working and when they're not.  
[00:45:28] It will be increasingly important to collect these really standardized datasets.  
[00:45:32] There are efforts now to create a standard set of challenge problems for AIs to solve, and not just  
[00:45:38] rely on the AI companies to only publish their wins and not disclose their negative results.  
[00:45:44] That will maybe give more clarity as to where we're actually at.  
[00:45:48] Although I think it's worth emphasizing how much progress in AI it constitutes already,  
[00:45:52] to have models that are capable of applying some technique that nobody had written down  
[00:45:58] as applicable to this particular problem. The progress is simultaneously amazing  
[00:46:02] and disappointing. It is a very strange  
[00:46:05] feeling to see these tools in action. But people also acclimatize really quickly.  
[00:46:12] I remember when Google's web search came out 20 years ago.  
[00:46:16] It just blew all the other searches out of the water.  
[00:46:18] You're getting relevant hits on the front page, exactly what you wanted.  
[00:46:23] It was amazing, and then after a few years, you just took for  
[00:46:26] granted that you could Google anything. 2026-level AI would be stunning in 2021.  
[00:46:35] A lot of it—face recognition, natural speech, doing college-level math problems—we just  
[00:46:42] take for granted now. Speaking of 2026 AI,  
[00:46:45] you made a prediction in 2023 that by 2026 it would be like a colleague in mathematics?  
[00:46:53] A trustworthy co-author if used correctly. Which is looking pretty good in retrospect.  
[00:46:57] Yeah, I'm pretty pleased. So let's see if you can continue this streak.  
[00:47:04] You personally are 2x more productive as a result of AI.  
[00:47:08] What year would you say that? Productivity, I think,  
[00:47:12] is not quite a one-dimensional quantity. I'm definitely noticing that the style  
[00:47:19] in which I do mathematics is changing quite a bit, and the type of things I do.  
[00:47:23] For example, my papers now have a lot more code, a lot more pictures,  
[00:47:29] because it's so easy to generate these things now. Some plot which would have taken me hours to do,  
[00:47:33] now I can do in minutes. But in the past, I just wouldn't have  
[00:47:37] put the plot in my paper in the first place. I would just talk about it in words.  
[00:47:41] So it's hard to measure what 2x means. On the one hand, I think the type of  
[00:47:50] papers that I would write today, if I had to do them without AI assistance,  
[00:47:54] would definitely take five times longer. But I would not write my papers that way.  
[00:47:58] 5x? Yeah, but these are auxiliary tasks.  
[00:48:06] Things like doing a much deeper literature search or supplying a lot more numerics.  
[00:48:14] They enrich the paper. The core of what I do, actually solving the most difficult part of a  
[00:48:24] math problem, hasn't changed too much. I still use pen and paper for that.  
[00:48:28] But there's lots of silly things. I use an AI agent now to reformat.  
[00:48:35] Sometimes if all my parentheses are not quite the right size, I used to manually change them  
[00:48:39] by hand, and now I can get an AI agent to do all that quite nicely in the background.  
[00:48:46] They've really sped up lots of secondary tasks. They haven't yet sped up the core thing that I do,  
[00:48:53] but it's allowed me to add more things to my papers.  
[00:49:00] By the same token, if I were to write a paper I wrote in 2020 again—and not add all these  
[00:49:06] extra features, but just have something of the same level of functionality—it actually  
[00:49:11] hasn't saved that much time, to be honest. It's made the papers richer and broader,  
[00:49:17] but not necessarily deeper. You made this distinction between  
[00:49:22] artificial cleverness and artificial intelligence. I would like to better understand those concepts.  
[00:49:29] What is an example of intelligence that is not just cleverness?  
[00:49:40] Intelligence is famously hard to define.  
[00:49:41] It's one of these things that you know when you see it.  
[00:49:45] But when I talk to someone and we're trying to collaboratively solve a math problem together,  
[00:49:53] there's this conversation where neither of us knows how to solve the problem initially.  
[00:50:00] One of us has some idea and it looks promising, so then we have some sort of prototype strategy.  
[00:50:06] We test it, and it doesn't work, but then we modify it.  
[00:50:10] There's adaptivity and continual improvement of the idea over time.  
[00:50:18] Eventually, we've systematically mapped out what doesn't work and what does work,  
[00:50:23] and we can see a path forward, but it's evolving with our discussion.  
[00:50:30] This isn't quite what the AIs do. The AIs can mimic this a little bit.  
[00:50:37] To go back to this analogy of these jumping robots, they can jump and fail, and jump and fail.  
[00:50:44] But what they can't do is jump a little bit, reach some handhold, stay there, pull other people up,  
[00:50:52] and then try to jump from there. There isn't this cumulative process  
[00:50:58] which is built up interactively. It seems to be a lot more trial and  
[00:51:04] error and just repetition: brute force. It scales, and it can work amazingly  
[00:51:12] well in certain contexts. But this idea of building  
[00:51:17] up cumulatively from partial progress is what's still not quite there yet.  
[00:51:23] Interesting. You're saying if Gemini 3 or Claude 4.5, whatever, solves a problem,  
[00:51:29] it is not the case that its own understanding of math has progressed.  
[00:51:32] No. Or even if it works  
[00:51:33] on a problem without solving it, it's not that its own understanding of math has progressed.  
[00:51:36] Yeah. You run a new session and it's forgotten what it just did.  
[00:51:40] It has no new skills to build on related problems. Maybe what you just did is 0.001% of the  
[00:51:49] training data for the next generation. So maybe eventually some of it gets absorbed.  
[00:51:54] So Terence talks about the importance of decomposing particularly gnarly  
[00:51:58] problems into a series of easier chunks. Even if this doesn't result in the full solution,  
[00:52:03] approaching problems in this way helps you build up the intuitions and practice the techniques  
[00:52:07] that you'll need to keep making progress. But models today tend to struggle with these  
[00:52:11] kinds of problem-solving techniques. That's where Labelbox comes in.  
[00:52:14] Labelbox helps you train models not just to get the right answer, but to think the right way.  
[00:52:19] They've operationalized these reasoning behaviors into rubrics, giving you the ability to evaluate  
[00:52:24] every important dimension of a model's output. These rubrics go beyond simple correctness.  
[00:52:28] Did the model reach for the right tools? Did it check its own work and  
[00:52:31] explore alternative paths? How clear was its response?  
[00:52:35] These skills are useful across domains: math, physics, finance, psychology, and more.  
[00:52:40] And they're becoming increasingly important as models take on harder, open-ended problems,  
[00:52:44] some of which have multiple solutions and some of which we don't even know the solutions to.  
[00:52:48] Labelbox can get you rubrics tailored to your domain, helping you systematically  
[00:52:52] measure and shape how your models think. Learn more at labelbox.com/dwarkesh.  
[00:53:00] One big question I have is how plausible is it that if we just keep training AIs—they get better  
[00:53:06] and better at solving problems in Lean—that they will continue to solve more and more impressive  
[00:53:12] problems, and then we will be surprised at how little insight we got from some Lean solution  
[00:53:18] to proving the Riemann hypothesis or something. Or do you think it is a necessary condition of  
[00:53:22] solving the Riemann hypothesis, even by an AI that is doing it entirely in Lean,  
[00:53:25] that the constructions and definitions created in the Lean program have to  
[00:53:32] advance our understanding of mathematics? Or could it just be assembly code gobbledygook?  
[00:53:40] We don't know. Some problems have been basically solved by pure brute force.  
[00:53:44] The four color theorem is a famous example. We have still not found a conceptually elegant  
[00:53:49] proof of this theorem, and maybe we never will. Some problems may only be solvable by splitting  
[00:53:56] into an enormous number of cases and doing brute force,  
[00:54:00] uninsightful computer analysis on each case. Part of the reason we prize problems like  
[00:54:08] the Riemann hypothesis is that we're pretty sure a new type of mathematics  
[00:54:14] has to be created, or a new connection between two previously unconnected areas of mathematics  
[00:54:18] has to be discovered to make this work. We don't even know what the shape of the solution  
[00:54:24] is, but it doesn't feel like a problem that will be solved just by exhaustively checking cases.  
[00:54:30] Or it could be false actually. Okay, there is an unlikely scenario  
[00:54:37] that the hypothesis is false, and you can just compute a zero off the line,  
[00:54:42] and a massive computer calculation verifies it. That would be very disappointing. I do  
[00:54:51] feel that fully autonomous, one-shot approaches are not the right approach for these problems.  
[00:54:59] You'll get a lot more mileage out of the interplay of humans collaborating with these tools.  
[00:55:08] I can see one of these problems being solved by smart humans  
[00:55:14] assisted by extremely powerful AI tools. But the exact dynamic may be very different  
[00:55:20] from what we envision right now. It could be a collaboration of  
[00:55:24] a type that just doesn't exist yet. There may be a way to generate a million variants  
[00:55:35] of the Riemann zeta function and do AI-assisted data analysis to discover some pattern connecting  
[00:55:41] them that we didn't know about before. This lets you transform the problem  
[00:55:46] into a different area of mathematics. There could be all kinds of scenarios.  
[00:55:51] Suppose the AI figures it out, and latent in the Lean is some brand-new construction which,  
[00:55:59] if we realized its significance, we would be able to apply in all these different situations.  
[00:56:04] How would we even recognize it? Again, a very naive question, but if you come  
[00:56:11] up with the equivalent of Descartes' idea that you can have a coordinate system unifying algebra  
[00:56:17] and geometry, in Lean code it would just look like R→R, and it wouldn't look that significant.  
[00:56:22] I'm sure there are other constructions which have this kind of property.  
[00:56:26] The beauty of formalizing a proof in something like Lean is that you can take  
[00:56:29] any piece of it and study it atomically. When I read a paper which solves some  
[00:56:39] difficult problem, there's often a big sequence of lemmas and theorems.  
[00:56:44] Ideally, the author will talk their way through what's important and what's not.  
[00:56:48] But sometimes they don't reveal what steps were the important ones and which ones  
[00:56:52] were just boilerplate, standard steps. You can study each lemma in isolation.  
[00:56:59] Some of them I can see look fairly standard and resemble something I'm familiar with.  
[00:57:04] I'm pretty sure there's nothing interesting going on there.  
[00:57:06] But this other lemma, that's something I haven't seen before, and I can see why having this result  
[00:57:12] would really help prove the main result. You can assess whether a step is really key  
[00:57:21] to your argument or not, and Lean really facilitates that.  
[00:57:26] The individual steps are identified really precisely.  
[00:57:29] I think in the future, there will be entire professions of mathematicians who might take  
[00:57:35] a giant Lean-generated proof and do some ablation on it, trying to remove parts of  
[00:57:41] it and find more elegant ways. They might get other AIs to do  
[00:57:46] some reinforcement learning to make the proof more elegant, and maybe other AIs will grade  
[00:57:52] whether this proof looks better or not. One thing that will change quite a bit  
[00:57:58] in the near future is how we write papers. Until recently, writing papers was the most  
[00:58:01] time-consuming and expensive part of the job. So you did it very rarely.  
[00:58:07] You only wrote up your results once all the other parts of your argument were checked out, because  
[00:58:14] rewriting and refactoring was just a total pain. That's become a lot easier now  
[00:58:19] with modern AI tools. You don't have to have just  
[00:58:21] one version of your paper. Once you have one,  
[00:58:24] people can generate hundreds more. One giant messy Lean proof may not be very  
[00:58:31] meaningful or understandable on its own, but other people can  
[00:58:35] refactor it and do all kinds of things with it. We've seen this with the Erdős problem website.  
[00:58:42] An AI will generate a proof, and here are 3,000 lines of code that verify the proof.  
[00:58:47] Then people got other AIs to summarize the proof, and people write their own  
[00:58:52] proofs. There's actually post-processing. Once you have one proof, we have a lot of  
[00:59:00] tools now to deconstruct and interpret it. It's a very nascent area of mathematics,  
[00:59:07] but I'm not as worried about it. Some people are concerned about what happens if  
[00:59:12] the Riemann hypothesis is proven with a completely incomprehensible proof.  
[00:59:14] I think once you have the artifact of a proof, we can do a lot of analysis on it.  
[00:59:20] You posted recently that it would be helpful to have a formal or semi-formal  
[00:59:24] language for mathematical strategies as opposed to just mathematical proofs,  
[00:59:28] which is what Lean specializes in. I would love to learn more about  
[00:59:32] what that would involve or look like. We don't really know. We've been very  
[00:59:37] lucky in mathematics that we have worked out the laws of logic and mathematics,  
[00:59:42] but this is a fairly recent accomplishment. It was started by Euclid two millennia ago,  
[00:59:47] but only in the early 20th century did we finally list out the axioms of mathematics,  
[00:59:54] the standard axioms of what we call ZFC, the axioms of first-order logic, and what a proof is.  
[01:00:00] This we've managed to automate and have a formal language for.  
[01:00:05] There could be some way to assess plausibility. You have a conjecture that something is true,  
[01:00:14] you test a few examples, and it works out. How does this increase your  
[01:00:18] confidence that the conjecture is true? We have a few sort of mathematical ways to model  
[01:00:24] this, like Bayesian probability, for example. But you often have to set certain base  
[01:00:32] assumptions, and there's a lot of subjectivity still in these tasks.  
[01:00:44] This is more of a wish than a plan to develop these languages, but just seeing how successful  
[01:00:52] having a formal framework in place, like Lean, has made deductive proofs so much easier to automate  
[01:00:59] and train AI on… The bottleneck for using AI to create strategies and make conjectures is we have  
[01:01:10] to rely on human experts and the test of time to validate whether something is plausible or not.  
[01:01:16] If there was some semi-formal framework where this could be done semi-automatically  
[01:01:22] in a way that isn't easily hackable... It's really important with these formal  
[01:01:32] proof assistants that there are no backdoors or exploits you can use to somehow get your  
[01:01:40] certified proof without actually proving it, because reinforcement learning is  
[01:01:44] just so good at finding these backdoors. If there's some framework that mimics how  
[01:01:56] scientists talk to each other in a semi-formal way, using data and argument,  
[01:02:01] but also constructing narratives... There's some subjective aspect of  
[01:02:08] science that we don't know how to capture in a way that we can insert AI into it in any useful way.  
[01:02:18] This is a future problem. There are research efforts to try to create automated conjectures,  
[01:02:27] and maybe there are ways to benchmark these and simulate this, but it's all very new science.  
[01:02:35] Can you help me get some intuition? I have two sub-questions. One, it would be very helpful  
[01:02:45] to have a specific example of what something like this would look like, the way scientists  
[01:02:56] communicate that we can't formalize yet. Two, it seems almost definitionally paradoxical  
[01:03:02] to say you're building up some narrative or natural language explanation and then also having  
[01:03:10] something which you could have formalized. I'm sure there's some intuition behind  
[01:03:16] where that overlap is, and I'd love to understand that better.  
[01:03:20] An example of a conjecture: Gauss was interested in the prime numbers and  
[01:03:28] created one of the first mathematical datasets. He just computed the first 100,000 prime numbers  
[01:03:31] or so, hoping to find patterns. He did find a pattern,  
[01:03:37] but maybe not the pattern he was expecting. He found a statistical pattern in the primes  
[01:03:41] that if you count how many primes there are up to 100, 1,000, one million, and so forth,  
[01:03:47] they get sparser and sparser, but the drop-off in the density was inversely proportional to  
[01:03:54] the natural logarithm of the range of numbers. So he conjectured what we now call the prime  
[01:03:59] number theorem: the number of primes up to X is X divided by the natural log of X.  
[01:04:05] He had no way to prove this. It was data-driven. This was a conjecture.  
[01:04:12] It was revolutionary for its time because it was maybe the first really important conjecture  
[01:04:19] of math that was statistical in nature. Normally you're talking about a pattern,  
[01:04:23] like maybe the spacing between the primes has a certain regularity.  
[01:04:27] But this didn't tell you exactly how many primes there were in any given range.  
[01:04:32] It just gave you an approximation that got better and better as you went further and further out.  
[01:04:42] It started the field of what we call analytic number theory.  
[01:04:47] It was the first in many conjectures like this, many of which got proved,  
[01:04:51] which started consolidating the idea that the prime numbers didn't really have a pattern,  
[01:04:56] that they behaved like random sets of numbers with a certain density.  
[01:05:03] They had some patterns, like they're almost all odd.  
[01:05:07] They're also not actually random, they're what's called pseudo-random.  
[01:05:10] There's no random number generation involved in creating the prime numbers.  
[01:05:14] But over time, it became more and more productive to think of the primes as  
[01:05:19] if they were just generated by some god rolling dice all the time and creating this random set.  
[01:05:26] This allowed us to make all these other predictions.  
[01:05:28] There's a still-open conjecture in number theory called the twin prime conjecture, that  
[01:05:32] there should be infinitely many pairs of primes that are twins just two apart, like 11 and 13.  
[01:05:37] We can't prove that, and there are good reasons why we can't prove it.  
[01:05:41] But because of this statistical random model of the primes, we are absolutely convinced it's true.  
[01:05:46] We know that if the primes were generated by flipping coins, we would just—by random chance  
[01:05:51] like infinite monkeys at a typewriter—see twin primes appear over and over again.  
[01:05:57] We have over time developed this very accurate conceptual model of what the primes should behave  
[01:06:02] like based on statistics and probability. It's mostly heuristic and non-rigorous,  
[01:06:07] but extremely accurate. The few times when we actually  
[01:06:12] can prove things about the primes, it has matched up with the predictions of what we  
[01:06:16] call the random model of the primes. We have this conjectural concept  
[01:06:21] framework for understanding the primes that everyone believes in.  
[01:06:25] It's the same reason why we believe the Riemann hypothesis is true, and why we  
[01:06:29] believe that cryptography based on the primes is mathematically secure.  
[01:06:35] It's all part of this belief. In fact, one reason why we care  
[01:06:40] about the Riemann hypothesis is that if the Riemann hypothesis failed,  
[01:06:44] if we knew it was false, it would be a serious blow to this model.  
[01:06:49] It would mean there's a secret pattern to the primes that we were not aware of.  
[01:06:54] I think we would very rapidly abandon any cryptography based on the primes,  
[01:06:58] because if there was one pattern that we didn't know about, there are probably more, and these  
[01:07:01] patterns can lead to exploits in crypto. It would be a big shock.  
[01:07:07] So we really want to make sure that doesn't happen.  
[01:07:15] We've been convinced of things like the Riemann hypothesis over time.  
[01:07:20] Some of it is experimental evidence, and some is that the few times we've been able to make  
[01:07:24] theoretical results, they've always aligned. It is possible that the consensus is wrong and  
[01:07:30] we've all just missed something very basic. There have been paradigm shifts in  
[01:07:34] the past in scientific history. But we don't really have a way of  
[01:07:40] measuring this, partly because we don't have enough data on how math or science develops.  
[01:07:46] We have one timeline of history, and we have maybe 100 stories of turning points in history.  
[01:07:53] If we had access to a million alien civilizations, each with a different  
[01:07:58] development of history and science in different orders, then maybe we'd actually have a decent  
[01:08:04] shot at understanding how we measure what progress is and what is a good strategy.  
[01:08:12] We could maybe start formalizing it and actually having a framework.  
[01:08:18] Maybe what we need to do is start creating lots of mini-universes or simulations of AI  
[01:08:24] solving very basic problems in arithmetic or whatever, but coming up with their  
[01:08:30] own strategies for doing these things and having these little laboratories to test.  
[01:08:34] There are people who investigate what's the smallest neural network that can do  
[01:08:39] 10-digit multiplication and things like that. I think we could learn a lot just from evolving  
[01:08:45] small AIs on simple problems. I was super excited when Mercury  
[01:08:50] reached out about sponsoring the podcast because I've been banking with them for years.  
[01:08:54] I think I opened my first account with them in 2023.  
[01:08:56] Something I've come to appreciate over the last few years is that Mercury is constantly  
[01:08:59] updating things and adding new features. Take their newest feature, Insights.  
[01:09:03] Insights summarizes your money in and out, showing you your biggest transactions and calling  
[01:09:07] out anything that deserves extra attention. Like maybe your revenue from a particular partner  
[01:09:11] has gone down, or you've got a big uncategorized purchase that needs to be investigated.  
[01:09:15] It's a super low-friction way for me to keep tabs on my business and make quick decisions.  
[01:09:19] For example, I try to invest any cash that I don't need on hand to keep running the business.  
[01:09:23] With Insights, with just a couple of clicks, I was able to see exactly how much money I  
[01:09:26] spent in each month of 2025 and that lets me know exactly how much cash I'll need for  
[01:09:31] the next year or so of operations. And then I can go invest the rest.  
[01:09:35] Mercury just keeps adding new features like this. Go to mercury.com to check it out.  
[01:09:39] Mercury is a fintech company, not an FDIC Insured Bank.  
[01:09:42] Banking services provided through Choice Financial Group and Column NA, members FDIC.  
[01:09:48] You have to learn about new fields not only very rapidly, but deeply enough  
[01:09:53] to contribute to the frontier. So in some sense, you're also  
[01:09:57] one of the world's greatest autodidacts. What is your process of learning about a new  
[01:10:04] subfield in math? What does that look like? We talked about depth and breadth before.  
[01:10:12] It's not a purely human-AI distinction. Humans also, I think it was Berlin who  
[01:10:19] split them into hedgehogs and foxes. The hedgehog knows one thing very well,  
[01:10:23] and a fox knows a little bit about everything. I definitely think of myself as a fox.  
[01:10:32] I work with hedgehogs a lot, and sometimes I can be a hedgehog if need be.  
[01:10:40] I've always had a little bit of an obsessive streak.  
[01:10:43] If there's something I read about which I feel like I have the capability to understand,  
[01:10:48] but I don't understand why it works and there's some magic in it… Someone was able  
[01:10:53] to use a type of mathematics I'm not familiar with and get a result I would like to prove.  
[01:10:58] I can't do it myself, but they could do it by their method,  
[01:11:01] and I want to find out what their trick was. It bugs me that someone else can do something  
[01:11:06] I think I can do, but I can't. I've always had that obsessive,  
[01:11:10] completionist streak. I've had to wean myself off  
[01:11:14] computer games because if I start a game, I want to play it to completion, through all the levels.  
[01:11:23] That's one way I learn new fields. I collaborate with a lot of people  
[01:11:29] who have taught me other types of mathematics. I just make friends with another mathematician  
[01:11:35] working on another area of mathematics. I find their problems interesting,  
[01:11:38] but they have to teach me some of the basic tricks, what's known, and what's not known.  
[01:11:44] I learn a lot from that. I found that writing about  
[01:11:49] what I've learned helps. I have a blog where I sometimes  
[01:11:54] record things I've learned. In the past when I was younger,  
[01:11:58] I would learn something, do this cool trick, and say, "Okay, I'm going to remember this."  
[01:12:02] Then six months later, I'd forgotten it. I remember remembering it,  
[01:12:07] but I can't reconstruct my arguments. The first few times, it was so frustrating  
[01:12:11] to have understood something and then lost it. I resolved I should always write down  
[01:12:16] anything cool that I've learned. That's part of how this blog came about.  
[01:12:22] How long does it take you to write a blog post? It's something I often do when I don't want  
[01:12:27] to do other work. There's some referee  
[01:12:30] report or something that feels slightly unpleasant for me to do at the time.  
[01:12:35] Writing a blog feels creative and fun. It's something I do for myself.  
[01:12:42] Depending on the topic, it could be a quick half an hour or several hours.  
[01:12:49] Because it's something I do voluntarily, time flies when I write these things down, as  
[01:12:58] opposed to doing something I have to do for administrative reasons that is just drudgery.  
[01:13:03] Those are tasks, by the way, that AI is really helping with nowadays.  
[01:13:07] If civilization could from first principles decide how to use Terry Tao's time, as a  
[01:13:14] limited resource, what is the biggest difference? What if the veil of ignorance got to decide how to  
[01:13:22] use Terry Tao's time versus what it does now? This podcast wouldn't be happening.  
[01:13:29] As much as I complain about certain tasks that I don't want to do, but have to do… As you get  
[01:13:34] more senior in academia, you get more and more responsibilities, more committees, and whatever.  
[01:13:42] I have also found that a lot of events I reluctantly went to because I was  
[01:13:47] obliged to for one reason or another… Because it's outside my comfort zone,  
[01:13:51] it often results in interactions with people I wouldn't normally talk to, like you for instance.  
[01:13:57] I would learn interesting things and have interesting experiences.  
[01:14:01] I would have opportunities to then network with other people that I never would have before.  
[01:14:08] So I do believe a lot in serendipity. I do optimize portions of my day  
[01:14:18] where I schedule very carefully. But I am willing to leave some portions just  
[01:14:25] to do something that is not my usual thing. Maybe it'll be a waste of my time,  
[01:14:29] but maybe I will learn something. More often than not, I get a positive  
[01:14:38] experience that I wouldn't have planned for. So I believe a lot in serendipity.  
[01:14:45] Maybe there's a danger in modern societies, not just with AI, that we've  
[01:14:50] become really good at optimizing everything. We’re not optimizing our own optimization.  
[01:14:59] With COVID, for example, we switched a lot to remote meetings, so everything was scheduled.  
[01:15:07] We kept busy in academia. We met almost the same number of people we met in person,  
[01:15:14] but everything had to be planned in advance. What we lost out on was the casual knocking  
[01:15:22] on a hallway door, just meeting someone while getting a coffee.  
[01:15:28] Those serendipitous interactions may not seem optimal, but they are actually really important.  
[01:15:37] When I was a grad student, I would go to the library to look for a journal article.  
[01:15:42] You had to physically check out the journal and read the article.  
[01:15:46] You could browse through and sometimes the next article was also interesting.  
[01:15:52] Sometimes it wasn’t, but you could accidentally find interesting things.  
[01:15:56] That has basically been lost now. If you want to access an article,  
[01:16:02] you just type it into a search engine or an AI, and you get exactly what you want instantly.  
[01:16:06] But you don't get the accidental things you might have found if you'd done it more inefficiently.  
[01:16:20] I spent a year once at the Institute for Advanced Study, which is  
[01:16:23] a great place with no distractions. You're there just to do research.  
[01:16:29] The first few weeks you're there, it's great. You're getting all these papers written up that  
[01:16:33] you've been wanting to do for a long time. You think about problems for  
[01:16:35] blocks of hours at a time. But I find if I stay there for more  
[01:16:39] than several months, I run out of inspiration. I get bored. I surf the internet a lot more.  
[01:16:46] You actually do need a certain level of distraction in your life.  
[01:16:50] It adds enough randomness and high temperature. I don't know the optimal way to schedule  
[01:17:02] my life. It just seems to work. I'm very curious when you expect AIs  
[01:17:08] that can actually do frontier math at least as well as the best human mathematicians.  
[01:17:15] In some ways, they're already doing frontier math that is super intelligent that humans can't do,  
[01:17:21] but it's a different frontier from what we're used to.  
[01:17:24] You could argue that calculators were doing frontier math that humans could not accomplish,  
[01:17:29] but it was number crunching. But replacing Terry Tao completely.  
[01:17:38] I mean, what do you want me for? You'll just go on all the podcasts after.  
[01:17:50] It might not be the right question to ask. I think within a decade, a lot of things that  
[01:18:01] math students currently do—what we spend the bulk of our time doing and a lot of stuff we  
[01:18:06] put in our papers today—can be done by AI. But we will find that that actually wasn't  
[01:18:12] the most important part of what we do. A hundred years ago, a lot of mathematicians  
[01:18:20] were just solving differential equations. Physicists needed some exact solution to  
[01:18:27] some system, and they hired a mathematician to laboriously go through the calculus and work out  
[01:18:33] the solution to this fluid equation, whatever. A lot of what a 19th-century mathematician would  
[01:18:40] do, you could make a call to Mathematica, Wolfram Alpha, a computer algebra package, or now more  
[01:18:46] recently to an AI, and it would just solve the problem in a few minutes. But we moved on. We  
[01:18:53] worked on different types of problems after that. Once computers came along—computers  
[01:18:59] used to be human. People used to laboriously  
[01:19:01] create log tables and work out primes as Gauss did, and that has all been outsourced  
[01:19:05] to computers. But we moved on. In genetics, to sequence the genome of a single organism,  
[01:19:16] that was an entire PhD of a geneticist, carefully separating all the chromosomes and whatever.  
[01:19:23] Now you can just spend $1,000 and send it to a sequencer and get it done.  
[01:19:26] But genetics is not dead as a subject. You move to a different scale.  
[01:19:31] Maybe you study whole ecosystems rather than individuals.  
[01:19:34] I take your point but when is most mathematical progress, or almost  
[01:19:38] all mathematical progress, happening by AI? If you find out this year a Millennium Prize  
[01:19:43] Problem has been solved, you would put 95% odds that an AI did it autonomously.  
[01:19:49] Surely there will be such a year. I guess I do believe that hybrid  
[01:19:57] human plus AIs will dominate mathematics for a lot longer. It will depend. It will require  
[01:20:04] some additional breakthroughs beyond what we already have, so it's going to be stochastic.  
[01:20:11] I think AIs currently are very good at certain things, but really terrible at others.  
[01:20:16] While you can add more and more frameworks on top to reduce the error rates and make them work with  
[01:20:23] each other a bit more, it feels like we don't have all the ingredients to really have a truly  
[01:20:33] satisfactory replacement for all intellectual tasks. It is complementary currently. It's not  
[01:20:42] a replacement. Because current level AIs will accelerate science in so many ways,  
[01:20:54] hopefully new discoveries and new breakthroughs will happen more quickly.  
[01:21:01] It's also possible that by destroying serendipity we actually inhibit certain types of progress.  
[01:21:07] Anything is possible at this point. I think the world is very,  
[01:21:11] very unpredictable at this point in time. What is your advice to somebody who would  
[01:21:16] consider a career in math or is early in a career in math, especially in light of AI progress?  
[01:21:25] How should they be thinking about their career differently, if at all,  
[01:21:27] as a result of AI progress? We live in a time of change.  
[01:21:32] As I said, we live in a particularly unpredictable era.  
[01:21:41] Things that we've taken for granted for centuries may not hold anymore.  
[01:21:48] The way we do everything, and not just mathematics, will change.  
[01:21:59] In many ways, I would prefer the much more boring, quiet era where things are much the  
[01:22:03] same as they were 10 years ago, 20 years ago. But I think one just has to embrace that  
[01:22:12] there's going to be a lot of change. The things that you study, some of them  
[01:22:18] may become obsolete or revolutionized, but some things will be retained.  
[01:22:26] You always have to keep an eye on opportunities for things that you wouldn't be able to do before.  
[01:22:37] In math, you previously had to go through years and years of education and be a math  
[01:22:42] PhD before you could contribute to the frontier of math research.  
[01:22:46] But now it's quite possible at the high school level, or whatever,  
[01:22:49] that you could get involved in a math project and actually make a real contribution because of all  
[01:22:52] these AI tools, Lean, and everything else. There will be a lot of non-traditional  
[01:22:58] opportunities to learn, so you need a very adaptable mindset.  
[01:23:06] There will be room for pursuing things just for curiosity and for playing around.  
[01:23:11] You still need to get your credentials. For a while it will still be important to  
[01:23:17] go through traditional education and learn math and science the old-fashioned way.  
[01:23:28] But you should also be open to very different ways of doing science, some of which don't exist yet.  
[01:23:37] It's a scary time, but also very exciting. That's a great note to close on. Terence,  
[01:23:42] thanks so much. Pleasure.  
