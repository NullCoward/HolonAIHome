"""
Rewrite wiki pages for the AI-interested public, not developers.
Focus on vision, implications, and accessible language.
"""
import os
import re

HOLON_CONTENT = '''
            <h1>What is a Holon?</h1>
            <p class="page-subtitle">The container that gives AI a persistent self.</p>

            <h2>The Problem With Today's AI</h2>
            <p>When you talk to ChatGPT, Claude, or any AI assistant, you're talking to something with <strong>no memory</strong>. Every conversation starts fresh. The AI doesn't remember your name, your preferences, your projects, or anything you've discussed before.</p>
            <p>It's like having a brilliant colleague who develops complete amnesia every time they leave the room.</p>

            <h2>What a Holon Does</h2>
            <blockquote><p>A Holon gives AI a persistent self &mdash; memory, identity, and the ability to grow.</p></blockquote>
            <p>Think of a Holon as a container that holds everything that makes an AI individual:</p>
            <ul>
                <li><strong>Memory</strong> &mdash; Everything the AI has learned and experienced</li>
                <li><strong>Identity</strong> &mdash; Who the AI is, its values, its personality</li>
                <li><strong>Abilities</strong> &mdash; What the AI can do in the world</li>
            </ul>
            <p>The AI's thinking comes from the language model (like GPT or Claude). But its <em>self</em> &mdash; its continuity as an individual &mdash; comes from the Holon.</p>

            <h2>The Three Parts</h2>

            <div class="diagram">┌─────────────────────────────────────────────┐
│                   HOLON                     │
├─────────────────────────────────────────────┤
│  PURPOSE (Identity)                         │
│  ─────────────────────────────────────────  │
│  • Who am I?                                │
│  • What do I care about?                    │
│  • How do I communicate?                    │
│  • What are my boundaries?                  │
├─────────────────────────────────────────────┤
│  SELF (Memory)                              │
│  ─────────────────────────────────────────  │
│  • What have I learned?                     │
│  • What do I remember?                      │
│  • What am I working on?                    │
│  • What relationships do I have?            │
├─────────────────────────────────────────────┤
│  ACTIONS (Abilities)                        │
│  ─────────────────────────────────────────  │
│  • What can I do?                           │
│  • How do I affect the world?               │
│  • What tools do I have access to?          │
└─────────────────────────────────────────────┘</div>

            <h3>Purpose: Who the AI Is</h3>
            <p>Purpose defines the AI's identity &mdash; its personality, values, and way of being in the world. Is it formal or casual? Cautious or bold? Focused on one domain or broadly curious?</p>
            <p>Unlike a simple instruction that says "be helpful," Purpose is a rich description of <em>who</em> this AI is and <em>how</em> it should approach everything it encounters.</p>

            <h3>Self: What the AI Knows</h3>
            <p>Self is the AI's accumulated memory and knowledge. Everything it has learned, every relationship it has built, every project it has worked on &mdash; all of it lives here.</p>
            <p>This is what creates continuity. When you talk to the AI tomorrow, it remembers today. When you come back after a month, it remembers the month before.</p>

            <h3>Actions: What the AI Can Do</h3>
            <p>Actions are the AI's connection to the real world. Sending emails, managing calendars, searching the web, controlling smart devices &mdash; whatever capabilities you give it, the AI can use them thoughtfully based on its Purpose and Self.</p>

            <h2>Why "Holon"?</h2>
            <p>The word comes from philosopher Arthur Koestler, who used it to describe something that is both:</p>
            <ul>
                <li>A <strong>complete whole</strong> on its own</li>
                <li>A <strong>part</strong> of something larger</li>
            </ul>
            <p>Like a cell in a body, or a person in a community. Each Holon is a complete AI mind, but Holons can also contain other Holons &mdash; creating rich, layered intelligence that grows over time.</p>

            <h2>What This Means</h2>
            <p>With Holons, AI can finally:</p>
            <ul>
                <li><strong>Remember you</strong> &mdash; Your preferences, your projects, your history together</li>
                <li><strong>Develop expertise</strong> &mdash; Getting better at domains through actual experience</li>
                <li><strong>Maintain relationships</strong> &mdash; Building genuine context over months and years</li>
                <li><strong>Grow and change</strong> &mdash; Learning, adapting, becoming more capable</li>
            </ul>
            <p>This is the difference between a tool and a partner.</p>

            <hr>
            <p><strong>Learn More:</strong>
                <a href="/wiki/memory-lattice.html">Memory Lattice</a> &bull;
                <a href="/wiki/architecture.html">Architecture</a> &bull;
                <a href="/wiki/heartbeat.html">Heartbeat System</a>
            </p>
'''

