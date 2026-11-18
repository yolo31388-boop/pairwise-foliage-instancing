# pairwise-foliage-instancing

风吹树林时整片树叶同步抖动、远处消失又弹出：风相位按实例索引但索引不稳定；法线只算顶点法线没算双面；LOD 交叉淡入用 alpha 但阴影没同步；实例包围盒没算风摆幅度；GPU culling 用上一帧风相位；树冠和树干分两个批次；草片在相机近处穿地；地形坡度没参与法线；风场纹理采样用世界坐标导致传送跳变；阴影级联和主视图 LOD 不一致。render/foliage_instancing.py 是核心，tests/test_foliage_instancing.py 15个红。要修的是：稳定风相位；双面法线；阴影淡入同步；风摆包围盒；当前帧剔除；批次合并；地面钳制；坡度法线；局部风场；阴影 LOD 同步。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：图形渲染；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。
