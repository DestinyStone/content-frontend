# 前端代码风格指南
本文档概述了基于 Vue.js 官方风格指南和既定 JavaScript 规范的编码标准。

## 1. 通用标准
### 1.1. 应用范围
* 适用于所有前端开发（JavaScript、HTML 和 Vue 组件）

### 1.2.命名规范
* 避免使用描述性不足的名称（例如：a_2、temp_var）
* 实现正确的命名格式（例如：loginState、isFilling）

## 2. 命名规则
* 组件文件：使用驼峰命名法（例如：contact.vue、userProfile.vue）
* 组件标签：使用短横线命名法（例如：<el-button>、<user-profile>）
* 函数名：使用驼峰命名法（例如：loadContacts、validateForm）
* 变量名：使用驼峰命名法（例如：loading、formRef）
* 常量值：使用大写字母加下划线（例如：API_BASE_URL、MAX_RETRY_COUNT）
* 组件属性：使用短横线命名法（例如：:user-data="userInfo", @click="submitForm")

## 3.代码格式化
### 3.1. 基本格式
* 缩进：使用 2 个空格缩进（避免使用制表符）
* 语句终止：语句结尾处添加分号

### 3.2. 导入组织
* 保持单独的导入行，并按以下顺序分组：
* 框架导入（例如：vue、vue-router）
* 外部库导入（例如：element-plus、axios）
* 内部模块导入（例如：from '../api'、from './components/...'）

## 4. 组件架构
* 脚本设置：实现新组件的语法
* 样式作用域：为组件样式应用 scoped 属性以防止 CSS 泄漏
### 4.1. 组件实现
* 对基本数据类型和单个对象/数组引用应用 ref
* 对需要直接修改的复杂数据结构实现响应式
* 使用 const functionName = () => {} 语法定义函数
### 4.2.生命周期管理
* 直接集成生命周期钩子（onMounted、onUpdated）

# 5. 应用架构与 API 集成
### 5.1. 核心原则
* API 管理：通过专用模块集中管理 API 交互（例如：api.js、api/index.js）
* 异步操作：采用 async/await 模式处理异步任务
* 错误管理：将 API 调用置于 try...catch 块中，并实现用户通知系统

### 5.2. 状态管理
* 为 API 操作实现加载状态跟踪（例如：loading = ref(false)）
* 利用加载状态禁用交互元素，防止重复请求