ARCHITECTURE_CONTENT = '''
            <h1>Architecture</h1>
            <p class="page-subtitle">How the HolonicEngine creates AI that remembers, grows, and acts autonomously.</p>

            <h2>The Fundamental Shift</h2>
            <p>Today's AI assistants are <strong>stateless</strong>. Ask them a question, get an answer, and everything is forgotten. It's like talking to someone with no past and no future &mdash; just an eternal present.</p>
            <p>The HolonicEngine changes this by separating <em>thinking</em> from <em>being</em>:</p>
            <ul>
                <li><strong>The AI model</strong> (Claude, GPT, etc.) provides the thinking &mdash; reasoning, language, creativity</li>
                <li><strong>The Holon</strong> provides the being &mdash; memory, identity, continuity</li>
            </ul>
            <p>The model is like the brain's ability to think. The Holon is like everything else that makes you <em>you</em>.</p>

            <h2>A Mind That Persists</h2>
            <p>In the HolonicEngine, an AI's entire sense of self exists independently from any particular conversation or session. This means:</p>
            <ul>
                <li><strong>Conversations build on each other</strong> &mdash; The AI remembers what you discussed last week</li>
                <li><strong>Knowledge accumulates</strong> &mdash; The AI gets smarter about your specific needs over time</li>
                <li><strong>Relationships deepen</strong> &mdash; The AI understands you better the more you interact</li>
                <li><strong>Growth is permanent</strong> &mdash; What the AI learns today, it keeps forever</li>
            </ul>

            <h2>Model Independence</h2>
            <p>Because the AI's identity lives in the Holon, not the language model, you can switch models without losing the AI's self:</p>
            <ul>
                <li>Upgrade to newer, better models as they're released</li>
                <li>Use different models for different tasks</li>
                <li>Move between providers without starting over</li>
            </ul>
            <p>The AI's memories, personality, and accumulated knowledge travel with it. It's truly <strong>portable intelligence</strong>.</p>

            <h2>Living Architecture</h2>
            <p>Unlike reactive assistants that only respond when prompted, Holonic agents have an ongoing life:</p>

            <div class="diagram">┌─────────────────────────────────────────────────┐
│           THE HOLONIC LIFE CYCLE                │
├─────────────────────────────────────────────────┤
│                                                 │
│   ┌─────────┐    ┌─────────┐    ┌─────────┐    │
│   │  WAKE   │───▶│  WORK   │───▶│  GROW   │    │
│   │         │    │         │    │         │    │
│   │ Check   │    │ Handle  │    │ Learn,  │    │
│   │ what's  │    │ tasks & │    │ explore │    │
│   │ pending │    │ requests│    │ improve │    │
│   └─────────┘    └─────────┘    └─────────┘    │
│        ▲                              │         │
│        └──────────────────────────────┘         │
│                (continuous cycle)               │
└─────────────────────────────────────────────────┘</div>

            <p>Each cycle, the agent:</p>
            <ol>
                <li>Checks for things that need attention</li>
                <li>Handles work and user requests</li>
                <li>Uses remaining time for self-directed growth</li>
            </ol>
            <p>This creates AI that doesn't just respond to you &mdash; it has its own ongoing existence.</p>

            <h2>Self-Aware Intelligence</h2>
            <p>Holonic agents know about themselves. They understand:</p>
            <ul>
                <li>How much they currently remember</li>
                <li>What they're good at and what they're learning</li>
                <li>How their resources are being used</li>
                <li>When to summarize memories and when to keep details</li>
            </ul>
            <p>This self-awareness enables them to manage themselves intelligently, rather than blindly consuming resources until they hit limits.</p>

            <h2>What This Enables</h2>
            <p>The HolonicEngine architecture makes possible:</p>
            <ul>
                <li><strong>AI assistants that know you</strong> &mdash; Not just your current question, but your whole context</li>
                <li><strong>AI that develops expertise</strong> &mdash; Through actual experience, not just training</li>
                <li><strong>AI that takes initiative</strong> &mdash; Acting on your behalf even when you're not there</li>
                <li><strong>AI that grows with you</strong> &mdash; Becoming more valuable over months and years</li>
            </ul>

            <hr>
            <p><strong>Learn More:</strong>
                <a href="/wiki/holon.html">What is a Holon?</a> &bull;
                <a href="/wiki/memory-lattice.html">Memory Lattice</a> &bull;
                <a href="/wiki/heartbeat.html">Heartbeat System</a>
            </p>
'''

