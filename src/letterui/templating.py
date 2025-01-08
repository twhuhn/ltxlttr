#fugly
def generate_letter_template_raw(sender_name, sender_streetaddress, sender_zipcity, sender_phone, sender_phonename, sender_email, business_yourref, business_yourmailfrom, business_myref, business_customernumber, business_invoicenumber, business_place, business_date, recipient_addrfield, content_subject, content_opening, content_text, content_closing, content_ps, content_enclosing, content_cc):
  template = """
\\documentclass[fontsize=12pt, paper=a4, enlargefirstpage=on, pagenumber=headright, headsepline=on, parskip=half, fromalign=right, fromphone=on, fromrule=off, fromfax=off, fromemail=on, fromurl=off, fromlogo=off, addrfield=on, backaddress=on, subject=beforeopening, locfield=narrow, foldmarks=on, numericaldate=off, refline=narrow, draft=off]{scrlttr2}

\\usepackage[ngerman]{babel}
\\usepackage[T1]{fontenc}
\\usepackage[utf8]{inputenc}
\\usepackage{url}

\\usepackage{marvosym}
\\DeclareUnicodeCharacter{20AC}{\\EUR}
\\setkomafont{fromname}{\\sffamily \\LARGE}
\\setkomafont{fromaddress}{\\sffamily}
\\setkomafont{pagenumber}{\\sffamily}
\\setkomafont{subject}{\\bfseries}
\\setkomafont{backaddress}{\\mdseries}
\\usepackage{mathptmx}


\\begin{document}
\\LoadLetterOption{DIN}
\\makeatletter
\\@setplength{firstheadvpos}{20mm}
\\@setplength{firstheadwidth}{\\paperwidth}
\\ifdim \\useplength{toaddrhpos}>\\z@
\\@addtoplength[-2]{firstheadwidth}{\\useplength{toaddrhpos}}
\\else
\\@addtoplength[2]{firstheadwidth}{\\useplength{toaddrhpos}}
\\fi
\\@setplength{foldmarkhpos}{6.5mm}
\\makeatother

\\setkomavar{fromname}{%(sender_name)s}
\\setkomavar{fromaddress}{%(sender_streetaddress)s\\\\%(sender_zipcity)s}
%(fromphone)s
%(phonename)s
\\setkomavar{fromemail}{%(sender_email)s}
\\setkomavar{backaddressseparator}{ -- }
\\setkomavar{signature}{\\vspace*{1.5cm}\\\\%(sender_name)s}
\\makeatother

%(yourref)s
%(yourmail)s
%(myref)s
%(customer)s
%(invoice)s
\\setkomavar{place}{%(business_place)s}
\\setkomavar{date}{%(business_date)s}
%\\setkomavar{placeseparator}{, den }

%\\renewcommand{\\enclname}{Anlagen}
%\\setkomavar{enclseparator}{: }
\\pagestyle{plain}

\\begin{letter}{%(recipient_addrfield)s}\\setkomavar{subject}{%(content_subject)s}
\\opening{%(content_opening)s}%(content_text)s\\closing{%(content_closing)s}

%(ps)s
%(encl)s
%(cc)s

\\end{letter}
\\end{document}
""" % {
          'sender_name': sender_name,
          'sender_streetaddress': sender_streetaddress,
          'sender_zipcity': sender_zipcity,
          'fromphone': f"\\setkomavar{{fromphone}}{{{sender_phone}}}" if sender_phone else "",
          'phonename': f"\\renewcommand{{\\phonename}}{{{sender_phonename}}}" if sender_phonename else "",
          'sender_email': sender_email,
          'yourref': f"\\setkomavar{{yourref}}{{{business_yourref}}}" if business_yourref else "",
          'yourmail': f"\\setkomavar{{yourmail}}{{{business_yourmailfrom}}}" if business_yourmailfrom else "",
          'myref': f"\\setkomavar{{myref}}{{{business_myref}}}" if business_myref else "",
          'customer': f"\\setkomavar{{customer}}{{{business_customernumber}}}" if business_customernumber else "",
          'invoice': f"\\setkomavar{{invoice}}{{{business_invoicenumber}}}" if business_invoicenumber else "",
          'business_place': business_place,
          'business_date': business_date,
          'recipient_addrfield': recipient_addrfield,
          'content_subject': content_subject,
          'content_opening': content_opening,
          'content_text': content_text,
          'content_closing': content_closing,
          'ps': f"\\ps{{{content_ps}}}" if content_ps else "",
          'encl': f"\\encl{{{content_enclosing}}}" if content_enclosing else "",
          'cc': f"\\cc{{{content_cc}}}" if content_cc else ""
      }
  return template

def generate_letter_template(form):
  return generate_letter_template_raw(
      sender_name=form.cleaned_data['sender_name'],
      sender_streetaddress=form.cleaned_data['sender_streetaddress'],
      sender_zipcity=form.cleaned_data['sender_zipcity'],
      sender_phone=form.cleaned_data['sender_phone'],
      sender_phonename=form.cleaned_data['sender_phonename'],
      sender_email=form.cleaned_data['sender_email'],
      business_yourref=form.cleaned_data['business_yourref'],
      business_yourmailfrom=form.cleaned_data['business_yourmailfrom'],
      business_myref=form.cleaned_data['business_myref'],
      business_customernumber=form.cleaned_data['business_customernumber'],
      business_invoicenumber=form.cleaned_data['business_invoicenumber'],
      business_place=form.cleaned_data['business_place'],
      business_date=form.cleaned_data['business_date'],
      recipient_addrfield=form.cleaned_data['recipient_addrfield'],
      content_subject=form.cleaned_data['content_subject'],
      content_opening=form.cleaned_data['content_opening'],
      content_text=form.cleaned_data['content_text'],
      content_closing=form.cleaned_data['content_closing'],
      content_ps=form.cleaned_data['content_ps'],
      content_enclosing=form.cleaned_data['content_enclosing'],
      content_cc=form.cleaned_data['content_cc']
  )