# 🎯 AI 简历专家 (Resume Expert)

> 2026 AI 时代程序员简历优化工具 — JD 驱动、ATS 兼容、HTML/DOCX 双格式输出

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-WorkBuddy%20%7C%20Claude%20Code%20%7C%20Cursor-brightgreen.svg)]()

---

## ✨ 为什么选择这个 Skill？

2026 年，AI 已经不是加分项，而是筛选条件。只会写 CRUD 的简历，大概率第一轮就刷掉了。

- 🎯 **JD 驱动优化** — 自动解析岗位描述，反向定制简历内容
- 🤖 **AI 时代检查** — 自动检测简历是否包含作品集、GitHub、AI 开发框架、AI 编程工具、监控运维等现代要素
- 🧠 **11+ 岗位深度定制** — 后端、前端、算法、产品、运营各有各的写法
- 🔍 **ATS 友好** — 关键词自动对齐，通过企业招聘系统自动筛选
- 📄 **双格式输出** — 同时生成 HTML 和 DOCX（Word 可编辑），含作品集/GitHub/项目链接
- 💡 **面试准备** — 自动生成高频考点、亮点故事线、弱点预判 + AI 时代加分题
- 🛡️ **基于真实经历** — 不编造数据，信息不足时主动追问

---

## 🆕 v2.0 更新内容（2026.06）

### AI 时代黄金法则
1. **求职意向带 AI 标签** — `Java 后端开发（具备 AI Agent 全栈开发经验）`
2. **作品集 + GitHub 必放头部** — 10 份简历 8 份没有，有就是区分度
3. **AI 技能 4 层结构** — AI 开发框架 → AI 应用实战 → AI 编程工具 → AI 编程模式
4. **项目必须上线** — 可访问地址是验证真实性的唯一方式
5. **每一条带量化数据** — QPS / DAU / 提升 X% / 成本降低 X%
6. **监控告警 + SEO/GEO** — "写完代码之后"的能力也是能力
7. **体现自主性** — 不只是参与，是主导、决策、交付

### 结构更新
- 所有岗位类型新增 AI 时代技能维度（Spring AI、LangChain4j、RAG、MCP、Agent 等）
- HTML 模板新增作品集链接、GitHub、项目 URL、其他作品展示区
- DOCX 脚本支持 AI 技能绿色高亮标签、产品信息、项目链接
- 面试准备模式新增 AI 时代加分题预判

---

## 🚀 快速开始

### 安装到 WorkBuddy

1. 下载本仓库
2. 放到 `~/.workbuddy/skills/resume-expert/`
3. 在对话中直接使用关键字触发，例如：
   - `帮我根据这个 JD 优化我的简历`
   - `审计一下我的简历，看看 AI 时代还缺什么`
   - `我要应聘后端工程师，帮我写一份 AI 时代的简历`

### 安装到 Claude Code

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/one6666666/resume-expert-skill.git ~/.claude/skills/resume-expert
```

### 安装到 Cursor / 其他 Agent

将 `SKILL.md` 的内容作为 System Prompt 或 Skill 注入即可。

---

## 📋 支持的六种模式

| 模式 | 触发条件 | 功能 |
|------|---------|------|
| **A — JD驱动优化** | 有简历 + 有JD | 解析JD（含AI相关检测）→ 诊断简历（含AI时代专项检查）→ 逐条重写 |
| **B — 简历审计** | 有简历 + 无JD | 30秒结论 + 分维度评分 + AI时代适配度评分 + 逐项修改 |
| **C — JD反向生成** | 无简历 + 有JD | 收集信息（含AI经验）→ 反向定制生成 |
| **D — 从零生成** | 无简历 + 无JD | 对话式信息收集 → 含AI时代检查生成 |
| **E — 面试准备** | 只要面试建议 | 高频考点 + 故事线 + 弱点预判 + AI时代加分题 |
| **F — 格式输出** | 只要格式转换 | HTML（含作品集/项目链接） / DOCX / ATS纯文本 |

---

## 🎨 支持的岗位类型

不套固定模板，按岗位类型动态决定技能维度和表达重点：

| 岗位 | 传统技能 | AI 时代新增 |
|------|---------|-----------|
| 后端工程师 ⚡ | Java/Go、Spring Boot、MySQL、Redis | Spring AI、LangChain4j、RAG/MCP、Agent Skills、Prometheus/Grafana、SEO/GEO |
| 前端工程师 ⚡ | React/Vue、TypeScript、Webpack/Vite | Cursor/v0、AI组件开发、Vibe Coding、Vercel作品集部署 |
| 算法/ML | PyTorch、Transformer、模型部署 | LLM应用、RAG/Agent、AI编程工具 |
| 产品经理 | 需求分析、数据分析、项目管理 | AI产品理解、Prompt Engineering基础、AI编程原型 |
| AI 产品经理 | LLM、RAG、Prompt Engineering | AI编程验证、模型评估、安全对齐 |
| 数据分析 | SQL、Python、可视化 | AI分析工具、AI编程辅助 |
| 运营 | 增长方法论、内容策划 | AI内容工具、GEO生成式引擎优化 |
| 设计师 | UI/UX、Figma | Midjourney/DALL-E、v0/Bolt、设计转代码 |
| 测试/QA | 自动化测试、CI/CD | AI测试生成、AI编程辅助 |
| 市场/品牌 | 品牌策略、内容营销 | AI营销工具、GEO |
| 财务/金融 | 财务分析、建模 | AI分析工具、AI编程辅助 |

---

## 📁 项目结构

```
resume-expert/
├── SKILL.md                          # Skill 核心文件（提示词与工作流）
├── README.md                         # 项目说明
├── LICENSE                           # MIT 协议
├── .gitignore
├── references/
│   └── job_types.md                  # 11+ 岗位类型技能维度（AI时代版）
├── scripts/
│   └── generate_docx.py              # DOCX 简历生成（含AI标签/作品集/项目链接）
└── assets/
    └── resume_template.html          # HTML 简历模板（含作品集/GitHub/项目URL）
```

---

## 📊 ATS 兼容性

- ✅ 标准模块标题（工作经历、教育背景、技能、项目经验）
- ✅ 无表格、无图片、无特殊符号
- ✅ 关键词自然嵌入（含 AI 时代关键词：Spring AI、RAG、MCP、Agent 等）
- ✅ 时间倒序排列
- ✅ PDF / DOCX 双格式输出
- ✅ 作品集 URL 在 ATS 可解析位置

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 📄 License

MIT License — 自由使用、修改和分发。