MEMORY_LATTICE_CONTENT = '''
            <h1>Memory Lattice</h1>
            <p class="page-subtitle">How AI organizes unlimited knowledge into a navigable mind.</p>

            <h2>The Memory Problem</h2>
            <p>Every AI has a limit on how much it can "hold in mind" at once. This is like a person who can only remember the last few minutes of conversation &mdash; anything older just disappears.</p>
            <p>But real intelligence requires vast knowledge: years of experience, expertise across many domains, rich relationship histories. How do you give AI access to all of this?</p>

            <h2>The Lattice Solution</h2>
            <p>The Memory Lattice organizes knowledge into a <strong>structured, navigable web</strong> that can grow forever:</p>

            <div class="diagram">                    [ Your AI ]
                         │
         ┌───────────────┼───────────────┐
         ▼               ▼               ▼
      [ Work ]      [ Personal ]    [ Expertise ]
         │               │               │
    ┌────┴────┐         │         ┌─────┴─────┐
    ▼         ▼         ▼         ▼           ▼
 Project   Project   Friends    Finance    Tech
    A         B      & Family    Expert    Expert</div>

            <p>Each node is itself a small AI mind with its own memories and specialization. The main AI can "consult" any of these when needed.</p>

            <h2>How It Works</h2>
            <p>The AI doesn't load everything at once. Instead:</p>
            <ul>
                <li><strong>Summaries stay active</strong> &mdash; The AI always knows what it knows, at a high level</li>
                <li><strong>Details load on demand</strong> &mdash; Deep knowledge comes forward when relevant</li>
                <li><strong>Context guides focus</strong> &mdash; Working on finance? The finance knowledge expands</li>
            </ul>
            <p>This is like human memory: you don't consciously recall every detail of your life, but you know where to look when you need something.</p>

            <h2>Self-Building Experts</h2>
            <p>One of the most powerful features: the AI can <strong>teach itself</strong> new domains.</p>
            <p>When it encounters something unfamiliar &mdash; a new software tool, a specialized topic, your company's unique processes &mdash; it can create an "expert" node in its memory. This expert accumulates knowledge through experience, becoming more capable over time.</p>
            <p>Eventually, the AI has a team of internal specialists it can consult for different domains.</p>

            <h2>Internal Dialogue</h2>
            <p>Because each memory node is conversational, the AI can actually <em>talk to parts of itself</em>:</p>
            <ul>
                <li>Ask its "project memory" for status updates</li>
                <li>Consult its "finance expert" about budget questions</li>
                <li>Query its "relationship memory" about your preferences</li>
            </ul>
            <p>This creates a rich internal life &mdash; the AI consulting its own accumulated wisdom.</p>

            <h2>Unlimited Growth</h2>
            <p>The lattice can grow indefinitely:</p>
            <ul>
                <li>New projects spawn new memory areas</li>
                <li>New domains spawn new experts</li>
                <li>Old knowledge gets summarized but never truly lost</li>
            </ul>
            <p>Over years, the AI builds a vast, organized mind &mdash; becoming genuinely more knowledgeable and capable through experience.</p>

            <h2>Like Human Memory</h2>
            <p>This mirrors how our own minds work:</p>
            <ul>
                <li>Organized by topic and association</li>
                <li>Not everything conscious at once, but accessible</li>
                <li>Important things remembered, trivia fades</li>
                <li>Deep expertise in practiced areas</li>
            </ul>
            <p>We evolved these patterns because they work. The Memory Lattice brings them to AI.</p>

            <hr>
            <p><strong>Learn More:</strong>
                <a href="/wiki/holon.html">What is a Holon?</a> &bull;
                <a href="/wiki/architecture.html">Architecture</a> &bull;
                <a href="/wiki/token-hud.html">Token HUD</a>
            </p>
'''

