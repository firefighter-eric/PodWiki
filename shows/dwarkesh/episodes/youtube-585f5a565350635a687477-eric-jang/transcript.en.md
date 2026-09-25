# What rebuilding AlphaGo teaches us about self-play, RL, and future of LLMs - Eric Jang

[00:00:00] Today, I'm here with Eric Jang, who was most recently vice president of AI at 1X  
[00:00:04] Technologies, and before that, senior research scientist at what is now Google DeepMind Robotics.  
[00:00:10] You've been on sabbatical for the last few months. One of the things you've been doing is rebuilding,  
[00:00:15] improving, and hacking on AlphaGo. Today, you're going to explain building  
[00:00:21] AlphaGo from scratch and what it tells us about the future of AI research and development.  
[00:00:26] Before we get to that, why is AlphaGo interesting? Why is this the project you decided to do on  
[00:00:31] sabbatical rather than just hanging out at the beach?  
[00:00:34] I like making things, and AlphaGo and Go AI is one of those things that really got me into the field.  
[00:00:40] When I saw the early breakthroughs on AlphaGo in 2014, 2015, 2016 and so forth,  
[00:00:46] it was profound to see how smart AI systems could become and the computational complexity  
[00:00:53] class they could tackle with deep learning. This is a problem that has long been understood  
[00:00:59] to be intractable for search, and yet it was solved through deep learning.  
[00:01:07] That was quite mysterious to me, and I've always wanted  
[00:01:09] to understand that phenomenon a little better. My training is in deep neural nets for robotics,  
[00:01:14] where the decisions made by the neural networks are a bit more intuitive.  
[00:01:19] But AlphaGo is a problem where the decisions are the result of a very, very deep search.  
[00:01:26] It's always been very mysterious to me how a ten-layer network can amortize the simulation  
[00:01:31] of something so deep in the game tree. If you plot out how much compute it took  
[00:01:38] to build various iterations of strong Go bots over the years, you can see that in  
[00:01:42] 2020 there was an open-source project called KataGo by David Wu from Jane Street, which  
[00:01:49] achieved a 40x reduction in the compute needed to train a really strong Go bot tabula rasa.  
[00:01:54] I'm not certain if it's stronger than AlphaGo Zero, AlphaZero, or MuZero, but it's very strong,  
[00:01:59] and this is what most Go practitioners today train against when they're playing an AI.  
[00:02:04] Thanks to LLM coding, what took a whole team of research scientists at DeepMind and millions of  
[00:02:09] dollars of research and compute can now be done for a few thousand dollars of rented compute.  
[00:02:14] We should first discuss how Go works. How does the game work?  
[00:02:19] Go is a very simple game that can be implemented quickly and easily on a computer.  
[00:02:24] The objective is to put down black and white stones and  
[00:02:29] try to occupy as much territory as possible. I might start by putting down a black stone.  
[00:02:34] Black always goes first. Go ahead. The way you capture an opponent's stones is that  
[00:02:38] for every intersection, if you can surround all four of its neighbors with your stones,  
[00:02:45] then it's cut off from oxygen, if you will, and it's a dead stone.  
[00:02:53] Now I control these four stones as well as this empty intersection here.  
[00:02:57] There are slight variations between Chinese, Japanese, and what are called Tromp-Taylor rules.  
[00:03:03] Tromp-Taylor rules are designed to be completely unambiguous, so this  
[00:03:06] is what all Go AIs train and resolve against. In typical Go, when humans play, you're actually  
[00:03:12] not allowed to put this white stone down here. It would be instant suicide. In Tromp-Taylor, it's  
[00:03:17] actually fine. You put it down, and it immediately resolves to death, so the outcome is the same.  
[00:03:22] Let's start over and play a few stones, and then I'll explain some more. I'll just start there.  
[00:03:32] I'm basically playing randomly here, but I'm trying to get around your stones and  
[00:03:36] see if I can surround them. This move exposes one empty  
[00:03:48] neighbor for your white stone. It's akin to a check in chess.  
[00:03:53] If you don't respond immediately by putting one here, then I can immediately capture this.  
[00:03:57] I see. Because it's the diagonals that determine whether you're surrounded or not.  
[00:04:01] The cross-section, not the diagonals. This one is surrounded on three sides,  
[00:04:06] so you're at threat of losing that stone if you don't play one immediately there.  
[00:04:11] Now you can see that I'm starting to pressure you, because by putting a stone here,  
[00:04:16] you're forced to put one here. Otherwise, you would have this  
[00:04:20] two-block to yourself. Yes. And if you think  
[00:04:23] through what happens if you were to respond here, you can probably  
[00:04:27] search into the future and deduce what I'll do in response once you do that.  
[00:04:31] You have a lot of confidence in my abilities, but I'm guessing you'd put the black here.  
[00:04:35] That's right, and then I would capture all three of these stones.  
[00:04:37] So I should just assume that this little block is gone.  
[00:04:40] Yes. In Go, it's actually okay to let an opponent capture some stones if,  
[00:04:45] for example, it lets you position to capture more stones somewhere else on the board.  
[00:04:50] This is what makes Go a beautiful game: you can lose the battle but win the war.  
[00:04:56] As the board size increases, the complexity of these micro versus macro  
[00:05:01] dynamics gets more interesting. Presumably you'd put one here.  
[00:05:06] So now I would capture this entire group, and this would be mine.  
[00:05:10] There's one more case I want to demonstrate, which I actually had a bug in my code for recently.  
[00:05:18] Let's consider a formation like this, with other pieces on the board in play.  
[00:05:28] Let's talk about how the game ends. In this territory, who controls these  
[00:05:35] areas? Is it white or black? White.  
[00:05:38] It's actually black, because I've surrounded this whole area.  
[00:05:43] Assuming I have other black stones here, it's very hard for you to break this  
[00:05:48] out of the control of these stones. And when the final score is tallied,  
[00:05:51] would these ones also count as being in... Great question. This is where different rule  
[00:05:57] sets have different ways of scoring. We should talk about how you resolve  
[00:06:02] scores between humans and how you resolve scores in computer Go, because there's some  
[00:06:06] ambiguity in how humans evaluate this. Most humans would look at this board  
[00:06:11] configuration and conclude that black has totally surrounded white, and white has no chance of life.  
[00:06:16] We could play out more here, but at the end I would capture everything.  
[00:06:21] However, if you have a way of breaking this formation and connecting white to  
[00:06:24] something outside of it, then it can flip. This is where it's a little bit hard for a  
[00:06:30] computer to decide these kinds of things. How do humans do it? It's worth thinking about how  
[00:06:34] humans resolve this, because this will map later to how we think about the deep neural network.  
[00:06:40] Humans basically say, "I think the game is done," and then you have to also say,  
[00:06:45] "I think the game is done." Then we'll say, "I think these  
[00:06:47] are my stones," and you have to agree. If you don't agree, we keep playing.  
[00:06:53] Essentially, once two humans—their so-called value function—agree on a consensus, then the  
[00:06:59] Chinese rules resolve that. In Tromp-Taylor scoring,  
[00:07:04] it's perfectly unambiguous, so it can be decided algorithmically by a computer.  
[00:07:09] If you have this at the endgame, the way you score it is that you first count how many  
[00:07:15] stones you control, and that's unambiguous. Then you count how many empty intersections  
[00:07:20] are not touched by your opponent's stones. These intersections would not count for either  
[00:07:25] player, because all of these intersections are connected to both white stones and black stones.  
[00:07:31] If this were like this, then white would get three points.  
[00:07:36] This is a little odd because a human would know that white is actually losing these points.  
[00:07:42] But Tromp-Taylor scoring would consider white to have all of these points as well as these points.  
[00:07:48] So that is a very big difference in how computer Go scores things and how humans score things.  
[00:07:53] How does the game end? The game ends when either  
[00:07:56] a player chooses to resign or both players pass consecutively. Those are the rules.  
[00:08:04] Now help me crack this with AI. Let's understand how AlphaGo  
[00:08:10] actually works and how somebody in the audience might be able to implement it.  
[00:08:13] Let's start with an intuition about the underlying search process used to make moves,  
[00:08:21] and we'll layer on ideas from deep learning to make it much more efficient and tractable.  
[00:08:27] Go is a game with just two players. We're going to draw a person here,  
[00:08:31] and we're going to draw an AI here. Let's say this person is playing black,  
[00:08:38] so they go first. They go here. Now the AI is going to make a move based on what it sees here.  
[00:08:51] There's a question of how you encode these inputs into the AI.  
[00:08:54] Maybe you could use ones and zeros, but you want to represent black, white, and empty.  
[00:09:00] You would need at least three different values. Maybe you could use zeros, ones, and twos.  
[00:09:05] The AI might see something like zero, zero, zero, zero, one.  
[00:09:23] This is the input to the AI on its turn. The AI can choose. Let's just pick three possible random  
[00:09:29] moves it can make, and I just drew these at random. Which move is best here? Well,  
[00:09:33] we don't know until the game ends. Go doesn't have any kind of local  
[00:09:37] reward for which move here is good. This is what makes Go a very difficult game.  
[00:09:41] You don't actually know who won until you really get to the end. How deep is this tree? On a 19x19  
[00:09:49] Go board, there are roughly on the order of 361 moves on any given move, and of course,  
[00:09:56] as it fills up, you have fewer moves. The number of steps in the game  
[00:10:02] can be somewhere from 250 to 300 moves. Experts might decide to end the game well before  
[00:10:08] that, but under Tromp-Taylor scoring, you actually have to play things all the way to the end.  
[00:10:12] So this could be 300 moves, a depth of 300 in the tree.  
[00:10:19] If you keep on expanding possible moves—here the AI goes, then here the human would go,  
[00:10:27] and so forth—you find that you end up with an enormous  
[00:10:41] explosion in the possible game outcomes originating from just this one state.  
[00:10:48] This is something on the order of 361³⁰⁰, which is far more than the number of atoms in the universe.  
[00:10:58] Of course, there are redundancies and symmetries, so it's not actually that, but if you were to do  
[00:11:04] a naive tree with no merging of children, you end up with a tree about this big.  
[00:11:09] What do you mean by "merging of children"? Let me use this board here.  
[00:11:13] If we start here, and then you play here, and then I play here, and then you play here,  
[00:11:20] that's equivalent to me starting here, you playing here, me playing here, and then you playing here.  
[00:11:28] Both arrived at the same spot, but through different paths.  
[00:11:30] So this child node can be thought of as a shared ancestor.  
[00:11:34] Got it. And I guess it starts at 361 but it decreases by one each time.  
[00:11:38] Yes, the branching factor decreases by one each time.  
[00:11:41] In any case, this is a very large tree. This is also why computer scientists for  
[00:11:47] many years thought that Go was not a tractable problem this century.  
[00:11:50] The amount of compute you would need to exhaustively  
[00:11:53] search every possibility is just too large. If you could, Go is actually a deterministic game.  
[00:12:00] In any given state, you can compute the best possible strategy you can  
[00:12:06] make in order to win the game. You can search all the possible  
[00:12:09] futures where you win, and then just make sure you always stay in that set of futures.  
[00:12:16] AlphaGo's core conceptual breakthrough was using neural nets to make this search problem tractable.  
[00:12:23] Before we get into how neural networks are involved, let's talk about how we can,  
[00:12:29] assuming we had a powerful enough computer, search this tree to find the best move.  
[00:12:35] In the beginning, you're not going to build out the whole tree,  
[00:12:39] because storing it would be very expensive. Instead, you might interactively figure out  
[00:12:44] which leaves of this tree are worthy of exploring and expanding into the  
[00:12:48] future to see what else is there. There are some early algorithms in  
[00:12:54] the bandit literature like UCB1, which is not exactly appropriate for a sequential game like Go,  
[00:13:02] but very much inspired the action selection algorithm used in AlphaGo.  
[00:13:08] UCB1 looks like: on every move, we're going to take the best action—the argmax over a that  
[00:13:16] maximizes Q of a, and I'll explain what Q of a is in a moment—plus some sort of exploration bonus.  
[00:13:34] On every node, we're going to track a few quantities.  
[00:13:38] Let's consider each of these a node. This is the root node where you're  
[00:13:43] making decisions from, and these are the children of the root node.  
[00:13:50] Each node is basically a data structure that stores a visit count of this child node.  
[00:14:04] How often the parent visited this node. Yes. One thing that's easy to trip on if you  
[00:14:09] come from robotics or other kinds of reinforcement learning is, where are the actions? I'm only  
[00:14:15] talking about nodes. Nodes here represent states, and because this is a perfectly deterministic  
[00:14:21] game with no randomness, you actually can just infer the action based on the child.  
[00:14:26] If I go here, that implies an action, and this is the state we resolve to.  
[00:14:32] If you ask LLMs to vibe-code an MCTS implementation, they will most likely  
[00:14:37] design the right data structure here. But it's sort of a chef's choice.  
[00:14:41] You can rewrite the tree structure however you like.  
[00:14:44] This is what Claude 4.6 wrote for me when I asked it, and it was a very reasonable choice.  
[00:14:52] Qₐ represents the mean action value of this action.  
[00:15:02] I'll use a subscript a to denote that this corresponds to taking a specific  
[00:15:05] action to get here from the root node. Taking a gets us to this node here.  
[00:15:17] We're also going to store the probability of taking this action  
[00:15:22] Again, from the parent? From the parent, yes. What are the odds that we  
[00:15:26] sample this one? This will become relevant later. We've talked about a deterministic tree for now,  
[00:15:32] so I'll bring probabilities into this later. Finally, we have a dictionary of children,  
[00:15:39] which is just more of these nodes in a classic linked list-style reference tree.  
[00:15:45] This is the basic data structure to implement a tree.  
[00:15:50] In AlphaGo, they use a slightly different action-selection criterion called PUCT,  
[00:15:56] short for Predicted Upper Confidence with Trees. When you select which child to take,  
[00:16:06] you do argmax a of Q(s,a) plus a constant. The equation forms are pretty similar. These  
[00:16:34] are both scoring criteria. You want to argmax this quantity and you want to argmax this quantity to  
[00:16:38] determine which action to take. Let's break down the intuition  
[00:16:41] of how you select actions here. Q(s,a) is the mean action value,  
[00:16:46] so how good a given child is on average. If you actually knew the whole tree,  
[00:16:52] this is all you need to select the best action. You don't really need to do more than that.  
[00:16:56] But if you're interactively building this tree as you're figuring out what the Q values should be,  
[00:17:01] then occasionally you have to try some other actions as an explore-versus-exploit trade-off.  
[00:17:08] In both UCB and PUCT, there's this term that basically rewards  
[00:17:13] taking actions you haven't taken before. As we mentioned, each node stores the visit  
[00:17:19] count of taking that specific action. Everything is initialized to zero. For a given action,  
[00:17:25] let's call it action a, initially it's zero. As n is increasing, if we've already made 10  
[00:17:36] action selections from that root node but we haven't picked a yet,  
[00:17:40] then this term starts to become quite large for a. Conversely, if we've chosen a 10 times out of 10,  
[00:17:47] then this term is quite small. It diminishes very quickly. The same thing is true here.  
[00:17:53] Just to make sure I'm understanding, let me put it in my own words. Let's focus on UCB. Conceptually,  
[00:18:03] you can think of it as two different things: the Q and the exploration term.  
[00:18:09] Let's be clear about what Q is. Q is basically saying, once we do  
[00:18:12] these rollouts—you're actually running all these simulations—you go down the tree and figure out:  
[00:18:17] if I end up at the terminal value of this tree, do I win this game or not?  
[00:18:23] You average whether I win or not across all the leaves of this tree starting from this node.  
[00:18:31] That average, you put in Q. So Q represents the probability that  
[00:18:38] I'll win this game starting at this node. That is your sort of exploit.  
[00:18:42] It's saying: I've run these simulations, and I think this is a good move or not.  
[00:18:46] The other term is saying: have I explored this branch enough yet  
[00:18:51] relative to the other actions I could be exploring, or have already explored?  
[00:18:56] If I haven't explored this branch yet, maybe I think it has a low score,  
[00:18:59] but I just haven't explored that many leaves down this node in this tree.  
[00:19:06] So I should try this even though Q, the exploit term, is telling me it's not that valuable.  
[00:19:11] Because ln(n) grows slower than n, over time you will move from the argmax being dominated  
[00:19:22] by the exploration term, which is the second term here, to the argmax being dominated by the Q term,  
[00:19:27] which is when you've done enough simulations and are confident that this is the branch to go down.  
[00:19:33] Yes, that's right. The motivation for UCB was to come up with an algorithm where,  
[00:19:39] if you don't know the payoff of the different actions you can select, this strategy,  
[00:19:47] given some exploration term here, bounds your regret in terms of how wrong you can possibly  
[00:19:52] be. I don't know the proof. I also don't know if this one is proved to have logarithmically or  
[00:19:58] square-root-bounded regret, but I think the algorithm was derived to look something like this.  
[00:20:02] You can tell these terms grow a little differently, and this is to account for the  
[00:20:06] fact that Go has many more actions for any given move compared to your standard bandit problem.  
[00:20:13] One small clarification: you talked about simulations and probabilities.  
[00:20:18] We should remember that Go fundamentally is a deterministic game.  
[00:20:22] Where does the notion of probability come from here?  
[00:20:27] If you had a very powerful computer, there are no probabilities.  
[00:20:32] You can just compute the true average of the mean action value.  
[00:20:36] So where does the probability come in? In computer Go before AlphaGo,  
[00:20:44] we've always done some sort of Monte Carlo method where we take the expected Q value averaged over  
[00:20:52] a randomly selected tree. That randomly selected  
[00:20:56] tree is where probabilities come in. The interpretation of Q is: what is the expected  
[00:21:02] action value under the random distribution induced by some random search process?  
[00:21:10] Where does the random search process come in? That's where Pₐ, of action, comes in.  
[00:21:15] If we assume a naive algorithm where you have a uniform probability of taking any valid action,  
[00:21:20] then this would just be one over the number of valid moves.  
[00:21:26] You would be taking this average over a very diffuse tree.  
[00:21:31] This is a valid integral, but it's very slow because you're going to consider a lot of trees  
[00:21:36] that have very low value. It's essentially almost  
[00:21:39] like an importance sampling problem. Only a few actions and paths contribute high  
[00:21:47] value, and almost everything else is low value. So that's a tricky problem here.  
[00:21:55] This is the action selection criterion for how you decide which moves to go down.  
[00:22:00] As you move down in tree search, you will eventually run into a node where  
[00:22:06] it's quite clear you've won or lost. At the very end of the game, when there  
[00:22:10] are no valid moves left to play under Tromp-Taylor scoring, you can decide whether you won or lost.  
[00:22:22] This is the final return of the whole game. We can assign a value, U, to a terminal leaf  
[00:22:37] node of the tree, but how do we assign values to the nodes prior to that, the parents?  
[00:22:44] You take the mean action value, which is essentially your average.  
[00:22:52] Suppose these were all leaf nodes. The mean action value of this node  
[00:23:01] is just the average of whether you won or lost at the leaf nodes.  
[00:23:07] Correspondingly, you can walk up the chain and say the mean action value of this node—let's call it  
[00:23:12] Qb—is just a weighted average of these ones here. The weighted average could depend on whether  
[00:23:23] you have a different sampling distribution. But the basic intuition is that you want to  
[00:23:27] resolve the game where you have a deterministic win or lose, and then you can go backwards—this  
[00:23:33] is called the backup step—and assign values to these nodes or actions corresponding  
[00:23:40] to the average over the final terminal leaf. If you were to do this without neural networks,  
[00:23:47] it would still be intractable. You would have trouble finding  
[00:23:51] which actions to sample. A lot of the actions would  
[00:23:55] contribute very low value, especially if you're trying to fight your way out of a losing position.  
[00:24:00] Only a few actions give you high value, so the search in practice is still very expensive.  
[00:24:05] But the idea is that because Go follows a tree structure, you can inform a very good  
[00:24:14] estimate of the value of this node based on the downstream values, assuming they're  
[00:24:19] all correct and you've searched deep enough. Your earlier explanation—about the sorts of  
[00:24:25] states where it's obvious to a human who's going to win, but deterministically you still have to  
[00:24:31] play it out—actually drew upon the intuition for why 1) the value function is both trainable and 2)  
[00:24:39] necessary in order to learn this game effectively. Maybe it's worth defining value  
[00:24:45] in the first place. We talked about U being your  
[00:24:51] final resolution of whether you won or lost. This is a terminal leaf node condition.  
[00:24:56] Humans don't play all the way to the leaves of the tree.  
[00:25:00] They stop dozens of moves before, maybe even 100 moves before in high-level play. How do they know?  
[00:25:09] You can think about humans as implicitly having a neural network called a value function that  
[00:25:16] takes in a board state and evaluates p(win). The human glances at the board and knows,  
[00:25:27] "I'm probably going to lose." They're essentially running a neural  
[00:25:30] network that looks at a board and implicitly amortizes a huge number of possible game playouts.  
[00:25:38] They take that average and decide whether the board is winnable or not, and whether they should  
[00:25:42] concede or keep playing. This is remarkable. If you think about the beauty of something like this,  
[00:25:51] a neural network in a human can somehow do all of this simulation at a glance.  
[00:25:57] They just know within a few seconds, without actually playing every single game logically,  
[00:26:03] based on crystallized knowledge and experience. They can do this. This  
[00:26:07] gives us a hint that in games like Go, there are ways to radically speed up the search process.  
[00:26:14] This is one of the fundamental intuitions behind why AlphaGo works.  
[00:26:18] You can train a value function to look at a board and quickly resolve the game without playing out  
[00:26:25] all of these trees to a very deep search depth. Makes sense. I will say for the audience,  
[00:26:36] for previous episodes when I was prepping and it seemed relevant to understand how AlphaGo  
[00:26:39] works, I would find it very confusing. But it's the kind of thing where once you  
[00:26:44] understand the problem in this way and then build the next few pieces, it is actually a lot more  
[00:26:49] understandable and it makes a lot of sense. It's okay to be confused right now,  
[00:26:53] but it's probably simpler to understand, by the end of this lecture, than you anticipate.  
[00:26:59] I’ll just make that note for the audience. The important intuition at a high level—to  
[00:27:03] step back about where we're going with all this—is that classically, for games like Go,  
[00:27:09] you could build a tree, but we don't have computers powerful enough for that.  
[00:27:15] Estimating the value of every action you could possibly take is also hard because  
[00:27:19] you don't know until the end of the game. You could take averages by playing them to the  
[00:27:24] end, but that's also hard because you don't know which actions to take to sample these averages.  
[00:27:30] Conceptually, there are two problems: the breadth of the tree and the depth of the tree.  
[00:27:35] AlphaGo gives us a way to shrink both of those to be tractable.  
[00:27:41] That's essentially the core idea behind it. We take the idea that humans can glance at a  
[00:27:47] board and instantly predict whether we win. That maybe gives us the opportunity to  
[00:27:51] truncate how deep we search. We also know that humans can  
[00:28:06] intuitively, at a glance, decide what moves might be good on a Go board.  
[00:28:10] These are two things we can use deep neural networks for, to accelerate the search process.  
[00:28:16] Before we talk about neural nets, let's go back to how this playout works.  
[00:28:20] We've only talked about making one move. The AI looks at this encoded Go board. It  
[00:28:25] has a tree. It searches deeply into the tree to find out which of its actions might be the best,  
[00:28:32] takes that action, and goes back to the human. Now the human sees a Go board that looks like  
[00:28:40] this, and they make their move. Maybe they put their stone here.  
[00:28:50] Now we go back to the AI, which now looks at a new encoded board.  
[00:29:07] I've used 2 to denote the AI playing as white, 1 to denote the  
[00:29:11] human playing as black, and 0 as empty. On the AI's turn, it does the MCTS tree  
[00:29:17] search all over again from scratch. It throws away the old tree that it  
[00:29:21] searched last round. Now there's a new root  
[00:29:23] node and it begins to search anew. You can basically think about MCTS  
[00:29:31] as a search algorithm that decides which moves to play best, aided by  
[00:29:36] neural networks, and it's done on every move. Let's talk about the neural network part of this.  
[00:29:46] While you're erasing, another thing that was important for me to understand was about the MCTS  
[00:29:52] data structure with nodes and children of nodes. This is done per move and reinstantiated  
[00:30:00] once a move is made. A human makes a move,  
[00:30:03] then the AI looks at this and runs a bunch of simulations to figure out what move to make next.  
[00:30:12] A simulation is exploring one more node in the MCTS tree.  
[00:30:19] Once you run 1,000 simulations, that informs the probability of what move to make next,  
[00:30:29] as you'll explain. That’s what you store. You choose the best move given those probabilities.  
[00:30:34] You discard all of that, the next player makes a move, and you restart this process  
[00:30:39] at the beginning of every move. Correct. One small addendum:  
[00:30:42] you don't discard all of that. You keep one thing behind that we'll use later.  
[00:30:47] Just like I did for Reiner, I wanted to make flashcards for this episode so that  
[00:30:50] people could retain these concepts. And ideally, an LLM could generate  
[00:30:54] some candidates for me to then refine. But to actually get high quality suggestions,  
[00:30:58] I needed to design a whole pipeline where the AI could take and ingest screenshots of  
[00:31:03] the blackboard at the right timestamps and then make SVG diagrams in case visuals were helpful,  
[00:31:08] and then run the writing and drawing through a critic and then revise the card in response  
[00:31:12] to this feedback. It's very hard to  
[00:31:14] accomplish this just by stacking LLM calls. This sort of step-by-step recipe works much better  
[00:31:19] if you have a durable agent that's been engaging with the task across all the previous stages.  
[00:31:23] So I used the Cursor SDK to spin up an agent for each card.  
[00:31:26] The Cursor harness saved me a bunch of work in designing some custom context scaffold or  
[00:31:31] figuring out how to design tool calls for taking screenshots or making animations.  
[00:31:36] These agents all run in the cloud, so I don't have to worry about leaving my laptop open.  
[00:31:40] I just get an email when I have candidates to review.  
[00:31:42] You can check out my cards at flashcards.dwarkesh.com.  
[00:31:47] You can start building with the agents SDK at cursor.com/dwarkesh.  
[00:31:54] Now that we have a basic intuition of how moves are made with search, we're going to  
[00:31:57] talk about how neural networks can speed this up by providing an analog to human intuition.  
[00:32:03] There are two networks. There is the value network, which takes in a  
[00:32:09] state and predicts, am I going to win or lose? It's a binary classification problem.  
[00:32:17] Then we have a policy network, which induces a distribution over good actions to take.  
[00:32:26] I'm going to draw a one-dimensional flattened move distribution, but this is really a square grid.  
[00:32:38] These are the probability distributions over good actions.  
[00:32:42] Both of these are categorical classification problems.  
[00:32:45] You can train this like any classifier with deep learning, cross-entropy loss, that kind of stuff.  
[00:32:54] The specific architecture does not matter too much.  
[00:32:57] I tried a few different architectures. Transformers work, ResNets work. For  
[00:33:01] small data regimes, my experience is that ResNets still outperform transformers and give you more  
[00:33:07] bang for the buck at lower budgets. But this may not always be true.  
[00:33:10] Wait, why is that? They provide the  
[00:33:12] inductive bias of local convolutions. Generally, transformers start to outperform  
[00:33:18] residual convolutional networks when you want more global context.  
[00:33:22] One interesting finding from the KataGo paper was that they found it quite useful to pool together  
[00:33:29] and aggregate global features throughout the network, to give the network a global  
[00:33:36] sense of how to connect value from one side of the board to the other.  
[00:33:40] What does it mean to aggregate global features? If you have a very large 19x19 Go board,  
[00:33:48] and you've got some battles going on here and some battles going on there, when you pass  
[00:33:55] this through a convolutional neural network, the receptive fields are going to be good at computing  
[00:34:02] local things and making that invariant. But they won't be able to connect these  
[00:34:08] two features easily. They need to be pooled  
[00:34:11] together and attend to each other somehow. The argument for why transformers are good  
[00:34:17] for computer vision tasks—vision transformers and so forth—is that because they have global  
[00:34:23] attention across the whole thing, they can more easily draw these connections.  
[00:34:27] But you do need more data there so that you can learn the invariant local features through data.  
[00:34:36] I've tried very hard to make transformers work for this problem because I was curious if transformers  
[00:34:40] would present some sort of breakthrough in Go and just remove a lot of those tricks.  
[00:34:44] But try as I might, I haven't figured out a way to make transformers better than ResNets for now.  
[00:34:50] One more tangential question. It makes sense why transformers, with their global pooling  
[00:34:56] of information, would be better if you need to consider information that is not just spatially…  
[00:35:04] CNNs give you a bias that the things next to you are especially relevant.  
[00:35:09] And then they're aggregated up slowly. For games where it isn't that relevant  
[00:35:15] what is happening locally—you just have to consider the whole thing—you're  
[00:35:18] saying transformers would work better. We’re talking about the spatial dimension.  
[00:35:22] How about the temporal dimension? Right now we're only considering the previous move because  
[00:35:27] it is a deterministic full-information game. What if it were something like poker or Diplomacy,  
[00:35:35] where a bluff they made a while back is relevant to understanding now?  
[00:35:40] And to decide your next move, you need to consider all those previous states.  
[00:35:44] Would that change the consideration of what inductive  
[00:35:47] bias and which architecture is most relevant? Great question. Go is a perfect information game.  
[00:35:54] In perfect information games, there does exist a Nash equilibrium strategy for which  
[00:36:00] you can do no worse than any other strategy. If you know your opponent has a particular bias,  
[00:36:07] like they love to play aggressively, you can in principle counter that specific strategy  
[00:36:12] better than a Nash equilibrium policy. But to counter any given strategy,  
[00:36:18] there exists a single Nash equilibrium that can be decided solely using the current state.  
[00:36:25] That is a design choice AlphaGo made, which in hindsight turned out to work very well because  
[00:36:31] the Nash equilibrium seems to be superhuman. No human strategy seems to be able to beat it.  
[00:36:38] There are variations of this where you would need to consider temporal history.  
[00:36:42] This is a very exciting research area, and I'd encourage people to fork my repo and try it out.  
[00:36:48] If you were to play 2v2 Go, you actually need to model your partner's behavior.  
[00:36:54] You may not have information on how they play, so you need to aggregate information on how they  
[00:36:58] play so you can respond accordingly. These are situations where it's no  
[00:37:04] longer a perfect information game. In games of imperfect information  
[00:37:08] or partial observability, you do need context to build a model.  
[00:37:13] That's a place where things can get very exciting in terms of self-play or Diplomacy-style games.  
[00:37:21] Returning to the neural network, the architecture again is not super important.  
[00:37:25] You can get it to work with transformers. You can get it to work with ResNets.  
[00:37:27] I found that for low-budget experiments, ResNets work a little better.  
[00:37:32] You can also use Karpathy-style AutoResearch hyperparameter  
[00:37:35] tuning to make your architecture pretty good. You don't have to worry too much about that.  
[00:37:40] You just need to set up the problem so that you have a target optimization.  
[00:37:46] We're going to pick a somewhat arbitrary architecture that worked for what I did.  
[00:37:50] But again, this part is not super important. You have your encoded board state and, similar  
[00:38:00] to an RGB, we're going to have three channels. One channel to encode black, one to encode white,  
[00:38:06] and one to encode empties or a masked region if you want to train on multiple board sizes.  
[00:38:17] I'm actually not going to talk about multiple board sizes for now. That's a bit too  
[00:38:20] complicated. We have this two- or three-channel RGB-like image, and we feed it into a ResNet.  
[00:38:33] Then we have two branching heads. One head predicts the value function,  
[00:38:40] which is a single logit, let's just call it R¹. Then we have the policy, which is R³⁶¹.  
[00:38:54] This is the architecture. We're going to train this to predict the outcomes of games  
[00:39:01] given the board state, and we're also going to train it to predict what are good moves.  
[00:39:06] The original AlphaGo paper, called AlphaGo Lee, initialized this network with a  
[00:39:13] supervised learning dataset of expert human play. Later, they removed this restriction by having  
[00:39:18] the model teach itself how to play well. I find it super nice for implementation,  
[00:39:23] for your audience, to always initialize your experiments to something easy and get  
[00:39:30] the problem working before trying to bite off the whole thing and learn tabula rasa.  
[00:39:37] In deep learning, initialization is everything. You always want to initialize your research  
[00:39:43] project to something as close to success as possible, especially if you're doing  
[00:39:47] something new that you haven't done before. Always pick something that works and then  
[00:39:50] get it to do something better, rather than start from something  
[00:39:52] that doesn't work at all and try to make it work. Under that philosophy, it's a great idea to start  
[00:39:59] with something that has a good initialization. We're going to take human expert plays  
[00:40:04] and train this model to predict good actions. We're going to take all the moves in which  
[00:40:14] an expert won and predict those actions. Regardless of board state, whether you won  
[00:40:20] or lost, you're going to predict the outcome. You might be wondering, for some of the early  
[00:40:24] boards where only one stone has been put down, how could  
[00:40:28] you possibly know who the winner of this game is? Well, if you have hundreds of thousands of games,  
[00:40:36] on average you'll probably see that boards starting like this have half of the games  
[00:40:41] branch off and win, and half branch off and lose. So that'll actually be fine. When you  
[00:40:46] train this model to predict those outcomes, the logit will sort of converge to 0.5.  
[00:40:52] For these things, it's expected that once you train the model, a starting board state will  
[00:40:57] look like 0.5, and then as you progress towards the end of the game, the win probability will  
[00:41:06] either go up or down. This is your move number. As you get hundreds of steps into the game,  
[00:41:18] it becomes much clearer who's more likely to win or lose under your expert data distribution.  
[00:41:24] I didn't understand the significance of why this way of thinking about value is  
[00:41:29] especially relevant to the expert data. It is not relevant to the expert data.  
[00:41:32] It's true for any data that you trained it on. If you were to learn tabula rasa, you would also  
[00:41:37] expect this to fall out. Imagine you're vibe coding AlphaGo. You gather some expert datasets  
[00:41:48] from KataGo online, or you have a dataset of human players, and you train this model.  
[00:41:54] It turns out this model is already a pretty good Go player.  
[00:41:56] It will most likely beat most human players. If you just take this policy recommendation  
[00:42:02] and take the argmax over these probabilities—if you take the argmax and just take this action  
[00:42:12] as your Go play—it'll be a very fast Go player that doesn't think in terms of reasoning steps.  
[00:42:18] It just shoots from the hip, and it'll be a very strong Go player.  
[00:42:21] This is already quite miraculous if you think about how ten neural network layers,  
[00:42:26] maybe under 3 million parameters, can already do something that impressive. You can start  
[00:42:35] this way. It's important when implementing this to verify that this is probably true.  
[00:42:39] It's good to verify that your Go rules are implemented correctly and that you  
[00:42:43] can run these simulations relatively quickly. Just as a checkpoint, you want to make sure  
[00:42:51] you can actually do this basic step before you try to layer on more complex things like search.  
[00:42:58] But we can do a lot better than taking the raw neural network and playing the moves.  
[00:43:05] So let’s apply the neural network to improve Monte Carlo tree search.  
[00:43:10] We start with our root node, and we now have a four-step iterative process to do MCTS.  
[00:43:24] This tripped me up when I was first reading the paper and trying to understand it.  
[00:43:29] Essentially what we're going to do is choose a number of simulations, and this number varies.  
[00:43:40] It can be somewhere between 200 and 2,048. I believe in the AlphaGo vs. Lee match,  
[00:43:47] they used tens of thousands of simulations per move because they really wanted to boost  
[00:43:50] the strength of the model as much as possible. But in training, you don't actually need too many.  
[00:43:55] KataGo, I think, uses something in this order as well.  
[00:43:58] Do you know if they used… If you watch the documentary,  
[00:44:00] they had a laptop out during the game. They didn't use the laptop itself. It was on some—  
[00:44:04] It was on some TPU pod, I think. Honestly, kind of unfair. Lee is  
[00:44:11] not using 1E22 FLOPS to do a move. Fair enough. Interestingly, modern Go  
[00:44:18] bots don't need that much compute at test time. What we'll find out, as we talk about how the  
[00:44:25] MCTS policy improvement works, is that over time the raw network actually takes  
[00:44:31] all of the burden of that big TPU pod and just pushes it into the network.  
[00:44:35] You can do all of that work with one neural network forward pass.  
[00:44:40] The TPU pod will always add the extra oomph on top, and that's what they wanted for the match.  
[00:44:46] We're going to pick this number of simulations thing, and for every simulation, we're going  
[00:44:51] to do several things simultaneously. We're going to see which moves are  
[00:44:56] the best in the current tree. We're going to add extra leaves  
[00:45:01] to the tree if we get to a point where we need to add a leaf, and we're going  
[00:45:04] to update the action values for the tree. Every simulation involves this four-step process:  
[00:45:13] selection, expansion, evaluation, and backup. At the beginning of our Monte Carlo tree search,  
[00:45:29] our tree is very basic. It only has the root node,  
[00:45:32] or our current board that our AI wants to play at. We're basically going to select  
[00:45:39] the best action for this. When this root node is created,  
[00:45:43] we also know that we can evaluate it under our neural network and get the quantities Vθ,  
[00:45:50] as well as our probability over actions. And I’m going to say root.  
[00:46:00] For all of the actions here, we can create a bunch of children.  
[00:46:09] In this case, I'm drawing a 3x3 board with one missing, so there are eight possible  
[00:46:15] children associated with this root node. Each of these has an associated probability  
[00:46:34] of taking that action, so there's P₈, P₁, ... P₂, and so on. So at the beginning of our Monte  
[00:46:43] Carlo tree search, we have our root node, and we can initialize it with some children.  
[00:46:48] The policy network evaluated on the root node gives us—on a 3x3  
[00:46:52] board with one existing stone placed—eight possible children that this AI could take.  
[00:46:59] With each of the children, the policy network also gives us the probability of selecting that child.  
[00:47:04] The first step is to do the selection of the tree. Again, this is a very shallow tree.  
[00:47:08] All we have so far is essentially a tree of depth one.  
[00:47:11] Our first move is to select by maximizing, or argmaxing, the PUCT criterion, which is basically  
[00:47:18] Q(s,a) + CPUCT x Pₐ x (√N / (1 + Nₐ)). For each of these, Nₐ is zero for all  
[00:47:42] the actions initially. N is zero. So we're going to pick according to this.  
[00:47:52] Initially, the chosen action is most likely going to be biased towards  
[00:48:01] the highest-likelihood action, because these are uniform for every node.  
[00:48:07] Let's suppose P₁ was the highest-probability node, so you selected this one here.  
[00:48:13] Now you get to this node and you realize it's not a leaf node.  
[00:48:17] It's not a terminal game, so you cannot resolve the final resolution. The next  
[00:48:21] step is expansion. You will then run this board state through the policy network.  
[00:48:31] Note that this is the AI's move. The AI is making this move.  
[00:48:36] When we expand this tree, we're now thinking about what the human, or any opponent, might do.  
[00:48:51] When we evaluate the node here, we're going to evaluate it from the perspective of this player.  
[00:49:00] This node has possible actions that we could take, and we expand the leaf nodes here.  
[00:49:07] For each of these nodes that we could arrive at, we're going to now check how good they are.  
[00:49:18] From here, the human could play here, here, or here.  
[00:49:23] We're going to store Vθ for each of these, so Vθ of Node₁’, Vθ of Node₁’’, and so on.  
[00:49:46] We're basically using our neural network to make an intuitive guess of how good this  
[00:49:53] board is from the perspective of this player. Fortunately, because it's a zero-sum game,  
[00:49:59] it's easy to deduce that the value for this player at this step is just one minus  
[00:50:04] the value from the other perspective. It's easy to flip the search process  
[00:50:08] depending on which player you're at. This is the expansion step. You've taken a non-leaf node,  
[00:50:15] expanded it, and evaluated the value. This is essentially a quick guess  
[00:50:19] as to whether I'm going to win or not if I were to play to the end.  
[00:50:23] You can almost think about Vθ as a shortcut for searching to the end  
[00:50:28] of the tree, for any given simulation. This is essentially the evaluation step.  
[00:50:35] We're evaluating the quality of each of these boards.  
[00:50:39] In the original AlphaGo Lee, they did something kind of interesting.  
[00:50:43] They took this value and averaged it with the value of a real Go playout.  
[00:50:49] They actually played a real game from here all the way to the end.  
[00:50:55] I'm just going to draw this squiggly line to indicate some path.  
[00:50:59] They play this all the way to Tromp-Taylor resolution of a full board.  
[00:51:06] So this is a zero or one. They took this value and  
[00:51:15] averaged it with this one here. The formula was α x Vθ of some node  
[00:51:25] plus (1 - α) of a truly randomly sampled playout. You might be wondering how they play this out.  
[00:51:38] It would be very costly to do another search on this playout, almost like a tree within a  
[00:51:43] tree. They don't do this. Instead, they just take the policy network and play it against itself.  
[00:51:49] They use it as both players, and they just play it all the way to the end.  
[00:51:52] This helps ground the estimates here in reality because you can get a single-sample  
[00:52:00] estimate of whether you win or not. In the endgame, where the board is  
[00:52:04] almost resolved, this becomes quite useful because the play according to the policy will  
[00:52:10] most likely decide a pretty reasonable guess of the game, so you're not facing a problem  
[00:52:15] where this becomes untethered from reality. It turns out this is totally unnecessary.  
[00:52:20] In all subsequent papers after AlphaGo Lee, they got rid of it.  
[00:52:24] In my implementation, I did the same, and it speeds things up a lot because you don't have to  
[00:52:28] roll these games out on every single simulation. Okay, just to reinforce my own  
[00:52:34] understanding and re-explain it. For the audience, by the way, in case it's not  
[00:52:39] obvious, the P there in the select, that is the probability coming from the network in this case.  
[00:52:44] Correct. The policy network here. Fundamentally, a simulation, just think of it as  
[00:52:54] rolling out one more node in the search process. Almost. A simulation is easy to think about  
[00:53:01] when the whole tree already exists. You just walk down the tree using the  
[00:53:06] PUCT selection criterion, and then you keep going. In AlphaGo, the data structure is such that we  
[00:53:16] begin with a tree that basically only has depth one—its only children—and you want to iteratively  
[00:53:23] build out the tree as you're also selecting actions down the tree. That's the core thing  
[00:53:28] here. Because Go is such a combinatorially complex game, you cannot afford to build  
[00:53:32] the tree in advance and then search it. You must search while building the tree.  
[00:53:38] Let me finish up with the last step, which is the backup.  
[00:53:41] Once you've scored these things, the Q value assigned to the node here for taking this action  
[00:53:50] is just the average across your evaluated values. You take a running mean over all the simulations  
[00:54:01] you've taken, averaging the values of the children nodes.  
[00:54:05] That's the backup step, and once you evaluate this, you can recursively go back up.  
[00:54:09] If you know the action value of this node, you can then take the average on its parent, and so on.  
[00:54:16] You have this four-step process: 1) You're choosing the best action you know of so far.  
[00:54:21] 2) You may run into a node you haven't been to before, so you need to grow the tree a bit. 3)  
[00:54:28] You run it through the network to guess whether you're going to win or not. 4) You walk all the  
[00:54:32] way back up to the root node to update your values on what the best moves are.  
[00:54:38] As you do this iteratively, because you're always selecting according to this criterion,  
[00:54:46] you're always going to be selecting the best action you think at any given branch.  
[00:54:51] The final visit counts of how often you chose these things will reflect  
[00:54:57] your correct policy distribution as induced through this search process.  
[00:55:03] The visit count we stored in the node earlier actually becomes the vote for which action  
[00:55:08] we should finally select. As a test of understanding,  
[00:55:14] it's worth thinking a little bit about whether we could make this even simpler.  
[00:55:18] Could we actually maybe even get rid of this one and still make the thing work?  
[00:55:24] Recall that when you do an expansion and then an evaluation at this node, you are checking the  
[00:55:30] win probability of each of the child nodes. So if this one is one and these are zero,  
[00:55:37] you do know something about which action might be better to take.  
[00:55:42] Why would you still need this, right? Why not just normalize the values into  
[00:55:48] a distribution and call that your policy distribution? This is fine.  
[00:55:53] You can do this, and it probably does work. But in practice, having a single forward pass  
[00:55:59] that gives you a pretty good guess is how the breadth is pruned out. There is a duality here.  
[00:56:10] It would be weird if the policy recommended an action that disagreed with the value.  
[00:56:15] If a policy said this was very high probability, but this one said it was a low value,  
[00:56:20] then there's something fundamentally wrong between your policy head and your value head.  
[00:56:25] They are linked, and you probably could get rid of this if you came up with a different way to  
[00:56:29] recover it from just the value evaluations. Right. Just to make sure I understand, the  
[00:56:36] reason you don't do that is so you don't have to do 360 independent forward passes to say, "Okay,  
[00:56:41] here's the value of everything. Let's argmax over it." Instead, you can just do one forward  
[00:56:44] pass and get the probabilities of all of them. You can usually batch these somewhat efficiently,  
[00:56:52] so it probably isn't a huge computational burden in practice.  
[00:56:55] But yes, you would have to pass up to 361 boards into a single mini-batch update to  
[00:57:02] evaluate all the values, then normalize them. There's actually a more important reason why  
[00:57:08] we still do this, which is how Monte Carlo tree search is used to feed back on itself  
[00:57:13] and recursively improve its own predictions and search capabilities.  
[00:57:18] That's where having this as an explicit entity you're modeling, rather than an implicit  
[00:57:23] normalization over your value, is a good idea. Makes sense. Okay.  
[00:57:28] We talked about the simulations. What you end up with as you roll out the number of simulations  
[00:57:33] is a tree that looks like… I'm drawing a very low-dimensional version of this.  
[00:57:41] Of course, in the real game, it's much more high-dimensional.  
[00:57:45] You'll end up with a tree structure that has a lot of leaves that terminate and are not visited  
[00:57:54] again because their value is deemed to be too low. But along one path, there will be a set of actions  
[00:58:00] with very high visit counts that gravitate towards that one set of decisions as you increase N.  
[00:58:09] This is the mental picture of what the tree in Monte Carlo tree search looks like.  
[00:58:13] You should contrast this with an exhaustive tree like in tic-tac-toe, where there are nine actions,  
[00:58:20] then eight, then seven and six, and so it's a nine-factorial-sized tree.  
[00:58:26] The Monte Carlo tree search in Go is very sparse.  
[00:58:29] It only considers the paths that you've expanded children nodes on.  
[00:58:36] Now that we have the search algorithm that applies the value function as well as the policy function,  
[00:58:44] we can talk about how the Monte Carlo tree search algorithm can act as an improvement  
[00:58:51] operator on top of these guys here. Twenty years ago, Jane Street's data  
[00:58:55] center fit in the corner of an office. Ron Minsky, who co-leads the tech group  
[00:59:00] there, told me about how it all got started. One of our compute clusters we called The Hive,  
[00:59:04] and I remember the first version of the Hive was literally like six Dell boxes stacked on  
[00:59:08] top of each other at the end of the row. And the trading systems themselves we also  
[00:59:12] had there because we actually wanted the ability to make sure we could turn the damn thing off.  
[00:59:17] I mean there were ups and downs, like literally at some point you know,  
[00:59:20] one of the people who was cleaning the office unplugged one of the trading systems in the  
[00:59:24] middle of the day as they were vacuuming. So, you know, in the end it is in fact  
[00:59:28] better to have it all in a data center. Jane Street's data centers have come a long  
[00:59:31] way since those sixth Dells, and I got to tour one of them in Texas with Ron and Dan Pontecorvo,  
[00:59:35] who leads Jane Street's physical engineering team. You know, these cabinets, these GB300 cabinets,  
[00:59:40] consume at peak about 140 kW each. Compare that to traditional air cooled, you're talking about  
[00:59:45] 10 to 40 KW? It's a lot more. We got deep into the details  
[00:59:49] of running one of these data centers. Things that I had never considered before.  
[00:59:52] It's filled with a liquid, a mix of deionized water  
[00:59:55] and propylene glycol, 25% of propylene glycol. That’s to inhibit any bacteria or algae growth.  
[01:00:02] I don't love the world where we have to worry about bacteria growing in our servers.  
[01:00:06] I got to see way more of what actually happens in a data center than I've ever seen before.  
[01:00:10] Jane Street was willing to literally pull up the floorboards and take out the racks and take me to  
[01:00:14] the back where all the chillers are. You can check all of this out at  
[01:00:18] JaneStreet.com/dwarkesh where we posted the full tour.  
[01:00:23] We now talk about the RL part of how this thing gets stronger by playing itself.  
[01:00:30] Let's say we play a game. You make a move. The AI will compute the search,  
[01:00:43] and this is the visit count distribution. Let's say this is your initial policy  
[01:00:49] recommendation at this node. After MCTS, it gets more  
[01:00:56] confident about one of these actions. Maybe the distribution looks a bit more  
[01:01:01] peaky like this based on the search. Of course, you can tune the search  
[01:01:05] process so that it ends up more diffuse, but that's probably not a good idea.  
[01:01:08] MCTS should get more confident about specific actions over others.  
[01:01:12] It might place a lot of weight on other actions initially, and then as you increase  
[01:01:17] the number of sims, it should converge to a very peaky distribution. Let's call this π.  
[01:01:25] Let's wrap this in an MCTS operator of (a | s). After applying the MCTS process, your policy  
[01:01:38] recommended distribution looks like this. It’s a bit more peaky than the previous one.  
[01:01:43] Then you take the argmax, or maybe you just sample from this.  
[01:01:47] It doesn't have to be the argmax. You make your move, throw away the  
[01:01:51] tree, and begin anew on the next move. Again, you compute a new distribution.  
[01:02:08] Initially, maybe your guess looks like this, and then you refine it through MCTS.  
[01:02:16] There should be one more X on the board, right? I'm sorry, that's correct, yes. Something that  
[01:02:22] looks like this. On every move, you have your initial guess from your policy network.  
[01:02:32] Then the search process, which combines your policy network and your value network,  
[01:02:35] arrives at a more confident action that you take, and so on and so forth.  
[01:02:40] Then the game ends, and one person wins and one person loses.  
[01:02:46] The beauty of how AlphaGo trains itself is that it can actually take this final search  
[01:02:53] process—the outcome of the search process—and tell the policy network, "Hey, instead of having  
[01:02:59] MCTS do all this legwork to arrive here, why don't you just predict that from the get-go?  
[01:03:04] Why don't you not use this guess and predict this to begin with?"  
[01:03:07] If you have this guess to begin with in your policy network, then MCTS has to do  
[01:03:11] a lot less work to get things to work. If we draw a test-time scaling plot…  
[01:03:18] Let's say this is the number of simulations. At zero simulations, your implicit win  
[01:03:26] rate is here. If you just take  
[01:03:33] this raw action, this is what your win rate is. Let’s say we increase the number of sims, maybe  
[01:03:39] you have a win rate curve that looks like this. When you search for 1,000 simulation steps,  
[01:03:49] that gets you to a policy here that gets you to here, which is great.  
[01:03:56] But if you were to distill this MCTS policy network back into your shoot-from-the-hip policy  
[01:04:03] network, then you could actually start here. Let’s say this was zero, by distillation,  
[01:04:14] if you then spend another 1,000 sim steps, you actually get to here.  
[01:04:19] It's almost as if you could amortize the first 1,000 steps into the policy network instead of  
[01:04:26] the search process, then you could begin at a much better starting point and get a much better  
[01:04:30] result for the number of sims that you play. The sigmoid type nature of test-time scaling  
[01:04:36] as the number of simulations increases, the increase in win rate gets smaller.  
[01:04:41] Is that true even for the distilled network? That is to say, is there some gain where we  
[01:04:46] start from the distilled network and get these early gains again,  
[01:04:48] or is that just inherent to the nature of MCTS? To be honest, I actually don't know the test-time  
[01:04:53] scaling behavior of MCTS simulations. I believe it might be quite sensitive to  
[01:04:58] how strong this one is in practice. I'm just drawing a monotonically  
[01:05:01] increasing function that gets to one. Don't pay too much attention to the  
[01:05:05] shape of the curve. Just know that it's  
[01:05:06] monotonic with respect to sims. The idea of MCTS is very brilliant.  
[01:05:15] We got something better by applying search. Now, on our next iteration of updating this  
[01:05:22] network, we're going to train it to approximate the outcome of 1,000 steps of search.  
[01:05:28] Instead of starting here, we get to have our neural network start here, and then the  
[01:05:32] play gets stronger once we then apply another 1,000 steps on top of it. You can keep going.  
[01:05:37] The training algorithm for AlphaGo is to basically take the games where you've applied the search on  
[01:05:43] every move that the policy encountered—whether you won or lost, and that's quite important—and just  
[01:05:49] train the model to imitate the search process. There's an analogy to robotics,  
[01:05:55] which is the DAgger algorithm. First I'm going to draw a  
[01:06:00] schematic of the states: S₀, S₁, S₂, S₃. Let's say we took a series of actions in  
[01:06:10] an MDP to get a trajectory. These actions may be suboptimal. Maybe we lost at the end of this game.  
[01:06:25] There is a family of algorithms that basically take trajectories and relabel  
[01:06:31] the actions to better trajectories. Maybe a better action here would  
[01:06:35] have been to take A₀’. A better action here would  
[01:06:39] have been A₁’, and yet another one, A₂’, A₃’. What MCTS is doing is saying: you played this  
[01:06:52] game where you eventually lost, but on every single action, I'm going to give you a strictly  
[01:06:57] better action that you should have taken instead. It does not guarantee that you are going to win,  
[01:07:02] but it does guarantee that if you take these tuples as training data and retrain your policy  
[01:07:10] network to predict these actions instead of the original ones, you're going to do better.  
[01:07:15] This is very related to DAgger in robotics and imitation learning,  
[01:07:19] where you want to collect an intervention here. Even if you're in a not-great state—for example,  
[01:07:25] a self-driving car that veers off the side of the road—there is still a valid  
[01:07:28] action that corrects you and brings you back. Pedantic question, but is there a guarantee  
[01:07:35] that MCTS must be better than the policy? For example, you could imagine early on in  
[01:07:39] training, because MCTS is informed by the value network, that when the value network hasn't been  
[01:07:47] well-trained on finished games, MCTS is worse than a randomly initialized policy.  
[01:07:54] Is it just a heuristic that MCTS is better than the policy, or is there some guarantee?  
[01:07:59] In practice, it is a heuristic. It does work in practice, but let  
[01:08:04] me illustrate an example where MCTS can give you a worse distribution than your policy network.  
[01:08:09] This can often happen if your self-play algorithm has trained to a good point,  
[01:08:13] but then somehow it collapses because it's not trained on diverse data or something.  
[01:08:20] Let's say we have a board state where the policy recommendations are very good.  
[01:08:25] So Πθ (a | s) is great. But somehow, maybe because we're  
[01:08:33] playing a lot of games where the bots just resign instead of playing all the way to  
[01:08:37] the Tromp-Taylor resolution, they forget how to evaluate those late-stage plans.  
[01:08:43] Like in the case we showed with the corner play, maybe 100% of our training data in  
[01:08:48] our replay buffer has lost examples of how to evaluate the value function at those states.  
[01:08:54] You might end up in a scenario where your terminal value is very bad.  
[01:09:01] If the terminal values of the leaves are not good, then this will propagate all the  
[01:09:06] way up and cause your PUCT selection criteria and your backups to be off.  
[01:09:12] And then you end up visiting a very different distribution than what  
[01:09:15] your policy initially recommended. Also, if your number of sims is low,  
[01:09:20] you might have a variance issue where you just don't explore enough.  
[01:09:24] It's only guaranteed to converge when you take N to infinity.  
[01:09:29] Variance in your search process as well as inaccuracies in your  
[01:09:33] evaluation can definitely screw with the quality of your policy recommendation.  
[01:09:38] That's why it's not a guaranteed improvement. That is why I suspect AlphaGo Lee had the playouts  
[01:09:45] to the end in their training algorithm, so that they could ground this thing in real playouts.  
[01:09:50] In practice, what you could also do is, for 10% of the games, prevent the bots from  
[01:09:55] resigning and just say, "Resolve it to the end." That way you get some training data in your replay  
[01:09:59] buffer to really resolve those late-stage playouts that normal human players would not play to.  
[01:10:09] If you assume that the value functions are correct,  
[01:10:12] this is why MCTS gives you a better policy. It's a very critical chain of assumptions.  
[01:10:18] Assuming this is accurate, your search process should give you a better  
[01:10:22] recommendation than your initial guess. If you have a cold-started policy—if  
[01:10:27] you have an AlphaZero-type thing—really what's happening for the first few epochs  
[01:10:31] is that the policy is kind of useless. What you're really just doing is, "Hey,  
[01:10:34] let's play full games, and once we have played full games, for the preceding moves,  
[01:10:41] we'll have labeled who won and who didn't win." The loss for AlphaZero has two components:  
[01:10:50] how good is the policy relative to MCTS, and how good is the value prediction relative to  
[01:10:55] who actually won the game from this move. You can think of this being applied to  
[01:10:59] every single action or every single move. Really what's happening at the beginning of  
[01:11:03] AlphaZero training is just that we're trying to get the value function to actually predict  
[01:11:07] who will win the game if you find yourself in this state and you're this player. Functionally,  
[01:11:14] that's all that's happening. Later on, once that's well trained, now the policy is also improving.  
[01:11:19] Correct. There’s one trick I found to be pretty useful.  
[01:11:22] This is not a peer-reviewed claim, so take it with a grain of salt.  
[01:11:26] I found it useful in my own implementation to do the following.  
[01:11:30] You want to first make sure that this is good before you invest a lot of cycles doing MCTS.  
[01:11:35] It doesn't really make a lot of sense to do search on garbage value predictions.  
[01:11:41] You want to start at a good place where this works.  
[01:11:43] AlphaGo Lee does a very good thing where it just takes human games, you train on them, and it just  
[01:11:48] works. It totally works. You can also take an open-source Go bot, play it against itself,  
[01:11:53] generate data, and that also works. If you have some offline dataset that  
[01:11:59] has realistic, good play, you can easily learn the late-stage value functions pretty well.  
[01:12:07] That's what you need to start the search process. Sorry, can you just repeat that sentence one  
[01:12:10] more time? Sure. It's  
[01:12:12] quite easy to evaluate a late-stage Go game. When almost all the pieces are on the board,  
[01:12:18] it's almost like a decidable problem because there's lower and  
[01:12:20] lower uncertainty as to the depth of the tree. So most games played to the end by reasonable  
[01:12:26] people will be good training data to train a good value function at terminal parts of the tree.  
[01:12:32] Then, as you play more games, the search will back up good  
[01:12:37] values into the intermediate nodes of the tree. As you increase the amount of data, your value  
[01:12:42] head gets a good intuition of what is a healthy board state versus a not-healthy board state.  
[01:12:48] Those are much more subtle to judge in the mid-game than at the beginning or the end.  
[01:12:52] The most difficult part to score is not the beginning, because the beginning is obviously 0.5,  
[01:12:57] and at the end it's pretty obvious who's winning. The hard part that you want to learn in the  
[01:13:01] value function is who is winning in the middle. So this is actually very analogous to TD learning.  
[01:13:06] Yes. There's a beautiful connection to TD learning that we can talk about in a bit,  
[01:13:11] contrasting it with Monte Carlo tree search. You first want to get good value functions,  
[01:13:17] and expert data can give you a quick shortcut. I recommend for practitioners, just do that first  
[01:13:22] to initialize to a good starting point. If you want to do the AlphaZero thing or  
[01:13:26] KataGo tabula rasa learning, what you can try to do is play random games on a small  
[01:13:31] board. Just take a random agent. If you play 50,000 games, you'll actually learn a pretty  
[01:13:39] good value function as well. On a 9x9 board, you can see  
[01:13:43] enough of the common patterns with random play. If you train on both 9x9 and 19x19 data—and KataGo  
[01:13:52] proposed one of these architectures—there's pretty good transfer learning from the  
[01:13:56] value head evaluated at 9x9 to 19x19. Right, because this, unlike other games,  
[01:14:02] has very much a sense… There's not like a new kind of piece introduced  
[01:14:06] when you increase the size or something. If we take it to its limit and consider a  
[01:14:10] very tiny 4x4 Go board, if you play 50,000 games, you're going to have a lot of end  
[01:14:15] states that look like human play. It's just Tic-Tac-Toe at that point.  
[01:14:18] If you broaden this a little bit to 5x5 or 9x9, it's not unrealistic to imagine that  
[01:14:24] purely random play will generate pretty reasonable-looking boards.  
[01:14:29] You can score those pretty easily. That is what gives you the bootstrapping  
[01:14:32] to then improve your policy with search. But it's very critical that MCTS has  
[01:14:37] accurate value estimates. You need to ground the value.  
[01:14:41] Ultimately, MCTS will fall apart if you don't have a grounding function for the value.  
[01:14:47] I'd be curious how much compute you save by training the value and policy on the same network.  
[01:14:53] Because they share the same representations, how much more efficient is learning?  
[01:14:59] We've just talked about how they're making similar predictions, or they  
[01:15:02] should be in line with each other. So I'd be curious if you're halving  
[01:15:07] the amount of compute you have to do by keeping them in the same network.  
[01:15:10] AlphaGo Lee, the original AlphaGo paper, had two separate networks.  
[01:15:14] In all subsequent papers, they merged them into two heads, and presumably this saves compute.  
[01:15:19] But answering that question in a rigorous scientific way is  
[01:15:23] a simple question that in practice, if you really want to chase the question down to its limit,  
[01:15:29] takes quite a bit of work to really resolve. Intuitively, yes, they share a lot of  
[01:15:34] representations. As we mentioned,  
[01:15:38] your policy network and your value network, when doing evaluations, should agree.  
[01:15:43] There really should be this consistency between them.  
[01:15:46] Tell me if this is the wrong way to think about it.  
[01:15:49] When I learn how an LLM works and how simple RLVR is as an algorithm,  
[01:15:58] I'm stunned by the kinds of things it can do. It can learn how to build very complicated code  
[01:16:04] repositories simply from getting a yes or no. Here, if you understand it more deeply, just  
[01:16:11] predicting MCTS, AlphaGo seems less impressive in retrospect the more you understand it.  
[01:16:19] You're putting in a lot of bias by telling it how it should titrate exploration as things go on.  
[01:16:26] You're building this very explicit tree search for it.  
[01:16:30] I don't know if you share that intuition where the more you understand it, the less  
[01:16:34] impressive the accomplishment in 2017 seems. I personally disagree. I think they're  
[01:16:41] profound for different reasons. I don't understand the LLM RL  
[01:16:45] enough to comment on it on your podcast. But why is AlphaGo a profound accomplishment?  
[01:16:53] It's worth stepping back a little bit. It is different from modern RL,  
[01:16:57] and we can talk a little bit about some of the algorithmic choices there.  
[01:17:01] I think the most profound thing here is that a 10-layer neural network pass, basically  
[01:17:12] 10 steps of reasoning… Of course, the reasoning is not just one trail of thought.  
[01:17:16] It could be distributed representations and a lot of thoughts going on at the same time.  
[01:17:20] But by construction, let's say a 10-layer neural network can only do 10 sequential  
[01:17:24] steps of thinking. 10 steps of neural network parallelized distributed-representation thinking  
[01:17:31] is able to amortize and approximate to very high fidelity a nearly intractable search problem.  
[01:17:40] This was a breakthrough that I think most people don't even fully comprehend today,  
[01:17:46] how profound that accomplishment is. This is what also girds AlphaFold,  
[01:17:52] for example, where you have a very, very difficult physical simulation process where  
[01:17:58] you would need to roll out as so many microscale simulations, and yet 10 steps of a somewhat small  
[01:18:04] neural network can somehow capture what feels like an NP-class problem into a single problem.  
[01:18:15] It actually makes me wonder if our understanding of problems like P=NP,  
[01:18:20] or these fundamental computational hardness problems, is incomplete.  
[01:18:26] Obviously, it's not a proof of P=NP, but there's something to it that is very disturbing,  
[01:18:34] where what felt like a very hard problem can fall to a very simple macroscopic solution.  
[01:18:40] That is a very interesting insight, that a lot of problems which are proven to be NP-hard—I don't  
[01:18:47] know if Go is proven to be NP-hard, but protein folding, et cetera—neural networks can solve.  
[01:18:54] They're NP-hard in the worst case, but we're usually not concerned about the worst case.  
[01:18:58] These problems usually have a lot of structure to them.  
[01:19:01] I think the question we should be asking ourselves is about how we've been formulating solutions to  
[01:19:08] NP-hard problems in worst-case complexity. I wouldn't say this solves Go.  
[01:19:14] It doesn't give us an exact solution of the optimum, but in practice, it is extremely useful.  
[01:19:20] The same thing has been shown in AlphaTensor and AlphaFold.  
[01:19:24] Yes, there is a very hard problem that, in the worst case, seems intractable, and yet we're able  
[01:19:28] to make almost arbitrary amounts of progress. In the limit, what might this look like?  
[01:19:36] If you want to simulate something very complex like weather, or predict the future—do we live  
[01:19:42] in a simulation or not—the computing resources you need to build a very complex simulation might  
[01:19:48] be much smaller than you think, based on our ability to amortize a lot of that computation  
[01:19:54] into the forward pass of a single network. To me, AlphaGo was the first paper that  
[01:20:00] really showed this profound level of simulation being compressed into a small amount of compute.  
[01:20:07] I feel totally not qualified on the computational complexity or the math to comment on this, but I  
[01:20:14] wonder if there's an important role of chaos here. What is the problem with weather,  
[01:20:22] and why does it take 10x the amount of resources to predict weather a day out,  
[01:20:27] and continually so for every additional day out? It's because it's a chaotic system, so small  
[01:20:32] perturbations can totally change the final estimate as time goes on.  
[01:20:39] I guess you would expect that for Go and protein folding as well.  
[01:20:42] Here's an analogy to weather that might be relevant in Go. Here's our current board state.  
[01:20:55] Given what we know about both players, what is the exact board state in the future?  
[01:21:03] This is extremely sensitive to initial conditions. A single stone placed here can disrupt  
[01:21:08] the entire prediction. This is hard. Intuitively, this is the chaotic problem.  
[01:21:14] Yet somehow, we can predict who's going to win. This captures a lot of possibilities.  
[01:21:26] There's a more macroscopic quantity that we really care about, which is the  
[01:21:29] average or expectation or some sort of global macrostructure over a lot of possible futures.  
[01:21:37] In weather, it could be the same thing. We don't exactly care what the  
[01:21:42] velocity of wind 6,000 feet above a specific latitude and longitude is.  
[01:21:48] We care where the hurricane is, and things like that.  
[01:21:52] In chaos, there's the classic Lorenz attractor. If you start anywhere on the Lorenz attractor,  
[01:22:00] you don't know where you're going to end up, but you do know that the thing looks like this.  
[01:22:05] There's a kind of beauty here. Sometimes we don't necessarily  
[01:22:08] care about the microscale things. We actually care about the macroscopic  
[01:22:11] structure, and these things can be predictable. Contrast that to something like a hash function,  
[01:22:18] which is also incredibly dependent on initial conditions but doesn't have a  
[01:22:21] macrostructure, or at least hopefully doesn't, if the algorithms work.  
[01:22:24] One would hope. There's no equivalent of  
[01:22:28] a value function or broadly how the weather is going to be that's interesting there.  
[01:22:33] It's really just about what the board is going to look like exactly 100 moves from now exactly.  
[01:22:39] Intuitively, that seems correct. This is also out of my area of expertise, but I  
[01:22:46] find it interesting that the tools of cryptography and hashing have also not been able to prove  
[01:22:56] that you cannot come up with fast approximations. You cannot come up with fast approximations.  
[01:23:02] If they were able to do that, then you could prove P is not equal to NP.  
[01:23:05] In fact, we know that there's structure in many cryptographic  
[01:23:08] protocols, obviously RSA cryptography. There is structure, and that structure  
[01:23:12] is what quantum computers exploit to break them. Reiner has a very interesting blog post, which  
[01:23:19] we've talked about in the episode, where he points out that if you look at a high level at what  
[01:23:24] cryptographic protocols look like and what neural networks look like, they're extremely similar.  
[01:23:29] You have sequential layers of jumbling information together.  
[01:23:35] There's a convergent evolution in the algorithms.  
[01:23:38] In cryptography, you want the final state to be incredibly sensitive to initial conditions,  
[01:23:43] so that it comes out looking jumbled if you change anything.  
[01:23:48] In neural networks, you similarly want everything to be dependent on all the information, because  
[01:23:53] you want to process all the information and consider how it relates to itself.  
[01:23:56] You have the maximum power of a neural network at the edge of chaos.  
[01:23:59] I think there are some research papers from Jascha Sohl-Dickstein on this.  
[01:24:04] There's something quite fundamental about chaos that's not just hopeless noise.  
[01:24:05] There's something useful in chaotic systems, at least at that boundary.  
[01:24:17] But this is just thinking about it as a philosophy.  
[01:24:19] I don't know the math well enough to comment on it.  
[01:24:25] We’ll talk about LLM RL in a little bit, because there’s some connection there,  
[01:24:28] but let's go back to MCTS. What is it doing? Crucially, it is not saying that we're going to  
[01:24:36] increase the probability of winning directly. It's not going to upweight all actions that won  
[01:24:42] and downweight all actions that didn't win. Importantly, what it is doing is saying:  
[01:24:47] for every action we took, we did a pretty exhaustive search on MCTS to see if we could  
[01:24:54] do better, and we're going to make every action that we took better by having the  
[01:24:58] policy network predict that outcome instead. This is a very nice idea because you have one  
[01:25:04] supervision target for every single action. The variance of your learning signal is very  
[01:25:10] low compared to the alternative naive RL thing. Let's consider a very naive algorithm that looks  
[01:25:18] a lot more like modern LLM RL today, where we do something like take the winner of a self-play  
[01:25:25] game and encourage it to do more of that. It's worth thinking a little bit about what  
[01:25:31] alternatives we could use to train self-play agents instead of MCTS.  
[01:25:35] We use a lot of LLM-style RL these days. Is that relevant? Could we do that instead? Suppose we  
[01:25:44] have a very naive algorithm where we take a league of agents of different  
[01:25:48] checkpoints and play them against each other. For the games where a single player wins,  
[01:25:54] we reinforce those actions up and retrain the policy network to imitate those winners,  
[01:26:01] instead of the MCTS objective. Let's say you have a chain of  
[01:26:10] actions that led to a win, and you have a matchup between two agents that are basically the same.  
[01:26:19] Assume policy a (Πₐ) and policy b (Πb) are evenly matched, so their true win rate is 50%.  
[01:26:34] Let's say you play 100 games, and each game lasts 300 moves.  
[01:26:47] You're doing some sort of evolution strategy or some way to perturb these  
[01:26:52] things to get them to do different things. Or maybe you don't, and you just play them  
[01:26:55] against each other to see that occasionally one might have a better strategy than the other.  
[01:27:00] Let's say policy a wins 51 games and policy b wins 49.  
[01:27:13] This is just due to random luck, or maybe you perturbed policy a  
[01:27:16] in some way that let it do this. Just to have a very simple model,  
[01:27:19] let's pretend that for 50 of the games, they played exactly equally.  
[01:27:34] In the one game where a won, it played slightly differently.  
[01:27:37] It made one critical move that normally it would have done differently, but due to some  
[01:27:42] exploration or random noise, it happened to make a smarter move than it did previously.  
[01:27:46] So you have one true supervision signal for your policy network, and then you have 99 games  
[01:27:58] times 300 moves for which imitating those actions gives you exactly the same policy you had before.  
[01:28:07] The scale of your variance is actually very bad, because you only have one label out of  
[01:28:12] this enormous dataset of supervision actions where you want… Actually, let me clarify a little bit.  
[01:28:20] We're talking about how the good move, the out-of-distribution move, is a small fraction  
[01:28:24] of all the moves that are played across all the games on which you'd want to train.  
[01:28:29] This, of course, reminds me of how LLMs are trained with policy gradient methods.  
[01:28:36] When Karpathy was on the podcast, he called it like "sucking supervision through a straw".  
[01:28:42] It's interesting that this thing you're saying—which would be intractable and prevents  
[01:28:45] you from actually getting beyond a certain level in Go—is just by default how LLMs are trained?  
[01:28:51] Right. This is not to say it doesn't work. If you imagine increasing the number of games  
[01:28:57] to millions of samples, you actually can get some meaningful supervision samples,  
[01:29:03] so long as you find a way to mask out the supervision from these guys.  
[01:29:08] This is where things start to get pretty related to RL in terms of advantage and baselines.  
[01:29:14] Let's look at the gradient variance of a very naive approach—I'm going  
[01:29:21] to call it gradient RL—that's basically the sum of rewards.  
[01:29:52] The sum of rewards is the return. In our naive setup here,  
[01:29:56] we only have an indicator variable for the return, where either you won or lost.  
[01:30:05] In the case where you lost, your gradient is zero, so you don't train on those examples,  
[01:30:10] and when you won, you try to predict those things.  
[01:30:13] You can think about this setup as a special case of this general formula here.  
[01:30:20] The trouble here is that this is very high variance.  
[01:30:24] When you multiply these terms out to compute the variance of the gradient,  
[01:30:34] it's equal to the expectation of… Just for simplicity, we can pretend this is on average zero  
[01:30:45] or something if you're centering it at no signal. The variance here basically means that you're  
[01:30:53] taking the square of this product term. You end up with  
[01:30:58] a term that grows quadratically with T. When you have a setup like this, this thing acts  
[01:31:08] as a coupling effect on top of these terms here. Let's actually map this to an LLM case,  
[01:31:17] and we can answer why LLMs only do one-step RL instead of a multi-step RL scenario.  
[01:31:25] In LLMs, you have a decoder that might predict some words like "hello world".  
[01:31:34] In current LLM RL, they treat this entire sequence as a single action, aₜ, and big T is just one.  
[01:31:44] It's true that because of how transformers are formulated through the product of conditional  
[01:31:51] probabilities, the log probability of the whole sequence is equal to the sum of the  
[01:32:03] probabilities of individual tokens. In this case, I would say something  
[01:32:10] like log(hel) + log(lo) + log(world). This is true, and if this term were one,  
[01:32:27] then they would be the same thing. However, when you're sampling, if you  
[01:32:32] have a reward term assigned to every specific token, now you have these interaction effects  
[01:32:39] between the cross-multiplication of these terms and these terms.  
[01:32:43] The problem becomes, how do you ascribe the credit associated with  
[01:32:47] every episode to all these different terms? The thing I'm confused on is what it would  
[01:32:52] even look like to do it that way in LLMs, because you only get a reward at the end of the episode.  
[01:33:01] You could imagine a reward that says, "I'm going to give you some process supervision where you get  
[01:33:07] a reward for each of these actions on every step." Okay, so you're saying if instead of doing it  
[01:33:13] that way… Well, the way you've written it, it would be a sum at the end anyway,  
[01:33:18] so they wouldn't have to be multiplied. But you're saying instead of doing it  
[01:33:22] that way, you would just add up these process rewards at the end and then  
[01:33:26] treat that as one single reward signal? Correct, for one single log prob action.  
[01:33:29] But isn't that how it's written to begin with anyways? The sum of the rewards?  
[01:33:36] The thing that's a little bit hidden here in the math is that we’re assuming that when you  
[01:33:39] decompose the problem into a multi-step problem, you're now introducing correlations between your  
[01:33:45] actions through the computation of this guy. If you separate these things out,  
[01:33:52] this will magnify the variance of this one. In the case where you don't separate it out,  
[01:33:57] if you just have T=1, you have a single estimate of log prob and a single estimate of reward. This  
[01:34:07] term still shows up. In LLMs, the naive REINFORCE estimator looks a bit like the return of the  
[01:34:15] single action… It looks kind of like this. This is the basic form here, but it's still  
[01:34:30] a contributor to variance. You want to make sure that,  
[01:34:35] similar to how in this case we were training on a lot of neutral labels, you're sort of  
[01:34:41] penalizing the labels that don't help and only rewarding the ones that actually make you better.  
[01:34:47] Intuitively, the analogy is: can we find a term in our training objective such that  
[01:34:52] it’s actually discouraged from doing this, or these don't have any effect on the gradient,  
[01:34:58] and this has an effect on the gradient? If you applied that there, the only thing  
[01:35:03] you could do is eliminate 49 of the games. At least the way you have it written there,  
[01:35:11] it would be 51 times… Actually, the optimal case is to discard  
[01:35:17] all of these moves, and only get a gradient on that single move that you got better on.  
[01:35:23] How would you do that? This is a pretty tricky problem in practice.  
[01:35:28] This is where advantage estimation happens in reinforcement learning.  
[01:35:32] You want to subtract a term from your multiplier. Instead of an indicator function of one and zero,  
[01:35:46] you want something that behaves like a zero for all of these guys, and then a one for these ones.  
[01:35:52] You could do that if you can say, "Hey, I won this game, so this is slightly  
[01:35:58] above baseline performance." Well, you won a lot of games.  
[01:36:03] But you don't know which ones let you win because they were truly better versus winning by accident.  
[01:36:07] How would you design a baseline where it's truly better?  
[01:36:10] This is where in RL people use things like TD learning to better approximate the quality  
[01:36:16] function, the Q that we mentioned earlier. You can try to subtract that from your return.  
[01:36:23] Ideally, what you really want to do in RL is push up the actions that make you better  
[01:36:30] than average and push down the actions that make you worse than average. They call this  
[01:36:36] advantage. There are multiple ways to compute it. I highly recommend John Schulman's "Generalized  
[01:36:41] Advantage Estimation" paper as a good treatment on how to think about various ways to compute it.  
[01:36:49] At the end of the day, you want to reduce variance by trying to make this smaller,  
[01:36:54] so it doesn't magnify the variance of this one. That makes sense. This requires you to have  
[01:36:59] a very good estimate of what average performance from a state would look like.  
[01:37:03] This gets us back to the value function thing we were talking about earlier.  
[01:37:08] Keep in mind that this model-free RL setting is trying to solve a credit assignment problem  
[01:37:14] where you don't know which actions were actually good and which ones were bad.  
[01:37:18] Monte Carlo tree search is doing something very fundamentally different.  
[01:37:20] It's not trying to do credit assignment on wins.  
[01:37:24] It's trying to improve the label for any given action you took.  
[01:37:30] We can actually think about a completely different algorithm called neural fictitious self-play,  
[01:37:34] which was used to great effect in systems like AlphaStar and OpenAI's Dota.  
[01:37:41] Let me talk a little bit about how you can unify some of these RL ideas in the model-free setting  
[01:37:47] as well as the self-play setting. What happens if you don't have  
[01:37:53] the ability to easily search a tree? In Go, it's a perfectly observable game.  
[01:37:58] You can easily construct a pretty deep tree that completely captures the game state.  
[01:38:02] In a game like StarCraft where you don't have complete control over the binary,  
[01:38:06] it's a little bit hard to do this, and I'm not even sure if it's a deterministic game.  
[01:38:11] That makes this difficult from a data structures perspective.  
[01:38:16] What is done instead is that the basic idea of supervising your  
[01:38:22] actions with a better teacher is still there. We’re going to talk a little bit about how neural  
[01:38:30] fictitious self-play works. It's the same idea. We're going to come up with better labels for  
[01:38:44] each of the actions we took, just like in MCTS. But how do we derive the better labels? In MCTS,  
[01:38:57] we perform search. Assuming we have a good value function, the search will give us  
[01:39:02] a better result than our initial guess. In a game where you can't easily simulate  
[01:39:08] a search process, what they do instead is train what's known as a best response policy.  
[01:39:18] You fix your opponent. Let's say you're currently training Πₐ against a strong opponent, Πb.  
[01:39:28] In StarCraft, maybe these are the Zergs and you're playing Protoss or something.  
[01:39:34] You fix your opponent, and you treat this as a classic model-free RL algorithm,  
[01:39:39] where your goal is just to beat this guy. Here you use your standard TD-learning-style  
[01:39:44] tricks, or use PPO or any model-free RL algorithm to  
[01:39:49] try to hill climb to winning against this player. You have a reward function where the return is one  
[01:40:02] if it wins against Πb, and zero otherwise. This is no longer a self-play problem.  
[01:40:09] It's just a fixed opponent, and you're trying to maximize a score against them.  
[01:40:19] You have a fixed environment where all you care about is beating this guy.  
[01:40:25] Once you have a good policy that you train with your favorite model-free RL algorithm—PPO  
[01:40:31] or SAC or V-MPO—you now have a good policy that gives you a good label for what this  
[01:40:40] one should do when playing against that player. When you train multiple best response policies,  
[01:40:46] you can basically distill the RL algorithms into the labels for a given opponent.  
[01:40:52] You might have a best response policy against πb, and then maybe you have  
[01:40:55] a league of opponents like πb, πc, πd. You're going to take the best response  
[01:41:04] policy that you train against each of these fixed opponents, and supervise  
[01:41:09] them with the label that this one would provide. This is almost like a proxy for your MCTS teacher.  
[01:41:16] Instead of an MCTS teacher, you use a model-free RL algorithm to find the best search action  
[01:41:22] that you could do to beat your opponent. Then you're distilling the policy here  
[01:41:29] into what's known as a mixed strategy, where it's trying to average across all  
[01:41:34] possible opponents you could play against. This is what gives you something that  
[01:41:37] can do no worse than an averagely selected opponent from the league.  
[01:41:43] This gets around the problem of having to derive a teaching signal from MCTS, but fundamentally  
[01:41:48] it's still about relabeling your states with better actions so that they improve your policy.  
[01:41:54] Just to make sure I understand, if you win a game against this other policy,  
[01:41:59] you reinforce all the actions on that trajectory. Yes. Here you can use a number of algorithms like  
[01:42:05] PPO, V-MPO, or even Q-learning if you want. The specific algorithm here is usually a  
[01:42:15] model-free thing because you don't have search, but there's an interesting connection between  
[01:42:19] MCTS and Q-learning that I want to bring up. In MCTS, you have a tree, and through the  
[01:42:30] resolution of your value function at the approximate leaves of the tree,  
[01:42:36] you can back up through many sequences and obtain some sort of mean value estimate.  
[01:42:44] Your Q is derived from the average of a bunch of simulations.  
[01:42:49] In model-free algorithms, there's often a component of estimating a Q value.  
[01:42:58] Q values are often learned through TD learning, although in PPO,  
[01:43:01] the way they do advantage estimation is not necessarily through a Bellman backup.  
[01:43:05] In Q-learning, there's this very cool trick where Q(s,a) is backed up as r plus some discount factor  
[01:43:19] times the max over a, Q of your next step. Intuitively, if you have an MDP and this is  
[01:43:33] terminal, it's saying that the best action you can take at this state is equal to the  
[01:43:46] reward you get for taking this action, plus the best that you can do at the next state.  
[01:43:52] There's a recursive, dynamic-programming property of MDPs, and you can train neural  
[01:43:57] networks to basically enforce this consistency. You can say, "Well, once I know the Q value of  
[01:44:04] this action, I can then use that to compute something about the Q value for the next."  
[01:44:09] Earlier I was like, "Hey, why are we training policy?  
[01:44:11] Why don't we just train the value alone?" That is what this is.  
[01:44:15] This is an algorithm for recovering value estimates of intermediate steps when you  
[01:44:20] don't have the ability to do forward search. You must collect a trajectory first of n steps  
[01:44:27] before you're able to do this trick. But the intuition is kind of the same.  
[01:44:32] Knowing something about the Q value here can tell you something about the Q value here.  
[01:44:36] And indeed, you can recover a policy from a Q value.  
[01:44:40] You don't need to explicitly model the policy distribution.  
[01:44:43] You can recover the policy distribution by doing argmax over your Q values.  
[01:44:50] Q-learning, or approximate dynamic programming, propagates what you  
[01:44:56] know about the future Qs backward like this. You can see that there's a similar structure  
[01:45:01] going on here, where in one case you're planning over trajectories your agent hasn't been to yet,  
[01:45:07] whereas in the other you're planning over trajectories your agent has visited.  
[01:45:13] Importantly, why was Q-learning a big deal? It's because historically we just haven't had the  
[01:45:19] ability to do search on fairly high-dimensional problems like robotics or whatever.  
[01:45:24] For a long time, we made the assumption that if we can't model the dynamics with a world model,  
[01:45:30] we're going to instead just collect trajectories and then  
[01:45:32] plan with respect to the only number that really matters, which is reward.  
[01:45:36] This is very interesting. To unify this with our discussion of LLMs, you don't have Q values,  
[01:45:44] but you're doing this backwards learning where you find the trajectories that pass  
[01:45:50] some unit test in some coding environment and then reinforce those trajectories.  
[01:45:54] There's a huge difference between that and this forward approach with MCTS.  
[01:45:59] The reason it's much more preferable to do MCTS is because you can do it per move and make each move  
[01:46:05] better, rather than having to learn per trajectory and hope, as Karpathy said, to learn this…  
[01:46:11] Through a straw. Right, you get supervision through a straw.  
[01:46:14] You basically just upgrade all the tokens in a trajectory that might or might not have been  
[01:46:17] relevant to getting the answer right. The reason you can do this much more  
[01:46:21] sample-efficient, favorable thing with Go is that because MCTS works in Go, you basically  
[01:46:30] know that if you just do the search locally here—and this search is truncated at the end  
[01:46:36] by a value function that works even if you haven't unfolded your whole trajectory—you can just say,  
[01:46:43] "This is my new policy," and improve in a more iterative, local way, rather than  
[01:46:50] having to unfold all these trajectories. There was some research from Google in  
[01:46:57] 2023 or 2024 where they tried to apply tree structures to reasoning.  
[01:47:04] The jury is still out as to whether this can ever work.  
[01:47:11] We probably will see a revisiting of this idea of forward search in the future.  
[01:47:18] But there are two things that make MCTS very simple for Go. Value estimation is concrete.  
[01:47:24] You can determine it for real, and then you can use it to truncate depth, as you said. The breadth  
[01:47:31] is also determined. What's critical is that the action selection algorithm, where you iteratively  
[01:47:37] visit and grow the tree, is well suited for the size and depth of problem that Go is.  
[01:47:45] But for something like LLM reasoning, PUCT might not be a good enough heuristic.  
[01:47:49] It might be too greedy with local tokens, and it might only give you obvious thoughts that are  
[01:47:57] correct but don't really solve your final problem. I would say the jury is probably still out  
[01:48:02] on what the final instantiation of reasoning for LLMs will look like.  
[01:48:06] I wouldn't rule out that this stuff could come back, but it's a bit hard.  
[01:48:09] Don't LLMs natively learn to do MCTS, where they'll try an approach and be like, "Oh,  
[01:48:16] that doesn't work. Let's back up. Let's try this other thing," and then go in the  
[01:48:20] direction that proves to be more fruitful? Certainly, LLMs manage to do something that  
[01:48:25] looks like real human reasoning without having to do an explicit tree structure.  
[01:48:30] That being said, I think the idea of doing forward search and simulation to get a better sense of  
[01:48:35] what is valuable might make a comeback, even if not in exactly the same instantiation as AlphaGo.  
[01:48:43] Just to make sure I understand the crux of it: the breadth comes from the number of legal actions  
[01:48:50] being wider, and the depth comes from not being able to train a value function as easily, because…  
[01:48:57] Here's an example where LLMs break down. The CPUCT rule involves the √N over 1+Nₐ.  
[01:49:03] In an LLM, you're most likely never going to sample the same child more than once.  
[01:49:10] If you have multiple steps of thinking, because language is so broad and open-ended, a  
[01:49:17] discrete set of actions is not really an appropriate choice for an LLM.  
[01:49:21] Even though they're discrete tokens, it's just such a large number that this type  
[01:49:25] of exploration heuristic is probably not the right thing to guide how to search down a tree.  
[01:49:31] I guess the crux comes down to the fact that in Go, you know that MCTS is almost certainly  
[01:49:38] better than your current policy, even though you haven't explored the end of any trajectory.  
[01:49:45] In normal reasoning for LLMs or robotics, there's no way to just locally evaluate  
[01:49:50] and improve your next move in a way that's independent of actually solving the problem.  
[01:49:58] "No way" is a strong word. Lots of people have thought  
[01:50:00] about how to apply MCTS or its successors like MuZero to continuous control spaces,  
[01:50:06] and I'm sure very cool research work is still ongoing to try to crack that problem.  
[01:50:11] But yes, the apparent challenge right now is that most problems in much higher-dimensional  
[01:50:19] action spaces, or something combinatorially much bigger like language, don't seem as amenable  
[01:50:25] to the discrete action-selection heuristics and game-evaluation type stuff that Go has.  
[01:50:33] That's not to say the idea of thinking into the future along  
[01:50:37] multiple parallel tracks might not give you some information about which way to search.  
[01:50:41] If you think about mathematics, it often occupies more of a logical search procedure where you can  
[01:50:48] back up and see which paths seem good or not. There's more of a rigid structure there,  
[01:50:53] whereas in a business negotiation it's less of a tree and maybe something a bit different.  
[01:51:03] We're now seated, so I can ask you some more questions about  
[01:51:05] AlphaGo and AI research more generally. In 2021, Andy Jones had a paper called  
[01:51:12] "Scaling Scaling Laws with Board Games", and he basically anticipated inference compute,  
[01:51:17] or inference scaling, by showing that you can trade off test-time compute and training compute.  
[01:51:22] That is to say, you can spend more compute searching through MCTS, and if you do that,  
[01:51:28] you can get the equivalent performance to having spent more time training the model.  
[01:51:34] If you see this pattern, you might think that with LLMs you might do something similar in the future,  
[01:51:38] and in fact that's what ended up happening. What is a fun exploration one could do now to  
[01:51:46] explore other axes of scaling in toy settings, which will be important to understanding what  
[01:51:52] AI development might be like in a few years? Test-time scaling and reasoning, and how they  
[01:52:01] interact with model size, are quite profound when it comes to how much needs to actually be done as  
[01:52:08] explicit search versus how much can be packed into the forward pass of a neural network.  
[01:52:14] How does a forward pass of a neural network learn to do something that should be sequential and  
[01:52:20] recursive? That's quite interesting. The Andy Jones "Scaling Scaling Laws with Board Games"  
[01:52:24] paper is quite cool. There was another  
[01:52:26] really nice result from that paper. Not only can you predict scaling laws of  
[01:52:32] the LLM variety—where as you increase parameters you can decrease the amount of compute for search  
[01:52:38] or vice versa—but he also showed that you can predict how much compute is needed to solve a  
[01:52:45] larger version of the board game. For example with Go, which can scale from  
[01:52:51] 3x3 to an infinitely sized Go board, you might be able to revisit this question and  
[01:52:57] try to reproduce whether this shows up. I actually started this project with the  
[01:53:02] motivation of asking: does the "Bitter Lesson", or our knowledge of scaling laws, allow us to  
[01:53:06] execute a lot better on a compute-optimal Go bot? Can we build a strong Go bot without all of the  
[01:53:12] KataGo tricks, just by really focusing on the Bitter Lesson and scaling laws?  
[01:53:16] I have not been successful so far, but usually when you want scaling laws to work, you want  
[01:53:23] to be in the regime where the recipe already works and the data sets are good, rather than  
[01:53:28] trying to figure out how to do scaling while also trying to figure out what the right data sets are.  
[01:53:34] The scientific understanding component in research often follows a step where  
[01:53:38] you get something to work first. Then you use that system to collect  
[01:53:43] data that then helps you build a mental model of how things work, such as scaling laws.  
[01:53:47] Usually, if you want to build a strong Go bot using scaling laws, you actually have to make  
[01:53:51] a strong Go bot first and then use the scaling laws to extrapolate a bit further into the future.  
[01:53:56] Say more. Just so I understand, are you saying scaling laws did not work?  
[01:54:01] There was no scaling-laws pattern that you could see in your Go bot?  
[01:54:05] A mistake I made initially, when I had some bugs around how MCTS labeling was working,  
[01:54:09] was that I would collect a bunch of data with an expert policy and then treat it  
[01:54:14] as a supervised learning problem and try to identify scaling laws with expert data sets.  
[01:54:19] You can indeed plot things that look like this, but if you're in a regime where  
[01:54:24] your policy is not working well, you might just be studying scaling laws on bad data.  
[01:54:29] One important implementation detail is that if you want to study a scaling-laws problem,  
[01:54:33] you have to have a problem for which the data is good, the architecture is good, and there  
[01:54:38] are no bugs, and then you solve it from there. Ex ante, I wasn't able to apply scaling laws  
[01:54:44] to direct what to look at until I had the rest of the system working. This sounds obvious to  
[01:54:51] researchers. Of course you want a working, bug-free system before you study scaling.  
[01:54:55] But as advice for practitioners, on where I tripped up when I started this project,  
[01:55:00] you don't necessarily want to jump into the science of studying your man-made  
[01:55:04] artifact before your man-made artifact is interesting enough to be studied.  
[01:55:08] Speaking of compute, you can look at these charts of compute used to train the best AI model in the  
[01:55:16] world over time going back 10 years. It's a very smooth line in log space  
[01:55:22] that grows exponentially year over year. Except there's this huge aberration, and that  
[01:55:27] aberration is AlphaGo Zero, which was trained on way more compute than any other AI model at  
[01:55:33] the time. It was 3E23 FLOPS. It's comparable to a frontier LLM, orders of magnitude off, but still.  
[01:55:44] The question is, especially with you being able to get something  
[01:55:47] off the ground, did you train it on your own? I got a donation from Prime  
[01:55:50] Intellect for about $10K. I spent maybe the first $4K doing exploratory  
[01:55:58] research, and then about $3K on the final run. Some of it remained for serving the model.  
[01:56:06] Is your sense that they did a bad job training it, if you can do it in $10K now?  
[01:56:11] The compute required to be the first to do something is always much larger  
[01:56:15] than the compute it takes to catch up. It's the same story playing out in LLMs.  
[01:56:18] Once someone else has done it, you can use tricks like distillation.  
[01:56:22] You can use all sorts of crutches to bootstrap your way to success.  
[01:56:27] With my own bot that I've hosted online, I actually used best-response training  
[01:56:32] against the KataGo models to get a strong level of performance.  
[01:56:37] As of the time of recording, I'm validating whether I can do that first step, which is  
[01:56:42] to do the tabula rasa play. Importantly for research,  
[01:56:45] you often want to start from a good init. The simple thing I did first was train  
[01:56:48] best-response agents against KataGo. The AlphaZero team did not have any  
[01:56:54] policy they could train against, because they were trying to do everything tabula rasa.  
[01:56:58] Being the first to do it means you're prioritizing getting the thing working rather than the most  
[01:57:02] compute-efficient possible implementation. This plays out in robotics as well.  
[01:57:07] If you look at the frontier of large models trained for robotics, the scatter plot is  
[01:57:12] all over the place, and there isn't a very clean line the way there is for frontier LLMs.  
[01:57:17] That's because the folks training these models often are not at the  
[01:57:22] scale where every FLOP counts and they need to squeeze out the performance of every single  
[01:57:27] FLOP as the deciding factor in pre-training. Instead, their focus is more, "We want a certain  
[01:57:33] capability to show up, so we optimize the training setup to make it easy to derive that capability."  
[01:57:39] Once you have that capability… Invariably if you scale up the compute, you are forced to make it  
[01:57:44] compute-efficient, because this is hundreds of millions of dollars we're talking about.  
[01:57:48] But in the past, when compute for experiments was more plentiful—or not accounted for in a way the  
[01:57:57] researcher was really responsible for—you end up with people optimizing for things besides being on  
[01:58:01] the compute-optimal Pareto frontier. I see, like speed or something?  
[01:58:04] Yeah, time to result, or just getting it to work. The first AlphaGo probably had lots of compute,  
[01:58:10] and they didn't need to worry too much about making it the most compute-optimal thing.  
[01:58:15] How much of the improvements to compute efficiency are methods that did not exist  
[01:58:19] as of 2017 versus things which they could have done in 2017 but didn't?  
[01:58:24] Great question. Going into this project, I knew in the back of my mind that things  
[01:58:28] always get easier to do over time. I wanted to see where Go was at,  
[01:58:32] given that there hadn't seemed to be any major open-source strong bot after KataGo in 2020.  
[01:58:39] Reading the KataGo paper, there were a lot of clever ideas.  
[01:58:42] I was thinking, "Let’s see if the Bitter Lesson had happened, where a lot of these tricks just go  
[01:58:48] away because Nvidia made faster GPUs. Roughly, where are we on that?"  
[01:58:53] Again, this is not a peer-reviewed claim. It's just my preliminary vibe guess based on  
[01:58:59] what I’ve seen with my own experiments. It seems like architecture choices  
[01:59:05] don't matter that much. Transformer versus ResNet…  
[01:59:09] We're at the speed of GPU where the size of the model is not so big that this really matters.  
[01:59:15] You can simplify the setup quite a lot. Instead of doing a distributed asynchronous  
[01:59:20] RL setup with replay buffers and pushers and collectors, you can do a dumb synchronous thing  
[01:59:25] where you collect, train a supervised learning model, and then collect again.  
[01:59:30] There are opportunities to simplify infrastructure.  
[01:59:33] Nvidia GPUs have indeed gotten faster. Whereas KataGo was trained on V100s,  
[01:59:37] you can train on half the number of desktop Blackwell GPUs and it still works.  
[01:59:45] Some of the auxiliary supervision objectives that KataGo developed aren't really necessary  
[01:59:50] if you have a strong initialization. If you're initializing best-response  
[01:59:55] training against KataGo itself, your own model needs none of the tricks that KataGo needs.  
[02:00:00] The core thing is getting as quickly as possible to some strong opponents.  
[02:00:05] That matters a lot more than the specific architectural innovations.  
[02:00:08] But there are still some nice compute multipliers.  
[02:00:11] I found that training on 9x9 boards was very nice for resolving endgame value functions.  
[02:00:16] If you can co-train that on an architecture that can transfer between 9x9 and 19x19,  
[02:00:21] you can really cut down the warm-start time to learn from scratch.  
[02:00:25] AlphaGo Zero's plot showed the first 30 hours or so spent basically catching up  
[02:00:29] to the supervised learning baseline. You can cut down that time a lot  
[02:00:34] by pre-training on a small board and then warm-starting that into your 19x19 board play.  
[02:00:42] There was some other stuff, like varying the number of sims between episodes.  
[02:00:46] This turns out to be not that sensitive. You can fix it or increase it. It doesn't  
[02:00:52] matter too much. Anyway, it's nice from a scientific perspective, revisiting an old  
[02:00:57] paper and seeing what really matters. This is a tangential question,  
[02:01:00] but why is it okay to have a buffer in AlphaGo? Every time I talk to an AI researcher, they're  
[02:01:05] telling me about how bad it is to be off-policy. But the way a naive implementation of AlphaGo Zero  
[02:01:10] would work is that most of the moves in a given backward step, or in a batch of backward steps,  
[02:01:18] would not be among the ones made by the most recently trained model. So why is that okay?  
[02:01:26] Great question. This gets into the fundamental off-policy versus on-policy  
[02:01:32] reinforcement learning questions. As you'll recall, in MCTS, you take  
[02:01:37] actions that you took, and you relabel them to take different actions on the same states.  
[02:01:44] The off-policy part comes in where, what if you're relabeling states that your new policy  
[02:01:49] would never visit? What's the point? You're wasting capacity. In the extreme limit, imagine  
[02:01:54] the distribution of states in your training buffer are all states you would never visit.  
[02:01:58] Then you're supervising them to take good actions on states you would never achieve.  
[02:02:05] Therefore, your policy can get really bad. This is where off-policy can really hurt AlphaGo.  
[02:02:12] However, if you interpret this from the DAgger perspective—which is basically a way to correct  
[02:02:17] yourself back to the optimal trajectory given some data—what you want in an algorithm like  
[02:02:24] this is to have mostly states that you would visit, but then a small or reasonable percentage  
[02:02:30] of states in this high-dimensional tube around your optimal trajectories.  
[02:02:36] Any of those states are given a supervision target to funnel you back into your optimal trajectory.  
[02:02:43] Maybe I can just draw real quickly here. In a DAgger-style setup, your optimal  
[02:02:50] training data distribution is your optimal states and actions.  
[02:02:56] You want to be in this state, you want to be in this state, you want to be  
[02:02:59] in this state, and then you win here. These are your optimal policy actions.  
[02:03:05] These are the things you definitely want to train on.  
[02:03:08] But to make it robust to disturbances, you want to make sure that if you happen to  
[02:03:12] drift off into some other states, you can funnel yourself back in.  
[02:03:17] But why isn't this a fully general argument for off-policy training?  
[02:03:20] This is actually why you want to do off-policy training sometimes.  
[02:03:24] You don't want a compounding error where, if you make a mistake, you don't have the data  
[02:03:28] for how to return to your optimal distribution. Optimal control doesn't really say too much about  
[02:03:37] how to not accidentally get here, because it's making the assumption that once you learn the  
[02:03:42] policy, you're going to get to here. But in applications like robotics,  
[02:03:47] a gust of wind blows you slightly off and now you need to correct.  
[02:03:51] Or the friction on one of your tires is slightly lower than the other wheel, and now your car is  
[02:03:55] drifting and you have to correct it. These kinds of things often happen in  
[02:03:59] more real environments. There was a funny quote about chess and Go.  
[02:04:07] The problem with Go and chess is that the other player is always trying to do some shit.  
[02:04:12] Things can drift off, and you always want to be able to correct back to your winning condition.  
[02:04:19] Your replay buffer really should have the states your policy would visit, plus some  
[02:04:25] distribution of states you might drift to, and then how to return back to your optimal states.  
[02:04:31] Now, if you take this to the extreme and you say, "We don't have any of this data,  
[02:04:41] and we're just going to be labeling with MCTS states that are so far away from our optimal  
[02:04:49] behavior, like this bag of states over here…" Well, now each of them gets an MCTS label,  
[02:04:58] and your policy learns how to take the best possible action here, but you never get here.  
[02:05:02] You're training your model on states you would never reach.  
[02:05:09] This is where off-policy can really hurt. As part of this project, I did try an experiment  
[02:05:15] where I took a bunch of trajectories, and to try to saturate the GPU as much as possible,  
[02:05:21] I took random states from the dataset and reran MCTS on just those states.  
[02:05:28] Instead of playing a whole game where I'm doing MCTS on every move, I ignore the causality of  
[02:05:33] moves and pick random board states, and I label those with my current network.  
[02:05:38] I might revisit old states I've labeled before and relabel them again with my current network.  
[02:05:43] In practice, this actually does work. You can take some states that are reasonable and  
[02:05:49] constantly be relabeling them while training. This starts to converge on a very  
[02:05:56] robotics-like setup, which is very common. You have your dataset of trajectories, and then  
[02:06:02] you have something like a replay buffer pusher. These are off-policy offline trajectories. Your  
[02:06:13] replay buffer pusher pushes transition tuples to the replay buffer, and then you have a job that's  
[02:06:27] continuously replanning what the best action you should have done instead of the action you took.  
[02:06:37] In robotics, it's very common to minimize TD error.  
[02:06:41] Your Bellman updater is constantly pulling things from here and trying to satisfy Q(s,a).  
[02:07:01] From here you have your trainer, which is trying to fit the Q to the Qᵗᵃʳᵍᵉᵗ.  
[02:07:12] You can think about this as a sort of planner. You visit old states you've been to,  
[02:07:17] and you take your current model and rethink. What could I have done better if I visited this?  
[02:07:25] This is how off-policy robotic learning systems are usually trained.  
[02:07:29] These days there's a simpler recipe, but in the Google QT-Opt days, we did things like this.  
[02:07:35] So what is the trainer? The trainer is where you try  
[02:07:39] to minimize Q(s,a) and Qᵗᵃʳᵍᵉᵗ. Can you explain the whole setup  
[02:07:47] again at a high level? You have your off-policy  
[02:07:50] data that came from various policies. You're constantly pushing transitions  
[02:07:54] you saw before to a replay buffer. Then you've got this thing called  
[02:07:58] a Bellman updater, which basically replans: instead of this action, what action should I  
[02:08:02] have taken at s to have a better value? The way you enforce that is by trying  
[02:08:07] to minimize the TD error. Given this, you have s’. You compute Q(s’,a) and you find  
[02:08:16] the action that should go with s’ that makes this Q value as high as possible.  
[02:08:21] Then you add that to the reward here, and that gives you your actual target.  
[02:08:24] For this current s and a, your Qᵗᵃʳᵍᵉᵗ is this. Now you send back the Qᵗᵃʳᵍᵉᵗ to this transition.  
[02:08:36] With this tuple, you pair a Qᵗᵃʳᵍᵉᵗ. Then on the trainer side, you simply  
[02:08:43] use supervised learning and minimize your current network's Q(s, a) with its target.  
[02:08:48] Got it. So in the background you're basically thinking through how valuable  
[02:08:54] all these actions actually were. Yeah. In a more optimal policy  
[02:08:57] where you're trying to maximize this, what is the Qᵗᵃʳᵍᵉᵗ of this transition?  
[02:09:01] It's sort of like daydreaming. Exactly. You can think about  
[02:09:03] it like you're going back in hindsight. Given what I've seen in the historical buffer,  
[02:09:11] was there a better action I could have taken? The connection to Go here—I tried and it was  
[02:09:16] moderately successful, but too complex to open source—was replacing this with an MCTS relabeler.  
[02:09:27] Instead of doing this target network computation, you run MCTS on your transition.  
[02:09:34] In this case, you have your state, your action, and whether you won or not at the game.  
[02:09:40] Actually, you can just toss those two. You don’t care about these ones.  
[02:09:42] You just take your state and plan MCTS to get your best policy, Π, on your current network.  
[02:09:54] Not the network that took this action, but your current best policy network.  
[02:10:00] You rerun your search offline on these transitions.  
[02:10:04] If these are transitions your policy can get to, this actually acts as  
[02:10:08] a very nice stabilizing effect. Another benefit is that you can  
[02:10:11] fully saturate your GPU better because you're not blocking on the Go game to give you board states.  
[02:10:18] You simply search across all board states at any depth in parallel.  
[02:10:24] Here the trainer would just predict the MCTS label as best as possible.  
[02:10:28] This kind of works, and it is quite relevant in robotics where you have a lot of offline  
[02:10:33] data and you can't simulate things like MCTS. But in practice, it does run into the problem  
[02:10:38] that if the current model is looking at states it would never reach, it's wasting capacity.  
[02:10:45] You have to be a little bit careful here. Much of RL has converged to a much more  
[02:10:51] on-policy setup where they don't really try to directly train on off-policy data.  
[02:10:55] At best, they use off-policy data as a way to reduce variance,  
[02:10:58] but not to directly influence the objective. Why have they converged to that?  
[02:11:03] It's just more stable. You might use the off-policy Q as a way to do advantage  
[02:11:10] computation, like Q minus the sum of Q. If there are N actions, this is your value,  
[02:11:26] and these are your current Q values. Your advantage for that action is  
[02:11:29] the average value minus your current one. People can try to estimate Q in an off-policy  
[02:11:34] way and then just use advantage here. If there's a problem in these dynamics,  
[02:11:40] it doesn't blow up your loss as much. In robotics, there's a convergence  
[02:11:45] toward using off-policy data to shape your rewards but not actually be directly here.  
[02:11:51] I'm reminded of our earlier conversation about why MCTS is so favorable compared to  
[02:11:57] the REINFORCE or policy gradient thing LLMs do. This might be totally wrong, but I wrote a blog  
[02:12:03] post a few months ago about how policy gradient RL is even more inefficient than you might think.  
[02:12:10] The inefficiency one thinks about naively is the fact that you have to roll out a whole trajectory  
[02:12:16] to get any learning signal at all. As these trajectories become longer  
[02:12:20] and longer—as an agent has to do two days' worth of work to figure out if  
[02:12:31] it did a project correctly, rather than just completing the next word in a sentence—the  
[02:12:34] amount of information per FLOP decreases. You have to unroll two days' worth of thinking to  
[02:12:41] see if you implemented a feature correctly, so the amount of samples per FLOP has been decreasing.  
[02:12:50] You're trying to maximize as you’re learning, bits per FLOP.  
[02:12:58] You can think of bits per FLOP as samples per FLOP times bits per sample.  
[02:13:14] What I mentioned a second ago is that the samples per FLOP go down as RL becomes more long-horizon.  
[02:13:21] But this kind of naive RL is also terrible from a bits-per-sample perspective,  
[02:13:28] at least compared to supervised learning. Early on in training, let's say you have a  
[02:13:34] vocabulary size for an LLM that is 100K long, so there are 100K  
[02:13:39] possible tokens that one could answer. You have a totally untrained model and  
[02:13:43] a prompt like, "The sky is…" With supervised learning, the model would have some probability  
[02:13:56] distribution over all the things it could say. There's a label that says the term here is "blue,"  
[02:14:01] and it would learn through cross-entropy loss exactly how far its distribution  
[02:14:05] is from correctly saying "blue." If you were doing this through RL,  
[02:14:12] the model would try, "The sky is halycon." Nope, that's wrong. "The sky is told." Nope,  
[02:14:20] that's wrong. This is a totally untrained model. You would have to do this on the order of 100K  
[02:14:25] times just to stumble on "blue" and get some learning signal.  
[02:14:31] In the supervised learning regime, you have your distribution of probabilities,  
[02:14:35] you get told that it's "blue," and you figure out how far off you were.  
[02:14:39] The amount you learn is a function of your pass rate.  
[02:14:44] The further away you are from "blue," the more you learn to  
[02:14:47] go toward "blue" using cross-entropy loss. You can think of it as like your pass rate,  
[02:14:52] your prior probability of having said "blue." As a function of that, in supervised learning,  
[02:14:58] through cross-entropy loss, you would learn negative log(p), p being pass rate,  
[02:15:05] bits, once you get this label. Whereas in RL, if you're just randomly  
[02:15:12] guessing and seeing if it works, that's basically just the entropy of a binary random variable.  
[02:15:25] What's also tough here is that the distribution you're sampling  
[02:15:28] under is your policy's distribution. If your policy has no chance of sampling  
[02:15:34] "blue," then you will never get a signal. Exactly. That's modeled by the fact that your  
[02:15:41] probability of sampling "blue" is extremely low. If you sample it, you do learn as much as  
[02:15:46] you would have in supervised learning. In all other cases—99.99% of the time in  
[02:15:51] an untrained model—you're learning incredibly little from seeing that  
[02:15:57] "halycon" or "told" is not the correct word. That's what happens most of the time. You  
[02:16:02] learn very little. If you put your pass rate on the X-axis and the bits you're learning  
[02:16:17] from a sample on the Y-axis, with 0%, 50%, and 100%, so at the end of training you're here.  
[02:16:28] If you have supervised learning, the negative log pass rate would look something like this.  
[02:16:36] The entropy of a binary random variable would look like this,  
[02:16:46] depending on whether you're doing nats or bits. If you do bits it's one here at the peak.  
[02:16:52] This is like a coin flip. You learn the most from a coin  
[02:16:54] flip. This is supervised learning. This is RL. However, the problem is you spend most of training  
[02:17:06] in this regime, in the low pass rate regime. How fast you're learning is a function of how  
[02:17:14] many bits per sample you're getting, and you're getting very little signal here.  
[02:17:20] If you chart the pass rate on a log scale—where at the beginning of training with a vocab size of  
[02:17:29] 100K the pass rate is 1/100,000, then 1/10,000, 1/1,000, 1/100—what this graph looks like here,  
[02:17:45] supervised learning would look like this, and then RL would look like that.  
[02:17:59] And arguably you spend all your time here, potentially never even getting a single success.  
[02:18:06] It's a depressing plot in the sense that once you're here,  
[02:18:10] it's not at all obvious how you get to there. Once you're here you have something,  
[02:18:14] but you actually spend all the time here in many RL problems.  
[02:18:19] There's a question of how you initialize so you're at least at a non-zero pass rate.  
[02:18:25] One more thing I'd like to add about bits per sample that's very relevant to  
[02:18:30] any machine learning problem is that there's a connection to soft targets and distillation.  
[02:18:37] If you have access to the logits, not just the one-hot token answer, if you  
[02:18:44] have access to the soft targets the entropy of this distribution is far higher than the one-hot.  
[02:18:53] There's way more information in bits per sample in a soft label.  
[02:18:58] That's why distillation is so effective per sample.  
[02:19:01] It's giving you way more information per sample. I wonder what the equation would be,  
[02:19:06] but obviously it's… It would just be the  
[02:19:07] entropy of this distribution. The entropy of this is zero.  
[02:19:11] The entropy of this is the entropy equation. This is also why AlphaGo is quite beautiful.  
[02:19:16] In AlphaGo, you don't train the policy network to imitate the MCTS action.  
[02:19:22] You train it to imitate the MCTS distribution. Both of these are valid, and if you wanted to do  
[02:19:27] a scientific experiment of how important this soft label is, dark knowledge distillation,  
[02:19:33] you can run an experiment where you retrain the policy network on the action  
[02:19:37] MCTS selected rather than the soft target. Earlier I was stumbling around. Intuitively,  
[02:19:44] why is this ability to do iterative search—where you don't necessarily need to be able to win the  
[02:19:54] game in the beginning, you just need to be able to improve your current  
[02:19:56] policy—so powerful a capability in learning compared to how LLMs currently learn RL?  
[02:20:04] It's exactly this thing of considering your pass rate of the entire trajectory.  
[02:20:10] I just don't know a formal way to think about this.  
[02:20:12] Maybe you should help me out here. Why is AlphaGo an elegant RL algorithm?  
[02:20:18] The major reason is that you never have to initialize at a zero percent success  
[02:20:24] rate and solve the exploration problem of how to get to a non-zero success rate.  
[02:20:28] This is what allows you to hill-climb this beautiful supervised learning signal.  
[02:20:32] If you look at the actual implementation of AlphaGo, every step of the way,  
[02:20:36] there's actually no TD error learning or dynamic programming, at least explicitly.  
[02:20:43] It's just supervised learning on a value classification as  
[02:20:47] well as a policy KL minimization. It's just a supervised learning problem  
[02:20:53] on improved labels. The training is very stable. You can train as big of a network as you want.  
[02:20:58] You can retrain this on the data set. Everything will just go stably. The infrastructure  
[02:21:02] is very simple to implement as well. You don't need a complex distributed  
[02:21:05] system to keep everything on policy. At the end of the day, you're just saying,  
[02:21:10] "I have some improved labels. Let's retrain my supervised  
[02:21:13] model on these targets." You're always in this  
[02:21:16] beautiful regime where you're just trying to improve the policy, rather than escape local  
[02:21:23] minima where every signal is flat all around you. One way to draw the curve is if you draw the win  
[02:21:29] rate of an MCTS policy versus the raw network… Let's say this dotted line is the raw network.  
[02:21:35] The MCTS policy looks like this. Every step of the way,  
[02:21:40] this supervision signal is very clean. You're never in a situation where the  
[02:21:46] MCTS is giving you no signal, unless your MCTS distribution converges to exactly  
[02:21:52] what your policy network predicts. That's a great way to explain it.  
[02:22:02] Maybe we sit down and I ask some questions about automated research.  
[02:22:06] One thing I really wanted to talk to you about is that you did a bunch  
[02:22:09] of the research for this project through this automated LLM coding assistant loop.  
[02:22:21] There's an idea that if you fully automated AI research, you could have some sort of singularity.  
[02:22:25] Obviously we're not there yet, but to the extent that we have early indications of what  
[02:22:28] this process might look like, I'm curious about your observations about what the AI is good at,  
[02:22:35] what it's not good at, what you think about this scenario's likelihood eventually, and what  
[02:22:41] thoughts you have about this in general. I think automated scientific research is  
[02:22:45] one of the most exciting skills that the frontier labs are developing right now.  
[02:22:50] It's important for everyone who's doing any kind of research to get a good intuition of what it  
[02:22:55] can do now and what it can't, and how the science process might work in the future once we have AIs  
[02:23:00] automating a lot of this investigation. In brief, I mostly used Opus 4.6  
[02:23:06] and 4.7 while working on this. What works is that the models can do  
[02:23:13] a very good job of hyperparameter optimization. In the past, people would come up with a search  
[02:23:18] space of hyperparameters like learning rate, weight decay,  
[02:23:21] and maybe how many layers are in your network. They would do a grid search or a Bayesian  
[02:23:26] hyperparameter optimization approach, and it would find some tuned parameters.  
[02:23:31] The really cool thing that automated coding can do now is search a much  
[02:23:38] more open-ended set of problems. It can say, "I've identified that  
[02:23:43] the gradients are small in this layer, so let me change it up here.  
[02:23:45] Let me rewrite the code so the data loader has a new augmentation I came up with.  
[02:23:50] Let's try to find the best way to fit the constraints of the optimization problem."  
[02:23:55] You end up with this much more flexible, high-level, almost grad-student-like  
[02:24:00] ability to just grind a performance metric. This can squeeze out quite a lot of performance.  
[02:24:06] On a fixed data set with a fixed time budget, you can improve perplexity by quite a lot on a  
[02:24:11] classification problem like LLMs or Go. It is also fantastic now at basically  
[02:24:18] executing any experiment. I have a Claude Skill that  
[02:24:21] I wrote called Experiment where I give it a description of what I want it to plot.  
[02:24:26] I just describe, "Here's the x-axis I want, here's the y-axis. Answer this question for  
[02:24:30] me." It'll run off and do all the experiments, compile the plot, make a report, and suggest  
[02:24:35] what might have caused it and so forth. That's what works quite well today,  
[02:24:40] and I think we can expect these abilities to get better in the future.  
[02:24:42] But it's also useful to know what it's not doing so well today.  
[02:24:47] In the blog version of this tutorial, I have a plot of all the experiments I did grouped in a  
[02:24:54] tree, where every node represents a failed, successful, or mixed experimental result.  
[02:25:00] From there, it branches off into a child representing the follow-on experiment.  
[02:25:03] Occasionally, I'll rabbit-hole down a track like off-policy MCTS relabeling, do a few experiments,  
[02:25:09] and then realize it's probably not worth it. So then I'll jump to a completely different track.  
[02:25:13] I call these things rows. What I find is that the current closed models the public can access today  
[02:25:22] don't seem to be that great at selecting what the next experiment should be in a given track.  
[02:25:27] They don't seem to be able to step back and do the lateral thinking of, "Wait a minute,  
[02:25:32] this track doesn't really make sense. Let's go back to first principles and  
[02:25:37] think about what the bottleneck might be, or what we are trying to achieve."  
[02:25:41] Often I had to catch infra bugs myself by prompting the right question to Claude to  
[02:25:46] investigate what's causing the discrepancy, and then it'll answer the question.  
[02:25:50] With Mythos-class models or Mythos++ models coming online, maybe this just completely changes and  
[02:25:56] these problems fall to improved scaling. But at the same time, I think there's a  
[02:26:02] rich opportunity to develop RL environments that might incentivize this kind of lateral thinking.  
[02:26:08] One of the motivations for setting up this Go environment was that Go captures a lot  
[02:26:13] of very interesting research problems, often overlapping with LLMs or robotics.  
[02:26:18] Yet it's very quick to verify. The outer loop is ultimately:  
[02:26:22] does the agent do what I think it does? You can check the outcome of a Go game  
[02:26:26] quite easily. The inner loop  
[02:26:28] involves all this research engineering around distributed systems, predicting whether an  
[02:26:33] idea is going to work or not, and predicting the difference a particular modification to  
[02:26:38] your training algorithm might make. I think there's a rich library of  
[02:26:42] subtasks and sub-environments that you can train an automated scientist to work on,  
[02:26:46] with Go as a sort of outer verification loop. Once you acquire these skills, maybe you can  
[02:26:51] apply them to other domains like biosciences or robotics.  
[02:26:55] Or automating AI research. Or automating AI research.  
[02:26:58] Which is the real crux, the scary/incredible thing of making AIs make future versions of AIs.  
[02:27:06] You're suggesting the outer loop here could just be your win rate against KataGo?  
[02:27:10] That's one of them. I think there are a lot of deeper questions that one could tackle.  
[02:27:15] For example, let's say you have an idea on how to improve a scaling-law compute multiplier.  
[02:27:23] The outcome isn't necessarily "achieve the best Go bot ever".  
[02:27:28] The outcome might just be, "Can I predict what the win rate of my Go bot will be?"  
[02:27:33] Or, "Can I predict the scaling-law plots that emerge from my idea?"  
[02:27:36] But then you can verify that you haven't reward-hacked anything by using a very  
[02:27:39] verifiable game like Go on the outer loop. I think there are a couple of interesting  
[02:27:43] follow-on questions. There are questions  
[02:27:45] on the inner loop and the outer loop. On the inner loop, there's a question  
[02:27:49] of how locally verifiable any modification you might make is.  
[02:27:54] That is to say, would you know whether some idea you try out is  
[02:27:58] actually an improvement or a degradation? Would you know if something isn't working  
[02:28:02] as a result of a bug, or is it the result of the idea itself being wrong?  
[02:28:08] Ilya was talking about how one of the things he thinks makes him a good researcher is that he has  
[02:28:21] a strong belief in what the correct idea is. He's able to persevere through bugs and know  
[02:28:30] which things are bugs versus mistakes in the fundamental idea, based on his high-level belief  
[02:28:34] that "this idea should work, so therefore there has to be a bug", versus the other way around.  
[02:28:38] Why don't we start with that question? How locally verifiable are things  
[02:28:42] which are good ideas? As in the case of the  
[02:28:46] success story for deep learning, you can think about this as a decades-long idea  
[02:28:50] that took a lot of faith to get it to work. This presents a very challenging long-horizon  
[02:28:57] RL problem where every step of the way you have a committee telling you that this is a bad idea,  
[02:29:03] and then ultimately you break through. How do you design RL environments that  
[02:29:09] maybe give you some feedback earlier? I think this is a very tough open  
[02:29:15] question that I don't have an answer to. Ultimately, to play a very strong Go bot,  
[02:29:20] you probably did need to discover deep learning. Having a challenging game that cannot be cheated  
[02:29:30] easily on the outer loop could be used as an outer-loop signal for something like  
[02:29:35] discovering the principles of deep learning. Now, of course, to make it tractable—and this  
[02:29:39] is where research taste really matters—you have to come up with ways to initialize  
[02:29:44] your problem so that you don't try to solve a very intractable problem.  
[02:29:49] Maybe you can leverage LLMs as a universal grammar in the middle to  
[02:29:54] give you some sort of local feedback. The fact that LLMs are a universal  
[02:29:58] grammar means that they can move at almost any level of the stack.  
[02:30:02] They can think very locally, as well as step back and think in very broad steps.  
[02:30:07] I think that's where a lot of the lateral thinking ability of humans comes from:  
[02:30:12] knowing when the track you're pursuing or the objective you're pursuing is not right,  
[02:30:15] and you should be asking a different question. The other question is how stackable local  
[02:30:20] improvements are in the attempt to get to a better result on the outer loop.  
[02:30:25] I've heard rumors that at some AI labs, the thing that has gone wrong is that  
[02:30:29] people will individually pursue good ideas, but those don't end up stacking well, and so  
[02:30:34] the training run fails because of some weird interaction between two seemingly good ideas.  
[02:30:40] Having a single top-down vision of how things should work is very important.  
[02:30:44] Having worked at different AI labs and also played around with parallel agents  
[02:30:50] trying different ideas, what's your sense of how parallelizable AI innovation is?  
[02:30:55] Great question. I think the research taste for executing well on the Bitter Lesson is  
[02:31:03] that you need to know how much the Bitter Lesson can buy you and how much is too much  
[02:31:09] to ask for, at any given moment. Of course, in the fullness of time  
[02:31:13] compute is the single most important determinant of how things work.  
[02:31:20] It's almost inevitable that as you scale up energy and compute and parameters,  
[02:31:24] intelligence will just fall out of that. That's super beautiful, super profound. No algorithmic  
[02:31:29] detail really matters beyond that. But in the present day, we don't  
[02:31:33] have infinite compute and parameters and arbitrarily good initialization, so we  
[02:31:37] have to come up with heuristics that give us that. These heuristics are probably somewhat redundant.  
[02:31:44] That's probably why you see this effect where a lot of these compute  
[02:31:47] multipliers don't necessarily stack. They might have some correlated benefit.  
[02:31:52] And then three years down the line, when the Nvidia GPUs have gotten even  
[02:31:56] stronger, maybe they stack even less well. Maybe at any given point in time, the benefit  
[02:32:03] of any given compute multiplier is transitory, which is what I suspected with the KataGo paper.  
[02:32:08] There were many algorithmic ideas applied, and then you can see that with modern Blackwell GPUs  
[02:32:14] and Ada-class GPUs—which are much better than the V100-grade GPUs that that paper used—some of these  
[02:32:21] algorithmic tricks to speed up convergence just don't matter so much compared to something else.  
[02:32:26] I think that's a matter of taste in the present time.  
[02:32:30] How about the outer loop? How verifiable for making AI smarter?  
[02:32:37] With Go, you do have this outer loop of win rate against the best open-source model out there.  
[02:32:43] Even there, as you were saying, there are other outer loops of whether you discovered a new  
[02:32:48] phenomenon, which is actually very hard to…. If you didn't know scaling laws were  
[02:32:53] important… When were Chinchilla or Kaplan scaling laws released?  
[02:32:56] 2018. So if you're back in 2015, there's  
[02:33:00] not an automated procedure one can easily imagine for knowing which paper is the scaling laws paper  
[02:33:07] versus which is just another random plot. Even in the Go case, it's a hard-to-verify  
[02:33:12] outer loop, and the whole idea of an outer loop is to have some backstop on improvement,  
[02:33:21] let alone for general AGI, where of course we have a bunch of these benchmarks. But there's  
[02:33:27] a problem. We know the things we can measure, and we improve on the things we can measure.  
[02:33:32] We care about this broader ability to do economically useful work,  
[02:33:35] which is not super easy to measure, at least until you automate everything.  
[02:33:42] There's a question of how good the outer verification loop is  
[02:33:47] for AI self-improvement, and does that matter? I'm going to give a non-rigorous argument,  
[02:33:53] but one that I intuitively believe. DeepMind started with a focus on games.  
[02:34:00] They used games as their outer loop, and then their researchers learned from the experience  
[02:34:06] of solving games, and now they're working on LLMs. Presumably, there was some positive transfer from  
[02:34:11] their time working on games and Atari and Go and StarCraft that now helps them make good LLMs.  
[02:34:19] I assume that there's positive transfer in some regard, whether it's coding or  
[02:34:22] general research ability or project management. All these things probably help them do well.  
[02:34:31] If that's the case, why wouldn't it also be true for automated AI researchers?  
[02:34:36] They should be able to positively transfer experience tackling quick-to-verify,  
[02:34:41] quick-to-iterate environments to something more ambitious and economically useful,  
[02:34:45] like automating drug discovery. I don't know. Isn't the issue…  
[02:34:51] Historically, until Gemini 3 or whatever a couple years ago, people were saying, "Look,  
[02:34:58] Google isn't catching up in LLMs because they're too tied to the old approach."  
[02:35:06] There are gains, but there are also ways in which it actively hinders you. It's not obvious to me.  
[02:35:14] The jury's still out. Let's say currently Google's doing quite well.  
[02:35:20] Who knows if the initialization of training on games is ultimately going to hobble their ability  
[02:35:25] to be the winner in the long term. It's hard to say for sure.  
[02:35:32] Likewise, who knows if the seeming late start was really just them pre-training  
[02:35:37] for longer on how to scale up TPUs. They invested all their tech tree in  
[02:35:42] getting TPUs to be good, which seemed not that useful in the short term but in the long term  
[02:35:46] it becomes… So it's even hard for humans to reason about what the optimal research strategy  
[02:35:51] should be, even with the data we have today. Okay, we should let people know how they can  
[02:35:59] find out more about this project, whether to fork it themselves, or check out your blog post where  
[02:36:04] you do an excellent job explaining many of these ideas. Where do people go next?  
[02:36:09] My website is evjang.com. There's a blog post that links to an interactive version of this tutorial.  
[02:36:16] On my GitHub, which is the username ericjang, there's an AutoGo repo that people can fork  
[02:36:22] and reproduce the training results. I also highly recommend people check  
[02:36:25] out this blog post, "As Rocks May Think." We touched on some of the ideas in this  
[02:36:28] conversation, but it's this grander thesis of what happens when you have thinking as a primitive in—  
[02:36:38] Computer science. Exactly. I highly recommend  
[02:36:41] people check out that blog post as well. I encourage the audience to think about  
[02:36:45] the relationship between thinking and Go via MCTS and search, and how it relates to LLMs.  
[02:36:51] I think there's something quite profound there, and probably underexplored just because Go has  
[02:36:56] been relatively underexplored compared to the boom in LLMs.  
[02:36:59] It's not to say that I think we should have trees in our LLMs, but there is  
[02:37:04] some very interesting duality between them. You can actually do a lot of research on Go,  
[02:37:09] MCTS, and reasoning with very small budgets. So that's very exciting.  
[02:37:14] Awesome, Eric. Thanks for doing this. Thank you. It's an honor to be on the podcast.  
