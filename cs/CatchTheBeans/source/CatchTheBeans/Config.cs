using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CatchTheBeans
{
    internal class Config
    {
        public const int WindowWidth = 80;
        public const int WindowHeight = 42;
        public static readonly int[] BeanSpeeds =
        {
            14, 10, 6
        };
        public static int SelectedSpeed = 2;
        public static int BeanSpeed = BeanSpeeds[SelectedSpeed];
        public const int ScoreWin = 5;
        public const int ScoreLose = 10;
        public const int PlayerWidth = 3;
        public const char PlayerChar = '#';
        public const char LineChar = '=';
        public const char BeanChar = '#';
    }
}