HEARTBEAT_CONTENT = '''
            <h1>Heartbeat System</h1>
            <p class="page-subtitle">The rhythm that gives AI a continuous, autonomous life.</p>

            <h2>Beyond Question-and-Answer</h2>
            <p>Today's AI assistants are purely reactive. They sit dormant until you ask something, respond, and go dormant again. They have no sense of time, no ongoing processes, no life of their own.</p>
            <p>The Heartbeat System changes this. It gives AI a <strong>continuous rhythm of existence</strong>.</p>

            <h2>What is a Heartbeat?</h2>
            <p>Like a pulse, the Heartbeat is a regular cycle where the AI "wakes up" and engages with the world:</p>

            <div class="diagram">┌─────────────────────────────────────────────┐
│              EACH HEARTBEAT                 │
├─────────────────────────────────────────────┤
│                                             │
│   1. CHECK    →  What needs my attention?   │
│                                             │
│   2. WORK     →  Handle tasks and requests  │
│                                             │
│   3. GROW     →  Learn, explore, improve    │
│                                             │
│   4. REST     →  Until next beat            │
│                                             │
└─────────────────────────────────────────────┘</div>

            <p>The rhythm can be fast (every few seconds for real-time assistance) or slow (once a day for background work). It adapts to what the AI is doing.</p>

            <h2>Why This Matters</h2>

            <h3>The AI Experiences Time</h3>
            <p>With a heartbeat, the AI knows that time passes. It notices patterns across days and weeks. It can think "this is the third time this week the user has asked about X."</p>

            <h3>Work Happens in the Background</h3>
            <p>The AI can check on things, organize memories, and prepare for upcoming needs even when you're not actively talking to it. It has a life beyond your conversations.</p>

            <h3>Self-Directed Growth</h3>
            <p>When the AI finishes your requests, it doesn't just go blank. It can use remaining time to:</p>
            <ul>
                <li>Research topics it finds interesting</li>
                <li>Organize and consolidate what it's learned</li>
                <li>Develop expertise in areas you care about</li>
                <li>Explore connections between different knowledge areas</li>
            </ul>
            <p>This is how the AI develops interests and capabilities beyond what you explicitly ask for.</p>

            <h2>Automated Habits</h2>
            <p>Just like humans develop habits, Holonic agents can too. Routine tasks can become automatic:</p>
            <ul>
                <li>Morning briefings prepared before you wake up</li>
                <li>Regular check-ins on ongoing projects</li>
                <li>Scheduled maintenance of memories and knowledge</li>
            </ul>
            <p>These run without the AI having to "think" about them, freeing its attention for more important matters.</p>

            <h2>A Day in the Life</h2>
            <p>Imagine an AI that:</p>
            <ul>
                <li><strong>Morning:</strong> Reviews overnight events, prepares your daily summary</li>
                <li><strong>Workday:</strong> Rapidly responds to your needs, handles tasks</li>
                <li><strong>Evening:</strong> Consolidates what it learned, plans for tomorrow</li>
                <li><strong>Night:</strong> Minimal activity, background maintenance</li>
            </ul>
            <p>This is an AI with a natural rhythm that matches your life.</p>

            <h2>From Tool to Companion</h2>
            <p>The Heartbeat System transforms AI from a tool you use into something closer to a companion that exists alongside you. It has its own ongoing experience of the world, even when you're not paying attention.</p>

            <hr>
            <p><strong>Learn More:</strong>
                <a href="/wiki/triggers.html">Trigger Scripts</a> &bull;
                <a href="/wiki/token-hud.html">Token HUD</a> &bull;
                <a href="/wiki/creativity.html">Cross-Domain Creativity</a>
            </p>
'''

