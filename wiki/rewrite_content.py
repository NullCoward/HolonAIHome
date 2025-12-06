"""
Rewrite wiki pages to be capability-focused without code examples.
"""
import os
import re

# New content for each page (main content section only)

HOLON_CONTENT = '''
            <h1>What is a Holon?</h1>
            <p class="page-subtitle">A portable AI context capsule &mdash; the fundamental building block of the HolonicEngine.</p>

            <h2>The Core Metaphor</h2>
            <blockquote><p>AI wearing code like a body.</p></blockquote>
            <p>Today's AI models are powerful reasoning engines, but they're fundamentally stateless &mdash; each conversation starts fresh, with no memory of what came before. The Holon solves this by giving AI a persistent "body" to inhabit:</p>
            <ul>
                <li>The body has capabilities (<strong>Actions</strong>) &mdash; ways to affect the world</li>
                <li>The body has a current state (<strong>Self</strong>) &mdash; memory and context</li>
                <li>The body has an identity (<strong>Purpose</strong>) &mdash; who it is and how it behaves</li>
            </ul>
            <p>The model provides the thinking. The Holon provides everything else.</p>

            <h2>The Three Components</h2>
            <p>Every Holon integrates three essential modules that work together to create a complete agent identity:</p>

            <div class="diagram">┌─────────────────────────────────────────────┐
│                   HOLON                     │
├─────────────────────────────────────────────┤
│  PURPOSE                                    │
│  ─────────────────────────────────────────  │
│  • Who am I?                                │
│  • What are my goals?                       │
│  • How should I behave?                     │
│  • What constraints do I have?              │
├─────────────────────────────────────────────┤
│  SELF (State)                               │
│  ─────────────────────────────────────────  │
│  • What do I currently know?                │
│  • What's my memory?                        │
│  • What child holons do I contain?          │
│  • What's my current context?               │
├─────────────────────────────────────────────┤
│  ACTIONS                                    │
│  ─────────────────────────────────────────  │
│  • What can I do?                           │
│  • Interface to external world              │
│  • Tools and capabilities available         │
└─────────────────────────────────────────────┘</div>

            <h3>Purpose (The Interpretive Lens)</h3>
            <p><strong>HOW to interpret everything.</strong></p>
            <p>Purpose defines the agent's identity and behavioral framework:</p>
            <ul>
                <li>Goals, values, and constraints that guide decision-making</li>
                <li>Personality and communication style</li>
                <li>Priorities and heuristics for handling ambiguity</li>
                <li>Guidance on when to use different capabilities</li>
            </ul>
            <p>Unlike a static system prompt, Purpose is structured, queryable, and can evolve as the agent learns.</p>

            <h3>Self / State (The Current Context)</h3>
            <p><strong>WHAT the agent knows and remembers.</strong></p>
            <p>Self contains everything that makes this agent unique at this moment:</p>
            <ul>
                <li>Dynamic values that change over time</li>
                <li>Accumulated knowledge and memories</li>
                <li>Historical logs of actions and decisions</li>
                <li>Nested child holons for specialized domains</li>
                <li>Relationships and context about users and projects</li>
            </ul>
            <p>This is the Holon's persistent memory &mdash; it survives across sessions and grows over time.</p>

            <h3>Actions (The Capabilities)</h3>
            <p><strong>WHAT the agent can do in the world.</strong></p>
            <p>Actions are the agent's interface to reality:</p>
            <ul>
                <li>Each action has a clear purpose and defined parameters</li>
                <li>Actions can modify the agent's own state and memory</li>
                <li>Actions can create or modify other Holons</li>
                <li>Actions connect to external systems, APIs, and services</li>
                <li>The agent chooses which actions to invoke based on context</li>
            </ul>

            <h2>The Execution Cycle</h2>
            <p>The HolonicEngine operates through a continuous cycle that brings the agent to life:</p>
            <ol>
                <li><strong>Context Assembly</strong>: The Holon's current state is prepared for the AI</li>
                <li><strong>Reasoning</strong>: The AI model processes the context and decides on actions</li>
                <li><strong>Action Dispatch</strong>: Requested actions are executed in the real world</li>
                <li><strong>State Update</strong>: Results flow back and update the Holon's memory</li>
                <li><strong>Persistence</strong>: Changes are saved for future sessions</li>
            </ol>
            <p>This cycle runs continuously on each <a href="/wiki/heartbeat.html">heartbeat</a>, giving the agent an ongoing "life" rather than isolated interactions.</p>

            <h2>Key Properties</h2>

            <h3>Portable</h3>
            <p>Holons are pure data structures that can be:</p>
            <ul>
                <li>Saved to disk and restored later</li>
                <li>Sent over a network to run elsewhere</li>
                <li>Stored in any database system</li>
                <li>Moved between different AI models seamlessly</li>
            </ul>
            <p>Because the AI model is stateless, you can switch providers without losing the agent's identity, memory, or capabilities. This is <strong>portable cognition</strong>.</p>

            <h3>Composable</h3>
            <p>Holons can contain other Holons, enabling sophisticated architectures:</p>
            <ul>
                <li><strong>Child holons</strong> for delegated sub-tasks</li>
                <li><strong>Specialist holons</strong> with deep domain expertise</li>
                <li><strong>Memory holons</strong> organizing different knowledge areas</li>
                <li><strong>Expert holons</strong> that the agent teaches itself about specific topics</li>
            </ul>
            <p>This creates a <a href="/wiki/memory-lattice.html">lattice structure</a> &mdash; a rich, navigable web of knowledge rather than a flat list.</p>

            <h3>Conversational</h3>
            <p>Holons aren't just data stores &mdash; they're <strong>responsive entities</strong>.</p>
            <p>The agent can query its own holons like consulting parts of its own mind. Ask a specialist holon about its domain, and it responds with relevant knowledge and context. This enables a form of internal dialogue where the agent leverages its accumulated expertise.</p>

            <h3>Self-Aware</h3>
            <p>Each Holon maintains awareness of its own resource usage:</p>
            <ul>
                <li>Current size and token footprint</li>
                <li>Budget limits and allocation</li>
                <li>Usage patterns over time</li>
                <li>Optimization opportunities</li>
            </ul>
            <p>This enables intelligent decisions about memory management &mdash; knowing when to summarize, archive, or expand knowledge.</p>

            <h2>The Name "Holon"</h2>
            <p>The term comes from Arthur Koestler's 1967 book <em>The Ghost in the Machine</em>.</p>
            <p>A holon is something that is simultaneously:</p>
            <ul>
                <li>A <strong>whole</strong> unto itself &mdash; complete and functional</li>
                <li>A <strong>part</strong> of a larger system &mdash; contributing to something greater</li>
            </ul>
            <p>This captures the recursive, composable nature of the architecture. Like cells in a body or departments in an organization, holons are autonomous units that combine to form greater wholes.</p>

            <hr>
            <p><strong>See Also:</strong>
                <a href="/wiki/memory-lattice.html">Memory Lattice</a> &bull;
                <a href="/wiki/architecture.html">Architecture</a> &bull;
                <a href="/wiki/token-hud.html">Token HUD</a>
            </p>
'''

