# fireworks-tech-graph 接入说明

本 Skill 不复制 `fireworks-tech-graph` 的完整资源；运行时从已安装的 `C:\Users\xiaoy\.agents\skills\fireworks-tech-graph` 读取其 SKILL.md、参考文档与脚本。

## 路由

当用户要求流程图、架构图、数据流、Agent/记忆系统、时序图、关系图、技术概念图、SVG、PNG 或 GIF 时：

1. 先把事实整理为图类型、节点、边、方向、标签和语义颜色；缺失工程事实必须标为未知，不凭空补齐。
2. 读取 Fireworks 技能要求的布局质量合同和对应风格；默认 Flat Icon，用户明确要求时使用指定风格。
3. 用其生成器或 Python 列表法写 SVG；优先保留 JSON/结构化源数据。
4. 运行 `validate-svg.sh` 或 `fireworks.py validate`，再导出 PNG；需要动效时只按 Fireworks 的 GIF 合同执行。
5. 视觉复核可用时读取 PNG；不可用时明确报告 `visual_review: skipped`。
6. 嵌入微信公众号前，默认使用 PNG/JPEG/GIF 或经过微信兼容转换的安全 SVG。不要把 `<script>`、`<style>`、`foreignObject`、外部资源或离线交互 HTML 放入正文。

## 交付物

- `<name>.json`：可编辑节点/边源数据；
- `<name>.svg`：技术图可编辑源；
- `<name>.png`：发布/预览资源；
- `<name>.report.json`：校验报告；
- 可选 `<name>.gif`：仅在用户明确要求动效时生成；
- HTML 正文中只引用通过资源检查的最终文件。

## 编辑约束

用户修改图表时只改源数据中的节点、边、标签或布局提示，再重新生成和校验；不要直接手改最终 SVG 后跳过校验。图表差异要记录 before/after，接受后才进入正文。
