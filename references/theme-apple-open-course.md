# 公众号排版组件库 —— 苹果公开课风（apple-open-course）

> 适合方法论、知识课、公开课笔记、商业框架与策略教程。设计目标是“先看懂，再行动”：先突出读者真正要完成的任务，再用课程编号、细线分隔和大留白组织步骤与证据。只吸收现代系统界面的秩序感，不使用 Apple 标识、产品图形或品牌文案，也不复刻任何官方页面。

## 目录

1. 设计变量
2. 主题专属组件
3. 完整文章骨架
4. 文章类型配方
5. Markdown 映射规则

---

## 一、设计变量

| 语义 | 色值 / 规则 | 用途 |
|---|---|---|
| 主墨色 | `#1D1D1F` | 标题、核心结论 |
| 正文灰 | `#424245` | 正文 |
| 辅助灰 | `#6E6E73` | 说明、来源、英文标签 |
| 线条灰 | `#D2D2D7` | 分隔线、矩阵边框 |
| 浅底色 | `#F5F5F7` | 课程导读、提示区 |
| 主色 | `#0066CC` | 课程编号、行动锚点、下划线 |
| 页面底 | `#FFFFFF` | 全文 |
| 字体 | 系统无衬线 | `-apple-system` 优先，不依赖外部字体 |
| 正文 | `15px / 1.9` | 手机端优先 |
| 圆角 | `0–12px` | 只给课程导读和提示，不做满篇卡片 |

### 视觉铁律

- 一篇只用蓝色作为主强调色；高频信息靠字重、细线和留白分层。
- 文章标题由公众号平台设置，正文不再重复一个超大 H1。
- 章节编号只做导航，可用 `STEP 01 / LESSON 01…`；主标题必须直接写读者任务，不能只写方法名。
- 用户点名的二八、STAR、四象限若只是整理手段，使用 11–12px 辅助灰小注，不占封面或前 3 个主标题。
- 组件以单层结构为主，不做卡片套卡片；四象限等关键关系使用全宽纵向卡片，不依赖 2×2 flex。
- 外层和关键内容区各自写明白底，防止公众号编辑器剥离最外层背景后变色。

---

## 二、主题专属组件

### 1. 最外层容器

```html
<section style="max-width:677px;margin:0 auto;background:#FFFFFF;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#424245;line-height:1.9;letter-spacing:0.2px;overflow-x:hidden;">
  <p style="margin:0;font-size:15px;line-height:1.9;color:#424245;"><span leaf="">正文内容</span></p>
</section>
```

### 2. 开场任务卡

用于文章最前面。不要复述平台标题，用一句读者任务和一句结果承诺打开正文；法则名仅在文章明确讲法则本身时进入此卡。

```html
<section style="margin:0 0 26px;padding:24px 20px;background:#F5F5F7;border-top:3px solid #0066CC;border-radius:0 0 12px 12px;">
  <p style="margin:0 0 10px;font-size:12px;line-height:1.4;color:#0066CC;font-weight:700;letter-spacing:1.2px;"><span leaf="">PRACTICAL GUIDE · 14 MIN</span></p>
  <p style="margin:0;font-size:24px;line-height:1.42;color:#1D1D1F;font-weight:800;"><span leaf="">怎么把账号从定位做到复盘</span></p>
  <p style="margin:10px 0 0;font-size:14px;line-height:1.8;color:#6E6E73;"><span leaf="">先说清楚服务谁，再选任务、写内容、做承接并看对结果。</span></p>
</section>
```

### 3. 前言正文

```html
<section style="margin:0 10px 24px;background:#FFFFFF;">
  <p style="margin:0 0 16px;font-size:15px;line-height:1.9;color:#424245;text-align:justify;"><span leaf="">很多人做内容，第一句话就是：“今天发什么？”</span></p>
  <p style="margin:0;font-size:15px;line-height:1.9;color:#424245;text-align:justify;"><span leaf="">这个问题问得太晚了。</span></p>
</section>
```

