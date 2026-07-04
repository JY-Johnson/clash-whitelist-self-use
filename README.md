# Clash 白名单规则（自用）

这是一套给 `Clash Verge / Mihomo / FlClash` 使用的白名单模式规则仓库。

设计目标：

- 国内站点与明确指定的服务直连
- 其余未命中流量统一交给代理组
- 不在仓库中保存真实节点信息
- 规则来源清晰，便于长期维护

## 项目结构

- `rules/custom-direct.txt`
  - 公开安全版示例直连规则
- `rules/custom-direct.private.txt`
  - 你自己本地维护的私有直连规则，默认不提交
- `dist/whitelist-overlay.yaml`
  - 生成后的 Mihomo 覆写片段
- `example/base-subscription.yaml`
  - 合并脚本示例输入
- `scripts/build_overlay.py`
  - 从自定义规则生成覆写文件
- `scripts/merge_subscription.py`
  - 把白名单逻辑合并到现有订阅
- `scripts/sync_loyalsoldier.ps1`
  - 同步上游规则集
- `THIRD_PARTY.md`
  - 第三方来源说明
- `CHANGELOG.md`
  - 变更记录

## 当前白名单策略

核心思路只有一句话：

1. 自定义直连规则优先
2. Loyalsoldier 白名单规则集命中则直连
3. `GEOIP,LAN` / `GEOIP,CN` 直连
4. 其余流量 `MATCH,代理模式`

默认模式组顺序：

1. `绕过大陆丨白名单(Whitelist)`
2. `绕过大陆丨黑名单(GFWlist)`

## 使用方式

### 1. 仅维护规则

直接编辑：

- `rules/custom-direct.txt`
- 需要私有规则时，额外创建 `rules/custom-direct.private.txt`

然后执行：

```powershell
python .\scripts\build_overlay.py
```

### 2. 合并到现有订阅

```powershell
python .\scripts\merge_subscription.py `
  --base .\example\base-subscription.yaml `
  --output .\dist\subscription-merged.yaml `
  --rules-base-url https://rules.example.com/loyalsoldier
```

### 3. 同步 Loyalsoldier 白名单规则集

```powershell
.\scripts\sync_loyalsoldier.ps1 -OutputDir .\public\rules\loyalsoldier
```

## 还建议补什么

如果后面要继续长期维护，这几个方向最值得继续做：

- 增加一个自动校验工作流，检查生成后的 YAML 是否可被 Mihomo 正常读取
- 把“发布到你自己的 VPS”整理成单独脚本
- 把自定义规则按主题继续拆分，例如：
  - `ai-services`
  - `china-sites`
  - `local-processes`

## 已采用的上游规则集

仅接入适合白名单模式的部分：

- `applications`
- `private`
- `direct`
- `lancidr`
- `cncidr`

未接入：

- `proxy`
- `gfw`
- `google`
- `telegramcidr`
- `tld-not-cn`

原因很简单：这套仓库只服务于白名单模式，不额外维护“强制代理名单”。

## 安全说明

本仓库不包含：

- 实际节点地址
- UUID / 密码 / Reality 公钥
- 真实订阅链接中的敏感字段
- 个人私用域名、内网主机地址、个人服务偏好清单

推荐做法：

- 把真实私有规则放到 `rules/custom-direct.private.txt`
- 把真实规则源地址在本地或 VPS 环境中单独维护
- 公共仓库只保留结构、脚本和公开安全版示例

真实节点配置与最终订阅发布仍应放在你自己的服务器或私有配置中维护。

## 上游致谢

- Loyalsoldier: [clash-rules](https://github.com/Loyalsoldier/clash-rules)

## 许可证与来源说明

- 本仓库中的自编脚本、说明文档与自定义规则整理方式，采用 [MIT License](./LICENSE)。
- 本仓库默认不直接提交上游规则文件内容。
- `scripts/sync_loyalsoldier.ps1` 下载的上游规则文件，仍然遵循其原始项目许可证与发布条款。
- 如果你将下载后的上游规则文件继续分发、镜像或修改，请自行遵循对应上游项目的许可证要求。

更详细的第三方来源说明见：

- [THIRD_PARTY.md](./THIRD_PARTY.md)
