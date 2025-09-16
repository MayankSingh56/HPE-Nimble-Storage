def can_create_snapshot(volume_size_gb, snapshot_size_gb, pool_free_gb=None, allowance_percent=5):
    """
    Naive rules:
      - If snapshot_size <= volume_size -> True
      - If pool_free_gb provided, snapshot should fit into pool_free_gb + small allowance
    Real world: Nimble snapshots are thin and consume space equal to changed data; this function is a conservative safety check.
    """
    if snapshot_size_gb <= volume_size_gb:
        if pool_free_gb is None:
            return True
        # be conservative: require snapshot to fit into pool free + small allowance (eg 5%)
        required = snapshot_size_gb * (1 + allowance_percent/100.0)
        return required <= pool_free_gb
    return False

# examples
print(can_create_snapshot(100, 10))           # True
print(can_create_snapshot(100, 150))          # False
print(can_create_snapshot(100, 90, pool_free_gb=80))  # False (90 > 80)
