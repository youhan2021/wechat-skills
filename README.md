# WeChat Skills

微信公众号文章发布技能集，包含6个skill：

- **wechat-api-lite** — 微信公众号API工具（上传图片、创建草稿等）
- **wechat-post** — 总调度（调度五个子skill）
- **wechat-writer** — 正文写作
- **wechat-writer-outline** — 大纲设计（写正文前先确认结构）
- **wechat-post-image** — 封面和配图生成
- **wechat-formatter** — HTML排版
- **wechat-score** — 标题+封面流量潜力打分（七维100分制，输出3个新标题+1个封面方向）

## 工作流程

```
Step 0: wechat-writer-outline → 设计大纲 → 用户确认
Step 1: wechat-writer   → 写正文 → 存档
Step 2: 用户确认文字
Step 2.5: wechat-score → 给标题打分 → 必要时改标题
Step 3: wechat-post-image → 生成封面/配图 → 上传（调用wechat-api-lite）
Step 4: 用户确认图片
Step 4.5: wechat-score → 终评（标题+封面一起）→ 必要时回炉
Step 5: wechat-formatter → 构建HTML → 写draft.json
Step 6: 用户确认格式
Step 7: wechat-post → 调用wechat-api-lite发草稿
```

## wechat-score 何时用

- 写完正文、准备做封面之前：先打标题的分
- 封面做完、准备发布之前：终评标题+封面
- 历史文章复盘：找出哪些标题好哪些差
