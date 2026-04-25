# WeChat Skills

微信公众号文章发布技能集，包含5个skill：

- **wechat-api-lite** — 微信公众号API工具（上传图片、创建草稿等）
- **wechat-post** — 总调度（调度四个子skill）
- **wechat-writer** — 正文写作
- **wechat-post-image** — 封面和配图生成
- **wechat-formatter** — HTML排版

## 工作流程

```
Step 1: wechat-writer   → 写正文 → 存档
Step 2: 用户确认文字
Step 3: wechat-post-image → 生成封面/配图 → 上传（调用wechat-api-lite）
Step 4: 用户确认图片
Step 5: wechat-formatter → 构建HTML → 写draft.json
Step 6: 用户确认格式
Step 7: wechat-post → 调用wechat-api-lite发草稿
```