### 4. 课程导读

只展示最重要的 3 个学习结果，不列出全部章节。

```html
<section style="margin:0 10px 34px;padding:18px 16px;background:#F5F5F7;border-radius:12px;">
  <p style="margin:0 0 12px;font-size:12px;line-height:1.4;color:#6E6E73;font-weight:700;letter-spacing:1px;"><span leaf="">YOU WILL LEARN</span></p>
  <p style="margin:0 0 8px;font-size:14px;line-height:1.7;color:#1D1D1F;"><span style="color:#0066CC;font-weight:800;"><span leaf="">01</span></span><span leaf="">　用两条轴判断内容任务</span></p>
  <p style="margin:0 0 8px;font-size:14px;line-height:1.7;color:#1D1D1F;"><span style="color:#0066CC;font-weight:800;"><span leaf="">02</span></span><span leaf="">　写出标题、证据与站内承接</span></p>
  <p style="margin:0;font-size:14px;line-height:1.7;color:#1D1D1F;"><span style="color:#0066CC;font-weight:800;"><span leaf="">03</span></span><span leaf="">　按正确指标复盘，而不是只看点赞</span></p>
</section>
```

### 5. 章节分割线

```html
<section style="margin:42px 10px 34px;height:1px;line-height:1px;background:#D2D2D7;font-size:0;"><span leaf="">.</span></section>
```

### 6. 步骤／课程章节标题

```html
<section style="margin:0 10px 22px;background:#FFFFFF;">
  <p style="margin:0 0 7px;font-size:12px;line-height:1.4;color:#0066CC;font-weight:750;letter-spacing:1px;"><span leaf="">STEP 01 · ACCOUNT POSITION</span></p>
  <p style="margin:0;font-size:25px;line-height:1.38;color:#1D1D1F;font-weight:800;"><span leaf="">先把账号定位说成人话</span></p>
</section>
```

### 7. 正文段落

```html
<p style="margin:0 10px 16px;font-size:15px;line-height:1.9;color:#424245;text-align:justify;"><span leaf="">一端是用户需求。用户希望解决一个具体问题，少走一步弯路，或者更快作出选择。</span></p>
```

### 8. 左竖条小标题

```html
<p style="margin:26px 10px 12px;padding-left:12px;border-left:3px solid #0066CC;font-size:17px;line-height:1.55;color:#1D1D1F;font-weight:800;"><span leaf="">象限一：热点引流</span></p>
```

### 9. 正文关键词标记

```html
<span style="border-bottom:2px solid #0066CC;font-weight:650;color:#1D1D1F;"><span leaf="">先决定服务谁、希望活多久</span></span>
```

### 10. 核心结论

```html
<section style="margin:24px 10px;padding:17px 0 17px 18px;background:#FFFFFF;border-left:3px solid #0066CC;">
  <p style="margin:0;font-size:18px;line-height:1.75;color:#1D1D1F;font-weight:750;"><span leaf="">热点是输入，不是策略。</span></p>
</section>
```

### 11. 边界提示

```html
<section style="margin:22px 10px;padding:16px 18px;background:#F5F5F7;border-radius:10px;">
  <p style="margin:0 0 5px;font-size:12px;line-height:1.4;color:#0066CC;font-weight:750;letter-spacing:1px;"><span leaf="">BOUNDARY</span></p>
  <p style="margin:0;font-size:14px;line-height:1.8;color:#6E6E73;"><span leaf="">这是一种决策工具，不是爆款或商业合作保证。</span></p>
</section>
```

### 12. 四象限／四任务关系组

每格只放“坐标＋名称＋一句任务”，按阅读顺序使用四张全宽卡片。微信可能剥离父级 flex 却保留子项半宽，因此复制正文不使用 2×2、`width:50%` 或 `flex-basis:50%`。长解释放在关系组后逐段展开。

