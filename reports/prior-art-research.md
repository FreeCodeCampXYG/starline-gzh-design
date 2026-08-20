# Prior-art research note

- Date: 2026-08-20
- Status: partial / missing evidence
- Intended queries: AI-assisted writing editor with inline rewrite and diff; WeChat HTML layout visual editor with SVG; AI resume editor with structured writing.
- Unified runner failed on Windows because the local `npx` executable was not discoverable (`WinError 2`). No catalog metrics are claimed.
- Web evidence reviewed separately: 微排版编辑器介绍、AI 智能排版实战、公众号 SVG 互动趋势、QuantumFloret/ai-editor、FunBlocks AI Markdown、Nimbalyst AI editing.
- Additional editor references: ProseMirror suggestion mode, Tiptap review changes/diff, Liveblocks Tiptap copilot, and Stet annotation-first editing. These support the proposed selection anchor, suggestion layer, atomic review, and undo design; they are reference projects/docs, not copied code.
- Adapt: block-level AI editing, explicit diff/accept/reject, structured resume mode, visual diagram insertion.
- Reject: claiming superiority from search snippets; direct copying of competitor interaction or proprietary assets.
- Invent: one shared document model with three render targets (editable draft, paste-safe HTML, technical SVG), plus provenance and rollback metadata.

## Sources
- https://weipaiban.cn/docs/introduction
- https://weipaiban.cn/blogs/article/6a400298fb81eb002e19785b/
- https://weipaiban.cn/blogs/article/6a256c2271d7ba002d86a9a0/
- https://github.com/QuantumFloret/ai-editor
- https://www.producthunt.com/p/ai-powered-markdown-text-editor/rethinking-ai-assisted-writing-the-editor-as-shared-workspace
- https://nimbalyst.com/blog/how-best-to-edit-ai-text/
- https://www.npmjs.com/package/prosemirror-suggestion-mode
- https://tiptap.dev/docs/ai/ai-toolkit/client/agents/review-changes/suggestions
- https://tiptap.dev/docs/content-ai/capabilities/ai-toolkit/api-reference/display-suggestions
- https://liveblocks.io/blog/building-an-ai-copilot-inside-a-tiptap-text-editor
- https://github.com/filu123/stet
- https://weipaiban.cn/blogs/article/699fbfd96796b3002c81eae1/