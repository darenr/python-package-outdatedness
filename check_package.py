from johnnydep.lib import JohnnyDist

def check_package(pkg):
    dist = JohnnyDist(pkg)
    summary = {
        'versions_available': dist.versions_available,
        'version_installed': dist.version_installed,
        'version_latest': dist.version_latest,
        'pinned': dist.pinned
    }
    if dist.version_installed in  dist.versions_available:
        summary['versions_behind'] = len(dist.versions_available) - dist.versions_available.index(dist.version_installed)

    return summary

if __name__ == '__main__':
    summary = check_package('pandas')
    print(summary)
