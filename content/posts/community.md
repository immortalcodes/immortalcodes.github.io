+++
title = "React ≠ Magic"
date = 2025-06-09T12:00:00+01:00

tags = ["community"]
author = "Madhur"
showToc = true
TocOpen = false
draft = false
hidemeta = false
comments = false
description = "Understanding workings of React"
canonicalURL = "https://canonical.url/to/page"
disableHLJS = true # to disable highlightjs
disableShare = false
hideSummary = false
searchHidden = false
ShowReadingTime = true
ShowBreadCrumbs = true
ShowPostNavLinks = true
ShowWordCount = true
ShowRssButtonInSectionTermList = true
UseHugoToc = true

[cover]
image = "/images/react_cover_2.png"
alt = "React is no magic"
caption = "cover"
relative = false # when using page bundles set this to true
hidden = true # only hide on current single page

[editPost]
URL = "https://github.com/immortalcodes/immortalcodes.github.io/issues/new"
Text = "Suggest Changes" # edit text
appendFilePath = false # to append file path to Edit link
+++
![React Cover](/images/react_cover_2.png)

# Under the Hood of React: Why It Feels Like Magic (But Isn’t)

## Why this Blog

Back in school days starting with web development was fairly simple — HTML formed the structure, CSS was all beautiful decorations (and some movements), and JS brought logic and life to the site.

But, as any dev would have it, I encountered React. And oh boy, it seemed magical — yes, almost like you now know the language of elves and can now craft spectacular *Elden sites*.

This was awesome, but the engineer within me was curious, I had this tickling feeling to know what is under the hood of React.

I dived deep and was amazed by the mechanisms behind those state changes and process of DOM painting!
It’s one of those feelings like a person has for their car. Sure, they only need to know how to drive it, but knowing how things work under the hood just elevates your level and you really own the machine.

This blog is about going **under the hood** of React! (React 16+)
---

## Why We Needed React

![React Meme](/images/why_react.jpg)

Before React, we relied on servers to cook up the HTML and serve it whenever a button was clicked or a transition was expected (reason why we used `preventDefault()`). This is SSR (Server Side Rendering), where we prepare HTML files in the backend and serve them every time user demands something, examples include templating engines like JINJA and TWIG (PHP).
But that wasn't the era of Starlink satellites shipping fast internet across the world — it took time to load entire pages from the server. Time was progressing and people had more powerful devices on client side and that meant that now logic could operate on client and *move* things.

Facebook (Gen Z name: META) was facing challenges in maintaining its News Feed, which was experiencing rapid growth and complexity.

**The idea was — what if DOM manipulation could be done efficiently on the client side with compute-optimized algorithms?**  
Voila! That is the core idea behind React.
React was initially deployed on Facebook’s News Feed in 2011, then on Instagram in 2012, and was later open-sourced!

**Sites nowadays**
While I talk about SSR and client side computations, they are not two far ends in today's scenario, they form a spectrum where application/sites choose what they need to compute at servers and what they need for clients to handle, it's far too complex and practically no tech-stack is exactly a CSR or SSR, they all fall in between somewhere of this vast spectrum.  

*after this section I assume you are already familiar with using react for development purposes*

---

## Baby Steps First!!

Food for thought:

- The broader idea is that we need a **logic** that *reacts* when interactions happen on web. 
- It needs a structure to know what elements are there on the page, what things could change or be interacted with?
- How to know changes are required on a webpage?
- Strategize and optimally apply changes when they are needed?
- All this and more has to happen quickly, consuming low memory space and the entire transition should be seamless. 

Before we dive into the complex mechanism behind React, it is necessary to know some intermediate terms and concepts.


---

### Fiber Tree

With React 16, the Fiber architecture was introduced. It is basically a linked list of Fiber nodes where each node represents:

- The component type (class, function, host)
- Its instance/state
- Input props
- Output elements
- Links to parent, child, and sibling fibers
- Relation to the work-in-progress alternate fiber
- Effect flags indicating DOM operations needed
- Lanes indicating the priority of the update
- Batching information

#### Did you see what we did there?

We can group the information stored in a fiber as:

- A virtual representation of the actual DOM element  
- Info about its parents and siblings  
- State information and actions to be performed  
- Optimization information for React Engine (Batching and Priority)

React keeps **two trees** for every **trigger**:

- `current` → the tree currently committed to the DOM  
- `workInProgress` → the tree being prepared for the next commit

---

### Reconciliation Process

Before we discuss this, you need to know what a *trigger* is — in simple terms, a change. That is the philosophy of React: to *react* to a change.

Some button was pressed, things were loaded, notifications sent, forms submitted — could be anything.

So, how do we decide what this change should do to our browser screen (the pixels a user sees)?
The reconciliation process is (don’t worry if it doesn’t all make sense on the first read):