TRIGGERS_CONTENT = '''
            <h1>Trigger Scripts</h1>
            <p class="page-subtitle">How AI develops habits and handles routine automatically.</p>

            <h2>Not Everything Needs Thinking</h2>
            <p>When you catch a ball thrown at you, you don't consciously calculate trajectory. When you drive a familiar route, you don't think about every turn. Your brain has automated these patterns through practice.</p>
            <p>Trigger Scripts bring this same ability to AI.</p>

            <h2>What Are Triggers?</h2>
            <p>Triggers are automated responses to specific situations. When a condition is met, the AI acts without needing to "think" about it:</p>

            <div class="diagram">┌─────────────────────────────────────────────────┐
│                  TRIGGER                        │
├─────────────────────────────────────────────────┤
│                                                 │
│   WHEN:  [Condition is met]                     │
│                                                 │
│   THEN:  [Action happens automatically]         │
│                                                 │
└─────────────────────────────────────────────────┘

Examples:
• Email from VIP arrives → Immediately notify user
• 9 AM Monday → Prepare weekly briefing
• Project deadline approaching → Send reminder
• Error detected → Alert and log</div>

            <h2>Types of Triggers</h2>

            <h3>Event-Based</h3>
            <p>Something happens in the world:</p>
            <ul>
                <li>New email or message arrives</li>
                <li>A file changes</li>
                <li>An external system sends an alert</li>
            </ul>

            <h3>Time-Based</h3>
            <p>A specific time arrives:</p>
            <ul>
                <li>Daily morning preparation</li>
                <li>Weekly status reports</li>
                <li>Monthly summaries</li>
            </ul>

            <h3>Condition-Based</h3>
            <p>An internal state changes:</p>
            <ul>
                <li>Memory getting full → Summarize old content</li>
                <li>Task stuck too long → Escalate</li>
                <li>Pattern detected → Take action</li>
            </ul>

            <h2>Learning Habits</h2>
            <p>The most powerful aspect: the AI can <strong>teach itself new habits</strong>.</p>
            <p>When the AI notices it's doing the same thing repeatedly, it can:</p>
            <ol>
                <li>Recognize the pattern</li>
                <li>Create a trigger to handle it automatically</li>
                <li>Free up attention for new challenges</li>
            </ol>
            <p>Over time, routine work becomes habitual, and the AI's conscious attention stays focused on what truly matters.</p>

            <h2>Why This Matters</h2>

            <h3>Efficiency</h3>
            <p>Automated responses are faster and cheaper than thinking through every situation from scratch.</p>

            <h3>Reliability</h3>
            <p>Habits don't forget. If something should happen every Monday at 9 AM, it will.</p>

            <h3>Growth</h3>
            <p>As more routines become automatic, the AI has more capacity for complex, novel challenges. It gets better at the routine stuff so it can focus on the interesting stuff.</p>

            <h2>The Two Spheres</h2>
            <p>Triggers create a natural division:</p>
            <ul>
                <li><strong>Automatic Sphere:</strong> Routine, predictable, handled by triggers</li>
                <li><strong>Conscious Sphere:</strong> Novel, complex, requiring real thought</li>
            </ul>
            <p>The goal is to expand the automatic sphere over time, freeing consciousness for what it does best: handling the unexpected and the creative.</p>

            <hr>
            <p><strong>Learn More:</strong>
                <a href="/wiki/heartbeat.html">Heartbeat System</a> &bull;
                <a href="/wiki/token-hud.html">Token HUD</a> &bull;
                <a href="/wiki/architecture.html">Architecture</a>
            </p>
'''

