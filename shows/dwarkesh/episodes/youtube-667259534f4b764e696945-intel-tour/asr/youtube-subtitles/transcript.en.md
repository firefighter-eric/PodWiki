# What will computer chips look like in 2045?

[00:00:00] There’s never been as big a shock to the semiconductor industry  
[00:00:03] as the current surge in demand from AI. AI is driving incredible computing demand.  
[00:00:09] Easily 40-50% above our maximum capacity, which I’ve never seen before.  
[00:00:13] Progress in AI has been driven by exponentially increasing compute.  
[00:00:17] To sustain that progress, foundries like Intel will need to manufacture far more  
[00:00:21] leading-edge compute, both by producing more chips and by improving what each chip can do.  
[00:00:26] But the production of these chips is bottlenecked by tools that Intel buys from their suppliers.  
[00:00:31] Most famously, ASML’s EUV machines. If they don’t have the equipment,  
[00:00:34] they can’t make the chips here. I spent two days touring Intel’s fabs to  
[00:00:38] prepare for these interviews with its leadership. I wanted to understand what it takes to  
[00:00:42] manufacture the world’s most advanced chips and how hardware is shaping the future of AI.  
[00:00:47] I’m joined by Chris Auth, who leads development of all the processes  
[00:00:51] that are currently under manufacturing. The thing I want to understand in more  
[00:00:54] concrete detail is how the development of a new process actually happens.  
[00:01:00] If 14A is going to come out in three years or two years from now,  
[00:01:03] what is happening from now till then? I want you to walk me through as much  
[00:01:07] detail as you can, everything from the level of “how is the yield improving?” to what  
[00:01:12] kind of telemetry you guys look at? What kind of experiments do you guys run?  
[00:01:15] I want to understand what is going to happen over the next two years as concretely as possible.  
[00:01:22] 14A has been in development for about three-plus years at this stage,  
[00:01:28] so quite a bit of pre-work has been done to get it to the stage that it’s at right now.  
[00:01:32] Right now, we’re getting very close to where we’re finalizing the process.  
[00:01:35] We’re finalizing the tool sets that it will be manufactured on,  
[00:01:38] and we’re working on the fine-tuning of each of the process steps.  
[00:01:42] There are about 2,000 steps in the factory that you have to go do.  
[00:01:46] You need to do really intricate work at each one of those to make sure it’s fine-tuned,  
[00:01:51] it can go into manufacturing, it can run thousands of wafers a week on this process,  
[00:01:55] and it can be repeatable every single time. Right now, you might have a certain yield.  
[00:02:00] Walk me through how that increases month over month.  
[00:02:03] There’s a line running at 14A. What happens from now till next  
[00:02:07] month that will result in the yield changing? How do you identify where the defects are?  
[00:02:10] How do you fix that? There’s a constant  
[00:02:13] process that we go through in identifying defects. There are two main ways that we’ll identify them.  
[00:02:18] One is we have inline metrology. We have tools that will look at  
[00:02:22] the wafers and say, “Ah, there’s a defect there, there’s a defect there, there’s a defect there.”  
[00:02:26] Then also at the end of line, either electrical test or we sort and see where the fails are.  
[00:02:32] We will identify failures, and then we will get analysis on those failures.  
[00:02:36] We’ll cross-section it. You were in the TEM lab yesterday,  
[00:02:40] and you saw how you can get cross-sections. You’ll get a cross-section of a defect,  
[00:02:43] and from that, you’ll be able to say, “Oh, that defect is between these layers, so it  
[00:02:47] must have come from this section of the flow. Oh, we have inline metrology in that section,  
[00:02:53] which has identified defects. Those are the defects we need to go after.”  
[00:02:57] What we’ve learned is that you don’t want to do too much innovation in one node,  
[00:03:02] because the more innovation that you do, the more complex it becomes.  
[00:03:05] While you’ll be able to get that to work, you need to hit a certain schedule, and that’s the  
[00:03:10] schedule that your customer ultimately wants. Having that predictable schedule is a key piece.  
[00:03:14] You’ve got to figure out how much innovation you can put in in order to meet the customer’s  
[00:03:20] requirements in the timeline that they need it. Intel learned how costly that tradeoff can  
[00:03:24] be with delays to its 10 nanometer node, whose original target launch date was 2016,  
[00:03:28] but which didn’t begin manufacturing until 2018. Usually Intel has been the keeper of Moore’s Law,  
[00:03:34] a new cadence of manufacturing every two years, but their last  
[00:03:38] set of products slipped almost four years. Intel today having its worst day in four months,  
[00:03:44] the stock now down more than 15%. I also want to point out Taiwan  
[00:03:49] Semiconductor up 13% off of Intel’s bad news. Walk me through what lessons you think Intel  
[00:03:57] has learned from 10 nanometer. Ten nanometer was a good example  
[00:04:01] of where we had very aggressive targets. We were doing what was called hyperscaling  
[00:04:06] at the time, so we were scaling much faster than what had been historically done.  
[00:04:10] In order to do that, we came up with all sorts of innovative ideas on how we could achieve that  
[00:04:18] without new tools, because the tools weren’t ready.  
[00:04:23] That put a lot of burden on the process and a lot of burden on the engineers.  
[00:04:27] Now, at the end of the day, 10 nanometer is a great technology.  
[00:04:30] It has world-class yield, it has world-class performance, it has world-class cost,  
[00:04:34] but it took us longer to do that than what we would have liked.  
[00:04:38] So we’ve tried to take that learning into future technology nodes and say, “Hey, we  
[00:04:43] need to limit the amount of innovation we put in there to make sure that we keep it on schedule.”  
[00:04:46] What do you think was the main technology that should’ve been saved for a future version?  
[00:04:52] EUV was probably the big thing. When we started to define 10 nanometer,  
[00:04:56] the conclusion was EUV was not ready. EUV is extreme ultraviolet lithography.  
[00:05:03] It prints chip patterns with light at a wavelength of 13.5 nanometers,  
[00:05:07] about 14 times shorter than that emitted by previous tools that chipmakers had relied on.  
[00:05:13] The shorter the wavelength, the finer the features that a single exposure can print.  
[00:05:18] But Intel decided this technology wasn’t going to be ready in time.  
[00:05:21] TSMC transitioned to EUV much sooner.  
[00:05:24] It put EUV into volume manufacturing in 2019 and ramped it up further on its 5nm node in 2020.  
[00:05:32] Intel’s first EUV process did not reach products until 2023, so TSMC had about four more years  
[00:05:38] of experience with these machines. Yesterday, we were at the research  
[00:05:43] lab getting a preview of 2D materials and CFET and ruthenium interconnects.  
[00:05:50] I’m curious about how you decide whether that technology is mature enough for the next node.  
[00:05:55] One thing that did also come out of 10 nanometer is we started to define a set of maturity metrics.  
[00:06:00] We use those maturity metrics in a process which we call phase gate, where we would say,  
[00:06:05] “To go from pathfinding into development, these are the criteria that we need to go hit.”  
[00:06:10] There are yield criteria, defect criteria, performance criteria, and we need to hit those  
[00:06:14] in order to move to the next set of the flow. If there’s something that doesn’t make that,  
[00:06:18] then it misses that, and it goes on to the next technology.  
[00:06:21] We focus on the items that are ready and we can run and put into a process, because  
[00:06:26] one of the key things is staying on schedule. Staying on schedule is hard partly because new  
[00:06:31] transistor designs take decades to mature. Modern chip transistors evolved from the  
[00:06:35] planar MOS transistor, demonstrated in 1960. The history of transistors since has been  
[00:06:41] the progression from two dimensions into three. Each development that Chris goes on to describe,  
[00:06:46] from FinFET to gate-all-around, is a step in that progression.  
[00:06:50] So it’ll help to first look at a basic transistor and how its parts have changed over time.  
[00:06:55] A transistor is basically a switch. When it’s turned on, it allows current  
[00:07:00] to flow between its two ends, which are called the source and the drain.  
[00:07:05] A piece called a gate sits on top of the silicon between the source and the drain.  
[00:07:11] Applying a positive voltage to the gate turns the switch on, because the positive  
[00:07:16] voltage pulls negatively charged electrons in the silicon beneath up toward the gate.  
[00:07:22] However, a thin layer of insulation stops them from actually reaching the gate.  
[00:07:25] So the electrons collect just beneath that insulation and form a thin conducting path  
[00:07:32] from the source to the drain. This is called the channel.  
[00:07:36] Remove the voltage and the electrons disperse, the channel disappears, and the switch turns off.  
[00:07:41] As transistors shrank, the source and the drain got so close together  
[00:07:45] that current could flow through the channel even when the switch was supposed to be off.  
[00:07:50] We needed a better way to control the channel and prevent current from leaking through.  
[00:07:54] The fix was to give the gate a tighter grip on the channel by touching it from more sides.  
[00:08:00] In the original planar transistor, the gate only touches the channel from the top.  
[00:08:04] The FinFET transistor squeezes the channel into a thin vertical fin of silicon.  
[00:08:09] The gate drapes over the fin, so it controls the channel from three sides.  
[00:08:14] The next progression from there was to cover not only the top and  
[00:08:17] the sides of the channel, but also the bottom. This technology is called gate-all-around, and  
[00:08:22] it slices the channel into thin ribbons, each of which gets completely wrapped around by the gate.  
[00:08:27] But getting gate-all-around to work required new materials and new manufacturing steps.  
[00:08:31] To build these floating ribbons of silicon, you first sandwich them between alternating  
[00:08:36] layers of a temporary placeholder material, which holds the space where the gate will eventually go.  
[00:08:42] We use a placeholder because the materials in the real gate wouldn’t survive the processing  
[00:08:46] that comes after, which involves baking the wafer at around 1,000 degrees Celsius.  
[00:08:52] Once these hot steps are done, chipmakers etch away the  
[00:08:55] placeholder, leaving the ribbons suspended. Then they fill the gaps around every ribbon  
[00:08:59] with a thin coat of a special insulator called a high-k material, whose purpose is to let the gate  
[00:09:04] pull more strongly on the channel. And then on top of this material,  
[00:09:09] they put the metal of the gate itself. FinFET was demonstrated in a lab in 1989  
[00:09:14] and reached volume production at Intel in 2011. A gate-all-around transistor had been demonstrated  
[00:09:20] a year earlier, in 1988, but Samsung didn’t begin producing gate-all-around chips until 2022.  
[00:09:27] So these ideas, FinFET and gate-all-around, were developed around the same time,  
[00:09:32] but they reached production a decade apart. I wanted to ask Chris why it took so long to  
[00:09:37] get to this current gate-all-around technology. Maybe you can walk me through the process of  
[00:09:41] getting into high-volume manufacturing. I want to understand concretely,  
[00:09:44] once you have an idea that, “Hey, we’re going to make the channel smaller, we’re going to  
[00:09:48] surround it…” All the other problems of material science, figuring out how to not destroy the gate,  
[00:09:56] how do they actually get figured out? Why does it take so long?  
[00:09:58] Gate-all-around’s a good example, because back in the ’90s we knew of this idea.  
[00:10:02] But we knew there were going to be these problems on how you put this  
[00:10:05] into high-volume manufacturing. At the same time, there are other  
[00:10:08] things like high-K metal gate. There’s strained silicon,  
[00:10:13] there’s FinFETs that are out there. It’s a question of when’s the right  
[00:10:17] time to go and tackle those? Well, you don’t want to  
[00:10:20] tackle something before you have to. If you have these other things that can drive  
[00:10:24] performance, you would go and do that. So we went through this path.  
[00:10:28] We did strained silicon, high-K metal gate, we did FinFETs, and then it became, “Well,  
[00:10:32] we need to do things further. How do we get there?”  
[00:10:35] Well, gate-all-around’s really the ultimate transistor out there.  
[00:10:38] Maybe it’s time to go and start tackling some of those issues that you have.  
[00:10:43] You’re right, now you have to look at how do you put high-K metal gate in with gate-all-around.  
[00:10:48] It’s that innovation that takes time. Sometimes you need new materials.  
[00:10:52] Sometimes you need a different tool in order to be able to do some of the  
[00:10:57] things that you need to go do, and that requires invention from the tool vendors.  
[00:11:01] You have to go to the tool vendor and say, “Hey, I need a tool that can do XYZ.  
[00:11:04] I need a gas that can deposit this particular material that goes into that.  
[00:11:09] I need a heating chuck that has this characteristic to it.”  
[00:11:14] All those things take time. Some of it’s iterative,  
[00:11:17] where you have to run a gate-all-around transistor and say, “Oh, well, that didn’t work.  
[00:11:21] Let me figure out what was wrong with my hypothesis and  
[00:11:25] try it again with some different structure.” How has the nature of R&D changed from the era of  
[00:11:35] just making planar transistors smaller and smaller and getting the benefits of Dennard scaling,  
[00:11:39] to the world we’re in today? Is it just a totally different  
[00:11:42] kind of R&D process? Previously it was,  
[00:11:43] “Let’s make things smaller, smaller, smaller.” Now you look at all these other facets  
[00:11:47] of performance at the same time, and improvements in size don’t come as easily.  
[00:11:52] Walk me through whether there was some crucial change in the R&D process at that point.  
[00:11:55] If you look at the ’80s and ’90s, yes, it was driven really by Dennard scaling, lithography.  
[00:11:59] We just made things smaller, transistors got faster, they got more reliable,  
[00:12:03] and it was a very predictable cadence. When we started to hit the 2000s, we saw,  
[00:12:09] “That’s not good enough anymore. We need to do something different.”  
[00:12:11] To me, it became this golden age of innovation. For each technology node,  
[00:12:16] how are you going to provide more scaling? How are you going to provide more performance?  
[00:12:21] It drove things like strained silicon. It drove high-K metal gate.  
[00:12:24] It drove FinFETs. It drove gate-all-around. It drove backside power.  
[00:12:29] These are things that in the ’80s and ’90s you would be like, “Oh no,  
[00:12:32] we’re not touching any of that,” because we just continued to have the same process flow.  
[00:12:35] We just scaled it, scaled it, scaled it. But for somebody like me who’s a  
[00:12:40] transistor junkie, it’s awesome, because now the playbook’s open.  
[00:12:46] You can do all sorts of things out there. You can bring in new materials.  
[00:12:49] Just look at the number of materials we used to use in the ’90s versus the materials today.  
[00:12:52] It’s probably gone up 10X. There’s a lot of innovation.  
[00:12:56] There’s atomic layer deposition. You’re controlling this stuff atom by atom.  
[00:13:02] So it’s changed a lot how you approach the process.  
[00:13:06] Before, it was, “Try to not change anything.” Now it’s, “Take the sledgehammer and start tearing  
[00:13:11] the thing up and come up with some new idea.” For 14A, Intel is using a new kind  
[00:13:16] of lithography machine: High-NA EUV. It uses the same extreme ultraviolet light  
[00:13:22] as today’s EUV machines, but changes the optics. NA, or numerical aperture, is a measure of how  
[00:13:29] wide a cone of light the machine’s mirrors can focus onto the wafer.  
[00:13:34] The wider the cone you can focus, the smaller the spot that your light can carve.  
[00:13:38] Standard EUV machines have an NA of 0.33. High-NA widens it to 0.55.  
[00:13:45] So High-NA can print features about 1.7 times smaller in a single pass.  
[00:13:51] When features are smaller than the lithography machine can print, chipmakers have to split  
[00:13:55] the pattern across several passes, each printing a different set of features.  
[00:14:00] The most tightly packed patterns can require two, three, or even four passes.  
[00:14:06] Each additional pass takes up valuable time on a machine that costs around $200 million,  
[00:14:10] and it introduces another opportunity for defects. High-NA machines cost about twice as much,  
[00:14:16] but they can reduce the number of passes that are needed.  
[00:14:19] So the question which determines whether they justify their higher  
[00:14:22] price is how much more time they save and how much they reduce the risk of defects.  
[00:14:27] Now you guys are using High-NA EUV tools for 14A, whereas TSMC has said  
[00:14:32] that they don’t make economic sense yet for them. How do you decide whether the next litho tool is  
[00:14:39] the one that is ready to adopt or not? High-NA’s a good example of where,  
[00:14:45] because of the architecture of our technology versus TSMC’s, we make different conclusions  
[00:14:52] off of the same tool set. We use backside power.  
[00:14:56] That means that you actually alleviate some of the pitch requirements you have on the front side.  
[00:15:01] That allows you to print that directly with High-NA.  
[00:15:04] TSMC has to run tighter pitches because they don’t have backside power,  
[00:15:08] and they can’t do that with High-NA, so they have to use double patterning EUV.  
[00:15:12] So for them, it’s not very helpful. For us, it is very helpful.  
[00:15:16] Now at 14A, we’ve left it as an option, and it’s something that we’ll have a discussion  
[00:15:20] with the customer on, because there’s some value proposition to it, and there’s some  
[00:15:24] complexity that it adds. Chris is referring to  
[00:15:27] a feature called backside power. A chip has two different kinds of wiring.  
[00:15:31] Power lines deliver electricity to the transistors, and they need to be thick.  
[00:15:35] Signal lines let the transistors talk to each other.  
[00:15:38] They’re much thinner, but they need to be spaced apart so that the signal from one wire doesn’t  
[00:15:42] interfere with the signal from another. In the past, all of these power lines  
[00:15:46] and signal lines had to be crammed together on top of the transistors.  
[00:15:50] Intel’s newest process moves these power lines below the transistors, to the back of the wafer.  
[00:15:55] This frees up space on top, so the signal lines don’t have to be packed as tightly.  
[00:16:00] This change makes High-NA worth it for Intel. Without backside power, the wiring is so  
[00:16:05] tight that it would require multiple passes to print, even with High-NA.  
[00:16:09] With backside power, a single High-NA pass is enough.  
[00:16:13] Outside companies can now commission Intel to manufacture chips that they’ve designed.  
[00:16:17] They follow Intel’s process design kit, or PDK: the menu of what a given process can build,  
[00:16:24] and the rules for building it. Do you need to lock that into  
[00:16:26] your PDK right now for customers who are planning on developing on 14A?  
[00:16:30] It’s an option in the PDK today, and we’re handling it as a customer-by-customer  
[00:16:35] discussion as to whether or not they want to go down that path or not.  
[00:16:39] For 18A, there was public reporting that there were delays in or issues with the PDK,  
[00:16:44] such that some instructions didn’t work, and it was difficult for people to use  
[00:16:47] your foundry to build their chips. Tell me about the process of Intel  
[00:16:51] becoming a foundry and then having a PDK that other customers can use to make  
[00:16:57] whatever chip they’re making as well. There’s definitely a learning curve to  
[00:17:00] how you become a foundry. That’s something that our  
[00:17:02] competitors have gone through as well. PDK is a good example of that.  
[00:17:05] For decades, we’ve been an IDM. We’ve gone to our product teams  
[00:17:09] and shown them our transistor data, and we share that data back and forth, and we haven’t  
[00:17:12] had a formal PDK-type process. So that’s a new process that  
[00:17:16] we’ve had to implement on 18A. 18A started out not having a PDK.  
[00:17:23] There’s definitely a lot of feedback we’ve gotten from the customers as to what they expect  
[00:17:27] for quality and maturity of the PDK and what sort of information they want to see in there.  
[00:17:33] We’ve tried to incorporate that into making sure that we have a PDK that  
[00:17:37] meets our customers’ requirements. That’s where we’ve ended up.  
[00:17:40] We’re starting to get PDKs that have this, and 14A will have that from the get-go.  
[00:17:45] It has very high quality PDKs. Again, there are maturity metrics for  
[00:17:49] what is a PDK 0.5 versus a 0.9 versus a 1.0. We’re constantly going through and taking  
[00:17:56] customer feedback and incorporating that into the quality of our PDK.  
[00:18:00] For most of its history, Intel’s fabs made only Intel’s chips.  
[00:18:04] That could be part of what allowed TSMC to gain an edge.  
[00:18:07] Serving many customers gave TSMC more wafers to learn from, more revenue to reinvest,  
[00:18:12] and more pressure to hit deadlines. Basically, all enterprise customers  
[00:18:16] have a shared set of product requirements that you have to meet if you want to even  
[00:18:20] start talking about doing business with them. These are things like SSO, so employees can  
[00:18:24] log into your app with their company accounts, or directory sync, so that whenever someone leaves,  
[00:18:29] their access gets shut off automatically. These features are harder to get right than  
[00:18:33] you think, and the risk-reward for building them in-house doesn’t really make sense:  
[00:18:37] a slightly better version of SSO probably won’t accelerate your growth,  
[00:18:40] but a broken one will definitely stunt it. WorkOS gives you access to battle-tested versions  
[00:18:45] of all the most common enterprise features—things like SSO, SCIM, RBAC, audit logs, and more.  
[00:18:51] WorkOS also has versions of these features that are purpose-built for agents, so they can log in,  
[00:18:56] grab the right permissions, and take actions within your product.  
[00:18:59] All of these features can be plugged in with just a few lines of code, so you can  
[00:19:03] add them and get started selling to enterprises. OpenAI, Anthropic, and Thinking Machines—as well  
[00:19:08] as more than 3,000 other companies—all rely on WorkOS to meet their enterprise requirements.  
[00:19:15] If you want to join them, go to workos.com and tell them that I sent you.  
[00:19:20] If a butterfly flapped its wings in the ’60s, could you imagine a world where gate-all-around  
[00:19:24] is not even a word people have heard of, an idea people are familiar with, but people are thinking  
[00:19:28] of an extremely different branch of the tech tree? How far down the tech tree do you think  
[00:19:31] things could be totally different? Could it be that we’re not even using copper?  
[00:19:35] If you look at, say, transistors and interconnects, where we’ve gotten to,  
[00:19:42] as far as the transistor and gate-all-around and it being the ideal transistor structure,  
[00:19:47] was somewhat inevitable. As I said, in the ’90s we were  
[00:19:49] already talking about these types of things. Backside power, that one’s pretty out there.  
[00:19:54] Even in the ’90s, the idea that you’re going to strip off the entire silicon substrate and put  
[00:20:00] lines on the backside, that one is probably something that’s a little bit out there.  
[00:20:06] Copper, of course copper wires are the best, so I don’t know how you would end  
[00:20:11] up somewhere else besides copper. But you guys are exploring other—  
[00:20:14] For some of the very tightest pitches, it’s inevitable that you will replace copper.  
[00:20:20] That’s a good example of where you will have another material that will come in there.  
[00:20:24] But for the larger lines, I think copper is about where it’s at.  
[00:20:28] Once you start to do gate-all-around transistors and you do backside power,  
[00:20:33] now you start to enter a very different regime.  
[00:20:36] Now you see it’s not, “Hey, there’s just some substrate and you stack everything on top.”  
[00:20:41] Now you’ve got a transistor which is floating in interconnect, and you’re like, “Okay, well,  
[00:20:45] why don’t I have transistors, interconnect, a little more transistors, more interconnect?”  
[00:20:50] This whole 3D stacking that we now do with just discrete chips that we stack on top of each other.  
[00:20:55] Now you’re like, “Why can’t I just build an entire structure like this?”  
[00:20:59] You see it with memory, NAND, DRAM. They have some incredible 3D structures.  
[00:21:06] NAND already does it, DRAM talks about it, but I think that DRAM inevitably  
[00:21:10] is going to go there too. A lot of people say, “Oh no,  
[00:21:13] we’re not going to do this because we can’t do it in the next five years.”  
[00:21:16] Well, come on, let’s put a larger timescale on this.  
[00:21:18] Let’s put 10 years, 20 years. In 2045, do you think you could do it?  
[00:21:23] Now you start to say, “Oh yeah, I could see us having some pretty  
[00:21:25] exotic structures at that point.” We limit ourselves by what we see  
[00:21:29] as possible in the next four years. As I’ve always said, when people say,  
[00:21:34] “How do you see technology scaling going?”, we have visibility for about four years.  
[00:21:38] Then you get out to the four years, and you go, “Yeah, I think there’s something  
[00:21:41] we can do another four years out of that.” And you get to that four years, and you’re like,  
[00:21:44] “Yeah, I think you can do something.” But if you start to talk about 10 years,  
[00:21:47] it becomes hard to say what it’s going to be. Chris’s idea of building upward could start  
[00:21:50] with the transistors themselves. Chips use two types of transistor,  
[00:21:54] called n-type and p-type, which work the same way, but with the charges reversed.  
[00:22:00] Nearly every circuit is built by pairing them up. Today, chipmakers build them side by side.  
[00:22:06] The next step is to stack them directly on top of each other in order to save space.  
[00:22:11] In principle, that fits twice as many transistors into the same area.  
[00:22:15] This design is called a CFET, short for complementary field-effect transistor.  
[00:22:20] But every extra layer adds manufacturing steps and cost, and also leads to heat building  
[00:22:24] up that doesn’t have a clear way to escape. Because logic consumes more power than memory, you  
[00:22:31] can’t do stacks of DRAM that make HBM or 3D NAND as easily with logic, because of the heat issue.  
[00:22:38] Is that the fundamental issue over the long run? How you—  
[00:22:42] Thermals. There are three things you have when you try to say, “Hey, what limits compute?”  
[00:22:49] It’s how fast can you do the switch, so the frequency of the device.  
[00:22:53] How much power does it take in order to do that switch, so the power efficiency of it.  
[00:22:58] The third one is, how do you dissipate the heat that was generated by doing that switch?  
[00:23:02] That’s the thermals piece of it. These are not new problems.  
[00:23:07] You can go back 20 years and you can see articles on these three things.  
[00:23:10] The question is, thermals… how do you deal with that, particularly when you  
[00:23:13] start to talk about these 3D-type devices? There is a need for that sort of system-level  
[00:23:21] analysis and simulation tools. I think we’re in its infancy  
[00:23:24] because we’ve just started to look at this. It is a limiter, and it will be a limiter, but  
[00:23:31] again, these are problems that we can go solve. The problems respond to work, but engineering time  
[00:23:36] is finite, and so are the wafers for experiments. Deciding where they go across thousands  
[00:23:41] of problems is itself one of the hardest parts of bringing up a node.  
[00:23:45] I sat in on one of Intel’s Hot Topics meetings, where those decisions get made.  
[00:23:50] I’m here with Kevin Fischer, who was laying down the law this morning at the Hot Topics meeting,  
[00:23:54] where you guys were discussing how you’re improving 18A and 18A-P technologies.  
[00:23:58] People would come to you with different experiments they were running,  
[00:24:01] different ideas they had for improving yield and performance, and then you and  
[00:24:06] your integration engineers would tell them what data you needed, how they should proceed,  
[00:24:11] how you think they could move things faster. I want people to have a sense of  
[00:24:15] the culture at these meetings. One thing I found striking is that this  
[00:24:20] is bottlenecking your most advanced node. You want progress to happen fast,  
[00:24:24] so you kind of lay down the hammer. I would say the average engineer doesn’t  
[00:24:29] understand the stakes or the urgency of how this is going to impact Intel’s bottom line,  
[00:24:39] how it’s going to impact our customer. They just have no visibility into those issues.  
[00:24:45] They will typically have a certain set of criteria that they want to go capture.  
[00:24:52] They’ll hit boundaries of, “I asked for something and someone said no, and I’m done.  
[00:25:00] I guess I can’t have this thing that I asked for.” One thing you learn in this industry is that  
[00:25:06] you will never have a complete data set. If you want to wait for a complete data set,  
[00:25:10] you’ve waited too long. It’s already too late.  
[00:25:12] A lot of what I end up doing in those meetings is deciding how much risk we’re  
[00:25:18] going to take on a certain decision or not take on a certain decision.  
[00:25:23] You need to say, “Look, do we go now? Do we start risking production?”  
[00:25:27] Because you’re risking the bottom line. You’re risking revenue.  
[00:25:31] I’m worried you’re going to put me in the light of being an ogre because I’m  
[00:25:35] putting the hammer down on people. That’s a great reputation to have.  
[00:25:39] It’s really conveying urgency. Every day counts.  
[00:25:43] Can you walk me through a particular issue that might come up?  
[00:25:47] One of the examples you saw this morning is epi nodules.  
[00:25:51] Epi is short for epitaxy, which means growing new material on top of an existing one.  
[00:25:56] Chipmakers flow gases over a heated wafer, and the gases leave atoms on its surface.  
[00:26:02] The crystal structure of the material underneath acts as a template.  
[00:26:06] Each new atom lines up with the atoms below it, and the new layer continues the same crystal.  
[00:26:11] Chipmakers use epitaxy at several stages of making a chip.  
[00:26:14] In the step Kevin describes, they use it to grow the source and the drain as small  
[00:26:18] crystals on either side of the gate. During the deposition of our epitaxy,  
[00:26:23] we get abnormal growth, a little thing like a tumor.  
[00:26:26] It’s growing super fast. That causes problems,  
[00:26:30] because one epi will short to the wrong epi and you get transistors not working.  
[00:26:35] Then you’ve got to narrow it down to how you’re going to fix it.  
[00:26:39] For the past decade, Intel’s chips have had this feature called Processor Trace.  
[00:26:43] When you turn it on, it starts recording all the code your program runs, and it captures  
[00:26:47] enough detail that you can go back later and reconstruct every single function call.  
[00:26:52] Most companies don’t need that level of detail. But Jane Street does: they need to investigate  
[00:26:56] specific, fleeting moments in their trading systems—things like  
[00:27:00] a delayed response to a network packet. Those events tend to be too brief for  
[00:27:04] most debugging tools to catch. So when one of Jane Street’s  
[00:27:07] engineers noticed Processor Trace, he started playing around with it.  
[00:27:11] And then he and a summer intern turned that exploration into a new tool called magic-trace.  
[00:27:16] Magic-trace leverages the output from Processor Trace to give Jane Street a  
[00:27:21] history of every function call leading up to a specific moment of interest.  
[00:27:25] This project was completely bottom-up—it started just as something that one  
[00:27:28] engineer thought would be valuable. And now, traders and developers across  
[00:27:31] Jane Street use magic-trace every single day. If you want to work somewhere where you’re trusted  
[00:27:36] to pursue the ideas that you think matter most, Jane Street is hiring researchers and engineers.  
[00:27:41] Go to janestreet.com/dwarkesh to learn more. One of the pieces that you observed this morning  
[00:27:47] was a special clean that we were looking at, which would eliminate the nodule.  
[00:27:53] The nodule would deposit, and then we’d get rid of it.  
[00:27:56] Some of the other discussion was about the source of the nodule.  
[00:27:59] Get rid of the source of the nodule. There’s some issue. How do you  
[00:28:04] decide what the source of it is? For the most part, we work highly parallel.  
[00:28:08] How do you decide? It’s not always evident  
[00:28:10] what the easiest way to fix the problem is, so you work on all the potential fixes.  
[00:28:16] Sometimes it’s not the one you expect first. Once we’ve identified it as a primary problem  
[00:28:22] for the technology, that’s where this Hot Topics meeting gets involved.  
[00:28:27] That’s how we align the resources into those engineering teams so that  
[00:28:33] we can accelerate the work. You said that there’s some  
[00:28:36] fast-track process where wafers can move through faster if they’re bottlenecking some experiment.  
[00:28:40] We have a tiered system of what we call hot boxes in the factory.  
[00:28:44] Every grade of hot box goes a little bit faster. It’s just how the factory prioritizes that  
[00:28:51] particular lot, that block of silicon that’s running through the factory.  
[00:28:55] Our highest grade of hot box, HotBox 1, races through the factory.  
[00:29:00] It gets priority at every single tool, but it’s a drag on the entire factory.  
[00:29:04] If you had a factory person in here, they don’t like playing that card,  
[00:29:09] because you end up using the tools inefficiently so that you can go super fast.  
[00:29:16] Think of it as a highway, and you set aside that one lane for the carpool,  
[00:29:20] which everyone could use, but you’re saying, “Okay, it’s just the carpool.”  
[00:29:23] That’s our HotBox 1. Everyone clear out of  
[00:29:26] that lane except for that one experiment, and that one experiment races down the highway.  
[00:29:30] Kevin’s job is deciding what goes onto the production line now, but the day before, I  
[00:29:35] went to Intel’s research lab with Jack Kavalieros to see ideas that aren’t ready for the node yet.  
[00:29:41] We started with wiring. A transistor is only useful once it’s connected  
[00:29:45] to others, and on a modern chip that takes more than a dozen layers of metal wire stacked  
[00:29:50] above the transistors, called interconnect. Those wires are made of copper, and as they  
[00:29:55] shrink, copper starts to run into trouble. Intel is exploring a replacement: ruthenium.  
[00:30:01] Ruthenium has higher resistivity, so why are you guys exploring ruthenium for the future?  
[00:30:05] Interestingly enough, as you scale the dimensions of those copper wires, you run into challenges.  
[00:30:11] For example, copper typically requires a liner in order to deposit the copper to fill those lines.  
[00:30:17] Ruthenium is very different in that regard because it’s a material that we can actually etch.  
[00:30:23] As such, by etching it, we don’t need that liner. Now you scale those very fine dimensions,  
[00:30:30] and if you can trade off that resistive liner with no liner, ruthenium starts to win.  
[00:30:37] There is a crossover point where ruthenium will have much better  
[00:30:40] conductivity, better resistivity than copper. That’s roughly in the 20-nanometer pitch range,  
[00:30:46] which means, if you can imagine, half of the pitch is your metal line, and the other half is  
[00:30:52] the dielectric that isolates them. So what is the liner?  
[00:30:56] Think of it almost like a glue layer or transition layer that we need in order to deposit the copper  
[00:31:02] and have it stick, and have it make that connection to the copper lines below it.  
[00:31:05] These are all interlocking copper lines that interconnect to each other.  
[00:31:10] But every time you deposit copper, you’ve always had a liner underneath it.  
[00:31:15] In the past, that liner may have been a significant  
[00:31:17] portion of the entirety of that conduction path. But over time, we’ve scaled it, made it thinner,  
[00:31:24] and so copper comes back into play as a contender. One thing I’d be curious to know is how you  
[00:31:30] decide that a technology is mature and ready for high-volume manufacturing.  
[00:31:36] With 10 nanometer, you were mentioning you guys moved on from copper to cobalt,  
[00:31:40] and there were potential issues with that. How do you decide that this  
[00:31:44] technology is going to work at scale? The integration of these materials into such  
[00:31:48] a complex system as the transistor ecosystem involves many, many different components.  
[00:31:54] The scalability is one part, but its ability to integrate is another.  
[00:31:59] At the time we made a decision for cobalt, it was the forerunner.  
[00:32:02] The results were stronger at the time. But as we work with our ecosystem externally,  
[00:32:07] the vendor ecosystem that provides these materials and the tools that we integrate them with, we find  
[00:32:13] solutions down the road that may bring copper back in line as being the stronger of the two.  
[00:32:20] That’s exactly what happens. Every technology that we go through,  
[00:32:24] we will evaluate multiple options. As we get closer to our time horizon  
[00:32:30] for delivering a manufacturing-worthy product, we have to make a decision.  
[00:32:35] The leading option at the time was cobalt. Now it’s copper again,  
[00:32:39] and perhaps in the future it’ll be ruthenium. I’d love to get your thoughts on CFET, basically  
[00:32:45] stacking the transistors on top of each other. What is progress like there?  
[00:32:50] Can you keep making more and more layers? Is it just two?  
[00:32:53] Can you go three, four? How high can you get?  
[00:32:55] That evaluation of CFET is currently underway. Not just by us, by our competition.  
[00:33:03] Labs externally are looking at it. It is the ultimate in stackability.  
[00:33:07] We’re taking transistors that had to be compressed more and more,  
[00:33:10] and we’re relaxing that in some ways because we’re going to stack them on top of each other.  
[00:33:15] But the act of stacking does not mean that they’re not interconnected.  
[00:33:18] What used to be connections on the top or even on the bottom,  
[00:33:21] as we’ve seen from our press release, now has to go vertically in between the transistors.  
[00:33:27] That’s a new challenge because the aspect ratio of creating trenches and filling those  
[00:33:32] trenches becomes more and more difficult. It’s not as straightforward as stacking the  
[00:33:37] transistors, because you still have to think about interconnecting them.  
[00:33:40] Is the issue there the etch to get that deep hole? Aspect ratio for the etches is a big part of it.  
[00:33:45] We’re working with our vendors to evolve on that and to improve that, but it’s also what  
[00:33:49] you fill those very tiny spaces with. Because filling can sometimes leave  
[00:33:54] air gaps or holes that are never really filled, and that’s not ideal.  
[00:33:58] I assume there’s a version of CFET that works inside this lab.  
[00:34:02] What is the kind of wafer or process that is working right now?  
[00:34:06] Then what’s the next step? What’s the next step after that,  
[00:34:08] until it’s inside the full high-volume process? Part of the process of evolving these  
[00:34:15] technologies, especially something more complex like an architecture — not just a basic chemistry  
[00:34:20] or a material, but a full architecture like CFET — is that we have to make short-loop vehicles  
[00:34:26] that can give us faster turnaround. The normal manufacturing process can  
[00:34:30] take a month or longer to complete the thousands of steps that it goes through.  
[00:34:35] Our goal here is to take unit cells of that process and qualify them.  
[00:34:41] We take advantage of short-loop vehicles that can give us electrical parameters,  
[00:34:47] chemical parameters that can resolve some of those challenges, those speed bumps.  
[00:34:52] Once we’ve resolved them, then we combine them into a more complex test vehicle.  
[00:34:58] What you would find in here is something very simple.  
[00:35:01] You might be making a diode, you might be making a capacitor, which are components of the transistor.  
[00:35:08] As those evolve and become stronger, better performing, you combine them to make the next  
[00:35:14] stage, which might be the transistor itself. In the CFET example, you might not choose to  
[00:35:20] do four ribbons on top of four ribbons. You might just choose to do one on one,  
[00:35:25] because naturally the aspect ratio of dealing with something that  
[00:35:29] much taller becomes more and more challenging. So we would have a simplified version of a CFET,  
[00:35:35] which has only one wire for the NMOS and one wire for the PMOS.  
[00:35:40] That simplifies our job, but it still helps us evaluate the stacking of devices  
[00:35:46] and how they will interconnect. But are the feature sizes here as  
[00:35:49] small as they will be eventually? Or are the feature sizes bigger?  
[00:35:52] Oh, absolutely. In some cases, at least as small. For example, you’ve heard of 2D materials,  
[00:35:59] these transition layer dichalcogenides, as they’re called.  
[00:36:03] They’re very, very thin materials. They’re essentially one monolayer  
[00:36:07] of atoms that we deal with. Those depositions can happen in this lab.  
[00:36:12] We can evaluate those films in terms of conductivity, our ability to contact them,  
[00:36:17] our ability to modulate that conductivity, which is what the transistor does.  
[00:36:22] So yes, we do have the ability to not only deposit films that are very small and thin to the  
[00:36:30] atomic scale, but also print very small features. We have EUV technology, or E-beam technology, that  
[00:36:38] can allow us to print very small features similar to what we will eventually make in production.  
[00:36:43] I guess I don’t understand intuitively, lacking the context in this process,  
[00:36:51] if you have the features that are as small for a working CFET right now.  
[00:36:57] Why will it take 10 years for it to be in my phone?  
[00:37:01] I understand that there’s a process, but why is it such a long process?  
[00:37:05] The answer is slightly different when you’re dealing with an architecture  
[00:37:09] like CFET versus a novel material. Materials have, of course, the  
[00:37:14] challenges of being deposited, etched, removed. Their compatibility with other layers above and  
[00:37:21] below, all those things have to be researched first before you put them in a production line.  
[00:37:26] An architecture may seem like a simple evolution. “Oh, you’re making nanoribbon  
[00:37:31] transistors next to each other. What’s wrong with just stacking them?”  
[00:37:35] But the act of stacking them, of course, increases the aspect ratio for etches, depositions, cleans,  
[00:37:41] and the technology may simply not be ready yet. But if you’ve already made it here, there’s a  
[00:37:47] version of the technology that’s ready, right? Correct. We’ve made a simplified version that  
[00:37:52] may not be an advantage over our current side-by-side technology of nanoribbons,  
[00:38:00] but we need to evolve it to make it maybe two nanoribbons, or to add the right type of  
[00:38:04] metals and dielectrics, in order to extract the maximum performance out of that device.  
[00:38:10] Got it. So it’s like a long tail of— There’s a thousand different steps that  
[00:38:14] all have to come together in a very unique way to make the performance compatible or actually  
[00:38:20] supersede the prior technology. Where do the ideas tend to fail?  
[00:38:24] You have 20 ideas like 2D materials. What is the way in which you decide  
[00:38:29] this is actually not worth pursuing further? Sometimes we discover fundamentals about the  
[00:38:37] material that will be incompatible with the rest of the processing that we do.  
[00:38:44] The first level of experiments may simply be very simple depositions.  
[00:38:48] You say, “Okay, I can deposit the film, I can look at it, I can measure it.  
[00:38:53] But the moment I try to make a contact to it, nothing sticks.”  
[00:38:56] It could be something as fundamental as the adhesion.  
[00:39:00] The next step in the process simply has no way to adhere to the material.  
[00:39:06] So you may rule out a material because of something as simple as that.  
[00:39:10] More complex challenges might be that the subsequent processing may  
[00:39:16] have gaseous interactions with downstream steps. For example, I’ve deposited the film, I’ve capped  
[00:39:23] it with other materials, but they’re not hermetic. So my third or fourth or fifth step in the  
[00:39:30] process may actually still interact with it and change its properties.  
[00:39:34] That makes it unstable, and now we have to find better hermetic sealing for that process.  
[00:39:40] If we don’t find a way to control it, then it’s a dead end for us.  
[00:39:45] Stacking transistors is still in the research lab. Stacking whole chips is already in production,  
[00:39:50] and it tackles a different problem: how separate chips communicate with each other.  
[00:39:55] Modern computers are divided into multiple parts, each optimized for a different task.  
[00:39:59] For example, Nvidia’s Blackwell data-center GPU joins two huge processor chips and surrounds them  
[00:40:06] with eight stacks of high-bandwidth memory. These chips have to constantly send  
[00:40:10] data back and forth with each other. And in AI, the speed of that traffic,  
[00:40:15] not the raw computation itself, is often what limits how fast the workload finishes.  
[00:40:20] Imagine two chips side by side, communicating through their facing edges.  
[00:40:24] If you double each chip’s width and length, you’ll have four times the area for circuitry,  
[00:40:28] but only twice the edge length for connections. This is the area-versus-perimeter problem.  
[00:40:33] As transistors become denser, a chip’s ability to do computations increases  
[00:40:37] faster than its ability to move data around. The industry has known about this problem  
[00:40:42] for years, so multiple technologies have been invented to address it.  
[00:40:45] The completed circuits must undergo two last operations: bonding and packaging.  
[00:40:51] Once a chip is made, it still has to be connected to other chips and to the rest of the computer.  
[00:40:56] That step is called packaging, and it has changed a lot in the last few decades.  
[00:41:00] At a high level, you can think of the evolution of packaging like this: initially,  
[00:41:04] chips were laid out side by side. Wires connecting them went out  
[00:41:07] the side of one chip to another. To allow for more communication  
[00:41:11] density, the industry introduced a shared piece of silicon, called an  
[00:41:15] interposer, for multiple chips to sit on. A chip can talk to other chips through the  
[00:41:19] wiring that runs directly through the interposer. This type of packaging is often called “2.5D”.  
[00:41:25] Another way to increase connection density is to bond chips directly to one another.  
[00:41:30] This allows for shorter connections between chips, but the early versions of this idea used solder  
[00:41:35] bumps, which are bulky and increased resistance. It would be better to skip the solder and fuse  
[00:41:41] the signal wire connections of the two chips directly to each other.  
[00:41:45] This is called hybrid bonding, and it is one of the technologies the  
[00:41:48] semiconductor industry is investing in the most. Hybrid bonding works by aligning the copper  
[00:41:53] interconnects of one chip with those of another. Then these chips are pushed together and heated  
[00:41:58] so their interconnects expand and bridge the gap between the chips.  
[00:42:01] This process makes the insulating surfaces around the copper bond as well.  
[00:42:05] And so by removing the solder bumps, you end up with much denser connections.  
[00:42:09] But the reason this technology is only now entering volume manufacturing is because  
[00:42:12] it took a while to iron out the alignment and defect challenges that it introduced.  
[00:42:16] In the packaging lab, I asked Tyler Osborn, a director in Intel’s advanced packaging  
[00:42:22] technology development group, how they put this into practice.  
[00:42:25] Intel has spent over 50 years optimizing its CPUs for speed.  
[00:42:28] But lots of these optimizations—like caching and branch prediction and  
[00:42:32] speculative execution—reduce predictability. The exact same instructions can take four  
[00:42:36] cycles to execute one time and 300 the next. When you stack billions of instructions together  
[00:42:41] and execute them across multiple threads and cores, these non-determinisms compound into  
[00:42:45] all sorts of hard-to-reproduce bugs. If you work on serious systems,  
[00:42:49] you’ve definitely experienced this. Antithesis solved this by doing something a bit  
[00:42:53] crazy: they built a 100% deterministic computer. They identified every single door in Intel’s x86  
[00:43:01] architecture where non-determinism could leak in—network packets, disk reads,  
[00:43:05] temperature sensors, even time itself. And they either welded each of these  
[00:43:09] shut or slotted in a controlled simulation. This deterministic computer is just a foundation.  
[00:43:15] On top of it, Antithesis built a testing platform that compresses  
[00:43:18] years of production hardening into minutes. It runs your software through thousands of  
[00:43:22] parallel worlds, injecting faults and intelligently steering each one  
[00:43:26] towards a one-in-a-billion failure that you’d never be able to test yourself.  
[00:43:30] This determinism is what’s behind all the other insane Antithesis features that I’ve  
[00:43:34] mentioned over the past few episodes. It’s what lets you reproduce any bug  
[00:43:38] and time travel to any point in the test run. Most importantly, it’s what lets you—or your  
[00:43:42] agents—trace every failure back to its root cause. Go to antithesis.com/dwarkesh to learn more.  
[00:43:53] Two different ways you could do hybrid bonding: die to die and die to wafer.  
[00:43:59] Maybe you can talk about the advantages of both and which one actually practically works better.  
[00:44:03] Sure. Around Intel, what I think you’re referring to as die to die,  
[00:44:07] we typically call wafer to wafer. We actually take a full wafer and  
[00:44:10] another wafer and bond them together. That’s an approach that’s really popular  
[00:44:14] right now in the CMOS image sensor industry. In fact, it basically dominates it.  
[00:44:19] It’s being looked at for other things like memory stacking.  
[00:44:22] People have published ideas about all kinds of stuff.  
[00:44:24] One of the challenges with that, though, is that you need dies that perfectly match each other, and  
[00:44:29] are perfectly left-handed and right-handed, so you have to be able to bond exactly one to the other.  
[00:44:35] One-to-one die size is a challenge. If they’re not the exact same design  
[00:44:39] device on top and bottom, that’s a problem. With wafer to wafer, it’s challenging to make  
[00:44:43] sure that you have wafers that match really well in terms of the sort.  
[00:44:46] So sort good array here versus sort good array here.  
[00:44:49] If they match exactly — good die and bad die all match — I can get 100% yield  
[00:44:53] of that operation of the good dies. But the chances of that are very low.  
[00:44:57] There’s going to be some randomization of the two, and whatever that randomization is,  
[00:45:01] will be loss of good bonding to bad. Whereas with chip to wafer,  
[00:45:06] I can dictate the terms. I can singulate and have known good dies  
[00:45:11] that I’ve tested at the chip level, and then only bond known good to a known good base position.  
[00:45:16] Do you think then chip to wafer is the way that you’ll do hybrid bonding in the future?  
[00:45:19] I think we’re going to do both. We definitely have the capability to do both.  
[00:45:23] It’s really customer and architecture driven, but certainly chip to wafer in  
[00:45:26] the logic-to-logic space makes a lot of sense. You were explaining that going from advanced  
[00:45:31] packaging to hybrid bonding, the size of the pitches is decreasing.  
[00:45:34] How much further could that go? That’s a wonderful question.  
[00:45:38] Historically, like we were saying, 15 years ago first-level interconnect  
[00:45:41] was 130-150 micrometer pitch. Today in HVM, we’re doing 25  
[00:45:46] micrometer pitch in Foveros. Here we’re doing sub-10,  
[00:45:50] but there’s already been literature out there. In fact, the biggest conference every year  
[00:45:54] in packaging is the IEEE ECTC conference that happens in May.  
[00:45:59] There was a paper there this year showing reliability data on a  
[00:46:03] 0.45 micron pitch hybrid bonded device. So you can imagine that’s a whole other  
[00:46:08] order of magnitude in density again from where we are right now in HVM.  
[00:46:14] That scalability has already been proven. So I see a long runway there.  
[00:46:18] Within interconnect, within a single wafer, how far separated are they usually?  
[00:46:23] In the back end of the fab, you can imagine the few layers below packaging are typically around  
[00:46:30] one micron to a half micron in size. So if you can push packaging down  
[00:46:35] to 0.5 microns or below, you can almost think about taking layers off the top of the die and  
[00:46:42] connecting a lower layer within the silicon to another lower layer within the silicon.  
[00:46:46] That’s really where the beauty of hybrid bonding happens.  
[00:46:49] You could think someday about even having reduced interconnect layers on both sides  
[00:46:53] that we can bond together and have less total IR drop between the two transistor layers.  
[00:46:59] It’s really cool to think about where that could go once we get into those regimes.  
[00:47:04] Actually, I am very curious about… For AI, it makes sense why hybrid  
[00:47:07] bonding is so powerful, because then you can get higher bandwidth to the memory.  
[00:47:11] But you were saying there are issues with heat and everything.  
[00:47:14] What is the advantage for non-AI applications of hybrid bonding?  
[00:47:17] Excellent question. There are companies out there that are looking at it for  
[00:47:21] non-AI applications, even in client devices. One of the big things I think it can help  
[00:47:28] with there is, number one, obviously the same raw interconnect density, especially  
[00:47:32] between something like a CPU and a GPU. But the other one is around power.  
[00:47:37] Like we talked about before, as you get to finer and finer interconnects,  
[00:47:41] you can reduce the total power consumption, in picojoules per bit, for that interface.  
[00:47:46] With hybrid bonding in those applications, you could think about that as another way  
[00:47:49] that packaging can help reduce the total system power budget.  
[00:47:53] That gives you lots of benefits: lower power, less heat, for the same benefit  
[00:47:58] in terms of actual electrical performance. So far, this has been about making better chips.  
[00:48:02] The other half of the question is how many chips the industry can make if AI labs are  
[00:48:07] willing to pay for far more of them. I’m getting a chance to talk to  
[00:48:11] Pushkar Ranade, who is the CTO of Intel. I’m very interested in understanding how  
[00:48:16] the fact that the entire industry has to rely on the same suppliers bottlenecks  
[00:48:20] your ability to ramp up production. For this EUV tool, ASML produces  
[00:48:24] fewer than 100 of them a year. They don’t plan to produce more  
[00:48:28] than 100 a year, or significantly more, even by the end of the decade.  
[00:48:31] That has to be split between you, between TSMC, between all the memory makers who  
[00:48:35] are ramping up production, like SK Hynix. How does that limit your ability to scale  
[00:48:38] up to all this demand? It is a limiter.  
[00:48:42] We have to make the most of the capacity that we already have installed.  
[00:48:45] We’ll try to increase the output from our existing fleet of tools.  
[00:48:50] But EUV or ASML is not the only bottleneck. It is definitely a bigger bottleneck than  
[00:48:56] some of the other tools, but to a large extent, we’re seeing  
[00:49:04] all equipment seeing tremendous supply shortage. Even though there are multiple providers of other  
[00:49:10] tools, once you lock into a process flow — let’s say 18A, which is a mature process  
[00:49:17] now — we need a specific tool. We can’t just go and get a  
[00:49:22] different tool for the same process. So we’re locked into that one tool,  
[00:49:27] one supplier, and we rely on that. What lessons does this give for  
[00:49:32] 14A in terms of how you structure it? By 2028, it’s going to be such a crazy world.  
[00:49:36] How do you structure things in such a way that you have flexibility in ramping?  
[00:49:40] The way to do it — and we’ve been doing it, and generally everybody does it — is  
[00:49:44] you try to maintain as much fungibility as possible going from one node to the next node.  
[00:49:48] Going from 18A to 14A, maybe you would say 80% of the tool set can be reused.  
[00:49:54] Then, of course, 14A would require some new capabilities because it’s a denser geometry,  
[00:50:01] so it would require some unique tools. Do you have a sense of what the ultimate  
[00:50:05] bottleneck is on how many wafers you guys could produce a month, even if you were to decide  
[00:50:11] to invest infinity money into doing CapEx? Given the existing constraints, let’s say we had  
[00:50:17] to maximize the output from a given footprint of tools, then I think it’s incremental, because the  
[00:50:25] process today is already yielding pretty high. If your yield is already pretty high,  
[00:50:31] getting every 1% extra yield is extremely hard because it’s already a finely tuned process.  
[00:50:38] Are there enough tools in the world so you could 10X the amount of wafers you’re  
[00:50:40] producing at the leading edge? Not 10X, but probably 2X, yes.  
[00:50:45] That’s quite interesting, because the AI industry for a decade has  
[00:50:49] been 3Xing compute year over year. You’re saying that just can’t continue.  
[00:50:55] Unless the entire supply chain — starting from the equipment suppliers, their suppliers,  
[00:51:01] their sub-suppliers — unless everybody produces more, you can’t increase the output.  
[00:51:07] Just to give the audience a sense of how big the AI demand is and how well it monetizes the  
[00:51:13] products you guys are producing: you can crunch the numbers, and the numbers seem to suggest  
[00:51:18] that just a couple billion dollars of CapEx on Intel’s account results in enough chips — or the  
[00:51:24] logic for enough chips — to produce, say, $100 billion of revenue for the AI model companies.  
[00:51:30] Of course, there are so many other players within that stack.  
[00:51:32] There’s also memory and other things. But it’s crazy that a couple billion  
[00:51:38] dollars of CapEx, which can be amortized over many different years, produces $100 billion  
[00:51:44] of revenue every single year. That seems to suggest that at  
[00:51:47] some point that should percolate down. At some point, the AI labs could just say,  
[00:51:52] “We’ll just buy everything. Produce as much as you can.  
[00:51:54] We’ll guarantee future income streams.” There are early signs that could  
[00:51:59] actually be happening already. The demand signals are just so high.  
[00:52:04] But I think you were alluding to how the value is accumulating at the top of the technology stack.  
[00:52:13] What is essentially happening is we moved from a fully vertically integrated industry 30-40  
[00:52:20] years ago, maybe longer, to a very horizontal industry, where you have foundries, you have  
[00:52:26] equipment makers, you have their suppliers. Today, every hyperscaler is designing their  
[00:52:34] own chips, and the scale of the hyperscalers is so large.  
[00:52:38] Some of the model companies, for example, their demand is so high  
[00:52:44] they could easily consume an entire fab’s worth of silicon on their own, or multiple fabs’ worth,  
[00:52:53] and they definitely have the capital to fund that. So in some sense, we are moving from a horizontal  
[00:53:01] world again to a pseudo-vertical world. It’s not monolithically vertically integrated,  
[00:53:10] but it’s kind of virtually vertically integrated. What is the nature of economies of  
[00:53:17] scale in this business? If you look at how many  
[00:53:21] wafers at the leading edge TSMC versus Intel is shipping, it’s upwards of 3X for TSMC.  
[00:53:28] What kinds of advantages do you get at this point from economies of scale?  
[00:53:32] Or is it that once you reach a certain point, the economies of scale get weaker?  
[00:53:36] That’s a very important question. This entire business just  
[00:53:41] relies on economies of scale. If you look at all the advanced manufacturing  
[00:53:49] companies out there, in semiconductor foundries the scale economics is probably the purest.  
[00:53:56] The reason for that is the fixed cost is just so incredibly high.  
[00:54:02] Once you build a fab, like 80% of your cost structure is fixed.  
[00:54:07] What that means is every extra percentage of utilization is adding far more in revenue.  
[00:54:16] So it’s extremely important. We’ll fight for every extra  
[00:54:19] percent of fab utilization, but also every extra percentage of fab output.  
[00:54:25] Let’s say I’m making some wafers today and the yield is 60%.  
[00:54:30] If I improve the process and the die yield becomes 65% or 70%, it’s not a linear advantage.  
[00:54:38] I’m getting way more output for the given footprint.  
[00:54:42] So there’s always room to improve the economies of scale.  
[00:54:45] That’s one of the reasons why you’re seeing so much consolidation in this business.  
[00:54:53] There are only three foundries left at the advanced node for that exact reason.  
[00:54:59] Along the way, many companies just stopped manufacturing.  
[00:55:04] I don’t know if you’ve seen… There’s a chart where 40  
[00:55:07] years ago there were like 20 foundries. Over time the number of foundries kept  
[00:55:13] diminishing until today there are only three. What is then the concrete master  
[00:55:17] plan to catch up to TSMC? Even though TSMC is ahead,  
[00:55:21] there’s so much overflow demand at their leading edge, where N3 is now majority AI  
[00:55:26] accelerators and maybe majority Nvidia alone. There’s all this demand for CPUs, for other  
[00:55:32] things, which are also, by the way, needed for AI. There’s this humongous influx  
[00:55:36] in demand for CPUs because of AI. How do you see this opportunity right now,  
[00:55:39] where Intel’s a few years behind, while TSMC is just way oversaturated?  
[00:55:44] Catching up to TSMC has multiple facets. The catch-up that we need to do is in scale.  
[00:55:52] Like you said, they’re just a much larger wafer manufacturer today than we are,  
[00:55:58] and even bigger than what Samsung is. Catching up in scale will be a gradual process.  
[00:56:08] If you meant catching up in terms of just the technology, I think we’re already there.  
[00:56:18] We might be a few percent off on performance or power or area density.  
[00:56:28] But this sort of benchmarking, where one foundry is ahead or one foundry is behind,  
[00:56:38] makes sense when you’re a whole generation behind or two generations behind or ahead.  
[00:56:45] That’s when it makes a meaningful difference in your die output or your  
[00:56:49] die area or functionality like power. But if you’re within a few percent,  
[00:56:59] you’re splitting hairs at that point in time, because it’s not very unidimensional.  
[00:57:06] It’s not just about density, it’s not just about raw performance.  
[00:57:11] Different applications require different vectors. You can be off by a few percent,  
[00:57:17] but you need to be on time. Your execution needs to be  
[00:57:20] such that your yields are very high to support very large and very rapid ramps.  
[00:57:27] That actually is more important than catching up on a few percent in performance or area.  
[00:57:33] I was looking at some SemiAnalysis numbers that seem to suggest that in  
[00:57:36] terms of transistor density, 14A — which will come out in 2028 — would be comparable to N2.  
[00:57:43] First of all, I would dispute your benchmarking.  
[00:57:47] But like I said, it’s important to be generally in the right ballpark and be very predictable.  
[00:57:56] Also, it’s not unidimensional. We don’t build one type of  
[00:58:01] transistor, let’s say 14A or 18A. You build a few different types of transistors.  
[00:58:08] There’s a low-leakage transistor, there’s a high-performance, high drive current transistor.  
[00:58:13] You’re building SRAMs. There’s a high-density SRAM, there’s a high-performance SRAM.  
[00:58:18] There are many other functionalities like analog circuits, RF circuits.  
[00:58:24] It’s the sum of all of those that makes a technology competitive.  
[00:58:29] I guess that makes the CapEx you do right now even more important.  
[00:58:34] TSMC is on track to do around $50 billion in CapEx this year.  
[00:58:38] You’re on track to do around $20 billion. If the tools you’re buying right now will  
[00:58:41] determine who can service all this crazy AI demand that’s coming up, it makes the difference  
[00:58:46] in CapEx right now even more important, or for the US versus other countries.  
[00:58:52] Yes, very much. It’s a little bit of an unfair comparison between us and TSMC today,  
[00:58:58] just because today they’re a foundry for basically everybody and we’re largely a foundry for Intel.  
[00:59:05] We’ll become a foundry for others. In due course, our CapEx will also grow.  
[00:59:11] Intel started as a DRAM business in the late ’60s. You guys were producing DRAM, which you sold off.  
[00:59:19] A couple years ago, you sold off your flash business.  
[00:59:25] Thoughts on that? For context for the audience, these are  
[00:59:28] now multi-trillion-dollar industries because they’ve just exploded as a result of AI demand.  
[00:59:36] Clearly, in hindsight, probably not the smartest time to sell off a flash memory business.  
[00:59:42] There were good reasons why we did that when we did.  
[00:59:46] Clearly, nobody could see this enormous demand. But today, the world will eat up as much compute  
[01:00:00] as can possibly be made, and it’ll eat up as much memory as can possibly be made.  
[01:00:06] I would argue that the supply crunch is larger for memory today than it is for compute.  
[01:00:12] Can I summarize what seems to me the takeaways from your projections?  
[01:00:16] You can tell me if that’s correct.  
[01:00:17] That marginal production can increase actually very fast — on the scale of 12  
[01:00:22] months — but the amount of increase up till the end of the decade is extremely limited.  
[01:00:27] Production could be higher next year than what people are forecasting, but production  
[01:00:30] in 2030 is not going to be significantly higher than what people are forecasting.  
[01:00:33] Unless the entire supply chain ramps up production very quickly.  
[01:00:36] We’re already in the middle of ’26, so there’s not that many years until the end of the decade.  
[01:00:42] Given the lead times… Let’s say you place an  
[01:00:45] enormous order for tools today, and you’re looking at 18 months to get those tools.  
[01:00:52] You’re already into basically ’28. From that point on, if you have to  
[01:00:57] build a new shell, build a new fab, you’re basically looking at the end of the decade.  
[01:01:02] I think it’ll be interesting to discuss the partnership you guys have with Elon on Terafab.  
[01:01:07] What’s going on there? Well, Elon’s publicly talked  
[01:01:14] about his desire to build a fab. We either build the Terafab or  
[01:01:19] we don’t have the chips. And we need the chips,  
[01:01:23] so we’re going to build the Terafab. Sort of the same thinking.  
[01:01:26] He’s seeing just an enormous increase in demand for silicon, for compute and for memory.  
[01:01:34] I think he came to the conclusion that his own businesses are going to require a lot of silicon.  
[01:01:42] He thought maybe he should just do it all on his own.  
[01:01:46] But unlike building a car, for example, this is such an intricate and complicated  
[01:01:52] process that we thought we could work together to help accelerate his bringing up his fab.  
[01:01:59] But because of the bottleneck at the tool level, it seems like the net  
[01:02:04] amount of silicon in the world won’t increase. It’s just that maybe if somebody were to start  
[01:02:09] a new fab, they would get access to guaranteed supply in a way that they wouldn’t have if they’re  
[01:02:14] working with another person’s foundry. It’s not just tools.  
[01:02:18] A fab does require a lot of power, a lot of water, a lot of consumables.  
[01:02:24] There are many other input variables as well. But those can be scaled in the  
[01:02:28] way that tools cannot. Some more than others, but yes.  
[01:02:34] In one sense, yes, we need a lot more equipment. But it is true, we also just need a lot more raw  
[01:02:42] fab space, raw clean room capacity. If you think of a foundry like Intel,  
[01:02:48] which has to build these expensive facilities and buy expensive tools, I wonder what you think the  
[01:02:55] economics of that fundamentally could look like, whether it could get more economical,  
[01:02:59] whether it could scale faster. Like I described earlier,  
[01:03:03] this is an extremely capital-heavy business. If you just plot how much it costs to build  
[01:03:11] a fab over the last 20, 30, 40 years, I think it’s doubling every 4-5 years.  
[01:03:19] Even inside the fab, if you look at the cost to do lithography, which is the most  
[01:03:24] expensive module — just patterning — that itself is doubling at more than that rate.  
[01:03:31] Today, a High-NA EUV scanner and all its associated equipment costs like $400 million.  
[01:03:41] So what does that mean? If that rate were to continue,  
[01:03:44] if you just draw the line, does that mean four years from now the cost of patterning  
[01:03:50] is going to be like $800 million? It doesn’t really make sense.  
[01:03:58] A very interesting thought exercise is to ask, are there things that could be  
[01:04:05] just very radically different that we could do today that we perhaps couldn’t do 20 years ago?  
[01:04:14] This is a very risk-averse industry for very good reason, for exactly that reason.  
[01:04:19] You put in tens of billions of dollars, and you really don’t want to take any risks.  
[01:04:25] You want to keep doing things the way they’ve been done for literally decades.  
[01:04:29] This is not just true of semiconductors, but everything really.  
[01:04:33] If you’ve just kept on doing that for decade upon decade, you just become indoctrinated.  
[01:04:42] There are engineers who probably work at Intel who are new, who come in and they’re taught, “This is  
[01:04:48] how the fab works, this is the process flow.” They just take that as gospel.  
[01:04:53] That’s just how it is done. But is that really the best  
[01:04:57] way to build a chip today? It’s a really valid question.  
[01:05:02] I’m very curious what you’re hinting at, because it could be anything from figuring  
[01:05:06] out ways to use fewer litho passes and economize on this expensive component, to maybe we need to  
[01:05:13] rethink the transistor. What is the level of—  
[01:05:19] All of the above. Transistor architecture is evolving.  
[01:05:25] Just the silicon transistor has continued to evolve over 30, 40 years, and that will continue.  
[01:05:33] You’ve seen the evolution from the planar transistor  
[01:05:36] to FinFETs to now gate-all-around transistors. There’ll be more. That roadmap exists, it’s pretty  
[01:05:44] well defined, with a lot of people working on it. But there are things like…  
[01:05:51] Do you really need a clean room today? Do you need the infrastructure to be as  
[01:05:58] sophisticated, as complex as it is today? Surely one can run an experiment where you  
[01:06:05] have people eating hamburgers and smoking cigars in the research fab and see what happens to yield.  
[01:06:12] That would be a great experiment to run, but no incumbent — Intel or TSMC or Samsung — would  
[01:06:20] want to willingly do that. That’s what I meant by this.  
[01:06:26] It’s a very risk-averse business, for good reason. Every one day lost in productivity is…  
[01:06:32] I don’t know how many dollars. But you save so much money in  
[01:06:35] not having to build clean rooms in the future. But it’s really the risk, the fear of the unknown.  
[01:06:41] Nobody is going to willingly take that risk. That’s why I think sometimes it’s good to just  
[01:06:49] start with a clean slate and rethink everything. The same thing applies to chip design, by the way.  
[01:06:59] Many of the ways we do CPU design were probably locked in 30 years ago.  
[01:07:06] Does that mean it’s smart to still do it the same way?  
[01:07:11] Probably not. But this is a very complex problem. In chip design, I guess the capacity to take  
[01:07:25] risk is maybe higher. This one, less so.  
[01:07:29] But given where the economics is today, I think it’s a very valid question to ask.  
[01:07:36] Maybe there’s a smarter way to do this. To close out, maybe we’ll start off at  
[01:07:40] the same question we began the interview with, which is, how does Intel respond to this crazy AI  
[01:07:47] demand that’s incoming and has already arrived? It sounds like what Intel ought to do — if the  
[01:07:54] ultimate bottleneck is that you guys already have these foundries, you already have the  
[01:07:58] ability to expand these foundries, but what you will eventually lack is the tools from upstream  
[01:08:05] in the supply chain — is to just raise as much capital as possible right now.  
[01:08:10] The same way that Nvidia has locked down memory and other components for reportedly hundreds  
[01:08:15] of billions of dollars worth of commitments that it’s made, Intel should maybe do the same thing:  
[01:08:21] make all these commitments so that over the coming years, the US is in good position to  
[01:08:28] have the bulk of semiconductor manufacturing at the most advanced levels happening here.  
[01:08:32] You’re suggesting we should be buying a lot more tools, right?  
[01:08:35] Yeah, because it sounds like otherwise in a couple years you’d just be in a position  
[01:08:39] where you’re like, “Oh man, we could be making trillions of dollars right now,  
[01:08:42] but all the tools are in Taiwan.” Yes, that’s a very valid question.  
[01:08:47] Had we known what we know today, we would have invested more like a year ago.  
[01:08:52] Knowing what we know now, I think we’ll be investing more.  