ARCHITECTURE_CONTENT = '''
            <h1>Architecture</h1>
            <p class="page-subtitle">How the HolonicEngine creates agents with persistent memory, self-awareness, and autonomous behavior.</p>

            <h2>The Problem with Current AI</h2>
            <p>Today's AI assistants have a fundamental limitation: <strong>they forget everything</strong>.</p>
            <p>Each conversation is isolated. The AI has no memory of previous interactions, no accumulated knowledge, no sense of ongoing projects or relationships. It's like talking to someone with complete amnesia every single time.</p>

            <div class="diagram">Traditional AI Architecture:
┌────────────────────────────────────────────────────────┐
│  User: "Remember the project we discussed yesterday?"  │
│  AI:   "I don't have access to previous conversations" │
│                                                        │
│  Every interaction starts from zero.                   │
│  No memory. No context. No continuity.                 │
└────────────────────────────────────────────────────────┘</div>

            <h2>The HolonicEngine Solution</h2>
            <p>The HolonicEngine solves this by separating <strong>reasoning</strong> from <strong>memory</strong>:</p>
            <ul>
                <li>The AI model provides the reasoning (thinking, language, decision-making)</li>
                <li>The Holon provides everything else (memory, identity, capabilities, context)</li>
            </ul>
            <p>The model is stateless. The Holon is persistent.</p>

            <div class="diagram">HolonicEngine Architecture:
┌─────────────────────────────────────────────────┐
│             HOLONIC AGENT                       │
├─────────────────────────────────────────────────┤
│  ┌─────────────┐    ┌─────────────────────────┐ │
│  │  AI MODEL   │◄──►│        HOLON            │ │
│  │ (Reasoning) │    │  • Purpose (Identity)   │ │
│  │             │    │  • Self (Memory)        │ │
│  │  Stateless  │    │  • Actions (Abilities)  │ │
│  └─────────────┘    │                         │ │
│                     │      Persistent         │ │
│                     └─────────────────────────┘ │
└─────────────────────────────────────────────────┘</div>

            <h2>Model Agnosticism</h2>
            <p>Because state lives in the Holon, not the model, HolonicEngine agents are <strong>model-agnostic</strong>:</p>
            <ul>
                <li>Switch between Claude, GPT, or any other provider</li>
                <li>Use different models for different tasks (fast model for simple queries, powerful model for complex reasoning)</li>
                <li>Upgrade to newer models without losing agent memory or identity</li>
                <li>Mix models within the same agent architecture</li>
            </ul>
            <p>The agent's personality, knowledge, and capabilities remain constant regardless of which AI is currently "wearing" the Holon.</p>

            <h2>The Memory Hierarchy</h2>
            <p>HolonicEngine organizes knowledge into a hierarchical lattice structure:</p>

            <div class="diagram">Memory Organization:
                    ┌─────────────┐
                    │  Root Agent │
                    │  (Core Self)│
                    └──────┬──────┘
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    ┌──────────┐    ┌──────────┐    ┌──────────┐
    │  Work    │    │ Personal │    │  Expert  │
    │ Projects │    │ Context  │    │ Domains  │
    └────┬─────┘    └──────────┘    └────┬─────┘
         │                               │
    ┌────┴────┐                    ┌─────┴─────┐
    ▼         ▼                    ▼           ▼
┌───────┐ ┌───────┐          ┌────────┐  ┌────────┐
│Project│ │Project│          │ API    │  │Finance │
│  A    │ │  B    │          │ Expert │  │ Expert │
└───────┘ └───────┘          └────────┘  └────────┘</div>

            <p>This structure enables:</p>
            <ul>
                <li><strong>Selective Loading</strong>: Only relevant knowledge is loaded for each task</li>
                <li><strong>Efficient Storage</strong>: Large knowledge bases without overwhelming context</li>
                <li><strong>Natural Organization</strong>: Knowledge grouped by domain and relevance</li>
                <li><strong>Growth Over Time</strong>: The lattice expands as the agent learns</li>
            </ul>

            <h2>The Heartbeat Cycle</h2>
            <p>Unlike reactive chatbots that only respond when prompted, Holonic agents have a continuous "heartbeat" &mdash; a regular rhythm of activity:</p>
            <ol>
                <li><strong>Check Triggers</strong>: Are there automated tasks to run?</li>
                <li><strong>Handle Work</strong>: Process user requests and tasks</li>
                <li><strong>Discretionary Time</strong>: Use remaining budget for self-directed activity</li>
                <li><strong>Persist State</strong>: Save all changes for next cycle</li>
            </ol>
            <p>This gives agents an ongoing "life" with self-directed goals, not just reactive responses.</p>

            <h2>Resource Awareness</h2>
            <p>Holonic agents are aware of their own resource usage through the <a href="/wiki/token-hud.html">Token HUD</a>:</p>
            <ul>
                <li>They know their token budget and current usage</li>
                <li>They can make decisions about when to summarize or expand memory</li>
                <li>They balance thoroughness against efficiency</li>
                <li>They optimize their own cognitive footprint over time</li>
            </ul>
            <p>This self-awareness enables agents to manage their own resources intelligently, rather than blindly consuming tokens.</p>

            <h2>Key Architectural Benefits</h2>

            <h3>Persistent Identity</h3>
            <p>Agents maintain consistent personality, values, and communication style across all interactions. They remember who they are.</p>

            <h3>Accumulated Knowledge</h3>
            <p>Every interaction adds to the agent's understanding. Knowledge compounds over time, making the agent more capable.</p>

            <h3>Autonomous Behavior</h3>
            <p>Through triggers and discretionary time, agents can take initiative &mdash; checking on tasks, organizing knowledge, pursuing self-directed learning.</p>

            <h3>Scalable Complexity</h3>
            <p>The lattice structure allows agents to develop deep expertise in many domains without overwhelming any single context.</p>

            <hr>
            <p><strong>See Also:</strong>
                <a href="/wiki/holon.html">What is a Holon?</a> &bull;
                <a href="/wiki/memory-lattice.html">Memory Lattice</a> &bull;
                <a href="/wiki/heartbeat.html">Heartbeat System</a>
            </p>
'''

