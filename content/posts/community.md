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
description = "Desc Text."
canonicalURL = "https://canonical.url/to/page"
disableHLJS = true # to disable highlightjs
disableShare = false
hideSummary = false
searchHidden = true
ShowReadingTime = true
ShowBreadCrumbs = true
ShowPostNavLinks = true
ShowWordCount = true
ShowRssButtonInSectionTermList = true
UseHugoToc = true

[cover]
image = "/images/react_cover.png"
alt = "React is no magic"
caption = "<text>"
relative = false # when using page bundles set this to true
hidden = true # only hide on current single page

[editPost]
URL = "https://github.com/<path_to_repo>/content"
Text = "Suggest Changes" # edit text
appendFilePath = true # to append file path to Edit link
+++
![React Cover](/images/react_cover.png)

# Under the Hood of React: Why It Feels Like Magic (But Isn’t)

## Why this Blog

When I was starting web, it was a very digestible scenario — HTML formed the structure, CSS was all beautiful decorations (and some movements), and JS brought logic and life to the site.

But, as any dev would have it, I encountered React. And oh boy, it is magical — yes, almost like you now know the language of elves and can craft spectacular sites.

This was awesome, but like many devs who are engineers, I too had this tickling feeling to know what is under the hood of React.

I dived deep and was amazed by the mechanisms behind those state changes.  
It’s one of those feelings like a person has for their car. Sure, they only need to know how to drive it, but knowing how things work under the hood just elevates you as a better driver.

This blog is about going **under the hood** of React! (React 16+)

---

## Why We Needed React

![React Meme](/images/why_react.jpg)

Before React, we relied on servers to cook up the HTML and serve it whenever a button was clicked or a transition was expected (reason why we used `preventDefault()`).

But that wasn't the era of Starlink satellites shipping fast internet across the world — it took time to load entire pages from the server.

Facebook (Gen Z name: META) was facing challenges in maintaining its News Feed, which was experiencing rapid growth and complexity.

**The idea was — what if DOM manipulation could be done efficiently on the client side with compute-optimized algorithms?**  
Voila! That is the core idea behind React.

React was initially deployed on Facebook’s News Feed in 2011, then on Instagram in 2012, and was later open-sourced!

---

## Baby Steps First!!

Before we dive into the complex mechanism behind React, it is necessary to know some intermediate terms and concepts.

---

### Fibre Tree

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

That’s your food for thought. The reconciliation process is (don’t worry if it doesn’t all make sense on the first read):

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

![React Cycle](/images/react_cycle.jpeg)

Or view the full diagram [here](https://lucid.app/lucidchart/060aaaf6-8f66-462f-a120-5bbe40b9a7f5/edit?viewport_loc=-831%2C-252%2C5026%2C2286%2C0_0&invitationId=inv_69925121-eac4-40e2-a476-3c1a739a31ee)

---

## 📚 Sources and Acknowledgements

- https://github.com/rohan-paul/Awesome-JavaScript-Interviews/blob/master/React/Virtual-DOM-and-Reconciliation-Algorithm.md  
- https://stackoverflow.com/questions/78909355/react-and-reconciliation-process/78909508#78909508  
- https://legacy.reactjs.org/docs/reconciliation.html  
- https://github.com/acdlite/react-fiber-architecture  
- https://www.velotio.com/engineering-blog/react-fiber-algorithm  
- https://github.com/koba04/react-fiber-resources  
- https://angular.love/inside-fiber-in-depth-overview-of-the-new-reconciliation-algorithm-in-react#Pre-mutation%20lifecycle%20methods  