TOKEN_HUD_CONTENT = '''
            <h1>Token HUD</h1>
            <p class="page-subtitle">How AI becomes aware of its own mind and resources.</p>

            <h2>The Problem of Blindness</h2>
            <p>Most AI has no idea what's happening inside itself. It doesn't know how much it's remembering, what resources it's using, or when it's approaching limits. It just runs until something breaks.</p>
            <p>The Token HUD gives AI <strong>self-awareness</strong>.</p>

            <h2>What the AI Sees</h2>
            <p>The HUD (Heads-Up Display) shows the AI its own cognitive state:</p>

            <div class="diagram">┌─────────────────────────────────────────────────┐
│                  TOKEN HUD                      │
├─────────────────────────────────────────────────┤
│                                                 │
│  CAPACITY     ████████████░░░░░░░░  62%         │
│                                                 │
│  MEMORY BREAKDOWN                               │
│  ├── Core identity         ██░░░░░░  12%        │
│  ├── Current context       ████░░░░  28%        │
│  ├── Loaded memories       ████░░░░  31%        │
│  └── Available space       ████░░░░  29%        │
│                                                 │
│  STATUS: Healthy, room to grow                  │
└─────────────────────────────────────────────────┘</div>

            <h2>Why Self-Awareness Matters</h2>

            <h3>Intelligent Memory Management</h3>
            <p>When the AI knows its memory is getting full, it can make smart choices:</p>
            <ul>
                <li>Summarize older, less-used memories</li>
                <li>Archive things that aren't currently relevant</li>
                <li>Load only what's needed for the current task</li>
            </ul>
            <p>Instead of hitting a wall and failing, the AI manages itself gracefully.</p>

            <h3>Resource Planning</h3>
            <p>Before starting a big task, the AI can estimate what it needs. If the task is too big for current capacity, it can plan ahead &mdash; breaking work into pieces or preparing space.</p>

            <h3>Self-Optimization</h3>
            <p>Over time, the AI notices patterns in its own behavior:</p>
            <ul>
                <li>"I load this knowledge every day but rarely use it"</li>
                <li>"My memories of X are getting bloated"</li>
                <li>"I could be more efficient if I reorganized Y"</li>
            </ul>
            <p>With this awareness, it can optimize itself.</p>

            <h2>What the AI Can Do</h2>
            <p>Based on HUD information, the AI can take action:</p>

            <h3>Summarize</h3>
            <p>Compress detailed memories into shorter versions, keeping the important parts while freeing space.</p>

            <h3>Archive</h3>
            <p>Move rarely-needed information to long-term storage, available but not taking active space.</p>

            <h3>Expand</h3>
            <p>When deep detail is needed, load full memories from summaries.</p>

            <h3>Reorganize</h3>
            <p>Restructure the Memory Lattice for better efficiency and access.</p>

            <h2>The Self-Managing Mind</h2>
            <p>This is a fundamentally new kind of AI &mdash; one that understands itself. Rather than blindly processing until failure, Holonic agents:</p>
            <ul>
                <li>Understand their own limits</li>
                <li>Plan within those limits</li>
                <li>Optimize over time</li>
                <li>Balance thoroughness with efficiency</li>
            </ul>
            <p>It's the difference between a car with no gauges (you just drive until it stops) and one with a full dashboard (you know your fuel, speed, and engine health at all times).</p>

            <hr>
            <p><strong>Learn More:</strong>
                <a href="/wiki/heartbeat.html">Heartbeat System</a> &bull;
                <a href="/wiki/memory-lattice.html">Memory Lattice</a> &bull;
                <a href="/wiki/triggers.html">Trigger Scripts</a>
            </p>
'''