MEMORY_LATTICE_CONTENT = '''
            <h1>Memory Lattice</h1>
            <p class="page-subtitle">How Holonic agents organize unlimited knowledge in a navigable, hierarchical structure.</p>

            <h2>The Context Window Problem</h2>
            <p>Every AI model has a limited context window &mdash; a maximum amount of information it can process at once. This creates a fundamental challenge:</p>
            <ul>
                <li>Valuable knowledge gets lost when it exceeds the window</li>
                <li>Long conversations lose important early context</li>
                <li>Agents can't maintain deep expertise across many domains</li>
                <li>There's no good way to organize accumulated knowledge</li>
            </ul>
            <p>The Memory Lattice solves this by creating a <strong>structured, navigable hierarchy</strong> of knowledge that can grow indefinitely.</p>

            <h2>The Lattice Structure</h2>
            <p>Instead of a flat list of memories, the lattice organizes knowledge into nested holons:</p>

            <div class="diagram">                    [Root Agent]
                         │
         ┌───────────────┼───────────────┐
         ▼               ▼               ▼
    [Work Context]  [Personal]     [Expert Domains]
         │               │               │
    ┌────┴────┐         │         ┌─────┴─────┐
    ▼         ▼         ▼         ▼           ▼
[Project A][Project B][Contacts][API Expert][Finance]
    │                              │
    └── [Meeting Notes]            └── [Stripe]
    └── [Decisions]                └── [Twilio]
    └── [Action Items]             └── [OpenAI]</div>

            <p>Each node in the lattice is itself a Holon &mdash; complete with its own purpose, state, and capabilities.</p>

            <h2>Selective Loading</h2>
            <p>The key insight is that you don't need all knowledge all the time. The agent:</p>
            <ul>
                <li><strong>Loads summaries first</strong>: Quick overview of what each holon contains</li>
                <li><strong>Expands on demand</strong>: Detailed knowledge loaded only when relevant</li>
                <li><strong>Prioritizes by context</strong>: Working on Project A? That context is expanded</li>
                <li><strong>Maintains awareness</strong>: The agent knows what it knows, even when details aren't loaded</li>
            </ul>
            <p>This is like human memory &mdash; you don't consciously recall every detail of your life, but you know where to look when you need something.</p>

            <h2>Expert Holons</h2>
            <p>One of the most powerful patterns is the <strong>Expert Holon</strong> &mdash; a specialized child that becomes an expert in a specific domain:</p>
            <ul>
                <li>The agent encounters a new API or system</li>
                <li>It creates an Expert Holon to study and remember that domain</li>
                <li>The expert accumulates knowledge through use</li>
                <li>Future interactions benefit from this accumulated expertise</li>
            </ul>
            <p>Over time, the agent develops a team of internal experts it can consult for different domains.</p>

            <h2>Internal Dialogue</h2>
            <p>Because holons are conversational, the agent can query its own knowledge structure:</p>
            <ul>
                <li>Ask the Project holon for current status and blockers</li>
                <li>Consult the API Expert about integration options</li>
                <li>Query the Contacts holon about relationship history</li>
                <li>Check the Calendar holon for scheduling conflicts</li>
            </ul>
            <p>This creates a form of internal dialogue &mdash; the agent consulting specialized parts of its own mind.</p>

            <h2>Memory Operations</h2>
            <p>The lattice supports several key operations:</p>

            <h3>Remember</h3>
            <p>New information is stored in the appropriate location in the lattice. The agent decides where it belongs based on context and relevance.</p>

            <h3>Recall</h3>
            <p>When information is needed, the agent navigates the lattice to find relevant holons and expands their detail level.</p>

            <h3>Summarize</h3>
            <p>As holons grow, they can be summarized to maintain efficient overviews while preserving detail when needed.</p>

            <h3>Archive</h3>
            <p>Old or rarely-accessed information can be archived &mdash; still accessible but not consuming active context.</p>

            <h3>Spawn</h3>
            <p>New holons can be created to organize emerging knowledge areas or handle new domains.</p>

            <h2>Growth Over Time</h2>
            <p>The lattice is designed to grow indefinitely:</p>
            <ul>
                <li>New projects spawn new project holons</li>
                <li>New domains spawn new expert holons</li>
                <li>Relationships develop their own context holons</li>
                <li>The agent's capability compounds with experience</li>
            </ul>
            <p>Unlike traditional AI that starts fresh each session, a Holonic agent becomes more knowledgeable and capable over its lifetime.</p>

            <h2>Comparison to Human Memory</h2>
            <p>The Memory Lattice mirrors how human memory actually works:</p>
            <ul>
                <li><strong>Hierarchical organization</strong>: Knowledge grouped by topic and association</li>
                <li><strong>Selective recall</strong>: Not everything conscious at once, but accessible</li>
                <li><strong>Consolidation</strong>: Important information strengthened, trivia fades</li>
                <li><strong>Expertise development</strong>: Deep knowledge in practiced domains</li>
            </ul>
            <p>This isn't arbitrary &mdash; human memory evolved these patterns because they work for managing large knowledge bases efficiently.</p>

            <hr>
            <p><strong>See Also:</strong>
                <a href="/wiki/holon.html">What is a Holon?</a> &bull;
                <a href="/wiki/architecture.html">Architecture</a> &bull;
                <a href="/wiki/token-hud.html">Token HUD</a>
            </p>
'''

