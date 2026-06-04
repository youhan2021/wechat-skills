---
name: wechat-post
description: 微信公众号文章发布总调度——写正文 → 用户确认文字 → 做图 → 用户确认图片 → 发草稿
triggers:
  - "写公众号"
  - "发微信公众号"
  - "生成公众号文章"
  - "wechat article"
env:
  WECHAT_API_SCRIPT: ~/.hermes/skills/wechat-api-lite/scripts/wechat_api.py
  RESEARCH_DIR: ~/.hermes/research/
  ARTICLE_HISTORY_FILE: ~/.hermes/research/articles_history.json
notes: |
  ===== WORKFLOW (must follow in order) =====
  
  Step 1: wechat-writer → 查相似度 → 写正文 markdown → 存档
  Step 2: 【用户确认文字】→ OK 才继续
  Step 3: wechat-post-image → 生成封面 + 配图 → 上传获取 media_id
  Step 4: 【用户确认图片】→ OK 才继续
  Step 5: wechat-formatter → 构建 HTML → 写入 draft.json
  Step 6: 【格式确认】→ OK 才继续
  Step 6.5: wechat-score → 标题+封面综合打分（流量潜力）→ 必走，发草稿前最后一道闸
  Step 7: 直接调用 wechat API → create-draft

  每步都要等用户确认，禁止跳步
  Step 6.5 必须执行：哪怕分数高，也要输出完整评分报告让用户看一眼；分低则必须回炉改标题或重做封面
---

# 微信公众号文章发布总调度

## 工作流程（7步+Step 6.5，每步等确认）

```
Step 1: wechat-writer
    - 查 articles_history.json 相似度
    - 写正文 markdown → 保存到 ~/.hermes/research/article_*.md
    - 存档到 articles_history.json
    ↓
Step 2: 【文字确认】
    - 把正文 markdown 内容发给用户看
    - 用户确认 OK 才继续
    ↓
Step 3: wechat-post-image
    - 生成封面 + 配图
    - 上传微信，获取 media_id
    ↓
Step 4: 【图片确认】
    - 把封面/配图发给用户看（MEDIA:路径）
    - 用户确认 OK 才继续
    ↓
Step 5: wechat-formatter
    - 读取 article_*.md
    - 用 media_id 构建完整 HTML
    - 写入 draft.json
    ↓
Step 6: 【格式确认】
    - 把 HTML 草稿内容发给用户看（关键段落节选）
    - 用户确认 OK 才继续
    ↓
Step 6.5: wechat-score 【发草稿前必走】
    - 收集：标题 + 封面 + 目标读者（按本文受众推算）
    - 调用 wechat-score 打分（七维 100 分制）
    - 输出完整评分报告给用户
    - 判定：
        · ≥70 分（中高潜力及以上）→ 用户确认后进 Step 7
        · 55-69（中等）→ 提示用户，可发可改
        · <55（偏弱/很弱）→ 强制回炉（改标题 / 重做封面 / 都改）
    - 用户可显式 override（如"我就发 60 分这个"），但必须留痕说"已知分低，按用户要求发"
    ↓
Step 7: 发草稿
    - 直接调用 wechat API: python3 ~/.hermes/skills/wechat-api-lite/scripts/wechat_api.py create-draft ~/.hermes/research/draft.json
    - 返回草稿 media_id 给用户
```

## 重要规则

- **禁止跳过用户确认步骤**
- **禁止在用户确认前进入下一步**
- **draft.json 不得在旧 JSON 上 patch，必须重建**
- **发草稿由 wechat-post 直接调用 API，不转发给用户操作**

## 调用子 skill

- `/wechat-writer` — 写作
- `/wechat-post-image` — 图片
- `/wechat-formatter` — 排版（只做 HTML 构建，不调用 API）
- `/wechat-score` — 标题+封面流量潜力打分（Step 6.5 必走）

## 交付格式

所有步骤完成后，输出：

```
---
草稿 media_id：[media_id]
封面：MEDIA:路径
配图：MEDIA:路径
---
```
