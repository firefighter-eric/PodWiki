# General relativity from first principles – Adam Brown

[00:00:00] I'm back with Adam Brown. You currently lead BlueShift at Google  
[00:00:02] DeepMind, which is cracking science and reasoning. In a previous life, Adam was a prolific physicist,  
[00:00:07] taught at Stanford, and did research on everything from cosmology to  
[00:00:11] string theory to general relativity. It's said that general relativity is  
[00:00:14] the most beautiful thing the human mind has ever conceived or seen.  
[00:00:17] I was curious if there's a way that ordinary people like me could understand what is happening,  
[00:00:22] or have some vantage on why it's beautiful, without taking your 20-lecture graduate course.  
[00:00:28] That was the prompt for this lecture. I appreciate you being willing to do it.  
[00:00:31] Super exciting to be here. Yes, I think the answer is yes, we can.  
[00:00:36] General relativity, Einstein's theory of gravity, is, as you say, the most beautiful  
[00:00:41] product of a single mind that we've ever created. It's one of the two great theories of 20th century  
[00:00:45] physics, along with quantum mechanics. Unlike quantum mechanics,  
[00:00:49] it was basically Einstein. He had a little help,  
[00:00:52] but basically it was one person doggedly pursuing this idea for 10 years and then he wrote down  
[00:00:58] this theory that ends up describing the motion of planets in the solar system  
[00:01:03] and also the origin and fate of the universe. It's pretty extraordinary. It took Einstein,  
[00:01:09] one of the most famous minds in history, about a decade to figure it out.  
[00:01:14] But when I teach it I'll do a 10-week course, and in 10 weeks people will  
[00:01:20] get a better idea of general relativity than Einstein really had in 10 years.  
[00:01:26] That's because we have an advantage that Einstein didn't have.  
[00:01:30] We have Einstein, and many others like him going before us, who've been able to take these super  
[00:01:35] complicated ideas—understood at the time as being totally incomprehensible by anybody with  
[00:01:39] a sub-Einstein level of intelligence—and boil them down to their essentials, and not make many of the  
[00:01:46] same mistakes that were made by our forebears. In 10 or 20 minutes, I can't give you a better  
[00:01:54] idea of general relativity than Einstein had, but we can get to the core insight—what Einstein  
[00:02:00] said was his most beautiful idea—and push through it to try and understand  
[00:02:07] what the central idea of this theory is. Ok, let's go. Before general relativity,  
[00:02:14] there was special relativity. Special, meaning it doesn't apply everywhere.  
[00:02:21] That was also invented by Einstein, 10 years earlier, in 1905, during his annus mirabilis.  
[00:02:32] If you want to sloganize special relativity, you would start with the observation, or the  
[00:02:38] hypothesis, that nothing can go faster than light. Special relativity takes that observation,  
[00:02:45] promotes it to a principle, takes that principle extremely seriously as the  
[00:02:50] central observation of our understanding of spacetime, and you arrive at special relativity.  
[00:02:56] Special relativity applies to electromagnetism. It applies—though Einstein didn't even know  
[00:03:03] about these at the time—straightforwardly to the strong and weak nuclear forces, two of the other  
[00:03:09] fundamental forces that we know about. It does not obviously apply to gravity.  
[00:03:14] That was corrected 10 years later by Einstein in his general theory of relativity,  
[00:03:24] a theory more general because it includes gravity. It completes the set of fundamental forces.  
[00:03:30] Again, it was invented by Einstein after 10 years of dogged pursuit, in 1915.  
[00:03:36] If you wanted to sloganize general relativity, you might say, "Not even gravity."  
[00:03:43] Nothing can go faster than light, not even gravity.  
[00:03:46] There's much more to it than that, but it's going to complete this arc of the centrality of nothing  
[00:03:53] being able to go faster than the speed of light. To see some background here, we're going to have  
[00:04:03] to rewind all the way back to the theory of gravity that existed before Einstein.  
[00:04:08] The reigning theory of gravity at the time of Einstein stretches all the way  
[00:04:13] back to Newton in the late 17th century, Newton's laws, in his Principia in 1687.  
[00:04:26] Well, he had a few. Maybe the one we  
[00:04:30] could most talk about today is two of them. His famous second law says the acceleration,  
[00:04:41] a, caused by a force is given by the formula ma=F. If you have a force F, it'll cause an acceleration  
[00:04:50] on an object given by a, where the mass tells you how much an object resists being accelerated.  
[00:04:59] The bigger the mass, the bigger the force you need to cause a given acceleration.  
[00:05:06] This law, his second law, will turn out to be still true once we come to general relativity.  
[00:05:13] We'll have to have a more sophisticated understanding of what we mean by force  
[00:05:17] and acceleration, but this will be preserved by general relativity.  
[00:05:20] A special case of the second law is Newton's first law.  
[00:05:23] Newton's first law says that if the force is zero, then the acceleration is zero.  
[00:05:29] If the force is zero, then objects continue to move on a straight line at all times.  
[00:05:37] That will also continue to be true in general relativity.  
[00:05:40] That if not subject to an external force, objects move along straight lines.  
[00:05:45] However, we'll have to upgrade our understanding of what we mean by force  
[00:05:49] and what we mean indeed by straight line. That's going to keep being true.  
[00:05:56] The one that's not going to keep being true is Newton's law of gravity.  
[00:06:00] Newtonian gravity tells you what the acceleration is in response to a force,  
[00:06:05] but you need to know what the force is to be able to do anything with that.  
[00:06:08] Newton's law of gravity says that the force caused by the gravitational interaction of two bodies is  
[00:06:19] what's called Newton's constant—just some constant of nature—times the mass of one  
[00:06:24] body times the mass of the other body—the mass of the sun times the mass of the Earth—divided  
[00:06:29] by the distance between them squared. It's the famous inverse-square law.  
[00:06:36] It's a vector that points in the direction of separation, and it's  
[00:06:40] attractive, so there's a minus sign there. This will not be true in general relativity.  
[00:06:48] In fact, you immediately see that there's a tension between this gravitational force  
[00:06:53] law and the claim that nothing can go faster than the speed of light.  
[00:06:56] If this were literally true, then by jiggling the sun, a straightforward  
[00:07:03] interpretation of this law would just say that the force at the Earth varies immediately.  
[00:07:08] I've changed the distance of the Earth and the sun, and so I can immediately detect it at the  
[00:07:13] Earth, not eight minutes later but immediately. That would imply that you could send an influence  
[00:07:20] faster than the speed of light. Newton's force  
[00:07:23] law is inconsistent with this principle. One option, of course, could be that this is true  
[00:07:32] for non-gravitational forces, but not true once you have gravity, and that indeed, using gravity,  
[00:07:37] you could perhaps build a faster-than-light telephone using gravitational effects.  
[00:07:42] That's a possibility, but not a possibility that Einstein really wanted to embrace.  
[00:07:47] He'd spent many years chasing out any possibility of going  
[00:07:53] faster than light or any superluminal influences. So Einstein, and in fact many people at the time,  
[00:08:00] thought that this is the one that has to give. Indeed, that is what's going to  
[00:08:03] turn out to be true. Okay, so where are we?  
[00:08:09] There's actually a precedent here for an inverse-square law getting modified  
[00:08:17] in such a way that it ends up being consistent with special relativity, and that precedent is  
[00:08:24] the other force of nature, the electric force. There's also the electrostatic force law—not  
[00:08:29] written down by Newton, but written down a century or so later—which says that the force caused,  
[00:08:38] not by the gravitational interaction of two objects, but by the electrostatic  
[00:08:41] interaction of two charged objects, has a very similar form to the gravitational force.  
[00:08:47] It tells you that the force is equal to some constant times the charge of one object times  
[00:08:53] the charge of the other object, pointing also in the direction of separation between the two  
[00:08:59] objects, divided by the distance squared. It’s another inverse-square law. Again,  
[00:09:07] for exactly the same reason, electrostatics looks to be inconsistent with special relativity.  
[00:09:15] But ultimately it's not. Or ultimately, this is not the full story.  
[00:09:20] Electrostatics is just one limit of the true theory of electromagnetism,  
[00:09:25] which is Maxwell's laws, which has not just electric forces, but it also has magnetic forces.  
[00:09:32] The electric forces only look exactly like this when nothing is moving.  
[00:09:35] When things do start to move, there are additional corrections to this, all of  
[00:09:40] which conspire to make the electrostatic force law fully consistent with special relativity.  
[00:09:47] In fact, the historical direction of understanding ran the opposite way.  
[00:09:51] First of all, you have Maxwell in the middle of the nineteenth  
[00:09:54] century writing down Maxwell's equations. Only later do people notice, "Hey, Maxwell's  
[00:10:01] equations actually are fully consistent with nothing going faster than the speed of light."  
[00:10:07] That consistency is reflected in a symmetry called the Lorentz symmetry of the Maxwell  
[00:10:12] field equations, only noticed later after they were written down, that eventually led Einstein  
[00:10:16] to formulate his special theory of relativity. So we have a precedent for starting with an  
[00:10:22] inverse-square law and then dressing it up in a full relativistically invariant theory.  
[00:10:29] So you might say, well, let's just take gravity and do exactly the same thing to  
[00:10:33] gravity that we did to electrostatics, in order to make some gravito-magnetic theory that makes  
[00:10:43] Newton's second law an approximation that's ultimately consistent with special relativity.  
[00:10:50] In some grand sense, that is what we're going to end up doing.  
[00:10:53] That is what Einstein's going to end up doing. But it's going to be a much more radical departure  
[00:10:58] than the Maxwell generalization of electrostatics. There's really two hints, both of which are  
[00:11:05] visible in this formula, that we're going to have to do something slightly different  
[00:11:08] than we did for electrostatics. The first difference between the  
[00:11:15] electrostatic force law and Newton's law of gravity is this sign difference.  
[00:11:22] There is a big difference, which is that here it is a minus sign, and here it is a plus sign.  
[00:11:27] That is reflected in the fact that if you have two positive masses—the Earth and the  
[00:11:33] Sun—they gravitationally attract each other. Conversely, if you have two like charges,  
[00:11:42] they electrostatically repel each other, which is why that's a minus sign and that's a plus sign.  
[00:11:51] That means that you cannot do literally the same thing for gravity that you did  
[00:11:57] for electromagnetism, because otherwise, if you did mathematically the same trick,  
[00:12:02] you'd end up with mathematically the same result, which is that you would find that like masses  
[00:12:06] would repel rather than attract. Not to get ahead of ourselves,  
[00:12:11] but ultimately that's because electrostatics is mediated by a spin-1 particle, the photon,  
[00:12:18] and gravity is going to be mediated by a spin-2 particle, and that's responsible  
[00:12:23] for the change in that sign there. That's why you can't do exactly  
[00:12:26] the same thing as electrostatics. So Einstein had to look for something else.  
[00:12:31] He had to look for some other way to try and lift this to a relativistically invariant theory.  
[00:12:38] In doing that, he had one clue. There's lots of stuff going on.  
[00:12:43] It's part of Einstein's central genius to focus on this as a highly  
[00:12:48] significant clue of where he should look. It's sometimes described as his most beautiful  
[00:12:52] thought, that's how he would describe it. The clue is this. There is another  
[00:12:58] difference between the gravitational force law and the electrostatics,  
[00:13:04] and that is the object that plays the analog of the charge in electrostatics, for gravity.  
[00:13:14] It's the fact that it's the mass sitting here. That's a strange coincidence from  
[00:13:24] Newtonian physics. Mass, in electrostatic  
[00:13:29] forces and accelerations, plays exactly one role. It's sitting here. It's the inertia of the object,  
[00:13:36] and it's what is resisting being accelerated. This is sometimes called the inertial mass.  
[00:13:44] And then the charge is completely different and unrelated to the mass.  
[00:13:46] You can have heavy objects that have no charge, like the neutron.  
[00:13:52] You can have light objects, like the electron, that have high charge.  
[00:13:55] There is no necessary relation between the charge of a particle and its mass.  
[00:14:01] They're just two entirely separate things. Not true in gravity. In gravity, this mass  
[00:14:07] that's sitting here in Newton's second law—the inertial mass that's resisting the  
[00:14:12] force—is exactly equal to the mass that's sitting here in Newton's gravitational law,  
[00:14:20] that's telling you how much you're pulled along. It's the same mass. So this is sometimes called  
[00:14:25] the gravitational mass, and this is sometimes called the inertial mass.  
[00:14:30] Unlike in electrostatics, the gravitational mass that appears in this formula is equal to  
[00:14:42] what's sometimes called the inertial mass that sits in this formula.  
[00:14:50] This equation is already true in Newtonian physics.  
[00:14:53] Newton noticed it, in fact, and did a number of experiments to confirm that  
[00:14:57] this was true to one part in 1,000 or so. By the time of Einstein, we knew it was  
[00:15:01] true to one part in a billion, and now we know it's true to one part in 10¹⁵.  
[00:15:08] It's striking that these two—which in Newtonian physics is just a complete coincidence,  
[00:15:13] essentially, that they're the same thing—nevertheless  
[00:15:16] were observed to be exactly the same thing. Einstein honed in on this fact, and it was his  
[00:15:23] central clue for what to do next. This is sometimes called the  
[00:15:27] equivalence principle. It's responsible for the  
[00:15:30] fact that if you take a feather and a brick in a vacuum chamber and drop them both, they will  
[00:15:37] both fall and hit the ground at the same time. They'll fall and hit the ground at the same  
[00:15:42] time because even though the force on the brick is much stronger than the force on the  
[00:15:48] feather because it's heavier, that exactly cancels out the fact that the resistance to  
[00:15:53] acceleration of the brick is larger than the resistance to acceleration of the feather,  
[00:16:00] and they fall exactly at the same rate. The equality of those two is responsible  
[00:16:04] for that exact equality. Einstein's genius was to  
[00:16:08] hone in on this as a central clue for how he is going to end up replacing Newton's law.  
[00:16:17] A reason it's a central clue is because there is, in fact, another class of forces—not  
[00:16:24] fundamental forces like electromagnetism or gravity, but a set of emergent forces—that  
[00:16:29] exactly have this property baked into them, that's guaranteed in those theories.  
[00:16:36] To explain that, we're now going to move over to the experimental section of this discussion.  
[00:16:42] So here's a bucket. Here's some water filling the bucket.  
[00:16:52] You better know your physics, Adam. Otherwise you'll destroy the studio.  
[00:16:56] No tricks. Will you put your finger in that and confirm that it's wet?  
[00:17:03] Here is the bucket. At the bottom, there's no mystery  
[00:17:06] why the water is not falling out of the bucket. It's not falling out because the force of gravity,  
[00:17:12] as we'd understand it, is pointing down to the bottom of the bucket.  
[00:17:15] But now what we're going to do is go a little bit faster and loop the loop.  
[00:17:22] Now there is what you might find superficially surprising,  
[00:17:28] which is that the water doesn't fall out of the bucket even when the bucket is upside down.  
[00:17:34] There are two ways to understand that. One way is just the straightforward way.  
[00:17:39] You would say the water wants to fall out of the bucket when it's at the top of its arc,  
[00:17:47] but by the time it's got itself together to accelerate enough to fall out of the bucket,  
[00:17:51] the bucket's moved on and is now below, and it just didn't have time to fall out of the bucket.  
[00:17:59] Or you might say the same reason that astronauts don't end up falling to Earth.  
[00:18:04] The second perspective, which is an equally valid perspective, is imagining that you're  
[00:18:08] riding along with the water in the bucket. And from that point of view, there's another  
[00:18:13] explanation for why the water doesn't fall out of the bucket, and that is the centrifugal force.  
[00:18:17] From the perspective of somebody moving along with the bucket, there is a force pushing them  
[00:18:22] towards the bottom of the bucket, and that force is known as the centrifugal force.  
[00:18:34] It's what's known as a fictitious or inertial force.  
[00:18:38] The centrifugal force just says that there is a force caused by being in a rotating  
[00:18:46] reference frame, given by your speed divided by the radius of the circle you're going  
[00:18:53] round in, pointing positively outwards. So this is the centrifugal force that pins  
[00:19:00] you to the bottom of the bucket, or pins you to the outside of the car as you go around a bend.  
[00:19:08] What do we notice? What we notice is that your charge under the centrifugal force,  
[00:19:13] if you will—how intensely you feel a centrifugal force—is once again, just like with gravity but  
[00:19:19] unlike with electrostatics, given by your mass. The mass that tells you how much centrifugal  
[00:19:28] force you get is given by your inertial mass. But of course, here it's absolutely no mystery  
[00:19:32] whatsoever why the mass that's sitting here on the right-hand side is given by your inertial mass.  
[00:19:40] It is given by your inertial mass precisely because the reason you're experiencing this  
[00:19:45] force is precisely the tendency of masses to wish to move along straight lines.  
[00:19:49] The fact that you're not moving along a straight line, you're moving in a circle,  
[00:19:53] it is precisely that inertial tendency that causes the mass to begin with.  
[00:19:57] Another way to say it: any time you have one of these inertial forces,  
[00:20:03] caused just by your inertia, it is guaranteed to be the case that the charge under that force  
[00:20:09] is given by the inertial mass. So inertial forces always have  
[00:20:17] a charge given by the inertial mass. Gravity has a charge, and the charge  
[00:20:26] of gravity is given by the inertial mass. So Einstein leapt: could it be the case,  
[00:20:31] and this was his central idea, that gravity itself is an inertial force?  
[00:20:38] That's permitted because the gravitational mass is equal to the inertial mass.  
[00:20:42] It would be totally impossible for something like electromagnetism,  
[00:20:46] because it would require that the electromagnetic charge was equal to the inertial mass,  
[00:20:51] which is simply false for electromagnetism. Could it be the case, Einstein asked,  
[00:20:55] that it's true for gravity? It's permitted by this fact.  
[00:20:58] It would also explain this fact as now not an accidental truth like in Newton's laws,  
[00:21:02] but a necessary fact about the world. So this was Einstein's central idea in 1907,  
[00:21:09] his most beautiful thought. But it sounds totally crazy.  
[00:21:14] It sounds totally crazy because it requires us to be wrong about what straight lines are.  
[00:21:21] It is an extremely radical proposition for the reason that I will describe right now.  
[00:21:26] Inertial forces—like the centrifugal force or the Coriolis force or any of these other ones that  
[00:21:35] we're familiar with—are forces you experience when you are not moving on a straight line.  
[00:21:42] When you are moving on a straight line, you don't experience any inertial forces.  
[00:21:49] So in order for this to be true, we'd have to say that astronauts who are free-floating and  
[00:21:56] free-falling are moving along a straight line. We'd have to say that you, who are just sitting  
[00:22:03] there, seemingly not moving, are experiencing the force of gravity pushing you into your chair.  
[00:22:08] We'd have to say that you're not moving along a straight line.  
[00:22:11] So we'd have to be pretty wrong about who's moving along a straight line and who's not.  
[00:22:17] As I’ve gotten to know the folks at Jane Street, I’ve noticed that a lot of them  
[00:22:20] have physics backgrounds. I recently got a chance to talk to Jed Thompson,  
[00:22:23] who was a particle physicist before he was a trader, about how his physics training  
[00:22:28] helps him with his work at Jane Street. I think very few Jane Street traders or  
[00:22:32] researchers come in with any finance background or any trading background.  
[00:22:36] When I used to be in physics, something that I would say is, I almost never do a calculation  
[00:22:41] without already having a pretty good guess at the answer. In trading, I think the same is true.  
[00:22:45] These things are fundamentally models for how the world is behaving. You can build good intuition  
[00:22:51] by seeing patterns over and over again, and come to a point where you’re mostly asking  
[00:22:56] the right question from the beginning, which short-circuits a lot of the work.  
[00:23:01] So even if you don’t have a finance background, or for that matter a physics background,  
[00:23:04] you should still consider applying. Go to janestreet.com/Dwarkesh to learn more.  
[00:23:10] So this is a radical idea because it requires us to be wrong about what a straight line is.  
[00:23:15] In particular, you sitting here, just sitting in your chair… Here is your height above the center  
[00:23:23] of the Earth as a function of time. Here is Dwarkesh just  
[00:23:34] sitting here at constant height. Because you are experiencing the force of  
[00:23:38] gravity, if gravity is an inertial force—because you're experiencing a force down—that means that  
[00:23:44] you have to be moving along a not straight line. So that's you. By contrast, this piece of chalk,  
[00:23:57] as it goes up and down, executes something that's well approximated by a parabola.  
[00:24:07] The chalk is in free fall until I catch it, which means that if gravity is an  
[00:24:14] inertial force, this has to be straight. Now, certainly the way I've plotted it,  
[00:24:20] this looks straight and that one does not. So if gravity is to be an inertial force,  
[00:24:25] we have to be wrong about what is a straight line and what is not a straight line.  
[00:24:33] However, this is actually a situation with which you should be familiar  
[00:24:36] if you've sat in an airplane seat and looked at the screen in front of you.  
[00:24:41] Imagine the map that you see on an airplane, and imagine you are  
[00:24:47] flying from San Francisco to London. Now, I'm not good at drawing the Earth,  
[00:24:56] but here is my version of it. Here we are in San Francisco.  
[00:25:01] Here is Greenland, coming in from the North Pole. And here is England. Here's London.  
[00:25:13] I can tell you're a physicist because of the very idealized forms of the continents.  
[00:25:22] Sometimes it can be quite frustrating sitting there in the backseat of the airplane,  
[00:25:27] because obviously the plane should be flying like this, moving along the  
[00:25:33] shortest distance from one place to another. But instead they take this massive detour  
[00:25:38] that clips Greenland and heads on down. You know that in fact that's not what's going on.  
[00:25:46] You know that in fact, despite what it looks like on the graph, this is not a straight line.  
[00:25:52] This rhumb line, it's sometimes called, is not straight, and would certainly not be the  
[00:25:57] shortest path from San Francisco to London. And this is in fact, to a good approximation,  
[00:26:04] a straight line. So in fact, the straight  
[00:26:10] line from San Francisco to London does indeed go over Greenland, as I will now demonstrate.  
[00:26:22] Here is San Francisco, here is London. You can see that the straight line that  
[00:26:28] goes straight from one to the other would go in this direction over Greenland and hit London.  
[00:26:39] That's obvious on this map, because this map reflects the curvature of the Earth.  
[00:26:45] This map is getting confused, and it's getting confused because it's  
[00:26:50] trying to pretend that the Earth is flat. It is trying to ignore the curvature of the Earth,  
[00:26:57] and because it's trying to map a round Earth onto a flat panel, there have to be distortions.  
[00:27:05] Whenever you try and take something that is curved and pretend it's not curved,  
[00:27:09] you will inevitably end up being wrong about what is and is not a straight line.  
[00:27:15] You see this on the Earth, where this line that goes up and then  
[00:27:22] comes down is in fact the straight line. You see it also in spacetime with general  
[00:27:29] relativity, where this parabolic arc of the chalk as it's thrown up, it is in free fall,  
[00:27:36] it is the straight line in general relativity. And just like in general relativity,  
[00:27:41] the reason you are confused about what's straight and what's not straight is that  
[00:27:45] you are trying to pretend with this graph that you are in a flat spacetime.  
[00:27:52] In fact, you are in a curved spacetime. So in Einstein's theory, the effect of  
[00:27:58] matter is going to be to curve spacetime. Through curving spacetime, it's going to  
[00:28:05] change what's a straight line and what's not a straight line.  
[00:28:10] People who are going along what they incorrectly think of as straight lines are going to experience  
[00:28:17] the gravitational force, whereas astronauts are going to not experience the gravitational force.  
[00:28:22] The only missing piece here is to mathematically characterize the way in which spacetime is curved.  
[00:28:33] In Newtonian physics, the Newtonian force is caused by the presence of mass.  
[00:28:37] In Einstein's general theory of relativity, it will be the curvature  
[00:28:41] of spacetime that is caused by the mass. He struggled for eight years between 1907,  
[00:28:49] when he had this picture approximately mapped out, and 1915, when he wrote down in its  
[00:28:56] finished form his general theory of relativity. The final output of those eight years was his  
[00:29:02] famous formula, that I will not explain but will write down, that exactly captures his intuition.  
[00:29:23] I will walk you through this formula. This is just a beautiful formula.  
[00:29:29] The left-hand side is some mathematics invented by some Eastern Europeans that  
[00:29:35] characterizes the curvature of spacetime. This says how much spacetime is curved.  
[00:29:42] This is some tensor, and the tensor will be zero if spacetime were flat, and non-zero  
[00:29:47] when spacetime is curved in a particular way. On the right-hand side is not spacetime anymore.  
[00:29:54] On the right-hand side is matter. There are some constants: our old  
[00:29:59] friend Newton's constant, π an even older friend, and the speed of light.  
[00:30:05] And then this quantity T_(μν). T_(μν) is like a relativistic  
[00:30:10] generalization of the mass that sits on the right-hand side of Newton's force equation.  
[00:30:18] So it is saying that the presence of mass—and in fact not just mass, but all forms of mass  
[00:30:24] and energy—on the right-hand side causes the curvature of spacetime on the left-hand side.  
[00:30:31] Or in a slogan: matter tells spacetime how to curve.  
[00:30:37] Once matter's told spacetime how to curve, the curvature of spacetime tells matter  
[00:30:42] how to move, in the second half of the slogan. The curvature of spacetime tells matter to move  
[00:30:47] along straight lines of the curved space, and so experience fictitious forces if you  
[00:30:51] try and pretend that spacetime is flat. That is Einstein's general theory of  
[00:30:56] relativity in a nutshell. Backing up: an amazing  
[00:30:59] thing about Newtonian gravity is that he invented it, allegedly due to some thought  
[00:31:06] experiment to do with an apple falling off a tree. It describes not only an apple falling off a tree,  
[00:31:11] but the motion of the objects in the heavens. It’s a massive cross hit that it describes  
[00:31:17] planetary motion and also an apple falling off a tree.  
[00:31:21] This was this amazing thing that Newton unified the heavens and the Earth and had  
[00:31:26] one formula that applied to both. General relativity does all of  
[00:31:29] that and goes one step further. It describes the motion of apples falling  
[00:31:32] off trees, it describes the motion of Mercury and the planets in the solar system, and it describes  
[00:31:37] the expansion of the entire universe. That's a crazy, huge number of  
[00:31:42] orders of magnitude that it hits. You were saying a moment ago that one  
[00:31:47] of the beautiful things about this theory is that it has reach in all these interesting ways  
[00:31:52] that were not originally anticipated, to solve this original observation that Einstein had.  
[00:31:57] One of them, obviously, is the black hole. I would love to get more insight than the high  
[00:32:03] school version—that light falls into it and can't get out—of why black holes work the way they do.  
[00:32:08] Black holes are fascinating objects in general relativity, really the quintessential object in  
[00:32:15] general relativity that doesn't exist in the same way in Newtonian physics.  
[00:32:20] The story is kind of wild. Einstein wrote down his field equations,  
[00:32:25] the field equations we wrote on the board, describing the relationship between curvature  
[00:32:29] and the amount of energy in the system. He thought that those equations are so  
[00:32:35] complicated, no one would ever come up with exact solutions to them, that we'd just  
[00:32:40] always be having to do approximations. That turned out not to be correct.  
[00:32:44] Schwarzschild was a Prussian artillery officer in the First World War.  
[00:32:50] In between calculating the trajectories of artillery they were lobbing in the direction  
[00:32:59] of their enemy, he figured out that Einstein's equations—pretty much immediately after Einstein  
[00:33:04] had written them down, within a matter of months—in fact have an exact solution, a  
[00:33:11] solution now known as the Schwarzschild equation, and that we now understand describes a black hole.  
[00:33:18] It is a solution in which there is no matter, except possibly at  
[00:33:22] the very center in a way we'll not describe. It's a central point-like amount of matter.  
[00:33:28] It describes what the spacetime around that looks like.  
[00:33:31] It's called the Schwarzschild solution, and it describes a black hole.  
[00:33:34] They were not called black holes at the time. In fact, people were extremely confused about  
[00:33:39] what this solution even meant. People wrote down wrong things for  
[00:33:43] about half a century about what this meant. Perhaps the worst offender was Einstein,  
[00:33:48] who got extremely confused about it. He got particularly confused about what I  
[00:33:51] will describe as the event horizon, and wrote all sorts of wrong things about how objects  
[00:33:54] would maybe bounce off the event horizon. He was just totally confused, but from  
[00:33:58] a modern perspective it's extremely simple to understand what's going on.  
[00:34:01] So let me tell you what a black hole is. General relativity, as we set it up,  
[00:34:06] is about a collision between gravity and the finite speed of light.  
[00:34:10] The simplest collision you could do was actually noticed by people even in the 18th century, before  
[00:34:14] we had special relativity or anything like that. They just asked a very simple question.  
[00:34:20] If you want to shoot something off the Earth, you know you need to shoot it with  
[00:34:25] a certain velocity, the escape velocity. You need to shoot it fast enough if you  
[00:34:30] want to escape far away from the Earth, so that the kinetic energy of the object you're  
[00:34:35] shooting is equal to the gravitational binding energy of the Earth's surface.  
[00:34:40] M is the mass of the Earth and r is the surface of the Earth.  
[00:34:43] For Earth, the escape velocity turns out to be about 11 kilometers per second.  
[00:34:48] But for objects that are heavier or more compact, the escape velocity is larger.  
[00:34:54] For example, for Jupiter it would be hundreds of kilometers a second.  
[00:34:58] You can imagine objects that are so heavy or so compact that in fact the escape  
[00:35:06] velocity becomes equal to the speed of light. So people idly wondered what would happen then.  
[00:35:12] They didn't have the tools to address it, but in the 18th century they wondered what would happen.  
[00:35:16] You can calculate what the critical value of the velocity is.  
[00:35:21] Just putting the velocity equal to the speed of light, this gives a critical radius of 2GM—the  
[00:35:29] mass of the object cancels—divided by c². So that's somewhat suggestive. If you had  
[00:35:37] an object that was this compact and had this mass, the escape velocity would be given by c,  
[00:35:43] the speed of light. The connection  
[00:35:44] you're pointing out is a Newtonian one. Did anyone make this connection before GR?  
[00:35:48] Absolutely. People in the late 18th century wrote this formula down.  
[00:35:52] I think both Michell and Laplace had this. And they said that if you had an object  
[00:35:59] that was that massive and compact, light would not be able to escape.  
[00:36:04] That reason is not particularly compelling by modern standards but it turns out to be  
[00:36:08] particularly correct, including crazily this factor of 2, which is correct  
[00:36:12] for completely coincidental reasons. But let me give you a more compelling  
[00:36:17] argument that something funny is going to happen around this radius.  
[00:36:22] And to do that, let's think about trying to extract energy from objects by lowering  
[00:36:27] the objects down towards a central mass. Let's start off perhaps with the Earth.  
[00:36:32] Here it is. We're going to start off a long way away from the Earth, with a brick of mass m.  
[00:36:39] I'm going to take this brick, attach it to a pulley system,  
[00:36:43] and then slowly lower the brick down towards the surface of the Earth and deposit it with zero  
[00:36:49] velocity on the surface of the Earth down there. In doing so, I can extract energy from the brick.  
[00:36:57] I've extracted energy from the brick because there's a force pulling the brick down.  
[00:37:02] That force I'm doing through a certain distance, and that gives you an energy.  
[00:37:05] We know, at least in Newtonian physics, what the formula for the amount of energy you can  
[00:37:09] extract from the brick is: G times the mass of the Earth times the mass of the brick,  
[00:37:18] divided by r, the radius away. It's an energy, not force, so it's an inverse  
[00:37:23] distance law, not an inverse square distance law. That's the energy you can extract from the  
[00:37:27] brick by lowering it down to a distance r away from the Earth.  
[00:37:30] Of course, if you try to lower it beyond the surface of the Earth, this formula changes.  
[00:37:34] But let's just put it on the surface of the Earth. So this is the amount of energy I have extracted  
[00:37:38] from the brick, out here a long way away. You can ask, what fraction of the rest  
[00:37:44] mass energy of the brick have I extracted? This is a question that you would only naturally  
[00:37:48] ask once you've invented special relativity and know that the rest mass energy is given by mc².  
[00:37:55] We can straightforwardly calculate, at least in this approximation, that the fraction of the  
[00:38:00] energy that you've extracted is that divided by the rest mass energy you started with.  
[00:38:08] The mass of the brick, of course, is going to cancel, but not the mass of the Earth.  
[00:38:12] This is going to be given by G times the mass of the Earth, divided by c²  
[00:38:19] times the radius away from the Earth at which you stop, the radius of the Earth.  
[00:38:25] So what fraction have I got out of it? If you lower down to the Earth's surface,  
[00:38:34] the answer is you haven't really extracted that much from the brick.  
[00:38:38] You've extracted a fraction 7x10⁻¹⁰ of the original rest mass energy of the brick,  
[00:38:46] doing useful work a long way away. First observation: this is small.  
[00:38:54] In other words, the gravitational binding energy of something on the Earth's surface  
[00:38:57] is quite small in natural units. That's why we didn't really notice  
[00:39:03] general relativity on the Earth's surface until we did very sensitive experiments, because general  
[00:39:09] relativity is in some sense a Taylor expansion in this number, where the relativistic effects,  
[00:39:13] where the first order term is just Newtonian, and then the next order terms will give you  
[00:39:17] the GR corrections to the Newtonian answer. Observation number two, and this is something  
[00:39:22] of a digression, is that by essentially sheer coincidence, this number here is very close to  
[00:39:31] the chemical binding energy of rocket fuel. So if you take a rocket fuel  
[00:39:36] like an oxygen-hydrogen mix, the chemical energy binding the rocket together, which is the energy  
[00:39:43] that you're going to extract when you burn it to make your rocket go, divided by the mc² of the  
[00:39:52] oxygen and hydrogen you're going to mix together, is given by 1.5x10⁻¹⁰.  
[00:40:01] First observation: these two are close to each other, even though they came  
[00:40:04] from completely different calculations. This was a gravitational calculation that  
[00:40:08] was something to do with the Earth. This is a chemical property  
[00:40:13] of hydrogen and oxygen. This is also very small.  
[00:40:19] The reason it's very small is that almost all of the energy in hydrogen and oxygen  
[00:40:23] is not stored in the chemical binding energy of these things going together.  
[00:40:28] The vast majority of it is stored in just the rest mass energy of the protons and the neutrons,  
[00:40:34] which chemical burning doesn't affect at all. The second largest amount is stored in the  
[00:40:40] nuclear binding energy of the protons and the neutrons to each other, given  
[00:40:43] by the strong force and the weak force, which again chemical reactions don't touch at all.  
[00:40:47] This is a small number because chemical bonds are very weak compared to the  
[00:40:52] rest mass of the things we're considering. These two small numbers are almost exactly  
[00:40:57] equal to each other, which is why we can use chemical rockets to get to space, but it's hard.  
[00:41:03] In particular, this number is a few times bigger than this number, which means that your payload  
[00:41:12] fraction is quite small when trying to use chemical rockets to get to space,  
[00:41:17] because most of your fuel cannot get to orbit. You have to pay a rocket factor that's going to  
[00:41:25] tell you that most of what's sitting there on the launch pad is going to have to be burnt up  
[00:41:29] before you get to space, in order to get a small fraction of the rocket up to space.  
[00:41:37] In other words, we can use chemical rockets to get to space in a way that  
[00:41:41] would be totally impossible if we tried to do it from the surface of the sun, but it's hard.  
[00:41:46] Okay, that's the fraction on the Earth. But this formula tells you that if you  
[00:41:50] have an object that's heavier or more compact, the fraction of energy that  
[00:41:56] you extract by lowering the object down to the surface is going to be larger.  
[00:41:59] For example, if you lower it not down to the Earth's surface but down to the sun's surface,  
[00:42:05] this would be larger. It’d be a million times larger,  
[00:42:10] because the sun is a few million times the mass of the Earth, but then it's also bigger,  
[00:42:15] so that takes it away a little bit. You end up with 2x10⁻⁶, the famous  
[00:42:23] redshift from the sun's surface. You can escalate from there.  
[00:42:28] You can imagine cramming a sun-like mass into an Earth-like  
[00:42:33] radius to make this formula even bigger. Sun mass, Earth radius. That's pretty much exactly  
[00:42:37] what happens in a white dwarf like Sirius B. And this would get even bigger again.  
[00:42:55] A larger fraction of the mass of the object you'd be extracting by lowering it down to the surface.  
[00:43:00] But it really feels like something has to give before we make an  
[00:43:04] object that is too massive and too compact. In particular, if you look at this formula, what  
[00:43:13] happens for r less than or equal to GM over c²? If this object were so compact and so heavy that  
[00:43:27] it had a radius less than the mass of the object divided by c², it sure looks like you  
[00:43:34] could get more than a hundred percent. The fraction would be bigger than one.  
[00:43:37] You could get more than a hundred percent of the mass of your brick back by lowering  
[00:43:41] it down to the surface of this object. And that feels wrong. That feels, in fact,  
[00:43:46] more wrong than what's going on here, because now you've got all this energy a long way away.  
[00:43:52] You could perhaps use it to make a whole new brick.  
[00:43:55] You've got all this more than mc² out there. Lower that one down, and it feels like we've  
[00:44:00] figured out a way to make a huge amount of energy where there was no energy before.  
[00:44:08] This argument is pretty suggestive that something has to go wrong by  
[00:44:12] the time you get down to that radius. Indeed, when you do the calculation—this  
[00:44:16] is a Newtonian calculation, so it's only suggestive —in full general relativity,  
[00:44:20] indeed something does go wrong. The thing that goes wrong is that  
[00:44:23] you form a black hole. You can imagine two  
[00:44:28] ways that you could avoid this conclusion. One would be somehow that gravity becomes very  
[00:44:34] weak when you get close to a massive object, weaker than the Newtonian law would predict.  
[00:44:41] That's sort of what saves you if you try and repeat this same trick in electromagnetism,  
[00:44:48] lowering a charge down towards another charge and trying to extract the  
[00:44:50] electrostatic energy between them. What happens is, essentially due to  
[00:44:56] quantum effects, when one gets too close to the other, they start to fuzz out.  
[00:45:04] The energy going like inverse r gets softened, and you can't extract more energy because they  
[00:45:10] stop attracting each other so hard. So that's one possibility,  
[00:45:15] the force gets weaker than Newtonian law would predict as you approach the other object.  
[00:45:22] That's actually the opposite of how general relativity resolves this.  
[00:45:25] General relativity resolves this paradox by the force getting  
[00:45:31] stronger than Newtonian law would predict. In particular, the force gets so strong when  
[00:45:38] you try to get within this radius, that in fact you cannot slowly lower the brick down towards  
[00:45:43] the surface because you've formed a black hole. The gravitational force becomes infinite at a  
[00:45:48] finite distance away—not at r=0, but at some finite value of r—and the brick simply gets  
[00:45:54] ripped out of your hand and you're unable to extract any more energy out of it.  
[00:45:58] That's the resolution that general relativity provides to this paradox.  
[00:46:01] In particular, you will find that you've formed a black hole.  
[00:46:05] Crusoe gave us early access to their serverless fine-tuning product,  
[00:46:08] which lets you fine-tune open models without having to deal with infra or provisioning.  
[00:46:12] I thought it’d be cool to try fine-tuning a question generator using the transcripts  
[00:46:16] of my old interviews. Have the models gotten so good that if they had all my research and prep,  
[00:46:20] and they could look at a conversation so far, they could ask a next question better than I would?  
[00:46:25] Crusoe made the implementation super straightforward. I just uploaded the data,  
[00:46:29] picked an open model, and started the run. I didn’t have to touch any of the hyperparameters.  
[00:46:33] Crusoe’s applied AI team maintains optimal recipes for each model, so I just set everything on auto.  
[00:46:38] When the run finished, I deployed it as a self-serve endpoint and built an eval for my  
[00:46:42] team. I had them choose the best next question out of three anonymized choices: one that was produced  
[00:46:47] by the base model, one that was produced by the fine-tuned model, and one that I actually asked.  
[00:46:52] Fortunately, my team preferred my actual questions about two-thirds of the time.  
[00:46:56] Hopefully this benchmark doesn’t saturate. And in the remaining cases, they almost always preferred  
[00:47:01] the fine-tuned model over the base model. Serverless inference is live now,  
[00:47:04] and serverless fine-tuning goes live next week. Learn more at crusoe.ai/Dwarkesh.  
[00:47:12] So far, everything we've written down on the board is Newtonian.  
[00:47:14] It's just Newtonian, and you start plugging in the speed of light, and you start getting confused.  
[00:47:18] To actually answer some of these questions that we're asking, you need to go to general  
[00:47:22] relativity, the theory that correctly unifies the speed of light with gravity.  
[00:47:29] This was first done in the context of black holes by Schwarzschild, who wrote down the  
[00:47:32] Schwarzschild metric that describes the gravitational field around a central mass,  
[00:47:36] including potentially around a black hole. Let me write down some of the  
[00:47:41] formulas that emerge. In fact, I think I'm going  
[00:47:44] to write down three formulas, three direct consequences of the Schwarzschild metric.  
[00:47:48] They're going to give us intuition for what it's like outside and indeed inside a black hole.  
[00:47:52] The first formula I'm going to write down is the formula for the gravitational field that  
[00:47:58] you would experience if you were trying to remain static outside a central mass.  
[00:48:08] So let's just talk about static observers. I can discuss how these will get upgraded  
[00:48:12] for observers who are moving around. But for now, I'm just going to imagine  
[00:48:16] that you're trying to sit here at some fixed radius r away from the black hole.  
[00:48:26] The reason you don't fall in, maybe I'm lowering you down on a pulley.  
[00:48:32] You're just sitting here holding the pulley.  
[00:48:34] The question is, how strong a force do you need to stop you falling down?  
[00:48:38] You're abseiling down very slowly. You're static. What is the local  
[00:48:41] force of gravity that you experience? Or you can imagine that you're sitting  
[00:48:46] here, and the reason you're static is that you're firing a rocket very hard.  
[00:48:50] The question is, how much acceleration do you locally feel?  
[00:48:54] So by whatever mechanism, you're remaining static. What is the local force of gravity that you feel?  
[00:49:04] In Newtonian physics, you know what the answer to that question would be.  
[00:49:08] The force of gravity is GM/r², which is Newton's famous inverse-square law.  
[00:49:18] But this gets a correction from general relativity.  
[00:49:21] The correction is 1/√(1-2GM/(c²r)), this same 2GM/c² that we find all over the place.  
[00:49:38] What this tells you: first of all, if you're a very long way away from the black hole,  
[00:49:44] this here is essentially one. r is very big, and you get Newton's force law back again.  
[00:49:54] For the Earth, this is very small. As we discussed, it's down by a factor of 10⁻¹⁰,  
[00:50:04] and then you take the square root. So you don't really notice it,  
[00:50:08] but you can Taylor-expand this at large r, and you find that you get corrections.  
[00:50:13] You get an inverse-square law plus an inverse-cube law correction plus an  
[00:50:17] inverse-fourth law correction. You find that gravity at short  
[00:50:22] distances is stronger than it would have been in Newtonian physics.  
[00:50:26] This is the general relativity correction and it's making the gravitational field stronger.  
[00:50:33] You have to accelerate harder to not fall into the black hole.  
[00:50:37] In particular, once r is equal to 2GM/c², what's called the Schwarzschild radius,  
[00:50:44] you have to accelerate infinitely. The proper acceleration required to  
[00:50:50] not move in r goes to infinity. In fact, if we now convert this  
[00:50:58] Earth to a black hole, this is a very significant radius over here, 2GM/c².  
[00:51:07] It's called the event horizon. It's called the event horizon because  
[00:51:16] if you want to remain static outside the event horizon, further away from the event horizon,  
[00:51:21] you just need to accelerate with some finite velocity in order to remain static.  
[00:51:28] You need to have a finite gravitational field. But the gravitational field, as you approach  
[00:51:31] the event horizon, becomes infinite. So once you're at or beyond the event  
[00:51:35] horizon, it is impossible to remain static. You will inevitably get sucked into the black  
[00:51:39] hole no matter how hard you fire your rocket. Now, this is just a static formula.  
[00:51:44] You might imagine, "Okay, it's impossible to remain static closer than that,  
[00:51:49] but maybe I could avoid falling into the black hole by orbiting really, really fast.  
[00:51:54] If I orbit really fast, I have a huge centrifugal force that pushes me away from the black hole,  
[00:51:59] and I can stay out of the black hole that way." That actually doesn't work. The reason it  
[00:52:03] doesn't work is somewhat instructive for the way gravitational attraction  
[00:52:08] happens in general relativity. Of course, if you think about  
[00:52:11] the International Space Station, why doesn't it fall towards the Earth?  
[00:52:14] It is precisely the fact that it's orbiting. The fact that it's orbiting gives it a  
[00:52:19] centrifugal force that shoots the astronauts away from the Earth and precisely balances  
[00:52:23] the gravitational field on the astronauts, which is why they feel weightless there.  
[00:52:29] So orbital angular momentum, if you're a long way away from the black hole, helps you stay away  
[00:52:36] from the black hole, stops you falling in. There is this kind of sci-fi notion that  
[00:52:41] black holes just suck in everything around them. Not true. You are perfectly able to orbit around  
[00:52:46] a black hole if you're a long way away from it, just like you would orbit around any central mass.  
[00:52:51] You are not inevitably falling into the black hole.  
[00:52:54] You can orbit just fine. But orbiting stops helping  
[00:52:58] when you get too close to the black hole. We said that the event horizon is 2GM/c².  
[00:53:03] In fact, once you're already within 3GM/c², orbiting is counterproductive  
[00:53:09] if you're trying to stay away from the black hole. That's because there are two effects of orbiting.  
[00:53:15] One effect helps you stay away from the black hole.  
[00:53:17] That's the centrifugal effect. Orbital angular momentum pushes you away from  
[00:53:21] the black hole due to the centrifugal effect. It's not too hard to write down the version of  
[00:53:28] this formula that applies when you have angular momentum, and you would see that  
[00:53:31] pushing you away from the black hole. But there's another effect which drags  
[00:53:34] you towards the black hole, and that is the fact that in general relativity,  
[00:53:39] all energy gravitates, not just rest mass energy. Kinetic energy also gravitates. So the effect of  
[00:53:47] orbiting is that you have an additional pull down towards the black hole from the coupling between  
[00:53:58] the gravitational attraction between the mass of the black hole and your orbital angular energy.  
[00:54:04] When you're far away from the black hole, the centrifugal force is the more important term.  
[00:54:09] When you're close to the black hole, that coupling is the more important term.  
[00:54:14] In fact, once you get within 3GM, orbital angular momentum stops helping and starts hurting.  
[00:54:21] There are no ballistic orbits that go within 3GM and manage to escape again.  
[00:54:26] So that's formula number one. It tells you what the gravitational field is  
[00:54:31] a distance r away from a black hole. In particular, it shows you that once  
[00:54:37] you get to this critical radius, the gravitational field becomes infinite.  
[00:54:42] If you cross that, you must proceed to the center of the black hole,  
[00:54:45] no matter how hard you fire a rocket. That's called the event horizon.  
[00:54:49] At the event horizon, you are not yet dead. You are, however, doomed if you  
[00:54:53] cross the event horizon. You will never be able to escape,  
[00:54:55] not if you convert yourself to light and try to shoot yourself out, not if  
[00:54:58] you fire your rocket infinitely hard. The other place, of course, is r=0,  
[00:55:04] which is where you actually die. That's at the singularity, and we'll  
[00:55:08] describe that a little bit in a moment. In Newtonian physics, the gravitational  
[00:55:12] force only becomes infinite there. In general relativity, it becomes  
[00:55:16] infinite already at the event horizon if you try to resist the force of gravity.  
[00:55:21] That's formula number one. Now let's do formula number two.  
[00:55:27] All three formulas I'm going to write down are heavily related to each other.  
[00:55:32] They're really going to be reformulations of each other.  
[00:55:34] Formula number two asks about gravitational time dilation.  
[00:55:39] Let's again imagine that you're sitting here, Dwarkesh sitting here some radius  
[00:55:45] r away from the black hole. I'm sitting out here,  
[00:55:52] way off at infinity, just watching you. We're static relative to each other.  
[00:55:56] There's no relative motion. You're just suspended here by your pulley system.  
[00:56:01] The question is, how fast does your watch go relative to mine?  
[00:56:05] Of course, as far as you're concerned, your watch is ticking at one second per second.  
[00:56:10] As far as I'm concerned, my watch is ticking at one second per second.  
[00:56:12] But if I look at you, I see your watch as running slow.  
[00:56:18] If you look at me, you see my watch as running fast.  
[00:56:22] The second formula makes that quantitative. How much slower does your wristwatch—which  
[00:56:29] is closer to the black hole—run than mine? It says that the time interval, as measured by  
[00:56:35] your wristwatch, is given by the time interval as measured by my wristwatch a long way away,  
[00:56:47] times this exact same square root factor that's showing up all over the place:  
[00:56:51] the square root of 1-2GM/(rc²). This factor here is less than one.  
[00:57:02] So if I think one second has passed, you think less than one second has passed.  
[00:57:07] In other words, if I slowly lower you down towards the black hole—you hang out some finite distance  
[00:57:13] away from the black hole for what feels to you like a year, and then I raise you back up a long  
[00:57:20] way away from the black hole—you will return to a world that has aged a lot more than you have.  
[00:57:27] This formula makes that precise. I observe your wristwatch to be running slow.  
[00:57:34] You observe my wristwatch to be running fast. Time passes slower down here than it does up here.  
[00:57:42] This is a fact that has by now been extremely well observed experimentally.  
[00:57:46] In the 1950s, in the Harvard physics department, they put two atomic clocks  
[00:57:50] at two different heights in the building, and noticed the one that was higher was  
[00:57:57] running faster than the one that was lower. This is an effect that is now considerably  
[00:58:03] within the precision of, for example, GPS. It just has to subtract that effect, otherwise  
[00:58:08] everything would drift all over the place. GPS clocks that are sitting on the Earth's  
[00:58:13] surface are running slow compared to the atomic clocks that are in orbit sending out the signal.  
[00:58:22] You have to account for that difference and subtract it off in order to get an accurate read.  
[00:58:29] This is known as gravitational time dilation. Notice it's quite different from the relativistic  
[00:58:34] time dilation you see in special relativity, which is caused by two  
[00:58:37] objects being in motion relative to each other. Here, we're not in motion relative to each other.  
[00:58:41] We're both static. We're fixed. This is caused by us being at a different place  
[00:58:45] in the gravitational potential, you deeper in the gravitational potential than me.  
[00:58:49] So those are two different sources of time dilation, and they stack.  
[00:58:54] Let's say instead of being static here, you're in orbit.  
[00:58:58] You're far enough away that you can orbit the black hole.  
[00:59:02] How slow do I see you as moving? There are now two contributions,  
[00:59:06] both of which make you look slow relative to me. One contribution is the gravitational time  
[00:59:11] dilation given by this formula. A second contribution is the good  
[00:59:17] old special relativity correction where moving observers look like they're going  
[00:59:22] slow, and we'll have both of those effects. So you'll look like you're going even slower  
[00:59:27] than you would have done otherwise as you go around the black hole.  
[00:59:34] One thing that seems different between this and special relativity is that there's no symmetry.  
[00:59:38] In special relativity, both observers will feel that the other one is aging slower than they are,  
[00:59:43] because they're both moving relative to each other at the same rate,  
[00:59:47] and there's no true inertial path. But here, it actually does seem like  
[00:59:53] there's a global sense in which one is a more relevant inertial frame than the other one.  
[01:00:03] You're exactly right. In special relativity, if you and I are moving relative to each other,  
[01:00:06] I think your watch is moving slow, you think my watch is moving slow.  
[01:00:10] Neither of us is more correct than the other. The principle of relativity tells you that  
[01:00:13] both of our perspectives are equally valid. Here, both of our perspectives are not equally  
[01:00:18] valid, because there is not the symmetry that there was in special relativity.  
[01:00:22] In particular, the symmetry is broken by the black hole.  
[01:00:25] We both agree that you are deeper in the gravitational well than I am,  
[01:00:30] and your clock runs slower than mine does. You do not see my clock reciprocally running slow.  
[01:00:38] You, in fact, see me sped up. If you were observing me, you see  
[01:00:42] me living my life in fast-forward. So this is the second formula.  
[01:00:47] It says how fast our wristwatches move relative to each other.  
[01:00:51] Now let's imagine that you're here with your slow-moving wristwatch,  
[01:00:55] and you shine a light towards me. Let's say the light has a particular frequency.  
[01:01:02] You made it with a sodium transition, for example. As that light travels upwards, by the time  
[01:01:11] it reaches me, I'm going to think that it is lower frequency than you thought  
[01:01:16] it was when you sent it. Why? Because frequency is  
[01:01:19] about how rapidly it oscillates. I just think that everything you  
[01:01:26] do is moving slow relative to me. You think it's oscillating slower.  
[01:01:30] It has lower frequency, which means it gets shifted towards the red part of the spectrum.  
[01:01:35] The word that we use is redshift, gravitational redshift.  
[01:01:39] It's redshifted: lower frequency, and therefore less energy.  
[01:01:43] If you send one photon up, the energy of the photon is given by the frequency.  
[01:01:48] It'll arrive at me more redshifted and with lower energy than it had when it left you.  
[01:01:56] Conversely, if I am up here, and I send you a photon generated by the sodium transition,  
[01:02:04] as observed by you, by the time the light reaches you—you see me moving  
[01:02:09] in fast-forward—you think that it has a higher frequency than I thought it had when it left me.  
[01:02:16] It's moved towards the blue part of the spectrum. We say that it is blueshifted.  
[01:02:23] So this thought experiment tells you that knowing the exchange rate for how time passes at different  
[01:02:33] altitudes directly gives you the exchange rate for how much energy is worth at different altitudes.  
[01:02:41] If you try to send me some energy, by the time it reaches me, it's worth less to me than you  
[01:02:46] perceived it as being worth to you. The amount it's less by is going to  
[01:02:51] be precisely given by the same square root formula that's controlling everything else.  
[01:02:57] So that gives us our third equation. The third formula says: suppose that you,  
[01:03:03] Dwarkesh, have an object of mass, mc², sitting with you at this fixed radius down there.  
[01:03:10] How much energy, as measured by me a long way away from the black hole, is that worth to me?  
[01:03:18] Of course, if I had it with me, it would be worth mc² worth of energy.  
[01:03:22] But I don't have it with me. It's unfortunately sitting with  
[01:03:25] you deep in a gravitational potential. So it's worth less than mc² to me.  
[01:03:30] In fact, it's just the exact same formula. The amount of energy that it's worth to me,  
[01:03:34] by the time it reaches me, is GM/(rc²). There are a couple of ways to see that.  
[01:03:41] One is the way that we just said. Suppose you take your object of mass m.  
[01:03:47] It's just half an Avogadro's number of carbon atoms and half  
[01:03:53] an Avogadro's number of anti-carbon atoms. One way you could send me the energy is by  
[01:04:02] smashing them together, a violent explosion. You convert all of that energy to light and  
[01:04:06] you try to beam that light energy up to me. But what you find, precisely because of this  
[01:04:12] gravitational time dilation, is by the time it reaches me, I'm not getting mc² worth out.  
[01:04:17] I'm getting, by the argument we just gave, less than mc² worth out.  
[01:04:20] I'm getting 1-GM/(rc²) out. Mass down here suffers this redshifting as it  
[01:04:28] goes up and has less energy by the time it reaches infinity than it did to begin with.  
[01:04:33] There is another way that you could have got the energy to me, not by beaming it up as light,  
[01:04:37] but by just taking your mass object, attaching it to the pulley, and having me pull the object out.  
[01:04:46] By the time I've pulled it out, I've now got mc² sitting out here,  
[01:04:50] a long way away from the black hole. So I do have the full mc² worth of energy.  
[01:04:55] But to get it, I needed to pay. What I needed to pay was precisely  
[01:05:00] pulling it out of the gravitational potential. So from that way of thinking about it,  
[01:05:05] that's why I have less than mc² worth of energy left, because I had to pay to pull it out of  
[01:05:11] the potential in order to accrue that mass. So this formula tells you: if I have a brick  
[01:05:16] of mass, mc², sitting at some radius r away from the black hole, how much energy can I extract from  
[01:05:24] that brick if I'm a long way from the black hole? If we know that formula, then we can in fact  
[01:05:32] calculate exactly this formula: how much energy have I extracted from the  
[01:05:38] brick by lowering it down to a radius r? Well, we know the answer to that question.  
[01:05:43] The energy it started with is mc². The energy it now has is this.  
[01:05:50] So the energy I've extracted from the brick while slowly lowering it down using my pulley  
[01:05:55] system must be the energy I started with, mc², minus the energy it now has.  
[01:06:01] In other words, the fraction of the energy that I've extracted by lowering  
[01:06:07] it down to a radius r is mc² minus this, all divided by mc²: 1 - √(1 - 2GM/(c²r)).  
[01:06:27] This is the exactly correct answer for the fraction of the energy extracted.  
[01:06:31] It doesn't look exactly like this, because this is only correct in the Newtonian limit.  
[01:06:35] We derived this using Newtonian physics. This is exactly correct, not just in the  
[01:06:39] Newtonian limit, but all the way to where the effects of general relativity are important.  
[01:06:46] Now, if you're a very, very long way away from the black hole—r is much,  
[01:06:49] much bigger than 2GM/c²—then you can Taylor-expand this formula.  
[01:06:55] The first order term is just the old Newtonian formula.  
[01:06:58] It better be. It better be that the long-distance limit of general relativity recovers the Newtonian  
[01:07:03] physics that we originally discovered. But as you get closer and closer to the black  
[01:07:07] hole, this starts to deviate from the Newtonian answer, in a way that exactly is going to end up  
[01:07:13] resolving our original thought experiment to do with lowering a brick down towards a black hole.  
[01:07:17] So how much, then, looking at this formula, have I extracted from the  
[01:07:24] brick as I lower it down towards the black hole? If r equals infinity—if the brick's still a long  
[01:07:32] way from the black hole—then I've extracted 1-1=0. I haven't extracted any energy.  
[01:07:39] As I lower it closer and closer to the black hole, initially I just get the Newtonian formula.  
[01:07:46] So in fact, these are pretty close to correct in general relativity as well,  
[01:07:51] because the corrections are only going to start getting large when this term becomes order one,  
[01:07:56] and it's still very small here. So these are all essentially correct.  
[01:08:00] But once I get closer and closer to the black hole, they stop being correct.  
[01:08:04] What I see is that as r approaches the black hole event horizon,  
[01:08:10] as this formula goes to zero, I have extracted exactly all of the energy from the brick.  
[01:08:18] So I start off with a brick a very, very long way from the black hole, attach it to a rope, slowly  
[01:08:25] lower the brick down towards the event horizon. Of course, I can't lower it past the event  
[01:08:30] horizon, otherwise I'll lose control of the brick. But I lower it right above the event horizon—the  
[01:08:35] last possible place I can lower it to—and then just let go of it with zero velocity.  
[01:08:39] The brick falls into the black hole and I have extracted the entire mc² that used to  
[01:08:45] be in the brick in my pulley system out there. So it exactly resolves this question we had.  
[01:08:52] Is it possible to extract more than mc² from the brick?  
[01:08:55] No. Is it possible to extract the full mc² from the brick using a black hole?  
[01:09:01] Yes, it is. That's actually pretty neat, and why people talk about  
[01:09:06] using black holes as power plants. Most power plants today operate  
[01:09:12] by burning chemical energy. That is not very efficient.  
[01:09:16] You have to pay a factor of 10⁻¹⁰, because chemical bonds are super  
[01:09:20] weak compared to the rest masses of objects. You're really only extracting a tiny fraction of  
[01:09:25] the rest mass of the fuel that you're considering. You can level up from there by going to nuclear  
[01:09:31] energy, which instead of dealing with the feeble electromagnetic bonds between atoms, starts to  
[01:09:39] concern itself with the nuclear forces between the protons and the neutrons within the nucleus.  
[01:09:45] So you can go up from about 10⁻¹⁰ to about 10⁻³ for fission, or 10⁻² for fusion.  
[01:09:51] But that's about as good as you can go, even with fission and fusion.  
[01:09:55] Because even though you can extract energy from the strong nuclear force,  
[01:10:00] neither fission nor fusion changes the total number of protons plus neutrons in your process.  
[01:10:05] The bulk of the energy—99% of the energy—is stored not in the electromagnetic interaction,  
[01:10:10] not in the strong interaction, but in the rest mass energy of the protons and  
[01:10:15] neutrons, something that neither chemical reactions nor nuclear reactions can touch.  
[01:10:20] But gravity can touch them. If I start off with a mass object of m,  
[01:10:26] I can extract, up to quantum corrections, essentially 100%  
[01:10:31] of the rest mass energy that I've gone in with. It is the most efficient possible power plant,  
[01:10:35] because by building an apparatus like this, in principle, I could extract 100%  
[01:10:40] of the energy of whatever I started with. I intuitively get how energy equals mass.  
[01:10:46] There's these chemical bonds. Those get dissolved, they release energy.  
[01:10:50] The thing weighs less if those bonds are released. I even get that if the bonds between the protons  
[01:10:55] and the neutrons are broken, that releases energy and makes the thing have less mass.  
[01:11:00] But if something with protons and neutrons is just slightly above the event horizon,  
[01:11:07] is the interpretation that those protons and neutrons stop existing right at that point?  
[01:11:12] What does it even mean for them to have 1% or 2% or 5% of their original mass?  
[01:11:19] That's a great question. It really becomes relevant once you turn on quantum mechanics,  
[01:11:24] which is beyond the scope of today's discussion. Classically, the black hole  
[01:11:28] just sits there forever. So you can just say, "Well,  
[01:11:30] what happened to the protons and neutrons?" You say, "Well, they now live  
[01:11:32] inside the black hole." The number of protons plus neutrons  
[01:11:37] is still conserved out there in the universe. It's just you need to assign what's called a  
[01:11:40] nucleon number to the black hole itself. That's fine as far as it goes classically.  
[01:11:47] Quantum mechanically—way beyond the scope of today's lecture—Hawking and Bekenstein  
[01:11:51] discovered that black holes radiate away energy, and eventually the black hole will be gone.  
[01:11:56] All of the energy, if you calculate it, ends up in gravitons and photons and perhaps some neutrinos.  
[01:12:02] None of it, or almost none of it, ends up in protons and neutrons.  
[01:12:05] So it is a very interesting fact, once you turn on quantum gravity,  
[01:12:09] that black holes eat nucleon number. This thing that seems like it's conserved,  
[01:12:14] at least perturbatively, both by electromagnetism and by the nuclear forces,  
[01:12:19] ends up being eaten by gravity. People like to promote this—we're  
[01:12:24] talking about quantum gravity now—to a general principle that quantum gravity  
[01:12:29] doesn't respect any global symmetries. It doesn't respect nucleon number symmetry.  
[01:12:34] It doesn't respect any of these symmetries. That's a whole other can of worms  
[01:12:38] that we can open some other day. I recently wrote this blog post where I  
[01:12:41] speculated that sample efficiency during training actually hasn’t improved that much over the last  
[01:12:46] few years, and rather, we’ve just dramatically improved and widened the data distribution.  
[01:12:51] I was having dinner with friends recently, and then I had this idea of how you could get some  
[01:12:55] empirical information on this question. There’s this nanoGPT speedrun where people compete to  
[01:12:59] train Karpathy’s GPT-2 baseline to a fixed loss with less and less compute. The training data has  
[01:13:05] frozen, so I wondered if the loss curves over time of each record could tell you  
[01:13:09] roughly how fast sample efficiency is improving. So I pulled out my phone, dumped this idea into  
[01:13:14] a voice note in the Cursor app, and went back to dinner. Then I got a notification about 15 minutes  
[01:13:18] later: the Cursor agent had cloned the modded nanoGPT repo, analyzed all the loss curves for all  
[01:13:23] the records, and estimated that sample efficiency had been improving about 2–5x every single year.  
[01:13:29] Of course, this is very naive and circumstantial evidence, but it inspired me to start writing a  
[01:13:33] full post with a friend where we investigate this question using many different methods.  
[01:13:38] The friction really mattered here. The idea would have just floated away if I  
[01:13:41] wasn’t able to kick off the investigation right then and there with the Cursor app.  
[01:13:44] If you want to try Cursor’s iOS app, go to cursor.com/Dwarkesh.  
[01:13:50] Okay, Adam. I like to think on this podcast we impart not only  
[01:13:52] theoretical but practical knowledge as well. So suppose one learns all these equations,  
[01:13:58] but then finds themself in the unfortunate position of falling into a black hole.  
[01:14:02] What would they see? Great question. There are actually  
[01:14:07] two different perspectives you could take. One is the perspective of me watching you  
[01:14:11] falling into the black hole. The other is the perspective  
[01:14:15] of you falling into the black hole. Those two perspectives are consistent with  
[01:14:19] each other but interestingly different, so maybe I should describe them both.  
[01:14:22] First, let's ask the question: what do I see as you fall into the black hole?  
[01:14:28] This is how hard you need to fire your rocket to not fall into the black  
[01:14:32] hole but you’re not going to do this. You're just going to sit here a long,  
[01:14:35] long way away from the black hole, turn off your rocket, and accept what comes.  
[01:14:40] What comes is you'll slowly accelerate towards the black hole, at a rate first given by the Newtonian  
[01:14:45] formula and then, when you get close to the black hole, start picking up general relativity  
[01:14:52] corrections to the Newtonian inverse-square law. What I will see as I watch you fall towards the  
[01:14:57] black hole is that first you'll go faster and faster and faster as you fall down the  
[01:15:02] gravitational potential of the black hole. But then something strange will happen.  
[01:15:09] You'll stop going faster, and you'll start going slower.  
[01:15:12] The reason you're going slower is that, as I watch you, you start to get gravitational  
[01:15:18] time dilation as you fall down, and I start to see your clock running slow.  
[01:15:24] The static formula doesn't apply exactly since you're moving, but the formula has  
[01:15:31] the same effect, which is that as you get closer and closer to the black hole, your wristwatch  
[01:15:36] starts running slower and slower and slower. In fact, if you do the appropriate integral,  
[01:15:40] I never see you cross the event horizon. I just see you getting closer and closer  
[01:15:43] to the event horizon, but slowing and slowing as you approach it.  
[01:15:50] As I watch you—I'm presumably using light to watch you—that light gets more and more redshifted.  
[01:15:55] The wavelength gets longer and longer, and the longer the wavelength of light,  
[01:15:59] the harder it is to even really see you. You start getting delocalized by the  
[01:16:03] wavelength of the light, and eventually I just stop seeing you entirely.  
[01:16:07] There's a final photon that you emit, and then you just fade to black, fade through red to black.  
[01:16:13] I never see you cross the event horizon. This was noticed by people in the early days  
[01:16:20] of general relativity and greatly confused them. They started to think that you would experience  
[01:16:26] something funny yourself as you fell across the event horizon.  
[01:16:29] That is not true. If I instead adopt your perspective, from your point of  
[01:16:35] view, your clock isn't running slow. It's running at one second per second.  
[01:16:38] If you look back at me, there's some funny stuff going on to do with me running fast perhaps.  
[01:16:42] But as far as you're concerned, everything's totally normal.  
[01:16:46] You accelerate towards the black hole, getting faster and faster as you approach it.  
[01:16:51] You just sail across the event horizon totally as normal.  
[01:16:55] The event horizon is not a particularly violent place for you.  
[01:16:58] You can calculate the tidal forces as you approach and then cross the event horizon.  
[01:17:06] They're not particularly big, or rather, for large black holes, they're not particularly big.  
[01:17:09] For a solar mass black hole, they would be pretty big and would be pretty painful.  
[01:17:14] You'd find that your feet are being attracted to the black hole much more  
[01:17:18] vigorously than your head is, because they're closer, and you end up getting stretched.  
[01:17:22] But if I take a big enough black hole, you wouldn't notice anything  
[01:17:25] funny happening whatsoever. The bigger the black hole,  
[01:17:31] the smaller the tidal effects. If I took a black hole the mass  
[01:17:36] of the galaxy, you'd be basically fine as you cross the event horizon.  
[01:17:39] If I took an even bigger black hole than that, you could live out your entire life  
[01:17:43] having crossed the event horizon, before you hit the singularity, which is fatal.  
[01:17:51] When you cross the event horizon, you are doomed. You are doomed because once you cross the event  
[01:17:58] horizon, you must proceed to the singularity. There's no way you can fire a rocket to stop  
[01:18:02] yourself hitting the singularity. You are doomed, but you are not dead.  
[01:18:07] You are only for sure dead once you hit the singularity and get spaghettified,  
[01:18:12] mangled by the tidal forces. But for a large enough black hole,  
[01:18:15] you can be doomed and not even know it. The event horizon is really a not  
[01:18:21] locally measurable quantity. It is a teleological fact.  
[01:18:24] It says that once you have crossed the event horizon, you must proceed to the singularity.  
[01:18:29] But it can take a long time to get there for a large enough black hole.  
[01:18:33] In principle, for a black hole that was many light centuries across,  
[01:18:41] you could live out your entire life. You could have descendants,  
[01:18:43] all of whom live inside the black hole. Only once you really approach the singularity  
[01:18:48] do the tidal forces get strong and kill you. As you were saying, GR explains  
[01:18:54] or predicts a lot of phenomena. Some we think are correct,  
[01:18:57] some we don't know are correct. Why do we think black holes  
[01:19:00] are correct but not wormholes? That's a great question. People  
[01:19:03] did not believe it to begin with. Schwarzschild wrote down his  
[01:19:05] solution almost immediately after Einstein wrote his field equations.  
[01:19:08] People thought that that equation was sick in some way, that it was a measure  
[01:19:11] zero thing that would never happen. It was some mathematical monstrosity,  
[01:19:15] but it was impossible to make black holes naturally in the real universe.  
[01:19:20] They were wrong, because black holes do exist. We're extremely confident now. There were  
[01:19:25] theoretical developments, and there was experimental evidence that black holes exist.  
[01:19:29] The biggest theoretical development was Penrose, and then later Hawking and Penrose—for which he  
[01:19:34] won the Nobel Prize—who showed theoretically that the formation of black holes is a generic  
[01:19:40] feature of general relativity. It's not just some sick thing that  
[01:19:44] happens if you fine-tune the initial conditions. If you start off with generic initial conditions,  
[01:19:49] the development of black holes is a generic feature.  
[01:19:52] That was a huge development. Then there was the experimental side.  
[01:19:55] The pieces of experimental evidence we have for black holes are now huge.  
[01:20:00] They did not exist in Einstein's day, and for 50 years after Einstein,  
[01:20:03] people were extremely confused about black holes and thought they didn't exist.  
[01:20:06] But there are numerous pieces of evidence. I think the most visually appealing piece of  
[01:20:10] evidence is just observing the center of our galaxy.  
[01:20:16] If you look at the center of the galaxy—spoiler alert—there is a black hole there.  
[01:20:21] We call it Sagittarius A*. It’s a huge black hole, weighing  
[01:20:24] many millions of times the mass of the sun. You can't see the black hole directly,  
[01:20:31] because it's black. What you can see is the stars around it.  
[01:20:35] If you watch these stars over the course of decades—and we now have a number of decades of  
[01:20:40] observations of them—you will see the stars not moving along what we would call straight lines,  
[01:20:46] but instead moving in nice little ellipses, or precessing ellipses.  
[01:20:52] Those ellipses look like they are orbiting something.  
[01:20:56] You cannot see the something, but you can see the stars that are orbiting it.  
[01:21:01] You can calculate how big it is, how massive it is.  
[01:21:05] What you find is that it's very massive indeed, and it's also very small indeed.  
[01:21:09] You know it's small because the stars get super close to it but don't seem to collide with it.  
[01:21:14] So by tracing these orbits, you can tell that there is something super heavy,  
[01:21:19] super dark, and super compact at the center of the galaxy.  
[01:21:22] That is Sagittarius A*, the black hole at the center of our galaxy.  
[01:21:26] That's one compelling piece of evidence. Another piece of compelling evidence:  
[01:21:30] about a decade ago, we not only saw black holes, we felt them.  
[01:21:34] LIGO is this huge laser interferometer that we built at a number of different sites, that is  
[01:21:42] super attuned to vibrations in spacetime itself. There's a famous event pretty much immediately  
[01:21:48] after we turned it on in late 2015, where we felt spacetime shaking.  
[01:21:54] You knew it was spacetime shaking, not just the Earth shaking, because we had  
[01:21:58] a bunch of these detectors—then two, now four—at different points on the Earth,  
[01:22:05] and they all shook in exactly the same way. So it couldn't just be explained by a truck  
[01:22:09] passing one and not the other, or a seismic event on one and not the other.  
[01:22:12] They all shook in exactly the same way, and we were able to back-calculate that  
[01:22:17] the thing causing them to shake was the collision of two ginormous black holes.  
[01:22:21] Two black holes, both of which weighed about 30 times as much as the sun, on the other side of  
[01:22:25] the universe, about 1.6 billion light-years away. That collision happened about 1.6 billion years  
[01:22:32] ago, and just happened to reach the Earth within weeks of us turning on the LIGO detectors.  
[01:22:37] We've now felt thousands of such shakings corresponding to thousands of black hole mergers.  
[01:22:44] And then there's more evidence. Later, we had what's called the Event Horizon  
[01:22:51] Telescope, which is a ginormous conglomeration of radio telescopes all over the Earth,  
[01:22:55] that were able to look very closely at the black hole at the center of our galaxy, Sagittarius A*,  
[01:23:00] and the even bigger black hole at the center of our neighboring galaxy, and see, very faintly, the  
[01:23:08] radio emissions of matter falling into these black holes, which shines super brightly as it does so.  
[01:23:16] So we felt them, we've seen them, and we've seen their gravitational effects on orbiting stars.  
[01:23:22] We're extremely confident at this stage that black holes exist.  
[01:23:26] It's so beautiful that not only can a single mind come up with this theory, but the theory has so  
[01:23:29] much reach, and that we can come up with the machinery to evaluate and perturb and understand  
[01:23:36] its implications in so many different wild ways. It's crazy the number of degrees of freedom,  
[01:23:43] the number of orders of magnitude that it covers. You first start thinking about it by doing thought  
[01:23:49] experiments to do with jumping up and down in elevators, and then it reaches out to describe  
[01:23:55] the orbit of Mercury and detectable perturbations of orbital dynamics within the Solar System,  
[01:24:00] and then the bending of light, and then it describes the rotation of the entire galaxy,  
[01:24:06] and then it describes the expansion and potential fate of the entire universe.  
[01:24:10] That's many orders of magnitude indeed, and it's pretty impressive that it  
[01:24:14] was the work of almost a single mind. Frankly, our universe should be honored  
[01:24:19] to be described by such a beautiful theory. Can you tell the story of how GR went from  
[01:24:23] a theory that Einstein had to something that the world came to believe is true?  
[01:24:28] That would be the bending of light. There were known anomalies with Newton's  
[01:24:32] physics beforehand, like we couldn't get the orbit of Mercury exactly right.  
[01:24:38] One of the very nice early tests of general relativity is that it did  
[01:24:42] get the orbit of Mercury exactly right. So that was a pretty good confirmation.  
[01:24:46] But at the same time, that's not quite so satisfying because it was a number that's  
[01:24:49] already known, as opposed to one where you invent a theory and then it correctly predicts.  
[01:24:53] It's considered more impressive if you get the right answer without knowing  
[01:24:58] what the right answer is in advance. So that would be the bending of light.  
[01:25:01] Certainly, historically, that was the most influential.  
[01:25:05] According to general relativity, all energy gravitates and all energy is affected by gravity.  
[01:25:12] So light, as it's passing a massive object like the Sun, will get bent in the direction  
[01:25:17] of the Sun. Actually,  
[01:25:18] the same will happen in Newtonian physics. Suppose you have a particle going along.  
[01:25:27] You know how much it gets bent as it passes the Sun, depending on  
[01:25:30] its impact parameter, but also its velocity. The faster it's going, the less it gets bent.  
[01:25:34] So you just take that Newtonian formula, plug in velocity equal to speed of light,  
[01:25:39] and see what answer you get. You can get a certain amount  
[01:25:41] of bending through Newtonian physics. In general relativity, you can do the  
[01:25:46] same calculation, and you actually get double the Newtonian answer.  
[01:25:51] The slightly strange history of it. Before he had finished writing down  
[01:25:56] general relativity, Einstein had a prediction based on his understanding of the equivalence  
[01:26:05] principle for what this answer should be. He wrote down the answer, and then in  
[01:26:09] response to him and a number of other people being interested in this, people were sending  
[01:26:13] out expeditions to go and try and measure it. I think the very first thing that he did was he  
[01:26:17] phoned up the observatory and said, "Can you look at distant stars behind the Sun and measure how  
[01:26:26] light bends as it passes the Sun?" This was the true theorist move,  
[01:26:30] because I think the director of the Mount Wilson Observatory said, "Absolutely not.  
[01:26:35] We cannot do that. If you point a telescope at the Sun, you'll go blind.  
[01:26:37] If you point it just next to the Sun, you'll just get washed out by the corona  
[01:26:40] of the Sun and you won't see anything." Except there's one time when you won't get  
[01:26:44] washed out by the Sun, and that's during a total solar eclipse, when the Moon blocks the Sun and  
[01:26:50] you're able to see stars very close to the Sun and measure the bending of the light behind them.  
[01:26:55] So during the 1910s, there were a whole bunch of expeditions  
[01:26:59] sent to measure the deflection of light. They'd park out in the path of totality and look  
[01:27:08] through telescopes at the stars right next to the Sun and see if they moved in the sky,  
[01:27:13] and if they moved, how much they moved. I think the first one was in 1911.  
[01:27:18] They went to Argentina for an eclipse, and everything's set up.  
[01:27:23] This is the problem with this thing. You get there, all the way to Argentina,  
[01:27:27] a very long way in those days, and then it's just washed out by the clouds.  
[01:27:31] You don't see anything, and it's very frustrating. The next one was a German expedition sponsored by  
[01:27:41] the arms manufacturer Krupp, who went to the Crimea and tried to measure it there.  
[01:27:47] Just before the solar eclipse happens, World War I breaks out, and now Germany and Russia are at war.  
[01:27:54] They're all arrested and turned for the rest of the war, and so that also fails.  
[01:28:00] It actually turns out to be a good thing for Einstein that they all failed.  
[01:28:03] It turned out that Einstein's original equivalence principle argument—before he had full general  
[01:28:07] relativity—was wrong and led him to predict that the bending of light in general relativity would  
[01:28:17] be the same as it was in Newtonian physics. During the war, while everything is shut  
[01:28:21] down and no one is thinking about eclipse expeditions, he corrects this mistake and  
[01:28:26] comes up with a new prediction that actually it'll be double the Newtonian prediction.  
[01:28:30] And then in 1919, Sir Arthur Eddington launches a British expedition to go and  
[01:28:35] observe the eclipses all over the world and successfully comes back and declares that  
[01:28:41] indeed it was the Einstein prediction. It was double the Newtonian prediction.  
[01:28:47] That's really what launches Einstein as a global celebrity.  
[01:28:50] This British experiment confirming a German-origin theory was part of the post-war reconciliation,  
[01:28:58] and Einstein had figured out everything. That is, I'd say, the point at which general  
[01:29:04] relativity became the consensus view, and people were super convinced by this very impressive test.  
[01:29:10] Nowadays, we've done hugely more tests than that, very precise orbital dynamics.  
[01:29:16] You can see it in the orbit of Mercury and indeed even in the other planets.  
[01:29:20] You can just measure the redshifting of light as it goes, the gravitational  
[01:29:25] effect on the propagation of light or the energy of light, all over the place.  
[01:29:28] But historically, that was the most impressive confirmation of general relativity.  
[01:29:33] One question you could ask is, we are maybe spending, as a society,  
[01:29:37] billions, maybe tens of billions of dollars on building these huge physics experiments.  
[01:29:42] If you look at maybe the most beautiful, the most important theory of physics ever conjured,  
[01:29:49] it seems like a guy who's just thinking in a cave. It seems like the empirical basis for that theory  
[01:29:53] is maybe knowing that light has a speed, and maybe you need to measure G experimentally.  
[01:29:57] Not really. G is a free parameter in general relativity.  
[01:30:01] It's not required. You're right, the empirical basis is pretty thin.  
[01:30:07] You don't need much, and theoretical physicists are pretty cheap.  
[01:30:12] There's a great temptation. Why don't we just spend it all on theoretical physicists and  
[01:30:16] not build these vastly expensive experiments? Well, these AI companies are really increasing  
[01:30:22] the demand curve for theoretical physicists. That's right, not so cheap anymore.  
[01:30:28] But how far can that get you? I would say that general relativity  
[01:30:31] is perhaps one extreme of that. That is not how it usually  
[01:30:37] works in the history of physics. This really is closer to some Ayn Rand hero  
[01:30:45] just sitting alone, the product of a single mind. He got a lot of help in various ways,  
[01:30:50] but it really was a singular vision that he pursued for years.  
[01:30:57] He wrote it down, and a lot of people were very impressed almost immediately.  
[01:31:01] It did require launching a somewhat expensive eclipse expedition to go  
[01:31:06] confirm it before he really achieved global celebrity and most people were sold on it.  
[01:31:11] But it's perhaps one of the most extreme examples of this, where somebody just sits down and thinks  
[01:31:18] very hard and writes down a true theory. In some sense, physics has been  
[01:31:23] chasing that high ever since. People love that romantic vision  
[01:31:27] of themselves just sitting down with very few empirical insights and thinking very,  
[01:31:32] very hard and doing thought experiments. It's typically not worked out quite as well  
[01:31:37] for everybody else as it worked out for Einstein. In fact, it didn't even work out that well for  
[01:31:41] Einstein in the later part of his career. How far could you get just by thinking?  
[01:31:48] What do you need to do general relativity? You need the finiteness of the speed of light.  
[01:31:52] You need to convince yourself not just that the speed of light is finite,  
[01:31:55] but that there's the symmetry that protects that, which Einstein came up with in special relativity.  
[01:32:01] Then you probably want the equivalence principle: it's an empirical fact that  
[01:32:06] the inertial mass and the gravitational mass are the same for everything.  
[01:32:09] But that's pretty sparse. From just those two things…  
[01:32:13] There's still a few options. But if you have lots and lots  
[01:32:16] of large language models and there's only a limited number of options, you can just explore  
[01:32:21] the entire tree and say, "Okay, focus on this. The equivalence principle is something that's  
[01:32:26] super significant, and this other thing. Now abandon simultaneity and see how  
[01:32:31] far that takes you." There's only a finite  
[01:32:33] number of things to explore there. I think they got very, very lucky  
[01:32:39] with general relativity, that it's quite so powerful under those circumstances.  
[01:32:43] But if you just had lots and lots of Einsteins and you gave each of them various options,  
[01:32:50] you could presumably see them in parallel. At the frontiers of physics today,  
[01:32:54] in your experience, does it feel like if you just have millions of them running autonomously  
[01:32:58] you could have enormous discoveries, or are we in a different era now, and really  
[01:33:06] there's limited usefulness of that parallelism? I think there is usefulness.  
[01:33:09] I do think that different parts of science have different branching fractions, and how  
[01:33:14] much experiment you need to cut off that branch. I talked about chasing the high of Einstein.  
[01:33:22] Arguably, string theory has really been going all in on that.  
[01:33:26] Einstein's theory is just general relativity. There's also quantum mechanics. Trying to marry  
[01:33:30] those two in a consistent way—which general relativity doesn't do at all,  
[01:33:34] there's no quantum mechanics in general relativity—has motivated a lot of people.  
[01:33:39] The problem is that in order to see that in experiments, if you just do the dimensional  
[01:33:45] analysis, you need ginormous particle colliders, absolutely galactic-sized particle colliders.  
[01:33:48] It's just very hard to see any of that stuff. But that doesn't stop people.  
[01:33:54] I mean, it stopped many people, but many people didn't stop and keep trying to do it.  
[01:33:58] So there you just have to hope that it works out sort of like it did with general relativity,  
[01:34:05] where just by thinking very, very hard with minimal input from experiment,  
[01:34:10] you can feel your way to the right answer. For that to be true, the tool you have at  
[01:34:20] your disposal is mathematical consistency and whether it reduces correctly in the known limits.  
[01:34:24] So you better hope that there's only one or a very small number of possible consistent  
[01:34:30] theories if you were going to do that. If it turns out that there's an unlimited  
[01:34:35] number of consistent theories, you're never going to feel your way to the correct answer,  
[01:34:39] because they're all consistent, and the only tool you have is consistency,  
[01:34:42] and perhaps some notion of aesthetics. But if there's only a few, then maybe  
[01:34:47] you could do it all the way. So string theory has kind  
[01:34:49] of gone all in on that, I would say. Trying, with minimal experimental input,  
[01:34:54] believing that there's only one consistent theory of gravity and that just by doing sufficient  
[01:34:57] consistency checks you can find it. For other examples it's much harder.  
[01:35:04] In condensed matter physics, often you simply need to go and do an  
[01:35:08] experiment to find out which one is correct. Whenever our future AI civilization does come  
[01:35:13] up with more and more unified theories of physics, or deeper theories that make better predictions,  
[01:35:18] do you think that humans will be able to keep up? Once this step is taken, will we actually be  
[01:35:27] in a position to understand what our AI civilization understands?  
[01:35:31] I don't know that we're going to be able to keep up entirely, but I think we'll keep up much better  
[01:35:36] than pessimistic forecasts would suggest. Let's take mathematics as a  
[01:35:41] simpler example than physics. Many mathematicians are worried that these  
[01:35:47] LLMs are just going to turn into proof machines. Terry Tao has this phrase, "indigestion", he uses,  
[01:35:53] in which these LLMs will produce billion-line inscrutable Lean code that will serve as a  
[01:36:01] certificate that a particular theorem is true without providing any insight as to  
[01:36:05] why that might be true. Wouldn't that be a  
[01:36:09] depressing world, say the mathematicians. I think that is a possible future, but I actually  
[01:36:13] don't find that to be a very likely future. Because as well as being superhuman provers,  
[01:36:20] we also expect these large language models to be superhuman explainers.  
[01:36:24] Maybe they'll do the exact opposite of that. Maybe they'll take proofs that are very hard  
[01:36:29] to understand, and by doggedly trying and trying and trying, they will be able to come  
[01:36:34] up with ways that are human comprehensible. They will take proofs that are difficult to  
[01:36:41] understand and make them easy to understand. I think the empirical evidence, it's early days,  
[01:36:46] but it's pretty supportive of that more positive vision.  
[01:36:52] There was an Erdős problem that was proved a few months ago now, and it  
[01:36:57] wasn't just an incomprehensible set of Lean. In fact, it wasn't even proved in Lean at all.  
[01:37:00] It was proved informally. There was a follow-up paper by some human mathematicians that took these  
[01:37:05] new, human interpretable ideas that the machine had come up with to prove this Erdős conjecture,  
[01:37:10] and used them to prove new theorems. So that was the exact opposite of that case.  
[01:37:16] It came up with a very human interpretable idea, and then humans were able to fully comprehend it,  
[01:37:22] comprehend it so well they were able to deploy it in a new scenario.  
[01:37:26] We've seen that throughout. The unit distance conjecture, I think, is a good example here for  
[01:37:30] a number of the themes you've been discussing. One is that it's totally comprehensible,  
[01:37:35] the disproof of the unit distance conjecture that it came up with.  
[01:37:41] To you, perhaps. To some mathematicians. I'm not a mathematician.  
[01:37:44] Perhaps the reason that humans haven't disproved the unit distance conjecture is because they  
[01:37:50] erroneously believe the conjecture to be true. The good thing about large language models is  
[01:37:54] that they're willing to push through that barrier and just waste their time, as a  
[01:37:58] human would understand it, trying to disprove a presumed true conjecture and reach the other end.  
[01:38:04] So that's another aspect of large language models that makes me pretty optimistic.  
[01:38:08] They just have extreme patience, even for doing things that perhaps  
[01:38:11] look like a low probability of success. Adam, thanks so much for coming back on  
[01:38:15] and doing this while you could be building superintelligence.  
[01:38:19] You're explaining 100-year-old physics, but it was very interesting.  
[01:38:22] It's a super fun subject. I'm super happy to share it.  