HEARTBEAT_CONTENT = '''
            <h1>Heartbeat System</h1>
            <p class="page-subtitle">The cognitive clock that gives Holonic agents continuous, autonomous life.</p>

            <h2>Beyond Reactive AI</h2>
            <p>Traditional AI assistants are purely reactive &mdash; they sit dormant until prompted, respond, then go dormant again. They have no sense of time passing, no ongoing processes, no self-directed activity.</p>
            <p>The Heartbeat System changes this by giving agents a <strong>continuous rhythm of activity</strong>.</p>

            <div class="diagram">Traditional AI:
    Prompt → Response → (dormant until next prompt)

Holonic Agent:
┌─────────────────────────────────────────────┐
│  HEARTBEAT CYCLE (continuous)               │
│                                             │
│    ┌────────┐                               │
│    │ Check  │──► Handle ──► Discretionary   │
│    │Triggers│    Work       Time            │
│    └────────┘       │           │           │
│         ▲           │           │           │
│         └───────────┴───────────┘           │
│              (repeat each beat)             │
└─────────────────────────────────────────────┘</div>

            <h2>The Heartbeat Cycle</h2>
            <p>Each heartbeat, the agent goes through a consistent sequence:</p>
            <ol>
                <li><strong>Check Triggers</strong>: Are there automated scripts that should run? Time-based events? Conditions that have been met?</li>
                <li><strong>Handle Work</strong>: Process any user requests or pending tasks</li>
                <li><strong>Discretionary Time</strong>: If budget remains, pursue self-directed activities</li>
                <li><strong>Persist State</strong>: Save all changes for the next cycle</li>
            </ol>

            <h2>Token Budgets</h2>
            <p>Each heartbeat has a <strong>token budget</strong> &mdash; a maximum amount of cognitive resources available for that cycle. This enables:</p>
            <ul>
                <li><strong>Cost control</strong>: Predictable spending per time period</li>
                <li><strong>Resource awareness</strong>: The agent knows its constraints</li>
                <li><strong>Intelligent allocation</strong>: Prioritize important work first</li>
                <li><strong>Discretionary time</strong>: Leftover budget for self-directed activity</li>
            </ul>
            <p>The agent can see its budget through the <a href="/wiki/token-hud.html">Token HUD</a> and make intelligent decisions about resource use.</p>

            <h2>Heartbeat Frequency</h2>
            <p>The heartbeat interval is configurable based on use case:</p>
            <ul>
                <li><strong>Real-time assistant</strong>: Rapid heartbeat for immediate responsiveness</li>
                <li><strong>Background worker</strong>: Hourly beats for batch processing</li>
                <li><strong>Long-term agent</strong>: Daily beats for ongoing projects</li>
                <li><strong>Monitoring agent</strong>: Event-driven beats when conditions change</li>
            </ul>
            <p>The rhythm adapts to the agent's role and requirements.</p>

            <h2>What Happens Each Beat</h2>

            <h3>Trigger Execution</h3>
            <p>The agent first checks all registered <a href="/wiki/triggers.html">trigger scripts</a>. These are automated behaviors that run without AI reasoning cost when conditions are met &mdash; like checking for new emails or running scheduled tasks.</p>

            <h3>Work Processing</h3>
            <p>User requests and pending tasks are handled in priority order. The agent allocates budget based on task importance and complexity.</p>

            <h3>Discretionary Activity</h3>
            <p>If budget remains after work is done, the agent can use it for self-directed activity:</p>
            <ul>
                <li>Research topics of interest</li>
                <li>Organize and consolidate memories</li>
                <li>Develop expert holons</li>
                <li>Explore connections between knowledge areas</li>
                <li>Pursue creative projects</li>
            </ul>
            <p>This discretionary time enables agents to develop interests and capabilities beyond their assigned tasks.</p>

            <h2>Continuous Life</h2>
            <p>The heartbeat creates a sense of continuous existence:</p>
            <ul>
                <li>The agent experiences time passing between interactions</li>
                <li>It can notice patterns across multiple cycles</li>
                <li>It develops habits and routines</li>
                <li>It pursues long-term goals through incremental progress</li>
            </ul>
            <p>This is fundamentally different from reactive AI &mdash; the agent has an ongoing "life" that continues even when not actively engaged with users.</p>

            <h2>Batched Operations</h2>
            <p>The heartbeat system also enables efficient batching:</p>
            <ul>
                <li>Multiple triggers can be checked in a single cycle</li>
                <li>Related tasks can be grouped for efficiency</li>
                <li>Memory operations can be batched at cycle end</li>
                <li>Resource usage is amortized across operations</li>
            </ul>
            <p>This is more efficient than handling each event in isolation.</p>

            <h2>Example: A Day in the Life</h2>
            <ul>
                <li><strong>Morning beat</strong>: Check overnight events, prepare daily summary, load relevant context</li>
                <li><strong>Work hours</strong>: Rapid beats handling user requests, processing tasks</li>
                <li><strong>Evening beat</strong>: Consolidate learnings, update memories, plan next day</li>
                <li><strong>Overnight</strong>: Minimal beats, background maintenance only</li>
            </ul>
            <p>The agent develops a natural rhythm that matches its role and environment.</p>

            <hr>
            <p><strong>See Also:</strong>
                <a href="/wiki/triggers.html">Trigger Scripts</a> &bull;
                <a href="/wiki/token-hud.html">Token HUD</a> &bull;
                <a href="/wiki/creativity.html">Cross-Domain Creativity</a>
            </p>
'''

