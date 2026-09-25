# Dylan Patel — The single biggest bottleneck to scaling AI compute

[00:00:00] All right, this is the episode where my roommate teaches me semiconductors.  
[00:00:04] It's also the send off for this current set. It is. After you use it, I'm like,  
[00:00:09] "I can't use this again. I gotta get out of here."  
[00:00:11] No sloppy seconds for Dwarkesh. Dylan is the CEO of SemiAnalysis.  
[00:00:18] Dylan, here’s the burning question I have for you. If you add up the big four—Amazon, Meta, Google,  
[00:00:23] Microsoft—their combined forecasted CapEx this year that you published recently is $600 billion.  
[00:00:31] Given yearly prices of renting that compute, that would be close to 50 gigawatts.  
[00:00:38] Obviously, we're not putting on 50 gigawatts this year,  
[00:00:40] so presumably that's paying for compute that is going to be coming online over the coming years.  
[00:00:46] How should we think about the timeline around when that CapEx comes online? Similar question  
[00:00:51] for the labs. OpenAI just announced they raised $110 billion, and Anthropic just  
[00:00:57] announced they raised $30 billion. If you look at the compute they  
[00:01:01] have coming online this year—you should tell me how much it is, but is it on the  
[00:01:08] order of another four gigawatts total? The cost to rent the compute that OpenAI  
[00:01:10] and Anthropic will have this year to sustain their compute spend is $10 to $13 billion a gigawatt.  
[00:01:18] Those individual raises alone are enough to cover their compute spend for the year.  
[00:01:23] And this is not even including the revenue that they're going to earn this year.  
[00:01:26] So help me understand: first, what is the timescale at which  
[00:01:30] the Big Tech CapEx actually comes online? And second, what are the labs raising all  
[00:01:34] this money for if the yearly price of a one-gigawatt data center is $13 billion?  
[00:01:41] So when you talk about the CapEx of these hyperscalers being on the order of $600 billion,  
[00:01:46] and you look across the rest of the supply chain, it gets you to the order of a trillion dollars.  
[00:01:51] A portion of this is immediately for compute going online this year: the chips and the  
[00:02:00] other parts of CapEx that get paid this year. But there's a lot of setup CapEx as well.  
[00:02:05] When we're talking about 20 gigawatts of incremental added capacity this year in America,  
[00:02:11] a portion of this is not spent this year. A portion of that CapEx was actually  
[00:02:16] spent the prior year. When you look at Google  
[00:02:19] having $180 billion, a big chunk of that is spent on turbine deposits for '28 and '29.  
[00:02:25] A chunk of that is spent on data center construction for '27.  
[00:02:28] A chunk of that is spent on power purchasing agreements, down payments, and all these other  
[00:02:33] things they're doing further out into the future so they can set up this super fast scaling.  
[00:02:40] This applies to all the hyperscalers and other people in the supply chain.  
[00:02:45] So with roughly 20 gigawatts deployed this year, a big chunk is hyperscalers, and a chunk is not.  
[00:02:51] For all of these companies, their biggest customers are Anthropic and OpenAI.  
[00:02:55] Anthropic and OpenAI are at roughly two to two-and-a-half gigawatts right  
[00:03:02] now, and they're trying to scale much larger. If you look at what Anthropic has done over the  
[00:03:08] last few months, with $4 billion or $6 billion in revenue added,  
[00:03:11] we can just draw a straight line and say they'll add another $6 billion of revenue a month.  
[00:03:16] People would argue that’s bearish, and that they should go faster.  
[00:03:18] What that implies is they're going to add $60 billion of revenue across the next ten months.  
[00:03:26] At the current gross margins Anthropic had, as last reported by media, that would imply  
[00:03:33] they have roughly $40 billion of compute spend for that inference, for that $60 billion of revenue.  
[00:03:39] That $40 billion of compute, at roughly $10 billion a gigawatt in rental costs,  
[00:03:44] means they need to add four gigawatts of inference capacity just to grow revenue.  
[00:03:49] That’s assuming their research and development training fleet stays flat.  
[00:03:55] In a sense, Anthropic needs to get to well above five gigawatts by the end of this year.  
[00:03:59] It's going to be really tough for them to get there, but it's possible.  
[00:04:01] Can I ask a question about that? If Anthropic was not on track to have  
[00:04:06] five gigawatts by the end of this year, but it needs that to serve both the revenue that's gone  
[00:04:12] crazier than expected—and maybe it's going to be even more than that—plus the research and training  
[00:04:16] to make sure its models are good enough for next year: Where is that capacity going to come from?  
[00:04:21] Dario, when he was on your podcast, was very conservative.  
[00:04:24] He said, "I'm not going to go crazy on compute because if my revenue inflects  
[00:04:28] at a different rate, at a different point… I don't want to go bankrupt.  
[00:04:31] I want to make sure that we're being responsible with this scaling."  
[00:04:35] But in reality, he's screwed the pooch compared to OpenAI, whose approach was,  
[00:04:40] "Let's just sign these crazy fucking deals." OpenAI has got way more access to compute  
[00:04:46] than Anthropic by the end of the year. What does Anthropic have to do to get the compute?  
[00:04:50] They have to go to lower-quality providers that they would not have gone to before.  
[00:04:56] Anthropic historically had the best quality providers, like Google and  
[00:05:00] Amazon, the biggest companies in the world. Now Microsoft is expanding across the supply  
[00:05:07] chain, and they're going to other newer players. OpenAI has been a bit more  
[00:05:12] aggressive on going to many players. Yes, they have tons of capacity from Microsoft,  
[00:05:16] Google, and Amazon, but they also have tons with CoreWeave and Oracle.  
[00:05:20] They've gone to random companies, or companies one would think are random, like SoftBank Energy,  
[00:05:25] who has never built a data center in their life but is building data centers now for OpenAI.  
[00:05:29] They've gone to many others, like NScale, to get capacity.  
[00:05:35] There's this conundrum for Anthropic because they were so conservative on compute,  
[00:05:42] because they didn't want to go crazy. In some sense, a lot of the financial  
[00:05:46] freakouts in the second half of last year were because, "OpenAI signed all these  
[00:05:50] deals but they didn't have the money to pay for them…" Okay, Oracle's stock is going to  
[00:05:55] tank, CoreWeave's stock is going to tank. All these companies' stocks tanked,  
[00:05:58] and credit markets went crazy because people thought the end buyer couldn't pay for this.  
[00:06:02] Now it's like, "Oh wait, they raised a ton of money.  
[00:06:04] Okay, fine, they can pay for it." Anthropic was a lot more conservative.  
[00:06:07] They were like, "We'll sign contracts, but we'll be principled.  
[00:06:11] We'll purposely undershoot what we think we can possibly do and be conservative because  
[00:06:16] we don't want to potentially go bankrupt." The thing I want to understand is, what does  
[00:06:20] it mean to have to acquire compute in a pinch? Is it that you have to go with neoclouds? Do they  
[00:06:26] have worse compute? In what way is it worse? Did you have to pay gross margins to a cloud  
[00:06:31] provider that you wouldn't have otherwise had to pay because they're coming in at the last minute?  
[00:06:35] Who built the spare capacity such that it's available for Anthropic  
[00:06:39] and OpenAI to get last minute? What is the concrete advantage  
[00:06:42] that OpenAI has gotten if they end up at similar compute numbers by 2027?  
[00:06:48] Are they just going to end this year with different gigawatts?  
[00:06:50] If so, how many gigawatts are Anthropic and OpenAI going to have by the end of this year?  
[00:06:56] To acquire excess compute, yes, there is capacity at hyperscalers.  
[00:07:01] Not all contracts for compute are long-term, five-year deals.  
[00:07:04] There's compute from 2023 or 2024, or H100s from 2025, that were signed at shorter terms.  
[00:07:11] The vast majority of OpenAI's compute is signed on five-year deals, but there were many other  
[00:07:16] customers that had one-year, two-year, three-year, or six-month deals, on demand.  
[00:07:20] As these contracts roll off, who is the participant in the  
[00:07:24] market most willing to pay price? In this sense, we've seen H100 prices  
[00:07:30] inflect a lot and go up. People are willing to  
[00:07:34] sign long-term deals for above $2 even. I've seen deals where certain AI labs—I'm being a  
[00:07:42] little bit vague here for a reason—have signed at as high as $2.40 for two to three years for H100s.  
[00:07:49] If you think about the margin, it costs $1.40 to build Hopper, across five years.  
[00:07:57] Now, two years in, you're signing deals for two to three years at $2.40? Those margins are way  
[00:08:03] higher. Now you can crowd out all of these other suppliers, whether Amazon had these, or CoreWeave,  
[00:08:09] or Together AI, or Nebius, or whoever it is. These neoclouds are the firms that had a  
[00:08:19] higher percentage of Hopper in general because they were more aggressive on it.  
[00:08:23] They also tended to sign shorter-term deals, not CoreWeave but the others.  
[00:08:30] So if I want Hopper, there is some capacity out there.  
[00:08:33] Also, while most of the capacity at an Oracle or a CoreWeave is signed for a long-term deal  
[00:08:39] in terms of Blackwell, anything that's going online this quarter is already sold.  
[00:08:44] In some cases, they're not even hitting all the numbers they promised they would sell because  
[00:08:48] there are some data center delays, not just those two, but Nebius, Microsoft, Amazon, and Google.  
[00:08:53] But there are a lot of neoclouds, as well as some of the hyperscalers, who have capacity they're  
[00:08:57] building that they haven't sold yet, or capacity they were going to allocate to some internal use  
[00:09:02] that is not necessarily super AGI-focused, that they may now turn around and sell.  
[00:09:06] Or in the case of Anthropic, they don't have to have all the compute directly.  
[00:09:10] Amazon can have the compute and serve Bedrock, or Google can have the compute and serve Vertex,  
[00:09:15] or Microsoft can have the compute and serve Foundry, and then do a  
[00:09:18] revenue share with Anthropic, or vice versa. Basically, you're saying Anthropic is having to  
[00:09:22] pay either this 50% markup in the sense of the revenue share, or in the sense of last-minute  
[00:09:28] spot compute that they wouldn't have otherwise had to pay had they bought the compute early.  
[00:09:32] Right, there's a trade-off there. But at the same time,  
[00:09:38] for a solid four months, everyone was saying to OpenAI, "We're not going to sign deals with you."  
[00:09:43] That sounds crazy, but it was because, "you don’t have the money."  
[00:09:45] Now everyone's saying, "OpenAI, we believed you the whole time.  
[00:09:48] We can sign any deal because you've raised all this money."  
[00:09:51] Anthropic is constrained in that sense. There are not that many incremental buyers of  
[00:09:58] compute yet, because Anthropic hit the capability tier first where their revenue is mooning.  
[00:10:03] That's interesting. Otherwise you might think having the best model is an  
[00:10:08] extremely depreciating asset, because three months later you don't have the best model.  
[00:10:12] But the reason it's important is that you can sign these deals, lock in the compute  
[00:10:16] in advance, and get better prices. Maybe this is an obvious point.  
[00:10:22] But at least until recently, people had made this huge point about the depreciation cycle of a GPU.  
[00:10:30] The bears, the Michael Burrys or whoever, have said, "Look, people  
[00:10:33] are saying four or five years for these GPUs. Maybe it's because the technology is improving  
[00:10:41] so fast, but it in fact makes sense to have two-year depreciation cycles for these GPUs,"  
[00:10:46] which increases the reported amortized CapEx in a given year and makes it financially  
[00:10:53] less lucrative to build all these clouds. But in fact you’re pointing out that maybe the  
[00:10:58] depreciation cycle is even longer than five years. If we're using Hoppers—especially if AI really  
[00:11:03] takes off and in 2030 we’re saying, "We have to get the seven-nanometer fabs up, we have  
[00:11:08] to go back and turn on the A100s again"—then the depreciation cycle is actually incredibly long.  
[00:11:18] I feel like that's an interesting financial implication of what you're saying.  
[00:11:21] There's a few strings to pull on there. One is, what happens to depreciation of GPUs?  
[00:11:30] I guess I didn't answer your prior question, which is that I think Anthropic will be able to  
[00:11:34] get to five gigawatts-ish, maybe a little bit more by the end of the year through  
[00:11:38] themselves as well as their product being served through Bedrock, Vertex, or Foundry.  
[00:11:45] I think they'll be able to get to five or six gigawatts, which is way above their initial plans.  
[00:11:53] OpenAI will be roughly the same, actually a little bit higher based on our numbers.  
[00:11:59] But anyway, the depreciation cycle of a GPU. Michael Burry was saying it's three years  
[00:12:04] or less. That’s sort of his argument. There are two lenses to look at this.  
[00:12:09] Mechanically, there's a TCO model, total cost of ownership of a GPU, where we project pricing out  
[00:12:17] for GPUs and build up the total cost of a cluster. There are a number of costs: your data center  
[00:12:23] cost, your networking cost, your smart hands and people in the data center swapping stuff out.  
[00:12:29] There's your spare parts, your actual chip cost, your server cost.  
[00:12:32] All these various costs get lumped together. There's some depreciation cycles on it,  
[00:12:37] certain credit costs on it. You build up to, "Hey, an H100 costs  
[00:12:42] $1.40/hour to deploy at volume across five years if your depreciation is five years."  
[00:12:48] If you sign a deal at $2/hour for those five years, your gross margin is roughly 35%.  
[00:12:53] It's a little bit above that. If you sign it for $1.90, it's 35% roughly.  
[00:12:58] Then you assume at that fifth year, the GPU falls off a bus and is dead.  
[00:13:03] In some cases, the argument people are making is if you didn't sign a long-term deal, because every  
[00:13:09] two years NVIDIA is tripling or quadrupling the performance while only 2X-ing or 50% increasing  
[00:13:15] the price… Then the price of an H100… Sure maybe the value in the market was $2 at 35%  
[00:13:20] gross margins in 2024, but in 2026, when Blackwell is in super high volume and deploying millions  
[00:13:28] a year, you’re actually now worth $1/hour. And when Rubin in '27 is in super high volume—even  
[00:13:33] though it starts shipping this year, it’s super high volume next year—doing millions of chips a  
[00:13:38] year deployed into clouds, you've got another 3X in performance, another 50% or 2X in price,  
[00:13:44] then the Hopper is only worth $0.70/hour. So the price of a GPU would continue to  
[00:13:49] fall. That's one lens. The other lens is, what is the utility you get out of the chip?  
[00:13:54] If you could build infinite Rubin or infinite of the newest chip,  
[00:13:59] then yes, that's exactly what would happen. The price of a Hopper would fall at a spot  
[00:14:04] or short-term contract rate as the new chips come out and the price per performance goes up.  
[00:14:10] But because you are so limited on semiconductors and deployment timelines, what actually prices  
[00:14:18] these chips is not the comparative thing I can buy today, but rather what is the value  
[00:14:24] I can derive out of this chip today. In that sense, let's take GPT-5.4.  
[00:14:31] GPT-5.4 is both way cheaper to run than GPT-4 and has fewer active parameters.  
[00:14:38] It's much smaller, in that sense of active parameter, because it's a  
[00:14:42] sparser MoE versus GPT-4 being a coarser MoE. There's also been so many other advancements  
[00:14:47] in training, RL, model architecture, and data qualities that have made GPT-5.4 way better than  
[00:14:54] GPT-4. And it's cheaper to serve. When you look at an H100, it can serve more tokens per GPU of  
[00:15:02] 5.4 than if you had ran GPT-4 on it. So it's producing more tokens of a  
[00:15:07] model that is of higher quality. What is the maximum TAM for GPT-4 tokens?  
[00:15:16] Maybe it was a few billion dollars, maybe it was tens of billions of dollars. Adoption  
[00:15:19] takes time. For GPT-5.4, that number is probably north of a hundred billion.  
[00:15:23] But there's an adoption lag, there's competition, and there's the constant  
[00:15:27] improvements that everyone else is having. If improvements stopped here, the value of  
[00:15:32] an H100 is now predicated on the value that GPT-5.4 can get out of it instead  
[00:15:36] of the value that GPT-4 can get out of it. These labs are in a competitive environment,  
[00:15:42] so their margins can't go to infinity. You sort of have this dynamic that is  
[00:15:47] quite interesting in that an H100 is worth more today than it was three years ago.  
[00:15:51] That's crazy. It's also interesting from the perspective of just taking that forward.  
[00:15:56] If we had actual AGI models developed, if we had a genuine human on a server… These  
[00:16:06] are such hand wave-y numbers about how many flops the brain can do.  
[00:16:08] But on a flop basis, an H100 is estimated to do 1e15, which is how much some people estimate  
[00:16:15] the human brain does in flops. Obviously, in terms of memory,  
[00:16:19] the human brain has way more. An H100 is 80 gigabytes,  
[00:16:22] and the brain might have petabytes. Oh, yeah, you've got petabytes? Name a petabyte  
[00:16:28] of ones and zeros, bro. Name me a string. Well, this is actually the point.  
[00:16:33] No, we’ve just got the best sparse attention techniques ever.  
[00:16:36] Genuinely though. In the amount of information that is compressed, it might be petabytes.  
[00:16:42] The brain is an extremely sparse MoE. But anyways, imagine a human knowledge  
[00:16:48] worker can produce six figures a year of value. If an H100 can produce something close to that,  
[00:16:54] if we had actual humans on a server, the value of an H100 is such that it can repay  
[00:16:58] itself in the course of a couple of months. So when I interviewed Dario, the point I was  
[00:18:02] trying to make is not that I think the singularity is two years away and therefore Dario desperately  
[00:18:08] needs to buy more compute, although the revenue is certainly there that he needs to buy more compute.  
[00:18:12] The point I was trying to make is that given what Dario seems to be saying—given his statements that  
[00:18:17] we're two years away from a data center of geniuses, and certainly not more than five  
[00:18:21] years away, and a data center of geniuses should be earning trillions upon trillions of dollars  
[00:18:25] of revenue—it just does not make sense why he keeps making these statements about being  
[00:18:30] more conservative on compute or, to your point, being less aggressive than OpenAI on compute.  
[00:18:35] I guess that point got lost because then people were roasting me, saying, "Oh, this podcaster  
[00:18:39] is trying to convince this multi-hundred billion dollar company CEO to YOLO it, bro."  
[00:18:44] I was just trying to say that internally, his statements are inconsistent.  
[00:18:50] Anyway, it's good to iron it out. I think going back to the earlier  
[00:18:55] view that if the models are so powerful, the value of a GPU goes up over time, right now  
[00:19:06] only OpenAI and Anthropic have that viewpoint. But as we approach further out, everyone is going  
[00:19:11] to be able to see that value skyrocket per GPU. So in that sense,  
[00:19:19] you should commit now to compute. Interestingly, in Anthropic fashion,  
[00:19:28] there's a bit of a meme that they have commitment issues and are sort of polyamorous.  
[00:19:35] Not Dario, but this is a bit of a meme. Explains everything. By the way, there's  
[00:19:42] this interesting economic effect called Alchian-Allen, which is the idea that if  
[00:19:48] you increase the fixed cost of different goods, one of which is higher quality and one which is  
[00:19:54] lower quality, that will make people choose the higher quality good, on the margin.  
[00:19:59] To give a specific example, suppose the better-tasting apple costs two dollars and  
[00:20:04] the shittier apple costs one dollar. Now suppose you put an import tariff on them.  
[00:20:10] Now it's $3 versus $2 for a great apple versus a medium apple.  
[00:20:15] Is that because they both increased by a dollar, or should it be a 50% increase?  
[00:20:18] No, because they both increased by $1. The whole effect is that if there's  
[00:20:22] a fixed cost that is applied to both. Then the price difference between them,  
[00:20:28] the ratio, changes. Previously, the more  
[00:20:31] expensive one was 2X more expensive. Now it's just 1.5X more expensive.  
[00:20:34] So I wonder if applied to AI that would mean that, if GPUs are going to get more expensive,  
[00:20:39] there will be a fixed cost increase in the price of compute.  
[00:20:43] As a result, that will push people to be willing to pay higher margins for slightly better models.  
[00:20:51] Because the calculus is, I'm going to be paying all this money for the compute anyway.  
[00:20:55] I might as well just pay slightly more to make sure it's the very best model rather  
[00:21:00] than a model that's slightly worse. So the Hopper went from $2 to $3.  
[00:21:03] If a Hopper can make a million tokens of Opus and it can make two million tokens of Sonnet,  
[00:21:11] the price differential between Opus and Sonnet has decreased because the price of  
[00:21:15] the GPU has increased by a dollar from $2 to $3. Interesting. I think that makes a ton of sense.  
[00:21:22] We just see all of the volumes are on the best models today,  
[00:21:25] all the revenue is on the best models today. In a compute-limited world, two things happen.  
[00:21:34] One, companies that don't have commitment issues and have these five-year contracts for compute  
[00:21:41] have locked in a humongous margin advantage. They've locked in compute for five years  
[00:21:47] at the price it transacted at two, three, or five years ago.  
[00:21:51] Whereas if you're three years into that five-year contract and someone else's  
[00:21:55] two-year or three-year contract rolled off, and now they're trying to buy that at modern pricing,  
[00:22:00] when it's priced to the value of models, the price is going to be up a lot more.  
[00:22:05] So the person who committed early has better margins in general.  
[00:22:11] The percentage of the market that is in long-term contracts is much larger than the percentage of  
[00:22:15] the market in short-term contracts that can be this flex capacity you add at the last second.  
[00:22:21] At the same time, where does the margin go? Because models get more valuable,  
[00:22:28] how much can the cloud players flex their pricing?  
[00:22:33] If you look at CoreWeave, their average term duration is over three years right now.  
[00:22:39] For ninety-eight percent plus of their compute, it's over three years.  
[00:22:43] They end up with this conundrum where they can't actually flex price.  
[00:22:46] But every year they're adding incrementally way more capacity than they had previously.  
[00:22:52] This year alone, Meta's adding as much capacity as they had in their entire fleet of compute and data  
[00:22:58] centers for all purposes for serving WhatsApp, Instagram, and Facebook in 2022, and doing AI.  
[00:23:03] They're adding that alone this year. In the same sense, you talk about Meta doing that,  
[00:23:07] CoreWeave, Google, and Amazon, all these companies are adding insane amounts of compute year on year.  
[00:23:13] That new compute gets transacted at the new price. In a sense, yes, you've locked in, as long as  
[00:23:19] we're in a takeoff. "Oh, OpenAI went from six hundred megawatts to two gigawatts last year,  
[00:23:24] and from two gigawatts to six plus this year, and six to twelve next year."  
[00:23:29] The incremental added compute is where all the cost is, not the prior long-term contracts.  
[00:23:34] Then who holds the cards is the infra providers for charging margin.  
[00:23:38] Now the cloud players, the neoclouds, or the hyperscalers can charge the margin.  
[00:23:43] They can to some extent, but then as you go upstream to who has access to all the memory and  
[00:23:48] logic capacity, it's Nvidia for the most part. They've signed a lot of long-term contracts.  
[00:23:53] They've got ninety billion dollars of long-term contracts today, and they're negotiating  
[00:23:56] three-year deals today with the memory vendors. You've got Amazon and Google through Broadcom,  
[00:24:04] Amazon directly, and AMD. These companies hold all the  
[00:24:07] cards because they've secured the capacity. TSMC is not raising prices, but memory vendors  
[00:24:13] are, to some extent, raising a lot of price. They're going to double or triple price again, but  
[00:24:18] then they're also signing these long-term deals. Who is able to accrue all the margin dollars is  
[00:24:23] potentially the cloud, potentially the chip vendors, and the memory vendors,  
[00:24:28] until TSMC or ASML break out and say, "No, we're going to charge a lot more."  
[00:24:33] But at the same time, do the model vendors get to charge crazy margins?  
[00:24:38] At least this year, we're going to see margins for the model vendors go up a lot.  
[00:24:41] Because they're so capacity constrained, they have to destroy demand.  
[00:24:46] There's no way Anthropic can continue at the current pace without destroying demand.  
[00:24:52] Let's get into logic and memory. How specifically has Nvidia been  
[00:24:58] able to lock up so much of both? I think according to your numbers,  
[00:25:02] by '27, Nvidia is going to have +70% of N3 wafer capacity, or around that area.  
[00:25:12] I forget what the numbers were for memory at SK Hynix and Samsung and so forth.  
[00:25:19] Think about how the neocloud business works and how Nvidia works with that,  
[00:25:22] or how the RL environment business works and how Anthropic works with that.  
[00:25:26] In both those cases, Nvidia is purposely trying to fracture the complementary industry to make sure  
[00:25:33] that they have as much leverage as possible. They're giving allocation to random neoclouds  
[00:25:37] to make sure that there's not one person that has all the compute.  
[00:25:39] Similarly, Anthropic or OpenAI, when they're working with the data providers, they say, "No,  
[00:25:44] we're going to just seed a huge industry of these things so that we're not locked  
[00:25:48] into any one supplier for data environments." And I wonder why on the 3 nm process—that's  
[00:25:56] going to be Trainium 3, that's going to be TPU v7, other accelerators potentially—why  
[00:26:03] is TSMC just giving it all up to Nvidia rather than trying to fracture the market?  
[00:26:09] There are a couple points here. On 3 nm, if we go back to last year,  
[00:26:15] the vast majority of 3 nm was Apple. Apple is being moved to 2 nm.  
[00:26:20] Memory prices are going up, so Apple's volumes may go down.  
[00:26:24] As memory prices go up, either they cut margin or they move on.  
[00:26:29] There's some time lag because they have long-term contracts, but Apple likely  
[00:26:33] reduces demand or moves to 2 nm faster, where 2 nm is only capable of mobile chips today.  
[00:26:39] In the future, AI chips will move there. So Apple has that. Apple is also talking to  
[00:26:44] third-party vendors because they're getting squeezed out of TSMC a little bit.  
[00:26:48] TSMC's margins on high-performance computing—HPC, AI chips, et cetera—are higher than they are  
[00:26:54] for mobile, because they have a bigger advantage in HPC than they do in mobile.  
[00:27:00] When you look at TSMC’s running calculus here, they're actually providing really good  
[00:27:06] allocations to companies that are doing CPUs. When you think about Amazon having Trainium and  
[00:27:14] Graviton, both of those are on 3 nm, Graviton being their CPU, Trainium being their AI chip.  
[00:27:20] TSMC is much more excited to give allocation to Graviton than they  
[00:27:23] are to Trainium because they view the CPU business as more stable, long-term growth.  
[00:27:30] As a company that is conservative and doesn't want to ride cycles of growth too hard,  
[00:27:35] you actually want to allocate to the market that is more stable with a lower growth rate first  
[00:27:42] before you allocate all the incremental capacity to the fast growth rate market. That is the case  
[00:27:48] generally. Same for AMD. The allocations they get on their CPUs, TSMC is much more excited  
[00:27:57] about those than they are for GPUs. Likewise for Amazon. Nvidia is a bit unique because yes,  
[00:28:03] they have CPUs, they make switches, they make networking, NVLink, InfiniBand, Ethernet, NICs.  
[00:28:11] By and large, most of these things will be on 3 nm by the end of this year with  
[00:28:14] the Rubin launch and all the chips in that family, the GPU being the most important one.  
[00:28:20] Yet Nvidia is getting the majority of supply. Part of this is because you look at the market  
[00:28:27] and TSMC and others forecast market demand in many ways, but it's also the market signal.  
[00:28:36] The market signaled, "Hey, we need this much capacity next year. We need this much. We'll  
[00:28:42] sign non-cancelable, non-returnable. We may even pay deposits." Nvidia just did  
[00:28:46] it way earlier than Google or Amazon. In some cases, Google and Amazon had  
[00:28:53] stumbling blocks. One of the chips  
[00:28:56] got delayed slightly by a couple quarters. Trainium and all these sorts of things happened.  
[00:29:01] In that case, there was a huge sort of, "Well, these guys are delaying,  
[00:29:05] but Nvidia is wanting more, more, more, more. And we are checking with the rest of the supply  
[00:29:10] chain, is there enough capacity?" They're going to all the PCB  
[00:29:13] vendors and saying, "Is there enough PCB?" Victory Giant is one of the largest suppliers  
[00:29:18] of PCBs to Nvidia, and they're a Chinese company. All the PCBs come from China, or many of them.  
[00:29:25] They're like, "Do you have enough PCB capacity? Great. Hey memory vendors, who has all the memory  
[00:29:28] capacity? Okay, Nvidia does. Great." When you look at who is AGI-pilled enough to buy compute  
[00:29:36] on long timelines at levels that seem ridiculous to people who aren't AGI-pilled—but nonetheless,  
[00:29:42] they're willing to pay a pretty good margin and sign it now because they view in the future that  
[00:29:49] ratio is screwed up—the same thing happens with the supply chain for semiconductors.  
[00:29:54] I don't think Nvidia is quite AGI-pilled. Jensen doesn't believe software is going  
[00:29:58] to be fully automated and all these things. Accelerated computing, not AI chips, right?  
[00:30:03] It's AI chips. But that's what he calls it, right?  
[00:30:05] Yeah. I think it's a broader term, AI is within that, but also physics modeling and simulations.  
[00:30:11] But it's like he's not embracing the main use case.  
[00:30:14] I think he's embracing it, but I just don't think he's AGI-pilled like Dario or Sam.  
[00:30:19] But he's still way, way more AGI-pilled than Google was in Q3 of last year, or Amazon was  
[00:30:30] in Q3 of last year, and he saw way more demand. The reason is pretty simple. You can see all the  
[00:30:33] data center construction. He's like, "Okay,  
[00:30:34] I want to have this market share." We have all the data centers tracked,  
[00:30:38] and there's a lot of data centers that could be one or the other.  
[00:30:44] To some extent, Google and Amazon, Google especially, even though their TPU is just  
[00:30:49] better for them to deploy, they have to deploy a crap load of GPUs because they  
[00:30:52] don't have enough TPUs to fill up their data centers. They can't get them fabbed.  
[00:30:56] I have a question about that. Google sold a million, was it  
[00:31:00] the v7s? Yes.  
[00:31:01] —the Ironwoods to Anthropic, and you're saying the big bottleneck right now, this year or next year,  
[00:31:07] I guess going forward forever now, is going to be the logic and memory,  
[00:31:13] the stuff it takes to build these chips. Google has DeepMind, the third prominent AI lab.  
[00:31:19] If this is the big bottleneck, why would they sell it rather than just giving it to DeepMind?  
[00:31:24] This is again a problem of… DeepMind people were like, "This is insane. Why did we do  
[00:31:29] this?" But Google Cloud people and Google executives saw a different thought process.  
[00:31:37] You and I know the compute team at Anthropic. Both of the main people came from Google.  
[00:31:45] They saw this dislocation, they negotiated a deal, and they were able to get access  
[00:31:49] to this compute before Google realized. The chain of events, at least from our  
[00:31:54] data that we found, was in early Q3, over the course of six weeks, we saw capacity  
[00:32:06] on TPUs go up by a significant amount. It went up multiple times in those six  
[00:32:12] weeks. There were multiple requests. Google even had to go to TSMC and explain to them  
[00:32:18] why they needed this increase in capacity because it was so sudden.  
[00:32:21] A lot of that capacity increase was for selling to Anthropic.  
[00:32:25] Because Anthropic saw it before Google. And then Google had Nano Banana and Gemini  
[00:32:29] 3 which caused their user metrics to skyrocket. Then leadership at Google was like, "Oh."  
[00:32:34] Then they started making the statement that we have to double compute every six months,  
[00:32:37] or whatever the exact number was. They really woke up a lot more, and then  
[00:32:42] they went to TSMC and said, "We want more. We want more." TSMC replied, "Sorry guys, we're sold out.  
[00:32:50] We can maybe get 5-10% more for 2026, but really we're going to work on 2027."  
[00:32:54] There was this information asymmetry among the labs, in my mind. I don't know exactly.  
[00:32:59] It's the narrative I've spun myself from seeing all the data in the supply chain on  
[00:33:02] wafer orders and what's going on with the data centers that Anthropic and Fluidstack signed.  
[00:33:09] It's pretty clear to me that Google screwed up. You can see this from Google's Gemini ARR.  
[00:33:16] They had next to nothing in Q1 to Q3—in Q3 a little bit once they started inflecting.  
[00:33:21] But in Q4 they reached $5 billion in revenue on an ARR basis.  
[00:33:30] It's clear Google didn't see revenue skyrocket initially.  
[00:33:34] In a sense, Anthropic had a little bit of commitment issues before their ARR exploded,  
[00:33:40] even though they had far more information asymmetry and saw what was coming down the pipe.  
[00:33:44] Google is going to be more conservative than Anthropic and Google had even less ARR.  
[00:33:52] So they were just not willing to do it, and then they realized they should do it.  
[00:33:58] Since then, Google has gotten absurdly AGI-pilled in terms of what they're doing.  
[00:34:05] They bought an energy company. They're putting deposits down for turbines.  
[00:34:09] They're buying a ridiculous percentage of powered land.  
[00:34:13] They're going to utilities and negotiating long-term agreements.  
[00:34:15] They're doing this on the data center and power side very aggressively.  
[00:34:22] I think Google woke up towards the end of last year, but it took them some time.  
[00:34:26] How many gigawatts do you think Google will have by the end of next year?  
[00:34:28] Buy my data. You charge for that kind of information.  
[00:34:32] Yes, yes. I feel like every year the bottleneck for what is preventing us  
[00:34:37] from scaling AI compute keeps changing. A couple years ago it was CoWoS. Last  
[00:34:41] year it was power. You'll tell me what the bottleneck is this year.  
[00:34:45] But I want to understand five years out, what will be the thing that is  
[00:34:48] constraining us from deploying the singularity? The biggest bottleneck is compute. For that,  
[00:34:55] the longest lead time supply chains are not power or data centers.  
[00:34:59] They're actually the semiconductor supply chains themselves.  
[00:35:01] It switches back from power and data centers as a major bottleneck to chips.  
[00:35:08] In the chip supply chain, there's a number of different bottlenecks.  
[00:35:11] There's memory, logic wafers from TSMC, and the fabs themselves.  
[00:35:17] Construction of the fabs takes two to three years, versus a data center which takes less than a year.  
[00:35:25] We've seen Amazon build data centers in as fast as eight months.  
[00:35:28] There's a big difference in lead times because of the complexity  
[00:35:31] of building the fab that actually makes the chips.  
[00:35:33] The tools also have really long lead times. The bottlenecks, as we've scaled,  
[00:35:39] have shifted based on what the supply chain is currently not able to do.  
[00:35:44] It was CoWoS, power, and data centers, but those were all shorter lead time items.  
[00:35:50] CoWoS is a much simpler process of packaging chips together.  
[00:35:54] Power and data centers are ultimately way simpler than the actual manufacturing of the chips.  
[00:35:59] There's been some sliding of capacity across mobile or PC to data center chips,  
[00:36:08] which has been somewhat fungible. Whereas CoWoS, power, and data  
[00:36:12] centers have had to start anew as supply chains. But now there's no more capacity for the mobile  
[00:36:19] and PC industries—which used to be the majority of the semiconductor industry—to shift over to AI.  
[00:36:26] Nvidia is now the largest customer at TSMC and SK Hynix, the largest memory manufacturer.  
[00:36:33] It's sort of impossible for the sliding of resources away from  
[00:36:39] the common person's PCs and smartphones to shift any more towards the AI chips.  
[00:36:45] So now the question is how do we scale AI chip production?  
[00:36:48] That's the biggest bottleneck as we go to 2030. It would be very interesting if there's an  
[00:36:53] absolute gigawatt ceiling that you can project out to 2030 based just on "We can't produce more  
[00:37:01] than this many EUV machines." To scale compute further,  
[00:37:06] there are different bottlenecks this year and next year, but ultimately by 2028 or 2029,  
[00:37:11] the bottleneck falls to the lowest rung on the supply chain, which is ASML.  
[00:37:16] ASML makes the world's most complicated machine: an EUV tool.  
[00:37:21] The selling price for those is $300-400 million. Currently, they can make about 70.  
[00:37:27] Next year, they'll get to 80. Even under very aggressive supply  
[00:37:31] chain expansion, they only get to a little bit over 100 by the end of the decade. What  
[00:37:35] does that mean? They can make a hundred of these tools by the end of the decade, and 70 right now.  
[00:37:40] How does that actually translate to AI compute? We see all these numbers from Sam Altman and  
[00:37:46] many others across the supply chain: gigawatts, gigawatts, gigawatts.  
[00:37:50] How many gigawatts are we adding? We see Elon saying a hundred gigawatts in space.  
[00:37:55] A year. A year. The problem with any of  
[00:37:59] these numbers, or the challenge to these numbers, is actually not the power or the data center.  
[00:38:04] We can dive into that, but it's manufacturing the chips.  
[00:38:07] Take a gigawatt of Nvidia's Rubin chips. Rubin is announced at GTC,  
[00:38:14] I believe the week this podcast goes live. To make a gigawatt worth of data center  
[00:38:19] capacity of Nvidia's latest chip that they're releasing towards the end of this year,  
[00:38:24] you need a few different wafer technologies. You need about 55,000 wafers of 3 nm.  
[00:38:32] You need about 6,000 wafers of 5 nm, and then you need about 170,000 wafers of DRAM memory.  
[00:38:41] Across these three different buckets, each requires different amounts of EUV.  
[00:38:46] When you manufacture a wafer, there are thousands and thousands of process steps where you're  
[00:38:50] depositing material and removing them. But the key critical step—which at least  
[00:38:55] in advanced logic is 30% of the cost of the chip—is something that  
[00:39:00] doesn't actually put anything on the wafer. You take the wafer, you deposit photoresist,  
[00:39:04] which is a chemical that chemically changes when you expose it to light.  
[00:39:07] Then you stick it into the EUV tool, which shines light at it in a certain way. It  
[00:39:11] patterns it. There's what's called a mask, which is effectively a stencil for the design.  
[00:39:16] When you look at a leading-edge 3 nm wafer, it has 70 or so masks, 70 or so layers of lithography,  
[00:39:23] but 20 of them are the most advanced EUV. If you need 55,000 wafers for a gigawatt, and you  
[00:39:33] do 20 EUV passes per wafer, you can do the math. That's 1.1 million passes of EUV for a single  
[00:39:43] gigawatt. It's pretty simple. Once you add the rest of the stuff, it ends up being 2 million,  
[00:39:47] across 5 nm and all the memory. You're at roughly 2 million EUV  
[00:39:52] passes for a single gigawatt. These tools are very complicated. When you think about  
[00:39:57] what it's doing across a wafer, it's taking the wafer and scanning and stepping across.  
[00:40:03] It does this dozens of times across the whole wafer.  
[00:40:09] When you're talking about how many EUV passes, that’s the  
[00:40:11] entire wafer being exposed at a certain rate. An EUV tool can do roughly 75 wafers per hour,  
[00:40:19] and the tool is up roughly 90% of the time. In the end, you need about three and a half  
[00:40:26] EUV tools to do the 2 million EUV wafer passes for the gigawatt.  
[00:40:32] So three and a half EUV tools satisfies a gigawatt.  
[00:40:35] It's funny to think about the numbers. What does a gigawatt cost? It costs roughly $50 billion.  
[00:40:40] Whereas what do three and a half EUV tools cost? That's $1.2 billion. It's actually quite a lower  
[00:40:46] number, which is interesting to think about. Fifty gigawatts of economic CapEx in the data  
[00:40:53] center, and what gets built on top of that in terms of tokens is even larger.  
[00:40:56] It might be $100 billion worth of AI value into the supply chain,  
[00:41:10] three years, TSMC has done $100 billion of CapEx. So it's $30/$30/$40 billion. A small fraction of  
[00:41:19] that is being used by Nvidia for the 3 nm, or previously 4 nm, that it's using for its chips.  
[00:41:30] What were its earnings last quarter? It was $40 billion.  
[00:41:34] So $40 billion times four is $160 billion. Nvidia alone is turning some small fraction  
[00:41:41] of $100 billion in CapEx, which is going to be depreciated over many years and not just  
[00:41:45] this one year, into $160 billion in a single year. That gets even more intense when you go down the  
[00:41:50] supply chain to ASML, which is taking a billion dollars' worth of machines to produce a gigawatt.  
[00:41:54] Of course, those machines last for more than a year so it’s doing more than that.  
[00:41:58] Now I want to understand, how many such machines will there be by 2030,  
[00:42:02] if you include not just the ones that are sold that year, but have been compiling over the  
[00:42:06] previous years? What does that imply? Sam Altman says he wants to do a gigawatt a week in 2030.  
[00:42:14] When you add up those numbers, is it compatible with that?  
[00:42:17] That's completely compatible, if you think about it.  
[00:42:19] TSMC and the entire ecosystem have something like 250 to 300 EUV tools already.  
[00:42:26] Then you stack on 70 this year, 80 next year, growing to 100 by 2030.  
[00:42:30] You're at 700 EUV tools by the end of the decade. 700 EUV tools, at three and a half tools per  
[00:42:35] gigawatt—assuming it's all allocated to AI, which it's not—gets you to 200 gigawatts worth of AI  
[00:42:43] chips for the data centers to deploy. Sam wants 52 gigawatts a year.  
[00:42:49] He's only taking 25% share then. Obviously, there's some share given to mobile and  
[00:42:54] PC, assuming we're even allowed to have consumer goods still and we don't get priced out of them.  
[00:43:04] But roughly, he's saying 25% market share of the total chips fabbed.  
[00:43:09] That's very reasonable given that this year alone, I think he's going to have  
[00:43:14] access to 25% of the Blackwell GPUs that are deployed. It's not that crazy.  
[00:43:23] When did ASML start shipping EUV tools, when 7 nm started?  
[00:43:27] I don't know when that was exactly. You're saying in 2030, they're going to be using  
[00:43:31] machines that initially were shipped in 2020. So for ten years, you're using the same most  
[00:43:36] important machine in this most technologically advanced  
[00:43:39] industry in the world? I find that surprising. ASML's been shipping EUV tools now for roughly a  
[00:43:45] decade, but it only entered mass volume production around 2020. The tool's not the same. Back then,  
[00:43:52] the tools were even lower throughput. There are various specifications around  
[00:43:57] them called overlay. I was mentioning you're  
[00:43:59] stacking layers on top of each other. You'll do some EUV, you'll do a bunch  
[00:44:02] of different process steps—depositing stuff, etching stuff, cleaning the wafer—dozens of  
[00:44:07] those steps before you do another EUV layer. There's a spec called overlay, which is:  
[00:44:11] you did all this work, you drew these lines on the wafer, now I want to draw these dots.  
[00:44:17] Let's say I want to draw these dots to connect these lines of metal to holes,  
[00:44:21] and then the next layer up is another set of lines going perpendicular, so now you're connecting  
[00:44:25] wires going perpendicular to each other. You have to be able to land them on top of  
[00:44:30] each other. It's called overlay. Overlay is a spec that's been improved rapidly by ASML.  
[00:44:36] Wafer throughput has been improved rapidly by ASML.  
[00:44:38] The price of the tool has gone up, but not as much as the capabilities of the tool.  
[00:44:42] Initially, the EUV tools were $150 million. Over time, they're now $400 million  
[00:44:49] as I look out to 2028. But the capabilities of the  
[00:44:51] tools have more than doubled as well, especially on throughput and overlay accuracy, which is  
[00:44:56] the ability to accurately align the subsequent passes on top of each other even though you do  
[00:45:03] tons of steps between. ASML is improving super rapidly. It's also noteworthy to say that ASML  
[00:45:13] is maybe one of the most generous companies in the world. They have this linchpin thing.  
[00:45:19] No one has anything competitive. Maybe China will have some EUV by the end of the decade, but no one  
[00:45:24] else has anything even close to EUV, and yet they haven't taken price and margins up like crazy.  
[00:45:31] You go ask some other folks that we talk to all the time, like Leopold,  
[00:45:37] and they're like, "Let's have the price go up." Because they can. The margin is there.  
[00:45:42] You can take the margin. Nvidia takes the margin. Memory players are taking the margin.  
[00:45:45] But ASML has never raised the price more than they've increased the capability of the tool.  
[00:45:51] In a sense, they've always provided net benefit to their customers.  
[00:45:54] It's not that the tool is stagnant, it's just that these tools are old.  
[00:45:58] Yes, you can upgrade them some, and the new tools are coming.  
[00:46:01] For simplicity's sake, we're ignoring the advances in overlay  
[00:46:06] or throughput per tool for this podcast. You say we're producing 60 of these machines  
[00:46:10] this year and then 70, 80 over subsequent years.  
[00:46:15] What would happen if ASML just decided to double its CapEx or triple its CapEx?  
[00:46:20] What is preventing them from producing more than 100 in 2030?  
[00:46:23] Why are you so confident that even five years out, you can be  
[00:46:27] relatively sure what their production will be? I think there are a couple factors here.  
[00:46:31] ASML has not decided to just go YOLO, let's expand capacity as fast as possible.  
[00:46:37] In general, the semiconductor supply chain has not.  
[00:46:39] It's lived through the booms and busts, and we can talk a bit more about it.  
[00:46:43] Basically some players have recently woken up, but in general no one really sees demand  
[00:46:52] for 200 gigawatts a year of AI chips, or trillions of dollars of spend a year in  
[00:46:58] the semiconductor supply chain. They're not AI-pilled. They're not AGI-pilled.  
[00:47:02] We're going to get to a trillion dollars this year.  
[00:47:05] Yeah, I feel you, but I'm saying no one really understands this in the supply chain.  
[00:47:11] Constantly, we're told our numbers are way too high, and then when they're right,  
[00:47:14] they're like, "Oh, yeah, but your next year's numbers are still too high."  
[00:47:18] ASML's tool has four major components. It has the source,  
[00:47:25] which is made by Cymer in San Diego. It has the reticle stage, which is made  
[00:47:31] in Wilmington, Connecticut. It has the wafer stage. It has the optics, the lenses and such.  
[00:47:39] Those last two are made in Europe. When you look at each of these four,  
[00:47:42] they're tremendously complex supply chains that, (A) they have not tried to expand massively,  
[00:47:48] and (B) when they try to expand them, the time lag is quite long.  
[00:47:55] Again, this is the most complicated machine that humans make, period, at any sort of volume.  
[00:48:02] Let's talk about the source specifically. What does the source do? It drops these tin droplets.  
[00:48:08] It hits it three subsequent times with a laser perfectly.  
[00:48:11] The first one hits this tin droplet, it expands out.  
[00:48:13] It hits it again, so it expands out to this perfect shape,  
[00:48:16] and then it blasts it at super high power. The tin droplets get excited enough that they  
[00:48:21] release EUV light, 13.5 nanometer, and then it's in this thing that is collecting all  
[00:48:26] the light and directing it into the lens stack. Then you have the lens stack, which is Carl Zeiss,  
[00:48:31] as you mentioned, and some other folks, but Zeiss being the most important part of it.  
[00:48:36] They also have not tried to expand production capacity because they don't see...  
[00:48:40] They're like, "We're growing a lot because of AI. We're growing from 60 to 100." It's like, "No, no,  
[00:48:46] no. We need to go to a couple hundred, but it's fine. Whatever." Each of these tools has, I think,  
[00:48:51] 18 of these lenses, effectively. They are multilayer mirrors,  
[00:48:57] which are perfect layers of molybdenum and ruthenium, if I recall correctly,  
[00:49:03] stacked on top of each other in many layers, and then the light bounces off of it perfectly.  
[00:49:08] When we think about a lens, it's in a shape, and it focuses the light.  
[00:49:12] This is like a mirror that's also a lens, so it's pretty complicated.  
[00:49:16] Any defect in these super thinly deposited stacks will mess it up.  
[00:49:23] Any curvature issues will mess it up. There are a lot of challenges  
[00:49:26] with scaling the production. It's quite artisanal in this sense  
[00:49:29] because you're not making tens of thousands of these a year, you're making hundreds,  
[00:49:34] you're making thousands. 60 tools a year, 18 of these per tool, you’re still in the hundreds,  
[00:49:43] of tools, or you're at the thousand number roughly for these lenses and projection optics.  
[00:49:51] Then you step forward to the reticle stage, which is also something really crazy.  
[00:49:57] This thing moves at, I want to say, nine Gs. It will shift nine Gs because as you step  
[00:50:03] across a wafer, the tool will go... The wafer stage is complementary. It's the  
[00:50:07] wafer part. You line these two things up. You're taking all the light through the  
[00:50:11] lenses that's focused, and here's the reticle, here's the wafer.  
[00:50:16] The reticle's moving one direction, the wafer's moving the other direction as it  
[00:50:20] scans a 26x33 millimeter section of the wafer, and then it stops.  
[00:50:25] It shifts over to another part of the wafer and does it again.  
[00:50:28] It does that in just seconds. Each of them is moving  
[00:50:32] at nine Gs in opposite directions. Each of these things is a wonder and marvel  
[00:50:37] of chemistry, fabrication, mechanical engineering, and optical engineering, because you have to align  
[00:50:47] all these things and make sure they're perfect. All of these things have crazy amounts  
[00:50:50] of metrology because you have to perfectly test everything.  
[00:50:53] If anything is messed up, the yield goes to zero, because this is such a finely tuned system.  
[00:50:58] By the way, it's so large that you're building it in the factory in Eindhoven, Netherlands,  
[00:51:05] and they're deconstructing it and shipping it on many planes to the customer site, and then you're  
[00:51:10] reassembling it there and testing it again. That process takes many, many months.  
[00:51:15] There are so many steps in the supply chain, whether it's Zeiss making their  
[00:51:19] lenses and projection optics or Cymer, which is an ASML-owned company, making the EUV source.  
[00:51:25] Each of these has its own complex supply chain. ASML has commented that their supply chain has  
[00:51:29] over ten thousand people in it. Like individual suppliers?  
[00:51:32] Yes. It might not be directly. It might be through Zeiss having so many suppliers  
[00:51:37] and XYZ company having so many suppliers. If you just think about it, you're talking  
[00:51:44] about two physically moving objects that are the size of a wafer, and it has to be accurate  
[00:51:51] to the level of single-digit nanometers or even smaller because the entire system, the overlay,  
[00:51:58] the layer-to-layer overlay variation, has to be on the order of 3 nanometers.  
[00:52:04] If the overlay is 3 nms, that means each individual part, the accuracy of its  
[00:52:09] physical movement has to be even less than that. It has to be sub-one nanometer in most cases,  
[00:52:14] because the error of these things stack up. There's no way to just snap your fingers and  
[00:52:23] increase production. Things as simple as power. The US going from zero percent power growth to  
[00:52:27] two percent power growth, even though China's already at thirty, was so hard for America to do.  
[00:52:34] And that's a really simple supply chain with very few people in it who make difficult things.  
[00:52:41] There are probably 100,000 electricians and people who work in  
[00:52:45] the electricity supply chain, or more, in the US? When you look at ASML, they employ so few people.  
[00:52:53] Carl Zeiss probably employs less than a thousand people working on this, and all of  
[00:52:58] those people are super, super specialized. You can't just train random people up  
[00:53:02] for this in the snap of a finger. You can't just get your entire supply  
[00:53:06] chain to get galvanized. Nvidia's had to do a lot  
[00:53:11] to get the entire supply chain to even deliver the capacity they're going to make this year.  
[00:53:15] When you go talk to Anthropic, they're like, "We're short of TPUs, we're short  
[00:53:18] of training, and we're short of GPUs." When you go talk to OpenAI, they're like,  
[00:53:21] "We're short of these things." OpenAI and Anthropic know they need X.  
[00:53:25] Nvidia is not quite as AGI-pilled. They're building X - 1. You go down the  
[00:53:31] supply chain, everyone's doing X - 1. In some cases, they're doing X ÷ 2,  
[00:53:36] because they're not AGI-pilled. You end up with this time lag  
[00:53:42] for the whip to react. The AI-pilledness and the  
[00:53:48] desire to increase production takes so long. Once they finally understand that they need  
[00:53:53] to increase production rapidly… They think they understand.  
[00:53:57] They think AI means we have to go from 60 to 100, in addition to the tools getting  
[00:54:01] better and faster, the source getting higher power from 500 watts to 1,000,  
[00:54:05] and all these other aspects of the supply chain advancing technically and increasing production.  
[00:54:09] They think they're actually increasing production a lot.  
[00:54:13] But if you flow through the numbers… What does Elon want?  
[00:54:15] He wants 100 gigawatts a year in space by 2028 or 2029.  
[00:54:23] Sam Altman wants 52 gigawatts a year by the end of the decade.  
[00:54:28] Anthropic probably needs the same, and Google needs that.  
[00:54:32] You go across the supply chain, and it's like, wait, no, the supply chain can't  
[00:54:35] possibly build enough capacity for everyone to get what they want on the side of compute.  
[00:55:44] I feel like in the data center supply chain for the last few years,  
[00:55:50] people have been making arguments like, "We are bottlenecked by this specific thing, therefore  
[00:55:55] AI compute can't scale more than X." But as you've written about, if the  
[00:56:00] grid is a bottleneck, then we just do behind the meter on the site, we do gas turbines, et cetera.  
[00:56:06] If that doesn't work, there are all these other alternatives that people fall back on.  
[00:56:11] I want to ask whether we can imagine a similar thing happening in the semiconductor supply chain.  
[00:56:17] If EUV becomes a bottleneck, what if we just went back to 7 nm and did what China  
[00:56:24] is doing currently, producing 7 nm chips with multi-patterning with DUV machines?  
[00:56:31] If you look at a 7 nm chip like the A100, there's been a lot of progress  
[00:56:36] obviously from the A100 to the B100 or B200. How much of that progress is just numerics?  
[00:56:45] If you just hold FP16 constant from A100 to B100. The B100 is a little over one petaflop, and the  
[00:56:54] A100 is like 300 teraflops. Yeah, 312.  
[00:57:02] Holding numerics constant, you have a 3x improvement from A100 to B100.  
[00:57:07] Some of that is the process improvement, some of that is just the accelerator design improving,  
[00:57:11] which we could replicate again in the future. It seems there's actually a very small effect  
[00:57:16] from the process improving from 7nm to 4 nm. I don't know the numbers offhand but let's  
[00:57:24] say there's 150k wafers per month of 3 nm and eventually similar amounts for 2 nm.  
[00:57:31] But then there's a similar amount for 7 nm. If you have all those old wafers and there's  
[00:57:36] maybe a 50% haircut because the bits per wafer area are 50% less or something,  
[00:57:45] it doesn't seem that bad to just bring on 7 nm wafers if that gives you another fifty or  
[00:57:50] hundred gigawatts. Tell me why that's naive. We potentially do go crazy enough that this  
[00:58:01] happens because we just need incremental compute, and the compute is worth the  
[00:58:04] higher cost and power of these chips. But it's also unlikely to a large extent  
[00:58:13] because some of these are not fair comparisons. For example, from A100, which is 312 teraflops,  
[00:58:22] to Blackwell, which is 1,000 or 2,000 FP16, and then Rubin is 5,000 or so FP16… It's not  
[00:58:31] a fair comparison because these chips have vastly different design targets.  
[00:58:38] With A100, Nvidia optimized for FP16 and BF16 numerics.  
[00:58:45] When you look at Hopper, they didn't care as much about that; they cared about FP8.  
[00:58:49] When you look at Rubin, they don’t care about FP16 and BF16 so much,  
[00:58:53] they care mostly about FP4 and FP6. Numerics are what they've designed their chip for.  
[00:59:06] Let's say we make a new chip design on 7 nm, optimized for the numerics of the modern day.  
[00:59:14] The performance difference is still going to be much larger  
[00:59:16] than the FLOPS difference you mentioned. Often it's easy to boil things down to FLOPS  
[00:59:23] per watt or FLOPS per dollar, but that's not a fair comparison.  
[00:59:32] Let's look at Kimi K2.5 and DeepSeek. When you look at those two models and  
[00:59:40] their performance on Hopper versus Blackwell on very optimized software,  
[00:59:45] you get vastly different performance. Most of this is not attributed to  
[00:59:50] FLOPS or numerics, because those models are actually eight-bit.  
[00:59:55] So it's not like Blackwells and Hopper are both optimized for eight-bit, and Blackwell is not  
[00:59:59] really taking advantage of its four-bit there. The performance gulf is actually much larger.  
[01:00:09] Sure it's one thing to shrink process technology and make the transistor smaller  
[01:00:14] so each chip has X number of FLOPS, but you forget the big gating factor.  
[01:00:18] These models don't run on a single chip. They run on hundreds of chips at a time.  
[01:00:22] If you look at DeepSeek's production deployment, which is well over a  
[01:00:25] year old now, they were running on 160 GPUs. That's what they serve production traffic on.  
[01:00:31] They split the model across 160 GPUs. Every time you cross the barrier from one  
[01:00:35] chip to another, there is an efficiency loss. You have to transmit over high-speed  
[01:00:40] electrical SerDes, which brings a latency cost and a power cost.  
[01:00:44] There are all these dynamics that hurt. As you shrink and shrink the process node, you've  
[01:00:51] increased the amount of compute in a single chip. Now in-chip movement of data is at least tens  
[01:01:01] of terabytes a second, if not hundreds of terabytes a second.  
[01:01:04] Whereas between chips, you're on the order of a terabyte a second.  
[01:01:09] Then you have this movement of data between chips that are super close to each other physically.  
[01:01:13] You can only put so many chips close to each other physically,  
[01:01:15] so you have to put chips in different racks. The movement of data between racks is on the order  
[01:01:20] of hundreds of gigabits a second, 400 gig or 800 gig a second, so roughly 100 gigabytes a second.  
[01:01:27] So you have this huge ladder: on-chip communication is super fast, within the  
[01:01:32] rack is an order of magnitude slower, and outside the rack is an order of magnitude lower than that.  
[01:01:39] As you break the bounds of chips, you end up with a performance loss.  
[01:01:43] The reason I explain this is because when you look at Hopper versus Blackwell,  
[01:01:47] even if both are using a rack's worth of chips, Hopper is significantly slower.  
[01:01:52] The amount of performance you have leveraged to the task within each domain—tens of terabytes a  
[01:02:00] second of communication between these processing elements versus terabytes a second between these  
[01:02:06] processing elements—is much, much higher and therefore the performance is much higher.  
[01:02:11] When you look at inference at 100 tokens a second for DeepSeek and Kimi K2.5,  
[01:02:19] the performance difference between Hopper and Blackwell is on the order of 20x.  
[01:02:21] It's not 2x or 3x like the FLOPS performance difference indicates,  
[01:02:24] even though those are on the same process node. There are just differences in networking  
[01:02:28] technologies and what they've worked on. You can translate some of these back,  
[01:02:32] but when you look at what they're doing on 3 nm with Rubin, some of those things  
[01:02:36] are simply not possible to do all the way back on A100, even if you make a new chip for 7 nm.  
[01:02:42] There are certain architectural improvements you can port and certain ones you cannot.  
[01:02:47] The performance difference is not just going to be the difference in FLOPS.  
[01:02:50] It's in some senses cumulative between the difference in FLOPS per chip,  
[01:02:56] networking speed between chips, how many FLOPS are on a chip versus a system, and memory  
[01:03:00] bandwidth on a single chip versus an entire system. All of these things compound.  
[01:03:03] Can I ask you a very naive question? The B200 now has two dies on a single chip,  
[01:03:10] so you can get that bandwidth without having to go through NVLink or InfiniBand.  
[01:03:16] Next year, Rubin Ultra will have four dies on one chip.  
[01:03:19] What is preventing us from just doing that with an older… How many dies could  
[01:03:24] you have on a single chip and still get these tens of terabytes a second?  
[01:03:28] Even within Blackwell, there are differences in  
[01:03:32] performance when you're communicating on the chip versus across the chips.  
[01:03:36] Those bounds are obviously much smaller than when you're going out of the entire chip.  
[01:03:45] When you scale the number of chips up, there is some performance loss.  
[01:03:50] It's not perfect, but it is way better than different entire packages.  
[01:03:54] How large can advanced packaging scale? The way Nvidia is doing it is CoWoS.  
[01:04:01] Google, Broadcom, MediaTek, and Amazon's Trainium are all doing CoWoS.  
[01:04:07] But actually you can go look back at what Tesla did with Dojo, which they cancelled and restarted.  
[01:04:16] Dojo was a chip that was the size of an entire wafer.  
[01:04:19] They had 25 chips on it. There were some tradeoffs. They couldn't put HBM on it.  
[01:04:26] But the positive side was that they had 25 chips on it.  
[01:04:30] To date, it is still probably the best chip for running convolutional neural networks.  
[01:04:35] It's just not great at transformers because the shape of the chip, the memory, the arithmetic,  
[01:04:41] and all these various specifications are just not well-suited for transformers. They're  
[01:04:45] well-suited for CNNs. Dojo chips were optimized around that, and they made a bigger package.  
[01:04:52] But as you make packages bigger and bigger, you have other constraints: networking speed,  
[01:04:59] memory bandwidth, and cooling capabilities. All of these things start to rear their heads.  
[01:05:03] It's not simple. But yes, you will see a trend line of more chips on the package, and yes,  
[01:05:08] you're going to be able to do that on 7 nm. In fact, that's what Huawei did  
[01:05:11] with their Ascend 910C or D. They initially put one, and then they did two.  
[01:05:20] They're focusing on scaling the packaging up because that is an  
[01:05:23] area where they can advance faster than process technology where they can't shrink.  
[01:05:28] But at the end of the day, that’s something you can do on the leading-edge chips too.  
[01:05:32] Anything you do on 7 nm, you can also probably do on 3 nm in terms of packaging.  
[01:05:36] If we end up in this world in 2030 where the West has the most advanced process technology  
[01:05:42] but has not ramped it up as much, whereas China… I don't know if you think by 2030  
[01:05:48] they would have EUV and 2 nm or whatever. But they are semiconductor-pilled and they  
[01:05:53] are producing in mass quantity. Basically, I'm wondering what  
[01:05:57] the year is where there's a crossover, where our advantage in process technology has faded enough,  
[01:06:03] and their advantage in scale has increased enough. And also, if their advantage in having one country  
[01:06:09] with the entire supply chain indigenized—rather than having random suppliers in Germany  
[01:06:13] and the Netherlands—would mean that China would be ahead in its ability to produce mass flops.  
[01:06:22] To date, China still does not have an entirely indigenized semiconductor supply chain.  
[01:06:28] But would they in 2030? By 2030, it's possible that they do.  
[01:06:33] But to date, all of China's 7 nm and 14 nm capacity uses ASML DUV tools.  
[01:06:42] The amount that they can import from ASML is large.  
[01:06:47] But the vast majority of ASML's revenue, especially on EUV all of it, is outside of China.  
[01:06:54] The scale advantage is still in the favor of the West plus Taiwan,  
[01:06:58] Japan, and Korea, et cetera. But they're trying to make  
[01:06:59] their own DUV and EUV tools, right? They're trying to do all these things.  
[01:07:03] The question is how fast can they advance and scale up production as well as quality.  
[01:07:08] To date, we haven't seen that. Now I'm quite bullish that they're  
[01:07:12] going to be able to do these things over the next five to ten years.  
[01:07:16] They will really scale up production and kick it into high gear.  
[01:07:20] They have more engineers working on it and more desire to throw capital at the problem.  
[01:07:24] So by 2030, will they have fully indigenized DUV? I think for sure. DUV, yes.  
[01:07:28] And fully indigenized EUV by 2030? I think they'll have working tools.  
[01:07:32] I don't think that they'll be able to manufacture a bunch yet.  
[01:07:36] There's having it work, and then there's production hell.  
[01:07:42] ASML had EUV working in the early 2010s at some capacity.  
[01:07:49] The tools were not accurate enough. They were not scaled for high-volume  
[01:07:54] manufacturing or reliable enough. They had to ramp production,  
[01:07:57] and that all took time. Production hell takes time. That's why it took another five to seven  
[01:08:01] years to get EUV into mass production at a fab rather than just working in the lab.  
[01:08:07] How many DUV tools do you think they'll be able to manufacture in 2030?  
[01:08:11] ASML? No, China.  
[01:08:14] That's a great question. It's a bit of a challenge to look into this supply chain  
[01:08:23] especially. We try really hard. In some instances, they're buying stuff from Japanese vendors.  
[01:08:31] If they want a fully indigenized supply chain, they need to not buy these lenses, projection  
[01:08:36] optics, or stages from Japanese vendors. They need to build it internally.  
[01:08:40] It's really tough to say where they'll be able to get to.  
[01:08:42] I honestly think it's a shot in the dark. But it's probably not unlikely that they'll  
[01:08:46] be able to do on the order of 100 DUV tools a year, whereas ASML is currently doing  
[01:08:51] hundreds of DUV tools a year. No company has a process node  
[01:09:00] where they make a million wafers a month. Elon says he wants to do it and China is  
[01:09:05] obviously going to do it. TSMC is trying to do that.  
[01:09:12] The memory makers may get to a million wafers a month as well, but not in a single fab.  
[01:09:16] It's mind-boggling to think of that scale, and challenging to  
[01:09:22] see the supply chain galvanized for that. I don't want to doubt China's capability to scale.  
[01:09:29] I guess this is an interesting question. I think at some point SemiAnalysis  
[01:09:34] will do the deep dive on this. By when would indigenized Chinese production  
[01:09:44] be bigger than the rest of the West combined. And put in the input of your model of when they'll  
[01:09:52] have DUV machines and EUV machines at scale? Because there's this question around if you  
[01:09:56] have long timelines on AI—by long meaning 2035, which is not that long in the grand  
[01:10:00] scheme of things—should you expect a world where China is dominating in semiconductors?  
[01:10:06] It doesn't get asked enough because if you're in San Francisco,  
[01:10:09] we're thinking on timescales of weeks. If you're outside of San Francisco,  
[01:10:14] you're not thinking about AGI at all. What if we have AGI? What if you have this transformational  
[01:10:19] thing that is commanding tens or hundreds of trillions of dollars of economic growth  
[01:10:23] and token output, but it happens in 2035? What does that imply for the West versus China?  
[01:10:33] SemiAnalysis has got to write the definitive model on this.  
[01:10:39] It's really challenging when you move timescales out that far.  
[01:10:43] What we tend to focus on is tracking every data center, every fab, and all the tools.  
[01:10:48] We track where they're going, but the time lags for these things are relatively short.  
[01:10:54] We can only make reasonably accurate estimates for data center capacity based on land purchasing,  
[01:11:01] permits, and turbine purchasing. We know where all these things  
[01:11:04] are going, that's the data we sell. As you go out to 2035, things are just  
[01:11:10] so radically different. Your error bars get so  
[01:11:13] large it's hard to make an estimate. But at the end of the day, if takeoff  
[01:11:19] or timelines are slow enough, I don't see why China wouldn't be able to catch up drastically.  
[01:11:28] In some sense, we've got this valley where, three to six months ago, or maybe even now, Chinese  
[01:11:36] models are as competitive as they've ever been. I think Opus 4.6 and GPT 5.4 have really pulled  
[01:11:41] away and made the gap a little bit bigger, but I'm sure some new Chinese models will come out.  
[01:11:45] As we move from selling tokens where they provide the entire reasoning chain, to  
[01:11:53] selling automated white-collar work—an automated software engineer, you send them the request,  
[01:11:59] they give you the result back, and there's a bunch of thinking on the back end that they don't show  
[01:12:02] you—the ability to distill out of American models into Chinese models will be harder.  
[01:12:05] Second, look at the scale of the compute the labs have.  
[01:12:10] OpenAI exited the year with roughly two gigawatts last year.  
[01:12:13] Anthropic will get to two-plus gigawatts this year.  
[01:12:17] By the end of next year, they'll both be at ten gigawatts of capacity.  
[01:12:21] China is not scaling their AI lab compute nearly as fast.  
[01:12:25] At some point, when you can't distill the learnings from these labs into the Chinese  
[01:12:30] models, plus with this compute race that OpenAI, Anthropic, Google, and Meta are all racing on,  
[01:12:37] they end up getting to a point where the model performance should start to diverge more.  
[01:12:44] Then look at all this CapEx being spent on data centers.  
[01:12:49] Amazon is spending $200 billion, Google $180 billion.  
[01:12:53] All these companies are spending hundreds of billions of dollars on CapEx.  
[01:12:57] There's nearly a trillion dollars of CapEx being invested in data  
[01:13:02] centers in America this year, roughly. What's the return on invested capital here?  
[01:13:08] You and I would think the return on invested capital for data center CapEx is very high.  
[01:13:14] If we look at Anthropic's revenues, in January they added $4 billion.  
[01:13:18] In February, which was a shorter month, they added $6 billion.  
[01:13:21] We'll see what they can do in March and April,  
[01:13:24] given that compute constraints are what's bottlenecking their growth.  
[01:13:27] The reliability of Claude is quite low because they're so compute constrained.  
[01:13:31] But if this continues, then the ROIC on these data centers is super high.  
[01:13:36] At some point, the US economy starts growing faster and faster over this year and next year  
[01:13:42] because of all this CapEx, all the revenue these models are generating, and the downstream supply  
[01:13:47] chain. China doesn't have that yet. They have not built the scale of infrastructure  
[01:13:54] to invest in models, get to the capabilities, and then deploy these models at such scale.  
[01:14:00] When you look at Anthropic, they're at $20 billion ARR.  
[01:14:05] The margins are sub-50 percent, at least as last reported by The Information.  
[01:14:09] So that's $13 or $14 billion of compute that it's running on rental cost-wise, which is actually $50  
[01:14:16] billion worth of CapEx that someone laid out for Anthropic to generate their current revenue.  
[01:14:22] China has just not done this. If and when Anthropic 10Xs revenue again—and  
[01:14:28] I think our answer would be when, not if—China doesn't have the compute to deploy at that scale.  
[01:14:34] So there is some sense that we're in a fast takeoff.  
[01:14:39] It's not like we're talking about a Dyson sphere by X date,  
[01:14:42] it's more like the revenue is compounding at such a rate that it does affect economic growth.  
[01:14:47] The resources these labs are gathering are growing so fast.  
[01:14:51] China hasn't done that yet, so in that case, the US and the West are actually diverging.  
[01:14:56] The flip side is that these infrastructure investments have middling returns.  
[01:15:01] Maybe they're not as good as hoped. Maybe Google is wrong for wanting  
[01:15:05] to take free cash flow to zero and spend $300 billion on CapEx next year.  
[01:15:09] Maybe they’re just wrong and people on Wall Street who are bearish and people  
[01:15:13] who don't understand AI are correct. In that case, the US is building all  
[01:15:19] this capacity but doesn't get great returns. Meanwhile, China is able to build a fully  
[01:15:23] vertical, indigenized supply chain, instead of the US/Japan/Korea/Taiwan/SE Asia/Europe countries  
[01:15:33] together building this less vertical supply chain. In a sense, at some point China is able to scale  
[01:15:40] past us if AI takes longer to get to certain capability levels than the vast majority of  
[01:15:47] your guests on this podcast believe. It's fast timelines, the US wins;  
[01:15:50] long timelines, China wins. Yeah but I don't know what fast timelines means.  
[01:15:54] I don't think you have to believe in AGI to have the timelines where the US wins.  
[01:16:01] Let's go back to memory. I think people on Wall Street and people in the industry are  
[01:16:06] understanding how big this is, but maybe generally people don't understand what a big deal it is.  
[01:16:10] So we've got this memory crunch, as you were talking about.  
[01:16:12] And earlier I was asking about, oh, could we solve for the EUV  
[01:16:16] tool shortage by going back to seven nanometers? So let me ask a similar question about memory.  
[01:16:21] HBM is made of DRAM, but has three to four times fewer bits per wafer  
[01:16:26] area than the DRAM it's made out of. Is it possible that accelerators in the  
[01:16:30] future could just use commodity DRAM and not HBM, so we can get  
[01:16:35] much more capacity out of the DRAM we have? The reason I think this might be possible is,  
[01:16:43] if we're going to have agents that are just going off and doing work, and it's  
[01:16:48] not a synchronous chatbot application, then you don't necessarily need extremely fast latency.  
[01:16:57] Maybe you can have lower bandwidth, because the reason you stack DRAM into  
[01:17:04] HBM is for higher bandwidth. Is it possible to go to HBM  
[01:17:09] accelerators and basically have the opposite of Claude Code Fast, like have Claude Slow?  
[01:17:17] At the end of the day, the incremental purchaser who's willing to pay the highest  
[01:17:20] price for tokens also ends up being the one that's less price-sensitive.  
[01:17:26] Compute should be allocated, in a capitalistic society, towards the goods that have the  
[01:17:31] highest value, and the private market determines this by willingness to pay.  
[01:17:35] To some extent, Anthropic could actually release a slow mode.  
[01:17:39] They could release Claude Slow Mode and increase tokens per dollar by a significant amount.  
[01:17:46] They could probably reduce the price of Opus 4.6 by 4-5x and reduce the speed by maybe just 2x.  
[01:17:54] The curve on inference throughput versus speed is already there just on HBM.  
[01:17:59] And yet they don't, because no one actually wants to use a slow model.  
[01:18:04] Furthermore, on these agentic tasks, it's great that the model can run at a time horizon of hours.  
[01:18:11] But if the model was running slower, those hours would become a day.  
[01:18:16] Vice versa, if the model is running faster, those hours become an hour.  
[01:18:21] No one really wants to move to a day-long wait period, because the highest-value tasks also have  
[01:18:27] some time sensitivity to them. I struggle to see… Yes,  
[01:18:34] you could use regular DRAM. There are a couple of challenges with this.  
[01:18:44] One of the core constraints of chips is that a chip is a certain size, and all  
[01:18:52] of the I/O escapes on the edges. Often, the left and right of the  
[01:18:58] chip are HBM—so the I/O from the chip to the HBM is on the sides—and then the  
[01:19:02] top and bottom are I/O to other chips. If you were to change from HBM to DDR,  
[01:19:11] all of a sudden this I/O on the edge would have significantly less bandwidth,  
[01:19:17] but significantly more capacity per chip. But the metric you actually care about  
[01:19:28] is bandwidth per wafer, not bits per wafer. Because the thing that is constraining the FLOPS  
[01:19:34] is just getting in and out the next matrix, and for that you just need more bandwidth.  
[01:19:39] Yeah, getting out the weights and getting in and out the KV cache.  
[01:19:44] In many cases, these GPUs are not running at full memory capacity.  
[01:19:47] It's obviously a system design thing: model, hardware, and software co-design.  
[01:19:52] You have to figure out how much KV cache you need, how much you keep on the chip,  
[01:19:55] how much you offload to other chips and call when you need it for tool calling,  
[01:20:00] and how many chips you parallelize this on. Obviously, the search space for this is very  
[01:20:05] broad, which is why we have InferenceX, an open-source model that searches all  
[01:20:09] the optimal points on inference for a variety of different chips and models.  
[01:20:16] The point is, you're not always necessarily constrained by memory capacity.  
[01:20:22] You can be constrained by FLOPS, network bandwidth, memory bandwidth, or memory capacity.  
[01:20:30] If you really simplify it down, there are four constraints,  
[01:20:33] and each of these can break out into more. If you switch to DDR, yes, you produce  
[01:20:39] four times the bits per DRAM wafer, but all of a sudden the constraints shift a lot and your  
[01:20:44] system design shifts. You go slower. Is the market smaller? Maybe. But also,  
[01:20:50] all these FLOPS are wasted because they're just sitting there waiting for memory.  
[01:20:53] You don't need all that capacity because you can't really increase batch size because then the KV  
[01:20:58] cache would take even longer to read. Makes sense. What is the bandwidth  
[01:21:04] difference between HBM and normal DRAM? An HBM4 stack—let's talk about the stuff  
[01:21:11] that's in Rubin, because that's what we've been indexing on—is 2048 bits across, connected in an  
[01:21:16] area that's 13 millimeters wide. It transfers memory at around  
[01:21:22] 10 giga-transfers a second. So a stack of HBM4 is 2048 bits on  
[01:21:27] an area that's roughly 11 to 13 millimeters wide. That's the shoreline you're taking on the chip.  
[01:21:33] In that shoreline, you have 2048 bits transferring at 10 giga-transfers per second.  
[01:21:39] You multiply those together and divide by eight,  
[01:21:41] bits to a byte, and you're at roughly 2.5 terabytes a second per HBM stack.  
[01:21:46] When you look at DDR, in that same area, it's maybe 64 or 128 bits wide.  
[01:21:53] That DDR5 is transferring at anywhere from 6.4 to maybe 8,000 giga-transfers a second.  
[01:22:01] So your bandwidth is significantly lower. It's 64 times 8,000 divided by  
[01:22:07] eight, which puts you at 64 gigabytes a second. Even if you take a generous interpretation of  
[01:22:14] 128 times 8 giga-transfers, you're at 128 gigabytes a second for the same shoreline,  
[01:22:18] versus 2.5 terabytes a second. There's an order of magnitude  
[01:22:21] difference in bandwidth per edge area. If your chip is a square, or 26 by 33  
[01:22:27] millimeters—which is the maximum size for an individual die—you only have so much edge area.  
[01:22:32] On the inside of that chip, you put all your compute.  
[01:22:34] There are things you can do to try and change that, like more SRAM or more caching.  
[01:22:38] But at the end of the day, you're very constrained by bandwidth.  
[01:22:42] Then there's the question of where you can destroy demand to free up enough for AI.  
[01:22:48] I guess the picture is especially bad because, as you're saying, if it takes four times more  
[01:22:52] wafer area to get the same byte, for HBM you have to destroy four times as much consumer demand for  
[01:22:58] laptops and phones to free up one byte for AI. What does this imply for the next year or two?  
[01:23:08] Sorry for the run-on question, in your newsletter you said 30% of Big Tech's CapEx in 2026 is going  
[01:23:14] towards memory? Yes.  
[01:23:16] That's insane, right? Of the $600 billion or whatever, 30% is going just to memory.  
[01:23:23] Yes. Obviously, there's some level of margin stacking that Nvidia does,  
[01:23:26] so you have to separate that out and apply their margin to the memory and the logic.  
[01:23:30] But at the end of the day, a third of their CapEx is going to memory.  
[01:23:33] That's crazy. What should we expect over the next year or two as this memory crunch hits?  
[01:23:41] The memory crunch will continue to get harder, and prices will continue to go up.  
[01:23:48] This affects different parts of the market differently.  
[01:23:52] Are people going to hate AI more and more? Yes, because smartphones and PCs are not  
[01:23:56] going to get incrementally better year on year. In fact, they're going to get incrementally worse.  
[01:24:00] If you look at the bill of materials for an iPhone, what fraction of it is the memory?  
[01:24:04] How much more expensive does an iPhone get if the memory is two times more expensive?  
[01:24:09] I believe an iPhone has 12 gigabytes of memory. Each gig used to cost roughly $3-4, so that's $50.  
[01:24:17] But now the price of memory has tripled. Let's say it's $12 per gig for DDR.  
[01:24:23] Now you're talking about $150 versus $50. That's a $100 increase in cost for Apple.  
[01:24:30] Apple has some margin, they're not just going to eat the margin.  
[01:24:32] NAND also has the same market dynamics, so in reality, it's probably a $150  
[01:24:32] increase on the iPhone. So now that’s a $100 cost  
[01:24:33] increase and that’s just on the DRAM. The NAND also has the same sort of market.  
[01:24:37] So in fact it’s probably a $150 increase on the iPhone.  
[01:24:41] Apple either has to pass that on to the consumer or eat it.  
[01:24:46] I don't see Apple reducing their margin too much, maybe they eat a little bit.  
[01:24:49] But at the end of the day, that means the end consumer is paying $250 more for an iPhone.  
[01:24:54] Now that’s just on last year’s pricing versus today’s.  
[01:24:59] There is some lag before Apple feels the heat because they tend to have long-term contracts  
[01:25:06] for memory that last three months to a year. But at the end of the day, Apple gets hit  
[01:25:09] pretty hard by this. They won't really  
[01:25:13] adjust until the next iPhone release. But that's the high end of the market,  
[01:25:17] which is only a few hundred million phones a year. Apple sells two or three hundred million  
[01:25:20] phones annually. The bulk of the market is mid-range and low-end.  
[01:25:25] It used to be that 1.4 billion smartphones were sold a year.  
[01:25:28] Now we're at about 1.1 billion. Our projections are that we might  
[01:25:31] drop to 800 million this year, and down to 500 or 600 million next year.  
[01:25:37] We look at data points out of China from some of our analysts in Asia,  
[01:25:42] Singapore, Hong Kong, and Taiwan. They've been tracking this,  
[01:25:45] and they see Xiaomi and Oppo cutting low-end and mid-range smartphone volumes by half.  
[01:25:52] Yes, it’s only a $150 BOM increase on a $1,000 iPhone where Apple has some larger margin.  
[01:26:02] But for smaller phones, the percentage of the BOM that goes to memory and storage is much larger.  
[01:26:08] And the margins are lower, so there's less capacity to even eat the margins.  
[01:26:13] And they have also generally tended not to do long-term agreements on memory.  
[01:26:20] Why this is a big deal is that if smartphone volumes halve, that drop will happen in  
[01:26:26] the low and mid-range, not the high end. So it’s not like the bits released are halving.  
[01:26:32] Currently, consumer devices account for more than half of memory demand.  
[01:26:35] Even if you halve smartphone volumes, because of the shape of the halving,  
[01:26:38] the low end gets cut by more than half, while the high end gets cut by less than half,  
[01:26:42] because you and I will still buy the high-end phones that cost north of a thousand dollars.  
[01:26:46] We'll buy them even if they get a little bit more expensive.  
[01:26:48] And Apple's volumes will not go down as much as a low-end smartphone provider.  
[01:26:52] The same applies to PCs. What this does to the market is quite drastic.  
[01:26:59] DRAM gets released and goes to AI chips, who are willing to do longer-term contracts and pay higher  
[01:27:06] margins, because at the end of the day the margin they extract from the end user is much larger.  
[01:27:14] This probably leads to people hating AI even more. Today, you already see all the memes on PC  
[01:27:22] subreddits and gaming PC Twitter. It's cat dancing videos saying,  
[01:27:27] "This is why memory prices have doubled and you can't get a new gaming GPU or desktop."  
[01:27:33] It's going to be even worse when memory prices double again, especially DRAM.  
[01:27:37] Another interesting dynamic is that it's not just DRAM, it's also NAND.  
[01:27:42] NAND is also going up in price. Both of these markets have expanded capacity very  
[01:27:46] slowly over the last few years, NAND almost zero. The percentage of NAND that goes to phones and  
[01:27:54] PCs is larger than the percentage of DRAM that goes to phones and PCs.  
[01:27:58] As you destroy demand, mostly for DRAM purposes, you unlock more NAND  
[01:28:03] that gets allocated and can go to other markets. The price increases of DRAM will be larger than  
[01:28:09] those of NAND because you've released more from the consumer, and in fact,  
[01:28:13] you've produced more memory for AI. Sorry, maybe you just explained  
[01:28:18] it and I missed it. Is it because SSDs are  
[01:28:21] being used in large quantities for data centers? They are, but not in as large quantities as DRAM.  
[01:28:27] Okay, so they will also increase because they'll be using some quantity, but there's  
[01:28:32] not as much of a need as there is for HBM. Makes sense. One thing I didn't appreciate until I was  
[01:28:37] reading some of your newsletters is that the same constraints preventing logic scaling over  
[01:28:43] the next few years are quite similar to what's preventing us from producing more memory wafers.  
[01:28:49] In fact, literally the same exact machine, this EUV tool, is needed for memory.  
[01:28:55] So I guess the question someone could ask right now is, why can't we just make more memory?  
[01:29:05] The constraints, as I was mentioning earlier, are not necessarily EUV tools today or next year.  
[01:29:11] They become that as we get to the latter part of the decade.  
[01:29:15] Currently, the constraints are more that they physically just haven't built fabs.  
[01:29:20] Over the last three to four years, these vendors have not built new fabs  
[01:29:25] because memory prices were really low. Their margins were low, and in fact,  
[01:29:29] they were losing money in 2023 on memory. So they decided they weren't building new fabs.  
[01:29:34] The market slowly recovered over time but never really got amazing until last year.  
[01:29:40] In 2024, we were banging on the drums that reasoning means long context,  
[01:29:44] which means a large KV cache, which means you need a lot of memory demand.  
[01:29:48] We've been talking about that for a year and a half, two years.  
[01:29:51] People who understand AI went really long on memory then.  
[01:29:57] So you’ve seen that dynamic, but now it has finally played out in pricing.  
[01:30:01] It took so long for what was obvious: long context means the KV  
[01:30:05] cache gets bigger, you need more memory. Half the cost of accelerators is memory.  
[01:30:09] Of course they're going to start going crazy on it.  
[01:30:13] It took a year for that to actually reflect in memory prices.  
[01:30:16] Once memory prices reflected that, it took another three to six months for the  
[01:30:20] memory vendors to start building fabs. Those fabs take two years to build.  
[01:30:24] So we won't have really meaningful fabs to even put these tools in until late 2027 or 2028.  
[01:30:34] Instead, you've seen some really crazy stuff to get capacity.  
[01:30:39] Micron bought a fab from a company in Taiwan that makes lagging-edge chips.  
[01:30:47] Hynix and Samsung are doing some pretty crazy things to try and expand capacity  
[01:30:51] at their existing fabs, which also have large knock-on effects in the economy.  
[01:30:56] So why can't we build more capacity? There's nowhere to put the tools.  
[01:31:02] It's not just EUV; there are other tools involved in DRAM and logic.  
[01:31:06] In logic, for N3, about 28%  
[01:31:11] of the cost of the final wafer is EUV. When you look at DRAM, it's in the teens.  
[01:31:19] It's going up, but it's a much smaller percentage of the cost.  
[01:31:24] These other tools are also bottlenecks, although their supply chains are not as complex as ASML's.  
[01:31:30] You see Applied Materials, Lam Research, and all these other  
[01:31:32] companies expanding capacity a lot as well. But you don't have anywhere to put the tool,  
[01:31:37] because the most complex buildings people make are fabs, and fabs take two years to build.  
[01:32:40] I interviewed Elon recently, and his whole plan is that they're going to build this TeraFab  
[01:32:47] and they're going to build the clean rooms. I won't even ask you about the dirty rooms thing,  
[01:32:53] but let's say they build the clean rooms. I have a couple of questions.  
[01:32:58] One, do you think this is the kind of thing that Elon Co. could build much  
[01:33:04] faster than people conventionally build it? This is not about building the end tools.  
[01:33:07] This is just about building the facility itself. How complicated is it to just build  
[01:33:11] the clean room extremely fast? Is this something that Elon, with his "move  
[01:33:15] fast" approach, could do much faster if that's what we're bottlenecked on this year or next year?  
[01:33:19] Two, does that even matter if, in two years, your view is that we're not bottlenecked on  
[01:33:24] clean room space, but on the tooling? As with any complex supply chain,  
[01:33:29] it takes time, and constraints shift over time. Even if something is no longer a constraint, that  
[01:33:33] doesn't mean that market no longer has margin. For example, energy will not be a big bottleneck  
[01:33:40] a couple of years from now, but that doesn't mean energy isn't growing super  
[01:33:43] fast and there's no margin there. It's just not the key bottleneck.  
[01:33:47] In the space of fabs, clean rooms are the biggest bottleneck this year and next year.  
[01:33:52] As we get to 2028, 2029, 2030, there will still be constraints there.  
[01:33:57] The thing about Elon is he has a tremendous capability to garner physical resources and  
[01:34:04] really smart people to build things. The way he recruits amazing people  
[01:34:08] is by trying to build the craziest stuff. In the case of AI, that hasn't really worked  
[01:34:12] because everyone's trying to build AGI. Everyone is very ambitious. But in the case of going to  
[01:34:17] Mars, making rockets that land themselves, fully autonomous electric cars, or humanoid robots,  
[01:34:25] these are methods of recruiting the people who think that's the most important problem in the  
[01:34:28] world to work on that problem, because he's the only one trying really hard.  
[01:34:31] In the case of semiconductors, he stated he wants to make a fab that's a million wafers per month.  
[01:34:35] No one has a fab that big. It's possible that he's able to recruit a  
[01:34:41] lot of really awesome people and get them on this crazy task of building a million wafers a month.  
[01:34:47] Step one is to build the clean room, and that I think he probably can do.  
[01:34:53] His mindset around deleting things, that it can be dirty, it's fine, is probably not right.  
[01:34:58] Actually I think it’s 100% not right. You need the fab to be very clean.  
[01:35:06] All of the air in the fab gets replaced every three seconds, it’s that fast.  
[01:35:11] There have to be so few particles. But I think he can build the clean room.  
[01:35:14] It'll take a year or two. Initially, it won't be super fast,  
[01:35:17] but over time, he'll get faster at it. The really complex part is actually developing  
[01:35:21] a process technology and building wafers. I don't think he can develop that quickly.  
[01:35:26] That has a lot of built-up knowledge. The most complicated integration of  
[01:35:32] very expensive tools and supply chains is done by TSMC, Intel, or Samsung.  
[01:35:39] These two other companies aren't even that great at it, and they're tremendously complex.  
[01:35:43] How surprised would you be if in 2030 there just happened to be some total  
[01:35:48] disruption where we're not using EUV? What if we're using something that has  
[01:35:52] much better effects, is much simpler to produce, and can be produced in much bigger quantities?  
[01:35:56] I'm sure as an industry insider that sounds like a totally naive question,  
[01:35:58] but do you see what I'm asking? What probability should we put on  
[01:36:03] something coming totally out of left field to make all of this irrelevant?  
[01:36:07] Something that's very simple and easy to scale, I assign a very, very low probability.  
[01:36:12] There are a number of companies working on effectively particle  
[01:36:16] accelerators or synchrotrons that generate light that's either 13.5 nanometer, like EUV,  
[01:36:21] or an even narrower wavelength, like X-ray at 7 nanometers, to then use in lithography tools.  
[01:36:29] But those things are massive particle accelerators generating this light.  
[01:36:32] It's a very complicated thing to build. There are a couple of companies and I think  
[01:36:35] that could be a big disruption to the industry beyond EUV.  
[01:36:38] But I don't think we're going to magically build something new that  
[01:36:43] is direct write and super simple, and can be manufactured at huge volumes, although  
[01:36:49] there are some attempts to do things like this. I ask because if you think about Elon's companies  
[01:36:54] in the past, rocketry was this thing that was thought to be—and is—incredibly complicated.  
[01:36:59] Look, I'm just a naive yapper compared to Elon. What have I built? So maybe it's possible.  
[01:37:05] In order to build more memory in the future, could we build 3D DRAM the way  
[01:37:12] we do 3D NAND and then go back to DUV? That is the hope currently. Everyone's  
[01:37:17] roadmap for 3D DRAM is that you'll still use EUV because you want to have that tighter overlay.  
[01:37:24] When you're doing these subsequent processing steps, everything is vertically stacked and you  
[01:37:28] have more layers on top of each other. You want the pitches to be tighter.  
[01:37:33] So generally, people are still trying to do it with EUV.  
[01:37:35] But what 3D would do is change the calculation of how many bits a single EUV pass can make.  
[01:37:42] That number would go up drastically if you go to 3D DRAM. That is the hope. Right now,  
[01:37:47] everyone's roadmap goes from the current 6F cell, to a 4F cell, and then finally 3D DRAM by the end  
[01:37:56] of the decade or early next decade. There's still a lot of R&D,  
[01:38:00] manufacturing, and integration to be done. I wouldn't call that out of the cards.  
[01:38:04] I think it's very likely going to happen. It's also going to require a huge  
[01:38:08] retooling of fabs. The breakdown of  
[01:38:11] tools in a fab will be very different. The lithography tool is actually the  
[01:38:14] only thing that isn't that different. But the number of them relative to different  
[01:38:18] types of chemical vapor deposition, atomic layer deposition, dry etch, or different kinds of etch  
[01:38:25] chambers with different chemistries… You have all these different tools for different process nodes.  
[01:38:31] You can't just convert a logic fab to a DRAM fab, or vice versa, or a NAND fab  
[01:38:35] to a DRAM fab, in a short amount of time. In the same way, existing DRAM fabs require a  
[01:38:41] lot of retooling just to go from 1-alpha to 1-beta to 1-gamma process nodes, because they have to  
[01:38:46] add DUV and change the chemistry stacks for when you’re using EUV in terms of deposition and etch.  
[01:38:51] And the EUV tool has to be there. Furthermore, when you change to 3D DRAM,  
[01:38:55] there's going to be an even larger shift, so a lot of retooling of these fabs needs to happen.  
[01:39:01] That would be a big disruption. That would make EUV demand generally lower.  
[01:39:06] But as we've seen across time, lithography demand as a percentage of wafer cost has trended up.  
[01:39:12] Around the 2014 era, it was 17% of the wafer cost, and it's gone to 30% over the last fifteen years.  
[01:39:24] For DRAM, it was in the low to mid-teens, and now it's trended toward the high teens.  
[01:39:30] Before we get to 3D DRAM, it'll likely cross into the 20% range.  
[01:39:33] But then, if we get to 3D DRAM, the total end wafer cost as a percentage of EUV tanks again.  
[01:39:39] I guess you care less about the percent of cost and more about how much it bottlenecks production.  
[01:39:43] Right, but the percentage of cost— It’s a proxy, yeah. If you're Jensen  
[01:39:50] or Sam Altman, or whoever stands to gain a lot from scaling up AI compute,  
[01:39:56] there are these stories that they'd go to TSMC and say, "Why can't we access Y and Z?"  
[01:40:01] But I think the point you're making is that it doesn't really  
[01:40:06] matter what TSMC does in some sense. In fact, even if you have Intel and  
[01:40:09] Samsung building more foundries, in the long run, you're going to be bottlenecked  
[01:40:13] by ASML and other tool and material makers. First, is that a correct interpretation?  
[01:40:18] Second, should Silicon Valley people be going to the Netherlands right now to try  
[01:40:23] to pitch ASML to make more tools so that in 2030 they can have more AI compute?  
[01:40:30] It's a funny dynamic we saw in 2023, 2024, and 2025.  
[01:40:35] People who saw the energy bottleneck before others asymmetrically went to  
[01:40:40] Siemens, Mitsubishi, and of course GE Vernova, and bought up turbine capacity.  
[01:40:45] Now they're able to charge excess amounts for deploying  
[01:40:47] these turbines in places because of energy. In the same sense, this could be done for EUV,  
[01:40:52] except ASML is not just going to trust any random bozo who wants to buy EUV tools.  
[01:41:00] These turbines are much cheaper than EUV tools, and there's many more of them produced.  
[01:41:04] Especially once you get to industrial gas turbines, not just combined-cycle but the cheaper,  
[01:41:10] smaller, less efficient ones, people put down deposits for these. Someone could  
[01:41:15] do this. Someone should go to the Netherlands and be like, "I'll pay you a billion dollars.  
[01:41:21] You give me the right to purchase ten EUV tools two years from now, and I'm first in line."  
[01:41:30] Then over those two years, you go around and wait for everyone to realize, "Oh crap,  
[01:41:34] I don't have enough EUV tools," and you try to sell your option at some premium.  
[01:41:38] All you're effectively doing is saying, "ASML, you're dumb.  
[01:41:41] You weren't making enough margin on these. I'm going to make a margin."  
[01:41:44] The question is, will ASML even agree to this? I don't think so.  
[01:41:49] There's a world where they at least get the demand signal from that to increase production.  
[01:41:53] Potentially. I agree. But it sounds like you're  
[01:41:56] saying they couldn't even increase production if they wanted to, given the supply chain.  
[01:41:59] Right. But that's exactly the market in which… If they can't increase production,  
[01:42:02] just like TSMC cannot increase production that fast, and yet demand is mooning,  
[01:42:06] then the obvious solution is to arbitrage this. You and I know demand is way higher than they're  
[01:42:12] projecting and their capability to build. You arbitrage this by locking up the capacity,  
[01:42:17] doing a forward contract, and then trying to sell it at a later date  
[01:42:21] once other people realize everything is fucked and we don't have enough capacity.  
[01:42:26] Then you'll have this insane margin that ASML and TSMC should have been charging.  
[01:42:30] But the thing is, I don't know if ASML and TSMC will ever agree to this.  
[01:42:34] Let me ask you about power now. It sounds like you think power  
[01:42:37] can be arbitrarily scaled. Not arbitrarily, but yes.  
[01:42:41] But beyond these numbers. If I'm remembering correctly, your blog post on  
[01:42:47] how AI labs are increasing power implied that GE Vernova, Mitsubishi, and Siemens could  
[01:42:54] produce 60 gigawatts a year in gas turbines. Then there are these other sources,  
[01:42:59] but they're less significant than the turbines. Only a fraction of that goes to AI, I assume.  
[01:43:10] If in 2030 we have enough logic and memory to do 200 gigawatts a year, do you just think that  
[01:43:15] these things are on a path to ramp up to more than 200 gigawatts a year, or what do you see?  
[01:43:20] Right now we're at 20 or 30. This is critical IT capacity, by the way,  
[01:43:26] which is an important thing to mention. When I'm talking about these gigawatts,  
[01:43:29] I'm talking about critical IT capacity. Server plugged in, that's how much power it pulls.  
[01:43:32] But there are losses along the chain. There is loss on transmission,  
[01:43:37] conversion, cooling, et cetera. So you should gross this factor  
[01:43:43] up from 20 gigawatts for this year, or 200 gigawatts by the end of the decade, to some  
[01:43:49] number 20-30% higher. Then you have capacity factors. Turbines don't run at 100 percent.  
[01:43:54] If you look at PJM, which I think is the largest grid in America—covering the Midwest and some of  
[01:43:59] the Northeast area—in their models they want to have roughly 20 percent excess capacity.  
[01:44:12] Within that 20 percent excess capacity, they're running all the turbines at 90%  
[01:44:16] because they are derated some for reliability, maintenance, and so on.  
[01:44:22] In reality, the nameplate capacity for energy is always way higher than the actual end critical IT  
[01:44:26] capacity because of all these factors. But it's not just turbines. If you were just making power  
[01:44:32] from turbines, that's simple, boring, and easy. Humans and capitalism are far more effective.  
[01:44:41] The whole point of that blog was that, yes, there are only three people making combined-cycle gas  
[01:44:45] turbines, but there's so much more we can do. We can do aeroderivatives. We can take  
[01:44:49] airplane engines and turn them into turbines. There are even new entrants in the market,  
[01:44:55] like Boom Supersonic trying to do that and working with Crusoe.  
[01:44:58] Also there's all the other ones like that already exist in the market.  
[01:45:00] There are also medium-speed reciprocating engines: engines  
[01:45:04] that spin in circles, like a diesel engine. There are ten people who make engines that way.  
[01:45:13] I'm from Georgia, and people used to be like, "Oh man, you got a  
[01:45:15] Cummins engine in there," regarding RAM trucks. Automobile manufacturing is going down, so these  
[01:45:22] companies all have capacity and could scale and convert that for data center power.  
[01:45:26] You stick all these reciprocating engines in. It's not as clean as combined-cycle, but maybe you  
[01:45:31] can convert them from diesel to gas if you want. What about ship engines? All of these engines for  
[01:45:38] massive cargo ships are great. Nebius is doing that for  
[01:45:41] a Microsoft data center in New Jersey. They're running ship engines to generate power.  
[01:45:49] Bloom Energy is doing fuel cells. We've been very positive on them for  
[01:45:52] a year and a half now because they have such a capability to increase their production.  
[01:45:57] Their payback period for a production increase is very fast, even if the cost  
[01:46:01] is a little bit higher than combined-cycle, which is the best for cost and efficiency.  
[01:46:06] Then there's solar plus battery, which can come online as those cost curves continue to come down.  
[01:46:11] There's wind, where you might only expect 15 percent of the maximum power because things  
[01:46:18] oscillate, but you add batteries. There are all these things. The other thing is that the  
[01:46:23] grid is scaled so we don't cut off power at peak usage on the hottest day of the summer.  
[01:46:32] But in reality, that's a load spike that is 10-20% higher than the average.  
[01:46:37] If you just put enough utility-scale batteries, or peaker plants that only  
[01:46:41] run a small portion of the year—and those could be gas, industrial gas turbines, combined-cycle,  
[01:46:49] batteries, or any of the other sources I mentioned—then all of a sudden you've  
[01:46:54] unlocked 20% of the US grid for data centers. Most of the time that capacity is sitting idle.  
[01:47:00] It's really only there for that peak, which is just a few hours over a few days of the year.  
[01:47:07] If you have enough capacity to absorb that peak load,  
[01:47:11] then all of the sudden you’ve transferred it all. Today, data centers are only 3-4% of the power of  
[01:47:15] the US grid, and by 2028 they'll be 10%. But if you can unlock 20% of the US grid  
[01:47:20] like this, it's not that crazy. The US grid is terawatt-level,  
[01:47:25] not hundreds-of-gigawatts-level. So we can add a lot more energy. I'm not saying  
[01:47:33] it's easy. These things are going to be hard. There's a lot of hard engineering,  
[01:47:36] risks people have to take, and new technologies people have to use.  
[01:47:40] But Elon was the first to do this behind-the-meter gas, and since then we've seen an explosion of  
[01:47:45] different things people are doing to get power. They're not easy,  
[01:47:50] but people are gonna be able to do them. The supply chains are just way simpler than chips.  
[01:47:56] Interesting. He made the point during the interview that for the specific blade for  
[01:48:00] the specific turbine he was looking at, the lead times go out beyond 2030. Your point is that—  
[01:48:06] That's great. There are so many other ways to make energy. Just be inefficient. It's fine.  
[01:48:10] Right now, combined-cycle gas turbines have CapEx of $1,500 per kilowatt.  
[01:48:17] Are you saying it would make sense to have either technologies that are much  
[01:48:20] more expensive than that, or other things are getting cheap enough to make it competitive?  
[01:48:24] Exactly. It can be as high as $3,500 per kilowatt. It could be twice as much as the cost of  
[01:48:31] combined-cycle, and the total cost of the GPU on a TCO basis has only gone up a few cents per hour.  
[01:48:40] Because we've been talking about Hopper pricing, $1.40, let's say the power price doubles.  
[01:48:46] The Hopper that was $1.40 is now $1.50 in cost. I don't care, because the models are improving so  
[01:48:54] fast that the marginal utility of them is worth way more than that ten-cent increase in energy.  
[01:49:00] So you're saying 20 percent of the grid—the grid is about one terawatt—can just come online from  
[01:49:06] utility-scale batteries, increasing what you'd be comfortable putting on the grid.  
[01:49:11] The regulatory mechanism there is not easy, by the way.  
[01:49:13] But that's 200 gigawatts, if that hypothetically happens.  
[01:49:18] Just from the different sources of gas generation you mentioned—the different kinds of engines  
[01:49:22] and turbines—combined, how many gigawatts could they unlock by the end of the decade?  
[01:49:28] We're tracking this in our data. There are over 16 different manufacturers  
[01:49:33] of power-generating things just from gas alone. Yes, there are only three turbine manufacturers  
[01:49:39] for combined-cycle, but we're tracking 16 different vendors,  
[01:49:43] and we have all of their orders. It turns out there are hundreds of  
[01:49:47] gigawatts of orders to various data centers. As we get to the end of the decade,  
[01:49:51] we think something like half of the capacity that's being added will be behind the meter.  
[01:49:59] Behind the meter is almost always more expensive than grid-connected, but there are just a lot of  
[01:50:03] problems with getting grid-connected: permits and interconnection queues and all this sort of stuff.  
[01:50:08] So even though it's more expensive, people are doing behind the meter.  
[01:50:12] What they're doing behind the meter ranges widely. It could be reciprocating engines, ship engines,  
[01:50:17] or aeroderivatives. It could be combined-cycle,  
[01:50:19] although combined-cycle is not that great for behind the meter.  
[01:50:22] It could be Bloom Energy fuel cells, or solar plus battery.  
[01:50:26] It could be any of these things. And you're saying any of these  
[01:50:29] individually could do tens of gigawatts? Any of these individually will do tens of  
[01:50:34] gigawatts, and as a whole, they will do hundreds of gigawatts.  
[01:50:36] Okay. So that alone should more than— Electrician wages will probably  
[01:50:42] double or triple again. There are going to be a lot of new people entering  
[01:50:45] that field, and a ton of people who make money, but I don't see that as the main bottleneck.  
[01:50:51] Right now in Abilene, at the 1.2-gigawatt data center that Crusoe is building for OpenAI,  
[01:50:59] I think they have 5,000 people working there, or at peak they did.  
[01:51:04] If you turn that into 100 gigawatts—and I'm sure things will get more efficient  
[01:51:10] over time—that would be 400,000 people it would take to build 100 gigawatts.  
[01:51:16] If you think about the US labor force, and how many electricians there are and how  
[01:51:20] many construction workers there are… I guess there are 800,000 electricians.  
[01:51:24] I don't know if they're all substitutable in this way.  
[01:51:26] There are millions of construction workers. But if we're in a world where we're adding  
[01:51:30] 200 gigawatts a year, are we going to be crunched on labor eventually, or do you  
[01:51:35] think that is actually not a real constraint? Labor is a big constraint. It's a humongous  
[01:51:38] constraint in this. People have to be trained. Likewise, we'll probably  
[01:51:43] start importing the highest-skilled labor. It makes sense that a really high-skilled  
[01:51:50] electrician in Europe who was working on destroying power plants now comes  
[01:51:55] to America and is building high-voltage electricity moving across a data center.  
[01:52:03] Humanoid robots or robotics at least might start to help, but the main factor for reducing the  
[01:52:09] number of people is going to be modularizing things and making them in factories in Asia.  
[01:52:13] Unfortunately for America, places like Korea, Southeast Asia, and in many ways China as well  
[01:52:24] are going to ship more and more built-out sections of the data center and those will be shipped in.  
[01:52:34] Today you currently ship servers or a rack in, and then you plug that into different pieces that  
[01:52:40] you're shipping from different places. But now you'll ship it to a factory  
[01:52:43] and integrate the entire thing. Maybe this is a two-megawatt block,  
[01:52:48] and this block goes from high-voltage AC power to the DC voltage that you deliver  
[01:52:56] to the rack, or something like this. Or with cooling, you ship a fully  
[01:53:03] integrated unit that has a lot of the cooling subsystems already put together,  
[01:53:08] because plumbers are also a big constraint here. Furthermore, instead of just a single rack where  
[01:53:13] you have people wiring up all these racks with electricity, you take a skid and put an entire  
[01:53:19] row of servers on it that is shipped directly from the factories.  
[01:53:25] Today, a single rack may be 120 or 140 kilowatts, but as we get to next-generation Nvidia Kyber and  
[01:53:32] things like that, it's almost a megawatt. In addition, if you do an entire  
[01:53:36] row, it'll have the rack, the networking, the cooling, and the power all integrated together.  
[01:53:42] Now when you come in, you have much less to cable. There's less networking fiber, fewer power  
[01:53:53] connections, and fewer plumbing things. This can drastically reduce the number  
[01:53:58] of people working in data centers, so our capability to build them will be much larger.  
[01:54:03] Along the way, some people will move faster to new things, and some will move slower.  
[01:54:08] Crusoe and Google have been talking a lot about this modularization,  
[01:54:12] as have companies like Meta and many others. The people who move faster to new things may  
[01:54:24] face delays, while the people who are slower will face labor problems.  
[01:54:27] There will always be dislocations in the market because this is a very complex supply chain.  
[01:54:30] At the end of the day, it's still simple enough that we will be able  
[01:54:33] to solve it through capitalism and human ingenuity on the timescales required.  
[01:54:39] Speaking of big problems to solve, Elon Musk is very bullish on space GPUs.  
[01:54:46] If you're right that power is not a constraint on Earth… I guess the other reason they would  
[01:54:50] make sense is that even if there will be enough gas turbines or whatever on Earth,  
[01:54:55] Elon's next argument is that you can't get the permitting to build hundreds of gigawatts on  
[01:55:00] Earth. Do you buy that argument? Land-wise, America is big. Data  
[01:55:05] centers don't actually take up that much space, so you can solve that.  
[01:55:09] Permitting-wise, air pollution permits are a challenge, but the Trump administration  
[01:55:12] made it much easier. You go to Texas,  
[01:55:15] and you can skip a lot of this red tape. Elon had to deal with a lot of this complex  
[01:55:22] stuff in Memphis, and then building a power plant across the border for Colossus 1 and 2.  
[01:55:28] But at the end of the day, there's a lot more you can get away with in the middle of Texas.  
[01:55:32] Given that Elon lives in Texas, why didn't he just go to Texas?  
[01:55:34] I think it was partially that they over-indexed on grid power for a temporary period of time.  
[01:55:40] That's just what they thought they needed more of. Because they had an aluminum refinery  
[01:55:43] connected to the grid there. It was actually an idled appliance factory.  
[01:55:50] But I think they may have indexed more to grid power, water access, and gas access.  
[01:55:56] I think they bought that knowing the gas line was right there and they were going  
[01:55:59] to tap it. Same with water. It was a whole host of different constraints.  
[01:56:03] It was probably an area where electricians were easier to find.  
[01:56:07] At the end of the day, I'm not exactly sure why they chose that site.  
[01:56:10] I bet Elon would've chosen somewhere in Texas if he could've gone back because  
[01:56:16] of the regulatory challenges he faced. Ultimately, permitting is a challenge,  
[01:56:23] but America is a big place with 50 states, and things will get done.  
[01:56:27] There are a lot of small jurisdictions where you can just transport in all the workers  
[01:56:32] you need for a temporary period of three to twelve months, depending on the contractor.  
[01:56:37] You can put them in temporary housing and pay out the butt, because labor is very cheap relative  
[01:56:44] to the GPUs and the networking, and the end value of the tokens it's going to produce.  
[01:56:52] So there is plenty of room to pay for all of these things.  
[01:56:59] Also, people are also diversifying now. Australia, Malaysia, Indonesia, and India  
[01:57:06] are all places where data centers are going up at a much faster pace.  
[01:57:09] But currently, over 70% of AI data centers are still in America,  
[01:57:12] and that continues to be the trend. People are figuring out how to build these things.  
[01:57:19] Ultimately, dealing with permitting and red tape in middle-of-nowhere Texas,  
[01:57:23] Wyoming, or New Mexico is probably a hell of a lot easier than sending stuff into space.  
[01:57:30] Other than the economic argument making less sense once you consider that energy is a small fraction  
[01:57:36] of the total cost of ownership of a data center, what are the other reasons you're skeptical?  
[01:57:41] Obviously, power is basically free in space. That's the reason to do it.  
[01:57:45] Yeah, that's the reason to do it. But there are all the other counterarguments.  
[01:57:50] Even if power costs double on Earth, it's still a fraction of the total cost of the GPU.  
[01:57:54] The main challenge is… We have ClusterMAX, which rates all the neoclouds.  
[01:58:03] We test over 40 cloud companies, including the hyperscalers and neoclouds.  
[01:58:06] Outside of software, what differentiates these clouds the most is their ability to deploy and  
[01:58:11] manage failure. GPUs are horrendously unreliable. Even today, around 15% of Blackwells that get  
[01:58:19] deployed have to be RMA'd. You have to take them out.  
[01:58:21] Sometimes you just have to plug them back in, but sometimes you have to take  
[01:58:23] them out and ship them back to Nvidia or their partners who do the RMAs and such.  
[01:58:28] What do you make of Elon's argument that after an initial phase, they actually don't fail that much?  
[01:58:34] Sure, but now you've done this, tested them all, deconstructed them, put them on a spaceship,  
[01:58:39] launched them into space, and then put them online again. That takes months. If  
[01:58:44] your argument is that a GPU has a useful life of five years, and this takes six additional months,  
[01:58:57] that is 10% of your cluster's useful life. Because we're so capacity-constrained,  
[01:59:04] that compute is theoretically most valuable in the first six months you have it.  
[01:59:08] We're more constrained now than we will be in the future.  
[01:59:11] That compute can contribute to a better model in the future, or generate revenue  
[01:59:15] today that you can use to raise more money. All these things make now the most important  
[01:59:20] moment, but you've potentially delayed your compute deployment by six months.  
[01:59:25] What separates these cloud providers is… We see some clouds taking six months to deploy  
[01:59:28] GPUs right here on Earth. We see clouds that take  
[01:59:31] a lot less than six months. So the question is, where does space get in there?  
[01:59:36] I don't see how you could test them all on Earth, deconstruct them, and ship them to space without  
[01:59:41] it taking significantly longer than just leaving them in the facility where you tested them.  
[01:59:45] The question I wanted to ask is about the topology of space communication.  
[01:59:50] Right now, Starlink satellites talk to each other at 100 gigabits per second.  
[01:59:56] You could imagine that being much higher with optical intersatellite  
[02:00:00] laser links optimized for this. That actually ends up being quite  
[02:00:04] close to InfiniBand bandwidth, which is 400 gigabytes a second.  
[02:00:09] But that's per GPU, not per rack. So multiply that by 72. Also, that was Hopper. When you go  
[02:00:16] to Blackwell and Rubin, that 2x's and 2x's again. But how much compute is happening per… During  
[02:00:24] inference, are the different scale-ups still working together, or is inference just  
[02:00:27] happening as a batch within a single scale-up? A lot of models fit within one scale-up domain,  
[02:00:33] but many times you split them across multiple scale-up domains.  
[02:00:42] As models become more and more sparse, which is the general trend, you want to  
[02:00:48] ping just a couple of experts per GPU. If leading models today have hundreds,  
[02:00:53] if not a thousand, of experts, then you'd want to run this across hundreds or thousands of chips,  
[02:00:59] even as we advance into the future. So then you end up with the problem of  
[02:01:05] needing to connect all these satellites together for communications as well.  
[02:01:09] That would be tough. If there's a world where you could do inference for a batch on a single  
[02:01:17] scale-up, then maybe it's more plausible. But if not, it's a different story.  
[02:01:21] Networking these chips together is a problem, and you can't just  
[02:01:24] make the satellite infinitely large. There are a lot of physics challenges to  
[02:01:29] making a satellite really big. That's why you need these  
[02:01:34] interconnects between the satellites. Those interconnects are more expensive. In a cluster,  
[02:01:38] 15-20% of the cost is networking. All of a sudden, you're using space lasers  
[02:01:43] instead of simple lasers that are manufactured in volumes of millions with pluggable transceivers.  
[02:01:50] And those things are very unreliable as well, more unreliable than the GPUs by the way.  
[02:01:54] Across the life of a cluster, you have to unplug and clean them all the time.  
[02:01:57] You have to unplug and replug them just for random reasons.  
[02:01:59] These things are just not as reliable. So you've got that problem as well.  
[02:02:03] You've got a more expensive, complicated space laser to communicate instead of this  
[02:02:08] pluggable optical transceiver that's been produced in super high volume.  
[02:02:11] So all in all, what does that imply for space data centers?  
[02:02:13] Space data centers effectively are not limited by their energy advantage.  
[02:02:19] They are limited by the same contended resource. We can only make two hundred gigawatts  
[02:02:24] of chips a year by the end of the decade. What are we going to do to get that capacity?  
[02:02:29] It doesn't matter if it's on land or in space. It doesn’t really matter,  
[02:02:36] because you can build that power. Human capabilities and capacity could get  
[02:02:41] to the period where we're adding a terawatt a year globally of various types of power.  
[02:02:47] At some point, we do cross the chasm where space data centers make sense, but it's not this decade.  
[02:02:52] It is much further out, once energy constraints actually become a big bottleneck  
[02:02:59] and land permitting becomes a much bigger bottleneck as it subsumes more of the economy.  
[02:03:04] And crucially, once chips are no longer the bottleneck.  
[02:03:07] Right now, chips are the biggest bottleneck. You want them deployed and working on  
[02:03:11] AI the moment they're manufactured. There are a lot of things people are  
[02:03:15] doing to increase that speed faster and faster. They’re modularizing data centers, or even  
[02:03:20] modularizing racks where you put the chip in at the data center, but only the chip and everything  
[02:03:26] else is already wired up and ready to go. There are things like this people are doing to  
[02:03:31] decrease that time that you cannot do in space. At the end of the day, all that matters in a  
[02:03:36] chip-constrained world is getting these chips producing tokens ASAP.  
[02:03:43] Maybe by 2035, the semiconductor industry, ASML, Zeiss, and suppliers like Lam  
[02:03:45] Research and Applied Materials and other fab manufacturers will catch up once the pendulum  
[02:03:53] swings and we are able to make enough chips. Then we will be optimizing every dial and it makes  
[02:03:58] sense to optimize the 10-15% of energy costs. As we move to ASICs potentially,  
[02:04:03] and if Nvidia's margins aren't +70%, maybe that energy cost becomes 30% of the cluster.  
[02:04:11] These are the things to optimize. But Elon doesn't win by doing 20% gains. He  
[02:04:18] never wins that way. Elon wins when he swings for the fences and does 10X gains. That's what SpaceX  
[02:04:24] is about. That's what Tesla is about. All of his success has been about that, not chasing the 20%.  
[02:04:31] I think space data centers will eventually be a 10X gain as Earth's resources get more  
[02:04:37] and more contentious, but that's not this decade. Just to drive some intuition about how much land  
[02:04:42] there is on Earth… Obviously, for the chips themselves, especially if you move to a world  
[02:04:46] where you have racks that have megawatts— That's the other thing. If manufacturing is  
[02:04:55] the constraint, right now it's roughly one watt per square millimeter for AI chips.  
[02:05:01] One easy way to improve that is to pump it to two watts per square millimeter.  
[02:05:05] You may not get 2x the performance, you may only get 20% more performance,  
[02:05:09] and that requires much more exotic cooling. It requires more complicated cold plates  
[02:05:13] and complex liquid cooling, or maybe even things like immersion cooling.  
[02:05:18] In space, higher watts per millimeter is very difficult,  
[02:05:20] whereas on Earth, these are solved problems. One of these things enables you to get a lot  
[02:05:25] more tokens, maybe 20% more tokens per wafer that's manufactured, and that's a humongous win.  
[02:05:31] Square millimeter, you mean of die area? Yeah, of die area.  
[02:05:36] It would be better for space because more watts per millimeter means the chip runs hotter.  
[02:05:42] I guess this is a question of computer chip engineering, but it cools to the  
[02:05:46] fourth power by the Stefan-Boltzmann law. If you can run a very hot  
[02:05:49] chip, it allows a lot of— No, you can't run it hotter.  
[02:05:51] You can only run it denser. The problem is that getting  
[02:05:54] the heat out of that dense area means you have to move away from standard air and liquid cooling to  
[02:06:00] more exotic forms of liquid cooling, or even immersion, to get to higher power densities.  
[02:06:05] That's more difficult in space than it is on Earth.  
[02:06:08] Maybe it's worth explaining at this point what exactly a scale-up is and what it looks like for  
[02:06:13] Nvidia versus Trainium versus TPUs. Earlier I was mentioning how  
[02:06:22] communication within a chip is super fast. Communication within chips that are in the  
[02:06:26] same rack is fast, but not as fast. It's on the order of terabytes.  
[02:06:30] Communication very far away is on the order of hundreds of gigabytes.  
[02:06:36] As you get further distance, maybe across the country, the order  
[02:06:39] of magnitude is on the order of gigabytes. A scale-up domain is this tight domain  
[02:06:44] where the chips are communicating on the order of terabytes a second.  
[02:06:50] For Nvidia, previously this meant an H100 server had eight GPUs,  
[02:06:55] and those eight GPUs could talk to each other at terabytes a second.  
[02:06:58] With Blackwell NVL72, they implemented rack-scale scale-up.  
[02:07:03] That meant all seventy-two GPUs in the rack could connect to each other at terabytes a second.  
[02:07:09] The speed doubled generation on generation, but the most important innovation was going from eight  
[02:07:13] to seventy-two in the domain. When we look at Google,  
[02:07:16] their scale-up domain is completely different. It has always been on the order of thousands.  
[02:07:20] With TPU v4, they had pods the size of four thousand chips.  
[02:07:23] With v8 or v7, they have pods in the eight or nine thousand range.  
[02:07:31] What's relevant here is that it's not the same as Nvidia. It's not like for like.  
[02:07:35] Google has a topology that's a torus. Every chip connects to six neighbors.  
[02:07:40] Nvidia's 72 GPUs connect all-to-all. They can send terabytes a second to  
[02:07:46] any arbitrary other chip in that pod of scale-up. Whereas Google, you have to bounce through chips.  
[02:07:52] If TPU 1 needs to talk to TPU 76, it has to bounce through various chips, and there is always some  
[02:07:59] blocking of resources when you do that because that one TPU is only connected to six other TPUs.  
[02:08:04] So there is a difference in topology and bandwidth,  
[02:08:07] and there are trade-offs and advantages to both. Google gets to have a massive scale-up domain,  
[02:08:11] but they have the trade-off of bouncing across chips to get from one to another.  
[02:08:15] You can only talk to six direct neighbors. Amazon has mutated their scale-up domain.  
[02:08:23] They're somewhere in between Nvidia and Google. They're trying to make larger scale-up domains.  
[02:08:28] They try to do all-to-all to some extent with switches, which is what Nvidia does, but they also  
[02:08:33] use torus topologies like Google to some extent. As we advance forward to next generations,  
[02:08:40] all three of them are moving more towards a dragonfly topology.  
[02:08:44] That means there are some fully connected elements and some elements that are not fully connected.  
[02:08:49] You can get the scale-up to be hundreds or thousands of chips, but also have it not contend  
[02:08:54] for resources when bouncing through chips. Related question: I heard somebody make the  
[02:09:00] claim that the reason parameter scaling has been slow—and only now are we getting bigger models  
[02:09:08] from OpenAI and Anthropic—is that… The original GPT-4 is over a trillion parameters, and only now  
[02:09:18] are models starting to approach that again. I heard a theory that the reason is that  
[02:09:24] Nvidia's scale-ups have just not had that much memory capacity.  
[02:09:37] Let's say you have a 5T model running at FP8, so that's five trillion gigabytes.  
[02:09:43] And then you have the KV cache, let's say it's— Just call it the same size.  
[02:09:47] Okay, let's say it's the same size for one batch. So you need ten terabytes to be able to run…  
[02:09:54] A single forward pass, yeah. And then only with the GB200 and NVL72  
[02:09:59] do you have an Nvidia scale-up that has twenty terabytes, and before that they were much smaller.  
[02:10:03] Whereas Google, on the other hand, has had these huge TPU pods that are not all-to-all,  
[02:10:09] but still have hundreds of terabytes of capacity in a single scale-up.  
[02:10:13] Does that explain why parameter scaling has been slow?  
[02:10:16] I think it's partially the capacity and bandwidth, but also as you build a larger  
[02:10:22] model, the ability to deploy it is slower. In terms of what the inference speed is for  
[02:10:28] the end user, that's kind of irrelevant. What's really relevant is RL. What we've seen with these  
[02:10:33] models and allocation of compute at a lab… There are a few main ways you can allocate compute.  
[02:10:38] You can allocate it to inference, i.e. revenue. You can allocate it to development,  
[02:10:42] i.e. making the next model. You can allocate it to research.  
[02:10:46] In development specifically, you split it between pre-training and RL.  
[02:10:52] When you think about what is happening, the compute efficiency gains you get from research  
[02:10:58] are so large that you actually want most of your compute to go to research, not to development.  
[02:11:04] All these researchers are generating new ideas, trying them out, testing them,  
[02:11:08] and continuing to push the Pareto optimal curve of scaling laws further and further.  
[02:11:14] Empirically, what we’ve seen is that model costs get ten times cheaper  
[02:11:17] every year, or even more than that. At the same scale it gets ten times cheaper,  
[02:11:23] and to reach new frontiers it costs the same amount or more.  
[02:11:27] So you don't want to allocate too many resources to pre-training and RL.  
[02:11:33] You actually want to allocate most of your resources to research.  
[02:11:36] In the middle is this development period. If you pre-train a five-trillion-parameter model,  
[02:11:45] how many rollouts do you have to do in RL? Rollouts for a five-trillion-parameter model  
[02:11:51] are five times larger than for a one-trillion-parameter model.  
[02:11:54] If you wanted to do as many rollouts—maybe the larger model is two times more sample  
[02:11:57] efficient—now you need 2.5x as much time of RL to get the model smarter.  
[02:12:05] Or you could RL the smaller model for 2x the time. You'd still have a 25% difference in the big  
[02:12:12] model, which is 2x as sample efficient and doing X number of rollouts.  
[02:12:16] But the smaller model, which is a trillion parameters, although its  
[02:12:19] less sample efficient, is doing twice as many rollouts and is still done faster.  
[02:12:23] You get the model sooner, you've done more RL, and then you can take that model to help you  
[02:12:28] build the next models, help your engineers train, and do all these research ideas.  
[02:12:33] This feedback loop is actually weighed towards smaller models in every case,  
[02:12:39] no matter what your hardware is. As you look to Google, they do  
[02:12:42] deploy the largest production model of any of the major labs with Gemini Pro.  
[02:12:49] It's a larger model than GPT-5.4. It's a larger model than Opus.  
[02:12:55] Google does this because they have a unipolar set of compute. It's almost all TPU. Whereas Anthropic  
[02:13:04] is dealing with H100s, H200s, Blackwell, Trainiums, and TPUs of various generations.  
[02:13:12] OpenAI is dealing with mostly Nvidia right now, but going towards having AMD and Trainium as well.  
[02:13:18] The fleets of compute like Google's can just optimize around a larger model.  
[02:13:23] They can leverage a thousand chips in a scale-up domain to get the RL time speed much faster  
[02:13:30] so that this feedback loop can be fast. But at the end of the day, in isolation,  
[02:13:36] you almost always want to go with a smaller model that gets RL'd faster and gets deployed  
[02:13:41] into research and development earlier. You can build the next thing and  
[02:13:44] get more efficiency wins. You have this compounding  
[02:13:47] effect of making a smaller model that can be deployed into research and development earlier.  
[02:13:53] I spend less compute on the training because I was able to allocate more compute to the research.  
[02:13:58] This compounding effect of being able to do research faster and faster is  
[02:14:01] potentially a faster takeoff. That's all these companies want:  
[02:14:03] the fastest takeoff possible. Okay, a spicy question. You've explained  
[02:14:10] that SemiAnalysis sells these spreadsheets. You're always pointing out how six  
[02:14:14] months or a year ago, you warned people about the memory crunch.  
[02:14:17] Now you're telling people about the cleanroom crunch, and in the future, the tool crunch.  
[02:14:22] Why is Leopold the only person using your spreadsheets to make outrageous money? What  
[02:14:27] is everybody else doing? I think there are a lot  
[02:14:30] of people making money in many ways. Leopold jokes that he's the only client  
[02:14:38] of mine who tells me our numbers are too low. Everyone else tells me our numbers are too high,  
[02:14:42] almost ad nauseam. Whether it's a hyperscaler saying,  
[02:14:46] "Hey, that other hyperscaler, their numbers are too high," and we're like, "Nah, that's it."  
[02:14:50] They're like, "No, no, no, it's impossible," blah, blah, blah.  
[02:14:52] You finally have to convince them through all these facts and data when we're working with  
[02:14:55] hyperscalers or AI labs that in fact, no, that number isn't too high, that's correct.  
[02:15:00] Eventually, sometimes it takes them six months to realize, or a year later.  
[02:15:05] Other clients, on the trading side, also use our data.  
[02:15:12] Roughly 60% of my business is industry. So AI labs, data center companies,  
[02:15:17] hyperscalers, semiconductor companies, the whole supply chain across AI infrastructure.  
[02:15:23] But 40% of our revenue is hedge funds. I'm not going to comment on who our customers are,  
[02:15:28] but a lot of people use the data. It's just how do you interpret it,  
[02:15:33] and then what do you view as beyond it? I will say Leopold is pretty much the only person  
[02:15:39] who tells me my numbers are too low, always. Sometimes he's too high, sometimes I'm too low.  
[02:15:44] But in general, I think other people are doing that.  
[02:15:50] You can look across the space at hedge funds and look at their 13Fs and see they own, maybe not  
[02:15:56] exactly what Leopold does, because it's always a question of what is the most constrained thing.  
[02:16:00] What's the thing that's going to be most outside of expectations?  
[02:16:03] That's what you're really trying to exploit: inefficiencies in the market.  
[02:16:06] In a sense, our data is making the market more efficient by making the base data  
[02:16:12] of what's happening more accurate. Many funds do trade on information  
[02:16:22] that is out there… I don't think Leopold's the only person.  
[02:16:26] I think he has the most conviction about the AGI takeoff, though.  
[02:16:32] Right, but the bets are not about what happens in 2035.  
[02:16:37] The bets that you're making—that are at least exemplified by public returns we can see for  
[02:16:41] different funds including Leopold's—are about what has happened in the last year.  
[02:16:45] The last year stuff could be predicted using your spreadsheets.  
[02:16:50] It's about buying the next year's spreadsheets. They're not just spreadsheets. There are  
[02:16:53] reports. There's API access to the data. There's a lot of data.  
[02:16:56] But do you see what I mean? It's not about some crazy singularity thing.  
[02:17:00] It's about, do you buy the memory crunch? You only buy the memory crunch if you  
[02:17:05] believe AI is going to take off in a huge way. The memory crunch, a lot of it was predicated  
[02:17:12] on… At least for people in the Bay Area who think about infrastructure, it's obvious.  
[02:17:17] KV cache explodes as context lengths get longer, so you need more memory. Then you do the math.  
[02:17:22] You also have to have a lot of supply chain understanding of what fabs are being built,  
[02:17:25] what data centers are being built, how many chips, and all these things.  
[02:17:28] We track all these different datasets very tightly, but at the end of the day,  
[02:17:32] it takes someone to fully believe that this is going to happen.  
[02:17:38] A year ago, if you told someone memory prices would quadruple and smartphone  
[02:17:42] volumes are going to go down 40% over the year or two after that, people were like,  
[02:17:48] "You're crazy. That'd never happen." Except a few people do believe that, and those people did trade  
[02:17:52] memory. And people did. I don't think Leopold was the only person buying memory companies.  
[02:18:00] He, of course, sized and positioned and did things in better ways than some, maybe most.  
[02:18:06] I don't want to comment on whose returns are what, but he certainly did well.  
[02:18:12] Other people also did really well. Wow, you've made me diplomatic for  
[02:18:18] the first time ever. No, no, you're fine. I think this is hilarious. I'm being a  
[02:18:22] diplomat, whereas usually I'm spicy. Okay, some rapidfire to close out.  
[02:18:31] If you're saying with the memory, logic, et cetera, the N3 is mostly  
[02:18:38] going to be AI accelerators, but then there's N2, which is mostly Apple now… In the future,  
[02:18:44] I guess AI would also want to go on N2. Can TSMC kick out Apple if Nvidia and  
[02:18:53] Amazon and Google say, "Hey, we're willing to pay a lot of money for N2 capacity?"  
[02:18:59] I think the challenge with this is chip design timelines take a long while, so that's more  
[02:19:04] than a year out, and the designs that are on two nanometer are more than a year out.  
[02:19:08] What would really happen is Nvidia and all these others will be like, "Hey,  
[02:19:12] we're going to prepay for the capacity and you're going to expand it for us."  
[02:19:17] Maybe TSMC takes a little bit of margin, but not a ton.  
[02:19:21] They're not going to kick Apple out entirely. What they're going to do is when Apple orders X,  
[02:19:25] they might say, "Hey, we project you only need X minus one, and so that's what we're going to  
[02:19:29] give you, X minus one." Then that flex capacity,  
[02:19:31] Apple's kind of screwed on. Traditionally, Apple has always  
[02:19:35] over-ordered by 10% and cut back by 10% over the course of the year.  
[02:19:38] Some years they hit the entire 10%. Volumes vary based on the season and macro.  
[02:19:47] I don't think TSMC would kick out Apple. I think Apple will become a smaller and smaller  
[02:19:52] percentage of TSMC's revenue, and therefore be less relevant for TSMC to cater to their demands.  
[02:19:57] TSMC could eventually start saying, "Hey, you've got to pre-book your capacity for next year,  
[02:20:01] for two years out, and you have to prepay for the CapEx," because that's what Nvidia and  
[02:20:05] Amazon and Google are doing. I wonder if it's worth  
[02:20:08] going into specific numbers. I don't have any of them on hand.  
[02:20:15] What percentage of N2 does Apple have its hands on over the coming years versus AI?  
[02:20:22] This year Apple has the majority of N2 that's going to get fabricated.  
[02:20:26] There's a little bit from AMD. They are trying to make some AI  
[02:20:28] chips and CPU chips early. There's a little bit,  
[02:20:30] but for the most part, it's Apple. As we go forward to the year after that, Apple  
[02:20:36] still gets closer to half of it as other people start ramping, but then it falls drastically,  
[02:20:43] just like for N3, where they were half. When I say N2, that includes A16,  
[02:20:49] which is a variant of N2. Over time, those nodes will be the majority.  
[02:20:56] What's also interesting is traditionally, Apple has been the first to a process node.  
[02:21:00] 2 nm is actually the first time they're not. Well, that’s besides Huawei. Huawei,  
[02:21:04] back in 2020 and before, was the first with Apple, but they were both making smartphones.  
[02:21:08] Now, with 2 nm, you've got AMD trying to make a CPU and a GPU chiplet that  
[02:21:14] they use advanced packaging to package together, in the same timeframe as Apple.  
[02:21:21] This is a big risk for AMD that causes potential delays because it's a brand-new  
[02:21:26] process technology. It's hard. But at the end of the day, this is a bet that they want to do  
[02:21:30] to scale faster than Nvidia and try and beat them. As we move forward, when we move to the A16 node,  
[02:21:36] the first customer there is not even Apple. It's AI. As we move forward,  
[02:21:41] that will become more and more prevalent. Not only will Apple not be the first to a node,  
[02:21:46] they will also not be the majority of the volume to the new node.  
[02:21:49] They'll then just be like any old customer. Because the scale of TSMC's CapEx keeps  
[02:21:53] ballooning, but Apple's business is not growing at the same pace,  
[02:21:56] they become a less and less relevant customer. They also will just cut their orders because  
[02:22:02] things in the supply chain are kicking them out, whether it be  
[02:22:04] packaging or materials or DRAM or NAND. These things are increasing in cost.  
[02:22:10] They can't pass on all the cost to customers likely because the consumer is not that strong.  
[02:22:14] You end up with this conundrum where they are just not TSMC's  
[02:22:18] best bud like they have been historically. Do you think if Huawei had access to 3 nm,  
[02:22:23] they would have a better accelerator than Rubin? Potentially, yeah. Huawei was the  
[02:22:29] first with a 7 nm AI chip as well. They were the first with a 5 nm mobile chip,  
[02:22:33] but they were the first with a 7 nm AI chip. The Huawei Ascend was two months before the TPU  
[02:22:41] and four months before Nvidia's A100, I think. That's just moving to a process node.  
[02:22:49] That doesn't imply software or hardware design or all these other things.  
[02:22:55] But Huawei is arguably the only company in the world that has all the legs. Huawei has cracked  
[02:23:02] software engineers. Huawei has cracked networking technologies. That's, in fact,  
[02:23:06] their biggest business historically. They have cracked AI talent. Furthermore, beyond Nvidia,  
[02:23:13] they actually have better AI researchers. Beyond Nvidia, they have their own fabs.  
[02:23:18] And beyond Nvidia, they have their own end market of selling tokens and things like that.  
[02:23:23] Huawei is able to get the top, top talent. Nvidia is as well, but not with as much  
[02:23:30] concentration, and Huawei has a bigger pool in China.  
[02:23:33] It's very arguable that Huawei, if they had TSMC, would be better than Nvidia.  
[02:23:38] There are areas where China has advantages in areas that Nvidia can't access as easily.  
[02:23:46] Not just scale, but certain optical technologies China's actually really good at.  
[02:23:54] I think it's very reasonable that if in 2019 Huawei was not banned from using TSMC,  
[02:24:02] Huawei would have already eclipsed Apple as the biggest TSMC customer.  
[02:24:06] Huawei has huge share in networking, compute, CPUs, and all these things.  
[02:24:10] They would have kept gaining share, and they'd likely be TSMC's biggest customer.  
[02:24:14] Wow. That's crazy. I've got a random final question for you.  
[02:24:18] The other part of the Elon interview was robots. If humanoids take off faster than people expect,  
[02:24:24] if by 2030 there's millions of humanoids running around which each need local compute,  
[02:24:33] any thoughts on what that implies? What would be required for that?  
[02:24:37] There's a lot of difficulties with the VLMs and VLAs that people are deploying on robots.  
[02:24:46] But to some extent, you don't need to have all the intelligence in the robot.  
[02:24:49] It would be much more efficient to not do that. Because in the cloud, you can batch  
[02:24:54] process and all these things. What you may want to do is have a  
[02:24:58] lot of the planning and longer-horizon tasks determined by a much more capable model in  
[02:25:04] the cloud that runs at very high batch sizes. Then it pushes those directions to the robots,  
[02:25:08] who interpolate between each subsequent action. Or it is given a command like, "Hey,  
[02:25:13] pick up that cup," and then the model on the robot can pick up the cup.  
[02:25:17] As it's picking up, things like weight and force may have to be determined by the model  
[02:25:27] on the robot, but not everything needs to be. It can say, "hey that’s a headphone" and the  
[02:25:34] super model in the cloud can say, "I know these headphones are Sony XM6s,"  
[02:25:38] which is not a Dwarkesh ad spot, but... I’m like, why is this guy's plugging this  
[02:25:42] thing so hard. It's on the table. It's on his neck when we're interviewing Satya together.  
[02:25:48] Is he getting paid by Sony? Unfortunately not. But anyways,  
[02:25:53] it might say, "Hey, the headband is soft, and this is the weight of it," and all these things.  
[02:25:58] Then the model on the robot can be less intelligent,  
[02:26:00] take these inputs, and do the actions. It may get told by the model in the cloud  
[02:26:05] every second, or maybe ten times a second, depending on the hertz of the action.  
[02:26:09] But a lot of that can be offloaded to the cloud. Otherwise, if you do all of the processing on the  
[02:26:15] device, I believe it would be more expensive because you can't batch.  
[02:26:17] Two, you couldn't have as much intelligence as you do in the cloud because the  
[02:26:20] models will just be bigger in the cloud. Three, we're in a semiconductor shortage world,  
[02:26:25] and any robot you deploy needs leading-edge chips because the power is really bad for robots.  
[02:26:31] You need it to be low power and efficient, and all of a sudden you're taking power  
[02:26:36] and chips that would've been for AI data centers, and you're putting them in robots.  
[02:26:39] So now that 200 gigawatts gets lower if you're deploying millions of humanoids.  
[02:26:43] I think this is very interesting because something people might not appreciate  
[02:26:47] about the future is how centralized, in a physical sense, intelligence will be.  
[02:26:52] Right now, there are eight billion humans, and their compute is in their heads, on their person.  
[02:27:00] In the future, even with robots that are out physically in the world—obviously,  
[02:27:04] knowledge work will be done in a centralized way from data centers with hundreds of thousands  
[02:27:09] or maybe millions of instances—the future you're suggesting is one where there's more  
[02:27:17] centralized thinking and centralized computation driving millions of robots out in the world.  
[02:27:25] That's an interesting fact about the future that I think people might not appreciate.  
[02:27:28] I think Elon recognizes this, which is why he's going to different places for his chips.  
[02:27:35] He signed this massive deal with Samsung to make his robot chips in Texas because I personally  
[02:27:41] think he thinks Taiwan risk is huge. Because of that and the centralization  
[02:27:46] of resources in Taiwan, having his robot chips in Texas means having a separate  
[02:27:51] supply chain that is not as constrained. No one's really making AI chips on Samsung  
[02:27:56] besides Nvidia's new LPU that they launched. They’re launching it next week, but we're  
[02:28:01] recording this the week before. This episode's coming out Friday.  
[02:28:04] Oh, this episode's coming out before. Sick. They're launching this new AI chip  
[02:28:09] next week which is built on Samsung, but that's a recent development from Nvidia.  
[02:28:15] That's the only other AI demand there, whereas on TSMC, everything is competing.  
[02:28:19] He gets both geopolitical diversification and supply chain diversity for his robots,  
[02:28:25] and he's not competing as much with the infinite willingness to pay for the data center geniuses.  
[02:28:34] Final question, on Taiwan. If we believe that tools are the ultimate bottleneck,  
[02:28:41] how much of Taiwan's place in the AI semiconductor supply chain could we de-risk simply by having a  
[02:28:50] plan to airlift every single process engineer at TSMC out if they get blockaded or something?  
[02:28:56] Or do you still need to ship out the EUV tools, which would be multiple plane loads  
[02:29:02] per single tool and would not be practical? If you ship out all the process engineers and  
[02:29:06] assuming it's hot enough that you destroy the fabs, no one has all the fabs in Taiwan now,  
[02:29:11] which is a big risk. These tools actually use a lot of  
[02:29:16] semiconductors which are manufactured in Taiwan. It's a snake eating its own tail meme because  
[02:29:22] you can't make the tools without the chips from Taiwan, which you can't use without the tools in  
[02:29:26] Taiwan. There's obviously some diversification there. They don't use super advanced chips in  
[02:29:32] lithography tools, but at the end of the day, there is some dragon eating its tail.  
[02:29:36] Just shipping out all the engineers and blowing up the fabs means China has a  
[02:29:40] stronger semiconductor supply chain than the rest of the world in terms of verticalization,  
[02:29:44] now that you've removed Taiwan. You've got all the know-how,  
[02:29:49] but you've got to replicate it in, let's say, Arizona or wherever for TSMC.  
[02:29:56] It's going to take a long time to build all the capacity that TSMC has built over the years.  
[02:30:01] And so you've drastically slowed US and global GDP.  
[02:30:06] Not just growth, you've shrunk the GDP massively, and you've got a lot bigger problems.  
[02:30:12] Your incremental ability to add compute goes to almost zero.  
[02:30:16] Instead of hundreds of gigawatts a year by the end of the decade,  
[02:30:18] let's say something happens to Taiwan, now you're at maybe 10 gigawatts across Intel and Samsung,  
[02:30:24] or 20 gigawatts. It's nothing. Now all of a sudden you've really caused some crazy dynamics in AI.  
[02:30:31] Of course, you have all the existing capacity, but that existing capacity pales in comparison  
[02:30:35] to the capacity that's being expanded. Okay. Dylan, that was excellent. Thank  
[02:30:39] you so much for coming on the podcast. Thank you for having me. And see you tonight.  
