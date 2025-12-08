# DeepWiki-Open

> **🏆 开源创新大赛参赛作品**  
> **赛题一：基于 Git 原理的实用性插件与应用开发 - Git 创新应用方向**.  
> **访问地址：[https://gitcode.huqi.host/](https://gitcode.huqi.host/)**

## 项目名称

**DeepWiki-Open** - 基于 Git 原理的智能文档自动生成工具，为 **GitCode**、GitHub、GitLab 等任何 Git 代码仓库自动创建美观、交互式的 Wiki 文档  
演示视频：[https://www.bilibili.com/video/BV1XrSWBjEvr/](https://www.bilibili.com/video/BV1XrSWBjEvr/)

<video  width="640" height="360" controls>
   <source src="https://huqi-blog.obs.cn-north-4.myhuaweicloud.com:443/videos/deepwiki-gitcode.mp4" type="video/mp4">
   <source src="screenshots/deepwiki-gitcode.mp4" type="video/mp4">
   <source src="https://www.bilibili.com/video/BV1XrSWBjEvr/?share_source=copy_web&vd_source=28618d8b8e38d1775b1dc2ec9260545b">
</video>

## 📋 赛题背景与项目定位

### 赛题方向：Git 创新应用（1.2.2）

DeepWiki-Open 是一个**基于 Git 原理的创新应用**，专注于解决开源协作中的核心痛点：

- **痛点 1：文档缺失**：许多优秀的开源项目因缺少完善文档而难以推广
- **痛点 2：理解困难**：新贡献者难以快速理解代码库结构和设计思路
- **痛点 3：协作效率低**：团队成员需要花费大量时间阅读和理解代码

### 基于 Git 原理的创新实现

DeepWiki-Open 深度利用 Git 的核心特性：

1. **Git 仓库克隆与分析**：基于 Git 协议克隆仓库，支持公开和私有仓库访问
2. **Git 历史追踪**：分析提交历史，理解代码演进和关键模块
3. **分支结构可视化**：自动识别项目结构，生成架构图和依赖关系
4. **多平台兼容**：原生支持 **GitCode**、GitHub、GitLab、Bitbucket 等所有基于 Git 的代码托管平台

### 实用价值

- ⚡ **降低开源参与门槛**：自动生成的 Wiki 让新手快速了解项目
- 🤖 **AI 驱动理解**：通过 RAG 技术实现智能问答，解答代码相关问题
- 📊 **可视化展示**：Mermaid 图表直观展示代码结构和数据流
- 🔍 **深度研究能力**：多轮研究机制彻底分析复杂技术问题

## ✨ 核心特点

### 🎯 GitCode 优先支持

- **GitCode 原生集成**：完美支持 GitCode 平台的公开和私有仓库
- **访问令牌认证**：安全访问 GitCode 私有仓库
- **中文社区优化**：针对中文开源社区优化的文档生成和问答体验

### 🚀 强大功能

- **即时文档生成**：几秒钟内将任何 Git 仓库转换为专业 Wiki 文档
- **私有仓库支持**：使用个人访问令牌安全访问私有仓库
- **AI 智能分析**：基于大语言模型的代码结构和关系理解
- **自动图表生成**：创建 Mermaid 图表可视化架构和数据流
- **智能导航**：简单、直观的界面快速探索文档
- **RAG 问答系统**：基于检索增强生成技术，精准回答代码相关问题
- **深度研究模式**：多轮迭代研究，彻底调查复杂主题
- **多模型支持**：支持 Google Gemini、OpenAI、OpenRouter 和本地 Ollama 模型

## 运行条件

### API 密钥要求

- Google API 密钥（从 [Google AI Studio](https://makersuite.google.com/app/apikey) 获取）
- OpenAI API 密钥（从 [OpenAI Platform](https://platform.openai.com/api-keys) 获取）
- OpenRouter API 密钥（可选，用于使用 OpenRouter 模型）
- **GitCode 访问令牌**（推荐配置，用于访问 GitCode 私有仓库）

### 软件依赖

- Python 3.8+ 和 pip
- Node.js 16+ 和 npm/yarn
- Docker 和 Docker Compose（如果使用 Docker 方式）
- Git

### 系统要求

- 至少 4GB RAM
- 足够的磁盘空间用于存储克隆的仓库和生成的嵌入文件

## 运行说明

### 🚀 快速开始（推荐使用 Docker）

```bash
# 1. 克隆仓库
git clone https://gitcode.com/huqi/deepwiki-open.git
cd deepwiki-open

# 2. 创建包含 API 密钥的 .env 文件
echo "CUSTOM_OPENAI_API_KEY=your_custom_api_key" > .env
echo "CUSTOM_OPENAI_BASE_URL=your_base_url" >> .env
echo "CUSTOM_OPENAI_MODEL_NAME=your_model_name" >> .env
echo "CUSTOM_OPENAI_EMBEDDING_MODEL=your_embedding_model" >> .env
echo "DEEPWIKI_EMBEDDER_TYPE=custom_openai" >> .env
# 可选：在前端默认填充 GitCode 访问令牌（仅适合可信环境）
# echo "NEXT_PUBLIC_GITCODE_ACCESSTOKEN=your_gitcode_pat" >> .env



# 3. 使用 Docker Compose 运行
docker-compose up
```

> ⚠️ `NEXT_PUBLIC_GITCODE_ACCESSTOKEN` 会被打包到前端代码中，仅在内网演示或受控环境下使用。
> 💡 **数据持久化说明：** Docker 配置会挂载 `~/.adalflow` 目录以持久化：
>
> - 克隆的仓库（`~/.adalflow/repos/`）
> - 嵌入和索引（`~/.adalflow/databases/`）
> - 缓存的 Wiki 内容（`~/.adalflow/wikicache/`）

### 📦 方式二：手动设置（推荐开发）

#### 步骤 1：设置 API 密钥

在项目根目录创建 `.env` 文件：

```bash
# 必需的 API 密钥（至少配置一个）
# GOOGLE_API_KEY=your_google_api_key
# OPENAI_API_KEY=your_openai_api_key
CUSTOM_OPENAI_API_KEY=your_custom_api_key
CUSTOM_OPENAI_BASE_URL=your_base_url
CUSTOM_OPENAI_MODEL_NAME=your_model_name
CUSTOM_OPENAI_EMBEDDING_MODEL=your_embedding_model
DEEPWIKI_EMBEDDER_TYPE=custom_openai



# 可选配置
OPENROUTER_API_KEY=your_openrouter_api_key
OPENAI_BASE_URL=https://custom-api-endpoint.com/v1  # 可选，用于自定义 OpenAI API 端点
```

#### 步骤 2：启动后端

```bash
# 安装 Python 依赖
python -m pip install poetry==2.0.1 && poetry install

# 激活虚拟环境并启动 API 服务器
source .venv/bin/activate && .venv/bin/python -m api.main
```

> 💡 后端 API 服务器将在 `http://localhost:8001` 启动

#### 步骤 3：启动前端

```bash
# 安装 JavaScript 依赖
npm install
# 或使用 yarn
yarn install

# 启动 Web 应用
npm run dev
# 或使用 yarn
yarn dev
```

> 💡 前端应用将在 `http://localhost:3000` 启动

#### 步骤 4：使用 DeepWiki

1. 在浏览器中打开 [http://localhost:3000](http://localhost:3000)
2. 输入 Git 仓库 URL，**推荐先尝试 GitCode 仓库**：
   - GitCode 公开仓库示例：`https://gitcode.com/huqi/deepwiki-open`
   - GitHub 仓库示例：`https://github.com/openai/whisper`
   - GitLab 仓库示例：`https://gitlab.com/gitlab-org/gitlab`
3. 对于私有仓库，点击 **"+ 添加访问令牌"** 并输入您的个人访问令牌
4. 选择 AI 模型提供商和具体模型
5. 点击 **"生成 Wiki"**，见证 AI 自动生成文档！

### 🎯 GitCode 仓库使用示例

#### 示例 1：为 GitCode 公开仓库生成文档

```
仓库 URL：https://gitcode.com/huqi/deepwiki-open
访问令牌：（公开仓库不需要）
```

#### 示例 2：为 GitCode 私有仓库生成文档

```
仓库 URL：https://gitcode.com/your-username/your-private-repo
访问令牌：在 GitCode 个人设置中创建的访问令牌
```

> 💡 **如何获取 GitCode 访问令牌：**
>
> 1. 登录 GitCode
> 2. 进入 **个人设置** → **访问令牌**
> 3. 创建新令牌，选择 `read_repository` 权限
> 4. 复制生成的令牌（仅显示一次）

### 环境变量说明

```bash
# ====== API 密钥（必需至少一个）======
GOOGLE_API_KEY=your_google_api_key        # Google Gemini 模型必需
OPENAI_API_KEY=your_openai_api_key        # OpenAI 模型必需或用于 embeddings
OPENROUTER_API_KEY=your_openrouter_api_key # OpenRouter 模型必需
CUSTOM_OPENAI_API_KEY=your_custom_api_key # 自定义 custom_openai 密钥

# Embedding 服务 (可以不同的 baseurl)
EMBEDDING_API_KEY=YOUR_EMBEDDING_API_KEY
EMBEDDING_BASE_URL=https://api.modelarts-maas.com/v1
EMBEDDING_MODEL_NAME=bge-m3

# ====== OpenAI API 基础 URL 配置（可选）======
OPENAI_BASE_URL=https://custom-api-endpoint.com/v1

# ====== 配置目录（可选）======
DEEPWIKI_CONFIG_DIR=/path/to/custom/config/dir

# ====== 授权模式（可选）======
DEEPWIKI_AUTH_MODE=true              # 启用授权模式
DEEPWIKI_AUTH_CODE=your_secret_code  # 授权码

# ====== 运行/部署配置（可选）======
SERVER_BASE_URL=http://localhost:8001         # 前端请求后端 API 的地址
PYTHON_BACKEND_HOST=http://localhost:8001     # Next.js API 路由访问的 Python 服务地址
NEXT_PUBLIC_GITCODE_ACCESSTOKEN=your_gitcode_pat # 可选：前端默认填充的 GitCode 访问令牌（仅适用于可信环境）
```

## 测试说明

### 基本功能测试

1. **公开仓库测试**：输入一个公开的 GitHub/GitLab/GitCode 仓库 URL，验证 Wiki 生成功能
2. **私有仓库测试**：使用访问令牌测试私有仓库的 Wiki 生成
3. **提问功能测试**：在生成的 Wiki 中使用提问功能，验证 RAG 问答
4. **深度研究测试**：启用深度研究模式，测试多轮研究功能

### 故障排除

#### API 密钥问题

- **"缺少环境变量"**：确保 `.env` 文件位于项目根目录并包含所需的 API 密钥
- **"API 密钥无效"**：检查您是否正确复制了完整密钥，没有多余空格

#### 连接问题

- **"无法连接到 API 服务器"**：确保 API 服务器在端口 8001 上运行
- **"CORS 错误"**：尝试在同一台机器上运行前端和后端

#### 生成问题

- **"生成 Wiki 时出错"**：对于非常大的仓库，请先尝试较小的仓库
- **"无效的仓库格式"**：确保您使用有效的仓库 URL 格式
- **"无法获取仓库结构"**：验证访问令牌的有效性和权限

#### 常见解决方案

1. 重启前端和后端服务器
2. 检查浏览器控制台日志查看 JavaScript 错误
3. 查看 API 终端的 Python 错误日志

## 技术架构

### 🔧 基于 Git 原理的核心设计

DeepWiki-Open 深度整合 Git 核心机制，实现智能文档自动化：

#### 1. Git 协议集成

- **Git Clone 机制**：使用标准 Git 协议克隆仓库，支持 HTTP(S)、SSH 等多种传输协议
- **认证系统**：支持 Personal Access Token (PAT) 认证，安全访问私有仓库
- **多平台适配**：统一接口支持 GitCode、GitHub、GitLab、Bitbucket 等所有 Git 托管平台

#### 2. Git 对象模型分析

- **Blob 对象解析**：读取文件内容，识别代码语言和结构
- **Tree 对象遍历**：分析目录树结构，构建项目文件层次
- **Commit 历史追踪**：分析提交记录，理解代码演进过程
- **Reference 识别**：识别分支、标签等引用，了解项目版本布局

#### 3. 代码语义理解

- **AST 抽取**：解析源代码的抽象语法树，理解代码结构
- **依赖关系图**：基于 import/include 等语句构建模块依赖关系
- **向量嵌入**：将代码片段转换为向量表示，支持语义检索

#### 4. AI 驱动文档生成

- **RAG 技术**：检索增强生成，基于实际代码生成准确文档
- **多模型支持**：集成 Google Gemini、OpenAI、OpenRouter 等主流 LLM
- **上下文窗口管理**：智能切分和组织代码上下文，优化 AI 理解

### 📊 系统工作流程

![DeepWiki 工作流程](screenshots/deepwiki-workflow.png)

### 💻 系统架构组成

```
deepwiki-open/
├── api/                  # 后端 API 服务器
│   ├── main.py           # API 入口点
│   ├── api.py            # FastAPI 实现
│   ├── rag.py            # 检索增强生成
│   ├── data_pipeline.py  # 数据处理工具
│   └── config/           # 配置文件目录
│       ├── generator.json    # 文本生成模型配置
│       ├── embedder.json     # 嵌入模型配置
│       └── repo.json         # 仓库处理配置
│
├── src/                  # 前端 Next.js 应用
│   ├── app/              # Next.js 应用目录
│   │   └── page.tsx      # 主应用页面
│   └── components/       # React 组件
│       └── Mermaid.tsx   # Mermaid 图表渲染器
│
├── public/               # 静态资源
├── package.json          # JavaScript 依赖
└── .env                  # 环境变量（需要创建）
```

### 技术栈

- **前端**：Next.js、React、TypeScript
- **后端**：Python、FastAPI
- **AI 模型**：Google Gemini、OpenAI、OpenRouter、Ollama
- **向量存储**：用于 RAG 的嵌入式向量数据库
- **可视化**：Mermaid.js 图表

### 核心功能

#### 提问功能（RAG 驱动）

- 上下文感知响应：基于仓库实际代码获取准确答案
- RAG 驱动：检索相关代码片段提供有根据的响应
- 实时流式传输：实时查看生成的响应
- 对话历史：保持上下文实现连贯交互

#### 深度研究功能

- 深入调查：通过多次迭代彻底探索复杂主题
- 结构化过程：遵循清晰的研究计划
- 自动继续：AI 自动继续研究直到达成结论（最多 5 次迭代）
- 研究阶段：研究计划 → 研究更新 → 最终结论

### 多模型支持

#### 支持的提供商和模型

- **Google**：`gemini-2.5-flash`（默认）、`gemini-2.5-flash-lite`、`gemini-2.5-pro` 等
- **OpenAI**：`gpt-5-nano`（默认）、`gpt-5`、`4o` 等
- **OpenRouter**：通过统一 API 访问 Claude、Llama、Mistral 等多种模型
- **Ollama**：支持本地运行的开源模型，如 `llama3`

#### 配置文件

1. **`generator.json`**：文本生成模型配置

   - 定义可用的模型提供商
   - 指定每个提供商的默认和可用模型
   - 包含特定模型的参数（temperature、top_p）

2. **`embedder.json`**：嵌入模型和文本处理配置

   - 定义用于向量存储的嵌入模型
   - 包含用于 RAG 的检索器配置
   - 指定文档分块的文本分割器设置

3. **`repo.json`**：仓库处理配置
   - 文件过滤器配置
   - 仓库大小限制和处理规则

### 授权模式

DeepWiki 支持授权模式，用于控制谁可以使用生成功能：

- 启用后，前端将显示授权码输入字段
- 限制使用前端页面生成 Wiki 并保护已生成页面的缓存删除
- 主要目的是保护管理员已生成的 Wiki 页面

### 🤖 自定义 LLM 支持

DeepWiki-Open 提供了灵活的自定义 LLM 配置能力，支持任何兼容 OpenAI API 格式的大语言模型服务。

#### 方式一：使用自定义 OpenAI 兼容端点

通过配置 `OPENAI_BASE_URL` 环境变量，您可以使用任何兼容 OpenAI API 的服务：

```bash
# .env 文件配置
OPENAI_API_KEY=your_custom_api_key
OPENAI_BASE_URL=https://your-custom-endpoint.com/v1

# 示例：使用阿里云百炼平台
OPENAI_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1

# 示例：使用智谱 AI
OPENAI_BASE_URL=https://open.bigmodel.cn/api/paas/v4

# 示例：使用硅基流动
OPENAI_BASE_URL=https://api.siliconflow.cn/v1
```

配置后，在前端选择 "OpenAI" 提供商，即可使用自定义端点的模型。

#### 方式二：直接在界面中输入自定义模型

DeepWiki 支持在前端界面直接输入自定义模型标识符：

1. 在模型选择对话框中，启用 **"自定义模型"** 选项
2. 输入您的自定义模型名称（如 `qwen-plus`、`glm-4`）
3. 确保对应的 API 密钥和 BASE_URL 已正确配置

#### 支持的自定义 LLM 服务商

✅ **国内主流 AI 平台**

- 阿里云百炼（通义千问系列）
- 智谱 AI（GLM 系列）
- 百度千帆（文心一言）
- 字节跳动豆包
- Moonshot AI（Kimi）
- 深度求索（DeepSeek）
- 零一万物（Yi 系列）

✅ **开源模型托管平台**

- 硅基流动（SiliconFlow）
- Together AI
- Replicate
- Hugging Face Inference API

✅ **私有部署**

- vLLM 部署的模型
- FastChat 部署的模型
- Text Generation Inference (TGI)
- 本地 Ollama（无需配置 BASE_URL）

#### 自定义 Embedding 模型

如果需要使用自定义的 embedding 模型（如阿里巴巴 Qwen Embedding）：

1. 用 `api/config/embedder_openai_compatible.json` 替换 `api/config/embedder.json`
2. 在 `.env` 文件中配置：
   ```bash
   OPENAI_API_KEY=your_embedding_api_key
   OPENAI_BASE_URL=https://your-embedding-endpoint.com/v1
   ```
3. 程序会自动使用配置的端点进行向量化

#### 配置文件自定义

高级用户可以直接修改配置文件来添加新的模型提供商：

**编辑 `api/config/generator.json`**：

```json
{
  "providers": {
    "custom_provider": {
      "default_model": "your-model-name",
      "available_models": ["your-model-name", "another-model"],
      "model_kwargs": {
        "temperature": 0.7,
        "top_p": 0.9
      }
    }
  }
}
```

### 授权模式

DeepWiki 支持授权模式，用于控制谁可以使用生成功能：

- 启用后，前端将显示授权码输入字段
- 限制使用前端页面生成 Wiki 并保护已生成页面的缓存删除
- 主要目的是保护管理员已生成的 Wiki 页面

配置方式：

```bash
DEEPWIKI_AUTH_MODE=true              # 启用授权模式
DEEPWIKI_AUTH_CODE=your_secret_code  # 设置授权码
```

## 🏆 参赛作品亮点总结

### 符合赛题要求（Git 创新应用 1.2.2）

**✅ 基于 Git 原理**

- 深度整合 Git 克隆、对象模型、历史追踪等核心机制
- 支持 HTTP(S)、SSH 等标准 Git 传输协议
- 原生支持 GitCode、GitHub、GitLab 等所有 Git 平台

**✅ 实用价值**

- 解决开源项目文档缺失的痛点问题
- 降低开源参与门槛，帮助新手快速理解代码
- AI 驱动的智能问答系统提升协作效率

**✅ 创新性**

- 首创基于 Git 仓库的 AI 自动文档生成
- RAG 技术实现精准的代码问答
- 多轮深度研究机制彻底分析复杂问题

### 技术创新点

#### 1️⃣ Git 深度集成

- **Git 对象模型分析**：解析 Blob、Tree、Commit 对象，理解代码结构
- **智能仓库克隆**：支持公开/私有仓库，多平台统一认证
- **提交历史分析**：追踪代码演进，识别关键模块

#### 2️⃣ AI 智能增强

- **RAG 技术**：检索增强生成，基于实际代码生成文档
- **多模型支持**：Google Gemini、OpenAI、OpenRouter、Ollama
- **自定义 LLM**：支持任何 OpenAI 兼容的 API 端点

#### 3️⃣ GitCode 优先适配

- 默认选择 GitCode 平台
- 专门优化 GitCode 私有仓库访问
- 专门优化 GitCode 私有仓库访问

#### 4️⃣ 可视化增强

- 自动生成 Mermaid 架构图和数据流图
- 交互式 Wiki 界面，易于导航
- 代码结构、依赖关系可视化

### 实际应用场景

🔹 **开源项目维护者**

- 自动生成项目文档，降低维护成本
- 吸引更多贡献者参与

🔹 **开发者学习**

- 快速理解新项目的架构和设计
- 通过问答系统深入学习代码细节

🔹 **企业团队**

- 私有仓库文档自动化
- 团队知识库建设
- 代码 review 辅助工具

🔹 **教育培训**

- 代码教学辅助工具
- 开源项目案例分析
- Git 原理实践演示

### 竞争优势

| 特性         | DeepWiki-Open | 传统文档工具  |
| ------------ | ------------- | ------------- |
| 自动化程度   | ✅ 全自动生成 | ❌ 手动编写   |
| Git 集成     | ✅ 深度集成   | ⚠️ 基础支持   |
| AI 问答      | ✅ RAG 驱动   | ❌ 无         |
| 可视化       | ✅ 自动图表   | ⚠️ 需手动绘制 |
| 私有仓库     | ✅ 完全支持   | ⚠️ 部分支持   |
| 多模型支持   | ✅ 4+ 提供商  | ❌ 单一或无   |
| GitCode 优化 | ✅ 优先支持   | ❌ 无         |

## 协作者

欢迎贡献！可以通过以下方式参与：

- 为 bug 或功能请求开 issue
- 提交 pull request 改进代码
- 分享您的反馈和想法

---

### 许可证

本项目根据 MIT 许可证授权 - 详情请参阅 [LICENSE](LICENSE) 文件。

### 截图

![DeepWiki主界面](screenshots/Interface.png)
_DeepWiki 的主界面_

![私有仓库支持](screenshots/privaterepo.png)
_使用个人访问令牌访问私有仓库_

![深度研究功能](screenshots/DeepResearch.png)
_深度研究为复杂主题进行多轮调查_