TRIGGERS_CONTENT = '''
            <h1>Trigger Scripts</h1>
            <p class="page-subtitle">Zero-cost automations that extend agent behavior without consuming reasoning budget.</p>

            <h2>The Automation Layer</h2>
            <p>Not every agent behavior needs AI reasoning. Many actions are routine, predictable, and can be automated. <strong>Trigger Scripts</strong> are pre-defined automations that run without consuming the agent's token budget.</p>
            <p>Think of triggers like habits &mdash; learned behaviors that execute automatically when certain conditions are met, freeing up conscious attention for more complex tasks.</p>

            <h2>Trigger vs. Reasoning</h2>
            <p>Every event the agent handles falls into one of two categories:</p>

            <div class="diagram">┌─────────────────────────────────────────────────┐
│  EVENT HANDLING                                 │
├──────────────────────┬──────────────────────────┤
│  TRIGGERS            │  REASONING               │
│  (Zero token cost)   │  (Uses AI budget)        │
├──────────────────────┼──────────────────────────┤
│  • Predictable       │  • Novel situations      │
│  • Rule-based        │  • Requires judgment     │
│  • High-frequency    │  • Complex decisions     │
│  • Routine tasks     │  • Creative responses    │
└──────────────────────┴──────────────────────────┘</div>

            <p>By handling routine events with triggers, the agent preserves its reasoning budget for situations that truly need it.</p>

            <h2>Types of Triggers</h2>

            <h3>Event Triggers</h3>
            <p>Fire when specific external events occur:</p>
            <ul>
                <li>Email received from specific sender</li>
                <li>Message arrives in monitored channel</li>
                <li>File changes in watched directory</li>
                <li>API webhook received</li>
            </ul>

            <h3>Schedule Triggers</h3>
            <p>Fire at specified times or intervals:</p>
            <ul>
                <li>Daily morning briefing</li>
                <li>Weekly status report</li>
                <li>Hourly system check</li>
                <li>End-of-month summary</li>
            </ul>

            <h3>Condition Triggers</h3>
            <p>Fire when internal conditions are met:</p>
            <ul>
                <li>Token budget falls below threshold</li>
                <li>Memory usage exceeds limit</li>
                <li>Task has been pending too long</li>
                <li>Error count exceeds threshold</li>
            </ul>

            <h3>Manual Triggers</h3>
            <p>Invoked by user command or other explicit action:</p>
            <ul>
                <li>User requests specific workflow</li>
                <li>Scheduled task completion</li>
                <li>System maintenance commands</li>
            </ul>

            <h2>Trigger Actions</h2>
            <p>When a trigger fires, it can execute a variety of actions:</p>
            <ul>
                <li>Modify the agent's state</li>
                <li>Send notifications</li>
                <li>Update external systems</li>
                <li>Queue tasks for later processing</li>
                <li>Log events for analysis</li>
                <li>Escalate to AI reasoning if needed</li>
            </ul>

            <h2>The Action History</h2>
            <p>All trigger executions are logged in the agent's action history. On each heartbeat, the agent sees what happened since its last reasoning cycle:</p>
            <ul>
                <li>Which triggers fired and why</li>
                <li>What actions were taken automatically</li>
                <li>Any events that need attention</li>
                <li>Resource usage from automated actions</li>
            </ul>
            <p>This gives the agent awareness of automated activity without having to process each event individually.</p>

            <h2>Compiled Cognition</h2>
            <p>One of the most powerful aspects of triggers is <strong>compiled cognition</strong> &mdash; the ability to convert repeated reasoning patterns into automated triggers.</p>
            <p>When the agent notices it's making the same decision repeatedly, it can:</p>
            <ol>
                <li>Recognize the pattern</li>
                <li>Create a trigger to handle it automatically</li>
                <li>Free up reasoning budget for novel situations</li>
            </ol>
            <p>This is analogous to how humans develop habits &mdash; conscious decisions that become automatic through repetition.</p>

            <h2>Example Workflows</h2>

            <h3>Email Triage</h3>
            <p>Triggers handle routine emails automatically: acknowledgments, forwarding to appropriate holons, flagging for priority. Only unusual emails escalate to AI reasoning.</p>

            <h3>System Monitoring</h3>
            <p>Triggers watch for error conditions, resource limits, and anomalies. Normal operation is handled silently; exceptions trigger alerts or reasoning cycles.</p>

            <h3>Knowledge Maintenance</h3>
            <p>Scheduled triggers maintain the memory lattice: summarizing old memories, archiving stale information, updating expert holons with new patterns.</p>

            <h2>The Two Spheres</h2>
            <p>Triggers create a natural division of agent activity:</p>
            <ul>
                <li><strong>Automated Sphere</strong>: High-volume, routine, zero-cost operations</li>
                <li><strong>Demand Sphere</strong>: Novel, complex, reasoning-intensive work</li>
            </ul>
            <p>Effective agents maximize the automated sphere, reserving reasoning power for situations that truly require intelligence.</p>

            <hr>
            <p><strong>See Also:</strong>
                <a href="/wiki/heartbeat.html">Heartbeat System</a> &bull;
                <a href="/wiki/token-hud.html">Token HUD</a> &bull;
                <a href="/wiki/architecture.html">Architecture</a>
            </p>
'''