```html
<section style="margin:24px 10px;background:#FFFFFF;border:1px solid #D2D2D7;overflow:hidden;">
  <section style="padding:16px 14px;background:#FFFFFF;border-left:4px solid #0066CC;border-bottom:1px solid #D2D2D7;">
    <p style="margin:0 0 5px;font-size:11px;line-height:1.4;color:#6E6E73;"><span leaf="">短期 × 用户</span></p>
    <p style="margin:0 0 5px;font-size:16px;line-height:1.5;color:#1D1D1F;font-weight:800;"><span leaf="">热点引流</span></p>
    <p style="margin:0;font-size:13px;line-height:1.65;color:#6E6E73;"><span leaf="">解决当下问题，承接主页访问。</span></p>
  </section>
  <section style="padding:16px 14px;background:#F5F5F7;border-left:4px solid #1D1D1F;border-bottom:1px solid #D2D2D7;">
    <p style="margin:0 0 5px;font-size:11px;line-height:1.4;color:#6E6E73;"><span leaf="">短期 × 品牌</span></p>
    <p style="margin:0 0 5px;font-size:16px;line-height:1.5;color:#1D1D1F;font-weight:800;"><span leaf="">商业抢位</span></p>
    <p style="margin:0;font-size:13px;line-height:1.65;color:#6E6E73;"><span leaf="">节点判断，展示受众与表达。</span></p>
  </section>
  <section style="padding:16px 14px;background:#F5F5F7;border-left:4px solid #0066CC;border-bottom:1px solid #D2D2D7;">
    <p style="margin:0 0 5px;font-size:11px;line-height:1.4;color:#6E6E73;"><span leaf="">长期 × 用户</span></p>
    <p style="margin:0 0 5px;font-size:16px;line-height:1.5;color:#1D1D1F;font-weight:800;"><span leaf="">搜索沉淀</span></p>
    <p style="margin:0;font-size:13px;line-height:1.65;color:#6E6E73;"><span leaf="">回答稳定问题，形成旧文回流。</span></p>
  </section>
  <section style="padding:16px 14px;background:#FFFFFF;border-left:4px solid #1D1D1F;">
    <p style="margin:0 0 5px;font-size:11px;line-height:1.4;color:#6E6E73;"><span leaf="">长期 × 品牌</span></p>
    <p style="margin:0 0 5px;font-size:16px;line-height:1.5;color:#1D1D1F;font-weight:800;"><span leaf="">合作背书</span></p>
    <p style="margin:0;font-size:13px;line-height:1.65;color:#6E6E73;"><span leaf="">沉淀案例与行业判断力。</span></p>
  </section>
</section>
```

### 13. 五步行动线

```html
<section style="margin:18px 10px 28px;background:#FFFFFF;border-top:1px solid #D2D2D7;">
  <section style="padding:14px 0;border-bottom:1px solid #D2D2D7;">
    <p style="margin:0 0 3px;font-size:12px;line-height:1.4;color:#0066CC;font-weight:800;"><span leaf="">01　封面</span></p>
    <p style="margin:0;font-size:14px;line-height:1.75;color:#424245;"><span leaf="">一个结果＋一个具体对象。</span></p>
  </section>
  <section style="padding:14px 0;border-bottom:1px solid #D2D2D7;">
    <p style="margin:0 0 3px;font-size:12px;line-height:1.4;color:#0066CC;font-weight:800;"><span leaf="">02　开头</span></p>
    <p style="margin:0;font-size:14px;line-height:1.75;color:#424245;"><span leaf="">三句交代对象、问题与结论。</span></p>
  </section>
</section>
```

### 14. 编号行动清单