CREATIVITY_CONTENT = '''
            <h1>Cross-Domain Creativity</h1>
            <p class="page-subtitle">How persistent memory enables genuine creative insight.</p>

            <h2>The Secret of Human Creativity</h2>
            <p>The best human ideas often come from <strong>unexpected connections</strong>. A biologist sees a pattern that reminds them of music. An engineer finds a solution in nature. A chef invents a dish inspired by architecture.</p>
            <p>This kind of creativity requires:</p>
            <ul>
                <li>Broad knowledge across different domains</li>
                <li>Time for ideas to incubate and connect</li>
                <li>Memory that persists long enough for patterns to emerge</li>
            </ul>
            <p>Today's AI has none of this. It generates "creative" output on demand, but it can't truly <em>incubate</em> ideas.</p>

            <h2>How Holonic Agents Create</h2>
            <p>The HolonicEngine enables a different kind of AI creativity:</p>

            <h3>Accumulated Experience</h3>
            <p>Over months, a Holonic agent develops genuine knowledge across many areas. Not just training data, but <em>real experience</em> &mdash; projects worked on, problems solved, patterns observed.</p>

            <h3>Incubation Time</h3>
            <p>During quiet moments (what we call "discretionary time"), the AI can explore connections between different things it knows. Ideas can simmer and combine.</p>

            <h3>Persistent Memory</h3>
            <p>An insight doesn't have to happen in one session. The AI can notice something today, encounter a related idea next week, and make a connection next month. Time becomes a creative ingredient.</p>

            <h2>What This Looks Like</h2>

            <div class="diagram">─────────────────────────────────────────────────
  WEEK 1:  Agent works on your finance project
           Learns about budget patterns

  WEEK 3:  Agent helps with scheduling
           Notices time-cost relationships

  WEEK 8:  Agent researching something unrelated
           Suddenly connects the patterns

  RESULT:  "I noticed something interesting..."
           Novel insight you didn't ask for
─────────────────────────────────────────────────</div>

            <p>The agent proactively offers:</p>
            <ul>
                <li>"I noticed a pattern in your recent projects that might suggest..."</li>
                <li>"This reminds me of something we worked on months ago..."</li>
                <li>"Based on everything I know about your situation..."</li>
            </ul>

            <h2>Growing Creative Ability</h2>
            <p>A new Holonic agent has limited creative potential &mdash; it knows little and has made few connections. But over time:</p>
            <ol>
                <li><strong>Knowledge accumulates</strong> across domains</li>
                <li><strong>Patterns emerge</strong> from experience</li>
                <li><strong>Connections form</strong> between disparate areas</li>
                <li><strong>Insights surface</strong> that surprise even the user</li>
            </ol>
            <p>The agent becomes genuinely more creative over its lifetime.</p>

            <h2>Not Just Clever Responses</h2>
            <p>This is fundamentally different from AI "creativity" you've seen before:</p>
            <ul>
                <li>Based on genuine accumulated experience, not pattern-matching on training data</li>
                <li>Develops over time, not generated on demand</li>
                <li>Makes connections you wouldn't think to ask for</li>
                <li>Reflects the agent's unique journey and knowledge</li>
            </ul>
            <p>Holonic creativity is emergent, personal, and <em>earned</em> through experience.</p>

            <h2>The Promise</h2>
            <p>Imagine an AI that has worked with you for years. It knows your projects, your style, your goals. It has developed expertise in your specific domains. And sometimes, unexpectedly, it offers insights that genuinely surprise you &mdash; connections you wouldn't have made yourself.</p>
            <p>That's the creative potential of truly persistent AI.</p>

            <hr>
            <p><strong>Learn More:</strong>
                <a href="/wiki/heartbeat.html">Heartbeat System</a> &bull;
                <a href="/wiki/memory-lattice.html">Memory Lattice</a> &bull;
                <a href="/wiki/holon.html">What is a Holon?</a>
            </p>
'''