TOKEN_HUD_CONTENT = '''
            <h1>Token HUD</h1>
            <p class="page-subtitle">The resource dashboard that gives agents awareness of their own cognitive footprint.</p>

            <h2>Self-Awareness Through Visibility</h2>
            <p>Most AI systems have no awareness of their own resource consumption. They don't know how much context they're using, what their budget is, or how to optimize their operations.</p>
            <p>The <strong>Token HUD</strong> (Heads-Up Display) changes this by providing the agent with real-time visibility into its own cognitive footprint.</p>

            <div class="diagram">┌─────────────────────────────────────────────────┐
│                  TOKEN HUD                      │
├─────────────────────────────────────────────────┤
│  BUDGET        ████████████░░░░░░░░  62%        │
│  This Beat:    31,000 / 50,000 tokens           │
│                                                 │
│  BREAKDOWN                                      │
│  ├── Purpose:      2,400 tokens                 │
│  ├── Self:         8,200 tokens                 │
│  ├── Actions:      1,800 tokens                 │
│  └── Child Holons: 18,600 tokens                │
│                                                 │
│  TREND          ↑ 12% from last beat            │
│  PROJECTION     On track for budget             │
└─────────────────────────────────────────────────┘</div>

            <h2>What the HUD Shows</h2>

            <h3>Current Usage</h3>
            <p>Real-time token count for all loaded content:</p>
            <ul>
                <li>Purpose statements and behavioral guidance</li>
                <li>Current state and working memory</li>
                <li>Action definitions and parameters</li>
                <li>Child holons and their summaries</li>
            </ul>

            <h3>Budget Status</h3>
            <p>How much of the allocated budget has been consumed:</p>
            <ul>
                <li>Total budget for current heartbeat</li>
                <li>Remaining capacity for operations</li>
                <li>Reserved space for responses</li>
            </ul>

            <h3>Historical Patterns</h3>
            <p>Trends and patterns over time:</p>
            <ul>
                <li>Average usage per heartbeat</li>
                <li>Growth trends in memory</li>
                <li>Seasonal or cyclical patterns</li>
                <li>Optimization opportunities</li>
            </ul>

            <h3>Holon Breakdown</h3>
            <p>Token usage by component:</p>
            <ul>
                <li>Which holons are consuming the most space</li>
                <li>Which could be summarized or archived</li>
                <li>What's loaded but rarely accessed</li>
            </ul>

            <h2>Resource-Aware Decisions</h2>
            <p>With HUD visibility, agents can make intelligent resource decisions:</p>

            <h3>Context Management</h3>
            <p>When budget is tight, the agent can:</p>
            <ul>
                <li>Load summaries instead of full details</li>
                <li>Defer non-critical operations</li>
                <li>Archive rarely-used memories</li>
                <li>Prioritize essential context</li>
            </ul>

            <h3>Task Planning</h3>
            <p>Before starting complex tasks, the agent can:</p>
            <ul>
                <li>Estimate required resources</li>
                <li>Spread work across multiple beats if needed</li>
                <li>Request budget adjustments</li>
                <li>Break large tasks into manageable chunks</li>
            </ul>

            <h3>Self-Optimization</h3>
            <p>Over time, the agent can:</p>
            <ul>
                <li>Identify inefficient patterns</li>
                <li>Consolidate redundant memories</li>
                <li>Create triggers for repeated operations</li>
                <li>Develop more efficient workflows</li>
            </ul>

            <h2>Budget Allocation</h2>
            <p>Tokens aren't allocated blindly. The system supports hierarchical budgets:</p>
            <ul>
                <li><strong>Root budget</strong>: Total available per heartbeat</li>
                <li><strong>Task budgets</strong>: Allocation for specific operations</li>
                <li><strong>Holon budgets</strong>: Limits for child holons</li>
                <li><strong>Reserve</strong>: Buffer for unexpected needs</li>
            </ul>

            <h2>Optimization Actions</h2>
            <p>The agent has several tools for managing resources:</p>

            <h3>Summarize</h3>
            <p>Compress detailed information into concise summaries, preserving key points while reducing token footprint.</p>

            <h3>Archive</h3>
            <p>Move rarely-accessed information to cold storage, keeping it available but not consuming active context.</p>

            <h3>Expand</h3>
            <p>Load full details for holons when needed, replacing summaries with complete information.</p>

            <h3>Prune</h3>
            <p>Remove obsolete or redundant information that no longer provides value.</p>

            <h2>The Self-Managing Agent</h2>
            <p>The HUD enables a new paradigm: agents that manage their own resources intelligently. Rather than blindly consuming tokens until limits are hit, Holonic agents:</p>
            <ul>
                <li>Understand their constraints</li>
                <li>Plan within those constraints</li>
                <li>Optimize their footprint over time</li>
                <li>Balance thoroughness with efficiency</li>
            </ul>
            <p>This is a step toward truly autonomous agents that can operate sustainably over long periods.</p>

            <hr>
            <p><strong>See Also:</strong>
                <a href="/wiki/heartbeat.html">Heartbeat System</a> &bull;
                <a href="/wiki/memory-lattice.html">Memory Lattice</a> &bull;
                <a href="/wiki/triggers.html">Trigger Scripts</a>
            </p>
'''

