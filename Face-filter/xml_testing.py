


CommandLineParser parser(argc, argv, keys);
parser.about("Application name v1.0.0");
if (parser.has("help"))
{
    parser.printMessage();
    return 0;
}
int N = parser.get<int>("N");
double fps = parser.get<double>("fps");
String path = parser.get<String>("path");
use_time_stamp = parser.has("timestamp");
String img1 = parser.get<String>(0);
String img2 = parser.get<String>(1);
int repeat = parser.get<int>(2);
if (!parser.check())
{
    parser.printErrors();
    return 0;
}