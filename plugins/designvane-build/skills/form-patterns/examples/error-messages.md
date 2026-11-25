# Gold standard — error copy excerpt (Checkout form)

Field: Email
- Empty: "Enter your email address — we send the receipt there."
- Bad format: "That email looks incomplete. Check for an @ and a domain,
  like name@example.com."
- Already registered (signup): "This email already has an account.
  Sign in instead?" (with link, focus moves to it)

Field: Card number
- Incomplete: "Card number needs 16 digits — you've entered 12."
- Declined (server): "Your card was declined. Try a different card, or
  contact your bank. You have not been charged."

Summary pattern: "2 things to fix before you can pay:" + anchor links that
move focus to each field. Errors never say "invalid" alone, never blame
("you failed to..."), and always state whether money moved.
