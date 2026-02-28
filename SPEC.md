# Always-love - 技术规格文档

## 1. 项目概述

**项目名称**: Always-love
**项目类型**: 全栈 Web 应用
**核心功能**: 用户可登录注册、选择兴趣分区、搜索角色周边、比价购物
**目标用户**: 动漫/游戏/明星/虚拟主播爱好者

## 1. 项目概述

**项目名称**: 角色周边星球 (CharacterHub)
**项目类型**: 全栈 Web 应用
**核心功能**: 用户可登录注册、选择兴趣分区、搜索角色周边、比价购物
**目标用户**: 动漫/游戏/明星/虚拟主播爱好者

---

## 2. 技术架构

### 2.1 技术栈

| 层级 | 技术选型 |
|------|----------|
| 前端 | React 18 + TypeScript + Vite |
| 后端 | Node.js + Express + TypeScript |
| 数据库 | SQLite (better-sqlite3) |
| 认证 | JWT + bcrypt |
| 爬虫 | Playwright (淘宝/闲鱼) |
| 样式 | CSS Modules + CSS Variables |

### 2.2 项目结构

```
always-love/
├── client/                 # 前端
│   ├── src/
│   │   ├── components/     # 组件
│   │   ├── pages/         # 页面
│   │   ├── hooks/         # 自定义 Hooks
│   │   ├── services/      # API 服务
│   │   ├── styles/        # 样式
│   │   └── types/         # TypeScript 类型
│   └── index.html
├── server/                 # 后端
│   ├── src/
│   │   ├── routes/        # 路由
│   │   ├── controllers/   # 控制器
│   │   ├── models/        # 数据模型
│   │   ├── middleware/    # 中间件
│   │   ├── services/       # 业务逻辑
│   │   └── scrapers/      # 爬虫
│   └── package.json
└── package.json           # 根配置
```

---

## 3. 数据库设计

### 3.1 用户表 (users)

| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER PRIMARY KEY | 用户ID |
| username | TEXT UNIQUE | 用户名 |
| email | TEXT UNIQUE | 邮箱 |
| password_hash | TEXT | 密码哈希 |
| created_at | DATETIME | 注册时间 |

### 3.2 分区表 (partitions)

| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER PRIMARY KEY | 分区ID |
| name | TEXT | 分区名称 |
| slug | TEXT UNIQUE | 分区标识 |
| icon | TEXT | 图标 |

### 3.3 用户分区关联表 (user_partitions)

| 字段 | 类型 | 说明 |
|------|------|------|
| user_id | INTEGER | 用户ID |
| partition_id | INTEGER | 分区ID |

### 3.4 角色表 (characters)

| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER PRIMARY KEY | 角色ID |
| name | TEXT | 角色名称 |
| partition_id | INTEGER | 所属分区 |
| image_url | TEXT | 角色图片 |
| description | TEXT | 描述 |

### 3.5 周边商品表 (products)

| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER PRIMARY KEY | 商品ID |
| character_id | INTEGER | 角色ID |
| title | TEXT | 商品标题 |
| type | TEXT | 周边类型 |
| price | REAL | 价格 |
| platform | TEXT | 平台 |
| url | TEXT | 商品链接 |
| image_url | TEXT | 商品图片 |
| scraped_at | DATETIME | 抓取时间 |

---

## 4. API 设计

### 4.1 认证接口

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | /api/auth/register | 用户注册 |
| POST | /api/auth/login | 用户登录 |
| GET | /api/auth/me | 获取当前用户 |

### 4.2 分区接口

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/partitions | 获取所有分区 |

### 4.3 用户偏好接口

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/user/partitions | 获取用户选择的分区 |
| PUT | /api/user/partitions | 更新用户分区选择 |

### 4.4 角色接口

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/characters | 获取角色列表（支持分区筛选） |
| GET | /api/characters/:id | 获取角色详情 |

### 4.5 商品接口

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/products | 搜索商品（支持角色/类型筛选） |
| GET | /api/products/compare | 价格对比 |

### 4.6 爬虫接口

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | /api/scrape/search | 触发关键词搜索爬取 |
| POST | /api/scrape/character | 爬取角色全周边 |

---

## 5. 功能模块

### 5.1 用户模块
- 邮箱/密码注册
- 登录返回 JWT Token
- 选择感兴趣的分區（多选）

### 5.2 分区模块
- 四大分区：动漫、游戏、明星偶像、虚拟主播
- 分区图标展示

### 5.3 首页推荐
- 根据用户选择的分区推流
- 热门角色展示
- 最新商品展示

### 5.4 搜索筛选
- 关键词搜索角色
- 筛选条件：分区、周边类型（徽章、海报、手办、抱枕等）
- 排序：价格、热度、时间

### 5.5 价格对比
- 同一商品多平台价格对比
- 均价计算
- 历史价格走势（可选）

---

## 6. 爬虫设计

### 6.1 淘宝爬虫
- 使用 Playwright 模拟浏览器
- 处理登录态（可选）
- 反爬策略：随机延时、代理轮换

### 6.2 闲鱼爬虫
- 闲鱼 API 接口调用
- 关键词搜索
- 详情页抓取

### 6.3 数据清洗
- 价格统一化为人民币
- 商品类型分类
- 去重处理

---

## 7. 前端页面

### 7.1 页面列表

| 页面 | 路由 | 说明 |
|------|------|------|
| 首页 | / | 个性化推荐流 |
| 登录 | /login | 登录页面 |
| 注册 | /register | 注册页面 |
| 分区选择 | /onboarding | 首次选择分区 |
| 搜索结果 | /search | 搜索+筛选 |
| 角色详情 | /character/:id | 角色及周边 |
| 商品详情 | /product/:id | 商品详情+比价 |

### 7.2 UI 设计

- 主题：深色模式为主
- 配色：
  - 主色：#6366f1 (靛蓝)
  - 背景：#0f172a (深蓝黑)
  - 卡片：#1e293b (深灰蓝)
  - 文字：#f8fafc (浅白)
- 布局：响应式 Grid + Flex

---

## 8. 验收标准

1. ✅ 用户可以注册、登录
2. ✅ 用户可以选择多个分区
3. ✅ 首页显示基于分区的推荐
4. ✅ 可以搜索角色并筛选周边类型
5. ✅ 可以获取淘宝/闲鱼的商品数据
6. ✅ 实现了价格对比功能
7. ✅ 项目可以正常启动运行
