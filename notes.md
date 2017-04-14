Velkommen
Dette er en introduksjon til sikkerhet i webapplikasjoner
Jeg heter Martin Ingesen,
jobber som sikkerhetskonsulent i Syscom AS i Oslo

- OWASP Top 10

Hva er OWASP top 10?

### DEMOS

[X] A1 Injection

[X] A2 Broken Authentication and Session Management

[ ] A3 Cross-Site Scripting (XSS)
Stored XSS. 2 brukere, gjestebok. Stjele session.

[ ] A4 Insecure Direct Object References
Ett API som henter ut brukerinfo. Feks matvarer? :P
/api/user/11

[ ] A7 Missing Function Level Access Control
admin har tilgang til en "change page background" funksjon som endrer bakgrunnsfargen. Via adminpanelet. Ved å accesse samme funksjon (til tross for at den ikke er tilstede i GUI, kan hvem som helst endre den)

[ ] A8 Cross-Site Request Forgery (CSRF)
"Make admin" funksjonalitet? User lurer admin (som er innlogget) til å gjøre user til admin.