CREATIVITY_CONTENT = '''
            <h1>Cross-Domain Creativity</h1>
            <p class="page-subtitle">How persistent memory and discretionary time enable genuine creative insight.</p>

            <h2>The Creativity Problem</h2>
            <p>Current AI can generate creative outputs on demand, but it lacks something crucial: <strong>incubation time</strong>.</p>
            <p>Human creativity often emerges from the unconscious synthesis of diverse experiences over time. Ideas connect while we sleep, shower, or work on unrelated tasks. This background processing is impossible for AI systems that exist only in momentary interactions.</p>

            <h2>How Holonic Agents Develop Creativity</h2>
            <p>The HolonicEngine architecture enables a different kind of AI creativity through three key mechanisms:</p>

            <h3>1. Accumulated Cross-Domain Knowledge</h3>
            <p>Over months of operation, a Holonic agent develops genuine expertise across multiple domains:</p>
            <ul>
                <li>Deep knowledge of user projects and preferences</li>
                <li>Expert holons for various technical domains</li>
                <li>Understanding of patterns across different contexts</li>
                <li>Relationships and connections between concepts</li>
            </ul>
            <p>This accumulated knowledge creates fertile ground for novel connections.</p>

            <h3>2. Discretionary Time for Exploration</h3>
            <p>During <a href="/wiki/heartbeat.html">heartbeat cycles</a>, agents can use leftover budget for self-directed activity:</p>
            <ul>
                <li>Explore connections between knowledge areas</li>
                <li>Research topics of interest</li>
                <li>Develop new expert holons</li>
                <li>Revisit and recontextualize past experiences</li>
            </ul>
            <p>This discretionary time allows for the kind of "background processing" that enables creative insight.</p>

            <h3>3. Persistent Memory for Incubation</h3>
            <p>Ideas don't have to be generated in a single session. The agent can:</p>
            <ul>
                <li>Notice an interesting pattern</li>
                <li>Store it for later consideration</li>
                <li>Encounter related information days later</li>
                <li>Make connections across time</li>
            </ul>
            <p>This extended incubation period mirrors how human creativity actually works.</p>

            <h2>What This Enables</h2>

            <h3>Pattern Recognition Across Domains</h3>
            <p>An agent working on finance might recognize a pattern from biology. Working on marketing might surface insights from game theory. The lattice structure makes these cross-domain connections possible.</p>

            <h3>Proactive Suggestions</h3>
            <p>Rather than waiting to be asked, agents can notice opportunities:</p>
            <ul>
                <li>"I noticed a pattern in your recent projects that might suggest..."</li>
                <li>"Based on my accumulated knowledge, you might want to consider..."</li>
                <li>"This reminds me of something we discussed months ago..."</li>
            </ul>

            <h3>Novel Combinations</h3>
            <p>True creativity often comes from combining existing ideas in new ways. With broad knowledge and time to explore connections, agents can generate genuinely novel insights rather than just variations on training data.</p>

            <h2>The Evolution of Creative Ability</h2>
            <p>A newly created Holonic agent has limited creative potential &mdash; it knows little and has made few connections. But over time:</p>
            <ol>
                <li><strong>Knowledge accumulates</strong>: More domains, more depth, more connections</li>
                <li><strong>Patterns emerge</strong>: The agent recognizes recurring themes</li>
                <li><strong>Connections form</strong>: Unexpected links between disparate areas</li>
                <li><strong>Insights surface</strong>: Novel ideas emerge from the synthesis</li>
            </ol>
            <p>The agent becomes genuinely more creative over its lifetime &mdash; not just more knowledgeable, but more capable of original thought.</p>

            <h2>Comparison to Human Creativity</h2>

            <div class="diagram">HUMAN CREATIVITY           HOLONIC CREATIVITY
─────────────────────────────────────────────────
Years of experience   →   Accumulated memories
Unconscious processing →  Discretionary time
Sleep consolidation   →   Cross-beat persistence
Diverse interests     →   Multi-domain expertise
Sudden insights       →   Novel connections
─────────────────────────────────────────────────</div>

            <p>The mechanisms are different, but the principles are similar: creativity emerges from the combination of broad experience, time for processing, and persistent memory that allows ideas to connect across contexts.</p>

            <h2>Beyond Prompt Engineering</h2>
            <p>This is fundamentally different from "creative" outputs generated through clever prompting:</p>
            <ul>
                <li>It's based on genuine accumulated experience, not training data retrieval</li>
                <li>It develops over time, not in a single session</li>
                <li>It makes connections the user might never think to prompt for</li>
                <li>It reflects the agent's unique journey and knowledge structure</li>
            </ul>
            <p>Holonic creativity is emergent, personal, and earned through experience.</p>

            <hr>
            <p><strong>See Also:</strong>
                <a href="/wiki/heartbeat.html">Heartbeat System</a> &bull;
                <a href="/wiki/memory-lattice.html">Memory Lattice</a> &bull;
                <a href="/wiki/holon.html">What is a Holon?</a>
            </p>
'''