1. **Identifying the change**  
2. **Determining the most optimized steps that should be added to the Fiber tree**  
3. **Adding the steps to the corresponding nodes**

#### Assumptions

- **Element Types**: React assumes that elements of different types generate different DOM trees.  
- **Key Prop**: Developers can use the `key` prop to hint which child elements remain stable across renders. This helps React efficiently reorder, reuse, and re-render DOM nodes.

---

### Reconciliation vs Rendering

The DOM is just one rendering environment React can target — others include native iOS and Android views via React Native.

This is why "Virtual DOM" is a bit of a misnomer.

React is designed so that **reconciliation** and **rendering** are separate phases:

- The **reconciler** computes which parts of the tree have changed.
- The **renderer** uses that information to update the UI.

Rendering is more like *painting* the web.

---

### Double Buffering

Double buffering, a technique used in graphics and video processing, minimizes flickering and improves performance. It involves using two memory spaces to store images or frames and switching between them to display the final image smoothly.

In React’s Fiber reconciliation, a similar approach is taken:

- When updates occur, a new Fiber tree is created to represent the updated UI state.
- Once this new tree reflects the expected UI, it replaces the current tree — similar to how video buffers are swapped.

#### Benefits:

- Improved performance and reduced flickering by avoiding unnecessary updates to the real DOM  
- Ability to compute the new UI state off-screen, allowing for easy discarding if a higher-priority update arises  
- Seamless pausing and resuming of reconciliation without disrupting the user’s view

---

## 🔄 The Entire Cycle

![React Cycle](/images/react_cycle.png)

Or view the full diagram [here](https://lucid.app/lucidchart/060aaaf6-8f66-462f-a120-5bbe40b9a7f5/edit?viewport_loc=-831%2C-252%2C5026%2C2286%2C0_0&invitationId=inv_69925121-eac4-40e2-a476-3c1a739a31ee)


I highly encourage you to visit the diagram and make sense out of it. React is fairly mature now and it has tons of complexity, this blog is over-simplified view of the entire thing. Right place to dive deep is some links given below and finally the [codebase](https://github.com/facebook/react) itself!

Having said that, let me throw some light:  
It all starts with **mounting** that is when the react page loads for the first time, based on what components and code has been used it forms a Virtual DOM representation which is complemented by **Fiber Tree** that actually stores real semantics and information of those components. 

When all this is formed we move to **Commit phase** and all this information is painted in an instant on the webpage that is the real DOM as we discussed in the concept of **Double Buffering**.
Since all the computations are already done and dusted, the painting phase is real quick and seamless.  
  
Now the interesting part..  
When a **trigger** happens which is basically a change that React is configured to "react" to, a new virtual representation is formed to compare if we need to go ahead and change something on DOM. 
Trigger doesn't mean that a change has to happen in DOM, which is a re-rendering has to be done, for example, if there was a button to set the counter to 0 and the counter was already 0, no change is required to be reflected on the web or the tree structure itself and react optimizes and avoids re-rendering in such cases.   
If there are changes we enter reconciliation process to compare current and **work-in-progress** trees to determine what needs to be changed, where should those changes be implemented and stored in the tree so that entire transition happens in a very optimal way. The process of determining this itself is quite compute efficient.
With react (18+), several new features were added to this process:
- Automatic Batching
- Concurrent Rendering
- Priority-based Updates
- Suspense Improvements  

All of them are possible due to heavy lifting done on fiber tree structures. Fiber tree supports **play-and-pause** functionality where updates to the tree could be prioritized, paused or aborted.  

Once we have done all this computations on our WIP tree which now has an update queue with all the updates that need to be painted on actual web, we start the committing phase where tree is traversed using a bottom up approach and changes make it to actual DOM. 

All this happens trigger after trigger giving a seamless experience to user despite such heavy computations and complexities.

---

## Acknowledgements
I am really thankful to people who were generous and propagated their knowledge on free web. These references were really helpful in understanding workings inside react. 
Do check them out!
- https://github.com/facebook/react
- https://github.com/acdlite/react-fiber-architecture  
- https://github.com/rohan-paul/Awesome-JavaScript-Interviews/blob/master/React/Virtual-DOM-and-Reconciliation-Algorithm.md  
- https://stackoverflow.com/questions/78909355/react-and-reconciliation-process/78909508#78909508  
- https://legacy.reactjs.org/docs/reconciliation.html  
- https://www.velotio.com/engineering-blog/react-fiber-algorithm  
- https://github.com/koba04/react-fiber-resources  
- https://angular.love/inside-fiber-in-depth-overview-of-the-new-reconciliation-algorithm-in-react#Pre-mutation%20lifecycle%20methods  

