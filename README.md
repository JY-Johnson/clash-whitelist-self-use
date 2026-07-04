# Clash 白名单规则（自用）

这是一套给 `Clash Verge / Mihomo / FlClash` 使用的白名单模式规则仓库。

设计目标：

- 国内站点与明确指定的服务直连
- 其余未命中流量统一交给代理组
- 不在仓库中保存真实节点信息
- 规则来源清晰，便于长期维护

## 仓库内容

- `rules/custom-direct.txt`
  - 自定义直连规则，按业务分组维护
- `dist/whitelist-overlay.yaml`
  - 可直接参考的 Mihomo 覆写片段
- `scripts/build_overlay.py`
  - 根据 `custom-direct.txt` 生成覆写片段
- `scripts/merge_subscription.py`
  - 将白名单规则合并进现有订阅 YAML
- `scripts/sync_loyalsoldier.ps1`
  - 下载 Loyalsoldier 白名单模式所需规则集

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

然后执行：

```powershell
python .\scripts\build_overlay.py
```

### 2. 合并到现有订阅

```powershell
python .\scripts\merge_subscription.py `
  --base .\example\base-subscription.yaml `
  --output .\dist\subscription-merged.yaml `
  --rules-base-url https://083105.xyz/rules/loyalsoldier
```

### 3. 同步 Loyalsoldier 白名单规则集

```powershell
.\scripts\sync_loyalsoldier.ps1 -OutputDir .\public\rules\loyalsoldier
```

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

真实节点配置与最终订阅发布仍应放在你自己的服务器或私有配置中维护。

## 上游致谢

- Loyalsoldier: [clash-rules](https://github.com/Loyalsoldier/clash-rules)
