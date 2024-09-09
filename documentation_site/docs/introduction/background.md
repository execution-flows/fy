# Background

The motivation behind the creation of the _Execution Flows_ ___fy___ [pronounced _fai_] tool stems from the need to deliver large, complex projects with hundreds of different use cases. These are common in Enterprise Software, where you often need to:

1. Deliver specific customizations for customers.
2. Integrate with various external vendors, automation tools, CRMs, payment systems, data feeds, communication channels, etc.
3. Maintain variations of use cases for different user groups, such as customer support, operations, billing and finance, regulatory compliance, security, and more.

This is particularly important where there is a need for a reusability at the sub-line-of-code level. In such cases, implementing variations of use cases often leads to significant code duplication because the required changes are subtle, affecting almost every line of code.

To address this challenge, the _Execution Flows_ approach takes the well-known Object-Oriented Programming (OOP) concept of [class mixins](https://en.wikipedia.org/wiki/Mixin) and elevates it to a first-class citizen—an entity used to deliver entire functionality. Just as an object is central to OOP and a function is to Functional Programming (FP), a flow is central to the _Execution Flows_ programming paradigm. And flows are exclusively constructed from mixins.

Managing your code through mixins allows you to break it down into the smallest possible chunks. These mixins are then assembled into what is called a `flow` class. The ___fy___ tool generates the boilerplate Python code for both the mixin classes and the top-level flow classes, allowing you, the developer, to focus on what truly matters: code structure and application logic.
