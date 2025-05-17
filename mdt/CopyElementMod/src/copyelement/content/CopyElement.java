package copyelement.content;

import java.util.*;
import mindustry.gen.*;
import mindustry.type.*;
import mindustry.world.*;
import mindustry.world.meta.*;

public class CopyElement extends Block {
    public static final int L = 156;
    public static Building[] qs = new Building[L + 4];
    public static Building[] qt = new Building[L + 4];
    public static int[] qf = new int[L + 4];
    public static Set<Building> bs = new HashSet<>();

    public CopyElement(String name) {
        super(name);
        hasItems = true;
        underBullets = true;
        destructible = true;
        group = BlockGroup.transportation;
        instantTransfer = true;
        unloadable = false;
        canOverdrive = false;
        itemCapacity = 0;
    }

    public class CopyElementBuild extends Building {
        private boolean canOutput(Building src, Building to, Item item, boolean fromInst) {
            return to != null && !(fromInst && to.block.instantTransfer) && to.team == team && to.acceptItem(src, item);
        }

        @Override
        public boolean acceptItem(Building baseSrc, Item item) {
            boolean fromInst = baseSrc.block.instantTransfer;
            int size = 0;
            qs[size] = baseSrc;
            qt[size] = this;
            qf[size++] = relativeToEdge(baseSrc.tile);
            while (size-- > 0) {
                Building src = qs[size];
                Building to = qt[size];
                int from = qf[size];
                if (to instanceof CopyElementBuild copy) {
                    if (bs.contains(copy) || size >= L) continue;
                    bs.add(copy);
                    Building n = copy.nearby((from + 1) & 3);
                    if (n != null) {
                        qs[size] = copy;
                        qt[size] = n;
                        qf[size++] = (from + 3) & 3;
                    }
                    n = copy.nearby((from + 2) & 3);
                    if (n != null) {
                        qs[size] = copy;
                        qt[size] = n;
                        qf[size++] = from;
                    }
                    n = copy.nearby((from + 3) & 3);
                    if (n != null) {
                        qs[size] = copy;
                        qt[size] = n;
                        qf[size++] = (from + 1) & 3;
                    }
                }
                else if (to != baseSrc && canOutput(src, to, item, fromInst)) {
                    bs.clear();
                    return true;
                }
            }
            bs.clear();
            return false;
        }

        @Override
        public void handleItem(Building baseSrc, Item item) {
            boolean fromInst = baseSrc.block.instantTransfer;
            int amount = -1;
            int size = 0;
            qs[size] = baseSrc;
            qt[size] = this;
            qf[size++] = relativeToEdge(baseSrc.tile);
            while (size-- > 0) {
                Building src = qs[size];
                Building to = qt[size];
                int from = qf[size];
                if (to instanceof CopyElementBuild copy) {
                    if (bs.contains(copy) || size >= L) continue;
                    bs.add(copy);
                    Building n = copy.nearby((from + 1) & 3);
                    if (n != null) {
                        qs[size] = copy;
                        qt[size] = n;
                        qf[size++] = (from + 3) & 3;
                    }
                    n = copy.nearby((from + 2) & 3);
                    if (n != null) {
                        qs[size] = copy;
                        qt[size] = n;
                        qf[size++] = from;
                    }
                    n = copy.nearby((from + 3) & 3);
                    if (n != null) {
                        qs[size] = copy;
                        qt[size] = n;
                        qf[size++] = (from + 1) & 3;
                    }
                }
                else if (to != baseSrc && canOutput(src, to, item, fromInst)) {
                    to.handleItem(src, item);
                    amount++;
                }
            }
            if (amount > 0) produced(item, amount);
            bs.clear();
        }

        @Override
        public byte version() {
            return 1;
        }
    }
}
