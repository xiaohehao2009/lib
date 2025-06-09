package supercheat;

import supercheat.content.ModBlocks;
import supercheat.content.ModTechTree;
import mindustry.mod.Mod;
import mindustry.Vars;
import mindustry.world.blocks.storage.CoreBlock;

public class SuperCheatMod extends Mod {
    public static ModBlocks blocks;
    public static ModTechTree techTree;

    @Override
    public void loadContent() {
        Vars.content.each(content -> {
            if (content instanceof CoreBlock core) {
                core.unitType.buildSpeed *= 50f;
                core.unitType.health *= 20f;
                core.unitType.mineSpeed *= 50f;
                core.unitType.mineTier = 50;
                core.unitType.rotateSpeed *= 1.6f;
                core.unitType.speed *= 1.6f;
                core.unitType.weapons.each(weapon -> {
                    weapon.reload *= 0.4f;
                    weapon.bullet.buildingDamageMultiplier = 1f;
                    weapon.bullet.damage *= 200f;
                    weapon.bullet.homingPower = 0.2f;
                    weapon.bullet.speed *= 2f;
                });
            }
        });

        blocks = new ModBlocks();
        blocks.load();
        techTree = new ModTechTree();
        techTree.load();
    }
}
