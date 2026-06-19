# 🎯 AI 简历专家 (Resume Expert)

> 符合 ATS 兼容标准的 AI 简历生成与优化工具 —— 一次输入，直接生成可投递的专业简历

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-WorkBuddy%20%7C%20Claude%20Code%20%7C%20Cursor-brightgreen.svg)]()

---

## ✨ 为什么选择这个 Skill？

传统的简历优化要么花钱找人改（贵且慢），要么自己反复打磨措辞（耗时耗力），要么用通用 AI 工具反复"调教"才能得到满意的结果。

**Resume Expert 的逻辑是：你负责提供素材，它负责转化成专业简历。**

- 🎯 **JD 驱动优化** — 自动解析岗位描述，反向定制简历内容
- 🧠 **11+ 岗位深度定制** — 后端、前端、算法、产品、运营各有各的写法
- 🔍 **ATS 友好** — 关键词自动对齐，通过企业招聘系统自动筛选
- 📄 **双格式输出** — 同时生成 HTML 和 DOCX（Word 可编辑）
- 💡 **面试准备** — 自动生成高频考点、亮点故事线、弱点预判
- 🛡️ **基于真实经历** — 不编造数据，信息不足时主动追问

---

## 🚀 快速开始

### 安装到 WorkBuddy

1. 下载 `resume-expert.zip`
2. 在 WorkBuddy 中导入 Skill
3. 直接说：`帮我根据这个 JD 优化我的简历`

### 安装到 Claude Code

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/yourusername/resume-expert.git ~/.claude/skills/resume-expert
```

### 安装到 Cursor / 其他 Agent

将 `SKILL.md` 的内容作为 System Prompt 或 Skill 注入即可。

---

## 📋 支持的六种模式

| 模式 | 触发条件 | 功能 |
|------|---------|------|
| **A — JD驱动优化** | 有简历 + 有JD | 解析JD → 诊断简历 → 逐条重写匹配 |
| **B — 简历审计** | 有简历 + 无JD | 30秒结论 + 分维度评分 + 逐项修改 |
| **C — JD反向生成** | 无简历 + 有JD | 收集信息 → 反向定制生成 |
| **D — 从零生成** | 无简历 + 无JD | 对话式信息收集 → 生成 |
| **E — 面试准备** | 只要面试建议 | 高频考点 + 故事线 + 弱点预判 |
| **F — 格式输出** | 只要格式转换 | HTML / DOCX / ATS纯文本 |

---

## 🎨 支持的岗位类型

不套固定模板，按岗位类型动态决定技能维度和表达重点：

| 岗位 | 技能维度示例 |
|------|-------------|
| 后端工程师 | 编程语言、框架、数据库、分布式、DevOps |
| 前端工程师 | JS/TS、框架、构建工具、CSS方案、工程化 |
| 算法工程师 | PyTorch、模型架构、NLP/CV、部署优化 |
| 产品经理 | 需求分析、数据分析、项目管理、行业认知 |
| AI 产品经理 | LLM、RAG、Prompt Engineering、Agent |
| 数据分析师 | SQL、Python、可视化、统计学、指标体系 |
| 运营 | 增长方法论、内容策划、数据分析、工具栈 |
| 设计师 | UI/UX、Figma、设计系统、用户研究 |
| 测试/QA | 自动化测试、CI/CD、性能测试 |
| 市场/品牌 | 品牌策略、内容营销、投放渠道、数据归因 |
| 财务/金融 | 财务分析、建模估值、CPA/CFA |

---

## 📁 项目结构

```
resume-expert/
├── SKILL.md                          # Skill 核心文件（提示词与工作流）
├── references/
│   └── job_types.md                  # 11+ 岗位类型技能维度参考
├── scripts/
│   └── generate_docx.py              # DOCX 简历生成脚本
└── assets/
    └── resume_template.html          # HTML 简历模板
```

---

## 📊 ATS 兼容性

- ✅ 标准模块标题（工作经历、教育背景、技能、项目经验）
- ✅ 无表格、无图片、无特殊符号
- ✅ 关键词自然嵌入，非堆砌
- ✅ 时间倒序排列
- ✅ PDF / DOCX 双格式输出

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 📄 License

MIT License — 自由使用、修改和分发。
