def get_heco_acm_metapath_list(
    scheme: str,
) -> list[list[str]]:
    if scheme == 'hop_2':
        return [
            ['PA', 'AP'],
            ['PS', 'SP'],
        ]
    elif scheme == 'hop_0_2':
        return [
            ['paper'],
            ['PA', 'AP'],
            ['PS', 'SP'],
        ]
    elif scheme == 'hop_0_2_4':
        return [
            ['paper'],
            ['PA', 'AP'],
            ['PS', 'SP'],
            ['PA', 'AP', 'PA', 'AP'],
            ['PS', 'SP', 'PS', 'SP'],
        ]
    elif scheme == 'hop_2_4':
        return [
            ['PA', 'AP'],
            ['PS', 'SP'],
            ['PA', 'AP', 'PA', 'AP'],
            ['PS', 'SP', 'PS', 'SP'],
        ]
    else:
        raise ValueError 


def get_heco_dblp_metapath_list(
    scheme: str,
) -> list[list[str]]:
    if scheme == 'hop_2':
        return [
            ['AP', 'PA'],
        ]
    elif scheme == 'hop_0_2':
        return [
            ['author'],
            ['AP', 'PA'],
        ]
    elif scheme == 'hop_2_4':
        return [
            ['AP', 'PA'],
            ['AP', 'PT', 'TP', 'PA'],
            ['AP', 'PC', 'CP', 'PA'],
        ]
    elif scheme == 'hop_0_2_4':
        return [
            ['author'],
            ['AP', 'PA'],
            ['AP', 'PT', 'TP', 'PA'],
            ['AP', 'PC', 'CP', 'PA'],
        ]
    elif scheme == 'hop_2_4_6':
        return [
            ['AP', 'PA'],
            ['AP', 'PT', 'TP', 'PA'],
            ['AP', 'PC', 'CP', 'PA'],
            ['AP', 'PT', 'TP', 'PT', 'TP', 'PA'],
            ['AP', 'PC', 'CP', 'PC', 'CP', 'PA'],
        ]
    else:
        raise ValueError 
    

def get_hin_aminer_metapath_list(
    scheme: str,
) -> list[list[str]]:
    if scheme == 'hop_2':
        return [
            ['PA', 'AP'],
            ['PR', 'RP'],
        ]
    elif scheme == 'hop_0_2':
        return [
            ['paper'],
            ['PA', 'AP'],
            ['PR', 'RP'],
        ]
    elif scheme == 'hop_0_2_4':
        return [
            ['paper'],
            ['PA', 'AP'],
            ['PR', 'RP'],
            ['PA', 'AP', 'PA', 'AP'],
            ['PR', 'RP', 'PR', 'RP'],
        ]
    elif scheme == 'hop_2_4':
        return [
            ['PA', 'AP'],
            ['PR', 'RP'],
            ['PA', 'AP', 'PA', 'AP'],
            ['PR', 'RP', 'PR', 'RP'],
        ]
    else:
        raise ValueError 


def get_imdb_metapath_list(
    scheme: str,
) -> list[list[str]]:
    if scheme == 'hop_2':
        return [
            ['MA', 'AM'],
            ['MD', 'DM'],
        ]
    elif scheme == 'hop_0_2':
        return [
            ['movie'],
            ['MA', 'AM'],
            ['MD', 'DM'],
        ]
    elif scheme == 'hop_0_2_4':
        return [
            ['movie'],
            ['MA', 'AM'],
            ['MD', 'DM'],
            ['MA', 'AM', 'MA', 'AM'],
            ['MD', 'DM', 'MD', 'DM'],
        ]
    elif scheme == 'hop_2_4':
        return [
            ['MA', 'AM'],
            ['MD', 'DM'],
            ['MA', 'AM', 'MA', 'AM'],
            ['MD', 'DM', 'MD', 'DM'],
        ]
    else:
        raise ValueError 


def get_heco_freebase_metapath_list(
    scheme: str,
) -> list[list[str]]:
    if scheme == 'hop_2':
        return [
            ['MA', 'AM'],
            ['MD', 'DM'],
            ['MW', 'WM'],
        ]
    elif scheme == 'hop_0_2':
        return [
            ['movie'],
            ['MA', 'AM'],
            ['MD', 'DM'],
            ['MW', 'WM'],
        ]
    elif scheme == 'hop_0_2_4':
        return [
            ['movie'],
            ['MA', 'AM'],
            ['MD', 'DM'],
            ['MW', 'WM'],
            ['MA', 'AM', 'MA', 'AM'],
            ['MD', 'DM', 'MD', 'DM'],
            ['MW', 'WM', 'MW', 'WM'],
        ]
    elif scheme == 'hop_2_4':
        return [
            ['MA', 'AM'],
            ['MD', 'DM'],
            ['MW', 'WM'],
            ['MA', 'AM', 'MA', 'AM'],
            ['MD', 'DM', 'MD', 'DM'],
            ['MW', 'WM', 'MW', 'WM'],
        ]
    else:
        raise ValueError 


def get_rcdd_subgraph_metapath_list(
    scheme: str,
) -> list[list[str]]:
    if scheme == 'hop_2':
        return [
            ['ib', 'bi'],
            ['if', 'fi'],
        ]
    elif scheme == 'hop_1_2':
        return [
            ['bi'],
            ['fi'],
            ['ib', 'bi'],
            ['if', 'fi'],
        ]
    elif scheme == 'hop_2_4':
        return [
            ['ib', 'bi'],
            ['if', 'fi'],
            ['ib', 'bi', 'ib', 'bi'],
            ['if', 'fi', 'if', 'fi'],
        ]
    elif scheme == 'hop_1_2_4':
        return [
            ['bi'],
            ['fi'],
            ['ib', 'bi'],
            ['if', 'fi'],
            ['ib', 'bi', 'ib', 'bi'],
            ['if', 'fi', 'if', 'fi'],
        ]
    else:
        raise ValueError 