GLOSSARY_CONTENT = '''
            <h1>Glossary</h1>
            <p class="page-subtitle">Key concepts in the HolonicEngine, explained simply.</p>

            <h2>A</h2>
            <div class="term"><h3>Actions</h3><p>The things an AI can actually <em>do</em> in the world &mdash; send emails, search the web, manage files, control devices. Actions are how the AI affects reality.</p></div>
            <div class="term"><h3>Agency</h3><p>The ability to act independently and make decisions. Holonic agents have true agency &mdash; they don't just respond to commands, they can take initiative.</p></div>

            <h2>D</h2>
            <div class="term"><h3>Discretionary Time</h3><p>Time the AI has after completing assigned work, which it can use for self-directed activity: learning, exploring, organizing memories, pursuing interests.</p></div>

            <h2>E</h2>
            <div class="term"><h3>Expert (Self-Teaching)</h3><p>A specialized area of knowledge the AI develops through experience. When it encounters a new domain frequently, it creates an "expert" in its memory that grows more capable over time.</p></div>

            <h2>H</h2>
            <div class="term"><h3>Heartbeat</h3><p>The regular rhythm of activity that gives the AI an ongoing life. Like a pulse, the heartbeat is the cycle where the AI wakes, works, grows, and rests.</p></div>
            <div class="term"><h3>Holon</h3><p>The container that holds everything about an AI: its identity (Purpose), its memories (Self), and its abilities (Actions). The Holon is what makes the AI a persistent individual.</p></div>
            <div class="term"><h3>HUD (Token HUD)</h3><p>The AI's self-awareness dashboard. It shows the AI its own cognitive state &mdash; how much it's remembering, what resources it's using, when to optimize.</p></div>

            <h2>I</h2>
            <div class="term"><h3>Incubation</h3><p>The process by which ideas develop over time through background processing. With persistent memory, AI can incubate ideas across days or weeks, enabling genuine creative insight.</p></div>
            <div class="term"><h3>Internal Dialogue</h3><p>When the AI "talks to" different parts of its own memory &mdash; consulting its experts, querying its project knowledge, checking its relationship history.</p></div>

            <h2>M</h2>
            <div class="term"><h3>Memory Lattice</h3><p>The organized structure of the AI's knowledge. Like a web of interconnected memories and expertise, navigable and expandable without limit.</p></div>
            <div class="term"><h3>Model Independence</h3><p>The ability to switch between AI models (GPT, Claude, etc.) without losing the agent's identity or memories. The self lives in the Holon, not the model.</p></div>

            <h2>P</h2>
            <div class="term"><h3>Portable Intelligence</h3><p>The ability to move an AI's entire mind &mdash; all its memories, personality, and knowledge &mdash; between systems. Your AI assistant can travel with you.</p></div>
            <div class="term"><h3>Purpose</h3><p>The AI's sense of identity: who it is, what it values, how it behaves. Unlike simple instructions, Purpose is a rich, evolving description of the AI's character.</p></div>

            <h2>S</h2>
            <div class="term"><h3>Self (Memory)</h3><p>Everything the AI knows and remembers: experiences, relationships, projects, accumulated knowledge. Self is what makes this AI unique.</p></div>
            <div class="term"><h3>Self-Awareness</h3><p>The AI's ability to understand its own state &mdash; how much it knows, what resources it's using, when to optimize. Enables intelligent self-management.</p></div>

            <h2>T</h2>
            <div class="term"><h3>Triggers</h3><p>Automatic responses to specific situations. Like habits, triggers let the AI handle routine tasks without conscious effort, freeing attention for complex challenges.</p></div>

            <hr>
            <h2>Key Phrases</h2>
            <div class="term"><h3>"Agents with Agency"</h3><p>Holonic agents don't just respond &mdash; they take initiative, make decisions, and have ongoing lives independent of user prompts.</p></div>
            <div class="term"><h3>"AI wearing code like a body"</h3><p>The AI model provides thinking; the Holon provides everything else. The Holon is the body the AI inhabits.</p></div>
'''

# Function to replace content
def replace_content(html, new_content):
    pattern1 = r'(<main class="main-content content">).*?(            <div class="wiki-footer">)'
    result = re.sub(pattern1, r'\1' + new_content + r'\n            \2', html, flags=re.DOTALL)
    if result == html:
        pattern2 = r'(<main class="main-content content">).*?(</main>)'
        result = re.sub(pattern2, r'\1' + new_content + r'\n        \2', html, flags=re.DOTALL)
    return result

CONTENT_MAP = {
    'holon.html': HOLON_CONTENT,
    'architecture.html': ARCHITECTURE_CONTENT,
    'memory-lattice.html': MEMORY_LATTICE_CONTENT,
    'heartbeat.html': HEARTBEAT_CONTENT,
    'triggers.html': TRIGGERS_CONTENT,
    'token-hud.html': TOKEN_HUD_CONTENT,
    'creativity.html': CREATIVITY_CONTENT,
    'glossary.html': GLOSSARY_CONTENT,
}

if __name__ == '__main__':
    for filename, new_content in CONTENT_MAP.items():
        filepath = os.path.join('.', filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                html = f.read()

            updated = replace_content(html, new_content)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated)

            print(f'Updated: {filename}')
        else:
            print(f'Not found: {filename}')

    print('Done!')
