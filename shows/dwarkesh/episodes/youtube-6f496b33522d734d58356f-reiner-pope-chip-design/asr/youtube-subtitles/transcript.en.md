# Chip design from the bottom up – Reiner Pope

[00:00:00] I'm back with Reiner Pope, CEO of MatX, a new AI chip company.  
[00:00:04] Last time we were talking about what happens inside a data center.  
[00:00:07] Now I want to understand what happens inside an AI chip.  
[00:00:10] How does a chip actually work? Full disclosure, by the way:  
[00:00:13] I am an angel investor in MatX. So hopefully you have designed a good chip.  
[00:00:19] Hope so. I'll start with the smallest fundamental unit of chip design, and we'll  
[00:00:25] build up to what an actual production chip is and what its components are.  
[00:00:30] At the very bottom level of a chip, the primitives we work with are logic gates,  
[00:00:37] very simple things like AND, OR, and NOT. These are connected together by wires that have to  
[00:00:42] be laid out physically as metal traces on a chip. The main function that AI chips want to compute  
[00:00:50] is the multiplication of matrices. Inside that, the fundamental primitive  
[00:00:54] is a multiply-accumulate of pairs of numbers. We're going to demonstrate what that calculation  
[00:01:01] looks like by hand, and then infer what a circuit would look like for that.  
[00:01:08] It'll be easiest if I do a multiply-accumulate of a four-bit number with another four-bit number.  
[00:01:20] The clearest primitive is actually multiply-accumulate.  
[00:01:24] So there's a multiply of these two terms, and then we're going to add in an eight-bit number.  
[00:01:40] Can I ask a clarifying question? Why is this the natural primitive for  
[00:01:49] whatever computation happens inside a computer? There are a few reasons.  
[00:01:55] It's a little bit more efficient, but the reason it's natural for AI chips is that if  
[00:02:00] you look at what's happening during a matrix multiply… What is a matrix multiply in short?  
[00:02:09] There's a for-loop over i, over j, and over k, of output [i,  
[00:02:21] k] += input [i, j] x other input [j, k]. A multiply-accumulate happens at every  
[00:02:36] single step of a matrix multiply. The other observation is that the  
[00:02:40] precision will almost always be higher in the accumulation step than in the multiplication step.  
[00:02:45] This is specific to AI chips. You're multiplying low-precision numbers,  
[00:02:49] and then when you accumulate, errors accumulate quickly, so you need more precision there.  
[00:02:54] This is why we've chosen to do a four-bit multiplication and an eight-bit addition.  
[00:02:58] Let me make sure I understood that. There are two ways to understand that.  
[00:03:01] One is that the value will be larger than the inputs.  
[00:03:06] The other is that if it was a floating-point number it would be…  
[00:03:10] Maybe that part is less intuitive to me. But maybe it's the same principle?  
[00:03:14] It really is the same principle. The separate principle is that as  
[00:03:20] you're summing up this number, you're summing up a whole bunch of numbers, so you've got a  
[00:03:23] lot of rounding errors accumulating. Whereas in this case, there's only  
[00:03:28] one multiplication in the chain, so there aren't a lot of rounding  
[00:03:30] errors accumulating in the multiplication. Why are you summing up a whole bunch of numbers?  
[00:03:33] There’s just two numbers there. This summation is repeated j many times.  
[00:03:39] Any errors accumulate. I see. So how would we perform this calculation by hand?  
[00:03:45] As a human, we would probably separate it into two, but we can do  
[00:03:48] it all in one using long multiplication. For the multiplication term first, we're  
[00:03:55] going to multiply this four-bit number by every single bit position in the other four-bit number.  
[00:04:03] We write that out. First, 1001 multiplied by this bit position.  
[00:04:10] That is the number itself. Then shifted across by one,  
[00:04:14] we're multiplying by 0. That gives us an all-0 number.  
[00:04:20] Shifted across one more to multiply by this one, we get 1001.  
[00:04:28] Finally, for this last bit position, we get an all-0 number again.  
[00:04:37] This gives us a bunch of terms that we have to add for the multiplication.  
[00:04:43] While we're doing that summation, we might as well add in the actual accumulator term as well.  
[00:04:50] So we just copy that directly across. So this is the sum.  
[00:05:00] It's a five-way sum that we want to compute.  
[00:05:07] What logic gates did it take us to get to this intermediate step?  
[00:05:12] We needed to produce all 16 of these partial products.  
[00:05:17] How do I produce one of these partial products? Let's take this number 1, for example here.  
[00:05:26] We produce it by multiplying this number by this one over here.  
[00:05:31] We can produce that with an AND gate. This number is 1 if both this bit  
[00:05:35] is 1 and this bit is 1. If either of them is 0,  
[00:05:37] then the multiplication of 0 times anything is 0. To produce all of this, we ended up  
[00:05:45] consuming 16 AND gates. In the general case,  
[00:05:50] if I were doing a p bit multiply times a q bit multiply, this will be p times q many ANDs.  
[00:06:10] Finally, I sum them. Most of the work is going to happen in the summing.  
[00:06:15] Let me describe the other logic gate that we use here.  
[00:06:20] AND is almost the simplest logic gate that exists on a chip.  
[00:06:23] It's almost the smallest. At the other extreme, the very largest logic gate you'll typically use  
[00:06:30] is something called a full adder. Coming from software, you might think  
[00:06:39] that a full adder adds 32-bit numbers together. In this case, it just adds three single-bit  
[00:06:43] numbers together, so you can think of it as adding 0, 1, and 1 together.  
[00:06:50] When I add these together, the result can be 0, 1, 2, or 3, so I can express that  
[00:06:54] in binary using just two bits. As input, it has three bits.  
[00:06:58] As output, it has two bits. The number 2 in binary is 10.  
[00:07:06] This is also known as a 3→2 compressor because it takes three bits of input  
[00:07:17] and produces two bits of output. Just to make sure I understood: the  
[00:07:19] two inputs are an X and a Y value and then some carry that came in…  
[00:07:27] The three inputs are all bits in the same bit position, like three bits in a column here.  
[00:07:35] The two outputs, I've drawn them vertically here and horizontally here to match this  
[00:07:41] vertical versus horizontal layout. This expresses that things in the same  
[00:07:45] column are in the same bit position, whereas things in adjacent columns are different.  
[00:07:50] This is a carry out, whereas this was the sum. So if the inputs in the full adder were, say,  
[00:07:56] 101, then the output would be 10. If it were 111, it'd be 11.  
[00:07:59] If it were 000, it'd be 00. If it were 010, it'd still be 01.  
[00:08:06] Got it. Yeah. It's essentially just counting the  
[00:08:09] number of things and expressing that in binary. This circuit captures what we as humans naturally  
[00:08:17] do when we're summing along a column. I'll show one iteration of using  
[00:08:24] the full adder to sum. The way I sum here is going  
[00:08:27] to be a little unnatural for humans. We would sum along the column and then  
[00:08:31] remember the carry, but instead of remembering the carry, we'll explicitly write it out.  
[00:08:39] We proceed from the rightmost column toward the left.  
[00:08:42] On the rightmost column, we sum the 1 and the 1, and that produces a zero here and a carry of one.  
[00:08:51] We've used this full adder circuit on this pair of bits and produced a pair of bits as output.  
[00:08:59] Now we can do the same thing with this column. We have a column of four numbers, so we'll take  
[00:09:04] the first three of them, run a full adder on them, and that gives us a 0 and a 0 as output.  
[00:09:12] The sum of these is 00. That's the full adder applied to all these bits.  
[00:09:18] As I've used up bits, I'll cross them out to indicate that I've handled them.  
[00:09:25] Let's keep going a little bit more. I take these three numbers, I add  
[00:09:31] them, and that gives me a 1 and a 0. I've dealt with these three numbers.  
[00:09:36] Now I take these three numbers and add them, and that gives me a 1 and a 0,  
[00:09:44] and I've dealt with these numbers. The way to view this is that I have  
[00:09:51] this whole grid of numbers that need to be added. I'm going to keep applying full adders to all the  
[00:09:57] bits here, constantly removing three numbers from a column and writing out two numbers as output.  
[00:10:03] Keep going over and over again until I eventually get just one single number coming out.  
[00:10:16] This approach is called a Dadda multiplier. This is the standard for how you do  
[00:10:31] area-efficient multipliers using full adders. Let's try to quantify the circuit size of  
[00:10:38] this so we have a sense of how big things are and can compare them later.  
[00:10:44] How many full adders did I use? How many numbers did I start with?  
[00:10:50] I have the 16 partial products, which is a product of all of these terms with all of these terms,  
[00:10:57] plus the eight terms that I'm adding here. I started off with 24 bits.  
[00:11:06] Eventually I produced eight bits on the output. In every step, I was crossing off three numbers  
[00:11:14] and writing two numbers out as a result. Every single use of a full adder eliminates  
[00:11:20] one of the bits here. So how many full adders?  
[00:11:23] It must be 24 minus 8, so there were 16 full adders in this circuit.  
[00:11:30] This is true in the general case as well. There will be p times q many  
[00:11:34] full adders in this circuit. Let me make sure I understand the logic of that.  
[00:11:39] The input bits, 24, is p x q, plus p + q. The output bits are just p + q.  
[00:11:42] So p x q plus p + q, minus p + q equals p x q. That's right. I think this explains,  
[00:12:00] or at least hints at, the second reason we chose to do a multiply-accumulate.  
[00:12:06] The first reason is that it's what shows up in matrix multiplication.  
[00:12:10] The second is that it gave us this very slick, simple p x q, very simple algebra.  
[00:12:17] We've described this whole procedure. Every single atomic step that I took  
[00:12:22] here becomes a logic gate, and then the wires are connected together.  
[00:12:26] When I had these three inputs that I used to produce these two outputs, if I think of mapping  
[00:12:31] this to a physical device, there would be a wire connecting all three of these things together  
[00:12:38] into a logic gate that produced this output. This is the main primitive, at different bit  
[00:12:46] widths, that's inside an AI chip. We're going to build up from here  
[00:12:54] to how you would use it to run all the other operations you might want.  
[00:12:58] This might be the wrong time to ask, but whenever Nvidia reports that this chip  
[00:13:02] can do X many FP4 or half as many FP8, it seems to imply those circuits are fungible,  
[00:13:11] that there's not a dedicated FP4 versus FP8. But the way you're mapping it out here, it seems  
[00:13:17] like if it has to be mapped out in the logic, you would need a dedicated FP4 multiply-accumulate and  
[00:13:27] then a dedicated FP8 accumulate. Can you "funge" them?  
[00:13:33] As drawn, they're not particularly fungible. This is actually one of the main choices you  
[00:13:37] have to make when designing a chip: how much of FP4 and how much of FP8 do I have?  
[00:13:42] Sometimes I'll make that consideration from the point of view of the customer requirement.  
[00:13:47] Another angle is to equalize the power budget between FP4 and FP8.  
[00:13:55] When they report those numbers and it just happens to be the case that it does 2x as many FP4 as FP8,  
[00:14:02] they're just choosing to give equivalent die areas to all the floating points,  
[00:14:08] and as a result it ends up being…? Why is the ratio exactly 2x?  
[00:14:13] Part of it is that surely it won't be exactly equivalent to die area.  
[00:14:20] There's a data movement reason. We'll maybe come back to this when we  
[00:14:24] look at how it goes into and out of memories. There's something really nice from a software  
[00:14:28] level about the fact that I can pack two four-bit numbers into the same  
[00:14:32] storage as an eight-bit number. When I store that to memory,  
[00:14:36] the sizing of the buses that I wire out within the chip makes that work out really nicely.  
[00:14:44] Come to think of it, it's not just 2x. The amount of area it takes sounds like  
[00:14:54] it's quadratic with the bit length. That's why smaller precision is even  
[00:15:00] more favorable than you might think. This is a really big reason.  
[00:15:04] In fact, Nvidia made a change. Historically, up until B100 or  
[00:15:10] B200, every time you halved the bit precision, you doubled the FLOP count.  
[00:15:18] For the reason you said, because of this quadratic scaling, that ratio is actually slightly wrong.  
[00:15:21] You should get an even bigger speedup than you might otherwise think.  
[00:15:28] Nvidia’s product specs have started acknowledging that in B300 and beyond, where the FP4 is three  
[00:15:34] times faster than the FP8. Though it should be 4x.  
[00:15:38] Yeah. What I've shown here is the simplest case of integer multiply.  
[00:15:42] When you're dealing with floating point, as you do in FP4 and FP8, there's this other term,  
[00:15:49] the exponent, that complicates the calculation. What can we see already from this?  
[00:15:54] I think the big observation you've made is that there's this quadratic scaling with bit width,  
[00:16:00] which is very effective and is the single reason low-precision  
[00:16:04] arithmetic has worked so well for neural nets. The other thing we're going to do now is compare  
[00:16:11] the area spent on the multiplication itself with all the circuitry around it.  
[00:16:20] We'll walk back in time a little bit and see how GPUs prior to Tensor Cores worked,  
[00:16:28] which is in fact the same way CPUs worked. Where do we stick this multiply-accumulate unit?  
[00:16:37] Generically, I'll describe a CUDA core or a CPU. You'll have some register file which stores some  
[00:16:47] number of entries, maybe eight entries of, in this case, 4-bit numbers, but typically 32-bit numbers.  
[00:17:03] Inside the CUDA core, I'll have some register file of some depth,  
[00:17:06] and then I'll have my multiply-accumulate circuit. What it's going to do is take three arbitrary  
[00:17:18] registers from this register file, perform the multiply-accumulate,  
[00:17:21] and then write back to the register file. It's going to write to this one,  
[00:17:25] but it was able to read from this one, this one, and another random one.  
[00:17:31] It will take three inputs like this. This is the core data path of many processors.  
[00:17:39] Most processors look like this. You've got some set of registers, and  
[00:17:42] then you've got some set of logic units, or ALUs. We want to analyze the cost of the data movement  
[00:17:50] from the register file to the ALU and back. Ultimately, there's going to be some  
[00:17:58] circuit that says, "Well, I don't always have to select this guy.  
[00:18:01] I might select any of the registers at any point in time."  
[00:18:04] The first question is: how can I build a circuit? The circuit I'm going to look for is a mux.  
[00:18:13] In this case, it's going to have eight inputs, one from each entry of the register file,  
[00:18:17] and it's going to have one output, which is actually producing this output.  
[00:18:26] What is the cost of this thing? All we have to build it out of is AND and OR.  
[00:18:32] How do we build it? We do the dumbest thing possible.  
[00:18:37] We form a mask. When we want to read the third entry, we're going to AND every  
[00:18:44] single entry with either 1 or 0 based on whether that's what we want to read,  
[00:18:48] and then we're going to OR all of them together. Just to make sure I understand the basics.  
[00:18:52] What the mux is doing is just selecting an input? Just selecting, invisible to software.  
[00:18:59] You say "I want input number three," and that means there's a mux here.  
[00:19:02] So what is the cost of this mux? An n-input  
[00:19:10] mux operating on p bits. I have n rows. That's just eight  
[00:19:21] rows, and each row is p bits wide. I have to AND every single bit,  
[00:19:25] so I get n x p many AND gates. For every single input I have to decide  
[00:19:32] whether I'm going to mask it out or not. Then I'm going to OR them all together.  
[00:19:38] There's going to be n – 1 times p many OR gates. I've got all of these different things,  
[00:19:47] almost all of them are 0s, but I need to collapse them from my eight options down into one option.  
[00:19:54] Every step, I need to OR one row into an existing row.  
[00:19:59] It's actually funny that you don't think at the level of hardware.  
[00:20:04] You just think, "Oh, I'll just select element three," and something as simple as that is  
[00:20:11] in and of itself quite a complicated circuit. This is the first step of all of the hidden  
[00:20:15] data movement costs that show up. We're just going to compare.  
[00:20:23] I have to pay this cost. I've got one mux here, and in fact  
[00:20:26] I have two more copies of that for each of the three inputs to my multiply-accumulate operation.  
[00:20:30] I have this cost, which is 3 x n x p AND gates over here, compared to p x q gates in the actual  
[00:20:42] circuit that is doing the thing I care about. If we plug in actual numbers, with n being  
[00:20:49] eight, I get 24 x p gates just in the data movement, compared to—if q is four—4 x p  
[00:21:00] gates just in the multiply-adder. Where is the three coming from?  
[00:21:05] Three different inputs here. What I'm hinting at is that all of this work,  
[00:21:14] which scales as the size of the register file—and this is a very small register  
[00:21:18] file—all of this work just moving the data from the register file to the logic unit is many,  
[00:21:26] many times more expensive than the logic unit. In the most recent ClusterMAX report, SemiAnalysis  
[00:21:31] ranked almost 100 different GPU clouds. Crusoe was one of only five that made the gold tier.  
[00:21:36] SemiAnalysis found that gold-tier providers like Crusoe had a total cost of ownership that  
[00:21:41] was 5% to 15% lower than silver-tier ones, even when they had identical GPU pricing.  
[00:21:46] This makes sense because total cost of ownership is downstream of a bunch of different things that  
[00:21:50] don't necessarily show up in the sticker price, but that Crusoe has optimized.  
[00:21:54] Things like how well you detect faults and how quickly you replace failed nodes.  
[00:21:58] For example, Crusoe was one of the first clouds to adopt NVSentinel, NVIDIA's own GPU monitoring  
[00:22:04] and self-healing software for enhanced GPU uptime, utilization, and reliability.  
[00:22:09] This lets Crusoe make use of everything that NVIDIA has learned about why chips fail across all  
[00:22:14] their different fleets and deployments, so that Crusoe can catch faults earlier in the process.  
[00:22:18] And once they identify a failure, Crusoe can swap in a healthy node in less than 10 minutes.  
[00:22:23] Because they’re not running bare metal, Crusoe doesn't have to spend time installing an  
[00:22:27] operating system or configuring drivers. They can just spin up a new VM on an  
[00:22:31] already running and pre-qualified host. If you want to learn more about this or  
[00:22:34] the other reasons that Crusoe made gold tier, go to crusoe.ai/dwarkesh.  
[00:22:41] It may be helpful to just see what a mux looks like,  
[00:22:44] maybe a two-bit or a four-bit mux. We’ll do a two-way mux.  
[00:22:53] We've got two different numbers, we’ve got these two inputs.  
[00:23:03] These are the inputs that are being selected between, and the selector can either be "I want  
[00:23:16] this one" or "I want the other one." This is a one-hot encoding.  
[00:23:24] This is what we start with. Let's focus on this case.  
[00:23:34] This is the actual input we got, and we want to produce this guy as the result.  
[00:23:42] Very laboriously, we AND this bit with all of these.  
[00:23:50] That produces ANDing this bit with this row. Likewise, we AND this bit with this row.  
[00:23:55] That produces all 0s. There are four ANDs here. Finally,  
[00:24:07] we OR these two together, and this gives a 1. We OR these two together, this gives a 1.  
[00:24:09] We OR these two together, it gives a 0. We OR these two together and it gives a 1.  
[00:24:15] Those are the four ORs. This actually ends up  
[00:24:22] looking a little bit like addition. We did exactly the same set of ANDs.  
[00:24:28] We've ANDed all of these things together, but then instead of collapsing it by using  
[00:24:34] full adder circuits, we just get a very simple collapsing with OR gates.  
[00:24:38] But that doesn't look like n times p. This was with n=2 inputs.  
[00:24:48] In the general case, we will have n rows, and we'll have p bits per row.  
[00:25:03] That gives us the n times p many AND gates. In this circuit I've described, almost all of  
[00:25:11] the cost, seven-eighths of the cost, is in reading and writing the register file, and only a tiny  
[00:25:19] fraction of the cost is in the logic unit itself. This is the problem to solve.  
[00:25:24] This essentially was the state of play prior to the Volta generation of Nvidia GPUs.  
[00:25:31] This kind of thing is what was inside the CUDA cores.  
[00:25:37] This problem statement is what motivated the introduction of Tensor Cores,  
[00:25:41] which are more generically called systolic arrays. Think about how we're going to solve this problem.  
[00:25:46] We're spending almost all of our circuit area on something that we  
[00:25:48] really don't care about and is hidden to the software programmer, and the thing that we  
[00:25:52] actually care about is not much of the area. Make this one bigger somehow while keeping  
[00:25:57] this at the same size. That's the goal.  
[00:26:01] The evolution was that we had baked this much into hardware at this stage.  
[00:26:06] This single line is a multiply-accumulate, and this single thing was baked into hardware.  
[00:26:11] The idea of a systolic array is to go two levels of loops up and bake this  
[00:26:17] entire loop out here into hardware. The idea is that if we have a much  
[00:26:22] bigger granularity fixed-function piece of logic, maybe the taxes we  
[00:26:27] pay on the input and output are much smaller. Interesting. It sounds like you're suggesting  
[00:26:30] that if you go up one step in the matrix multiply loop, you can tilt the balance  
[00:26:41] more towards compute than communication. That's right. There are two effects we're  
[00:26:46] going to take advantage of here. One is that we can do more stuff  
[00:26:49] per every trip through our register file. The other is that in some of this loop, we can  
[00:26:58] take advantage of certain things staying fixed. Visually, we're going to look at this  
[00:27:07] matrix multiplication. This portion of the loop  
[00:27:09] corresponds to a matrix-vector multiplication. We'll take a matrix and multiply it by a vector.  
[00:27:21] How do we do this? Every column gets  
[00:27:23] multiplied by the vector and then summed. We're going to sum along columns.  
[00:27:28] This 0 and 3 gets multiplied by the 3 and 7 and gets summed, and then the 1 and 2  
[00:27:32] gets multiplied by the 3 and 7 and gets summed. There is a multiply-accumulate associated with  
[00:27:38] every single one of these entries in the matrix. We'll draw out these four multiply-accumulates.  
[00:27:53] Just to make sure I understand why there are four multiply-accumulates: each entry in the  
[00:28:01] column that corresponds to the output vector is a dot product, and in this  
[00:28:09] case it will be two multiplications and then the addition of those two multiplications.  
[00:28:16] You're accumulating... Really there's only one addition per  
[00:28:20] dot product, but we like to start with zero. But it includes the initialization of zero.  
[00:28:23] Yeah. We want to have quadratically more compute.  
[00:28:30] We have x times y as much compute as we had before.  
[00:28:41] But we want to aim for having only x times as much communication.  
[00:28:52] The intention is to get this advantage term going as y.  
[00:28:57] We've laid down the multiplications. We want to bring in a vector of size two, and  
[00:29:06] that is already in line with our columns target. That's fine. However, we need to manage the  
[00:29:11] communication of this matrix, which exceeds our budget of x.  
[00:29:18] The idea is that in an AI context, this matrix is going to stay fixed for a long period of time.  
[00:29:29] We've got some register files sitting over here. The amount of stuff coming out of this register  
[00:29:36] file… this is the term that we want to go as x, in some sense.  
[00:29:43] We don't want to bring this full matrix in from the register file every cycle,  
[00:29:47] because that would cost too much in terms of wiring from the register file.  
[00:29:55] Our key trick is that this matrix can be stored locally to the systolic array.  
[00:30:04] We'll store these numbers 0, 1, 2, and 3 in a gate called a register that physically  
[00:30:15] stores these numbers, and we're going to reuse these numbers over and over again  
[00:30:19] for a large number of different vectors. The optimization here is that the nature of  
[00:30:23] matrix multiplication is that you can store this square quadratic thing directly where the logic is  
[00:30:35] happening, which has an extra dimension compared to the inputs that you keep swapping in and out.  
[00:30:45] That’s right. This is the nature of  
[00:30:46] what a matrix multiplication is. You do a lot of multiplication  
[00:30:52] to get one value out. A dot product is the  
[00:30:55] result of a lot of multiplications. So that optimization means you can  
[00:30:59] stuff a lot of multiplication in before you get some value out of it.  
[00:31:03] That's right. Just to complete the picture of concretely how that looks:  
[00:31:09] I swapped the 3 and the 2 here. Just like this 0 and 3 is going  
[00:31:17] to multiply by the 3 and the 7, we're going to form a dot product along columns here.  
[00:31:26] We're going to feed a 3 and a 7 in here. This feeds into this multiplication and also  
[00:31:35] feeds into this multiplication. Likewise, the 3 feeds  
[00:31:39] into here and also into here. Then we're going to sum along here.  
[00:31:49] Starting at the top of a column, we feed in 0s, and then coming out the bottom we get results.  
[00:31:55] Visually, there's a dot product performed along columns in a matrix, and that maps exactly to  
[00:32:03] what is done spatially in the systolic array. This is one dot product summed vertically,  
[00:32:09] and this is a second dot product also summed vertically.  
[00:32:13] What is the data that needs to go into and out of the register file?  
[00:32:17] We have x amount of data coming out on the output, and we also  
[00:32:23] have x amount of data coming from the input. With respect to the input and output vectors  
[00:32:33] at least, we've met our goal of having only x as much data going in and out of the register file.  
[00:32:44] This leaves open the question: I said the weight matrix is stored locally in the systolic  
[00:32:51] array, so how did it get there in the first place? At some point, you need to boot your chip and  
[00:32:56] populate this data, so where did that come from? The trick is that we just do it very slowly.  
[00:33:02] We very slowly trickle-feed it into the systolic array.  
[00:33:07] The simplest strategy is that we run this daisy chain: feed a number in here,  
[00:33:13] and on the next clock cycle it will move down to the next entry of the systolic array.  
[00:33:18] We can do that in every column in parallel, this is also going to come from here,  
[00:33:26] and that gives us another factor of approximately x units of bandwidth coming in.  
[00:33:32] Would you mind repeating that sentence one more time?  
[00:33:36] We know that we're going to be bringing numbers only rarely into the matrix.  
[00:33:43] We just want to come up with any construction at all such that the amount of wiring that  
[00:33:48] crosses the boundary of the systolic array is bounded to x and not go as xy.  
[00:33:56] A particularly simple strategy is that we bring a number into the top row of  
[00:34:03] the systolic array in one clock cycle. Then, for y consecutive clock cycles,  
[00:34:11] we bring in the top row every time and shift all the other rows down by one.  
[00:34:16] This keeps the wiring that needs to come from this expensive register file  
[00:34:22] only down to a factor of x rather than xy. I see. There are two questions in terms  
[00:34:27] of communication: communication time and communication bandwidth.  
[00:34:33] You're saying that since we're only going to be loading this in once, let's minimize bandwidth,  
[00:34:39] because bandwidth equals die area. We load it in slowly over smaller  
[00:34:45] lanes because we're just going to keep this value in there for a while.  
[00:34:48] Exactly. It's interesting to me that when we were talking  
[00:34:52] last time about inference across many chips, the big high-level thing we're trying to optimize for  
[00:34:58] is increasing the amount of compute per memory bandwidth, that is to say, per communication.  
[00:35:03] Here also, we're trying to increase the amount of actual multiplies  
[00:35:08] or additions relative to transporting information from registers to the logic.  
[00:35:16] In both cases, you're trying to maximize compute relative to communication.  
[00:35:20] This shows up all the way up and down the stack. This is close to the bottom, to the gates.  
[00:35:28] There's a version that's maybe even closer to the gates in the precision of the number  
[00:35:34] format that you choose to use. We saw that same effect.  
[00:35:39] There's a squared versus linear term going on both purely in the precision of the ALU,  
[00:35:47] but also in the size of the matrix. This unit is the next bigger unit.  
[00:35:55] We had the multiplication circuit, and on top of that we have a pretty large systolic array.  
[00:36:01] I drew it as 2x2, but older TPUs were described as 128x128 of this circuit shown here.  
[00:36:12] This ends up being the most efficient known circuit for implementing a matrix multiply.  
[00:36:21] We've talked about how it seems obvious that you should try to  
[00:36:26] maximize compute relative to communication. What are non-obvious trade-offs that  
[00:36:35] keep you up at night, about whether you should do X or Y and it's not obvious what the answer is?  
[00:36:41] Most of the decisions in chip design are sizing decisions.  
[00:36:48] Already in what we've drawn so far… AI chips all have this circuit in them.  
[00:36:56] They have a systolic array, and somewhere near it a register file providing inputs and outputs.  
[00:37:06] Even within this scope, the sizing questions you have are: how big should I make my systolic array,  
[00:37:11] and how big should I make the register file? These two questions are coupled.  
[00:37:25] One way to think of it is to set a budget for what percentage of chip  
[00:37:32] area you want to spend on data movement. Maybe I say that I want this to be 10%  
[00:37:36] and the systolic array to be 90%. Then I can size my register file.  
[00:37:42] Bigger register files are more flexible. They allow me to get more application-level  
[00:37:47] performance out, but they take away from the area spent on the systolic array.  
[00:37:55] I recently ran an essay contest where I asked people to write about what I consider to be some  
[00:37:59] of the biggest open questions about AI. The submission window closed last week,  
[00:38:03] so I used Cursor to create a couple of different interfaces to help me review the entries.  
[00:38:07] One interface anonymizes submissions and hides the necessary information.  
[00:38:10] It lets me group responses by question, add notes, and record my scores.  
[00:38:14] The other interface helps me review entrants who also want to be considered  
[00:38:17] for the researcher role that I'm hiring for. The UI puts the applicant's essay right next  
[00:38:21] to their resume and their personal website so that I can see everything at once.  
[00:38:25] Cursor's harness is really good at helping these models see and improve their UIs.  
[00:38:29] I watched it render these interfaces in the built-in browser, take screenshots,  
[00:38:33] click through sections, and keep iterating. At this point,  
[00:38:36] Cursor is where I do most of my work. Whether I'm reading and visualizing a bunch  
[00:38:40] of research papers, or coding up an interface to review applications, or making flashcards for my  
[00:38:45] blackboard lectures, Cursor just makes it very easy for an AI to look at whatever I'm looking at  
[00:38:50] and help me understand it and work with me on it. So whatever you're working on,  
[00:38:54] you should do it in Cursor. Go to cursor.com/dwarkesh.  
[00:39:00] Where does the clock cycle of a chip come in? What determines what that is?  
[00:39:08] And what is a clock cycle of a chip? At baseline, it's worth observing  
[00:39:12] that chips are incredibly parallel. You've got 100 billion transistors in a chip.  
[00:39:16] A key thing you need to do whenever you have massive parallelism is synchronize  
[00:39:21] between the different parallel units. In software, typically you have these very  
[00:39:27] expensive synchronization methods like a mutex. One thread will finish what it's doing,  
[00:39:34] grab a lock stored somewhere in memory, and notify the other thread that it's done.  
[00:39:39] On chips, we take a very different approach. Every nanosecond or so, all circuitry in the chip  
[00:39:50] will pause for a moment and synchronize. That is the clock cycle.  
[00:39:58] The entire chip typically goes in lockstep to the next operation in one fell swoop.  
[00:40:06] What this looks like in circuitry is that the clock is mediated by registers, which  
[00:40:17] are these storage devices we've drawn elsewhere. The way to think of it is: I have some storage  
[00:40:24] holding a bit, which might be 0 or 1. Then I have some cloud of logic,  
[00:40:29] which maybe is this systolic array or multiplier. I have a bunch of inputs feeding into this cloud  
[00:40:42] of logic, and eventually there's going to be some output register that it writes to.  
[00:40:48] There is a global clock signal driving all these registers.  
[00:40:57] At a certain instance in time, when the clock strikes, whatever value happens to be on that  
[00:41:05] wire at that instant is what gets stored. The challenge is that I would like to have  
[00:41:15] my clock speed run as fast as possible. If I run at two gigahertz, I get twice as  
[00:41:19] many operations done per second as if I run at one gigahertz.  
[00:41:24] But what that ends up meaning is that I'm very sensitive to the delay through this cloud of  
[00:41:30] logic, because any computation happening in there needs to finish before the next clock cycle hits.  
[00:41:40] A major point of optimization on any chip is to make this delay as short as possible.  
[00:41:53] Interesting. The constraint here seems to be that if you add too much logic,  
[00:42:02] you might risk missing the clock cycle. But if you don't add enough, you're  
[00:42:07] leaving potential compute on the table. Is there ever a situation where you take  
[00:42:15] a probabilistic chance that a computation finishes, or is it strictly that it either  
[00:42:23] finishes by the clock cycle or it doesn't? In standard chip design, you margin it such  
[00:42:28] that there is a probability, but it's many standard deviations out.  
[00:42:34] For all intents and purposes, it is a reliable part and will always meet the clock.  
[00:42:40] There are some weird exceptions, like clock domain crossings where you go from one clock to another.  
[00:42:45] Then you actually do have to reason about this probability.  
[00:42:47] But in the main path, you margin it such that you'll get there 25% of the clock cycle in  
[00:42:55] advance, making it very unlikely that it misses. Where the clocks synchronize, where the  
[00:43:07] registers are, is this something you determine as a chip designer?  
[00:43:11] Or is it an artifact where you want a certain sequence of logic, and the software you use to  
[00:43:18] convert your Verilog into what you send to TSMC just determines that to make it work,  
[00:43:25] you have to put a register here, here, and here, making sure no single step makes the  
[00:43:33] whole chip's clock cycle longer than it has to be? Inserting them is actually a huge part of the  
[00:43:38] work of designing a chip. It's done by a combination  
[00:43:42] of manual and automatic methods. To show the very dumb version of  
[00:43:48] what you can do here, you can take this logic and split it in half.  
[00:43:53] Instead of just one cloud of logic, I can have two smaller clouds of logic that do the same thing,  
[00:44:02] but split them up by a register. If you split it in the middle,  
[00:44:13] you can hit twice the clock frequency. That's great, you get twice the performance,  
[00:44:17] but at the cost of an extra register, which means more storage.  
[00:44:22] Stepping back, why do we need to synchronize the whole chip?  
[00:44:25] If you imagine playing Factorio or something, there's no global clock cycle.  
[00:44:28] Things are just done when they're done. There's iron on the plate, and you can  
[00:44:31] take it if you want. Taking that analogy,  
[00:44:36] the thing you need to be mindful of is if I have two different paths through some logic.  
[00:44:41] Say I have to do computation f here and computation g here,  
[00:44:47] and they're going to meet for computation h. There's going to be manufacturing variance.  
[00:44:59] In some chips f will take a little longer; in some chips g will take a little longer.  
[00:45:03] If I have a signal propagating through, and the results from f and g have to meet up at h,  
[00:45:12] what can go wrong is that f gets there early and it meets the previous  
[00:45:16] value of g, or the next value of g. Ah. And h needs to know when to start,  
[00:45:21] when the next iteration has… Exactly.  
[00:45:24] This explains why different chips made at the same process node, the same TSMC  
[00:45:32] technology, can have different clock cycles. Two chips made at 3 nm might have different clock  
[00:45:38] cycles based on whether they were able to optimize to ensure no single critical path is so long that  
[00:45:48] it slows down the whole chip's clock cycle. That's right. This optimization I showed here  
[00:45:53] is called pipeline register insertion. We've inserted a register in the  
[00:45:59] middle of the pipeline. This is a pure trade-off  
[00:46:02] between clock speed and area. That is the easy case.  
[00:46:08] There is a harder case too. I drew out a pipeline of logic,  
[00:46:14] but in other cases you may have some calculation which actually feeds back in on itself.  
[00:46:22] It runs some function f and then writes back to itself.  
[00:46:27] For example, this might be an addition where you're adding a number every clock cycle.  
[00:46:43] This little circuit essentially sums all the numbers presented on different clock cycles.  
[00:46:49] The challenge is, if this plus takes too long, what can I do?  
[00:46:54] If I try to put a pipeline register right in the middle of it, it  
[00:47:05] changes the computation that's done. Instead of forming a running sum  
[00:47:08] of everything that comes in, I will actually have two different running sums.  
[00:47:12] I'll end up with a running sum of the even numbers and a running sum of the odd numbers.  
[00:47:18] This constraint—where I have a loop in my logic, which all chips have somewhere—is the hardest  
[00:47:25] thing to address and sets the clock cycle. I don't understand why it would be  
[00:47:29] a problem to have that. I'm not even sure what it  
[00:47:30] would mean to have a register there. Is it a sort of atomic operation?  
[00:47:36] Well, plus is not really atomic. As you just demonstrated.  
[00:47:41] It took a whole lot of work to do a summation. You can take the early parts of that work,  
[00:47:45] stick a register in the middle, and then take the late parts of that work.  
[00:47:48] Okay. TSMC offers a PDK which specifies the primitives of  
[00:47:58] logic they can grant you in the chip. It's up to them to determine that no  
[00:48:03] primitive is bigger than the clock cycle they're hoping a process node targets.  
[00:48:10] But other than that, can't you just take all the primitives from TSMC and keep adding  
[00:48:19] registers between them as much as needed until you get to your desired clock cycle?  
[00:48:24] As a logic designer, the chip architect sets the clock cycle.  
[00:48:28] For example, the primitives you get from TSMC are on the order of AND gates or full adders.  
[00:48:36] It depends a lot on voltage and which library you choose, but generally you can have about 10, 20,  
[00:48:46] or 30 of these sequentially in a clock cycle. These primitives are very fast,  
[00:48:51] maybe 10 picoseconds. As a logic designer, in principle,  
[00:48:57] if you just had a register and an AND gate in a loop, you could get an insanely fast clock speed,  
[00:49:07] more than four, five, or six gigahertz. But if you take this really simple circuit  
[00:49:16] and look at the area you're spending here… This is called one gate equivalent  
[00:49:23] in size, so unit of one in area. This thing is maybe a unit of eight in area.  
[00:49:31] Again, almost all your cost becomes synchronization or  
[00:49:34] communication cost compared to the actual logic. This would be a case where you've gone too far.  
[00:49:40] You've made your clock speed really fast at the cost of spending almost  
[00:49:43] all of your area on pipeline registers. Interesting. So you're hinting at a dynamic  
[00:49:50] where you can have a really fast clock speed but you're not getting that much work done.  
[00:49:56] You can have low latency but low throughput. It hurts your throughput, in fact, because  
[00:50:05] the throughput of your chip is the product of how much you get done per clock cycle—which  
[00:50:11] is based on area efficiency—times how many clocks you get per second.  
[00:50:15] This is actually so similar to the thing we were discussing last time about batch size,  
[00:50:21] where if you have a low batch size, any one user can receive their next token really fast,  
[00:50:28] but the total number of tokens processed in, say, an hour will be lower than it could otherwise be.  
[00:50:34] Exactly. You get less parallelism out if you drive your clock speed up really high.  
[00:50:39] Language models are starting to compete against the best human forecasters.  
[00:50:42] I sat down with two senior Jane Streeters, Ron Minsky and Dan Pontecorvo, and asked: at some  
[00:50:48] point, does AI just do what Jane Street does? There's a world that we should take seriously  
[00:50:52] where, you know, we're going to build large language models or some other AI systems that  
[00:50:56] are like strictly smarter than all humans on the planet and more capable at all cognitive tasks.  
[00:51:02] Trading in particular feels to me as like kind of AGI complete, sort of like NP complete,  
[00:51:08] because at the end of the day trading involves figuring out what things are worth, which means  
[00:51:15] making predictions about the future. Jane Street isn't betting against AI.  
[00:51:18] They just signed a six billion dollar compute deal.  
[00:51:20] But Ron's view is that the edge keeps moving. I have never been more desperate to hire more  
[00:51:25] engineers and more traders than I am today. You know, you have the usual thing of like  
[00:51:29] the other hard parts that we don't yet know how to automate.  
[00:51:31] Well, that ends up being where the competitive edge lies.  
[00:51:34] You can find these open positions and watch the full interview at janestreet.com/dwarkesh.  
[00:51:41] I remember talking to an FPGA engineer at Jane Street, Clark, who helped me prep for  
[00:51:48] the previous interview we did together. He was explaining why they use FPGAs.  
[00:51:55] I imagine that for high-frequency trading, throughput is less important than latency,  
[00:52:01] so having very specific control over the clock  
[00:52:03] cycle in a deterministic way is the most important thing.  
[00:52:08] Maybe it'd be interesting to talk about why you can't just achieve that with an ASIC,  
[00:52:14] or why you might use an FPGA to have deterministic clock cycles for high-frequency trading.  
[00:52:25] Let's consider the business case for an FPGA versus an ASIC.  
[00:52:31] FPGAs and ASICs use largely the same conceptual model.  
[00:52:36] You have a series of gates built from small primitives—ANDs, ORs, XORs—connected together  
[00:52:48] with wires running in a fixed clock cycle. Anything you can express in an FPGA you  
[00:52:53] can express in an ASIC too. It will be about an order of  
[00:52:55] magnitude cheaper and have better energy efficiency on an ASIC than an FPGA.  
[00:53:01] The trade-off is that the first FPGA costs you $10,000, whereas the first ASIC you make costs $30  
[00:53:08] million because it requires an entire tape-out. The business use case for an FPGA is when you want  
[00:53:16] something that has very deterministic latency, fast runtime, and high parallelism,  
[00:53:25] but you are going to change the workload frequently, maybe every month.  
[00:53:29] You don't want to pay that tape-out cost every time.  
[00:53:34] How does an FPGA actually emulate the ASIC programming model in a fixed piece of hardware?  
[00:53:42] At its core, it has the two components we just talked about.  
[00:53:54] It has registers as storage devices, and it has lookup tables  
[00:54:03] (LUTs) which provide all of the gates. Then there's a third component.  
[00:54:11] We have a swarm of these registers and LUTs, and they are connected by a big set of muxes.  
[00:54:30] In front of every single one of these, we have a mux which selects an input from everywhere else.  
[00:54:44] We have a whole bunch of different options feeding into all of these things.  
[00:54:54] What this allows is essentially that when I program my FPGA, I can take all of these  
[00:55:01] components and superimpose a particular wiring which goes through this LUT, feed it into another  
[00:55:10] LUT, send it to this register, and then feed it into another LUT, or something like that.  
[00:55:16] What I've drawn in orange is how you… FPGA means Field-Programmable Gate Array.  
[00:55:22] The orange is what has been programmed in the field, whereas the white is all the  
[00:55:26] wires that must exist in the FPGA in order to actually make the device in the first place.  
[00:55:30] What does it mean to be programmed in the field? Programmed in the field means the device is  
[00:55:34] being deployed in a data center. It's sitting out in the world,  
[00:55:36] and then you can come and program it. Ah, not field as in like electric field.  
[00:55:39] Field as in like out there in the world, ok. If I look at how the field programming comes  
[00:55:48] out of the first lookup table and goes into a second one, how does that work?  
[00:55:57] Where are the wires that make that happen? I got a little bit lazy in drawing all of these.  
[00:56:03] Every single device here has a mux sitting in front of it, which can select from all of the  
[00:56:11] nearby circuits that are available. The actual configuration of the  
[00:56:19] FPGA amounts to the mux control. In this mux, we have the data inputs,  
[00:56:28] and we have the control that selects. There's a little storage device sitting next  
[00:56:34] to every single one of these muxes saying, "This is where you're going to source your input from."  
[00:56:43] Programming it consists of configuring every single one of these muxes.  
[00:56:47] That makes sense. What is happening inside of the lookup table?  
[00:56:51] The lookup table is also going to have a little bit of control telling it what to do.  
[00:56:56] Its purpose is to configurably take the role of an AND gate,  
[00:57:03] OR gate, XOR, or any of those different things. There are many ways you could consider doing that.  
[00:57:10] The way it's done in traditional FPGAs… A lookup table has four bits  
[00:57:25] of input and one bit of output. How many different functions are  
[00:57:31] there from four bits to one bit? There are 16 different functions.  
[00:57:37] You can tabulate this as 16 different numbers. You've got a table of 0111001, 16 entries.  
[00:57:52] This table is stored in this blue configuration bit.  
[00:58:00] It views these four bits as binary, looks up the relevant row of the table, and emits that bit.  
[00:58:08] This is essentially a truth-table view of lookup tables.  
[00:58:11] Okay, so if you think about an AND gate, OR gate, NOR gate, XOR gate, these all take as input…  
[00:58:18] Those are two-input functions. Sometimes we have a three-input function, like a three-way XOR,  
[00:58:25] or a four-way XOR. In this case,  
[00:58:27] does it just depend on how big it is? The typical size for LUTs is four inputs.  
[00:58:32] It's sort of just a sweet spot. There’s another compute vs. communication  
[00:58:37] trade-off here. If it has too  
[00:58:39] few inputs, you need to use more LUTs. Basically the lookup table is a truth table.  
[00:58:47] With a truth table, you can program in any gate you want.  
[00:58:50] So instead of a lookup table, you can just think of it as a programmable gate.  
[00:58:53] That's right. One of the things you can do here is you can see where the rule of thumb  
[00:58:59] that an FPGA is an order of magnitude more expensive than an ASIC comes from.  
[00:59:04] You count how many gates would be inside this lookup table.  
[00:59:10] We can view this lookup table essentially as one of these muxes.  
[00:59:14] It has to select between 16 different values,  
[00:59:19] so it's a mux with n=16 options and p=1 bits. As we saw earlier, this circuit  
[00:59:37] costs n times p many gates. So it costs np, which is 16,  
[00:59:45] AND gates, and also 16 ORs. This circuit being the mux?  
[00:59:52] Exactly, the mux. The mux that goes into the lookup table?  
[00:59:56] The lookup table itself you can think of as being a big mux that selects from all 16  
[01:00:02] rows down to one output. That's the lookup table.  
[01:00:05] But the way you've drawn it here, there's a mux and then a lookup table.  
[01:00:08] It's muxes all the way down. There is a second mux that is inside here.  
[01:00:12] This mux is this mux. And the other mux is just saying…  
[01:00:18] where it came from in this mess of gates. Right, and the second mux is, "Okay,  
[01:00:23] now you have one value, but that value is still a four-bit value."  
[01:00:29] Yeah, I've selected four bits from the soup. Then I use those four bits to select which  
[01:00:35] entry in the lookup table I'm going to use. Suppose in the first mux you're pulling  
[01:00:45] from eight nearby registers as input. That's a total of 32 bits going in.  
[01:00:53] Out of that, four bits come out. Those four bits go into the second mux,  
[01:00:58] which is inside the lookup table. In this case, these registers  
[01:01:02] are single-bit registers. If there are eight nearby  
[01:01:06] registers and lookup tables, then I have eight bits total coming in nearby.  
[01:01:11] I select from eight down to four different values. There are actually four different muxes, a little  
[01:01:21] mux associated with each of these input bits. Each of them is selecting one out of eight.  
[01:01:26] Where are those eight coming from? Nearby registers and other LUTs.  
[01:01:30] Each register is one bit. Yes.  
[01:01:33] I guess AMD or whoever makes these FPGAs still has to be opinionated about which  
[01:01:42] registers are connected to which registers. You can program in the actual gates,  
[01:01:47] but they add a wire in the connect… the communication topology, right?  
[01:01:53] You get flexibility at a local grain. There's a nearby neighborhood you can select from,  
[01:02:00] but for more coarse, long-distance connections, they form an opinion on that.  
[01:02:06] And the reason it's 10x slower is why? If you look at the cost of building this  
[01:02:11] lookup table, it's 32 gates. It can give me the equivalent  
[01:02:17] of—what’s an interesting thing I can do here—a four-way AND gate.  
[01:02:26] A four-way AND means AND, AND, and then an AND of an AND.  
[01:02:36] This is a circuit I could implement in an ASIC directly using three AND gates.  
[01:02:41] Using a LUT, I can also implement it, but it's going to take 32 gates instead of three.  
[01:02:47] So the overhead is really coming from the fact that there's a more concise  
[01:02:58] way to describe a truth table than listing out every single possible combination of inputs,  
[01:03:06] which is just to write out the gate. Yes, to place down the polysilicon  
[01:03:11] and the wires and so on. Interesting. One important point you  
[01:03:15] made to me is that the reason they prefer FPGAs to CPUs is that they get deterministic clock cycles.  
[01:03:21] They know when a packet will come in and go out. Why isn't that a guarantee in CPUs?  
[01:03:28] You can actually design a CPU that has deterministic latency as well.  
[01:03:34] In fact, the processors inside a lot of AI chips also have deterministic latency.  
[01:03:40] Groq has advertised this. TPUs have that in the core as well.  
[01:03:46] The challenge is getting deterministic latency and high speed at the same time.  
[01:03:53] Non-deterministic latency comes from specific design choices in a CPU.  
[01:04:03] It's actually possible to remove those design choices and make a CPU with deterministic latency,  
[01:04:08] but those are not very attractive in the market, so people don't make those CPUs anymore.  
[01:04:16] In some sense, deterministic latency is a simpler starting point, and some chip designers have  
[01:04:24] added things in to make it non-deterministic. To take a concrete example, probably the most  
[01:04:33] important source of non-determinism on a CPU is the CPU cache itself.  
[01:04:43] In a CPU, you have the CPU die itself, and then DDR memory off on the side.  
[01:04:54] You have a cache system inside that remembers recent accesses to DDR and stores them.  
[01:05:09] When I'm running through my CPU instructions, every time  
[01:05:12] I have an instruction that accesses memory, it first checks if the data was stored in the cache.  
[01:05:17] If not, it fetches it from DDR. This is a huge optimization.  
[01:05:23] The cache is two orders of magnitude faster than the DDR.  
[01:05:27] If you never used the cache, basically all programs would run a hundred times slower.  
[01:05:34] The presence of a cache is absolutely necessary for a CPU to run at a reasonable speed.  
[01:05:39] But whether or not you get a cache hit depends on the ambient environment of the CPU:  
[01:05:45] what other programs are running, what has run recently, and what the random number  
[01:05:48] generator inside the cache system is doing. That is a big source of non-determinism  
[01:05:53] in the runtime of a CPU. That is the memory system for a CPU.  
[01:06:01] The big thing you can do differently is, instead of having the hardware say,  
[01:06:06] "I’m going to read memory" and then the hardware decides whether or not it comes  
[01:06:11] from the cache, you can bake this decision into software, a different design philosophy.  
[01:06:22] You see this in TPUs, for example. I'll draw the same diagram,  
[01:06:28] but I'll call it a scratchpad. The main difference is… This would be a TPU,  
[01:06:36] and you have HBM in this case rather than DDR, but it's still an off-chip memory.  
[01:06:43] Instead of the software saying "first access memory" and letting the hardware decide,  
[01:06:48] you have one kind of instruction that goes to the scratchpad and a totally different kind  
[01:06:53] of instruction that goes to HBM. This style is generically known  
[01:06:58] as scratchpad instead of cache. The key distinction is that you have  
[01:07:04] one kind of instruction that says "read or write scratchpad," and a totally different instruction  
[01:07:08] that says "read or write HBM." So scratchpad being the cache.  
[01:07:12] Yeah, this thing here is the scratchpad. Stepping way back: people say computers have the  
[01:07:22] "von Neumann architecture", where there's this serial processing of information.  
[01:07:28] Maybe it's just because we've been talking about parallel  
[01:07:30] accelerators, but the FPGA is super parallel. The AI accelerators, the TPUs, are super parallel.  
[01:07:41] Even CPUs are super parallel if you think about all the cores they have.  
[01:07:46] In what sense is modern hardware actually the von Neumann architecture?  
[01:07:50] Is that actually a fair way to describe modern hardware?  
[01:07:52] I think it's a fair way to describe CPUs. The amount of parallelism you get on a CPU is  
[01:07:58] about 100 cores times maybe 16-way vector units, so about 1,000-way parallelism on a CPU.  
[01:08:06] One question: there is a die being used for the CPU, and if there are fewer threads,  
[01:08:15] just as a matter of transistor voltages switching on and off, is it that there's  
[01:08:22] literally one control flow—a small part of the die—where voltages are switching on and off?  
[01:08:28] How do you actually occupy the die area of a CPU… If there are so few cores, what are  
[01:08:35] you spending all of the die on? Yeah, what is happening there?  
[01:08:37] The cores are just much bigger and more complicated.  
[01:08:44] We should compare a CPU core, which takes up one one-hundredth of the die, to a LUT.  
[01:08:50] A LUT is only 16 gates. It's clear why there are so many  
[01:08:54] more LUTs in an FPGA than cores in a CPU. But why are there more CUDA cores,  
[01:09:04] for example, than CPU cores? What's the difference between a CPU and a GPU?  
[01:09:13] Inside the CPU, one big use of the area is the cache.  
[01:09:23] Very little is actually the ALUs. Mostly it's these register  
[01:09:28] files rather than the logic units. Both of those have equivalents in a GPU,  
[01:09:36] so that's not a big difference. But the thing that does not have  
[01:09:39] an equivalent in a GPU is the branch predictor. There is a whole big area in the CPU which is  
[01:09:49] just a bunch of predictors saying when the next branch will be and where the branch target is.  
[01:09:58] Stripping a lot of that out, as well as making these register files tighter,  
[01:10:06] drives a lot of the GPU gains over the CPU. What is the purpose of the branch predictor?  
[01:10:10] To execute both branches at once, or what does it do?  
[01:10:13] The issue is that when I've got a series of instructions, if I have a branch,  
[01:10:27] the actual step of processing an instruction takes a really long time.  
[01:10:32] It takes maybe five nanoseconds. The time to notice that I've got a branch,  
[01:10:43] evaluate whether the Boolean is true, update the program counter to the new target,  
[01:10:49] and then read from the instruction memory could take five nanoseconds to finish.  
[01:10:56] So in reality, this may finish somewhere down here.  
[01:11:03] I want to run a clock speed that is much faster than what five nanoseconds allows.  
[01:11:07] Five nanoseconds is a 200 MHz clock speed. I would like to run at one or two gigahertz.  
[01:11:13] So I need to run other instructions while the branch is being evaluated.  
[01:11:21] I just want to keep running the instructions that happen after me.  
[01:11:27] But that might have been wrong. If the branch ended up being taken, then  
[01:11:30] I need to know that instead of evaluating these instructions, I actually need to jump to wherever  
[01:11:34] the target is and run those instructions instead. The purpose of the branch predictor is to predict,  
[01:11:42] five cycles earlier, that a branch is going to happen, before you even get to that instruction.  
[01:11:49] If I think about how the brain works versus what you're describing here,  
[01:11:52] at a high level the differences might be that while you can do structured sparsity in these  
[01:11:59] accelerators and save yourself some area that you would have otherwise had to dedicate to gates,  
[01:12:07] in the brain there's unstructured sparsity. Any neuron can connect to any other neuron, and  
[01:12:12] not in ways where they have the column aligned. Then there's the fact that memory  
[01:12:18] and compute are co-located. Although I guess you could say in a way the memory  
[01:12:22] and compute are co-located on these dies too. This is exactly the co-location,  
[01:12:25] in some sense, of the memory and compute. So maybe that isn't a big difference.  
[01:12:30] Another big difference is that the clock cycle on the brain is much slower than on computers.  
[01:12:40] Partly that's to preserve energy, because the faster the clock cycle, the bigger the voltage  
[01:12:47] needs to be in order for the signal to settle and to identify what state a transistor is in.  
[01:12:54] That’s right. I don't know if  
[01:12:56] you have any commentary on what the brain might be doing versus how these chips work.  
[01:13:06] Let's take the clock speed one first. The clock speed is quite high on a  
[01:13:16] chip because that drives higher throughput. When we compare a GPU running some workload,  
[01:13:26] it's running batch size 1,000. Whereas the brain is not running  
[01:13:29] batch size 1,000, there's only one of me. You could imagine saying, "Take a GPU and  
[01:13:35] instead of running at a gigahertz, run it at a megahertz," and that would start  
[01:13:39] to look a little more like the equivalent things you're talking about in the brain.  
[01:13:45] But in the way silicon works, that does not give you a 1,000x advantage in energy efficiency.  
[01:13:58] What it ends up looking like is you just run this circuit once to stabilization,  
[01:14:07] and then it will sit idle for a long period of time.  
[01:14:10] It doesn't consume a lot of energy while it's sitting  
[01:14:12] idle because most of the energy is consumed in toggling bits from zero to one and back.  
[01:14:22] Let's talk about the energy consumption of a circuit like this.  
[01:14:26] The way to think of a bit being stored is that you've deposited some charge in a capacitor  
[01:14:32] sitting somewhere in the chip implicitly. It becomes charged when the bit becomes a one,  
[01:14:38] and then it becomes discharged when it next goes to a zero.  
[01:14:41] That cycle of charging the capacitor and then dumping that charge out  
[01:14:45] to ground is where the energy is consumed. This is called the dynamic or switching power,  
[01:14:49] and it's most of the energy consumption of a chip. There is some other energy consumption just  
[01:14:54] coming from the fact that insulators aren't perfect, but we'll discard that.  
[01:15:00] Most of the energy consumption comes from toggling from zero to one and back to zero.  
[01:15:08] If you run a chip much slower and you only clock it once every thousand clock cycles,  
[01:15:12] you will have 1,000 times fewer transitions. It will be about 1,000 times  
[01:15:16] less energy consumption. But it's not a substantial  
[01:15:20] advantage in energy efficiency. Okay, so you described how a TPU  
[01:15:25] works at a high level. What is the difference  
[01:15:29] at a high level between how a GPU and a TPU work? There is a high-level organization principle that  
[01:15:37] is different, and then inside the cores things are different.  
[01:15:41] Looking at the high level, we'll take a GPU and a TPU and see what  
[01:15:50] the top-level block structure looks like. If you think of this as the whole chip  
[01:15:55] in each case, the organization of the GPU is mostly a bunch of  
[01:16:03] almost-identical units, which are the SMs. They've got an L2 memory in the middle,  
[01:16:12] and then a bunch more of these SMs on the bottom. So there is a fairly regular grid of cores.  
[01:16:24] If we look at a TPU in comparison, you end up with much coarser-grained units of logic.  
[01:16:34] You end up with just a few matrix units, which are the big systolic arrays.  
[01:16:48] In the middle you've got some vector unit, and then you've got your matrix units at the bottom.  
[01:17:00] These matrix units with a vector unit in the middle make up the whole TPU chip.  
[01:17:06] You can think of scaling this thing down into a really tiny unit with a  
[01:17:10] smaller matrix unit and a smaller vector unit, and that is sort of what an SM is.  
[01:17:16] From a very high-level point of view, the GPU has a lot of tiny TPUs tiled across the whole chip.  
[01:17:24] Oh, interesting. You're suggesting the tensor core within a streaming SM is analogous to an MXU?  
[01:17:31] Yeah, it's all very similar. I see. If you had more lack of structure,  
[01:17:38] having a bunch of tiny TPUs makes a lot of sense. Whereas if you just have huge matrix  
[01:17:44] multiplications, you might want to avoid the cost of having individual SMs with their own  
[01:17:54] registers and warp schedulers. Why not just make a huge thing  
[01:17:58] and amortize those costs across the whole thing? This shows up in how large you can grow things.  
[01:18:04] We've seen this theme, especially with the systolic array, where a larger systolic  
[01:18:08] array amortizes the register file costs better. This design allows you to have larger systolic  
[01:18:14] arrays, whereas the GPU design constrains you to having small units of everything.  
[01:18:21] There is a trade-off, however. Because of this coarse-grained  
[01:18:29] separation of things, you need to move a lot of data from the vector unit to the matrix units,  
[01:18:37] through just two lines of perimeter here. If you look at the equivalent thing  
[01:18:46] in a GPU, you've got vector units everywhere, and you can move data through many different lines.  
[01:18:55] The amount of data you can move between a vector unit and a matrix unit is actually  
[01:19:00] much higher in a GPU than in a TPU. Instead of having to move all the data  
[01:19:08] through just two lines, you're moving it through 16 lines of wiring in a GPU.  
[01:19:16] Right. But also you might have to move across less area.  
[01:19:21] Which is an energy saving as well. So if you can operate entirely within  
[01:19:27] an SM, the data movement is much smaller. But the moment you want to operate across SMs,  
[01:19:33] it becomes more complicated and expensive. So you don’t have to comment, but one might  
[01:19:37] expect that a thing MatX might try to do is get the GPU-like smaller structure of  
[01:19:45] systolic arrays surrounded by SRAM, but at the same time make it so that the things you need in  
[01:19:55] an SM to support the CUDA architecture—which take a bunch of space—you might discard.  
[01:20:05] We've talked publicly about something we call a splittable systolic array, which  
[01:20:09] in some sense you can think of as big systolic arrays that can be small systolic arrays too.  
[01:20:13] Cool. Okay, I think that's a good note to close on.  
[01:20:16] Reiner, thank you so much. Thanks, Dwarkesh.  