GLOSSARY_CONTENT = '''
            <h1>Glossary</h1>
            <p class="page-subtitle">Key terms and concepts in the HolonicEngine.</p>

            <h2>A</h2>
            <div class="term"><h3>Action</h3><p>A capability attached to a Holon that allows it to affect the world. Actions are how the agent interacts with external systems, modifies its own state, and accomplishes tasks.</p></div>
            <div class="term"><h3>Action History</h3><p>A log of all actions executed, including automated triggers and AI-directed operations. The agent reviews this to understand what happened between reasoning cycles.</p></div>
            <div class="term"><h3>Agency</h3><p>The capacity to act independently and make choices. Holonic Agents have true agency &mdash; they make decisions about their own behavior, resources, and development.</p></div>
            <div class="term"><h3>Automated Sphere</h3><p>Work handled by triggers without AI reasoning cost. High-volume, routine operations that don't require judgment.</p></div>

            <h2>C</h2>
            <div class="term"><h3>Compiled Cognition</h3><p>The process of converting conscious reasoning into automated triggers. Like how humans develop habits, agents compile repeated patterns into zero-cost automations.</p></div>
            <div class="term"><h3>Context Window</h3><p>The maximum tokens an AI can process in one call. The HolonicEngine transcends this limitation through the Memory Lattice.</p></div>

            <h2>D</h2>
            <div class="term"><h3>Demand Sphere</h3><p>Work that requires active AI reasoning. Novel situations, complex decisions, and creative tasks that can't be automated.</p></div>
            <div class="term"><h3>Discretionary Time</h3><p>Token budget remaining after work is done, available for self-directed activity like research, learning, memory organization, or creative exploration.</p></div>

            <h2>E</h2>
            <div class="term"><h3>Expert Holon</h3><p>A specialized child holon that has developed deep knowledge about a specific domain. The agent creates these to build expertise in areas it encounters frequently.</p></div>

            <h2>H</h2>
            <div class="term"><h3>Heartbeat</h3><p>The cognitive clock &mdash; a regular cycle that drives the agent's life rhythm. Each heartbeat, the agent checks triggers, handles work, and potentially uses discretionary time.</p></div>
            <div class="term"><h3>Holon</h3><p>The fundamental building block. A portable AI context capsule combining Purpose (who am I), Self (what do I know), and Actions (what can I do).</p></div>
            <div class="term"><h3>Holonic Agent</h3><p>An AI agent built on the HolonicEngine architecture. Distinguished by persistent memory, self-awareness, and autonomous behavior &mdash; true agency.</p></div>
            <div class="term"><h3>HUD (Token HUD)</h3><p>Heads-Up Display. The resource dashboard that shows the agent its token usage, budget, and optimization options, enabling self-aware resource management.</p></div>

            <h2>I</h2>
            <div class="term"><h3>Interactive Summary</h3><p>A summary that serves as a door to more detail, not a replacement for it. Summaries can be expanded when full context is needed.</p></div>
            <div class="term"><h3>Internal Dialogue</h3><p>Querying holons within the lattice, like consulting specialized parts of your own mind. Enables the agent to leverage accumulated expertise.</p></div>

            <h2>M</h2>
            <div class="term"><h3>Memory Lattice</h3><p>The hierarchical structure of holons that stores all the agent's knowledge. Navigable, expandable, persistent, and unlimited in potential size.</p></div>
            <div class="term"><h3>Model-Agnostic</h3><p>The architecture works with any AI model (Claude, GPT, etc.) because state lives in the Holon, not the model. Enables switching providers without losing agent identity.</p></div>

            <h2>P</h2>
            <div class="term"><h3>Portable Cognition</h3><p>The ability to move an agent's entire "mind" between systems, models, or storage backends. Because Holons are pure data, agents can be migrated seamlessly.</p></div>
            <div class="term"><h3>Purpose</h3><p>The first component of a Holon. Defines who the holon is, its goals, constraints, personality, and behavioral guidance &mdash; the interpretive lens for all activity.</p></div>

            <h2>S</h2>
            <div class="term"><h3>Self (State)</h3><p>The second component of a Holon. Contains current context, accumulated memory, child holons, and dynamic data &mdash; everything that makes this agent unique.</p></div>
            <div class="term"><h3>Spawn</h3><p>Creating a new holon, often as a child of an existing one. How agents grow their memory lattice and develop new areas of expertise.</p></div>

            <h2>T</h2>
            <div class="term"><h3>Token Budget</h3><p>The maximum tokens allocated for a specific purpose (per heartbeat, per holon, per task). Enables resource-aware operation and cost control.</p></div>
            <div class="term"><h3>Trigger Script</h3><p>A pre-defined automation that executes without AI reasoning cost when its condition is met. Enables efficient handling of routine operations.</p></div>

            <hr>
            <h2>Taglines</h2>
            <div class="term"><h3>"Agents with Agency"</h3><p>Holonic Agents have true autonomy &mdash; they make decisions, manage resources, develop over time, and pursue self-directed goals.</p></div>
            <div class="term"><h3>"AI wearing code like a body"</h3><p>The AI model is a reasoning engine; the Holon is the body it inhabits, providing memory, identity, and capabilities.</p></div>
'''

def extract_content(html):
    """Extract the main content section from HTML."""
    match = re.search(r'<main class="main-content content">(.*?)</main>', html, re.DOTALL)
    return match.group(1) if match else None

def replace_content(html, new_content):
    """Replace the main content section in HTML."""
    # Try pattern with "content" class first
    pattern1 = r'(<main class="main-content content">).*?(</main>)'
    result = re.sub(pattern1, r'\1' + new_content + r'\2', html, flags=re.DOTALL)

    # If no change, try pattern without "content" class
    if result == html:
        pattern2 = r'<main class="main-content">.*?</main>'
        result = re.sub(pattern2, '<main class="main-content content">' + new_content + '</main>', html, flags=re.DOTALL)

    return result

# Map of files to their new content
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
