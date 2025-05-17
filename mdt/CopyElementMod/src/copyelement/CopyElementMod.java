package copyelement;

import copyelement.content.ModBlocks;
import copyelement.content.ModTechTree;
import mindustry.mod.Mod;

public class CopyElementMod extends Mod {
    public static ModBlocks blocks;
    public static ModTechTree techTree;

    @Override
    public void loadContent() {
        blocks = new ModBlocks();
        blocks.load();
        techTree = new ModTechTree();
        techTree.load();
    }
}