```html
<section style="margin:0 10px 24px;background:#FFFFFF;">
  <p style="margin:0 0 11px;font-size:14px;line-height:1.8;color:#424245;"><span style="display:inline-block;width:24px;height:24px;line-height:24px;text-align:center;border-radius:50%;background:#0066CC;color:#FFFFFF;font-size:12px;font-weight:800;margin-right:9px;"><span leaf="">1</span></span><span leaf="">笔记先解决一个问题，完成第一次价值交换。</span></p>
  <p style="margin:0;font-size:14px;line-height:1.8;color:#424245;"><span style="display:inline-block;width:24px;height:24px;line-height:24px;text-align:center;border-radius:50%;background:#0066CC;color:#FFFFFF;font-size:12px;font-weight:800;margin-right:9px;"><span leaf="">2</span></span><span leaf="">主页用一句话说明“我持续帮助谁解决什么”。</span></p>
</section>
```

### 15. 一句话公式

```html
<section style="margin:24px 10px;padding:20px;background:#1D1D1F;">
  <p style="margin:0 0 8px;font-size:11px;line-height:1.4;color:#A1A1A6;font-weight:700;letter-spacing:1px;"><span leaf="">ONE-SENTENCE BRIEF</span></p>
  <p style="margin:0;font-size:17px;line-height:1.75;color:#FFFFFF;font-weight:700;"><span leaf="">给【谁】解决【什么问题】，用【什么证据】，让他下一步【做一个站内动作】。</span></p>
</section>
```

### 16. 来源与二次归纳说明

```html
<section style="margin:34px 10px 0;padding:18px 0 0;background:#FFFFFF;border-top:1px solid #D2D2D7;">
  <p style="margin:0 0 6px;font-size:12px;line-height:1.5;color:#0066CC;font-weight:750;letter-spacing:1px;"><span leaf="">SOURCE NOTE</span></p>
  <p style="margin:0;font-size:13px;line-height:1.8;color:#6E6E73;"><span leaf="">本文原始思路来自公开分享。感谢原作者；本文在其基础上结合自己的理解与实践，再做结构化整理、归纳和总结。</span></p>
</section>
```

### 17. 参考资料

```html
<section style="margin:24px 10px 0;padding:18px 0 0;background:#FFFFFF;border-top:1px solid #D2D2D7;">
  <p style="margin:0 0 12px;font-size:15px;line-height:1.5;color:#1D1D1F;font-weight:800;"><span leaf="">参考资料</span></p>
  <p style="margin:0;font-size:12px;line-height:1.8;color:#6E6E73;word-break:break-all;"><span style="color:#0066CC;font-weight:700;"><span leaf="">[1]</span></span><span leaf=""> 原始分享：https://example.com/source</span></p>
</section>
```

### 18. END 与作者签名

```html
<section style="margin:42px 10px 24px;background:#FFFFFF;text-align:center;">
  <p style="margin:0 0 18px;font-size:11px;line-height:1;color:#A1A1A6;letter-spacing:3px;"><span leaf="">END</span></p>
  <section style="height:1px;line-height:1px;background:#D2D2D7;font-size:0;"><span leaf="">.</span></section>
</section>
<section style="margin:0 10px 24px;padding:20px 0;background:#FFFFFF;text-align:center;">
  <p style="margin:0 0 8px;font-size:14px;line-height:1.75;color:#1D1D1F;font-weight:700;"><span leaf="">我是 {{作者名}}，{{一句话简介}}</span></p>
  <p style="margin:0;font-size:13px;line-height:1.75;color:#6E6E73;"><span leaf="">如果你觉得今天这篇有收获，欢迎点赞、在看、转发，我们下篇见。</span></p>
</section>
```

---

## 三、完整文章骨架

