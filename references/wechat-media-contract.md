# 微信公众号媒体与嵌入合同

## 发布层允许

- `<img>` 加公网 `http(s)` URL；本地路径必须先图床。
- PNG、JPEG、GIF 作为默认发布资产。
- GIF 应准备静态首帧或降级 PNG。
- 外链正文使用脚注化参考资料，不保留可点击 `<a>`。

## 发布层禁止

- `<script>`、`<style>`、`<div>`、外部 CSS/JS、`foreignObject`；
- SVG、SVG data URI、`data:image/svg+xml` 作为默认公众号正文媒体；
- `javascript:`、`data:`、`vbscript:` 等危险协议；
- 相对路径、绝对本地路径、未确认的私有资源；
- 离线交互 HTML 直接混入复制正文。

## 技术图降级

Fireworks 的 SVG 是工作区可编辑源。进入公众号发布层时，优先导出 PNG；用户明确需要动画时可用 GIF，但仍保留静态降级图。若渲染器或视觉复核失败，应报告失败，不宣称已通过。