```html
<section style="max-width:677px;margin:0 auto;background:#FFFFFF;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#424245;line-height:1.9;letter-spacing:0.2px;overflow-x:hidden;">
  <!-- 开场任务卡：先说读者要完成什么 -->
  <!-- 前言正文 -->
  <!-- 课程导读：只选 3 个学习结果 -->
  <!-- STEP／LESSON 01–N：核心行动标题 + 正文 + 主题组件 -->
  <!-- 整理法则：若非主题本身，放对应步骤小注或文末辅助说明 -->
  <!-- 结语 -->
  <!-- 来源与二次归纳说明 -->
  <!-- 参考资料 -->
  <!-- END + 作者签名 -->
</section>
```

骨架顺序固定：读者任务 → 学习结果 → 行动步骤 → 行动总结 → 辅助方法说明 → 来源致谢 → 参考资料 → 作者签名。来源说明必须放在正文完成之后，避免打断开场，但不得省略原始思路署名与二次归纳边界。

---

## 四、文章类型 → 组件组合配方

| 文章类型 | 核心组件 | 点缀组件 |
|---|---|---|
| 方法论／公开课 | 开场任务卡 2 + 课程导读 4 + 章节标题 6 + 正文 7 | 四象限 12、五步行动线 13、一句话公式 15 |
| 教程／操作指南 | 课程导读 4 + 章节标题 6 + 五步课程线 13 | 编号清单 14、边界提示 11 |
| 观点／深度分析 | 开场课程卡 2 + 章节标题 6 + 核心结论 10 | 小标题 8、来源说明 16 |
| 案例复盘 | 课程导读 4 + 章节标题 6 + 五步课程线 13 | 一句话公式 15、边界提示 11 |
| 数据复盘／报告 | 章节标题 6 + 正文 7 + 通用库表格 | 核心结论 10、来源说明 16 |

全类型固定使用组件 16 的来源／二次归纳说明（存在外部思路时）、组件 17 的参考资料（存在链接时）和组件 18 的 END／签名。

---

## 五、Markdown → 组件映射规则

| Markdown 元素 | 组件 | 说明 |
|---|---|---|
| 开头 `>` | 2 开场任务卡 | 改成读者任务＋结果承诺，不堆方法名 |
| 前言段落 | 3 前言正文 | 保持短段落 |
| 3 个核心看点 | 4 课程导读 | 不是全量目录 |
| `##` | 6 步骤／课程章节标题 | 自动 `STEP` 或 `LESSON 01/02…`；主标题写行动任务 |
| `###` | 8 左竖条小标题 | 用于象限或子问题 |
| 普通段落 | 7 正文段落 | 每段 1–3 个关键词标记 |
| `**加粗**` | 深墨色加粗 | 不要每句都加粗 |
| `++关键词++` | 9 蓝色下划线 | 主题默认关键词样式 |
| 核心金句 | 10 核心结论 | 全文少量 |
| 提示／边界 | 11 边界提示 | 不用警告式大色块 |
| 四象限 | 12 四任务关系组 | 全宽纵向卡片，每格只放短信息，详情后置 |
| 操作步骤 | 13 五步课程线／14 编号清单 | 据步骤长短选择 |
| 一句话公式 | 15 一句话公式 | 全文最多 1–2 次 |
| 来源致谢 | 16 来源说明 | 正文完成后、参考资料前 |
| `[text](url)` | 通用库脚注 + 17 参考资料 | 正文不留 `<a>` |
| 代码、图片、GIF | `common-components.md` | 套用主色 `#0066CC` |
| 文末 | 18 END 与签名 | 仅一处，未知作者保留占位 |

### 公众号复制约束

- 只输出 `<section>` 片段，不含 `<html>`、`<head>`、`<body>`、`<style>` 或 `<script>`。
- 只用内联样式；不用 `class`、`id`、`div`、`position`、`grid`、`width:50%`、`flex-basis:50%`、CSS 变量或媒体查询。
- 所有正文文字用 `<span leaf="">` 包裹；代码按通用库逐行 `<p style="margin:0">`。
- 生成后必须运行 `validate_gzh_html.py`，手动粘贴前再运行 `wrap_preview.py` 生成浏览器预览。
